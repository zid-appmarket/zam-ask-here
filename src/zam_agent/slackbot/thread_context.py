"""Thread history for follow-up questions.

A follow-up like "and for paid themes?" is meaningless alone. The agent reads
the thread it is replying in, renders it compactly, and passes it to the
classifier (which rewrites it into a standalone retrieval query) and to the
answer step.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from typing import Any

from ..observability.logging import get_logger
from ..security import sanitize_outbound
from .retry import SlackCallFailed, call_with_retry

log = get_logger(__name__)

MAX_MESSAGE_CHARS = 600


@dataclass(frozen=True)
class ThreadContext:
    rendered: str
    bot_participated: bool
    message_count: int


EMPTY = ThreadContext(rendered="", bot_participated=False, message_count=0)


def fetch_thread_context(
    client: Any,
    *,
    channel_id: str,
    thread_ts: str,
    current_ts: str,
    bot_user_id: str | None,
    limit: int = 12,
) -> ThreadContext:
    try:
        response = call_with_retry(
            client.conversations_replies,
            operation="conversations.replies",
            channel=channel_id,
            ts=thread_ts,
            limit=max(2, min(limit * 2, 100)),
            inclusive=True,
        )
    except SlackCallFailed as exc:
        # Context is a nice-to-have; never fail the reply because of it.
        log.warning(
            "could not read thread context",
            extra={"context": {"error": exc.error, "channel_id": channel_id}},
        )
        return EMPTY

    messages: Sequence[Mapping[str, Any]] = response.get("messages") or []
    return render_thread(
        messages,
        current_ts=current_ts,
        bot_user_id=bot_user_id,
        limit=limit,
    )


def render_thread(
    messages: Sequence[Mapping[str, Any]],
    *,
    current_ts: str,
    bot_user_id: str | None,
    limit: int = 12,
) -> ThreadContext:
    prior = [m for m in messages if str(m.get("ts")) != str(current_ts)]
    prior = prior[-limit:]

    bot_participated = any(
        (bot_user_id and m.get("user") == bot_user_id) or m.get("bot_id") for m in messages
    )

    lines: list[str] = []
    for item in prior:
        text = str(item.get("text") or "").strip()
        if not text:
            continue
        is_agent = bool(item.get("bot_id")) or (bot_user_id and item.get("user") == bot_user_id)
        speaker = "agent" if is_agent else f"employee:{item.get('user', 'unknown')}"
        snippet = sanitize_outbound(text, max_chars=MAX_MESSAGE_CHARS)
        lines.append(f"[{speaker}] {snippet}")

    return ThreadContext(
        rendered="\n".join(lines),
        bot_participated=bool(bot_participated),
        message_count=len(prior),
    )
