"""Deterministic confidence evaluation and escalation policy.

The model's own ``self_confidence`` is deliberately treated as a weak hint,
worth a small slice of the score and nothing more. The decision is driven by
things that can be checked:

* **Retrieval coverage** - how many meaningful terms of the question actually
  appear in the retrieved passages.
* **Independent grounding verdicts** - a separate grader call that sees only
  the passages and the claims, and says whether each claim is really in them.
* **Citation validity** - every label the answer cites must exist in the
  retrieved set. A fabricated citation is a hard failure, never a low score.
* **Source quality** - verified vs draft vs deprecated, and staleness.
* **Structural conflict** - metadata-level contradictions in the source set.

Hard rules run first and can force escalation whatever the score says. Only if
no hard rule fires does the weighted score choose between answer / clarify /
escalate.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass, field
from enum import StrEnum
from typing import Any

from .config import ConfidenceConfig
from .knowledge.index import RetrievalResult


class ConfidenceLevel(StrEnum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class Action(StrEnum):
    ANSWER = "answer"
    CLARIFY = "clarify"
    ESCALATE = "escalate"
    IGNORE = "ignore"


# Weights sum to 1.0. The model's self-report is capped at 10% on purpose.
WEIGHTS: Mapping[str, float] = {
    "evidence_coverage": 0.30,
    "grounding": 0.35,
    "retrieval_strength": 0.15,
    "source_quality": 0.10,
    "self_report": 0.10,
}

_VERDICT_CREDIT = {"supported": 1.0, "partial": 0.45, "unsupported": 0.0, "contradicted": 0.0}


@dataclass(frozen=True)
class GradingSummary:
    """Normalised view of the grader's output."""

    total_claims: int = 0
    supported: int = 0
    partial: int = 0
    unsupported: int = 0
    contradicted: int = 0
    uncited_facts: bool = False
    sources_contradict: bool = False
    note: str = ""
    available: bool = False

    @property
    def support_ratio(self) -> float:
        if not self.total_claims:
            return 0.0
        credit = (
            self.supported * _VERDICT_CREDIT["supported"]
            + self.partial * _VERDICT_CREDIT["partial"]
        )
        return credit / self.total_claims

    @property
    def failed_claims(self) -> int:
        return self.unsupported + self.contradicted

    @classmethod
    def from_payload(cls, payload: Mapping[str, Any] | None) -> GradingSummary:
        if not payload:
            return cls()
        claims = payload.get("claims") or []
        counts = {"supported": 0, "partial": 0, "unsupported": 0, "contradicted": 0}
        for claim in claims:
            verdict = str((claim or {}).get("verdict", "unsupported")).strip().lower()
            counts[verdict if verdict in counts else "unsupported"] += 1
        return cls(
            total_claims=len(claims),
            supported=counts["supported"],
            partial=counts["partial"],
            unsupported=counts["unsupported"],
            contradicted=counts["contradicted"],
            uncited_facts=bool(payload.get("answer_contains_uncited_facts")),
            sources_contradict=bool(payload.get("sources_contradict_each_other")),
            note=str(payload.get("verdict_note") or ""),
            available=True,
        )


@dataclass(frozen=True)
class ConfidenceVerdict:
    level: ConfidenceLevel
    action: Action
    score: float
    components: Mapping[str, float]
    reasons: tuple[str, ...]
    hard_failures: tuple[str, ...] = ()
    needs_clarification: bool = False
    escalation_summary: str = ""

    @property
    def may_answer(self) -> bool:
        return self.action is Action.ANSWER

    def to_dict(self) -> dict[str, Any]:
        return {
            "level": self.level.value,
            "action": self.action.value,
            "score": self.score,
            "components": dict(self.components),
            "reasons": list(self.reasons),
            "hard_failures": list(self.hard_failures),
        }


