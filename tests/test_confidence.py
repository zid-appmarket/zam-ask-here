"""The confidence gate: what forces escalation, and what the score may decide."""

from __future__ import annotations

import datetime as _dt

from zam_agent.confidence import Action, ConfidenceInputs, ConfidenceLevel, GradingSummary, evaluate
from zam_agent.knowledge.documents import Chunk, Document
from zam_agent.knowledge.index import Evidence, RetrievalResult

from .helpers import make_config

CONFIG = make_config().confidence


def _doc(
    doc_id: str = "d1",
    *,
    status: str = "verified",
    updated: _dt.date | None = _dt.date(2026, 10, 1),
) -> Document:
    return Document(
        doc_id=doc_id,
        title=f"Doc {doc_id}",
        body="body",
        source=f"markdown:{doc_id}.md",
        product="zam",
        status=status,
        updated=updated,
        tags=("t",),
    )


def _evidence(doc: Document, score: float = 0.6, label_suffix: str = "#0") -> Evidence:
    chunk = Chunk(
        chunk_id=f"{doc.doc_id}{label_suffix}",
        doc_id=doc.doc_id,
        text="body",
        heading=None,
        position=0,
        document=doc,
    )
    return Evidence(chunk=chunk, score=score, matched_terms=("a", "b"))


def _retrieval(
    *,
    evidence: tuple[Evidence, ...] = (),
    coverage: float = 1.0,
    conflicts: tuple[str, ...] = (),
    conflicting_doc_ids: frozenset[str] = frozenset(),
    stale: tuple[str, ...] = (),
    excluded_restricted: int = 0,
) -> RetrievalResult:
    return RetrievalResult(
        query="q",
        evidence=evidence,
        coverage=coverage,
        query_terms=("a", "b"),
        matched_terms=("a", "b"),
        conflicts=conflicts,
        stale_doc_ids=stale,
        excluded_restricted=excluded_restricted,
        conflicting_doc_ids=conflicting_doc_ids,
    )


def _answer(label: str, **overrides: object) -> dict[str, object]:
    payload: dict[str, object] = {
        "answer": "Review takes 4 business days.",
        "claims": [{"statement": "Review takes 4 business days.", "source_ids": [label], "kind": "stated"}],
        "cited_source_ids": [label],
        "sufficient_evidence": True,
        "conflicts": [],
        "missing_information": [],
        "clarifying_question": "",
        "self_confidence": 0.9,
    }
    payload.update(overrides)
    return payload


def _grading(*verdicts: str, **overrides: object) -> GradingSummary:
    payload: dict[str, object] = {
        "claims": [{"statement": "s", "verdict": v, "evidence_quote": "q"} for v in verdicts],
        "answer_contains_uncited_facts": False,
        "sources_contradict_each_other": False,
        "verdict_note": "",
    }
    payload.update(overrides)
    return GradingSummary.from_payload(payload)


# ------------------------------------------------------------------ happy path


def test_well_grounded_answer_is_allowed() -> None:
    doc = _doc()
    ev = _evidence(doc, score=0.6)
    verdict = evaluate(
        ConfidenceInputs(
            retrieval=_retrieval(evidence=(ev,)),
            answer_payload=_answer(ev.label),
            grading=_grading("supported", "supported"),
        ),
        CONFIG,
    )
    assert verdict.action is Action.ANSWER
    assert verdict.level is ConfidenceLevel.HIGH
    assert verdict.hard_failures == ()


# ----------------------------------------------------------- hard escalations


def test_no_evidence_escalates() -> None:
    verdict = evaluate(ConfidenceInputs(retrieval=_retrieval()), CONFIG)
    assert verdict.action is Action.ESCALATE
    assert any("no approved internal source" in r for r in verdict.hard_failures)


def test_fabricated_citation_escalates_even_with_perfect_grading() -> None:
    doc = _doc()
    ev = _evidence(doc)
    verdict = evaluate(
        ConfidenceInputs(
            retrieval=_retrieval(evidence=(ev,)),
            answer_payload=_answer("made-up-label#9"),
            grading=_grading("supported"),
        ),
        CONFIG,
    )
    assert verdict.action is Action.ESCALATE
    assert any("not retrieved" in r for r in verdict.hard_failures)


def test_unsupported_claim_escalates_despite_high_self_confidence() -> None:
    doc = _doc()
    ev = _evidence(doc, score=0.9)
    verdict = evaluate(
        ConfidenceInputs(
            retrieval=_retrieval(evidence=(ev,)),
            answer_payload=_answer(ev.label, self_confidence=1.0),
            grading=_grading("supported", "unsupported"),
        ),
        CONFIG,
    )
    assert verdict.action is Action.ESCALATE
    assert any("not supported" in r for r in verdict.hard_failures)


