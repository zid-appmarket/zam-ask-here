"""Keeping technical issues and ticket links out of the channel."""

from __future__ import annotations

import pytest

from zam_agent.confidence import Action
from zam_agent.deflection import deflection_message
from zam_agent.llm.fake import FakeLLM
from zam_agent.store.sqlite_store import SQLiteStore
from zam_agent.triage import detect_ticket_links

from .fakes import FakeSlackClient, slack_envelope, slack_message_event
from .helpers import (
    OWNER_ZAM,
    TODAY,
    build_pipeline,
    classification,
    make_config,
    message,
)
from .test_slack_events import build_agent

HUBSPOT_URL = "https://app.hubspot.com/contacts/1234/ticket/5678"
JIRA_URL = "https://zid.atlassian.net/browse/ZAMCASE-4821"


# ------------------------------------------------------------ link detection


@pytest.mark.parametrize(
    ("text", "kind"),
    [
        (f"see {HUBSPOT_URL}", "hubspot"),
        (f"already raised <{HUBSPOT_URL}|the ticket>", "hubspot"),
        ("form here https://share.hsforms.com/abcdefg", "hubspot"),
        (f"tracking in {JIRA_URL}", "jira"),
        ("ZAMCASE-4821 is still open", "jira"),
        ("can someone look at ZAM-77", "jira"),
        ("فتحت تكت https://app.hubspot.com/x/1 وما رد أحد", "hubspot"),
        ("What are the Theme Market pricing tiers?", "none"),
        ("كم مدة مراجعة التطبيق؟", "none"),
        ("we hit the COVID-19 limits", "none"),
        ("per RFC-2119 the word must", "none"),
        ("the ISO-8601 format", "none"),
        ("", "none"),
    ],
)
def test_ticket_link_detection(text: str, kind: str) -> None:
    assert detect_ticket_links(text).kind == kind


def test_hubspot_wins_when_both_links_are_present() -> None:
    signal = detect_ticket_links(f"{JIRA_URL} and {HUBSPOT_URL}")
    assert signal.kind == "hubspot"
    assert signal.already_in_hubspot is True


# ---------------------------------------------------------------- messages


def test_a_hubspot_link_is_told_to_follow_up_there() -> None:
    text = deflection_message(reason="hubspot_link", language="en")
    assert "follow it up there" in text
    assert "rather than in this channel" in text


def test_a_jira_link_is_told_to_raise_a_hubspot_ticket() -> None:
    text = deflection_message(
        reason="jira_link", language="en", hubspot_ticket_url="https://example.invalid/form"
    )
    assert "raise it as a HubSpot ticket" in text
    assert "<https://example.invalid/form|Raise a ticket>" in text


def test_the_nudge_is_localised() -> None:
    assert "HubSpot" in deflection_message(reason="hubspot_link", language="ar")
    assert "تابعها هناك" in deflection_message(reason="hubspot_link", language="ar")
    assert "ارفع تكت" in deflection_message(
        reason="technical_issue", language="ar", hubspot_ticket_url="https://example.invalid/f"
    )


def test_the_nudge_never_tags_anyone() -> None:
    for reason in ("hubspot_link", "jira_link", "technical_issue"):
        for language in ("ar", "en"):
            text = deflection_message(reason=reason, language=language)  # type: ignore[arg-type]
            for marker in ("<@", "<!here>", "<!channel>", "@here", "@channel"):
                assert marker not in text


def test_the_nudge_works_without_a_configured_form_url() -> None:
    text = deflection_message(reason="technical_issue", language="en", hubspot_ticket_url=None)
    assert "HubSpot" in text
    assert "<" not in text.replace("<", "", 0) or "|" not in text


# ---------------------------------------------------------------- pipeline


@pytest.mark.parametrize(
    ("text", "expected_reason"),
    [
        (f"the merchant's app is stuck, see {HUBSPOT_URL}", "hubspot_link"),
        (f"any update on {JIRA_URL}?", "jira_link"),
        ("ZAMCASE-4821 still not resolved for the ZAM app", "jira_link"),
    ],
)
def test_a_ticket_link_is_deflected_without_any_model_call(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore, text: str, expected_reason: str
) -> None:
    pipeline = build_pipeline(config, fixture_knowledge, llm, store)

    decision = pipeline.handle(message(text), today=TODAY)

    assert decision.action is Action.DEFLECT
    assert decision.skip_reason == expected_reason
    assert llm.calls == [], "a ticket link needs no classification"
    assert decision.text


