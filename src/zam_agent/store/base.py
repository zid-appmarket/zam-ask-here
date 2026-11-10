"""Persistence contract.

Two things genuinely need durability:

1. **Event de-duplication.** Slack retries event deliveries; without a durable
   record the bot double-posts after a restart.
2. **Escalation state.** The owner must not be re-tagged for a question that is
   already waiting on them, and an owner's answer must survive until somebody
   folds it into the knowledge base.

Everything else (interaction log, knowledge gaps) is operational telemetry that
makes the knowledge base improvable.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from typing import Any, Protocol


@dataclass(frozen=True)
class EscalationRecord:
    id: int
    question_key: str
    channel_id: str
    thread_ts: str | None
    product: str | None
    owner_user_id: str
    topic: str
    question: str
    status: str
    created_at: float
    resolved_at: float | None
    resolved_by: str | None = None
    resolution_note: str | None = None


@dataclass(frozen=True)
class KnowledgeGap:
    question_key: str
    question: str
    topic: str
    product: str | None
    occurrences: int
    first_seen: float
    last_seen: float
    last_channel_id: str
    last_thread_ts: str | None
    resolved: bool
    resolved_at: float | None = None
    resolved_by: str | None = None
    resolution_note: str | None = None


class Store(Protocol):
    def setup(self) -> None: ...

    def claim_event(self, event_key: str, *, channel_id: str = "", message_ts: str = "") -> bool:
        """Atomically record ``event_key``. False means it was already seen."""

    def release_event(self, event_key: str) -> None:
        """Undo a claim so a transient failure can be retried by Slack."""

    def recent_escalation(
        self, key: str, *, channel_id: str, within_hours: int
    ) -> EscalationRecord | None: ...

    def record_escalation(
        self,
        *,
        question_key: str,
        channel_id: str,
        thread_ts: str | None,
        product: str | None,
        owner_user_id: str,
        topic: str,
        question: str,
    ) -> EscalationRecord: ...

    def resolve_escalation(self, escalation_id: int, *, note: str = "", resolved_by: str = "") -> None: ...

    def reopen_escalation(self, escalation_id: int) -> None: ...

    def escalation_for_thread(self, channel_id: str, thread_ts: str | None) -> EscalationRecord | None:
        """The most recent escalation in a thread, resolved or not."""

    def record_interaction(self, **fields: Any) -> None: ...

    def upsert_knowledge_gap(
        self,
        *,
        question_key: str,
        question: str,
        topic: str,
        product: str | None,
        channel_id: str,
        thread_ts: str | None,
    ) -> None: ...

    def knowledge_gaps(self, *, limit: int = 50, include_resolved: bool = False) -> Sequence[KnowledgeGap]: ...

    def knowledge_gap(self, question_key: str) -> KnowledgeGap | None: ...

    def resolve_knowledge_gap(self, question_key: str, *, note: str = "", resolved_by: str = "") -> None: ...

    def reopen_knowledge_gap(self, question_key: str) -> None: ...

    def stats(self) -> dict[str, Any]: ...

    def prune(self, *, older_than_days: int = 30) -> int: ...
