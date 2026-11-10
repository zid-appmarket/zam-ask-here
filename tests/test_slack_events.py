"""Slack event intake: filtering, de-duplication, loop prevention, posting."""

from __future__ import annotations

import pytest

from zam_agent.confidence import Action
from zam_agent.llm.fake import FakeLLM
from zam_agent.slackbot.app import SlackAgent
from zam_agent.slackbot.filters import event_key, should_handle
from zam_agent.store.sqlite_store import SQLiteStore

from .fakes import FakeBoltApp, FakeSlackClient, slack_envelope, slack_message_event
from .helpers import (
    BOT_USER,
    CHANNEL,
    OTHER_CHANNEL,
    OWNER_ZAM,
    answer_payload,
    classification,
    first_label,
    grade_payload,
    make_config,
)

QUESTION = "How long does ZAM app review take?"


def build_agent(
    config,
    fixture_knowledge,
    llm: FakeLLM,
    store: SQLiteStore,
    client: FakeSlackClient | None = None,
) -> SlackAgent:
    app = FakeBoltApp(client)
    return SlackAgent(config=config, knowledge=fixture_knowledge, llm=llm, store=store, app=app)


def script_answer(llm: FakeLLM, fixture_knowledge, query: str = QUESTION) -> None:
    label = first_label(fixture_knowledge, query, "zam")
    llm.script("classify", classification(category="zam_question", search_query=query))
    llm.script("answer", answer_payload(answer="App review takes 4 business days.", source_ids=[label]))
    llm.script("grade", grade_payload(verdicts=["supported"]))


# ------------------------------------------------------------------ filtering


@pytest.mark.parametrize(
    ("event", "expected_reason"),
    [
        (slack_message_event("hi", user=BOT_USER), "self_message"),
        (slack_message_event("hi", bot_id="B0OTHERBOT"), "bot_message"),
        (slack_message_event("hi", subtype="bot_message", bot_id="B0OTHERBOT"), "ignored_subtype:bot_message"),
        (slack_message_event("hi", subtype="message_changed"), "ignored_subtype:message_changed"),
        (slack_message_event("hi", subtype="message_deleted"), "ignored_subtype:message_deleted"),
        (slack_message_event("hi", subtype="channel_join"), "ignored_subtype:channel_join"),
        (slack_message_event("hi", channel=OTHER_CHANNEL), "channel_not_watched"),
        (slack_message_event("", client_msg_id=None), "empty_text"),
        (slack_message_event("hi", user="", client_msg_id=None), "no_user"),
        (slack_message_event("hi", channel_type="im"), "channel_type:im"),
        (slack_message_event("hi", app_id="A0OTHERAPP"), "app_message"),
        (slack_message_event("hi", hidden=True), "hidden_message"),
        ({"type": "reaction_added", "user": "U1"}, "unsupported_event_type:reaction_added"),
    ],
)
def test_events_the_agent_must_not_act_on(config, event, expected_reason: str) -> None:
    decision = should_handle(event, config=config.slack, bot_user_id=BOT_USER, bot_id="B0FAKEBOT1")
    assert decision.handle is False
    assert decision.reason == expected_reason


def test_a_normal_human_message_in_the_watched_channel_is_handled(config) -> None:
    decision = should_handle(
        slack_message_event(QUESTION), config=config.slack, bot_user_id=BOT_USER, bot_id="B0FAKEBOT1"
    )
    assert decision.handle is True


def test_file_share_messages_are_still_read(config) -> None:
    decision = should_handle(
        slack_message_event(QUESTION, subtype="file_share"),
        config=config.slack,
        bot_user_id=BOT_USER,
        bot_id="B0FAKEBOT1",
    )
    assert decision.handle is True


def test_event_key_prefers_the_envelope_event_id() -> None:
    event = slack_message_event(QUESTION)
    assert event_key(event, "Ev0ABC") == "evt:Ev0ABC"
    assert event_key(event) == "cmid:11111111-2222-3333-4444-555555555555"
    assert event_key({"channel": "C1", "ts": "1.0"}) == "msg:C1:1.0"


# ------------------------------------------------------------ de-duplication


def test_a_retried_delivery_posts_only_once(config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore) -> None:
    client = FakeSlackClient()
    agent = build_agent(config, fixture_knowledge, llm, store, client)
    script_answer(llm, fixture_knowledge)

    event = slack_message_event(QUESTION)
    body = slack_envelope(event)
    first = agent.process_event(body, event)
    second = agent.process_event(slack_envelope(event, retry_num=1), event)

    assert first is not None and first.action is Action.ANSWER
    assert second is None, "the retry must be dropped"
    assert len(client.posted) == 1


