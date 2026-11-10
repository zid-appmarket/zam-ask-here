"""Configuration loading and validation."""

from __future__ import annotations

import pytest

from zam_agent.config import ConfigError, load_config

MINIMAL = {
    "SLACK_BOT_TOKEN": "xoxb-placeholder",
    "SLACK_APP_TOKEN": "xapp-placeholder",
    "SLACK_CHANNEL_ID": "C0TESTCHAN1",
    "ESCALATION_USER_ID": "U0OWNERDEF1",
    "ANTHROPIC_API_KEY": "sk-ant-placeholder",
}


def apply(monkeypatch: pytest.MonkeyPatch, env: dict[str, str], *, clear: bool = True) -> None:
    if clear:
        for key in list(MINIMAL) + [
            "SLACK_MODE", "SLACK_SIGNING_SECRET", "SLACK_CHANNEL_IDS", "ZAM_ESCALATION_USER_ID",
            "THEME_MARKET_ESCALATION_USER_ID", "CONFIDENCE_THRESHOLD", "MEDIUM_CONFIDENCE_THRESHOLD",
            "CLAUDE_MODEL", "CLAUDE_CLASSIFIER_MODEL", "CLAUDE_EFFORT", "DATABASE_URL",
            "RESPOND_TO_UNRELATED", "DRY_RUN", "ANSWER_IN_THREAD",
            "BROADCAST_APPROVER_USER_IDS", "BROADCAST_REACTION", "ENABLE_BROADCAST",
            "HUBSPOT_TICKET_URL", "DEFLECT_TECHNICAL_ISSUES", "KNOWLEDGE_EDITOR_USER_IDS",
            "RESOLVE_REACTION", "ENABLE_SLACK_RESOLUTION",
        ]:
            monkeypatch.delenv(key, raising=False)
    for key, value in env.items():
        monkeypatch.setenv(key, value)


def test_minimal_configuration_loads(monkeypatch: pytest.MonkeyPatch) -> None:
    apply(monkeypatch, MINIMAL)
    config = load_config()

    assert config.slack.mode == "socket"
    assert config.slack.channel_ids == ("C0TESTCHAN1",)
    assert config.llm.model == "claude-opus-5-5"
    assert config.escalation.owner_for("zam") == "U0OWNERDEF1"
    assert config.confidence.high_threshold == 0.68


@pytest.mark.parametrize("missing", list(MINIMAL))
def test_each_required_variable_is_enforced(monkeypatch: pytest.MonkeyPatch, missing: str) -> None:
    env = {k: v for k, v in MINIMAL.items() if k != missing}
    apply(monkeypatch, env)
    with pytest.raises(ConfigError) as excinfo:
        load_config()
    assert missing.split("_")[0] in str(excinfo.value) or missing in str(excinfo.value)


def test_http_mode_requires_a_signing_secret(monkeypatch: pytest.MonkeyPatch) -> None:
    apply(monkeypatch, {**MINIMAL, "SLACK_MODE": "http"})
    with pytest.raises(ConfigError, match="SLACK_SIGNING_SECRET"):
        load_config()

    apply(monkeypatch, {**MINIMAL, "SLACK_MODE": "http", "SLACK_SIGNING_SECRET": "s"}, clear=False)
    assert load_config().slack.mode == "http"


def test_socket_mode_requires_an_app_token(monkeypatch: pytest.MonkeyPatch) -> None:
    env = {k: v for k, v in MINIMAL.items() if k != "SLACK_APP_TOKEN"}
    apply(monkeypatch, env)
    with pytest.raises(ConfigError, match="SLACK_APP_TOKEN"):
        load_config()


def test_an_unknown_slack_mode_is_rejected(monkeypatch: pytest.MonkeyPatch) -> None:
    apply(monkeypatch, {**MINIMAL, "SLACK_MODE": "webhook"})
    with pytest.raises(ConfigError, match="SLACK_MODE"):
        load_config()


