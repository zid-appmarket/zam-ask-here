"""Message-processing pipeline: classify -> retrieve -> answer -> verify -> act.

The pipeline is pure with respect to Slack: it takes an
:class:`IncomingMessage` and returns an :class:`AgentDecision`. Nothing here
calls the Slack API, which is what makes the whole decision path testable
without a workspace.
"""

from __future__ import annotations

import datetime as _dt
import time
from collections.abc import Mapping, Sequence
from dataclasses import dataclass, field, replace
from typing import Any, Literal

from .confidence import Action, ConfidenceInputs, ConfidenceVerdict, GradingSummary, evaluate
from .config import AppConfig
from .deflection import deflection_message
from .escalation import EscalationManager
from .knowledge.index import RetrievalResult
from .knowledge.ingest import KnowledgeBase, format_evidence_block
from .language import LanguageProfile
from .language import profile as language_profile
from .llm.base import LLMClient, LLMError, LLMInvalidOutput, LLMRateLimited, LLMRefusal, LLMTimeout
from .observability.logging import get_logger
from .observability.metrics import METRICS
from .prompts import answer as answer_prompt
from .prompts import classifier as classifier_prompt
from .prompts import grader as grader_prompt
from .security import allowed_audiences, sanitize_outbound
from .store.base import Store
from .store.sqlite_store import question_key
from .triage import TicketSignal, detect_ticket_links

log = get_logger(__name__)

PRODUCT_BY_CATEGORY = {
    "zam_question": "zam",
    "theme_market_question": "theme_market",
}

# Cheap relevance signal so a busy company-wide channel does not cost an LLM
# call per message. The classifier remains the authority -- this only decides
# whether it is worth asking it.
PRODUCT_KEYWORDS: tuple[str, ...] = (
    "zam", "زام", "app market", "appmarket", "سوق التطبيقات", "متجر التطبيقات",
    "theme market", "thememarket", "سوق القوالب", "متجر القوالب", "القوالب", "قالب",
    "theme", "themes", "app", "apps", "تطبيق", "تطبيقات", "partner", "شريك", "الشركاء",
    "merchant", "تاجر", "التجار", "زد", "zid", "publish", "نشر", "review", "مراجعة",
    "revenue share", "نسبة", "عمولة", "payout", "مستحقات", "sandbox", "vitrin", "فترين",
)


@dataclass(frozen=True)
class IncomingMessage:
    channel_id: str
    user_id: str
    text: str
    message_ts: str
    event_key: str
    thread_ts: str | None = None
    is_thread_reply: bool = False
    bot_participated_in_thread: bool = False
    directly_addressed: bool = False
    thread_context: str = ""
    permalink: str | None = None

    @property
    def reply_thread_ts(self) -> str:
        """Always reply in a thread: a new one on the message, or the existing one."""

        return self.thread_ts or self.message_ts


@dataclass(frozen=True)
class SourceRef:
    label: str
    title: str
    url: str | None
    status: str
    updated: str | None


DEFLECTION_REASON_BY_SIGNAL = {"hubspot": "hubspot_link", "jira": "jira_link"}


@dataclass(frozen=True)
class DecisionContext:
    """The classification facts every decision for one message carries."""

    category: str = ""
    product: str | None = None
    language: Literal["ar", "en"] = "en"
    topic: str = ""
    thread_ts: str | None = None


@dataclass(frozen=True)
class AgentDecision:
    action: Action
    text: str = ""
    thread_ts: str | None = None
    category: str = ""
    product: str | None = None
    language: Literal["ar", "en"] = "en"
    topic: str = ""
    verdict: ConfidenceVerdict | None = None
    sources: tuple[SourceRef, ...] = ()
    owner_user_id: str | None = None
    owner_context: str = ""
    tagged_owner: bool = False
    question_key: str = ""
    skip_reason: str = ""
    retryable_error: bool = False
    latency_ms: int = 0
    diagnostics: Mapping[str, Any] = field(default_factory=dict)

    @property
    def should_post(self) -> bool:
        return self.action is not Action.IGNORE and bool(self.text)

    @property
    def confidence_level(self) -> str:
        return self.verdict.level.value if self.verdict else ""

    @property
    def confidence_score(self) -> float:
        return self.verdict.score if self.verdict else 0.0


