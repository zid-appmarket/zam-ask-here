"""Slack app wiring: event intake, async processing, reply posting.

**Acknowledgement.** Slack requires a 2xx within 3 seconds or it retries. The
LLM pipeline takes much longer than that, so events are acknowledged
immediately and handed to a worker pool (``process_before_response=False`` plus
an explicit executor). Retried deliveries are discarded by
``Store.claim_event``, which is an atomic insert -- so a retry that arrives
while the first delivery is still being processed is dropped, not duplicated.
"""

from __future__ import annotations

import contextlib
import threading
import time
from collections.abc import Mapping
from concurrent.futures import ThreadPoolExecutor
from typing import Any

from slack_bolt import App
from slack_sdk.errors import SlackApiError

from ..confidence import Action
from ..config import AppConfig
from ..escalation import EscalationManager
from ..knowledge.ingest import KnowledgeBase
from ..llm.base import LLMClient
from ..observability.logging import get_logger
from ..observability.metrics import METRICS
from ..pipeline import AgentDecision, IncomingMessage, SupportPipeline
from ..resolution import ResolutionManager, ResolutionResult
from ..store.base import Store
from .filters import (
    event_key,
    is_directly_addressed,
    reaction_event_key,
    should_handle,
    should_handle_reaction,
    strip_bot_mention,
)
from .retry import SlackCallFailed, call_with_retry
from .thread_context import EMPTY, fetch_thread_context

log = get_logger(__name__)


