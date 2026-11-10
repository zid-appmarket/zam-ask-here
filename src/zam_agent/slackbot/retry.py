"""Slack Web API calls with rate-limit and transient-failure handling.

``slack_sdk`` does not retry by default. Slack returns HTTP 429 with a
``Retry-After`` header when rate limited (chat.postMessage is per-channel
~1 message/second), and transient 5xx happens during Slack incidents.
"""

from __future__ import annotations

import random
import time
from collections.abc import Callable
from typing import Any, TypeVar

from slack_sdk.errors import SlackApiError, SlackClientError

from ..observability.logging import get_logger
from ..observability.metrics import METRICS

log = get_logger(__name__)

T = TypeVar("T")

# Slack errors that will never succeed on retry -- fail fast and loudly.
FATAL_SLACK_ERRORS: frozenset[str] = frozenset(
    {
        "invalid_auth",
        "account_inactive",
        "token_revoked",
        "token_expired",
        "no_permission",
        "missing_scope",
        "channel_not_found",
        "not_in_channel",
        "is_archived",
        "msg_too_long",
        "invalid_blocks",
        "invalid_blocks_format",
        "restricted_action",
        "ekm_access_denied",
        "team_access_not_granted",
    }
)

TRANSIENT_SLACK_ERRORS: frozenset[str] = frozenset(
    {"ratelimited", "service_unavailable", "internal_error", "fatal_error", "request_timeout"}
)


class SlackCallFailed(RuntimeError):
    def __init__(self, operation: str, error: str, *, fatal: bool) -> None:
        super().__init__(f"Slack {operation} failed: {error}")
        self.operation = operation
        self.error = error
        self.fatal = fatal


def call_with_retry(
    func: Callable[..., T],
    *args: Any,
    operation: str = "slack_call",
    max_attempts: int = 4,
    base_delay: float = 1.0,
    max_delay: float = 30.0,
    sleep: Callable[[float], None] = time.sleep,
    **kwargs: Any,
) -> T:
    last_error = "unknown"
    for attempt in range(1, max_attempts + 1):
        try:
            return func(*args, **kwargs)
        except SlackApiError as exc:
            error_code = str((exc.response or {}).get("error") or "unknown")
            status = getattr(exc.response, "status_code", None)
            last_error = error_code

            if error_code in FATAL_SLACK_ERRORS:
                METRICS.incr(f"slack.fatal.{error_code}")
                log.error(
                    "Slack call cannot succeed -- check app configuration",
                    extra={"context": {"operation": operation, "error": error_code, "status": status}},
                )
                raise SlackCallFailed(operation, error_code, fatal=True) from exc

            retryable = error_code in TRANSIENT_SLACK_ERRORS or (status is not None and status >= 500)
            if not retryable:
                METRICS.incr(f"slack.error.{error_code}")
                raise SlackCallFailed(operation, error_code, fatal=False) from exc

            if attempt == max_attempts:
                break

            if error_code == "ratelimited" or status == 429:
                METRICS.incr("slack.ratelimited")
                retry_after = _retry_after(exc, default=base_delay * attempt)
                delay = min(retry_after, max_delay)
            else:
                delay = min(base_delay * (2 ** (attempt - 1)) + random.uniform(0, 0.5), max_delay)

            log.warning(
                "retrying Slack call",
                extra={
                    "context": {
                        "operation": operation,
                        "error": error_code,
                        "attempt": attempt,
                        "sleep_seconds": round(delay, 2),
                    }
                },
            )
            sleep(delay)
        except SlackClientError as exc:
            last_error = type(exc).__name__
            if attempt == max_attempts:
                break
            delay = min(base_delay * (2 ** (attempt - 1)) + random.uniform(0, 0.5), max_delay)
            log.warning(
                "retrying Slack call after client error",
                extra={"context": {"operation": operation, "error": last_error, "attempt": attempt}},
            )
            sleep(delay)

    METRICS.incr("slack.exhausted_retries")
    raise SlackCallFailed(operation, last_error, fatal=False)


def _retry_after(exc: SlackApiError, *, default: float) -> float:
    headers = getattr(exc.response, "headers", None) or {}
    raw = headers.get("Retry-After") or headers.get("retry-after")
    if raw is None:
        return max(1.0, default)
    try:
        return max(1.0, float(str(raw)))
    except (TypeError, ValueError):
        return max(1.0, default)