def test_a_hubspot_link_gets_the_follow_up_wording(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    pipeline = build_pipeline(config, fixture_knowledge, llm, store)

    decision = pipeline.handle(message(f"no reply on {HUBSPOT_URL}"), today=TODAY)

    assert "follow it up there" in decision.text
    assert "Raise a ticket" not in decision.text


def test_an_arabic_technical_post_is_deflected_in_arabic(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    pipeline = build_pipeline(config, fixture_knowledge, llm, store)

    decision = pipeline.handle(message(f"التكت ما فيها رد {HUBSPOT_URL}"), today=TODAY)

    assert decision.action is Action.DEFLECT
    assert decision.language == "ar"
    assert "تابعها هناك" in decision.text


def test_an_unlinked_technical_issue_is_deflected_by_the_classifier(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    pipeline = build_pipeline(config, fixture_knowledge, llm, store)
    llm.script(
        "classify",
        classification(
            category="technical_issue_or_incident",
            products=["zam"],
            search_query="app install failing for merchant",
        ),
    )

    decision = pipeline.handle(
        message("The ZAM app install keeps failing for merchant 88213, urgent"), today=TODAY
    )

    assert decision.action is Action.DEFLECT
    assert decision.skip_reason == "technical_issue"
    assert "raise it as a HubSpot ticket" in decision.text
    assert llm.call_counts["answer"] == 0
    assert llm.call_counts["grade"] == 0


def test_a_technical_issue_does_not_tag_the_owner(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    """A broken thing is not an unanswered question: nobody gets pinged."""

    pipeline = build_pipeline(config, fixture_knowledge, llm, store)
    llm.script("classify", classification(category="technical_issue_or_incident", search_query="x"))

    decision = pipeline.handle(message("ZAM installs are failing, nothing works"), today=TODAY)

    assert decision.tagged_owner is False
    assert f"<@{OWNER_ZAM}>" not in decision.text
    assert store.knowledge_gaps() == []


def test_a_genuine_question_is_still_answered_normally(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    from .helpers import answer_payload, first_label, grade_payload

    pipeline = build_pipeline(config, fixture_knowledge, llm, store)
    query = "How long does ZAM app review take?"
    label = first_label(fixture_knowledge, query, "zam")
    llm.script("classify", classification(category="zam_question", search_query=query))
    llm.script("answer", answer_payload(answer="App review takes 4 business days.", source_ids=[label]))
    llm.script("grade", grade_payload(verdicts=["supported"]))

    decision = pipeline.handle(message(query), today=TODAY)

    assert decision.action is Action.ANSWER


def test_deflection_can_be_turned_off(fixture_knowledge, llm: FakeLLM, store: SQLiteStore) -> None:
    config = make_config(slack={"deflect_technical_issues": False})
    pipeline = build_pipeline(config, fixture_knowledge, llm, store)
    llm.script("classify", classification(category="zam_question", search_query="x"))

    decision = pipeline.handle(message(f"see {HUBSPOT_URL} for the ZAM issue"), today=TODAY)

    assert decision.action is not Action.DEFLECT


def test_the_classifier_category_can_be_ignored_when_deflection_is_off(
    fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    config = make_config(slack={"deflect_technical_issues": False})
    pipeline = build_pipeline(config, fixture_knowledge, llm, store)
    llm.script("classify", classification(category="technical_issue_or_incident", search_query="x"))

    decision = pipeline.handle(message("the ZAM app is broken for everyone"), today=TODAY)

    assert decision.action is Action.IGNORE
    assert decision.skip_reason == "technical_issue_deflection_disabled"


# ------------------------------------------------------------------- Slack


def test_the_nudge_is_posted_in_the_thread_not_the_channel(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    client = FakeSlackClient()
    agent = build_agent(config, fixture_knowledge, llm, store, client)

    event = slack_message_event(f"please check {JIRA_URL}", ts="1762790400.000555")
    result = agent.process_event(slack_envelope(event, event_id="Ev0DEF001"), event)

    assert result is not None and result.action is Action.DEFLECT
    assert len(client.posted) == 1
    assert client.posted[0]["thread_ts"] == "1762790400.000555"
    assert "HubSpot" in client.posted[0]["text"]


def test_the_deflection_is_not_gated_on_an_approval(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    """Routing goes out immediately -- the channel should not stay cluttered."""

    client = FakeSlackClient()
    agent = build_agent(config, fixture_knowledge, llm, store, client)

    event = slack_message_event(f"stuck on {HUBSPOT_URL}", ts="1762790400.000666")
    agent.process_event(slack_envelope(event, event_id="Ev0DEF002"), event)

    assert len(client.posted) == 1, "no approval reaction was needed"
