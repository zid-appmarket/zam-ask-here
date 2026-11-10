"""Human hand-off: who to tag, what to say, and when to stay quiet.

Rules implemented here:

* The owner is picked per product (ZAM / Theme Market / default).
* The owner is tagged with a **configured Slack ID**, never a guessed name.
* The same question is not re-escalated inside the cooldown window; the agent
  replies without a ping and points at the open thread instead.
* The escalation message always says *what* needs verifying, so the human can
  answer without reading the whole thread.
* Every escalation is logged as a knowledge gap so the answer can be added to
  the knowledge base afterwards.
"""

from __future__ import annotations

import time
from collections.abc import Sequence
from dataclasses import dataclass
from typing import Literal

from .config import EscalationConfig
from .security import mention, sanitize_outbound, summarize_for_owner
from .store.base import EscalationRecord, Store
from .store.sqlite_store import question_key

Lang = Literal["ar", "en"]

# The wording the product spec asked for, kept verbatim as the opening line.
_LEAD_IN: dict[Lang, str] = {
    "ar": (
        "ما عندي معلومة مؤكدة كفاية للإجابة على هذا الاستفسار، "
        "وما أبغى أعطيك معلومة غير دقيقة."
    ),
    "en": (
        "I'm unable to verify this answer from the available sources, "
        "and I don't want to provide inaccurate information."
    ),
}

_ASK: dict[Lang, str] = {
    "ar": "ممكن تتأكد لنا من النقطة هذي؟",
    "en": ", could you please confirm this?",
}

_NEEDS_LABEL: dict[Lang, str] = {
    "ar": "*اللي يحتاج تأكيد:*",
    "en": "*What needs confirming:*",
}

_PARTIAL_LEAD: dict[Lang, str] = {
    "ar": "هذا اللي أقدر أأكده من المصادر المعتمدة، والباقي يحتاج تأكيد:",
    "en": "Here is what I can confirm from the approved sources; the rest needs confirming:",
}

_ALREADY_FLAGGED: dict[Lang, str] = {
    "ar": "هذا الاستفسار مرفوع مسبقًا وننتظر التأكيد — ما ودي أكرر التنبيه.",
    "en": "This one is already with the owner and we're waiting on confirmation — not re-pinging.",
}

_APPROVAL_NEEDED: dict[Lang, str] = {
    "ar": "هذا الطلب يحتاج موافقة بشرية، ما أقدر أعتمده من طرفي.",
    "en": "This request needs a human decision; I can't approve it myself.",
}

_RESTRICTED: dict[Lang, str] = {
    "ar": "هذا الاستفسار يمس معلومات قد تكون مقيّدة، فما أقدر أجاوب عليه في قناة عامة.",
    "en": "This touches information that may be restricted, so I can't answer it in a public channel.",
}

_OWNER_HEADER: dict[Lang, str] = {
    "ar": "استفسار يحتاج تأكيدك",
    "en": "A question needs your confirmation",
}


@dataclass(frozen=True)
class EscalationPlan:
    text: str
    owner_user_id: str
    tagged: bool
    record: EscalationRecord | None
    question_key: str
    suppressed_reason: str = ""


class EscalationManager:
    def __init__(self, config: EscalationConfig, store: Store) -> None:
        self.config = config
        self.store = store

    def owner_for(self, product: str | None) -> str:
        return self.config.owner_for(product)

    def build(
        self,
        *,
        question: str,
        language: Lang,
        product: str | None,
        channel_id: str,
        thread_ts: str | None,
        topic: str,
        reasons: Sequence[str],
        summary: str = "",
        partial_answer: str = "",
        source_lines: Sequence[str] = (),
        requires_human_approval: bool = False,
        restricted: bool = False,
    ) -> EscalationPlan:
        key = question_key(question, product)
        owner = self.owner_for(product)

        existing = self.store.recent_escalation(
            key, channel_id=channel_id, within_hours=self.config.cooldown_hours
        )
        if existing is not None:
            return EscalationPlan(
                text=_already_flagged_text(language, existing),
                owner_user_id=owner,
                tagged=False,
                record=existing,
                question_key=key,
                suppressed_reason="duplicate within cooldown",
            )

        lines: list[str] = []
        if requires_human_approval:
            lines.append(_APPROVAL_NEEDED[language])
        elif restricted:
            lines.append(_RESTRICTED[language])
        elif partial_answer:
            lines.append(_PARTIAL_LEAD[language])
            lines.append(sanitize_outbound(partial_answer, max_chars=900))
        else:
            lines.append(_LEAD_IN[language])

        tag = mention(owner)
        if language == "ar":
            lines.append(f"{tag} {_ASK['ar']}")
        else:
            lines.append(f"{tag}{_ASK['en']}")

        detail = [sanitize_outbound(reason, max_chars=220) for reason in reasons[:3] if str(reason).strip()]
        if detail:
            lines.append(_NEEDS_LABEL[language])
            lines.extend(f"• {item}" for item in detail)
        elif summary:
            lines.append(f"_{sanitize_outbound(summary, max_chars=220)}_")

        if source_lines:
            lines.append("")
            lines.extend(source_lines)

        record = self.store.record_escalation(
            question_key=key,
            channel_id=channel_id,
            thread_ts=thread_ts,
            product=product,
            owner_user_id=owner,
            topic=topic,
            question=question[:1000],
        )
        self.store.upsert_knowledge_gap(
            question_key=key,
            question=question[:1000],
            topic=topic,
            product=product,
            channel_id=channel_id,
            thread_ts=thread_ts,
        )
        return EscalationPlan(
            text="\n".join(line for line in lines if line is not None),
            owner_user_id=owner,
            tagged=True,
            record=record,
            question_key=key,
        )

    def owner_context_message(
        self,
        *,
        question: str,
        asker_user_id: str,
        channel_id: str,
        permalink: str | None,
        reasons: Sequence[str],
        product: str | None,
        language: Lang = "en",
    ) -> str:
        """Context block for the owner, posted in-thread under the ping."""

        lines = [
            f"*{_OWNER_HEADER[language]}* — {product or 'general'}",
            summarize_for_owner(question),
            f"Asked by {mention(asker_user_id)} in <#{channel_id}>" if asker_user_id else f"In <#{channel_id}>",
        ]
        if permalink:
            lines.append(f"<{permalink}|Open the message>")
        detail = [sanitize_outbound(r, max_chars=220) for r in reasons[:4] if str(r).strip()]
        if detail:
            lines.append("*Why the agent did not answer:*")
            lines.extend(f"• {item}" for item in detail)
        lines.append(
            "_Reply in this thread with the correct answer; add it to the knowledge base "
            "so the agent can answer it next time (see `scripts/report_gaps.py`)._"
        )
        return "\n".join(lines)


def _already_flagged_text(language: Lang, existing: EscalationRecord) -> str:
    """Acknowledge a repeat ask without pinging the owner again."""

    hours = max(0, int((time.time() - existing.created_at) // 3600))
    base = _ALREADY_FLAGGED[language]
    if hours < 1:
        return base
    suffix = f" (مرفوع قبل {hours} ساعة)" if language == "ar" else f" (raised {hours}h ago)"
    return base + suffix
