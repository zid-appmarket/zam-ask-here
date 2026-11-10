"""Slack test doubles. Nothing here touches the network."""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

from slack_sdk.errors import SlackApiError

from .helpers import BOT_USER, CHANNEL


class StubResponse(dict):
    """Minimal stand-in for ``slack_sdk.web.SlackResponse``."""

    def __init__(self, data: dict[str, Any] | None = None, *, status_code: int = 200, headers: dict | None = None):
        super().__init__(data or {"ok": True})
        self.status_code = status_code
        self.headers = headers or {}

    def __bool__(self) -> bool:  # SlackApiError does `exc.response or {}`
        return True


def slack_error(code: str, *, status_code: int = 200, retry_after: str | None = None) -> SlackApiError:
    headers = {"Retry-After": retry_after} if retry_after else {}
    return SlackApiError(
        f"The request to the Slack API failed: {code}",
        StubResponse({"ok": False, "error": code}, status_code=status_code, headers=headers),
    )


class FakeSlackClient:
    """Records calls; can be scripted to fail a given method N times."""

    def __init__(
        self,
        *,
        bot_user_id: str = BOT_USER,
        thread_messages: list[dict[str, Any]] | None = None,
    ) -> None:
        self.bot_user_id = bot_user_id
        self.posted: list[dict[str, Any]] = []
        self.reactions: list[dict[str, Any]] = []
        self.calls: list[str] = []
        self.thread_messages = thread_messages or []
        self.failures: dict[str, list[SlackApiError]] = {}

    def fail_once(self, method: str, error: SlackApiError) -> FakeSlackClient:
        self.failures.setdefault(method, []).append(error)
        return self

    def _maybe_fail(self, method: str) -> None:
        self.calls.append(method)
        queue = self.failures.get(method)
        if queue:
            raise queue.pop(0)

    # -- Web API surface the agent uses ------------------------------------

    def auth_test(self, **_: Any) -> StubResponse:
        self._maybe_fail("auth_test")
        return StubResponse({"ok": True, "user_id": self.bot_user_id, "bot_id": "B0FAKEBOT1", "team": "T0FAKETEAM"})

    def chat_postMessage(self, **kwargs: Any) -> StubResponse:  # noqa: N802 - Slack's name
        self._maybe_fail("chat_postMessage")
        self.posted.append(kwargs)
        return StubResponse({"ok": True, "ts": f"{1000 + len(self.posted)}.000000"})

    def chat_getPermalink(self, **kwargs: Any) -> StubResponse:  # noqa: N802 - Slack's name
        self._maybe_fail("chat_getPermalink")
        return StubResponse(
            {
                "ok": True,
                "permalink": f"https://example.invalid/archives/{kwargs.get('channel')}/p1",
            }
        )

    def conversations_replies(self, **_: Any) -> StubResponse:
        self._maybe_fail("conversations_replies")
        return StubResponse({"ok": True, "messages": self.thread_messages})

    def reactions_add(self, **kwargs: Any) -> StubResponse:
        self._maybe_fail("reactions_add")
        self.reactions.append(kwargs)
        return StubResponse({"ok": True})


class FakeBoltApp:
    """Captures Bolt listener registration without constructing a real app."""

    def __init__(self, client: FakeSlackClient | None = None) -> None:
        self.client = client or FakeSlackClient()
        self.handlers: dict[str, list[Callable[..., Any]]] = {}

    def event(self, name: str) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
        def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
            self.handlers.setdefault(name, []).append(func)
            return func

        return decorator


def slack_message_event(
    text: str,
    *,
    channel: str = CHANNEL,
    user: str = "U0EMPLOYEE1",
    ts: str = "1762790400.000100",
    thread_ts: str | None = None,
    subtype: str | None = None,
    bot_id: str | None = None,
    event_type: str = "message",
    client_msg_id: str | None = "11111111-2222-3333-4444-555555555555",
    **extra: Any,
) -> dict[str, Any]:
    event: dict[str, Any] = {
        "type": event_type,
        "channel": channel,
        "channel_type": "channel",
        "user": user,
        "text": text,
        "ts": ts,
        "event_ts": ts,
    }
    if client_msg_id:
        event["client_msg_id"] = client_msg_id
    if thread_ts:
        event["thread_ts"] = thread_ts
    if subtype:
        event["subtype"] = subtype
    if bot_id:
        event["bot_id"] = bot_id
    event.update(extra)
    return event


def reaction_event(
    *,
    reaction: str = "white_check_mark",
    user: str = "U0OWNERZAM1",
    channel: str = CHANNEL,
    ts: str = "1762790400.000100",
    event_type: str = "reaction_added",
    item_type: str = "message",
    item_user: str = "U0BOTUSER01",
) -> dict[str, Any]:
    return {
        "type": event_type,
        "user": user,
        "reaction": reaction,
        "item_user": item_user,
        "item": {"type": item_type, "channel": channel, "ts": ts},
        "event_ts": "1762790900.000100",
    }


def slack_envelope(event: dict[str, Any], *, event_id: str = "Ev0TEST0001", retry_num: int | None = None) -> dict[str, Any]:
    body: dict[str, Any] = {
        "token": "verification-token-placeholder",
        "team_id": "T0FAKETEAM",
        "api_app_id": "A0FAKEAPP1",
        "event": event,
        "type": "event_callback",
        "event_id": event_id,
        "event_time": int(float(event.get("ts", "0") or 0)),
    }
    if retry_num is not None:
        body["retry_num"] = retry_num
        body["headers"] = {"x-slack-retry-num": [str(retry_num)]}
    return body
