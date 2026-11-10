"""Which Slack events the agent is allowed to act on.

This is the first and cheapest line of defence against the classic failure
modes: replying to itself, replying to another bot, looping inside its own
thread, and acting on edits/joins/deletions.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any

from ..config import SlackConfig

# Subtypes that are not a human typing a new message.
IGNORED_SUBTYPES: frozenset[str] = frozenset(
    {
        "bot_message",
        "message_changed",
        "message_deleted",
        "message_replied",
        "thread_broadcast",
        "channel_join",
        "channel_leave",
        "channel_topic",
        "channel_purpose",
        "channel_name",
        "channel_archive",
        "channel_unarchive",
        "group_join",
        "group_leave",
        "pinned_item",
        "unpinned_item",
        "file_comment",
        "reminder_add",
        "tombstone",
        "huddle_thread",
        "bot_add",
        "bot_remove",
        "me_message",
        "ekm_access_denied",
    }
)


@dataclass(frozen=True)
class FilterDecision:
    handle: bool
    reason: str = ""


def event_key(event: Mapping[str, Any], envelope_event_id: str | None = None) -> str:
    """Stable de-duplication key.

    Slack's ``event_id`` is the right key for a retried delivery, but a retry
    that arrives through a different path (or after a redeploy that lost the
    envelope) still carries the same channel + ts, so fall back to that.
    """

    if envelope_event_id:
        return f"evt:{envelope_event_id}"
    client_msg_id = event.get("client_msg_id")
    if client_msg_id:
        return f"cmid:{client_msg_id}"
    return f"msg:{event.get('channel', '')}:{event.get('ts', '')}"


def should_handle(
    event: Mapping[str, Any],
    *,
    config: SlackConfig,
    bot_user_id: str | None,
    bot_id: str | None = None,
) -> FilterDecision:
    if not isinstance(event, Mapping):
        return FilterDecision(False, "not_an_event")

    if event.get("type") not in ("message", "app_mention"):
        return FilterDecision(False, f"unsupported_event_type:{event.get('type')}")

    subtype = event.get("subtype")
    if subtype in IGNORED_SUBTYPES:
        return FilterDecision(False, f"ignored_subtype:{subtype}")
    if subtype == "file_share":
        pass  # a human sharing a file can still ask a question in the text
    elif subtype:
        return FilterDecision(False, f"unknown_subtype:{subtype}")

    # Never act on anything a bot wrote -- including ourselves.
    if event.get("bot_id"):
        return FilterDecision(False, "bot_message")
    if event.get("app_id"):
        return FilterDecision(False, "app_message")
    if event.get("user_profile", {}).get("is_bot") if isinstance(event.get("user_profile"), Mapping) else False:
        return FilterDecision(False, "bot_profile")

    user = event.get("user")
    if not user:
        return FilterDecision(False, "no_user")
    if bot_user_id and user == bot_user_id:
        return FilterDecision(False, "self_message")
    if bot_id and event.get("bot_id") == bot_id:
        return FilterDecision(False, "self_bot_id")

    channel = event.get("channel", "")
    if not config.is_watched_channel(channel):
        return FilterDecision(False, "channel_not_watched")

    if event.get("channel_type") not in (None, "channel", "group"):
        return FilterDecision(False, f"channel_type:{event.get('channel_type')}")

    if event.get("hidden"):
        return FilterDecision(False, "hidden_message")

    text = str(event.get("text") or "").strip()
    if not text:
        return FilterDecision(False, "empty_text")

    return FilterDecision(True)


def should_handle_reaction(
    event: Mapping[str, Any],
    *,
    config: SlackConfig,
    bot_user_id: str | None,
) -> FilterDecision:
    """Reactions the agent may act on (gap resolution).

    Only a reaction on a *message* in a watched channel, added by a human who
    is not the agent. Authorisation (owner / knowledge editor) is a separate
    check in :mod:`zam_agent.resolution`.
    """

    if not isinstance(event, Mapping):
        return FilterDecision(False, "not_an_event")
    if event.get("type") not in ("reaction_added", "reaction_removed"):
        return FilterDecision(False, f"unsupported_event_type:{event.get('type')}")

    item = event.get("item") or {}
    if not isinstance(item, Mapping) or item.get("type") != "message":
        return FilterDecision(False, f"reaction_on:{(item or {}).get('type', 'unknown')}")

    user = str(event.get("user") or "")
    if not user:
        return FilterDecision(False, "no_user")
    if bot_user_id and user == bot_user_id:
        return FilterDecision(False, "self_reaction")

    channel = str(item.get("channel") or "")
    if not config.is_watched_channel(channel):
        return FilterDecision(False, "channel_not_watched")
    if not item.get("ts"):
        return FilterDecision(False, "no_message_ts")

    return FilterDecision(True)


def reaction_event_key(event: Mapping[str, Any], envelope_event_id: str | None = None) -> str:
    """De-duplication key for a reaction event."""

    if envelope_event_id:
        return f"evt:{envelope_event_id}"
    item = event.get("item") or {}
    return (
        f"rxn:{event.get('type', '')}:{event.get('reaction', '')}:"
        f"{event.get('user', '')}:{item.get('channel', '')}:{item.get('ts', '')}"
    )


def is_directly_addressed(event: Mapping[str, Any], bot_user_id: str | None) -> bool:
    if event.get("type") == "app_mention":
        return True
    if not bot_user_id:
        return False
    return f"<@{bot_user_id}>" in str(event.get("text") or "")


def strip_bot_mention(text: str, bot_user_id: str | None) -> str:
    if not bot_user_id:
        return text.strip()
    return text.replace(f"<@{bot_user_id}>", " ").strip()
