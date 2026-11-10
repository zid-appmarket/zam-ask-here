"""Composition root: build the agent from configuration."""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass
from typing import Any

from .config import AppConfig, load_config
from .knowledge.ingest import KnowledgeBase
from .llm.base import LLMClient
from .observability.logging import configure_logging, get_logger
from .slackbot.app import SlackAgent
from .store.base import Store
from .store.sqlite_store import SQLiteStore

log = get_logger(__name__)


@dataclass
class Runtime:
    config: AppConfig
    knowledge: KnowledgeBase
    store: Store
    llm: LLMClient
    agent: SlackAgent


def build_runtime(
    config: AppConfig | None = None,
    *,
    llm: LLMClient | None = None,
    store: Store | None = None,
    knowledge: KnowledgeBase | None = None,
) -> Runtime:
    config = config or load_config()
    configure_logging(config.log_level, config.log_format)

    for warning in config.warnings:
        log.warning("configuration warning", extra={"context": {"detail": warning}})

    knowledge = knowledge or KnowledgeBase(config.knowledge)
    report = knowledge.reload()
    if report.documents == 0:
        log.error(
            "the knowledge base is empty -- the agent will escalate every question. "
            "Add documents under KNOWLEDGE_DIR or configure Notion/Drive.",
            extra={"context": {"knowledge_dir": config.knowledge.directory}},
        )
    for failure in report.errors:
        log.error("knowledge source error", extra={"context": {"detail": failure}})

    store = store or SQLiteStore(config.database_url)

    if llm is None:
        from .llm.anthropic_client import AnthropicLLM

        llm = AnthropicLLM(config.llm)

    agent = SlackAgent(config=config, knowledge=knowledge, llm=llm, store=store)

    log.info(
        "agent ready",
        extra={
            "context": {
                "mode": config.slack.mode,
                "model": config.llm.model,
                "channels": list(config.slack.channel_ids),
                "documents": report.documents,
                "chunks": report.chunks,
                "confidence_threshold": config.confidence.high_threshold,
                "dry_run": config.dry_run,
            }
        },
    )
    return Runtime(config=config, knowledge=knowledge, store=store, llm=llm, agent=agent)


def run_socket_mode(runtime: Runtime) -> None:
    from slack_bolt.adapter.socket_mode import SocketModeHandler

    app_token = runtime.config.slack.app_token
    if not app_token:
        raise RuntimeError("SLACK_APP_TOKEN is required for Socket Mode")
    log.info("starting in Socket Mode")
    SocketModeHandler(runtime.agent.app, app_token).start()


def build_wsgi_app(runtime: Runtime) -> Any:
    """WSGI app serving ``/slack/events`` plus ``/health`` and ``/metrics``."""

    import json

    from slack_bolt.adapter.wsgi import SlackRequestHandler

    slack_handler = SlackRequestHandler(runtime.agent.app)

    def application(environ: dict[str, Any], start_response: Any) -> Iterable[bytes]:
        path = environ.get("PATH_INFO", "")
        if path in ("/health", "/healthz", "/readyz"):
            payload = runtime.agent.health()
            body = json.dumps(payload, ensure_ascii=False, default=str).encode("utf-8")
            status = "200 OK" if payload.get("status") == "ok" else "503 Service Unavailable"
            start_response(status, [("Content-Type", "application/json"), ("Content-Length", str(len(body)))])
            return [body]
        if path == "/metrics":
            from .observability.metrics import METRICS

            body = json.dumps(METRICS.snapshot()).encode("utf-8")
            start_response("200 OK", [("Content-Type", "application/json"), ("Content-Length", str(len(body)))])
            return [body]
        return slack_handler(environ, start_response)

    return application
