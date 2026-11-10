"""Closing a knowledge gap from Slack.

The loop this completes:

    employee asks ──► agent escalates ──► owner answers in the thread
                                           │
                                           └─► owner adds ✅
                                                 │
            agent captures the owner's reply, marks the gap resolved,
            and confirms in-thread ──► `scripts/report_gaps.py --draft`
            writes a ready-to-review document into knowledge/_inbox/

The captured answer is the point. Marking a gap "done" without keeping what
the human actually said would lose the only thing worth keeping.

Authorisation matters here: anyone in a public channel can add a reaction, so
only a configured owner or knowledge editor may resolve
(:meth:`EscalationConfig.may_resolve`). An unauthorised reaction is logged and
ignored -- silently, because publicly correcting a colleague for clicking an
emoji is worse than doing nothing.

This module makes no Slack calls. Thread lookups are injected, which keeps the
whole decision path testable.
"""

from __future__ import annotations

from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass
from typing import Any, Literal

from .config import AppConfig
from .language import reply_language
from .observability.logging import get_logger
from .observability.metrics import METRICS
from .security import mention, sanitize_outbound
from .store.base import EscalationRecord, Store

log = get_logger(__name__)

Outcome = Literal[
    "resolved",
    "reopened",
    "not_authorized",
    "no_escalation",
    "already_resolved",
    "not_resolved",
    "wrong_reaction",
    "disabled",
]

MAX_NOTE_CHARS = 2000

# A thread lookup: (channel_id, message_ts) -> the thread's parent ts.
ThreadLookup = Callable[[str, str], str | None]
# Thread history: (channel_id, thread_ts) -> raw Slack messages.
ThreadFetcher = Callable[[str, str], Sequence[Mapping[str, Any]]]

_CONFIRM_RESOLVED = {
    "en": (
        "Thanks {owner} — noted as confirmed. I've saved your answer so this "
        "can go into the knowledge base and I can answer it directly next time."
    ),
    "ar": (
        "شكرًا {owner} — سجّلتها كمؤكدة، وحفظت جوابك عشان يضاف لقاعدة المعلومات "
        "وأقدر أجاوب عليه مباشرة المرة الجاية."
    ),
}

_CONFIRM_RESOLVED_NO_ANSWER = {
    "en": (
        "Thanks {owner} — noted as confirmed. I didn't find an answer written in "
        "this thread, so nothing was saved for the knowledge base; add it to "
        "`knowledge/` directly if it should be reusable."
    ),
    "ar": (
        "شكرًا {owner} — سجّلتها كمؤكدة. ما لقيت جواب مكتوب في هذا الثريد، فما "
        "حفظت شي لقاعدة المعلومات — لو تبغاه يتكرر، أضفه في `knowledge/` مباشرة."
    ),
}

_CONFIRM_REOPENED = {
    "en": "Reopened — this is back on the unanswered list. No one has been re-pinged.",
    "ar": "رجّعتها لقائمة غير المجابة. ما نبّهت أحد من جديد.",
}


def _as_epoch(ts: str) -> float | None:
    """A Slack ``ts`` as a float, or None when it is not one."""

    try:
        return float(ts)
    except (TypeError, ValueError):
        return None


@dataclass(frozen=True)
class ResolutionResult:
    outcome: Outcome
    question_key: str = ""
    escalation: EscalationRecord | None = None
    captured_answer: str = ""
    reply: str = ""
    thread_ts: str | None = None
    actor_user_id: str = ""

    @property
    def should_reply(self) -> bool:
        return bool(self.reply)

    @property
    def changed_state(self) -> bool:
        return self.outcome in ("resolved", "reopened")


