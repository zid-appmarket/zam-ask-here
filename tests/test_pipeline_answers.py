"""End-to-end: verified questions in English, Arabic and Saudi dialect."""

from __future__ import annotations

import pytest

from zam_agent.confidence import Action
from zam_agent.knowledge.ingest import KnowledgeBase
from zam_agent.llm.fake import FakeLLM
from zam_agent.store.sqlite_store import SQLiteStore

from .helpers import (
    OWNER_ZAM,
    TODAY,
    answer_payload,
    build_pipeline,
    classification,
    first_label,
    grade_payload,
    make_config,
    message,
)


def _script(
    llm: FakeLLM,
    knowledge: KnowledgeBase,
    *,
    category: str,
    product: str | None,
    query: str,
    answer: str,
) -> str:
    label = first_label(knowledge, query, product)
    llm.script("classify", classification(category=category, products=[product] if product else [], search_query=query))
    llm.script("answer", answer_payload(answer=answer, source_ids=[label]))
    llm.script("grade", grade_payload(verdicts=["supported"]))
    return label


def test_verified_zam_question_in_english_is_answered(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    pipeline = build_pipeline(config, fixture_knowledge, llm, store)
    label = _script(
        llm,
        fixture_knowledge,
        category="zam_question",
        product="zam",
        query="How long does ZAM app review take?",
        answer="App review takes 4 business days from submission.",
    )

    decision = pipeline.handle(
        message("How long does ZAM app review take?"), today=TODAY
    )

    assert decision.action is Action.ANSWER
    assert decision.confidence_level == "high"
    assert "4 business days" in decision.text
    assert decision.language == "en"
    assert decision.product == "zam"
    assert decision.tagged_owner is False
    assert OWNER_ZAM not in decision.text, "a verified answer must not tag anyone"
    assert label in [ref.label for ref in decision.sources]
    assert "Source:" in decision.text


def test_verified_theme_market_question_is_answered(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    pipeline = build_pipeline(config, fixture_knowledge, llm, store)
    _script(
        llm,
        fixture_knowledge,
        category="theme_market_question",
        product="theme_market",
        query="What are the Theme Market pricing tiers?",
        answer="Theme Market has three tiers: Basic 900 SAR, Plus 1800 SAR, Premium 3600 SAR.",
    )

    decision = pipeline.handle(message("What are the Theme Market pricing tiers?"), today=TODAY)

    assert decision.action is Action.ANSWER
    assert decision.product == "theme_market"
    assert "Basic 900 SAR" in decision.text


def test_arabic_question_is_answered_in_arabic(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    pipeline = build_pipeline(config, fixture_knowledge, llm, store)
    _script(
        llm,
        fixture_knowledge,
        category="zam_question",
        product="zam",
        query="كم مدة مراجعة التطبيق في زام؟",
        answer="مراجعة التطبيق تاخذ 4 أيام عمل من وقت الرفع.",
    )

    decision = pipeline.handle(message("كم مدة مراجعة التطبيق في زام؟"), today=TODAY)

    assert decision.action is Action.ANSWER
    assert decision.language == "ar"
    assert "4 أيام عمل" in decision.text
    assert "المصدر" in decision.text, "the source footer must be localised"


def test_saudi_dialect_question_is_answered_and_the_dialect_is_signalled(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    pipeline = build_pipeline(config, fixture_knowledge, llm, store)
    _script(
        llm,
        fixture_knowledge,
        category="theme_market_question",
        product="theme_market",
        query="وش سياسة الاسترجاع للقوالب؟",
        answer="التاجر يقدر يطلب استرجاع القالب خلال 7 أيام من الشراء، بشرط ما يكون فعّله.",
    )

    decision = pipeline.handle(message("وش سياسة الاسترجاع للقوالب؟"), today=TODAY)

    assert decision.action is Action.ANSWER
    assert decision.language == "ar"
    assert "7 أيام" in decision.text
    answer_call = next(call for call in llm.calls if call["purpose"] == "answer")
    assert "saudi_dialect=true" in answer_call["messages"][0]["content"]
    assert "reply_language=ar" in answer_call["messages"][0]["content"]


def test_general_company_question_with_a_source_is_answered(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    pipeline = build_pipeline(config, fixture_knowledge, llm, store)
    _script(
        llm,
        fixture_knowledge,
        category="general_company_question",
        product=None,
        query="When is partner support available?",
        answer="Partner support runs Sunday to Thursday, 09:00-17:00 Riyadh time.",
    )

    decision = pipeline.handle(message("When is partner support available?"), today=TODAY)

    assert decision.action is Action.ANSWER
    assert "Sunday to Thursday" in decision.text


def test_answers_are_posted_in_a_thread_on_the_original_message(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    pipeline = build_pipeline(config, fixture_knowledge, llm, store)
    _script(
        llm,
        fixture_knowledge,
        category="zam_question",
        product="zam",
        query="What is the ZAM revenue share?",
        answer="The ZAM revenue share is 25 percent of the subscription price.",
    )

    msg = message("What is the ZAM revenue share?", ts="1762790400.000999")
    decision = pipeline.handle(msg, today=TODAY)

    assert decision.thread_ts == msg.message_ts


def test_source_links_can_be_turned_off(fixture_knowledge, llm: FakeLLM, store: SQLiteStore) -> None:
    config = make_config(slack={"include_sources": False})
    pipeline = build_pipeline(config, fixture_knowledge, llm, store)
    _script(
        llm,
        fixture_knowledge,
        category="zam_question",
        product="zam",
        query="What is the ZAM revenue share?",
        answer="The ZAM revenue share is 25 percent.",
    )

    decision = pipeline.handle(message("What is the ZAM revenue share?"), today=TODAY)

    assert decision.action is Action.ANSWER
    assert "Source" not in decision.text


def test_the_interaction_is_recorded_for_auditing(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    pipeline = build_pipeline(config, fixture_knowledge, llm, store)
    _script(
        llm,
        fixture_knowledge,
        category="zam_question",
        product="zam",
        query="How long does ZAM app review take?",
        answer="App review takes 4 business days.",
    )

    pipeline.handle(message("How long does ZAM app review take?"), today=TODAY)

    rows = store.recent_interactions(limit=5)
    assert rows and rows[0]["action"] == "answer"
    assert rows[0]["confidence_level"] == "high"
    assert rows[0]["product"] == "zam"


@pytest.mark.parametrize(
    ("question", "product", "category"),
    [
        ("How long does ZAM app review take?", "zam", "zam_question"),
        ("كم مدة مراجعة التطبيق؟", "zam", "zam_question"),
        ("What are the Theme Market pricing tiers?", "theme_market", "theme_market_question"),
    ],
)
def test_the_grader_sees_the_evidence_and_the_claims(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore, question: str, product: str, category: str
) -> None:
    pipeline = build_pipeline(config, fixture_knowledge, llm, store)
    label = _script(
        llm, fixture_knowledge, category=category, product=product, query=question, answer="Answer text."
    )

    pipeline.handle(message(question), today=TODAY)

    grade_call = next(call for call in llm.calls if call["purpose"] == "grade")
    content = grade_call["messages"][0]["content"]
    assert "<internal_sources>" in content
    assert "<draft_answer>" in content
    assert label in content