@dataclass
class ConfidenceInputs:
    """Everything the gate is allowed to look at."""

    retrieval: RetrievalResult
    answer_payload: Mapping[str, Any] = field(default_factory=dict)
    grading: GradingSummary = field(default_factory=GradingSummary)
    classifier_confidence: float = 1.0
    requires_human_approval: bool = False
    asks_for_restricted_info: bool = False
    restricted_sources_excluded: int = 0
    is_ambiguous: bool = False

    @property
    def answer_text(self) -> str:
        return str(self.answer_payload.get("answer") or "").strip()

    @property
    def claims(self) -> list[Mapping[str, Any]]:
        return list(self.answer_payload.get("claims") or [])

    @property
    def cited_ids(self) -> set[str]:
        cited = {str(x) for x in (self.answer_payload.get("cited_source_ids") or [])}
        for claim in self.claims:
            cited.update(str(x) for x in (claim.get("source_ids") or []))
        return {c for c in cited if c}

    @property
    def clarifying_question(self) -> str:
        return str(self.answer_payload.get("clarifying_question") or "").strip()

    @property
    def self_confidence(self) -> float:
        try:
            return max(0.0, min(1.0, float(self.answer_payload.get("self_confidence", 0.0))))
        except (TypeError, ValueError):
            return 0.0


def evaluate(inputs: ConfidenceInputs, config: ConfidenceConfig) -> ConfidenceVerdict:
    retrieval = inputs.retrieval
    available_labels = {ev.label for ev in retrieval.evidence}
    hard: list[str] = []
    reasons: list[str] = []

    # ---------------------------------------------------------- hard failures

    if inputs.requires_human_approval:
        hard.append("the request needs a human decision or approval")

    if inputs.asks_for_restricted_info:
        hard.append("the request may involve restricted or confidential information")

    for note in retrieval.resolution_notes:
        reasons.append(note)

    if inputs.restricted_sources_excluded:
        reasons.append(
            f"{inputs.restricted_sources_excluded} restricted source(s) were withheld from this channel"
        )

    if retrieval.is_empty:
        hard.append("no approved internal source matched the question")

    fabricated = inputs.cited_ids - available_labels
    if fabricated:
        hard.append(f"answer cited source(s) that were not retrieved: {', '.join(sorted(fabricated))}")

    if inputs.answer_payload and not inputs.answer_payload.get("sufficient_evidence", False):
        hard.append("the sources do not cover the question")

    if inputs.answer_text and not inputs.cited_ids:
        hard.append("the drafted answer cites no source")

    model_conflicts = tuple(str(c) for c in (inputs.answer_payload.get("conflicts") or []) if str(c).strip())
    # A disagreement between documents the answer never used is not a reason to
    # withhold the answer -- only conflicts touching a cited document count.
    cited_doc_ids = {
        ev.document.doc_id for ev in retrieval.evidence if ev.label in inputs.cited_ids
    }
    structural_conflicts = (
        retrieval.conflicts
        if (not cited_doc_ids or (retrieval.conflicting_doc_ids & cited_doc_ids))
        else ()
    )
    all_conflicts = tuple(dict.fromkeys(structural_conflicts + model_conflicts))
    if all_conflicts:
        hard.append("the sources conflict or are marked out of date: " + "; ".join(all_conflicts[:3]))

    if inputs.grading.available:
        if inputs.grading.contradicted:
            hard.append(f"{inputs.grading.contradicted} claim(s) are contradicted by the sources")
        if inputs.grading.failed_claims > config.max_unsupported_claims:
            hard.append(
                f"{inputs.grading.failed_claims} claim(s) are not supported by the sources "
                f"(limit {config.max_unsupported_claims})"
            )
        if inputs.grading.uncited_facts:
            hard.append("the answer states facts that no source backs")
        if inputs.grading.sources_contradict:
            hard.append("the verifier found the sources contradict each other")
        if inputs.claims and inputs.grading.support_ratio < config.min_supported_claim_ratio:
            hard.append(
                f"grounding support {inputs.grading.support_ratio:.0%} is below the "
                f"{config.min_supported_claim_ratio:.0%} minimum"
            )
    elif inputs.answer_text:
        hard.append("grounding verification did not run")

    if retrieval.coverage < config.min_evidence_coverage and not retrieval.is_empty:
        hard.append(
            f"only {retrieval.coverage:.0%} of the question's key terms appear in the sources "
            f"(minimum {config.min_evidence_coverage:.0%})"
        )

    # Every cited document is stale -> we cannot vouch for the answer.
    cited_docs = [
        ev.document for ev in retrieval.evidence if ev.label in inputs.cited_ids
    ] or list(retrieval.documents())
    if cited_docs and all(doc.doc_id in retrieval.stale_doc_ids for doc in cited_docs):
        hard.append("every source behind this answer is older than the freshness limit")
    if cited_docs and not any(doc.is_verified for doc in cited_docs):
        hard.append("no verified source backs this answer (only draft or deprecated ones)")

    # ------------------------------------------------------------- components

    components = {
        "evidence_coverage": round(min(1.0, retrieval.coverage), 4),
        "grounding": round(inputs.grading.support_ratio if inputs.grading.available else 0.0, 4),
        "retrieval_strength": round(min(1.0, retrieval.top_score / 0.5), 4) if retrieval.evidence else 0.0,
        "source_quality": round(_source_quality(retrieval, inputs.cited_ids), 4),
        "self_report": round(inputs.self_confidence, 4),
    }
    score = round(sum(WEIGHTS[name] * value for name, value in components.items()), 4)

    # ---------------------------------------------------------------- verdict

    if hard:
        summary = _summarize(hard)
        if inputs.is_ambiguous and inputs.clarifying_question and _only_ambiguity(hard):
            return ConfidenceVerdict(
                level=ConfidenceLevel.MEDIUM,
                action=Action.CLARIFY,
                score=score,
                components=components,
                reasons=tuple(reasons + hard),
                hard_failures=tuple(hard),
                needs_clarification=True,
                escalation_summary=summary,
            )
        return ConfidenceVerdict(
            level=ConfidenceLevel.LOW,
            action=Action.ESCALATE,
            score=score,
            components=components,
            reasons=tuple(reasons + hard),
            hard_failures=tuple(hard),
            escalation_summary=summary,
        )

    if score >= config.high_threshold and inputs.classifier_confidence >= 0.5:
        return ConfidenceVerdict(
            level=ConfidenceLevel.HIGH,
            action=Action.ANSWER,
            score=score,
            components=components,
            reasons=tuple(reasons or ["evidence supports the answer"]),
        )

    if score >= config.medium_threshold:
        if inputs.clarifying_question:
            return ConfidenceVerdict(
                level=ConfidenceLevel.MEDIUM,
                action=Action.CLARIFY,
                score=score,
                components=components,
                reasons=tuple(reasons + [f"score {score:.2f} is below the answer threshold "
                                         f"{config.high_threshold:.2f}"]),
                needs_clarification=True,
                escalation_summary="Partially answerable: the agent needs one clarification.",
            )
        return ConfidenceVerdict(
            level=ConfidenceLevel.MEDIUM,
            action=Action.ESCALATE,
            score=score,
            components=components,
            reasons=tuple(reasons + [f"score {score:.2f} is below the answer threshold "
                                     f"{config.high_threshold:.2f} and clarification would not resolve it"]),
            escalation_summary="The available sources only partly cover this question.",
        )

    return ConfidenceVerdict(
        level=ConfidenceLevel.LOW,
        action=Action.ESCALATE,
        score=score,
        components=components,
        reasons=tuple(reasons + [f"score {score:.2f} is below the escalation floor "
                                 f"{config.medium_threshold:.2f}"]),
        escalation_summary="The agent could not verify an answer from the approved sources.",
    )


