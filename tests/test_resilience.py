"""Failure handling: Claude outages, Slack rate limits, bad model output."""

from __future__ import annotations

import pytest

from zam_agent.confidence import Action
from zam_agent.llm.base import LLMError, LLMInvalidOutput, LLMRateLimited, LLMRefusal, LLMTimeout
from zam_agent.llm.fake import FakeLLM
from zam_agent.slackbot.retry import SlackCallFailed, call_with_retry
from zam_agent.store.sqlite_store import SQLiteStore

from .fakes import FakeSlackClient, slack_envelope, slack_error, slack_message_event
from .helpers import (
    TODAY,
    answer_payload,
    build_pipeline,
    classification,
    first_label,
    grade_payload,
    message,
)
from .test_slack_events import build_agent

QUESTION = "How long does ZAM app review take?"


# ------------------------------------------------------------- Claude failures


@pytest.mark.parametrize("error", [LLMTimeout("timed out"), LLMRateLimited("429")])
def test_a_transient_claude_failure_posts_nothing_and_asks_slack_to_retry(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore, error: Exception
) -> None:
    client = FakeSlackClient()
    agent = build_agent(config, fixture_knowledge, llm, store, client)
    llm.fail("classify", error)

    event = slack_message_event(QUESTION)
    decision = agent.process_event(slack_envelope(event), event)

    assert decision is not None
    assert decision.action is Action.IGNORE
    assert decision.retryable_error is True
    assert client.posted == [], "a transient outage must not produce a confusing reply"
    # The claim is released, so Slack's retry can succeed.
    assert store.was_processed("evt:Ev0TEST0001") is False


