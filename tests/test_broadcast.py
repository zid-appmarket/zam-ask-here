"""Pushing an answer to the whole channel on 📣, approvers only."""

from __future__ import annotations

import pytest

from zam_agent.broadcast import BroadcastManager
from zam_agent.confidence import Action
from zam_agent.llm.fake import FakeLLM
from zam_agent.store.sqlite_store import SQLiteStore

from .fakes import FakeSlackClient, reaction_event, slack_envelope, slack_message_event
from .helpers import (
    APPROVER_NORA,
    APPROVER_OLA,
    BOT_USER,
    CHANNEL,
    EMPLOYEE,
    KB_EDITOR,
    OWNER_ZAM,
    answer_payload,
    classification,
    first_label,
    grade_payload,
    make_config,
)
from .test_slack_events import build_agent

QUESTION = "How long does ZAM app review take?"
QUESTION_TS = "1762790400.000100"
ANSWER_TS = "1762790401.000200"
ANSWER_TEXT = "App review takes 4 business days from submission.\n\n_Source: ZAM app review process_"


def thread_with_answer(question: str = QUESTION, answer: str = ANSWER_TEXT) -> list[dict]:
    return [
        slack_message_event(question, ts=QUESTION_TS),
        {
            "type": "message",
            "subtype": "bot_message",
            "bot_id": "B0FAKEBOT1",
            "user": BOT_USER,
            "text": answer,
            "ts": ANSWER_TS,
            "thread_ts": QUESTION_TS,
        },
    ]


def answer_in_thread(agent, llm: FakeLLM, fixture_knowledge, *, event_id: str = "Ev0ANS001") -> None:
    label = first_label(fixture_knowledge, QUESTION, "zam")
    llm.script("classify", classification(category="zam_question", search_query=QUESTION))
    llm.script("answer", answer_payload(answer="App review takes 4 business days.", source_ids=[label]))
    llm.script("grade", grade_payload(verdicts=["supported"]))
    event = slack_message_event(QUESTION, ts=QUESTION_TS)
    decision = agent.process_event(slack_envelope(event, event_id=event_id), event)
    assert decision is not None and decision.action is Action.ANSWER


# ------------------------------------------------------------ authorisation


@pytest.mark.parametrize("approver", [APPROVER_OLA, APPROVER_NORA])
def test_an_approver_can_push_an_answer_to_the_channel(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore, approver: str
) -> None:
    client = FakeSlackClient(thread_messages=thread_with_answer())
    agent = build_agent(config, fixture_knowledge, llm, store, client)
    answer_in_thread(agent, llm, fixture_knowledge)
    posts_before = len(client.posted)

    event = reaction_event(reaction="mega", user=approver, ts=ANSWER_TS)
    result = agent.process_reaction(slack_envelope(event, event_id="Ev0BC001"), event, added=True)

    assert result is not None and result.outcome == "broadcast"
    assert len(client.posted) == posts_before + 1
    post = client.posted[-1]
    assert post.get("thread_ts") is None, "a broadcast is a channel-level message"
    assert "4 business days" in post["text"]
    assert QUESTION in post["text"], "the question gives the answer context in the channel"


@pytest.mark.parametrize("actor", [EMPLOYEE, OWNER_ZAM, KB_EDITOR, "U0RANDOM001"])
def test_nobody_else_can_push_to_the_channel(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore, actor: str
) -> None:
    """Not even an escalation owner or knowledge editor -- only the approvers."""

    client = FakeSlackClient(thread_messages=thread_with_answer())
    agent = build_agent(config, fixture_knowledge, llm, store, client)
    answer_in_thread(agent, llm, fixture_knowledge)
    posts_before = len(client.posted)

    event = reaction_event(reaction="mega", user=actor, ts=ANSWER_TS)
    result = agent.process_reaction(slack_envelope(event, event_id="Ev0BC002"), event, added=True)

    assert result is not None and result.outcome == "not_authorized"
    assert len(client.posted) == posts_before


