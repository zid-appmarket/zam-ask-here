"""Follow-up questions inside a thread."""

from __future__ import annotations

from zam_agent.confidence import Action
from zam_agent.llm.fake import FakeLLM
from zam_agent.slackbot.thread_context import fetch_thread_context, render_thread
from zam_agent.store.sqlite_store import SQLiteStore

from .fakes import FakeSlackClient, slack_envelope, slack_message_event
from .helpers import (
    BOT_USER,
    CHANNEL,
    EMPLOYEE,
    TODAY,
    answer_payload,
    build_pipeline,
    classification,
    first_label,
    grade_payload,
    message,
)
from .test_slack_events import build_agent

THREAD_TS = "1762790400.000100"


def _thread_messages() -> list[dict[str, object]]:
    return [
        slack_message_event(
            "What are the Theme Market pricing tiers?", ts=THREAD_TS, thread_ts=THREAD_TS
        ),
        {
            "type": "message",
            "subtype": "bot_message",
            "bot_id": "B0FAKEBOT1",
            "user": BOT_USER,
            "text": "Theme Market has three tiers: Basic, Plus and Premium.",
            "ts": "1762790460.000200",
            "thread_ts": THREAD_TS,
        },
        slack_message_event(
            "وللقوالب المدفوعة؟", ts="1762790520.000300", thread_ts=THREAD_TS, client_msg_id=None
        ),
    ]


def test_render_thread_excludes_the_current_message_and_labels_speakers() -> None:
    context = render_thread(
        _thread_messages(), current_ts="1762790520.000300", bot_user_id=BOT_USER, limit=12
    )

    assert context.message_count == 2
    assert context.bot_participated is True
    assert "[agent]" in context.rendered
    assert f"[employee:{EMPLOYEE}]" in context.rendered
    assert "وللقوالب المدفوعة" not in context.rendered


def test_thread_context_strips_mentions_from_history() -> None:
    messages = [
        slack_message_event("ping <!channel> <@U0SOMEONE1> about pricing", ts="1.000100", thread_ts="1.000100"),
        slack_message_event("and now?", ts="2.000200", thread_ts="1.000100", client_msg_id=None),
    ]
    context = render_thread(messages, current_ts="2.000200", bot_user_id=BOT_USER)

    assert "<!channel>" not in context.rendered
    assert "<@U0SOMEONE1>" not in context.rendered


def test_fetch_thread_context_survives_a_slack_failure() -> None:
    from .fakes import slack_error

    client = FakeSlackClient(thread_messages=_thread_messages())
    for _ in range(5):
        client.fail_once("conversations_replies", slack_error("channel_not_found"))

    context = fetch_thread_context(
        client,
        channel_id=CHANNEL,
        thread_ts=THREAD_TS,
        current_ts="1762790520.000300",
        bot_user_id=BOT_USER,
    )

    assert context.rendered == ""
    assert context.bot_participated is False


def test_the_classifier_receives_the_thread_and_rewrites_the_query(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    client = FakeSlackClient(thread_messages=_thread_messages())
    agent = build_agent(config, fixture_knowledge, llm, store, client)
    query = "سياسة الاسترجاع للقوالب المدفوعة"
    label = first_label(fixture_knowledge, "سياسة الاسترجاع للقوالب", "theme_market")
    llm.script(
        "classify",
        classification(
            category="thread_follow_up", products=["theme_market"], search_query=query, topic="theme refunds"
        ),
    )
    llm.script(
        "answer",
        answer_payload(answer="الاسترجاع متاح خلال 7 أيام من الشراء.", source_ids=[label]),
    )
    llm.script("grade", grade_payload(verdicts=["supported"]))

    follow_up = slack_message_event(
        "وللقوالب المدفوعة؟", ts="1762790520.000300", thread_ts=THREAD_TS, client_msg_id=None
    )
    decision = agent.process_event(slack_envelope(follow_up, event_id="Ev0FOLLOW"), follow_up)

    classify_call = next(call for call in llm.calls if call["purpose"] == "classify")
    content = classify_call["messages"][0]["content"]
    assert "<thread_context>" in content
    assert "pricing tiers" in content
    assert "in_existing_thread=true" in content

    assert decision is not None and decision.action is Action.ANSWER
    assert decision.category == "thread_follow_up"
    # The retrieval query is the rewritten standalone question, not the ellipsis.
    answer_call = next(call for call in llm.calls if call["purpose"] == "answer")
    assert "<thread_context>" in answer_call["messages"][0]["content"]
    assert client.posted[0]["thread_ts"] == THREAD_TS


def test_a_follow_up_in_a_bot_thread_is_handled_even_without_question_marks(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    pipeline = build_pipeline(config, fixture_knowledge, llm, store)
    query = "theme refund window for paid themes"
    label = first_label(fixture_knowledge, "سياسة الاسترجاع للقوالب", "theme_market")
    llm.script(
        "classify",
        classification(
            category="thread_follow_up",
            products=["theme_market"],
            is_question=False,
            search_query=query,
        ),
    )
    llm.script("answer", answer_payload(answer="Refunds are available within 7 days.", source_ids=[label]))
    llm.script("grade", grade_payload(verdicts=["supported"]))

    decision = pipeline.handle(
        message(
            "same for paid ones",
            ts="1762790520.000300",
            thread_ts=THREAD_TS,
            thread_context="[employee:U1] What are the Theme Market pricing tiers?",
            bot_in_thread=True,
        ),
        today=TODAY,
    )

    assert decision.action is Action.ANSWER


def test_a_follow_up_in_a_thread_the_bot_never_joined_is_not_forced(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    pipeline = build_pipeline(config, fixture_knowledge, llm, store)
    llm.script(
        "classify",
        classification(category="thread_follow_up", products=["zam"], is_question=False, search_query="x"),
    )

    decision = pipeline.handle(
        message(
            "same for the app one",
            ts="1762790520.000300",
            thread_ts=THREAD_TS,
            thread_context="[employee:U1] we should change the ZAM listing copy",
            bot_in_thread=False,
        ),
        today=TODAY,
    )

    assert decision.action is Action.IGNORE
    assert decision.skip_reason == "not_a_question"