@pytest.mark.parametrize("bad", ["general", "#general", "U0123456789", "C1"])
def test_a_channel_id_that_is_not_a_channel_id_is_rejected(
    monkeypatch: pytest.MonkeyPatch, bad: str
) -> None:
    apply(monkeypatch, {**MINIMAL, "SLACK_CHANNEL_ID": bad})
    with pytest.raises(ConfigError, match="SLACK_CHANNEL_ID"):
        load_config()


@pytest.mark.parametrize("bad", ["@someone", "someone", "C0TESTCHAN1"])
def test_a_guessed_username_is_rejected_as_an_escalation_target(
    monkeypatch: pytest.MonkeyPatch, bad: str
) -> None:
    apply(monkeypatch, {**MINIMAL, "ESCALATION_USER_ID": bad})
    with pytest.raises(ConfigError, match="ESCALATION_USER_ID"):
        load_config()


def test_a_user_group_id_is_accepted_as_an_escalation_target(monkeypatch: pytest.MonkeyPatch) -> None:
    apply(monkeypatch, {**MINIMAL, "ESCALATION_USER_ID": "S0PLATFORM1"})
    assert load_config().escalation.default_user_id == "S0PLATFORM1"


def test_per_product_owners_override_the_default(monkeypatch: pytest.MonkeyPatch) -> None:
    apply(
        monkeypatch,
        {
            **MINIMAL,
            "ZAM_ESCALATION_USER_ID": "U0OWNERZAM1",
            "THEME_MARKET_ESCALATION_USER_ID": "U0OWNERTHM1",
        },
    )
    config = load_config()

    assert config.escalation.owner_for("zam") == "U0OWNERZAM1"
    assert config.escalation.owner_for("theme_market") == "U0OWNERTHM1"
    assert config.escalation.owner_for(None) == "U0OWNERDEF1"
    assert not any("ESCALATION_USER_ID" in warning for warning in config.warnings)


def test_a_warning_is_raised_when_no_per_product_owner_is_set(monkeypatch: pytest.MonkeyPatch) -> None:
    apply(monkeypatch, MINIMAL)
    assert any("ESCALATION_USER_ID" in warning for warning in load_config().warnings)