def test_broadcasting_fails_closed_with_no_approvers_configured(
    fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    config = make_config(slack={"broadcast_approver_user_ids": ()})
    client = FakeSlackClient(thread_messages=thread_with_answer())
    agent = build_agent(config, fixture_knowledge, llm, store, client)
    answer_in_thread(agent, llm, fixture_knowledge)
    posts_before = len(client.posted)

    event = reaction_event(reaction="mega", user=APPROVER_OLA, ts=ANSWER_TS)
    result = agent.process_reaction(slack_envelope(event, event_id="Ev0BC003"), event, added=True)

    assert result is not None and result.outcome == "not_authorized"
    assert len(client.posted) == posts_before


# ---------------------------------------------------------------- behaviour


def test_only_the_agents_own_answers_can_be_broadcast(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    """Broadcasting an employee's message would put words in their mouth."""

    client = FakeSlackClient(thread_messages=thread_with_answer())
    agent = build_agent(config, fixture_knowledge, llm, store, client)
    answer_in_thread(agent, llm, fixture_knowledge)
    posts_before = len(client.posted)

    event = reaction_event(reaction="mega", user=APPROVER_OLA, ts=QUESTION_TS)
    result = agent.process_reaction(slack_envelope(event, event_id="Ev0BC004"), event, added=True)

    assert result is not None and result.outcome == "not_an_agent_message"
    assert len(client.posted) == posts_before


def test_an_answer_is_broadcast_only_once(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    client = FakeSlackClient(thread_messages=thread_with_answer())
    agent = build_agent(config, fixture_knowledge, llm, store, client)
    answer_in_thread(agent, llm, fixture_knowledge)

    first = reaction_event(reaction="mega", user=APPROVER_OLA, ts=ANSWER_TS)
    agent.process_reaction(slack_envelope(first, event_id="Ev0BC005"), first, added=True)
    posts_after_first = len(client.posted)

    second = reaction_event(reaction="mega", user=APPROVER_NORA, ts=ANSWER_TS)
    result = agent.process_reaction(slack_envelope(second, event_id="Ev0BC006"), second, added=True)

    assert result is not None and result.outcome == "already_broadcast"
    assert len(client.posted) == posts_after_first


def test_removing_the_reaction_does_not_try_to_unsend(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    client = FakeSlackClient(thread_messages=thread_with_answer())
    agent = build_agent(config, fixture_knowledge, llm, store, client)
    answer_in_thread(agent, llm, fixture_knowledge)
    posts_before = len(client.posted)

    event = reaction_event(reaction="mega", user=APPROVER_OLA, ts=ANSWER_TS, event_type="reaction_removed")
    result = agent.process_reaction(slack_envelope(event, event_id="Ev0BC007"), event, added=False)

    assert result is not None and result.outcome == "removal_ignored"
    assert len(client.posted) == posts_before


def test_an_arabic_answer_is_broadcast_with_arabic_framing(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    arabic_q = "كم مدة مراجعة التطبيق في زام؟"
    client = FakeSlackClient(
        thread_messages=thread_with_answer(arabic_q, "مراجعة التطبيق تاخذ 4 أيام عمل.")
    )
    agent = build_agent(config, fixture_knowledge, llm, store, client)
    label = first_label(fixture_knowledge, arabic_q, "zam")
    llm.script("classify", classification(category="zam_question", search_query=arabic_q))
    llm.script("answer", answer_payload(answer="مراجعة التطبيق تاخذ 4 أيام عمل.", source_ids=[label]))
    llm.script("grade", grade_payload(verdicts=["supported"]))
    event_msg = slack_message_event(arabic_q, ts=QUESTION_TS)
    agent.process_event(slack_envelope(event_msg, event_id="Ev0BC008"), event_msg)

    event = reaction_event(reaction="mega", user=APPROVER_NORA, ts=ANSWER_TS)
    agent.process_reaction(slack_envelope(event, event_id="Ev0BC009"), event, added=True)

    assert "يستاهل المشاركة" in client.posted[-1]["text"]


def test_a_broadcast_cannot_smuggle_in_a_mention(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    client = FakeSlackClient(
        thread_messages=thread_with_answer(
            "ping <!channel> about review", "Takes 4 days <!channel> <@U0VICTIM01>"
        )
    )
    agent = build_agent(config, fixture_knowledge, llm, store, client)
    answer_in_thread(agent, llm, fixture_knowledge)

    event = reaction_event(reaction="mega", user=APPROVER_OLA, ts=ANSWER_TS)
    agent.process_reaction(slack_envelope(event, event_id="Ev0BC010"), event, added=True)

    text = client.posted[-1]["text"]
    assert "<!channel>" not in text
    assert "<@U0VICTIM01>" not in text
    assert "4 days" in text


def test_the_broadcast_links_back_to_the_thread(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    client = FakeSlackClient(thread_messages=thread_with_answer())
    agent = build_agent(config, fixture_knowledge, llm, store, client)
    answer_in_thread(agent, llm, fixture_knowledge)

    event = reaction_event(reaction="mega", user=APPROVER_OLA, ts=ANSWER_TS)
    agent.process_reaction(slack_envelope(event, event_id="Ev0BC011"), event, added=True)

    assert "See the thread" in client.posted[-1]["text"]
    assert f"<#{CHANNEL}>" in client.posted[-1]["text"]


def test_broadcasting_can_be_turned_off(fixture_knowledge, llm: FakeLLM, store: SQLiteStore) -> None:
    config = make_config(slack={"enable_broadcast": False})
    client = FakeSlackClient(thread_messages=thread_with_answer())
    agent = build_agent(config, fixture_knowledge, llm, store, client)
    answer_in_thread(agent, llm, fixture_knowledge)
    posts_before = len(client.posted)

    event = reaction_event(reaction="mega", user=APPROVER_OLA, ts=ANSWER_TS)
    result = agent.process_reaction(slack_envelope(event, event_id="Ev0BC012"), event, added=True)

    # With broadcasting off the reaction falls through to the resolve path,
    # which has nothing to do for a 'mega' reaction.
    assert result is None or result.outcome in ("disabled", "wrong_reaction")
    assert len(client.posted) == posts_before


def test_dry_run_broadcasts_nothing(fixture_knowledge, llm: FakeLLM, store: SQLiteStore) -> None:
    config = make_config(dry_run=True)
    client = FakeSlackClient(thread_messages=thread_with_answer())
    agent = build_agent(config, fixture_knowledge, llm, store, client)
    answer_in_thread(agent, llm, fixture_knowledge)
    posts_before = len(client.posted)

    event = reaction_event(reaction="mega", user=APPROVER_OLA, ts=ANSWER_TS)
    result = agent.process_reaction(slack_envelope(event, event_id="Ev0BC013"), event, added=True)

    assert result is not None and result.outcome == "broadcast"
    assert len(client.posted) == posts_before


def test_the_resolve_reaction_still_resolves_and_does_not_broadcast(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    """The two reactions do different jobs and must not be confused."""

    from zam_agent.store.sqlite_store import question_key

    unknown = "What is the enterprise uninstall-refund SLA?"
    client = FakeSlackClient()
    agent = build_agent(config, fixture_knowledge, llm, store, client)
    llm.script("classify", classification(category="zam_question", search_query=unknown))
    msg = slack_message_event(unknown, ts=QUESTION_TS)
    agent.process_event(slack_envelope(msg, event_id="Ev0BC014"), msg)
    client.thread_messages = [
        slack_message_event(unknown, ts=QUESTION_TS),
        {"type": "message", "user": OWNER_ZAM, "text": "30 days.", "ts": "1762790500.000300",
         "thread_ts": QUESTION_TS},
    ]

    event = reaction_event(reaction="white_check_mark", user=OWNER_ZAM, ts=QUESTION_TS)
    result = agent.process_reaction(slack_envelope(event, event_id="Ev0BC015"), event, added=True)

    assert result is not None and result.outcome == "resolved"
    assert store.knowledge_gap(question_key(unknown, "zam")).resolved is True


def test_the_manager_is_usable_without_slack(config) -> None:
    manager = BroadcastManager(config)  # no fetchers injected
    result = manager.handle_reaction(
        reaction_event(reaction="mega", user=APPROVER_OLA, ts=ANSWER_TS), added=True
    )
    assert result.outcome == "no_message"
