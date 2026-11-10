"""Structured logging with secret redaction.

Nothing in this project writes a token, signing secret or API key to a log.
``RedactingFilter`` is a belt-and-braces second line of defence: even if a
third-party library (or a stack trace) carries a credential into a log record,
the pattern list below masks it before the record is formatted.
"""

from __future__ import annotations

import json
import logging
import re
import sys
from collections.abc import Mapping
from typing import Any

# Slack bot/user/app/refresh tokens, Anthropic keys, Notion keys, bearer headers.
_SECRET_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(r"xox[abposr]-[A-Za-z0-9-]{8,}"),
    re.compile(r"xapp-[A-Za-z0-9-]{8,}"),
    re.compile(r"sk-ant-[A-Za-z0-9_\-]{8,}"),
    re.compile(r"secret_[A-Za-z0-9]{20,}"),
    re.compile(r"ntn_[A-Za-z0-9]{20,}"),
    re.compile(r"(?i)(bearer)\s+[A-Za-z0-9._\-]{12,}"),
    re.compile(r"(?i)\b(api[_-]?key|signing[_-]?secret|client[_-]?secret|password|token)\b\s*[:=]\s*\S+"),
)

_REDACTED = "«redacted»"

_SENSITIVE_KEYS = {
    "token",
    "bot_token",
    "app_token",
    "api_key",
    "anthropic_api_key",
    "signing_secret",
    "authorization",
    "password",
    "secret",
    "notion_api_key",
}


def redact(value: Any) -> Any:
    """Mask anything that looks like a credential, recursively."""

    if isinstance(value, str):
        out = value
        for pattern in _SECRET_PATTERNS:
            out = pattern.sub(_REDACTED, out)
        return out
    if isinstance(value, Mapping):
        return {
            key: (_REDACTED if str(key).lower() in _SENSITIVE_KEYS else redact(val))
            for key, val in value.items()
        }
    if isinstance(value, (list, tuple)):
        return [redact(item) for item in value]
    return value


class RedactingFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:  # noqa: A003
        record.msg = redact(record.msg)
        if isinstance(record.args, dict):
            record.args = redact(record.args)
        elif record.args:
            record.args = tuple(redact(arg) for arg in record.args)
        extra = getattr(record, "context", None)
        if extra is not None:
            record.context = redact(extra)
        return True


_RESERVED = set(
    logging.LogRecord("", 0, "", 0, "", None, None).__dict__
) | {"message", "asctime", "taskName"}


class JsonFormatter(logging.Formatter):
    """One JSON object per line -- friendly to Datadog / CloudWatch / Loki."""

    def format(self, record: logging.LogRecord) -> str:
        payload: dict[str, Any] = {
            "ts": self.formatTime(record, "%Y-%m-%dT%H:%M:%S%z"),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }
        context = getattr(record, "context", None)
        if isinstance(context, Mapping):
            payload["context"] = dict(context)
        for key, value in record.__dict__.items():
            if key not in _RESERVED and key not in ("context",):
                payload[key] = redact(value)
        if record.exc_info:
            payload["exception"] = redact(self.formatException(record.exc_info))
        return json.dumps(payload, ensure_ascii=False, default=str)


def configure_logging(level: str = "INFO", fmt: str = "json") -> None:
    handler = logging.StreamHandler(stream=sys.stdout)
    handler.addFilter(RedactingFilter())
    if fmt == "json":
        handler.setFormatter(JsonFormatter())
    else:
        handler.setFormatter(
            logging.Formatter("%(asctime)s %(levelname)-7s %(name)s :: %(message)s")
        )
    root = logging.getLogger()
    for existing in list(root.handlers):
        root.removeHandler(existing)
    root.addHandler(handler)
    root.setLevel(getattr(logging, level.upper(), logging.INFO))
    # slack_bolt is chatty at DEBUG and can echo request bodies.
    logging.getLogger("slack_bolt").setLevel(max(root.level, logging.INFO))
    logging.getLogger("slack_sdk").setLevel(max(root.level, logging.INFO))
    logging.getLogger("urllib3").setLevel(logging.WARNING)


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)
