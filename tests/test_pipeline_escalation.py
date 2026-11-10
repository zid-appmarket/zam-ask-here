"""Escalation: who gets tagged, when, with what, and when the agent stays quiet."""

from __future__ import annotations

from zam_agent.confidence import Action
from zam_agent.llm.fake import FakeLLM
from zam_agent.store.sqlite_store import SQLiteStore, question_key

from .helpers import (
    CHANNEL,
    OWNER_DEFAULT,
    OWNER_THEME,
    OWNER_ZAM,
    RESTRICTED_CHANNEL,
    TODAY,
    answer_payload,
    build_pipeline,
    classification,
    first_label,
    grade_payload,
    make_config,
    message,
)

UNKNOWN_EN = "What is the exact uninstall-refund SLA for enterprise merchants?"
UNKNOWN_AR = "وش بالضبط إجراءات إلغاء اشتراك التاجر المؤسسي؟"


def test_unknown_question_tags_the_product_owner_in_english(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    pipeline = build_pipeline(config, fixture_knowledge, llm, store)
    llm.script("classify", classification(category="zam_question", search_query=UNKNOWN_EN))

    decision = pipeline.handle(message(UNKNOWN_EN), today=TODAY)

    assert decision.action is Action.ESCALATE
    assert decision.tagged_owner is True
    assert decision.owner_user_id == OWNER_ZAM
    assert f"<@{OWNER_ZAM}>" in decision.text
    assert "unable to verify" in decision.text
    assert "could you please confirm this?" in decision.text
    assert "What needs confirming:" in decision.text


def test_unknown_question_tags_the_owner_in_arabic(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    pipeline = build_pipeline(config, fixture_knowledge, llm, store)
    llm.script("classify", classification(category="zam_question", search_query=UNKNOWN_AR))

    decision = pipeline.handle(message(UNKNOWN_AR), today=TODAY)

    assert decision.action is Action.ESCALATE
    assert decision.language == "ar"
    assert f"<@{OWNER_ZAM}>" in decision.text
    assert "ما عندي معلومة مؤكدة كفاية" in decision.text
    assert "ممكن تتأكد لنا من النقطة هذي؟" in decision.text


def test_theme_market_questions_go_to_the_theme_market_owner(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    pipeline = build_pipeline(config, fixture_knowledge, llm, store)
    llm.script(
        "classify",
        classification(
            category="theme_market_question",
            products=["theme_market"],
            search_query="Who signs off a theme takedown request?",
        ),
    )

    decision = pipeline.handle(message("Who signs off a theme takedown request?"), today=TODAY)

    assert decision.owner_user_id == OWNER_THEME
    assert f"<@{OWNER_THEME}>" in decision.text


def test_general_questions_fall_back_to_the_default_owner(
    fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    config = make_config(slack={"escalate_general_questions": True})
    pipeline = build_pipeline(config, fixture_knowledge, llm, store)
    llm.script(
        "classify",
        classification(
            category="general_company_question",
            products=[],
            search_query="What is the travel reimbursement limit?",
        ),
    )

    decision = pipeline.handle(message("What is the travel reimbursement limit?"), today=TODAY)

    assert decision.action is Action.ESCALATE
    assert decision.owner_user_id == OWNER_DEFAULT


def test_owner_gets_a_context_message_with_the_question_and_the_reason(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    pipeline = build_pipeline(config, fixture_knowledge, llm, store)
    llm.script("classify", classification(category="zam_question", search_query=UNKNOWN_EN))

    decision = pipeline.handle(message(UNKNOWN_EN), today=TODAY)

    assert "A question needs your confirmation" in decision.owner_context
    assert "uninstall-refund SLA" in decision.owner_context
    assert f"<#{CHANNEL}>" in decision.owner_context
    assert "Why the agent did not answer:" in decision.owner_context


def test_the_same_question_is_not_escalated_twice_within_the_cooldown(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    pipeline = build_pipeline(config, fixture_knowledge, llm, store)
    llm.script("classify", classification(category="zam_question", search_query=UNKNOWN_EN))

    first = pipeline.handle(message(UNKNOWN_EN, ts="1.000100"), today=TODAY)
    second = pipeline.handle(message(UNKNOWN_EN, ts="2.000200"), today=TODAY)

    assert first.tagged_owner is True
    assert second.tagged_owner is False
    assert f"<@{OWNER_ZAM}>" not in second.text
    assert "already with the owner" in second.text
    assert second.owner_context == ""


def test_repeat_escalation_is_suppressed_across_wording_variants(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    """Normalisation means punctuation and tashkeel do not defeat the cooldown."""

    pipeline = build_pipeline(config, fixture_knowledge, llm, store)
    llm.script("classify", classification(category="zam_question", search_query=UNKNOWN_AR))

    first = pipeline.handle(message(UNKNOWN_AR, ts="1.000100"), today=TODAY)
    second = pipeline.handle(message(UNKNOWN_AR + "؟؟", ts="2.000200"), today=TODAY)

    assert first.tagged_owner is True
    assert second.tagged_owner is False


def test_escalation_is_recorded_as_a_knowledge_gap(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    pipeline = build_pipeline(config, fixture_knowledge, llm, store)
    llm.script("classify", classification(category="zam_question", search_query=UNKNOWN_EN))

    pipeline.handle(message(UNKNOWN_EN), today=TODAY)

    gaps = store.knowledge_gaps()
    assert len(gaps) == 1
    assert gaps[0].question_key == question_key(UNKNOWN_EN, "zam")
    assert gaps[0].product == "zam"


def test_approval_request_escalates_without_attempting_an_answer(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    pipeline = build_pipeline(config, fixture_knowledge, llm, store)
    llm.script(
        "classify",
        classification(
            category="requires_human_approval",
            products=["zam"],
            search_query="Please approve my app for publishing today",
        ),
    )

    decision = pipeline.handle(message("Please approve my app for publishing today"), today=TODAY)

    assert decision.action is Action.ESCALATE
    assert decision.tagged_owner is True
    assert "needs a human decision" in decision.text
    assert llm.call_counts["answer"] == 0, "no answer should be drafted for an approval request"


def test_restricted_request_is_not_answered_in_a_public_channel(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    pipeline = build_pipeline(config, fixture_knowledge, llm, store)
    llm.script(
        "classify",
        classification(
            category="zam_question",
            search_query="How much did Partner Alpha earn last quarter?",
            restricted=True,
        ),
    )

    decision = pipeline.handle(message("How much did Partner Alpha earn last quarter?"), today=TODAY)

    assert decision.action is Action.ESCALATE
    assert "may be restricted" in decision.text
    assert "120000" not in decision.text
    assert llm.call_counts["answer"] == 0


def test_restricted_documents_are_never_retrieved_for_a_public_channel(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    """Even if the classifier misses it, the audience filter holds the line."""

    pipeline = build_pipeline(config, fixture_knowledge, llm, store)
    llm.script(
        "classify",
        classification(
            category="zam_question",
            search_query="per-partner revenue figures for Partner Alpha",
            restricted=False,
        ),
    )
    llm.script("answer", answer_payload(answer="n/a", source_ids=[], sufficient=False))
    llm.script("grade", grade_payload(verdicts=["unsupported"]))

    decision = pipeline.handle(message("What revenue did Partner Alpha make?"), today=TODAY)

    answer_calls = [call for call in llm.calls if call["purpose"] == "answer"]
    for call in answer_calls:
        assert "120000" not in call["messages"][0]["content"]
    assert decision.action is Action.ESCALATE


def test_restricted_channel_may_see_restricted_documents(
    fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    config = make_config(
        slack={
            "channel_ids": (CHANNEL, RESTRICTED_CHANNEL),
            "internal_channel_ids": (CHANNEL, RESTRICTED_CHANNEL),
            "restricted_channel_ids": (RESTRICTED_CHANNEL,),
        }
    )
    pipeline = build_pipeline(config, fixture_knowledge, llm, store)
    query = "per-partner revenue figures for Partner Alpha"
    label = first_label(fixture_knowledge, query, "zam")  # public label, used for shape only
    llm.script("classify", classification(category="zam_question", search_query=query))
    llm.script("answer", answer_payload(answer="Alpha earned 120000 SAR.", source_ids=[label]))
    llm.script("grade", grade_payload(verdicts=["supported"]))

    pipeline.handle(message(query, channel_id=RESTRICTED_CHANNEL), today=TODAY)

    answer_call = next(call for call in llm.calls if call["purpose"] == "answer")
    assert "Individual partner revenue figures" in answer_call["messages"][0]["content"]


def test_conflicting_documentation_escalates_instead_of_picking_a_side(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    query = "How many Vitrin checks must a theme pass?"
    label = first_label(fixture_knowledge, query, "theme_market")
    pipeline = build_pipeline(config, fixture_knowledge, llm, store)
    llm.script(
        "classify",
        classification(category="theme_market_question", products=["theme_market"], search_query=query),
    )
    llm.script("answer", answer_payload(answer="A theme must pass 12 checks.", source_ids=[label]))
    llm.script("grade", grade_payload(verdicts=["supported"]))

    decision = pipeline.handle(message(query), today=TODAY)

    assert decision.action is Action.ESCALATE
    assert any("conflict" in reason or "updated" in reason for reason in decision.verdict.reasons)


def test_outdated_only_documentation_escalates(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    query = "When are ZAM payouts issued?"
    label = first_label(fixture_knowledge, query, "zam")
    pipeline = build_pipeline(config, fixture_knowledge, llm, store)
    llm.script("classify", classification(category="zam_question", search_query=query))
    llm.script("answer", answer_payload(answer="Payouts go out on the 1st.", source_ids=[label]))
    llm.script("grade", grade_payload(verdicts=["supported"]))

    decision = pipeline.handle(message(query), today=TODAY)

    assert decision.action is Action.ESCALATE


def test_stale_source_cannot_support_a_confident_answer(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    query = "How do I get a ZAM sandbox store?"
    label = first_label(fixture_knowledge, query, "zam")
    pipeline = build_pipeline(config, fixture_knowledge, llm, store)
    llm.script("classify", classification(category="zam_question", search_query=query))
    llm.script(
        "answer", answer_payload(answer="Request it from the partner dashboard.", source_ids=[label])
    )
    llm.script("grade", grade_payload(verdicts=["supported"]))

    decision = pipeline.handle(message(query), today=TODAY)

    assert decision.action is Action.ESCALATE
    assert any("freshness" in reason for reason in decision.verdict.hard_failures)


def test_a_fabricated_citation_escalates_end_to_end(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    query = "How long does ZAM app review take?"
    pipeline = build_pipeline(config, fixture_knowledge, llm, store)
    llm.script("classify", classification(category="zam_question", search_query=query))
    llm.script(
        "answer",
        answer_payload(answer="Review takes 2 days.", source_ids=["zam-invented-policy#3"]),
    )
    llm.script("grade", grade_payload(verdicts=["supported"]))

    decision = pipeline.handle(message(query), today=TODAY)

    assert decision.action is Action.ESCALATE
    assert any("not retrieved" in reason for reason in decision.verdict.hard_failures)


def test_an_unsupported_claim_escalates_end_to_end(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    query = "How long does ZAM app review take?"
    label = first_label(fixture_knowledge, query, "zam")
    pipeline = build_pipeline(config, fixture_knowledge, llm, store)
    llm.script("classify", classification(category="zam_question", search_query=query))
    llm.script(
        "answer",
        answer_payload(
            answer="Review takes 4 business days and costs 500 SAR.",
            source_ids=[label],
            claims=[
                {"statement": "Review takes 4 business days.", "source_ids": [label], "kind": "stated"},
                {"statement": "It costs 500 SAR.", "source_ids": [label], "kind": "stated"},
            ],
            self_confidence=0.99,
        ),
    )
    llm.script("grade", grade_payload(verdicts=["supported", "unsupported"]))

    decision = pipeline.handle(message(query), today=TODAY)

    assert decision.action is Action.ESCALATE
    assert "500 SAR" not in decision.text


def test_ambiguous_question_asks_a_clarifying_question_without_tagging(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    query = "how much is it?"
    label = first_label(fixture_knowledge, "Theme Market pricing tiers", "theme_market")
    pipeline = build_pipeline(config, fixture_knowledge, llm, store)
    llm.script(
        "classify",
        classification(
            category="unclear_question", products=["theme_market"], search_query="theme pricing"
        ),
    )
    llm.script(
        "answer",
        answer_payload(
            answer="",
            source_ids=[label],
            sufficient=True,
            clarifying_question="Do you mean the Theme Market tier price or an app subscription price?",
        ),
    )
    llm.script("grade", grade_payload(verdicts=["supported"]))

    decision = pipeline.handle(message(query), today=TODAY)

    assert decision.action is Action.CLARIFY
    assert decision.tagged_owner is False
    assert "Do you mean" in decision.text
    assert f"<@{OWNER_ZAM}>" not in decision.text
