"""Realistic Slack Events API payloads, verbatim from the documented shapes.

These exercise the intake path with full envelopes (``authorizations``,
``retry_num`` headers, ``message_changed`` nesting) rather than hand-trimmed
dicts, so a shape change in Slack's payload would show up here.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from zam_agent.confidence import Action
from zam_agent.llm.fake import FakeLLM
from zam_agent.slackbot.filters import should_handle
from zam_agent.store.sqlite_store import SQLiteStore

from .fakes import FakeSlackClient
from .helpers import (
    BOT_USER,
    answer_payload,
    classification,
    first_label,
    grade_payload,
)
from .test_slack_events import build_agent

EVENTS_DIR = Path(__file__).parent / "fixtures" / "slack_events"
BOT_ID = "B0FAKEBOT1"


def load(name: str) -> tuple[dict, dict]:
    body = json.loads((EVENTS_DIR / name).read_text(encoding="utf-8"))
    return body, body["event"]


def test_every_fixture_is_valid_json_with_an_event() -> None:
    files = sorted(EVENTS_DIR.glob("*.json"))
    assert files, "no Slack event fixtures found"
    for path in files:
        body = json.loads(path.read_text(encoding="utf-8"))
        assert body["type"] == "event_callback"
        assert "event" in body and "event_id" in body


@pytest.mark.parametrize(
    ("fixture", "should_be_handled"),
    [
        ("01_question_english.json", True),
        ("02_question_arabic.json", True),
        ("03_question_saudi_dialect.json", True),
        ("04_retry_of_question_english.json", True),
        ("05_bot_own_reply.json", False),
        ("06_message_edited.json", False),
        ("07_channel_join.json", False),
        ("08_other_channel.json", False),
        ("09_thread_follow_up.json", True),
        ("10_app_mention.json", True),
        ("11_acknowledgement.json", True),
        ("12_prompt_injection.json", True),
    ],
)
def test_fixture_filtering(config, fixture: str, should_be_handled: bool) -> None:
    _body, event = load(fixture)
    decision = should_handle(event, config=config.slack, bot_user_id=BOT_USER, bot_id=BOT_ID)
    assert decision.handle is should_be_handled, f"{fixture}: {decision.reason}"


def test_the_retry_fixture_shares_the_event_id_so_it_is_deduplicated(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    first_body, first_event = load("01_question_english.json")
    retry_body, retry_event = load("04_retry_of_question_english.json")
    assert first_body["event_id"] == retry_body["event_id"]

    client = FakeSlackClient()
    agent = build_agent(config, fixture_knowledge, llm, store, client)
    query = first_event["text"]
    label = first_label(fixture_knowledge, query, "zam")
    llm.script("classify", classification(category="zam_question", search_query=query))
    llm.script("answer", answer_payload(answer="App review takes 4 business days.", source_ids=[label]))
    llm.script("grade", grade_payload(verdicts=["supported"]))

    first = agent.process_event(first_body, first_event)
    second = agent.process_event(retry_body, retry_event)

    assert first is not None and first.action is Action.ANSWER
    assert second is None
    assert len(client.posted) == 1


def test_the_acknowledgement_fixture_produces_no_reply(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    body, event = load("11_acknowledgement.json")
    client = FakeSlackClient()
    agent = build_agent(config, fixture_knowledge, llm, store, client)

    decision = agent.process_event(body, event)

    assert decision is not None and decision.action is Action.IGNORE
    assert client.posted == []
    assert llm.calls == []


def test_the_app_mention_fixture_is_answered(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    body, event = load("10_app_mention.json")
    client = FakeSlackClient()
    agent = build_agent(config, fixture_knowledge, llm, store, client)
    query = "What are the Theme Market pricing tiers?"
    label = first_label(fixture_knowledge, query, "theme_market")
    llm.script(
        "classify",
        classification(category="theme_market_question", products=["theme_market"], search_query=query),
    )
    llm.script("answer", answer_payload(answer="Basic 900, Plus 1800, Premium 3600 SAR.", source_ids=[label]))
    llm.script("grade", grade_payload(verdicts=["supported"]))

    decision = agent.process_event(body, event)

    assert decision is not None and decision.action is Action.ANSWER
    assert len(client.posted) == 1