class SlackAgent:
    def __init__(
        self,
        *,
        config: AppConfig,
        knowledge: KnowledgeBase,
        llm: LLMClient,
        store: Store,
        app: App | None = None,
        pipeline: SupportPipeline | None = None,
        resolution: ResolutionManager | None = None,
    ) -> None:
        self.config = config
        self.knowledge = knowledge
        self.store = store
        self.started_at = time.time()
        self.pipeline = pipeline or SupportPipeline(
            config=config,
            knowledge=knowledge,
            llm=llm,
            store=store,
            escalation=EscalationManager(config.escalation, store),
        )
        self.app = app or App(
            token=config.slack.bot_token,
            signing_secret=config.slack.signing_secret,
            process_before_response=False,
            # Socket Mode has no signing secret to verify against.
            request_verification_enabled=config.slack.mode == "http",
            raise_error_for_unhandled_request=False,
        )
        self._executor = ThreadPoolExecutor(
            max_workers=max(1, config.worker_threads), thread_name_prefix="zam-agent"
        )
        self._bot_user_id: str | None = None
        self._bot_id: str | None = None
        self._identity_lock = threading.Lock()
        self.resolution = resolution or ResolutionManager(
            config,
            store,
            thread_lookup=self._thread_parent_ts,
            thread_fetcher=self._thread_messages,
        )
        self._register()

    # --------------------------------------------------------------- identity

    @property
    def bot_user_id(self) -> str | None:
        if self._bot_user_id is None:
            with self._identity_lock:
                if self._bot_user_id is None:
                    try:
                        auth = call_with_retry(self.app.client.auth_test, operation="auth.test")
                        self._bot_user_id = auth.get("user_id")
                        self._bot_id = auth.get("bot_id")
                        log.info(
                            "slack identity resolved",
                            extra={"context": {"bot_user_id": self._bot_user_id, "team": auth.get("team")}},
                        )
                    except SlackCallFailed as exc:
                        log.error("auth.test failed", extra={"context": {"error": exc.error}})
        return self._bot_user_id

    # ------------------------------------------------------------- registration

    def _register(self) -> None:
        @self.app.event("message")
        def _on_message(body: dict[str, Any], event: dict[str, Any], ack: Any) -> None:  # noqa: ANN401
            # Bolt acknowledges events for us before the listener runs
            # (process_before_response=False); ack() here is harmless and makes
            # the contract explicit. Some adapters have already acked.
            with contextlib.suppress(Exception):
                ack()
            self._submit(body, event)

        @self.app.event("app_mention")
        def _on_mention(body: dict[str, Any], event: dict[str, Any], ack: Any) -> None:  # noqa: ANN401
            with contextlib.suppress(Exception):
                ack()
            self._submit(body, event)

        @self.app.event("reaction_added")
        def _on_reaction_added(body: dict[str, Any], event: dict[str, Any], ack: Any) -> None:  # noqa: ANN401
            with contextlib.suppress(Exception):
                ack()
            self._submit_reaction(dict(body), dict(event), added=True)

        @self.app.event("reaction_removed")
        def _on_reaction_removed(body: dict[str, Any], event: dict[str, Any], ack: Any) -> None:  # noqa: ANN401
            with contextlib.suppress(Exception):
                ack()
            self._submit_reaction(dict(body), dict(event), added=False)

    def _submit(self, body: Mapping[str, Any], event: Mapping[str, Any]) -> None:
        METRICS.incr("slack.events_received")
        retry_num = _retry_number(body)
        if retry_num:
            METRICS.incr("slack.events_retried")
        self._executor.submit(self._guarded_process, dict(body), dict(event))

    def _submit_reaction(self, body: Mapping[str, Any], event: Mapping[str, Any], *, added: bool) -> None:
        if not self.config.slack.enable_slack_resolution:
            return
        METRICS.incr("slack.reactions_received")
        self._executor.submit(self._guarded_reaction, dict(body), dict(event), added)

    def _guarded_process(self, body: Mapping[str, Any], event: Mapping[str, Any]) -> None:
        try:
            self.process_event(body, event)
        except Exception:  # pragma: no cover - a worker must never die silently
            METRICS.incr("pipeline.unhandled_error")
            log.exception(
                "unhandled error processing Slack event",
                extra={"context": {"channel_id": event.get("channel"), "ts": event.get("ts")}},
            )

    def _guarded_reaction(self, body: Mapping[str, Any], event: Mapping[str, Any], added: bool) -> None:
        try:
            self.process_reaction(body, event, added=added)
        except Exception:  # pragma: no cover
            METRICS.incr("pipeline.unhandled_error")
            log.exception("unhandled error processing a reaction event")

    # ---------------------------------------------------------------- handling

    def process_event(self, body: Mapping[str, Any], event: Mapping[str, Any]) -> AgentDecision | None:
        decision_filter = should_handle(
            event, config=self.config.slack, bot_user_id=self.bot_user_id, bot_id=self._bot_id
        )
        if not decision_filter.handle:
            METRICS.incr(f"slack.filtered.{decision_filter.reason.split(':')[0]}")
            log.debug("event filtered", extra={"context": {"reason": decision_filter.reason}})
            return None

        key = event_key(event, _event_id(body))
        if not self.store.claim_event(
            key, channel_id=str(event.get("channel", "")), message_ts=str(event.get("ts", ""))
        ):
            METRICS.incr("slack.duplicate_event")
            log.info("duplicate Slack event ignored", extra={"context": {"event_key": key}})
            return None

        message = self._build_message(event, key)
        try:
            decision = self.pipeline.handle(message)
        except Exception:
            # Let Slack's retry (or a human) have another go at this message.
            self.store.release_event(key)
            raise

        if decision.retryable_error:
            self.store.release_event(key)
            log.warning(
                "releasing event for retry after a transient failure",
                extra={"context": {"event_key": key, "reason": decision.skip_reason}},
            )
            return decision

        if not decision.should_post:
            log.info(
                "no reply sent",
                extra={
                    "context": {
                        "action": decision.action.value,
                        "reason": decision.skip_reason or decision.category,
                        "channel_id": message.channel_id,
                    }
                },
            )
            return decision

        self._post(message, decision)
        return decision

    def process_reaction(
        self, body: Mapping[str, Any], event: Mapping[str, Any], *, added: bool
    ) -> ResolutionResult | None:
        """An owner marking a gap resolved (or undoing it) with a reaction."""

        decision = should_handle_reaction(
            event, config=self.config.slack, bot_user_id=self.bot_user_id
        )
        if not decision.handle:
            METRICS.incr(f"slack.reaction_filtered.{decision.reason.split(':')[0]}")
            return None

        key = reaction_event_key(event, _event_id(body))
        item = event.get("item") or {}
        if not self.store.claim_event(
            key, channel_id=str(item.get("channel", "")), message_ts=str(item.get("ts", ""))
        ):
            METRICS.incr("slack.duplicate_event")
            return None

        self.resolution.bot_user_id = self.bot_user_id
        try:
            result = self.resolution.handle_reaction(event, added=added)
        except Exception:
            self.store.release_event(key)
            raise

        if not result.changed_state:
            log.debug(
                "reaction did not change anything",
                extra={"context": {"outcome": result.outcome, "actor": result.actor_user_id}},
            )
            return result

        if self.config.dry_run:
            log.info(
                "DRY_RUN -- resolution confirmation not sent",
                extra={
                    "context": {
                        "outcome": result.outcome,
                        "question_key": result.question_key,
                        "captured_answer_chars": len(result.captured_answer),
                        "text": result.reply,
                    }
                },
            )
            return result

        if result.should_reply:
            try:
                call_with_retry(
                    self.app.client.chat_postMessage,
                    operation="chat.postMessage(resolution)",
                    channel=str(item.get("channel", "")),
                    thread_ts=result.thread_ts,
                    text=result.reply,
                    mrkdwn=True,
                    unfurl_links=False,
                )
                METRICS.incr(f"slack.posted.{result.outcome}")
            except SlackCallFailed as exc:
                log.warning(
                    "could not confirm the resolution in Slack",
                    extra={"context": {"error": exc.error, "outcome": result.outcome}},
                )
        return result

    def _thread_parent_ts(self, channel_id: str, message_ts: str) -> str | None:
        """The thread a message belongs to; the message itself if it is a root."""

        try:
            response = call_with_retry(
                self.app.client.conversations_replies,
                operation="conversations.replies(thread_lookup)",
                channel=channel_id,
                ts=message_ts,
                limit=1,
                inclusive=True,
            )
        except SlackCallFailed as exc:
            log.warning("could not resolve the thread of a reaction", extra={"context": {"error": exc.error}})
            return None
        messages = response.get("messages") or []
        if not messages:
            return None
        return str(messages[0].get("thread_ts") or messages[0].get("ts") or message_ts)

    def _thread_messages(self, channel_id: str, thread_ts: str) -> list[dict[str, Any]]:
        response = call_with_retry(
            self.app.client.conversations_replies,
            operation="conversations.replies(capture)",
            channel=channel_id,
            ts=thread_ts,
            limit=100,
            inclusive=True,
        )
        return list(response.get("messages") or [])

    def _build_message(self, event: Mapping[str, Any], key: str) -> IncomingMessage:
        channel_id = str(event.get("channel", ""))
        ts = str(event.get("ts", ""))
        thread_ts = str(event.get("thread_ts")) if event.get("thread_ts") else None
        is_reply = bool(thread_ts and thread_ts != ts)
        text = strip_bot_mention(str(event.get("text") or ""), self.bot_user_id)

        context = EMPTY
        if is_reply and thread_ts:
            context = fetch_thread_context(
                self.app.client,
                channel_id=channel_id,
                thread_ts=thread_ts,
                current_ts=ts,
                bot_user_id=self.bot_user_id,
                limit=self.config.slack.max_thread_context_messages,
            )

        return IncomingMessage(
            channel_id=channel_id,
            user_id=str(event.get("user", "")),
            text=text,
            message_ts=ts,
            event_key=key,
            thread_ts=thread_ts,
            is_thread_reply=is_reply,
            bot_participated_in_thread=context.bot_participated,
            directly_addressed=is_directly_addressed(event, self.bot_user_id),
            thread_context=context.rendered,
            permalink=self._permalink(channel_id, ts),
        )

    # ----------------------------------------------------------------- posting

    def _post(self, message: IncomingMessage, decision: AgentDecision) -> None:
        thread_ts: str | None = decision.thread_ts or message.reply_thread_ts
        if not self.config.slack.reply_in_thread and not message.is_thread_reply:
            thread_ts = None

        if self.config.dry_run:
            log.info(
                "DRY_RUN -- reply not sent",
                extra={
                    "context": {
                        "channel_id": message.channel_id,
                        "thread_ts": thread_ts,
                        "action": decision.action.value,
                        "confidence": decision.confidence_score,
                        "text": decision.text,
                        "owner_context": decision.owner_context,
                    }
                },
            )
            return

        if self.config.slack.add_ack_reaction:
            self._react(message)

        try:
            call_with_retry(
                self.app.client.chat_postMessage,
                operation="chat.postMessage",
                channel=message.channel_id,
                thread_ts=thread_ts,
                text=decision.text,
                mrkdwn=True,
                unfurl_links=False,
                unfurl_media=False,
            )
            METRICS.incr(f"slack.posted.{decision.action.value}")
        except SlackCallFailed as exc:
            METRICS.incr("slack.post_failed")
            log.error(
                "could not post reply",
                extra={
                    "context": {
                        "error": exc.error,
                        "fatal": exc.fatal,
                        "channel_id": message.channel_id,
                        "action": decision.action.value,
                    }
                },
            )
            return

        if decision.action is Action.ESCALATE and decision.tagged_owner and decision.owner_context:
            try:
                call_with_retry(
                    self.app.client.chat_postMessage,
                    operation="chat.postMessage(owner_context)",
                    channel=message.channel_id,
                    thread_ts=thread_ts,
                    text=decision.owner_context,
                    mrkdwn=True,
                    unfurl_links=False,
                )
            except SlackCallFailed as exc:
                log.warning("could not post owner context", extra={"context": {"error": exc.error}})

        log.info(
            "reply posted",
            extra={
                "context": {
                    "action": decision.action.value,
                    "category": decision.category,
                    "product": decision.product,
                    "confidence_level": decision.confidence_level,
                    "confidence_score": decision.confidence_score,
                    "language": decision.language,
                    "tagged_owner": decision.tagged_owner,
                    "sources": [ref.label for ref in decision.sources],
                    "latency_ms": decision.latency_ms,
                    "channel_id": message.channel_id,
                    "thread_ts": thread_ts,
                }
            },
        )

    def _react(self, message: IncomingMessage) -> None:
        try:
            self.app.client.reactions_add(
                channel=message.channel_id,
                timestamp=message.message_ts,
                name=self.config.slack.ack_reaction,
            )
        except SlackApiError as exc:
            if str((exc.response or {}).get("error")) not in ("already_reacted", "invalid_name"):
                log.debug("reaction failed", extra={"context": {"error": str(exc)}})

    def _permalink(self, channel_id: str, ts: str) -> str | None:
        try:
            response = self.app.client.chat_getPermalink(channel=channel_id, message_ts=ts)
            return response.get("permalink")
        except SlackApiError:
            return None

    # ------------------------------------------------------------------ health

    def health(self) -> dict[str, Any]:
        return {
            "status": "ok" if not self.knowledge.is_empty else "degraded",
            "uptime_seconds": round(time.time() - self.started_at, 1),
            "environment": self.config.environment,
            "mode": self.config.slack.mode,
            "dry_run": self.config.dry_run,
            "watched_channels": len(self.config.slack.channel_ids),
            "slack_resolution": {
                "enabled": self.config.slack.enable_slack_resolution,
                "reaction": self.config.slack.resolve_reaction,
                "authorized_actors": len(self.config.escalation.owner_ids)
                + len(self.config.escalation.knowledge_editor_user_ids),
            },
            "knowledge": self.knowledge.status(),
            "store": self.store.stats(),
            "metrics": METRICS.snapshot(),
        }

    def shutdown(self, *, wait: bool = True) -> None:
        self._executor.shutdown(wait=wait)


def _event_id(body: Mapping[str, Any]) -> str | None:
    value = body.get("event_id")
    return str(value) if value else None


def _retry_number(body: Mapping[str, Any]) -> int:
    headers = body.get("headers") or {}
    raw = body.get("retry_num") or (headers.get("x-slack-retry-num") if isinstance(headers, Mapping) else None)
    if isinstance(raw, list):
        raw = raw[0] if raw else None
    try:
        return int(raw) if raw is not None else 0
    except (TypeError, ValueError):
        return 0