class ResolutionManager:
    def __init__(
        self,
        config: AppConfig,
        store: Store,
        *,
        thread_lookup: ThreadLookup | None = None,
        thread_fetcher: ThreadFetcher | None = None,
        bot_user_id: str | None = None,
    ) -> None:
        self.config = config
        self.store = store
        self.thread_lookup = thread_lookup
        self.thread_fetcher = thread_fetcher
        self.bot_user_id = bot_user_id

    # ------------------------------------------------------------------ entry

    def handle_reaction(self, event: Mapping[str, Any], *, added: bool) -> ResolutionResult:
        if not self.config.slack.enable_slack_resolution:
            return ResolutionResult(outcome="disabled")

        reaction = str(event.get("reaction") or "").strip().strip(":")
        if reaction != self.config.slack.resolve_reaction:
            return ResolutionResult(outcome="wrong_reaction")

        actor = str(event.get("user") or "")
        item = event.get("item") or {}
        channel_id = str(item.get("channel") or "")
        item_ts = str(item.get("ts") or "")
        if not channel_id or not item_ts:
            return ResolutionResult(outcome="no_escalation", actor_user_id=actor)

        thread_ts = self._thread_ts_for(channel_id, item_ts)
        escalation = self.store.escalation_for_thread(channel_id, thread_ts)
        if escalation is None:
            return ResolutionResult(
                outcome="no_escalation", actor_user_id=actor, thread_ts=thread_ts
            )

        if not self.config.escalation.may_resolve(actor):
            METRICS.incr("resolution.unauthorized")
            log.info(
                "ignoring a resolve reaction from someone who is not an owner or editor",
                extra={
                    "context": {
                        "actor": actor,
                        "channel_id": channel_id,
                        "thread_ts": thread_ts,
                        "question_key": escalation.question_key,
                    }
                },
            )
            return ResolutionResult(
                outcome="not_authorized",
                question_key=escalation.question_key,
                escalation=escalation,
                actor_user_id=actor,
                thread_ts=thread_ts,
            )

        language = reply_language(escalation.question or "")
        if added:
            return self._resolve(escalation, actor=actor, language=language, thread_ts=thread_ts)
        return self._reopen(escalation, actor=actor, language=language, thread_ts=thread_ts)

    # ----------------------------------------------------------------- actions

    def _resolve(
        self,
        escalation: EscalationRecord,
        *,
        actor: str,
        language: str,
        thread_ts: str | None,
    ) -> ResolutionResult:
        if escalation.status == "resolved":
            return ResolutionResult(
                outcome="already_resolved",
                question_key=escalation.question_key,
                escalation=escalation,
                actor_user_id=actor,
                thread_ts=thread_ts,
            )

        answer = self._capture_answer(escalation, thread_ts)
        self.store.resolve_escalation(escalation.id, note=answer, resolved_by=actor)
        self.store.resolve_knowledge_gap(escalation.question_key, note=answer, resolved_by=actor)
        METRICS.incr("resolution.resolved")

        template = _CONFIRM_RESOLVED if answer else _CONFIRM_RESOLVED_NO_ANSWER
        reply = template[language].format(owner=mention(actor))
        log.info(
            "knowledge gap resolved from Slack",
            extra={
                "context": {
                    "question_key": escalation.question_key,
                    "resolved_by": actor,
                    "captured_answer_chars": len(answer),
                    "thread_ts": thread_ts,
                }
            },
        )
        return ResolutionResult(
            outcome="resolved",
            question_key=escalation.question_key,
            escalation=escalation,
            captured_answer=answer,
            reply=reply,
            thread_ts=thread_ts,
            actor_user_id=actor,
        )

    def _reopen(
        self,
        escalation: EscalationRecord,
        *,
        actor: str,
        language: str,
        thread_ts: str | None,
    ) -> ResolutionResult:
        if escalation.status != "resolved":
            return ResolutionResult(
                outcome="not_resolved",
                question_key=escalation.question_key,
                escalation=escalation,
                actor_user_id=actor,
                thread_ts=thread_ts,
            )
        self.store.reopen_escalation(escalation.id)
        self.store.reopen_knowledge_gap(escalation.question_key)
        METRICS.incr("resolution.reopened")
        log.info(
            "knowledge gap reopened from Slack",
            extra={"context": {"question_key": escalation.question_key, "actor": actor}},
        )
        return ResolutionResult(
            outcome="reopened",
            question_key=escalation.question_key,
            escalation=escalation,
            reply=_CONFIRM_REOPENED[language],
            thread_ts=thread_ts,
            actor_user_id=actor,
        )

    # ----------------------------------------------------------------- helpers

    def _thread_ts_for(self, channel_id: str, item_ts: str) -> str | None:
        """Which thread the reacted-to message belongs to.

        The owner may react on the question, on the agent's escalation, or on
        any reply, so try the cheap case (the ts *is* the thread) before
        spending a Slack call.
        """

        if self.store.escalation_for_thread(channel_id, item_ts) is not None:
            return item_ts
        if self.thread_lookup is None:
            return item_ts
        return self.thread_lookup(channel_id, item_ts) or item_ts

    def _capture_answer(self, escalation: EscalationRecord, thread_ts: str | None) -> str:
        """The human replies in the thread, as plain text.

        Anything the agent itself wrote is skipped, as is the question that
        started the thread. The cut-off is the thread's own root timestamp
        rather than the wall-clock time the escalation was recorded: both are
        Slack timestamps, so the comparison needs no assumption about this
        process's clock agreeing with Slack's.
        """

        if self.thread_fetcher is None or not thread_ts:
            return ""
        floor = _as_epoch(thread_ts)
        if floor is None:
            floor = escalation.created_at
        try:
            messages = self.thread_fetcher(escalation.channel_id, thread_ts)
        except Exception:  # pragma: no cover - a capture failure must not block the resolve
            log.warning("could not read the thread to capture the answer", exc_info=True)
            return ""

        parts: list[str] = []
        for item in messages:
            if item.get("bot_id") or item.get("app_id"):
                continue
            user = str(item.get("user") or "")
            if self.bot_user_id and user == self.bot_user_id:
                continue
            posted_at = _as_epoch(str(item.get("ts") or ""))
            # Only what was said after the question itself.
            if posted_at is None or posted_at <= floor:
                continue
            text = str(item.get("text") or "").strip()
            if not text:
                continue
            parts.append(text)

        if not parts:
            return ""
        joined = "\n\n".join(parts)
        return sanitize_outbound(joined, max_chars=MAX_NOTE_CHARS)