def test_a_released_event_is_answered_on_the_retry(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    client = FakeSlackClient()
    agent = build_agent(config, fixture_knowledge, llm, store, client)
    llm.fail("classify", LLMTimeout("timed out"))

    event = slack_message_event(QUESTION)
    agent.process_event(slack_envelope(event), event)

    # Claude recovers; Slack redelivers the same event.
    llm.failures.clear()
    label = first_label(fixture_knowledge, QUESTION, "zam")
    llm.script("classify", classification(category="zam_question", search_query=QUESTION))
    llm.script("answer", answer_payload(answer="App review takes 4 business days.", source_ids=[label]))
    llm.script("grade", grade_payload(verdicts=["supported"]))

    decision = agent.process_event(slack_envelope(event, retry_num=1), event)

    assert decision is not None and decision.action is Action.ANSWER
    assert len(client.posted) == 1


def test_a_permanent_classification_failure_stays_silent(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    pipeline = build_pipeline(config, fixture_knowledge, llm, store)
    llm.fail("classify", LLMInvalidOutput("not json"))

    decision = pipeline.handle(message(QUESTION), today=TODAY)

    assert decision.action is Action.IGNORE
    assert decision.skip_reason == "classification_failed"
    assert decision.retryable_error is False


def test_an_answer_timeout_releases_the_event_rather_than_escalating(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    client = FakeSlackClient()
    agent = build_agent(config, fixture_knowledge, llm, store, client)
    llm.script("classify", classification(category="zam_question", search_query=QUESTION))
    llm.fail("answer", LLMTimeout("timed out"))

    event = slack_message_event(QUESTION)
    decision = agent.process_event(slack_envelope(event), event)

    assert decision is not None and decision.retryable_error is True
    assert client.posted == []


def test_a_model_refusal_escalates_instead_of_going_silent(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    pipeline = build_pipeline(config, fixture_knowledge, llm, store)
    llm.script("classify", classification(category="zam_question", search_query=QUESTION))
    llm.fail("answer", LLMRefusal(category="cyber"))

    decision = pipeline.handle(message(QUESTION), today=TODAY)

    assert decision.action is Action.ESCALATE
    assert decision.tagged_owner is True


def test_malformed_answer_output_escalates(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    pipeline = build_pipeline(config, fixture_knowledge, llm, store)
    llm.script("classify", classification(category="zam_question", search_query=QUESTION))
    llm.fail("answer", LLMInvalidOutput("model returned prose"))

    decision = pipeline.handle(message(QUESTION), today=TODAY)

    assert decision.action is Action.ESCALATE


def test_a_grader_failure_escalates_rather_than_trusting_the_draft(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    pipeline = build_pipeline(config, fixture_knowledge, llm, store)
    label = first_label(fixture_knowledge, QUESTION, "zam")
    llm.script("classify", classification(category="zam_question", search_query=QUESTION))
    llm.script("answer", answer_payload(answer="App review takes 4 business days.", source_ids=[label]))
    llm.fail("grade", LLMError("grader unavailable"))

    decision = pipeline.handle(message(QUESTION), today=TODAY)

    assert decision.action is Action.ESCALATE
    assert any("verification did not run" in r for r in decision.verdict.hard_failures)


def test_an_empty_generated_answer_escalates(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    pipeline = build_pipeline(config, fixture_knowledge, llm, store)
    label = first_label(fixture_knowledge, QUESTION, "zam")
    llm.script("classify", classification(category="zam_question", search_query=QUESTION))
    llm.script("answer", answer_payload(answer="   ", source_ids=[label]))
    llm.script("grade", grade_payload(verdicts=["supported"]))

    decision = pipeline.handle(message(QUESTION), today=TODAY)

    assert decision.action is Action.ESCALATE


# ------------------------------------------------------------- Slack failures


def test_rate_limited_calls_honour_retry_after() -> None:
    slept: list[float] = []
    attempts = {"n": 0}

    def flaky() -> str:
        attempts["n"] += 1
        if attempts["n"] < 3:
            raise slack_error("ratelimited", status_code=429, retry_after="2")
        return "ok"

    result = call_with_retry(flaky, operation="chat.postMessage", sleep=slept.append)

    assert result == "ok"
    assert slept == [2.0, 2.0]


def test_server_errors_are_retried_with_backoff() -> None:
    slept: list[float] = []
    attempts = {"n": 0}

    def flaky() -> str:
        attempts["n"] += 1
        if attempts["n"] < 2:
            raise slack_error("internal_error", status_code=500)
        return "ok"

    assert call_with_retry(flaky, operation="chat.postMessage", sleep=slept.append) == "ok"
    assert len(slept) == 1


def test_fatal_slack_errors_are_not_retried() -> None:
    attempts = {"n": 0}

    def always_fatal() -> str:
        attempts["n"] += 1
        raise slack_error("missing_scope")

    with pytest.raises(SlackCallFailed) as excinfo:
        call_with_retry(always_fatal, operation="chat.postMessage", sleep=lambda _: None)

    assert excinfo.value.fatal is True
    assert attempts["n"] == 1


def test_retries_are_eventually_given_up() -> None:
    def always_rate_limited() -> str:
        raise slack_error("ratelimited", status_code=429, retry_after="1")

    with pytest.raises(SlackCallFailed) as excinfo:
        call_with_retry(
            always_rate_limited, operation="chat.postMessage", max_attempts=3, sleep=lambda _: None
        )

    assert excinfo.value.fatal is False
    assert excinfo.value.error == "ratelimited"


def test_a_failed_post_does_not_crash_the_worker(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    client = FakeSlackClient()
    for _ in range(6):
        client.fail_once("chat_postMessage", slack_error("ratelimited", status_code=429, retry_after="1"))
    agent = build_agent(config, fixture_knowledge, llm, store, client)
    label = first_label(fixture_knowledge, QUESTION, "zam")
    llm.script("classify", classification(category="zam_question", search_query=QUESTION))
    llm.script("answer", answer_payload(answer="App review takes 4 business days.", source_ids=[label]))
    llm.script("grade", grade_payload(verdicts=["supported"]))

    event = slack_message_event(QUESTION)
    decision = agent.process_event(slack_envelope(event), event)

    assert decision is not None and decision.action is Action.ANSWER
    assert client.posted == []


def test_a_crash_inside_the_pipeline_releases_the_event(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    client = FakeSlackClient()
    agent = build_agent(config, fixture_knowledge, llm, store, client)

    class Boom(RuntimeError):
        pass

    def explode(*_args, **_kwargs):
        raise Boom("unexpected")

    agent.pipeline.handle = explode  # type: ignore[method-assign]

    event = slack_message_event(QUESTION)
    with pytest.raises(Boom):
        agent.process_event(slack_envelope(event), event)

    assert store.was_processed("evt:Ev0TEST0001") is False


def test_the_worker_wrapper_swallows_unexpected_errors(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    agent = build_agent(config, fixture_knowledge, llm, store)

    def explode(*_args, **_kwargs):
        raise RuntimeError("unexpected")

    agent.process_event = explode  # type: ignore[method-assign]
    event = slack_message_event(QUESTION)

    agent._guarded_process(slack_envelope(event), event)  # must not raise