def test_contradicted_claim_escalates() -> None:
    doc = _doc()
    ev = _evidence(doc)
    verdict = evaluate(
        ConfidenceInputs(
            retrieval=_retrieval(evidence=(ev,)),
            answer_payload=_answer(ev.label),
            grading=_grading("contradicted"),
        ),
        CONFIG,
    )
    assert verdict.action is Action.ESCALATE
    assert any("contradicted" in r for r in verdict.hard_failures)


def test_uncited_facts_in_the_answer_escalate() -> None:
    doc = _doc()
    ev = _evidence(doc)
    verdict = evaluate(
        ConfidenceInputs(
            retrieval=_retrieval(evidence=(ev,)),
            answer_payload=_answer(ev.label),
            grading=_grading("supported", answer_contains_uncited_facts=True),
        ),
        CONFIG,
    )
    assert verdict.action is Action.ESCALATE


def test_missing_grading_escalates_rather_than_trusting_the_model() -> None:
    doc = _doc()
    ev = _evidence(doc)
    verdict = evaluate(
        ConfidenceInputs(
            retrieval=_retrieval(evidence=(ev,)),
            answer_payload=_answer(ev.label),
            grading=GradingSummary(),  # verification did not run
        ),
        CONFIG,
    )
    assert verdict.action is Action.ESCALATE
    assert any("verification did not run" in r for r in verdict.hard_failures)


def test_conflict_touching_a_cited_document_escalates() -> None:
    doc = _doc()
    ev = _evidence(doc)
    verdict = evaluate(
        ConfidenceInputs(
            retrieval=_retrieval(
                evidence=(ev,),
                conflicts=("docs disagree",),
                conflicting_doc_ids=frozenset({doc.doc_id}),
            ),
            answer_payload=_answer(ev.label),
            grading=_grading("supported"),
        ),
        CONFIG,
    )
    assert verdict.action is Action.ESCALATE
    assert any("conflict" in r for r in verdict.hard_failures)


def test_conflict_between_documents_the_answer_never_used_is_ignored() -> None:
    """Two unrelated documents disagreeing must not block an unrelated answer."""

    cited = _doc("cited")
    other = _doc("other")
    ev = _evidence(cited)
    verdict = evaluate(
        ConfidenceInputs(
            retrieval=_retrieval(
                evidence=(ev, _evidence(other, score=0.55)),
                conflicts=("the other two disagree",),
                conflicting_doc_ids=frozenset({other.doc_id}),
            ),
            answer_payload=_answer(ev.label),
            grading=_grading("supported"),
        ),
        CONFIG,
    )
    assert verdict.action is Action.ANSWER


def test_model_reported_conflict_always_escalates() -> None:
    """The model saw the passages; if it says they disagree, do not answer."""

    doc = _doc()
    ev = _evidence(doc)
    verdict = evaluate(
        ConfidenceInputs(
            retrieval=_retrieval(evidence=(ev,)),
            answer_payload=_answer(ev.label, conflicts=["source A says 4 days, source B says 10"]),
            grading=_grading("supported"),
        ),
        CONFIG,
    )
    assert verdict.action is Action.ESCALATE


def test_all_sources_stale_escalates() -> None:
    doc = _doc(updated=_dt.date(2022, 1, 1))
    ev = _evidence(doc)
    verdict = evaluate(
        ConfidenceInputs(
            retrieval=_retrieval(evidence=(ev,), stale=(doc.doc_id,)),
            answer_payload=_answer(ev.label),
            grading=_grading("supported"),
        ),
        CONFIG,
    )
    assert verdict.action is Action.ESCALATE
    assert any("freshness limit" in r for r in verdict.hard_failures)


def test_only_draft_sources_escalates() -> None:
    doc = _doc(status="draft")
    ev = _evidence(doc)
    verdict = evaluate(
        ConfidenceInputs(
            retrieval=_retrieval(evidence=(ev,)),
            answer_payload=_answer(ev.label),
            grading=_grading("supported"),
        ),
        CONFIG,
    )
    assert verdict.action is Action.ESCALATE
    assert any("no verified source" in r for r in verdict.hard_failures)


def test_low_term_coverage_escalates() -> None:
    doc = _doc()
    ev = _evidence(doc)
    verdict = evaluate(
        ConfidenceInputs(
            retrieval=_retrieval(evidence=(ev,), coverage=0.2),
            answer_payload=_answer(ev.label),
            grading=_grading("supported"),
        ),
        CONFIG,
    )
    assert verdict.action is Action.ESCALATE
    assert any("key terms" in r for r in verdict.hard_failures)


