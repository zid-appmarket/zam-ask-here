"""Outbound message safety.

Two separate jobs:

* **Mention control.** The agent must be the only thing that decides when a
  human gets tagged. Model output is stripped of every mention and broadcast
  form, so a document or a Slack message cannot make the bot ping a channel.
* **Escaping.** Slack mrkdwn needs ``&``, ``<`` and ``>`` escaped. Model text
  is escaped, while the ``<url|label>`` links the prompt explicitly allows are
  preserved.

Also here: the audience policy that decides which documents a channel may see.
"""

from __future__ import annotations

import re
from collections.abc import Sequence

from .config import SlackConfig
from .observability.logging import redact

MAX_SLACK_TEXT = 2900  # Slack hard limit is 3000 chars per section block.

_BROADCASTS = re.compile(r"<!(?:here|channel|everyone)(?:\|[^>]*)?>", re.IGNORECASE)
_BARE_BROADCASTS = re.compile(r"(?<![\w/])@(?:here|channel|everyone)\b", re.IGNORECASE)
_USER_MENTION = re.compile(r"<@([UWS][A-Z0-9]{2,})(?:\|[^>]*)?>")
_GROUP_MENTION = re.compile(r"<!subteam\^([A-Z0-9]+)(?:\|[^>]*)?>")
_BARE_AT = re.compile(r"(?<![\w/])@([A-Za-z][\w.\-]{1,30})")
_LINK = re.compile(r"<(https?://[^|>\s]+)(\|[^>]*)?>")
_RAW_URL = re.compile(r"(?<![<|\w])(https?://[^\s<>|]+)")


def strip_mentions(text: str) -> str:
    """Remove every way of pinging someone from model-authored text."""

    text = _BROADCASTS.sub("", text)
    text = _BARE_BROADCASTS.sub("", text)
    text = _USER_MENTION.sub("", text)
    text = _GROUP_MENTION.sub("", text)
    return _BARE_AT.sub(r"\1", text)


def escape_mrkdwn(text: str) -> str:
    """Escape Slack's three special characters, keeping allowed links intact."""

    placeholders: list[str] = []

    def stash(match: re.Match[str]) -> str:
        placeholders.append(match.group(0))
        return f"\x00LINK{len(placeholders) - 1}\x00"

    text = _LINK.sub(stash, text)
    text = _RAW_URL.sub(stash, text)
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    for idx, original in enumerate(placeholders):
        text = text.replace(f"\x00LINK{idx}\x00", original)
    return text


def sanitize_outbound(text: str, *, max_chars: int = MAX_SLACK_TEXT) -> str:
    """Make model-authored text safe to post: no pings, no secrets, bounded."""

    if not text:
        return ""
    cleaned = strip_mentions(str(text))
    cleaned = str(redact(cleaned))
    cleaned = escape_mrkdwn(cleaned)
    cleaned = re.sub(r"[ \t]+\n", "\n", cleaned)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned).strip()
    if len(cleaned) > max_chars:
        cleaned = cleaned[: max_chars - 1].rstrip() + "…"
    return cleaned


def mention(user_or_group_id: str) -> str:
    """Render a mention for a *configured* ID. Never called on model output."""

    uid = (user_or_group_id or "").strip()
    if not uid:
        return ""
    if uid.startswith("S"):  # user group
        return f"<!subteam^{uid}>"
    return f"<@{uid}>"


def allowed_audiences(channel_id: str, config: SlackConfig) -> tuple[str, ...]:
    """Which document audiences may be surfaced in this channel.

    ``all`` is always allowed. ``internal`` needs the channel to be listed in
    ``INTERNAL_CHANNEL_IDS`` (which defaults to the watched channels, since
    those are internal company channels). ``restricted`` needs the channel to
    be listed explicitly in ``RESTRICTED_CHANNEL_IDS`` -- this is the knob that
    keeps confidential documents out of a company-wide channel.
    """

    audiences = ["all"]
    if channel_id in config.internal_channel_ids:
        audiences.append("internal")
    if channel_id in config.restricted_channel_ids:
        audiences.append("restricted")
    return tuple(audiences)


def summarize_for_owner(question: str, *, max_chars: int = 400) -> str:
    """Quote an employee's question back to the owner, safely."""

    text = sanitize_outbound(question, max_chars=max_chars)
    return "\n".join(f"> {line}" for line in text.splitlines() if line.strip()) or "> (empty message)"


def contains_mention(text: str, user_ids: Sequence[str]) -> bool:
    return any(mention(uid) in text for uid in user_ids if uid)