def _source_quality(retrieval: RetrievalResult, cited_ids: set[str]) -> float:
    docs = [ev.document for ev in retrieval.evidence if ev.label in cited_ids] or list(
        retrieval.documents()
    )
    if not docs:
        return 0.0
    total = 0.0
    for doc in docs:
        value = 1.0 if doc.is_verified else (0.5 if doc.status == "draft" else 0.15)
        if doc.doc_id in retrieval.stale_doc_ids:
            value *= 0.6
        total += value
    return total / len(docs)


_AMBIGUITY_ONLY_PREFIXES = (
    "only ",
    "the sources do not cover the question",
    "no approved internal source matched",
)


def _only_ambiguity(hard: Sequence[str]) -> bool:
    """True when the blockers are 'we may have misunderstood', not 'we are wrong'.

    Clarifying is only safe when nothing suggests the draft is actually
    inaccurate; a contradiction or a fabricated citation always escalates.
    """

    for failure in hard:
        if not failure.startswith(_AMBIGUITY_ONLY_PREFIXES):
            return False
    return bool(hard)


def _summarize(hard: Sequence[str]) -> str:
    if not hard:
        return ""
    head = hard[0]
    if len(hard) == 1:
        return f"Needs verification: {head}."
    return f"Needs verification: {head} (+{len(hard) - 1} more)."