def test_insufficient_evidence_flag_escalates() -> None:
    doc = _doc()
    ev = _evidence(doc)
    verdict = evaluate(
        ConfidenceInputs(
            retrieval=_retrieval(evidence=(ev,)),
            answer_payload=_answer(ev.label, sufficient_evidence=False),
            grading=_grading("supported"),
        ),
        CONFIG,
    )
    assert verdict.action is Action.ESCALATE


def test_approval_request_and_restricted_ask_always_escalate() -> None:
    doc = _doc()
    ev = _evidence(doc)
    for kwargs in ({"requires_human_approval": True}, {"asks_for_restricted_info": True}):
        verdict = evaluate(
            ConfidenceInputs(
                retrieval=_retrieval(evidence=(ev,)),
                answer_payload=_answer(ev.label),
                grading=_grading("supported"),
                **kwargs,
            ),
            CONFIG,
        )
        assert verdict.action is Action.ESCALATE


def test_withheld_restricted_sources_are_reported_but_not_fatal() -> None:
    doc = _doc()
    ev = _evidence(doc, score=0.6)
    verdict = evaluate(
        ConfidenceInputs(
            retrieval=_retrieval(evidence=(ev,), excluded_restricted=3),
            answer_payload=_answer(ev.label),
            grading=_grading("supported"),
            restricted_sources_excluded=3,
        ),
        CONFIG,
    )
    assert verdict.action is Action.ANSWER
    assert any("withheld" in r for r in verdict.reasons)


# --------------------------------------------------------------- medium band


def test_ambiguous_question_with_a_clarifier_asks_instead_of_escalating() -> None:
    doc = _doc()
    ev = _evidence(doc, score=0.6)
    verdict = evaluate(
        ConfidenceInputs(
            retrieval=_retrieval(evidence=(ev,), coverage=0.2),
            answer_payload=_answer(ev.label, clarifying_question="Do you mean free or paid themes?"),
            grading=_grading("supported"),
            is_ambiguous=True,
        ),
        CONFIG,
    )
    assert verdict.action is Action.CLARIFY
    assert verdict.needs_clarification is True


def test_ambiguity_never_overrides_a_real_accuracy_failure() -> None:
    doc = _doc()
    ev = _evidence(doc)
    verdict = evaluate(
        ConfidenceInputs(
            retrieval=_retrieval(evidence=(ev,), coverage=0.2),
            answer_payload=_answer(ev.label, clarifying_question="Which product?"),
            grading=_grading("contradicted"),
            is_ambiguous=True,
        ),
        CONFIG,
    )
    assert verdict.action is Action.ESCALATE


def test_partial_grounding_below_the_ratio_escalates() -> None:
    doc = _doc()
    ev = _evidence(doc, score=0.8)
    verdict = evaluate(
        ConfidenceInputs(
            retrieval=_retrieval(evidence=(ev,)),
            answer_payload=_answer(ev.label),
            grading=_grading("partial", "partial"),
        ),
        CONFIG,
    )
    assert verdict.action is Action.ESCALATE
    assert any("grounding support" in r for r in verdict.hard_failures)


def test_self_reported_confidence_cannot_carry_a_weak_answer() -> None:
    """Even a self_confidence of 1.0 contributes at most 10% of the score."""

    doc = _doc()
    ev = _evidence(doc, score=0.05)
    verdict = evaluate(
        ConfidenceInputs(
            retrieval=_retrieval(evidence=(ev,), coverage=0.4),
            answer_payload=_answer(ev.label, self_confidence=1.0),
            grading=_grading("partial"),
        ),
        CONFIG,
    )
    assert verdict.action is not Action.ANSWER
    assert verdict.components["self_report"] == 1.0
    assert verdict.score < CONFIG.high_threshold


def test_thresholds_are_configurable() -> None:
    doc = _doc()
    ev = _evidence(doc, score=0.2)
    inputs = ConfidenceInputs(
        retrieval=_retrieval(evidence=(ev,), coverage=0.5),
        answer_payload=_answer(ev.label, self_confidence=0.5),
        grading=_grading("supported"),
    )
    strict = evaluate(inputs, make_config(confidence={"high_threshold": 0.95}).confidence)
    lenient = evaluate(inputs, make_config(confidence={"high_threshold": 0.3}).confidence)
    assert strict.action is not Action.ANSWER
    assert lenient.action is Action.ANSWER