class SupportPipeline:
    def __init__(
        self,
        *,
        config: AppConfig,
        knowledge: KnowledgeBase,
        llm: LLMClient,
        store: Store,
        escalation: EscalationManager | None = None,
    ) -> None:
        self.config = config
        self.knowledge = knowledge
        self.llm = llm
        self.store = store
        self.escalation = escalation or EscalationManager(config.escalation, store)

    # ------------------------------------------------------------------ entry

    def handle(self, message: IncomingMessage, *, today: _dt.date | None = None) -> AgentDecision:
        started = time.perf_counter()
        lang = language_profile(message.text)
        today = today or _dt.date.today()

        def finish(decision: AgentDecision) -> AgentDecision:
            elapsed = int((time.perf_counter() - started) * 1000)
            decided = replace(decision, latency_ms=elapsed)
            self._record(message, decided)
            METRICS.incr(f"pipeline.action.{decided.action.value}")
            METRICS.observe("pipeline.latency_ms", elapsed)
            return decided

        skip = self._prefilter(message, lang)
        if skip:
            return finish(
                AgentDecision(action=Action.IGNORE, skip_reason=skip, language=lang.reply_in)
            )

        # A ticket link is a string, not a judgement call: redirect it before
        # spending a model call, and before the prefilter's product keywords can
        # route it into the answering path.
        ticket = detect_ticket_links(message.text)
        if ticket.found and self.config.slack.deflect_technical_issues:
            return finish(self._deflect(message, lang, ticket=ticket))

        # -------------------------------------------------------- 1. classify
        try:
            classification = self._classify(message, lang)
        except (LLMTimeout, LLMRateLimited) as exc:
            log.warning("classification unavailable", extra={"context": {"error": str(exc)}})
            return finish(
                AgentDecision(
                    action=Action.IGNORE,
                    skip_reason="transient_llm_error",
                    retryable_error=True,
                    language=lang.reply_in,
                )
            )
        except LLMError as exc:
            log.error("classification failed", extra={"context": {"error": str(exc)}})
            return finish(
                AgentDecision(action=Action.IGNORE, skip_reason="classification_failed", language=lang.reply_in)
            )

        category = str(classification.get("category", "unclear_question"))
        products = [str(p) for p in (classification.get("products") or [])]
        product = PRODUCT_BY_CATEGORY.get(category) or (products[0] if len(products) == 1 else None)
        topic = str(classification.get("topic") or "")[:120]
        search_query = str(classification.get("search_query") or message.text).strip() or message.text
        is_question = bool(classification.get("is_question"))
        restricted = bool(classification.get("asks_for_restricted_info"))
        injection = bool(classification.get("injection_attempt"))
        needs_approval = category == "requires_human_approval"
        try:
            classifier_confidence = float(classification.get("confidence", 0.5))
        except (TypeError, ValueError):
            classifier_confidence = 0.5

        if injection:
            METRICS.incr("security.injection_attempt")
            log.warning(
                "message attempted to override agent instructions",
                extra={
                    "context": {
                        "channel_id": message.channel_id,
                        "message_ts": message.message_ts,
                        "category": category,
                    }
                },
            )

        context = DecisionContext(
            category=category,
            product=product,
            language=lang.reply_in,
            topic=topic,
            thread_ts=message.reply_thread_ts,
        )

        if category == "technical_issue_or_incident":
            if not self.config.slack.deflect_technical_issues:
                return finish(
                    _decide(context, Action.IGNORE, skip_reason="technical_issue_deflection_disabled")
                )
            return finish(self._deflect(message, lang, context=context))

        # ----------------------------------------------------------- 2. route
        gate = self._route(
            category=category,
            is_question=is_question,
            injection=injection,
            message=message,
        )
        if gate:
            return finish(_decide(context, Action.IGNORE, skip_reason=gate))

        # -------------------------------------------------------- 3. retrieve
        audiences = allowed_audiences(message.channel_id, self.config.slack)
        retrieval = self.knowledge.retrieve(
            search_query,
            product=product,
            allow_internal="internal" in audiences,
            allow_restricted="restricted" in audiences,
            today=today,
        )

        # A general company question the knowledge base cannot address is not
        # the agent's business -- staying quiet beats pinging an owner about it.
        # "Cannot address" uses the same coverage floor as the confidence gate,
        # so a weak incidental match is treated as no match.
        unusable = retrieval.is_empty or retrieval.coverage < self.config.confidence.min_evidence_coverage
        if (
            category == "general_company_question"
            and unusable
            and not self.config.slack.escalate_general_questions
        ):
            return finish(_decide(context, Action.IGNORE, skip_reason="general_question_no_sources"))

        # Approval requests and restricted asks never get an answer attempt.
        if needs_approval or restricted:
            return finish(
                self._escalate(
                    message=message,
                    lang=lang,
                    product=product,
                    topic=topic,
                    search_query=search_query,
                    reasons=(
                        ("the request needs a human decision or approval",)
                        if needs_approval
                        else ("the request may involve restricted or confidential information",)
                    ),
                    summary="",
                    requires_human_approval=needs_approval,
                    restricted=restricted,
                    verdict=None,
                    context=context,
                )
            )

        evidence_block = format_evidence_block(retrieval.evidence)

        # ---------------------------------------------------------- 4. answer
        answer_payload: Mapping[str, Any] = {}
        if not retrieval.is_empty:
            try:
                answer_payload = self._answer(
                    message=message,
                    lang=lang,
                    product=product,
                    question=search_query,
                    evidence_block=evidence_block,
                    today=today,
                )
            except (LLMTimeout, LLMRateLimited) as exc:
                log.warning("answer generation unavailable", extra={"context": {"error": str(exc)}})
                return finish(
                    _decide(
                        context,
                        Action.IGNORE,
                        skip_reason="transient_llm_error",
                        retryable_error=True,
                    )
                )
            except LLMRefusal as exc:
                log.warning("model refused to answer", extra={"context": {"category": exc.category}})
                answer_payload = {}
            except (LLMInvalidOutput, LLMError) as exc:
                log.error("answer generation failed", extra={"context": {"error": str(exc)}})
                answer_payload = {}

        # ------------------------------------------------------- 5. verify it
        grading = GradingSummary()
        claims = list(answer_payload.get("claims") or [])
        if answer_payload.get("answer") and claims:
            try:
                grading = GradingSummary.from_payload(
                    self._grade(
                        question=search_query,
                        answer=str(answer_payload.get("answer") or ""),
                        claims=claims,
                        evidence_block=evidence_block,
                    )
                )
            except LLMError as exc:
                # Unverified means not answerable: fall through to escalation.
                log.warning("grounding verification failed", extra={"context": {"error": str(exc)}})
                grading = GradingSummary()

        # ------------------------------------------------------ 6. confidence
        verdict = evaluate(
            ConfidenceInputs(
                retrieval=retrieval,
                answer_payload=answer_payload,
                grading=grading,
                classifier_confidence=classifier_confidence,
                requires_human_approval=False,
                asks_for_restricted_info=False,
                restricted_sources_excluded=retrieval.excluded_restricted
                if "restricted" not in audiences
                else 0,
                is_ambiguous=category == "unclear_question",
            ),
            self.config.confidence,
        )

        sources = _source_refs(retrieval, answer_payload)

        # ----------------------------------------------------------- 7. reply
        if verdict.action is Action.ANSWER:
            text = sanitize_outbound(str(answer_payload.get("answer") or ""))
            if not text:
                verdict = ConfidenceVerdict(
                    level=verdict.level,
                    action=Action.ESCALATE,
                    score=verdict.score,
                    components=verdict.components,
                    reasons=verdict.reasons + ("the generated answer was empty",),
                    hard_failures=verdict.hard_failures + ("the generated answer was empty",),
                    escalation_summary="The agent produced no usable answer.",
                )
            else:
                if self.config.slack.include_sources and sources:
                    text = f"{text}\n\n{_source_footer(sources, lang.reply_in)}"
                METRICS.incr("pipeline.answered")
                return finish(
                    _decide(
                        context,
                        Action.ANSWER,
                        text=text,
                        verdict=verdict,
                        sources=sources,
                        question_key=question_key(search_query, product),
                        diagnostics=_diagnostics(retrieval, grading),
                    )
                )

        if verdict.action is Action.CLARIFY:
            clarifier = sanitize_outbound(str(answer_payload.get("clarifying_question") or ""), max_chars=400)
            if clarifier:
                METRICS.incr("pipeline.clarified")
                return finish(
                    _decide(
                        context,
                        Action.CLARIFY,
                        text=clarifier,
                        verdict=verdict,
                        question_key=question_key(search_query, product),
                        diagnostics=_diagnostics(retrieval, grading),
                    )
                )

        partial = ""
        if verdict.level.value == "medium" and answer_payload.get("answer"):
            partial = str(answer_payload.get("answer") or "")

        return finish(
            self._escalate(
                message=message,
                lang=lang,
                product=product,
                topic=topic,
                search_query=search_query,
                reasons=verdict.hard_failures or verdict.reasons,
                summary=verdict.escalation_summary,
                partial_answer=partial,
                sources=sources if self.config.slack.include_sources else (),
                verdict=verdict,
                context=context,
                diagnostics=_diagnostics(retrieval, grading),
            )
        )

    # ----------------------------------------------------------- stage helpers

    def _prefilter(self, message: IncomingMessage, lang: LanguageProfile) -> str:
        text = message.text.strip()
        if not text:
            return "empty_message"
        if lang.is_acknowledgement:
            return "acknowledgement_only"
        if not self.config.slack.prefilter_enabled:
            return ""
        if message.directly_addressed or message.bot_participated_in_thread:
            return ""
        lowered = text.lower()
        if any(keyword in lowered for keyword in PRODUCT_KEYWORDS):
            return ""
        if lang.is_question:
            return ""
        return "no_question_or_product_signal"

    def _route(
        self,
        *,
        category: str,
        is_question: bool,
        injection: bool,
        message: IncomingMessage,
    ) -> str:
        if category == "unrelated_conversation" and not self.config.slack.respond_to_unrelated:
            return "classified_unrelated"
        if injection and category in ("unrelated_conversation", "unclear_question"):
            return "injection_attempt_no_question"
        if (
            category == "general_company_question"
            and not self.config.slack.answer_general_questions
        ):
            return "general_questions_disabled"
        if not is_question and self.config.slack.respond_only_to_questions:
            if category == "thread_follow_up" and message.bot_participated_in_thread:
                return ""
            return "not_a_question"
        return ""

    def _classify(self, message: IncomingMessage, lang: LanguageProfile) -> Mapping[str, Any]:
        user_turn = classifier_prompt.build_user_turn(
            message=message.text,
            thread_context=message.thread_context,
            language_hint=lang.detected,
            heuristic_is_question=lang.is_question,
            in_thread=message.is_thread_reply,
        )
        result = self.llm.generate_json(
            system=classifier_prompt.SYSTEM,
            messages=[{"role": "user", "content": user_turn}],
            schema=classifier_prompt.SCHEMA,
            model=self.config.llm.classifier_model,
            effort=self.config.llm.classifier_effort,
            max_tokens=1024,
        )
        return result.data

    def _answer(
        self,
        *,
        message: IncomingMessage,
        lang: LanguageProfile,
        product: str | None,
        question: str,
        evidence_block: str,
        today: _dt.date,
    ) -> Mapping[str, Any]:
        user_turn = answer_prompt.build_user_turn(
            question=message.text,
            evidence_block=evidence_block,
            thread_context=message.thread_context,
            language=lang.reply_in,
            saudi_dialect=lang.saudi_dialect,
            product=product,
            today=today.isoformat(),
        )
        result = self.llm.generate_json(
            system=answer_prompt.SYSTEM,
            messages=[{"role": "user", "content": user_turn}],
            schema=answer_prompt.SCHEMA,
            model=self.config.llm.model,
            effort=self.config.llm.effort,
        )
        return result.data

    def _grade(
        self,
        *,
        question: str,
        answer: str,
        claims: Sequence[Mapping[str, Any]],
        evidence_block: str,
    ) -> Mapping[str, Any]:
        user_turn = grader_prompt.build_user_turn(
            question=question,
            answer=answer,
            claims=[dict(claim) for claim in claims],
            evidence_block=evidence_block,
        )
        result = self.llm.generate_json(
            system=grader_prompt.SYSTEM,
            messages=[{"role": "user", "content": user_turn}],
            schema=grader_prompt.SCHEMA,
            model=self.config.llm.grader_model,
            effort=self.config.llm.grader_effort,
            max_tokens=2048,
        )
        return result.data

    def _deflect(
        self,
        message: IncomingMessage,
        lang: LanguageProfile,
        *,
        ticket: TicketSignal | None = None,
        context: DecisionContext | None = None,
    ) -> AgentDecision:
        """Point a technical issue at HubSpot instead of answering it."""

        reason = (
            DEFLECTION_REASON_BY_SIGNAL[ticket.kind]
            if ticket is not None and ticket.found
            else "technical_issue"
        )

        text = deflection_message(
            reason=reason,  # type: ignore[arg-type]
            language=lang.reply_in,
            hubspot_ticket_url=self.config.slack.hubspot_ticket_url,
        )
        METRICS.incr(f"pipeline.deflected.{reason}")
        log.info(
            "redirected a technical issue out of the channel",
            extra={
                "context": {
                    "reason": reason,
                    "channel_id": message.channel_id,
                    "message_ts": message.message_ts,
                    "matched": list(ticket.matched) if ticket else [],
                }
            },
        )
        base = context or DecisionContext(
            category="technical_issue_or_incident",
            language=lang.reply_in,
            thread_ts=message.reply_thread_ts,
        )
        return _decide(
            base,
            Action.DEFLECT,
            text=text,
            skip_reason=reason,
            diagnostics={"deflection": {"reason": reason, "matched": list(ticket.matched) if ticket else []}},
        )

    def _escalate(
        self,
        *,
        message: IncomingMessage,
        lang: LanguageProfile,
        product: str | None,
        topic: str,
        search_query: str,
        reasons: Sequence[str],
        summary: str,
        context: DecisionContext,
        verdict: ConfidenceVerdict | None,
        partial_answer: str = "",
        sources: Sequence[SourceRef] = (),
        requires_human_approval: bool = False,
        restricted: bool = False,
        diagnostics: Mapping[str, Any] | None = None,
    ) -> AgentDecision:
        source_lines = [_source_footer(sources, lang.reply_in)] if sources else []
        plan = self.escalation.build(
            question=message.text,
            language=lang.reply_in,
            product=product,
            channel_id=message.channel_id,
            thread_ts=message.reply_thread_ts,
            topic=topic or search_query[:60],
            reasons=reasons,
            summary=summary,
            partial_answer=partial_answer,
            source_lines=source_lines,
            requires_human_approval=requires_human_approval,
            restricted=restricted,
        )
        owner_context = ""
        if plan.tagged:
            owner_context = self.escalation.owner_context_message(
                question=message.text,
                asker_user_id=message.user_id,
                channel_id=message.channel_id,
                permalink=message.permalink,
                reasons=reasons,
                product=product,
                language="en",
            )
            METRICS.incr("pipeline.escalated")
        else:
            METRICS.incr("pipeline.escalation_suppressed")
        return _decide(
            context,
            Action.ESCALATE,
            text=plan.text,
            verdict=verdict,
            sources=tuple(sources),
            owner_user_id=plan.owner_user_id,
            owner_context=owner_context,
            tagged_owner=plan.tagged,
            question_key=plan.question_key,
            diagnostics=dict(diagnostics or {}),
        )

    # ------------------------------------------------------------------ audit

    def _record(self, message: IncomingMessage, decision: AgentDecision) -> None:
        try:
            self.store.record_interaction(
                event_key=message.event_key,
                channel_id=message.channel_id,
                thread_ts=message.thread_ts,
                message_ts=message.message_ts,
                user_id=message.user_id,
                category=decision.category or decision.skip_reason,
                action=decision.action.value,
                confidence_level=decision.confidence_level,
                confidence_score=decision.confidence_score,
                language=decision.language,
                topic=decision.topic,
                product=decision.product,
                reasons="; ".join((decision.verdict.reasons if decision.verdict else ())[:4]),
                source_ids=",".join(ref.label for ref in decision.sources),
                latency_ms=decision.latency_ms,
            )
        except Exception:  # pragma: no cover - telemetry must never break a reply
            log.exception("failed to record interaction")


