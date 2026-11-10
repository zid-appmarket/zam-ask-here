"""Non-fixture helpers shared by the test modules.

Kept out of ``conftest.py`` so tests can import them explicitly rather than
relying on fixture magic.
"""

from __future__ import annotations

import datetime as _dt
from pathlib import Path
from typing import Any

from zam_agent.config import (
    AppConfig,
    ConfidenceConfig,
    EscalationConfig,
    KnowledgeConfig,
    LLMConfig,
    SlackConfig,
)
from zam_agent.escalation import EscalationManager
from zam_agent.knowledge.ingest import KnowledgeBase
from zam_agent.llm.fake import FakeLLM
from zam_agent.pipeline import IncomingMessage, SupportPipeline
from zam_agent.store.sqlite_store import SQLiteStore

FIXTURE_KNOWLEDGE = Path(__file__).parent / "fixtures" / "knowledge"
FIXTURE_EVENTS = Path(__file__).parent / "fixtures" / "slack_events"

# Placeholder IDs with the right shape. Not real Slack IDs.
CHANNEL = "C0TESTCHAN1"
RESTRICTED_CHANNEL = "C0RESTRICT1"
OTHER_CHANNEL = "C0OTHERCHN1"
EMPLOYEE = "U0EMPLOYEE1"
BOT_USER = "U0BOTUSER01"
OWNER_DEFAULT = "U0OWNERDEF1"
OWNER_ZAM = "U0OWNERZAM1"
OWNER_THEME = "U0OWNERTHM1"
KB_EDITOR = "U0EDITOR0001"
APPROVER_OLA = "U0APPROVER1"
APPROVER_NORA = "U0APPROVER2"
OUTSIDER = "U0OUTSIDER1"

TODAY = _dt.date(2026, 11, 10)


def knowledge_config(directory: str | None = None, **overrides: Any) -> KnowledgeConfig:
    base = dict(
        directory=directory or str(FIXTURE_KNOWLEDGE),
        snapshot_path="/tmp/zam-test-snapshot.json",  # noqa: S108 - test-only
        top_k=6,
        min_score=0.08,
        max_age_days=365,
        chunk_target_chars=1200,
        chunk_overlap_chars=160,
        notion_api_key=None,
        notion_database_ids=(),
        notion_page_ids=(),
        gdrive_credentials_file=None,
        gdrive_folder_ids=(),
    )
    base.update(overrides)
    return KnowledgeConfig(**base)


def make_config(**overrides: Any) -> AppConfig:
    slack_overrides = overrides.pop("slack", {})
    escalation_overrides = overrides.pop("escalation", {})
    confidence_overrides = overrides.pop("confidence", {})
    knowledge_overrides = overrides.pop("knowledge", {})

    slack_defaults: dict[str, Any] = dict(
        bot_token="xoxb-test-not-a-real-token",
        signing_secret="test-signing-secret",
        app_token="xapp-test-not-a-real-token",
        mode="socket",
        channel_ids=(CHANNEL,),
        restricted_channel_ids=(),
        internal_channel_ids=(CHANNEL,),
        reply_in_thread=True,
        respond_to_unrelated=False,
        respond_only_to_questions=True,
        add_ack_reaction=False,
        ack_reaction="eyes",
        max_thread_context_messages=12,
        port=3000,
        prefilter_enabled=True,
        answer_general_questions=True,
        escalate_general_questions=False,
        include_sources=True,
        enable_slack_resolution=True,
        resolve_reaction="white_check_mark",
        broadcast_reaction="mega",
        enable_broadcast=True,
        broadcast_approver_user_ids=(APPROVER_OLA, APPROVER_NORA),
        deflect_technical_issues=True,
        hubspot_ticket_url="https://example.invalid/hubspot-ticket-form",
    )
    slack_defaults.update(slack_overrides)

    confidence_defaults: dict[str, Any] = dict(
        high_threshold=0.68,
        medium_threshold=0.40,
        min_evidence_coverage=0.34,
        min_supported_claim_ratio=0.75,
        max_unsupported_claims=0,
    )
    confidence_defaults.update(confidence_overrides)

    escalation_defaults: dict[str, Any] = dict(
        default_user_id=OWNER_DEFAULT,
        zam_user_id=OWNER_ZAM,
        theme_market_user_id=OWNER_THEME,
        cooldown_hours=24,
        knowledge_editor_user_ids=(KB_EDITOR,),
    )
    escalation_defaults.update(escalation_overrides)

    app_defaults: dict[str, Any] = dict(
        database_url="sqlite://:memory:",
        log_level="WARNING",
        log_format="text",
        dry_run=False,
        worker_threads=1,
        environment="test",
    )
    app_defaults.update(overrides)

    return AppConfig(
        slack=SlackConfig(**slack_defaults),
        escalation=EscalationConfig(**escalation_defaults),
        llm=LLMConfig(
            api_key="sk-ant-test-not-a-real-key",
            model="claude-opus-5-5",
            classifier_model="claude-opus-5-5",
            grader_model="claude-opus-5-5",
            effort="medium",
            classifier_effort="low",
            grader_effort="medium",
            max_tokens=4096,
            timeout_seconds=30.0,
            max_retries=1,
            enable_refusal_fallback=True,
        ),
        knowledge=knowledge_config(**knowledge_overrides),
        confidence=ConfidenceConfig(**confidence_defaults),
        **app_defaults,
    )