def test_a_second_delivery_without_an_event_id_is_still_deduplicated(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    client = FakeSlackClient()
    agent = build_agent(config, fixture_knowledge, llm, store, client)
    script_answer(llm, fixture_knowledge)

    event = slack_message_event(QUESTION)
    agent.process_event({"event": event}, event)
    agent.process_event({"event": event}, event)

    assert len(client.posted) == 1


def test_the_agent_never_processes_its_own_reply(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    """The loop guard: feeding the bot's own message back changes nothing."""

    client = FakeSlackClient()
    agent = build_agent(config, fixture_knowledge, llm, store, client)
    script_answer(llm, fixture_knowledge)

    own = slack_message_event(
        "App review takes 4 business days.", user=BOT_USER, bot_id="B0FAKEBOT1", ts="2.000200"
    )
    assert agent.process_event(slack_envelope(own, event_id="Ev0SELF"), own) is None
    assert client.posted == []
    assert llm.calls == []


# ---------------------------------------------------------------- posting


def test_an_answer_is_posted_as_a_thread_reply(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    client = FakeSlackClient()
    agent = build_agent(config, fixture_knowledge, llm, store, client)
    script_answer(llm, fixture_knowledge)

    event = slack_message_event(QUESTION, ts="1762790400.000777")
    agent.process_event(slack_envelope(event), event)

    assert len(client.posted) == 1
    post = client.posted[0]
    assert post["channel"] == CHANNEL
    assert post["thread_ts"] == "1762790400.000777"
    assert post["unfurl_links"] is False
    assert "4 business days" in post["text"]


def test_an_escalation_posts_the_ping_and_the_owner_context(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    client = FakeSlackClient()
    agent = build_agent(config, fixture_knowledge, llm, store, client)
    llm.script("classify", classification(category="zam_question", search_query="undocumented thing"))

    event = slack_message_event("What is the enterprise uninstall-refund SLA?")
    agent.process_event(slack_envelope(event), event)

    assert len(client.posted) == 2
    assert f"<@{OWNER_ZAM}>" in client.posted[0]["text"]
    assert "A question needs your confirmation" in client.posted[1]["text"]


def test_nothing_is_posted_for_a_filtered_message(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    client = FakeSlackClient()
    agent = build_agent(config, fixture_knowledge, llm, store, client)

    event = slack_message_event("thanks!")
    decision = agent.process_event(slack_envelope(event), event)

    assert decision is not None and decision.action is Action.IGNORE
    assert client.posted == []


def test_dry_run_decides_but_posts_nothing(fixture_knowledge, llm: FakeLLM, store: SQLiteStore) -> None:
    config = make_config(dry_run=True)
    client = FakeSlackClient()
    agent = build_agent(config, fixture_knowledge, llm, store, client)
    script_answer(llm, fixture_knowledge)

    event = slack_message_event(QUESTION)
    decision = agent.process_event(slack_envelope(event), event)

    assert decision is not None and decision.action is Action.ANSWER
    assert client.posted == []


def test_replies_go_to_the_channel_when_threading_is_disabled(
    fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    config = make_config(slack={"reply_in_thread": False})
    client = FakeSlackClient()
    agent = build_agent(config, fixture_knowledge, llm, store, client)
    script_answer(llm, fixture_knowledge)

    event = slack_message_event(QUESTION)
    agent.process_event(slack_envelope(event), event)

    assert client.posted[0]["thread_ts"] is None


def test_an_ack_reaction_is_added_when_enabled(fixture_knowledge, llm: FakeLLM, store: SQLiteStore) -> None:
    config = make_config(slack={"add_ack_reaction": True, "ack_reaction": "eyes"})
    client = FakeSlackClient()
    agent = build_agent(config, fixture_knowledge, llm, store, client)
    script_answer(llm, fixture_knowledge)

    event = slack_message_event(QUESTION)
    agent.process_event(slack_envelope(event), event)

    assert client.reactions and client.reactions[0]["name"] == "eyes"


def test_the_bot_mention_is_stripped_before_classification(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    client = FakeSlackClient()
    agent = build_agent(config, fixture_knowledge, llm, store, client)
    script_answer(llm, fixture_knowledge)

    event = slack_message_event(f"<@{BOT_USER}> {QUESTION}", event_type="app_mention")
    agent.process_event(slack_envelope(event), event)

    classify_call = next(call for call in llm.calls if call["purpose"] == "classify")
    assert BOT_USER not in classify_call["messages"][0]["content"]


def test_health_reports_knowledge_and_store_state(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    agent = build_agent(config, fixture_knowledge, llm, store)
    health = agent.health()
    assert health["status"] == "ok"
    assert health["knowledge"]["documents"] > 0
    assert "processed_events" in health["store"]
    assert health["mode"] == "socket"


def test_listeners_are_registered_for_messages_and_mentions(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    app = FakeBoltApp()
    SlackAgent(config=config, knowledge=fixture_knowledge, llm=llm, store=store, app=app)
    assert set(app.handlers) == {"message", "app_mention"}