def test_broadcasting_warns_when_nobody_is_allowed_to_approve(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Broadcasting on with no approver would silently never fire."""

    apply(monkeypatch, MINIMAL)
    config = load_config()
    assert config.slack.enable_broadcast is True
    assert config.slack.broadcast_approver_user_ids == ()
    assert any("BROADCAST_APPROVER_USER_IDS" in warning for warning in config.warnings)
    assert config.slack.may_broadcast("U0ANYONE001") is False, "must fail closed"


def test_only_configured_approvers_may_broadcast(monkeypatch: pytest.MonkeyPatch) -> None:
    apply(monkeypatch, {**MINIMAL, "BROADCAST_APPROVER_USER_IDS": "U0APPROVER1, U0APPROVER2"})
    config = load_config()

    assert config.slack.broadcast_approver_user_ids == ("U0APPROVER1", "U0APPROVER2")
    assert config.slack.may_broadcast("U0APPROVER1") is True
    assert config.slack.may_broadcast("U0APPROVER2") is True
    assert config.slack.may_broadcast("U0OWNERDEF1") is False, "an escalation owner is not an approver"
    assert config.slack.may_broadcast("") is False
    assert not any("BROADCAST_APPROVER_USER_IDS" in w for w in config.warnings)


@pytest.mark.parametrize("value", ["mega", ":mega:", " :mega: "])
def test_reaction_names_accept_colons(monkeypatch: pytest.MonkeyPatch, value: str) -> None:
    apply(monkeypatch, {**MINIMAL, "BROADCAST_REACTION": value})
    assert load_config().slack.broadcast_reaction == "mega"


def test_a_bad_approver_id_is_rejected(monkeypatch: pytest.MonkeyPatch) -> None:
    apply(monkeypatch, {**MINIMAL, "BROADCAST_APPROVER_USER_IDS": "@ola"})
    with pytest.raises(ConfigError, match="BROADCAST_APPROVER_USER_IDS"):
        load_config()


def test_deflection_warns_without_a_ticket_url(monkeypatch: pytest.MonkeyPatch) -> None:
    apply(monkeypatch, MINIMAL)
    assert any("HUBSPOT_TICKET_URL" in warning for warning in load_config().warnings)

    apply(monkeypatch, {**MINIMAL, "HUBSPOT_TICKET_URL": "https://example.invalid/form"}, clear=False)
    config = load_config()
    assert config.slack.hubspot_ticket_url == "https://example.invalid/form"
    assert not any("HUBSPOT_TICKET_URL" in warning for warning in config.warnings)


def test_multiple_channels_can_be_watched(monkeypatch: pytest.MonkeyPatch) -> None:
    apply(monkeypatch, {**MINIMAL, "SLACK_CHANNEL_IDS": "C0TESTCHAN1, C0SECONDCH1"})
    config = load_config()

    assert config.slack.channel_ids == ("C0TESTCHAN1", "C0SECONDCH1")
    assert config.slack.is_watched_channel("C0SECONDCH1")
    assert not config.slack.is_watched_channel("C0OTHERCHN1")


def test_thresholds_must_be_ordered(monkeypatch: pytest.MonkeyPatch) -> None:
    apply(monkeypatch, {**MINIMAL, "CONFIDENCE_THRESHOLD": "0.3", "MEDIUM_CONFIDENCE_THRESHOLD": "0.8"})
    with pytest.raises(ConfigError, match="MEDIUM_CONFIDENCE_THRESHOLD"):
        load_config()


def test_an_invalid_effort_level_is_rejected(monkeypatch: pytest.MonkeyPatch) -> None:
    apply(monkeypatch, {**MINIMAL, "CLAUDE_EFFORT": "extreme"})
    with pytest.raises(ConfigError, match="CLAUDE_EFFORT"):
        load_config()


def test_stage_models_default_to_the_main_model(monkeypatch: pytest.MonkeyPatch) -> None:
    apply(monkeypatch, {**MINIMAL, "CLAUDE_MODEL": "claude-opus-5-5"})
    config = load_config()
    assert config.llm.classifier_model == "claude-opus-5-5"
    assert config.llm.grader_model == "claude-opus-5-5"

    apply(monkeypatch, {**MINIMAL, "CLAUDE_CLASSIFIER_MODEL": "claude-haiku-5-5"}, clear=False)
    assert load_config().llm.classifier_model == "claude-haiku-5-5"


@pytest.mark.parametrize(
    ("value", "expected"), [("true", True), ("1", True), ("yes", True), ("false", False), ("0", False)]
)
def test_boolean_parsing(monkeypatch: pytest.MonkeyPatch, value: str, expected: bool) -> None:
    apply(monkeypatch, {**MINIMAL, "DRY_RUN": value})
    assert load_config().dry_run is expected


def test_a_nonsense_boolean_is_rejected(monkeypatch: pytest.MonkeyPatch) -> None:
    apply(monkeypatch, {**MINIMAL, "DRY_RUN": "maybe"})
    with pytest.raises(ConfigError, match="DRY_RUN"):
        load_config()


def test_tooling_can_load_configuration_without_secrets(monkeypatch: pytest.MonkeyPatch) -> None:
    apply(monkeypatch, {})
    config = load_config(require_secrets=False)
    assert config.knowledge.directory
    assert config.slack.channel_ids == ()


def test_an_unsupported_database_url_fails_with_a_clear_message() -> None:
    from zam_agent.store.sqlite_store import path_from_database_url

    with pytest.raises(ValueError, match="SQLite only"):
        path_from_database_url("postgresql://user:pass@host/db")
