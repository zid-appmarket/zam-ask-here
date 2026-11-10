"""Claude-backed implementation of :class:`~zam_agent.llm.base.LLMClient`.

Design notes that matter in production:

* **Structured outputs, not prose parsing.** Every call uses
  ``output_config.format`` with a JSON Schema, so the pipeline gets a typed
  object instead of regex-scraping a paragraph.
* **Prompt caching on the system prompt.** The system prompt is a frozen
  string; the volatile parts (the question, the retrieved evidence) go in the
  user turn, after the cache breakpoint.
* **Refusal fallbacks are on by default.** A safety decline on a support
  question would otherwise silently drop the reply.
* **No ``temperature``/``top_p``.** Those are rejected by current models.
"""

from __future__ import annotations

import json
import time
from collections.abc import Mapping, Sequence
from typing import Any

import anthropic

from ..config import LLMConfig
from ..observability.logging import get_logger
from ..observability.metrics import METRICS
from .base import (
    LLMClient,
    LLMError,
    LLMInvalidOutput,
    LLMRateLimited,
    LLMRefusal,
    LLMResult,
    LLMTimeout,
)

log = get_logger(__name__)

REFUSAL_FALLBACK_BETA = "server-side-fallback-2026-07-01"


class AnthropicLLM(LLMClient):
    def __init__(self, config: LLMConfig, client: Any | None = None) -> None:
        self.config = config
        self._client = client or anthropic.Anthropic(
            api_key=config.api_key,
            timeout=config.timeout_seconds,
            max_retries=config.max_retries,
        )

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
        chosen_model = model or self.config.model
        system_blocks: list[dict[str, Any]] = [{"type": "text", "text": system}]
        if cache_system:
            # Caches the frozen instructions; the question/evidence sit after it.
            system_blocks[0]["cache_control"] = {"type": "ephemeral"}

        params: dict[str, Any] = {
            "model": chosen_model,
            "max_tokens": max_tokens or self.config.max_tokens,
            "system": system_blocks,
            "messages": list(messages),
            "output_config": {
                "effort": effort or self.config.effort,
                "format": {"type": "json_schema", "schema": dict(schema)},
            },
        }

        started = time.perf_counter()
        try:
            if self.config.enable_refusal_fallback:
                response = self._client.beta.messages.create(
                    betas=[REFUSAL_FALLBACK_BETA], fallbacks="default", **params
                )
            else:
                response = self._client.messages.create(**params)
        except anthropic.APITimeoutError as exc:
            METRICS.incr("llm.timeout")
            raise LLMTimeout(str(exc)) from exc
        except anthropic.RateLimitError as exc:
            METRICS.incr("llm.rate_limited")
            raise LLMRateLimited(str(exc)) from exc
        except anthropic.APIStatusError as exc:
            METRICS.incr("llm.api_error")
            # Never surface the provider body: it echoes the prompt.
            raise LLMError(f"Claude API error (HTTP {exc.status_code})") from exc
        except anthropic.APIConnectionError as exc:
            METRICS.incr("llm.connection_error")
            raise LLMError(f"could not reach the Claude API: {type(exc).__name__}") from exc

        latency = time.perf_counter() - started
        METRICS.observe("llm.latency_seconds", latency)

        if getattr(response, "stop_reason", None) == "refusal":
            details = getattr(response, "stop_details", None)
            METRICS.incr("llm.refusal")
            raise LLMRefusal(
                category=getattr(details, "category", None),
                explanation=getattr(details, "explanation", None),
            )

        text = _first_text(response)
        if not text:
            raise LLMInvalidOutput("model returned no text block")
        try:
            data = json.loads(text)
        except json.JSONDecodeError as exc:
            raise LLMInvalidOutput(f"model output was not valid JSON: {exc}") from exc
        if not isinstance(data, dict):
            raise LLMInvalidOutput("model output was not a JSON object")

        usage = getattr(response, "usage", None)
        result = LLMResult(
            data=data,
            raw_text=text,
            model=getattr(response, "model", chosen_model),
            input_tokens=getattr(usage, "input_tokens", 0) or 0,
            output_tokens=getattr(usage, "output_tokens", 0) or 0,
            cache_read_tokens=getattr(usage, "cache_read_input_tokens", 0) or 0,
            latency_seconds=latency,
            request_id=getattr(response, "_request_id", None),
            metadata={"stop_reason": getattr(response, "stop_reason", None)},
        )
        METRICS.incr("llm.calls")
        METRICS.incr("llm.output_tokens", result.output_tokens)
        log.debug(
            "claude call complete",
            extra={
                "context": {
                    "model": result.model,
                    "input_tokens": result.input_tokens,
                    "output_tokens": result.output_tokens,
                    "cache_read_tokens": result.cache_read_tokens,
                    "latency_seconds": round(latency, 3),
                    "request_id": result.request_id,
                }
            },
        )
        return result


def _first_text(response: Any) -> str:
    for block in getattr(response, "content", []) or []:
        if getattr(block, "type", None) == "text":
            return getattr(block, "text", "") or ""
    return ""
