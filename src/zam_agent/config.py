"""Environment-driven configuration for the ZAM / Theme Market Slack agent.

Every secret is read from the process environment (or a secrets manager that
exports into it). Nothing is defaulted to a real credential and nothing here is
ever logged verbatim -- see ``zam_agent.observability.logging``.
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from typing import Literal

SlackMode = Literal["socket", "http"]

_TRUTHY = {"1", "true", "yes", "on", "y"}
_FALSY = {"0", "false", "no", "off", "n", ""}


class ConfigError(RuntimeError):
    """Raised when required configuration is missing or invalid."""


def _env(name: str, default: str | None = None) -> str | None:
    value = os.environ.get(name)
    if value is None:
        return default
    value = value.strip()
    return value if value else default


def _env_bool(name: str, default: bool) -> bool:
    raw = _env(name)
    if raw is None:
        return default
    lowered = raw.lower()
    if lowered in _TRUTHY:
        return True
    if lowered in _FALSY:
        return False
    raise ConfigError(f"{name} must be a boolean-ish value, got {raw!r}")


def _env_int(name: str, default: int) -> int:
    raw = _env(name)
    if raw is None:
        return default
    try:
        return int(raw)
    except ValueError as exc:  # pragma: no cover - defensive
        raise ConfigError(f"{name} must be an integer, got {raw!r}") from exc


def _env_float(name: str, default: float) -> float:
    raw = _env(name)
    if raw is None:
        return default
    try:
        return float(raw)
    except ValueError as exc:  # pragma: no cover - defensive
        raise ConfigError(f"{name} must be a number, got {raw!r}") from exc


def _env_list(name: str, default: tuple[str, ...] = ()) -> tuple[str, ...]:
    raw = _env(name)
    if raw is None:
        return tuple(default)
    return tuple(part.strip() for part in raw.replace(";", ",").split(",") if part.strip())


# Slack user IDs look like U01234567 / W01234567; group IDs like S01234567.
def _looks_like_slack_actor_id(value: str) -> bool:
    return len(value) >= 9 and value[0] in {"U", "W", "S"} and value[1:].isalnum()


def _normalize_reaction(value: str | None) -> str:
    """Accept ``:white_check_mark:`` or ``white_check_mark``; Slack sends bare."""

    return (value or "").strip().strip(":")


def _looks_like_slack_channel_id(value: str) -> bool:
    return len(value) >= 9 and value[0] in {"C", "G", "D"} and value[1:].isalnum()


@dataclass(frozen=True)
class SlackConfig:
    bot_token: str
    signing_secret: str | None
    app_token: str | None
    mode: SlackMode
    channel_ids: tuple[str, ...]
    restricted_channel_ids: tuple[str, ...]
    internal_channel_ids: tuple[str, ...]
    reply_in_thread: bool
    respond_to_unrelated: bool
    respond_only_to_questions: bool
    add_ack_reaction: bool
    ack_reaction: str
    max_thread_context_messages: int
    port: int
    prefilter_enabled: bool
    answer_general_questions: bool
    escalate_general_questions: bool
    include_sources: bool
    enable_slack_resolution: bool
    resolve_reaction: str
    broadcast_reaction: str
    enable_broadcast: bool

    def is_watched_channel(self, channel_id: str) -> bool:
        return channel_id in self.channel_ids


@dataclass(frozen=True)
class EscalationConfig:
    default_user_id: str
    zam_user_id: str
    theme_market_user_id: str
    cooldown_hours: int
    knowledge_editor_user_ids: tuple[str, ...] = ()

    def owner_for(self, product: str | None) -> str:
        if product == "zam":
            return self.zam_user_id
        if product == "theme_market":
            return self.theme_market_user_id
        return self.default_user_id

    @property
    def owner_ids(self) -> tuple[str, ...]:
        seen = (self.default_user_id, self.zam_user_id, self.theme_market_user_id)
        return tuple(dict.fromkeys(uid for uid in seen if uid))

    def may_resolve(self, user_id: str) -> bool:
        """Only a configured owner or knowledge editor may close a gap.

        Anyone can add a reaction in a public channel, so the authorisation
        check has to live here rather than relying on the reaction itself.
        """

        uid = (user_id or "").strip()
        if not uid:
            return False
        return uid in self.owner_ids or uid in self.knowledge_editor_user_ids


@dataclass(frozen=True)
class LLMConfig:
    api_key: str
    model: str
    classifier_model: str
    grader_model: str
    effort: str
    classifier_effort: str
    grader_effort: str
    max_tokens: int
    timeout_seconds: float
    max_retries: int
    enable_refusal_fallback: bool


@dataclass(frozen=True)
class KnowledgeConfig:
    directory: str
    snapshot_path: str
    top_k: int
    min_score: float
    max_age_days: int
    chunk_target_chars: int
    chunk_overlap_chars: int
    notion_api_key: str | None
    notion_database_ids: tuple[str, ...]
    notion_page_ids: tuple[str, ...]
    gdrive_credentials_file: str | None
    gdrive_folder_ids: tuple[str, ...]
    gdrive_file_ids: tuple[str, ...] = ()
    draft_directory: str = "./knowledge/_inbox"

    @property
    def notion_enabled(self) -> bool:
        return bool(self.notion_api_key) and bool(self.notion_database_ids or self.notion_page_ids)

    @property
    def gdrive_enabled(self) -> bool:
        return bool(self.gdrive_credentials_file) and bool(self.gdrive_folder_ids or self.gdrive_file_ids)


@dataclass(frozen=True)
class ConfidenceConfig:
    """Thresholds for the deterministic confidence gate.

    ``high_threshold`` is ``CONFIDENCE_THRESHOLD``: at or above it the agent may
    answer on its own. Below ``medium_threshold`` it escalates. In between it
    clarifies (or escalates if clarification cannot help).
    """

    high_threshold: float
    medium_threshold: float
    min_evidence_coverage: float
    min_supported_claim_ratio: float
    max_unsupported_claims: int


@dataclass(frozen=True)
class AppConfig:
    slack: SlackConfig
    escalation: EscalationConfig
    llm: LLMConfig
    knowledge: KnowledgeConfig
    confidence: ConfidenceConfig
    database_url: str
    log_level: str
    log_format: str
    dry_run: bool
    worker_threads: int
    environment: str
    warnings: tuple[str, ...] = field(default=())


def _require(name: str) -> str:
    value = _env(name)
    if not value:
        raise ConfigError(
            f"{name} is required. Copy .env.example to .env and fill it in, "
            "or export it from your secrets manager."
        )
    return value


def load_config(*, require_secrets: bool = True) -> AppConfig:
    """Build an :class:`AppConfig` from the environment.

    ``require_secrets=False`` is used by tooling (e.g. the ingestion CLI) that
    needs knowledge settings but no Slack or Anthropic credentials.
    """

    warnings: list[str] = []

    mode_raw = (_env("SLACK_MODE", "socket") or "socket").lower()
    if mode_raw not in ("socket", "http"):
        raise ConfigError("SLACK_MODE must be 'socket' or 'http'")
    mode: SlackMode = mode_raw  # type: ignore[assignment]

    bot_token = _require("SLACK_BOT_TOKEN") if require_secrets else _env("SLACK_BOT_TOKEN", "") or ""
    signing_secret = _env("SLACK_SIGNING_SECRET")
    app_token = _env("SLACK_APP_TOKEN")

    if require_secrets:
        if mode == "http" and not signing_secret:
            raise ConfigError("SLACK_SIGNING_SECRET is required when SLACK_MODE=http")
        if mode == "socket" and not app_token:
            raise ConfigError("SLACK_APP_TOKEN is required when SLACK_MODE=socket")

    channel_ids = _env_list("SLACK_CHANNEL_IDS") or _env_list("SLACK_CHANNEL_ID")
    if require_secrets and not channel_ids:
        raise ConfigError("SLACK_CHANNEL_ID is required (comma-separate for several channels)")
    for cid in channel_ids:
        if not _looks_like_slack_channel_id(cid):
            raise ConfigError(
                f"SLACK_CHANNEL_ID entry {cid!r} does not look like a Slack channel ID "
                "(expected something like C0123456789)"
            )

    default_owner = _require("ESCALATION_USER_ID") if require_secrets else _env("ESCALATION_USER_ID", "") or ""
    if default_owner and not _looks_like_slack_actor_id(default_owner):
        raise ConfigError(
            f"ESCALATION_USER_ID {default_owner!r} does not look like a Slack user or group ID "
            "(expected something like U0123456789). Look it up in Slack; never guess a username."
        )
    zam_owner = _env("ZAM_ESCALATION_USER_ID") or default_owner
    theme_owner = _env("THEME_MARKET_ESCALATION_USER_ID") or default_owner
    for name, value in (("ZAM_ESCALATION_USER_ID", zam_owner), ("THEME_MARKET_ESCALATION_USER_ID", theme_owner)):
        if value and not _looks_like_slack_actor_id(value):
            raise ConfigError(f"{name} {value!r} does not look like a Slack user or group ID")
    if require_secrets and zam_owner == theme_owner == default_owner:
        warnings.append(
            "ZAM_ESCALATION_USER_ID and THEME_MARKET_ESCALATION_USER_ID are unset; "
            "all escalations go to ESCALATION_USER_ID."
        )

    editors = _env_list("KNOWLEDGE_EDITOR_USER_IDS")
    for editor in editors:
        if not _looks_like_slack_actor_id(editor):
            raise ConfigError(
                f"KNOWLEDGE_EDITOR_USER_IDS entry {editor!r} does not look like a Slack user or group ID"
            )

    model = _env("CLAUDE_MODEL", "claude-opus-5-5") or "claude-opus-5-5"
    llm = LLMConfig(
        api_key=(_require("ANTHROPIC_API_KEY") if require_secrets else _env("ANTHROPIC_API_KEY", "") or ""),
        model=model,
        classifier_model=_env("CLAUDE_CLASSIFIER_MODEL", model) or model,
        grader_model=_env("CLAUDE_GRADER_MODEL", model) or model,
        effort=(_env("CLAUDE_EFFORT", "medium") or "medium").lower(),
        classifier_effort=(_env("CLAUDE_CLASSIFIER_EFFORT", "low") or "low").lower(),
        grader_effort=(_env("CLAUDE_GRADER_EFFORT", "medium") or "medium").lower(),
        max_tokens=_env_int("CLAUDE_MAX_TOKENS", 4096),
        timeout_seconds=_env_float("CLAUDE_TIMEOUT_SECONDS", 90.0),
        max_retries=_env_int("CLAUDE_MAX_RETRIES", 3),
        enable_refusal_fallback=_env_bool("CLAUDE_ENABLE_REFUSAL_FALLBACK", True),
    )
    for label, effort in (
        ("CLAUDE_EFFORT", llm.effort),
        ("CLAUDE_CLASSIFIER_EFFORT", llm.classifier_effort),
        ("CLAUDE_GRADER_EFFORT", llm.grader_effort),
    ):
        if effort not in ("low", "medium", "high", "xhigh", "max"):
            raise ConfigError(f"{label} must be one of low|medium|high|xhigh|max, got {effort!r}")

    knowledge = KnowledgeConfig(
        directory=_env("KNOWLEDGE_DIR", "./knowledge") or "./knowledge",
        snapshot_path=_env("KNOWLEDGE_SNAPSHOT_PATH", "./data/knowledge_index.json")
        or "./data/knowledge_index.json",
        top_k=_env_int("RETRIEVAL_TOP_K", 6),
        min_score=_env_float("RETRIEVAL_MIN_SCORE", 0.08),
        max_age_days=_env_int("KNOWLEDGE_MAX_AGE_DAYS", 365),
        chunk_target_chars=_env_int("KNOWLEDGE_CHUNK_CHARS", 1200),
        chunk_overlap_chars=_env_int("KNOWLEDGE_CHUNK_OVERLAP", 160),
        notion_api_key=_env("NOTION_API_KEY"),
        notion_database_ids=_env_list("NOTION_DATABASE_IDS"),
        notion_page_ids=_env_list("NOTION_PAGE_IDS"),
        gdrive_credentials_file=_env("GOOGLE_DRIVE_CREDENTIALS_FILE"),
        gdrive_folder_ids=_env_list("GOOGLE_DRIVE_FOLDER_IDS"),
        gdrive_file_ids=_env_list("GOOGLE_DRIVE_FILE_IDS"),
        draft_directory=_env("KNOWLEDGE_DRAFT_DIR", "./knowledge/_inbox") or "./knowledge/_inbox",
    )

    high = _env_float("CONFIDENCE_THRESHOLD", 0.68)
    medium = _env_float("MEDIUM_CONFIDENCE_THRESHOLD", 0.40)
    if not 0.0 <= medium <= high <= 1.0:
        raise ConfigError(
            "Expected 0 <= MEDIUM_CONFIDENCE_THRESHOLD <= CONFIDENCE_THRESHOLD <= 1, "
            f"got medium={medium} high={high}"
        )
    confidence = ConfidenceConfig(
        high_threshold=high,
        medium_threshold=medium,
        min_evidence_coverage=_env_float("MIN_EVIDENCE_COVERAGE", 0.34),
        min_supported_claim_ratio=_env_float("MIN_SUPPORTED_CLAIM_RATIO", 0.75),
        max_unsupported_claims=_env_int("MAX_UNSUPPORTED_CLAIMS", 0),
    )

    slack = SlackConfig(
        bot_token=bot_token,
        signing_secret=signing_secret,
        app_token=app_token,
        mode=mode,
        channel_ids=channel_ids,
        restricted_channel_ids=_env_list("RESTRICTED_CHANNEL_IDS"),
        internal_channel_ids=_env_list("INTERNAL_CHANNEL_IDS") or channel_ids,
        reply_in_thread=_env_bool("ANSWER_IN_THREAD", True),
        respond_to_unrelated=_env_bool("RESPOND_TO_UNRELATED", False),
        respond_only_to_questions=_env_bool("RESPOND_ONLY_TO_QUESTIONS", True),
        add_ack_reaction=_env_bool("ADD_ACK_REACTION", False),
        ack_reaction=_env("ACK_REACTION", "eyes") or "eyes",
        max_thread_context_messages=_env_int("MAX_THREAD_CONTEXT_MESSAGES", 12),
        port=_env_int("PORT", 3000),
        prefilter_enabled=_env_bool("PREFILTER_ENABLED", True),
        answer_general_questions=_env_bool("ANSWER_GENERAL_QUESTIONS", True),
        escalate_general_questions=_env_bool("ESCALATE_GENERAL_QUESTIONS", False),
        include_sources=_env_bool("INCLUDE_SOURCE_LINKS", True),
        enable_slack_resolution=_env_bool("ENABLE_SLACK_RESOLUTION", True),
        resolve_reaction=_normalize_reaction(_env("RESOLVE_REACTION", "white_check_mark")),
        broadcast_reaction=_normalize_reaction(_env("BROADCAST_REACTION", "mega")),
        enable_broadcast=_env_bool("ENABLE_BROADCAST", False),
    )

    database_url = _env("DATABASE_URL", "sqlite:///./data/zam_agent.db") or "sqlite:///./data/zam_agent.db"

    return AppConfig(
        slack=slack,
        escalation=EscalationConfig(
            default_user_id=default_owner,
            zam_user_id=zam_owner,
            theme_market_user_id=theme_owner,
            cooldown_hours=_env_int("ESCALATION_COOLDOWN_HOURS", 24),
            knowledge_editor_user_ids=editors,
        ),
        llm=llm,
        knowledge=knowledge,
        confidence=confidence,
        database_url=database_url,
        log_level=(_env("LOG_LEVEL", "INFO") or "INFO").upper(),
        log_format=(_env("LOG_FORMAT", "json") or "json").lower(),
        dry_run=_env_bool("DRY_RUN", False),
        worker_threads=_env_int("WORKER_THREADS", 4),
        environment=_env("ENVIRONMENT", "development") or "development",
        warnings=tuple(warnings),
    )
