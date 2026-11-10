"""Provider-agnostic LLM interface.

The pipeline only ever calls :meth:`LLMClient.generate_json`. Keeping the
surface this small is what makes the agent testable (``FakeLLM``) and makes the
AI provider genuinely swappable.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass, field
from typing import Any, Protocol


class LLMError(RuntimeError):
    """Any failure talking to the model provider."""


class LLMTimeout(LLMError):
    """The request exceeded its deadline."""


class LLMRateLimited(LLMError):
    """Provider returned 429 after the SDK's own retries."""


class LLMRefusal(LLMError):
    """The model declined to answer (``stop_reason == "refusal"``)."""

    def __init__(self, category: str | None = None, explanation: str | None = None) -> None:
        super().__init__(f"model refused (category={category})")
        self.category = category
        self.explanation = explanation


class LLMInvalidOutput(LLMError):
    """The model returned something that is not valid JSON for the schema."""


@dataclass(frozen=True)
class LLMResult:
    data: Mapping[str, Any]
    raw_text: str
    model: str
    input_tokens: int = 0
    output_tokens: int = 0
    cache_read_tokens: int = 0
    latency_seconds: float = 0.0
    request_id: str | None = None
    metadata: Mapping[str, Any] = field(default_factory=dict)


class LLMClient(Protocol):
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
    ) -> LLMResult: ...