def _decide(context: DecisionContext, action: Action, **fields: Any) -> AgentDecision:
    """Build an :class:`AgentDecision` carrying this message's context."""

    return AgentDecision(
        action=action,
        category=context.category,
        product=context.product,
        language=context.language,
        topic=context.topic,
        thread_ts=context.thread_ts,
        **fields,
    )


def _source_refs(
    retrieval: RetrievalResult, answer_payload: Mapping[str, Any]
) -> tuple[SourceRef, ...]:
    cited = {str(x) for x in (answer_payload.get("cited_source_ids") or [])}
    for claim in answer_payload.get("claims") or []:
        cited.update(str(x) for x in (claim.get("source_ids") or []))
    chosen = [ev for ev in retrieval.evidence if ev.label in cited] or list(retrieval.evidence[:2])

    refs: list[SourceRef] = []
    seen: set[str] = set()
    for ev in chosen:
        doc = ev.document
        if doc.doc_id in seen:
            continue
        seen.add(doc.doc_id)
        refs.append(
            SourceRef(
                label=ev.label,
                title=doc.title,
                url=doc.source_url,
                status=doc.status,
                updated=doc.updated.isoformat() if doc.updated else None,
            )
        )
    return tuple(refs[:3])


def _source_footer(sources: Sequence[SourceRef], language: str) -> str:
    if not sources:
        return ""
    label = "المصدر" if language == "ar" else "Source"
    if len(sources) > 1:
        label = "المصادر" if language == "ar" else "Sources"
    rendered = [
        f"<{ref.url}|{ref.title}>" if ref.url else ref.title for ref in sources
    ]
    return f"_{label}: " + " · ".join(rendered) + "_"


def _diagnostics(retrieval: RetrievalResult, grading: GradingSummary) -> dict[str, Any]:
    return {
        "retrieval": {
            "coverage": retrieval.coverage,
            "top_score": retrieval.top_score,
            "chunks": len(retrieval.evidence),
            "conflicts": list(retrieval.conflicts),
            "resolution_notes": list(retrieval.resolution_notes),
            "stale_docs": list(retrieval.stale_doc_ids),
            "query_terms": list(retrieval.query_terms),
            "matched_terms": list(retrieval.matched_terms),
        },
        "grading": {
            "available": grading.available,
            "claims": grading.total_claims,
            "supported": grading.supported,
            "partial": grading.partial,
            "unsupported": grading.unsupported,
            "contradicted": grading.contradicted,
            "support_ratio": round(grading.support_ratio, 3),
            "note": grading.note,
        },
    }
