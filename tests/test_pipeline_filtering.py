"""Messages the agent must leave alone."""

from __future__ import annotations

import pytest

from zam_agent.confidence import Action
from zam_agent.llm.fake import FakeLLM
from zam_agent.store.sqlite_store import SQLiteStore

from .helpers import (
    TODAY,
    answer_payload,
    build_pipeline,
    classification,
    first_label,
    grade_payload,
    make_config,
    message,
)


@pytest.mark.parametrize(
    "text",
    [
        "thanks!",
        "شكراً",
        "يعطيك العافية",
        "تمام",
        "+1",
        "   ",
    ],
)
def test_acknowledgements_never_get_a_reply(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore, text: str
) -> None:
    pipeline = build_pipeline(config, fixture_knowledge, llm, store)

    decision = pipeline.handle(message(text), today=TODAY)

    assert decision.action is Action.IGNORE
    assert decision.text == ""
    assert llm.calls == [], "an acknowledgement must not cost an LLM call"


@pytest.mark.parametrize(
    "text",
    [
        "Standup moved to 11:00 tomorrow",
        "I'll be out this afternoon",
        "اجتماع الفريق اتأجل لبكرة",
    ],
)
def test_chatter_with_no_product_signal_is_filtered_before_any_llm_call(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore, text: str
) -> None:
    pipeline = build_pipeline(config, fixture_knowledge, llm, store)

    decision = pipeline.handle(message(text), today=TODAY)

    assert decision.action is Action.IGNORE
    assert decision.skip_reason == "no_question_or_product_signal"
    assert llm.calls == []


def test_the_prefilter_can_be_disabled_so_everything_is_classified(
    fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    config = make_config(slack={"prefilter_enabled": False})
    pipeline = build_pipeline(config, fixture_knowledge, llm, store)
    llm.script("classify", classification(category="unrelated_conversation", products=[], is_question=False))

    decision = pipeline.handle(message("Standup moved to 11:00 tomorrow"), today=TODAY)

    assert decision.action is Action.IGNORE
    assert decision.skip_reason == "classified_unrelated"
    assert llm.call_counts["classify"] == 1


def test_a_message_classified_as_unrelated_is_ignored(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    pipeline = build_pipeline(config, fixture_knowledge, llm, store)
    llm.script("classify", classification(category="unrelated_conversation", products=[], is_question=False))

    decision = pipeline.handle(message("Anyone up for lunch? The app store downstairs is nice"), today=TODAY)

    assert decision.action is Action.IGNORE
    assert decision.skip_reason == "classified_unrelated"
    assert llm.call_counts["answer"] == 0


def test_unrelated_messages_can_be_answered_when_explicitly_configured(
    fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    config = make_config(slack={"respond_to_unrelated": True})
    pipeline = build_pipeline(config, fixture_knowledge, llm, store)
    query = "How long does ZAM app review take?"
    label = first_label(fixture_knowledge, query, "zam")
    llm.script(
        "classify",
        classification(category="unrelated_conversation", products=["zam"], search_query=query),
    )
    llm.script("answer", answer_payload(answer="Review takes 4 business days.", source_ids=[label]))
    llm.script("grade", grade_payload(verdicts=["supported"]))

    decision = pipeline.handle(message(query), today=TODAY)

    assert decision.action is Action.ANSWER


def test_a_statement_that_asks_nothing_is_ignored(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    pipeline = build_pipeline(config, fixture_knowledge, llm, store)
    llm.script(
        "classify",
        classification(category="zam_question", products=["zam"], is_question=False, search_query="theme app"),
    )

    decision = pipeline.handle(message("We shipped the new ZAM app listing page today"), today=TODAY)

    assert decision.action is Action.IGNORE
    assert decision.skip_reason == "not_a_question"


def test_general_question_with_no_source_stays_quiet_by_default(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    pipeline = build_pipeline(config, fixture_knowledge, llm, store)
    llm.script(
        "classify",
        classification(
            category="general_company_question",
            products=[],
            search_query="what is the parking permit renewal process",
        ),
    )

    decision = pipeline.handle(message("How do I renew my parking permit?"), today=TODAY)

    assert decision.action is Action.IGNORE
    assert decision.skip_reason == "general_question_no_sources"
    assert llm.call_counts["answer"] == 0


def test_general_questions_can_be_disabled_entirely(
    fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    config = make_config(slack={"answer_general_questions": False})
    pipeline = build_pipeline(config, fixture_knowledge, llm, store)
    llm.script(
        "classify",
        classification(
            category="general_company_question", products=[], search_query="partner support hours"
        ),
    )

    decision = pipeline.handle(message("When is partner support available?"), today=TODAY)

    assert decision.action is Action.IGNORE
    assert decision.skip_reason == "general_questions_disabled"


def test_a_directly_addressed_message_bypasses_the_prefilter(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    pipeline = build_pipeline(config, fixture_knowledge, llm, store)
    llm.script("classify", classification(category="unrelated_conversation", products=[], is_question=False))

    decision = pipeline.handle(message("hello there", directly_addressed=True), today=TODAY)

    assert llm.call_counts["classify"] == 1
    assert decision.skip_reason == "classified_unrelated"
