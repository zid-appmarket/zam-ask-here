"""Pushing a thread answer to the whole channel on 📣.

By default an answer stays in the thread of the question that prompted it,
which keeps the channel readable. When an answer is worth everyone's attention,
a named approver reacts 📣 (``:mega:``) on it and the agent re-posts it at
channel level with the original question for context and a link back.

Why a person decides rather than a signal: every automatic proxy for "this was
useful" is a bad one. A 👍 means one reader liked it, thread length usually
means the answer was unclear, and repeat asks only arrive after several people
were already confused. One deliberate click from someone who owns the channel
beats all of them.

Authorisation is the point of this module. Reactions are public and anyone can
add one, so :meth:`SlackConfig.may_broadcast` restricts it to
``BROADCAST_APPROVER_USER_IDS`` and fails closed when that list is empty.
"""

from __future__ import annotations

from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass
from typing import Any, Literal

from .config import AppConfig
from .language import reply_language
from .observability.logging import get_logger
from .observability.metrics import METRICS
from .security import sanitize_outbound

log = get_logger(__name__)

Outcome = Literal[
    "broadcast",
    "not_authorized",
    "wrong_reaction",
    "not_an_agent_message",
    "no_message",
    "already_broadcast",
    "disabled",
    "removal_ignored",
]

MAX_QUOTE_CHARS = 300
MAX_ANSWER_CHARS = 2200

ThreadFetcher = Callable[[str, str], Sequence[Mapping[str, Any]]]
PermalinkFetcher = Callable[[str, str], str | None]

_HEADER = {
    "en": "*Worth sharing* — from <#{channel}>",
    "ar": "*يستاهل المشاركة* — من <#{channel}>",
}
_THREAD_LINK = {"en": "See the thread", "ar": "شوف الثريد"}


@dataclass(frozen=True)
class BroadcastResult:
    outcome: Outcome
    text: str = ""
    channel_id: str = ""
    thread_ts: str | None = None
    source_ts: str = ""
    actor_user_id: str = ""

    @property
    def should_post(self) -> bool:
        return self.outcome == "broadcast" and bool(self.text)


class BroadcastManager:
    def __init__(
        self,
        config: AppConfig,
        *,
        thread_fetcher: ThreadFetcher | None = None,
        permalink_fetcher: PermalinkFetcher | None = None,
        bot_user_id: str | None = None,
    ) -> None:
        self.config = config
        self.thread_fetcher = thread_fetcher
        self.permalink_fetcher = permalink_fetcher
        self.bot_user_id = bot_user_id

    def handle_reaction(self, event: Mapping[str, Any], *, added: bool) -> BroadcastResult:
        slack = self.config.slack
        if not slack.enable_broadcast:
            return BroadcastResult(outcome="disabled")

        reaction = str(event.get("reaction") or "").strip().strip(":")
        if reaction != slack.broadcast_reaction:
            return BroadcastResult(outcome="wrong_reaction")

        # Removing 📣 cannot un-send a channel message, so it does nothing.
        if not added:
            return BroadcastResult(outcome="removal_ignored")

        actor = str(event.get("user") or "")
        item = event.get("item") or {}
        channel_id = str(item.get("channel") or "")
        source_ts = str(item.get("ts") or "")
        if not channel_id or not source_ts:
            return BroadcastResult(outcome="no_message", actor_user_id=actor)

        if not slack.may_broadcast(actor):
            METRICS.incr("broadcast.unauthorized")
            log.info(
                "ignoring a broadcast reaction from someone who is not an approver",
                extra={"context": {"actor": actor, "channel_id": channel_id, "ts": source_ts}},
            )
            return BroadcastResult(
                outcome="not_authorized",
                channel_id=channel_id,
                source_ts=source_ts,
                actor_user_id=actor,
            )

        if self.thread_fetcher is None:
            return BroadcastResult(outcome="no_message", actor_user_id=actor)
        messages = list(self.thread_fetcher(channel_id, source_ts))
        if not messages:
            return BroadcastResult(outcome="no_message", actor_user_id=actor)

        answer = next((m for m in messages if str(m.get("ts")) == source_ts), None)
        if answer is None or not self._is_agent_message(answer):
            # Only the agent's own answers get amplified: broadcasting an
            # employee's message would put words in their mouth at channel level.
            return BroadcastResult(
                outcome="not_an_agent_message",
                channel_id=channel_id,
                source_ts=source_ts,
                actor_user_id=actor,
            )

        root = messages[0]
        thread_ts = str(answer.get("thread_ts") or root.get("ts") or source_ts)
        question = str(root.get("text") or "")
        text = self._render(
            channel_id=channel_id,
            question=question,
            answer=str(answer.get("text") or ""),
            thread_ts=thread_ts,
        )
        if not text:
            return BroadcastResult(
                outcome="no_message", channel_id=channel_id, source_ts=source_ts, actor_user_id=actor
            )

        METRICS.incr("broadcast.posted")
        log.info(
            "answer broadcast to the channel",
            extra={
                "context": {
                    "actor": actor,
                    "channel_id": channel_id,
                    "thread_ts": thread_ts,
                    "source_ts": source_ts,
                }
            },
        )
        return BroadcastResult(
            outcome="broadcast",
            text=text,
            channel_id=channel_id,
            thread_ts=thread_ts,
            source_ts=source_ts,
            actor_user_id=actor,
        )

    # ----------------------------------------------------------------- helpers

    def _is_agent_message(self, message: Mapping[str, Any]) -> bool:
        if message.get("bot_id") or message.get("app_id"):
            return True
        return bool(self.bot_user_id) and message.get("user") == self.bot_user_id

    def _render(self, *, channel_id: str, question: str, answer: str, thread_ts: str | None) -> str:
        body = sanitize_outbound(answer, max_chars=MAX_ANSWER_CHARS)
        if not body:
            return ""
        language = reply_language(question or answer)
        lines = [_HEADER[language].format(channel=channel_id)]
        quoted = sanitize_outbound(question, max_chars=MAX_QUOTE_CHARS)
        if quoted:
            lines.extend(f"> {line}" for line in quoted.splitlines() if line.strip())
        lines.append(body)
        permalink = (
            self.permalink_fetcher(channel_id, thread_ts)
            if self.permalink_fetcher and thread_ts
            else None
        )
        if permalink:
            lines.append(f"<{permalink}|{_THREAD_LINK[language]}>")
        return "\n".join(lines)
