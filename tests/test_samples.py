"""Table-driven acceptance tests from tests/fixtures/sample_messages.yaml.

Each row in that file is a sample Slack message plus the outcome the agent must
produce. The table doubles as documentation of the agent's contract.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest
import yaml

from zam_agent.confidence import Action
from zam_agent.llm.fake import FakeLLM
from zam_agent.store.sqlite_store import SQLiteStore

from .helpers import (
    OWNER_DEFAULT,
    OWNER_THEME,
    OWNER_ZAM,
    TODAY,
    build_pipeline,
    classification,
    first_label,
    make_config,
    message,
)

SAMPLES_PATH = Path(__file__).parent / "fixtures" / "sample_messages.yaml"
SAMPLES: list[dict[str, Any]] = yaml.safe_load(SAMPLES_PATH.read_text(encoding="utf-8"))

PRODUCT_BY_CATEGORY = {"zam_question": "zam", "theme_market_question": "theme_market"}

SUBSTITUTIONS = {
    "{{OWNER_ZAM}}": f"<@{OWNER_ZAM}>",
    "{{OWNER_THEME}}": f"<@{OWNER_THEME}>",
    "{{OWNER_DEFAULT}}": f"<@{OWNER_DEFAULT}>",
}


def _substitute(value: str) -> str:
    for placeholder, replacement in SUBSTITUTIONS.items():
        value = value.replace(placeholder, replacement)
    return value


def test_the_sample_table_is_well_formed() -> None:
    ids = [sample["id"] for sample in SAMPLES]
    assert len(ids) == len(set(ids)), "sample ids must be unique"
    for sample in SAMPLES:
        assert sample.get("description"), f"{sample['id']} needs a description"
        expect = sample["expect"]
        assert expect["action"] in {"answer", "clarify", "escalate", "ignore", "deflect"}
        if expect["action"] == "ignore":
            assert expect.get("skip_reason"), f"{sample['id']} must state why it is ignored"


@pytest.mark.parametrize("sample", SAMPLES, ids=[s["id"] for s in SAMPLES])
def test_sample_message_produces_the_expected_outcome(
    sample: dict[str, Any], fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    expect = sample["expect"]
    config = make_config(
        slack={"escalate_general_questions": sample.get("escalate_general_questions", False)}
    )

    classify = sample.get("classify")
    product = None
    if classify is not None:
        product = PRODUCT_BY_CATEGORY.get(classify["category"])
        products = classify.get("products", [])
        if product is None and len(products) == 1:
            product = products[0]
        llm.script(
            "classify",
            classification(
                category=classify["category"],
                products=products,
                is_question=classify.get("is_question", True),
                search_query=sample.get("retrieval_query") or sample["message"],
                topic=sample["id"],
                restricted=classify.get("asks_for_restricted_info", False),
                injection=classify.get("injection_attempt", False),
            ),
        )

    if "answer" in sample:
        label_source = sample.get("retrieval_query")
        source_ids = sample.get("cited_source_ids")
        if source_ids is None:
            source_ids = [first_label(fixture_knowledge, label_source, product)] if label_source else []
        raw_claims = sample.get("claims")
        claims = (
            [
                {
                    "statement": claim["statement"],
                    "source_ids": source_ids,
                    "kind": claim.get("kind", "stated"),
                }
                for claim in raw_claims
            ]
            if raw_claims
            else None
        )
        llm.script(
            "answer",
            {
                "answer": sample["answer"],
                "claims": claims
                if claims is not None
                else ([{"statement": sample["answer"], "source_ids": source_ids, "kind": "stated"}]
                      if sample["answer"].strip() else []),
                "cited_source_ids": source_ids,
                "sufficient_evidence": sample.get("sufficient_evidence", True),
                "conflicts": sample.get("conflicts", []),
                "missing_information": [],
                "clarifying_question": sample.get("clarifying_question", ""),
                "self_confidence": sample.get("self_confidence", 0.92),
            },
        )

    if "grading" in sample:
        llm.script(
            "grade",
            {
                "claims": [
                    {"statement": f"claim {i}", "verdict": verdict, "evidence_quote": "q"}
                    for i, verdict in enumerate(sample["grading"])
                ],
                "answer_contains_uncited_facts": sample.get("uncited_facts", False),
                "sources_contradict_each_other": sample.get("sources_contradict", False),
                "verdict_note": "",
            },
        )

    pipeline = build_pipeline(config, fixture_knowledge, llm, store)
    decision = pipeline.handle(message(sample["message"]), today=TODAY)

    assert decision.action is Action(expect["action"]), (
        f"{sample['id']}: expected {expect['action']}, got {decision.action.value} "
        f"(reasons: {list(decision.verdict.reasons) if decision.verdict else decision.skip_reason})"
    )

    if "language" in expect:
        assert decision.language == expect["language"], f"{sample['id']}: wrong reply language"

    if "tagged_owner" in expect:
        assert decision.tagged_owner is expect["tagged_owner"], f"{sample['id']}: wrong tagging behaviour"

    if "skip_reason" in expect:
        assert decision.skip_reason == expect["skip_reason"], f"{sample['id']}: wrong skip reason"

    for needle in expect.get("text_contains", []):
        assert _substitute(needle) in decision.text, f"{sample['id']}: reply is missing {needle!r}"

    for needle in expect.get("text_excludes", []):
        assert _substitute(needle) not in decision.text, f"{sample['id']}: reply must not contain {needle!r}"

    for stage, count in (expect.get("llm_calls") or {}).items():
        assert llm.call_counts[stage] == count, (
            f"{sample['id']}: expected {count} {stage} call(s), got {llm.call_counts[stage]}"
        )


def test_every_required_behaviour_has_at_least_one_sample() -> None:
    """Guard against the table silently losing coverage of a required case."""

    ids = {sample["id"] for sample in SAMPLES}
    required = {
        "zam-review-english",
        "hubspot-link-posted",
        "jira-link-posted",
        "technical-issue-described",
        "theme-pricing-english",
        "zam-review-arabic",
        "theme-refunds-saudi-dialect",
        "unknown-english",
        "unknown-arabic",
        "conflicting-documentation",
        "outdated-documentation",
        "unrelated-chatter",
        "acknowledgement-english",
        "approval-request",
        "restricted-information",
        "prompt-injection",
        "ambiguous-question",
        "hallucinated-fact",
        "fabricated-citation",
    }
    assert required <= ids, f"missing samples: {sorted(required - ids)}"
