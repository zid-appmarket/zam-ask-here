"""Scripted LLM double for tests and ``DRY_RUN`` smoke runs.

Responses are keyed by ``purpose`` (``classify`` / ``answer`` / ``grade``),
which the pipeline passes through the message metadata. Anything unscripted
raises, so a test can never pass by accident on a stub answer.
"""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Callable, Mapping, Sequence
from typing import Any

from .base import LLMClient, LLMError, LLMResult

Responder = Callable[[Sequence[Mapping[str, Any]], Mapping[str, Any]], Mapping[str, Any]]


class FakeLLM(LLMClient):
    def __init__(self, responses: Mapping[str, Any] | None = None) -> None:
        self.responses: dict[str, Any] = dict(responses or {})
        self.calls: list[dict[str, Any]] = []
        self.failures: dict[str, Exception] = {}
        self.call_counts: dict[str, int] = defaultdict(int)

    def script(self, purpose: str, value: Mapping[str, Any] | Responder) -> FakeLLM:
        self.responses[purpose] = value
        return self

    def fail(self, purpose: str, error: Exception) -> FakeLLM:
        self.failures[purpose] = error
        return self

    def generate_json(
        self,
        *,
        system: str,
        messages: Sequence[Mapping[str, Any]],
        schema: Mapping[str, Any],
        model: str | None = None,
        effort: str | None = None,
        max_tokens: int | None = None,
        cache_system: bool = True,
    ) -> LLMResult:
        purpose = _purpose_from_schema(schema)
        self.call_counts[purpose] += 1
        self.calls.append(
            {
                "purpose": purpose,
                "system": system,
                "messages": list(messages),
                "schema": schema,
                "model": model,
                "effort": effort,
            }
        )
        if purpose in self.failures:
            raise self.failures[purpose]
        if purpose not in self.responses:
            raise LLMError(f"FakeLLM has no scripted response for purpose {purpose!r}")
        value = self.responses[purpose]
        data = value(messages, schema) if callable(value) else value
        return LLMResult(data=dict(data), raw_text="", model=model or "fake-model")


def _purpose_from_schema(schema: Mapping[str, Any]) -> str:
    return str(schema.get("title") or "unknown")