def build_pipeline(
    config: AppConfig,
    knowledge: KnowledgeBase,
    llm: FakeLLM,
    store: SQLiteStore,
) -> SupportPipeline:
    return SupportPipeline(
        config=config,
        knowledge=knowledge,
        llm=llm,
        store=store,
        escalation=EscalationManager(config.escalation, store),
    )

def message(
    text: str,
    *,
    channel_id: str = CHANNEL,
    user_id: str = EMPLOYEE,
    ts: str = "1762790400.000100",
    event_key: str | None = None,
    thread_ts: str | None = None,
    thread_context: str = "",
    bot_in_thread: bool = False,
    directly_addressed: bool = False,
) -> IncomingMessage:
    return IncomingMessage(
        channel_id=channel_id,
        user_id=user_id,
        text=text,
        message_ts=ts,
        event_key=event_key or f"evt:{ts}",
        thread_ts=thread_ts,
        is_thread_reply=bool(thread_ts and thread_ts != ts),
        bot_participated_in_thread=bot_in_thread,
        directly_addressed=directly_addressed,
        thread_context=thread_context,
        permalink=f"https://example.invalid/archives/{channel_id}/p{ts.replace('.', '')}",
    )


def classification(
    *,
    category: str = "zam_question",
    products: list[str] | None = None,
    is_question: bool = True,
    search_query: str = "",
    topic: str = "test topic",
    restricted: bool = False,
    injection: bool = False,
    confidence: float = 0.95,
) -> dict[str, Any]:
    return {
        "category": category,
        "products": products if products is not None else (["zam"] if category == "zam_question" else []),
        "is_question": is_question,
        "search_query": search_query,
        "topic": topic,
        "asks_for_restricted_info": restricted,
        "injection_attempt": injection,
        "confidence": confidence,
        "reason": "test",
    }


def answer_payload(
    *,
    answer: str,
    source_ids: list[str],
    sufficient: bool = True,
    conflicts: list[str] | None = None,
    clarifying_question: str = "",
    self_confidence: float = 0.9,
    claims: list[dict[str, Any]] | None = None,
    missing: list[str] | None = None,
) -> dict[str, Any]:
    resolved_claims = claims if claims is not None else [
        {"statement": answer, "source_ids": source_ids, "kind": "stated"}
    ]
    return {
        "answer": answer,
        "claims": resolved_claims,
        "cited_source_ids": source_ids,
        "sufficient_evidence": sufficient,
        "conflicts": conflicts or [],
        "missing_information": missing or [],
        "clarifying_question": clarifying_question,
        "self_confidence": self_confidence,
    }


def grade_payload(
    *,
    verdicts: list[str],
    uncited: bool = False,
    sources_contradict: bool = False,
    note: str = "",
) -> dict[str, Any]:
    return {
        "claims": [
            {"statement": f"claim {idx}", "verdict": verdict, "evidence_quote": "quoted"}
            for idx, verdict in enumerate(verdicts)
        ],
        "answer_contains_uncited_facts": uncited,
        "sources_contradict_each_other": sources_contradict,
        "verdict_note": note,
    }


def first_label(knowledge: KnowledgeBase, query: str, product: str | None = None) -> str:
    """The citation label the agent would really have available for a query."""

    result = knowledge.retrieve(query, product=product, today=TODAY)
    assert result.evidence, f"fixture knowledge returned nothing for {query!r}"
    return result.evidence[0].label
