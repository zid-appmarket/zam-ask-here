"""Closing a knowledge gap from Slack with a reaction."""

from __future__ import annotations

import datetime as _dt
import time

import pytest

from zam_agent.confidence import Action
from zam_agent.knowledge.drafts import render_draft, slugify, write_draft
from zam_agent.llm.fake import FakeLLM
from zam_agent.resolution import ResolutionManager
from zam_agent.slackbot.filters import reaction_event_key, should_handle_reaction
from zam_agent.store.sqlite_store import SQLiteStore, question_key

from .fakes import FakeSlackClient, reaction_event, slack_envelope, slack_message_event
from .helpers import (
    BOT_USER,
    CHANNEL,
    EMPLOYEE,
    KB_EDITOR,
    OTHER_CHANNEL,
    OUTSIDER,
    OWNER_THEME,
    OWNER_ZAM,
    classification,
    make_config,
)
from .test_slack_events import build_agent

UNKNOWN = "What is the exact uninstall-refund SLA for enterprise merchants?"
UNKNOWN_AR = "وش بالضبط إجراءات إلغاء اشتراك التاجر المؤسسي في زام؟"
QUESTION_TS = "1762790400.000100"


def escalate(agent, llm: FakeLLM, text: str = UNKNOWN, *, ts: str = QUESTION_TS, event_id: str = "Ev0ESC001"):
    """Drive a real escalation so there is something to resolve."""

    llm.script("classify", classification(category="zam_question", search_query=text))
    event = slack_message_event(text, ts=ts)
    decision = agent.process_event(slack_envelope(event, event_id=event_id), event)
    assert decision is not None and decision.action is Action.ESCALATE
    assert decision.tagged_owner is True
    return decision


def owner_reply(text: str, *, ts: str, user: str = OWNER_ZAM) -> dict:
    return {
        "type": "message",
        "user": user,
        "text": text,
        "ts": ts,
        "thread_ts": QUESTION_TS,
    }


def agent_message(text: str, *, ts: str) -> dict:
    return {
        "type": "message",
        "subtype": "bot_message",
        "bot_id": "B0FAKEBOT1",
        "user": BOT_USER,
        "text": text,
        "ts": ts,
        "thread_ts": QUESTION_TS,
    }


# ------------------------------------------------------------------ filtering


@pytest.mark.parametrize(
    ("event", "expected_reason"),
    [
        (reaction_event(user=BOT_USER), "self_reaction"),
        (reaction_event(channel=OTHER_CHANNEL), "channel_not_watched"),
        (reaction_event(item_type="file"), "reaction_on:file"),
        (reaction_event(user=""), "no_user"),
        ({"type": "message", "user": EMPLOYEE}, "unsupported_event_type:message"),
    ],
)
def test_reactions_the_agent_must_ignore(config, event, expected_reason: str) -> None:
    decision = should_handle_reaction(event, config=config.slack, bot_user_id=BOT_USER)
    assert decision.handle is False
    assert decision.reason == expected_reason


def test_a_reaction_from_a_human_in_the_watched_channel_is_handled(config) -> None:
    decision = should_handle_reaction(
        reaction_event(), config=config.slack, bot_user_id=BOT_USER
    )
    assert decision.handle is True


def test_reaction_event_keys_are_distinct_per_action_and_actor() -> None:
    added = reaction_event()
    removed = reaction_event(event_type="reaction_removed")
    assert reaction_event_key(added) != reaction_event_key(removed)
    assert reaction_event_key(added) != reaction_event_key(reaction_event(user=OWNER_THEME))
    assert reaction_event_key(added, "Ev0ABC") == "evt:Ev0ABC"


# ------------------------------------------------------------- authorisation


def test_an_owner_can_resolve(config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore) -> None:
    client = FakeSlackClient()
    agent = build_agent(config, fixture_knowledge, llm, store, client)
    escalate(agent, llm)
    client.thread_messages = [
        slack_message_event(UNKNOWN, ts=QUESTION_TS),
        agent_message("I'm unable to verify this…", ts="1762790401.000200"),
        owner_reply("Enterprise merchants get 30 days.", ts="1762790500.000300"),
    ]

    event = reaction_event(user=OWNER_ZAM, ts=QUESTION_TS)
    result = agent.process_reaction(slack_envelope(event, event_id="Ev0RXN001"), event, added=True)

    assert result is not None
    assert result.outcome == "resolved"
    assert "30 days" in result.captured_answer
    gap = store.knowledge_gap(question_key(UNKNOWN, "zam"))
    assert gap is not None and gap.resolved is True
    assert gap.resolved_by == OWNER_ZAM
    assert "30 days" in (gap.resolution_note or "")


def test_a_knowledge_editor_can_resolve(config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore) -> None:
    client = FakeSlackClient()
    agent = build_agent(config, fixture_knowledge, llm, store, client)
    escalate(agent, llm)
    client.thread_messages = [owner_reply("30 days.", ts="1762790500.000300", user=KB_EDITOR)]

    event = reaction_event(user=KB_EDITOR, ts=QUESTION_TS)
    result = agent.process_reaction(slack_envelope(event, event_id="Ev0RXN002"), event, added=True)

    assert result is not None and result.outcome == "resolved"


def test_anyone_else_cannot_resolve(config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore) -> None:
    """A reaction is not an authorisation: a passer-by must not close a gap."""

    client = FakeSlackClient()
    agent = build_agent(config, fixture_knowledge, llm, store, client)
    escalate(agent, llm)
    posts_before = len(client.posted)

    event = reaction_event(user=OUTSIDER, ts=QUESTION_TS)
    result = agent.process_reaction(slack_envelope(event, event_id="Ev0RXN003"), event, added=True)

    assert result is not None and result.outcome == "not_authorized"
    gap = store.knowledge_gap(question_key(UNKNOWN, "zam"))
    assert gap is not None and gap.resolved is False
    # Silent: nobody is publicly corrected for clicking an emoji.
    assert len(client.posted) == posts_before


def test_the_asker_cannot_resolve_their_own_question(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    client = FakeSlackClient()
    agent = build_agent(config, fixture_knowledge, llm, store, client)
    escalate(agent, llm)

    event = reaction_event(user=EMPLOYEE, ts=QUESTION_TS)
    result = agent.process_reaction(slack_envelope(event, event_id="Ev0RXN004"), event, added=True)

    assert result is not None and result.outcome == "not_authorized"


# ------------------------------------------------------------------ behaviour


def test_the_wrong_reaction_changes_nothing(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    client = FakeSlackClient()
    agent = build_agent(config, fixture_knowledge, llm, store, client)
    escalate(agent, llm)

    event = reaction_event(user=OWNER_ZAM, reaction="tada", ts=QUESTION_TS)
    result = agent.process_reaction(slack_envelope(event, event_id="Ev0RXN005"), event, added=True)

    assert result is not None and result.outcome == "wrong_reaction"
    assert store.knowledge_gap(question_key(UNKNOWN, "zam")).resolved is False


def test_a_reaction_on_a_thread_with_no_escalation_is_ignored(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    client = FakeSlackClient()
    agent = build_agent(config, fixture_knowledge, llm, store, client)

    event = reaction_event(user=OWNER_ZAM, ts="1762799999.000100")
    result = agent.process_reaction(slack_envelope(event, event_id="Ev0RXN006"), event, added=True)

    assert result is not None and result.outcome == "no_escalation"
    assert client.posted == []


def test_a_reaction_on_a_reply_resolves_the_whole_thread(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    """The owner may react on their own reply, not the original question."""

    client = FakeSlackClient()
    agent = build_agent(config, fixture_knowledge, llm, store, client)
    escalate(agent, llm)
    reply_ts = "1762790500.000300"
    client.thread_messages = [
        slack_message_event(UNKNOWN, ts=QUESTION_TS),
        owner_reply("Enterprise merchants get 30 days.", ts=reply_ts),
    ]

    event = reaction_event(user=OWNER_ZAM, ts=reply_ts)
    result = agent.process_reaction(slack_envelope(event, event_id="Ev0RXN007"), event, added=True)

    assert result is not None and result.outcome == "resolved"
    assert result.thread_ts == QUESTION_TS
    assert "30 days" in result.captured_answer


def test_resolving_confirms_in_the_thread(config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore) -> None:
    client = FakeSlackClient()
    agent = build_agent(config, fixture_knowledge, llm, store, client)
    escalate(agent, llm)
    client.thread_messages = [owner_reply("30 days.", ts="1762790500.000300")]
    posts_before = len(client.posted)

    event = reaction_event(user=OWNER_ZAM, ts=QUESTION_TS)
    agent.process_reaction(slack_envelope(event, event_id="Ev0RXN008"), event, added=True)

    assert len(client.posted) == posts_before + 1
    post = client.posted[-1]
    assert post["thread_ts"] == QUESTION_TS
    assert f"<@{OWNER_ZAM}>" in post["text"]
    assert "saved your answer" in post["text"]


def test_an_arabic_question_is_confirmed_in_arabic(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    client = FakeSlackClient()
    agent = build_agent(config, fixture_knowledge, llm, store, client)
    escalate(agent, llm, UNKNOWN_AR)
    client.thread_messages = [owner_reply("ثلاثين يوم.", ts="1762790500.000300")]

    event = reaction_event(user=OWNER_ZAM, ts=QUESTION_TS)
    agent.process_reaction(slack_envelope(event, event_id="Ev0RXN009"), event, added=True)

    assert "سجّلتها كمؤكدة" in client.posted[-1]["text"]


def test_resolving_without_a_written_answer_says_so(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    client = FakeSlackClient()
    agent = build_agent(config, fixture_knowledge, llm, store, client)
    escalate(agent, llm)
    client.thread_messages = [slack_message_event(UNKNOWN, ts=QUESTION_TS)]  # no reply

    event = reaction_event(user=OWNER_ZAM, ts=QUESTION_TS)
    result = agent.process_reaction(slack_envelope(event, event_id="Ev0RXN010"), event, added=True)

    assert result is not None and result.outcome == "resolved"
    assert result.captured_answer == ""
    assert "nothing was saved" in client.posted[-1]["text"]


def test_the_agents_own_messages_are_not_captured_as_the_answer(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    client = FakeSlackClient()
    agent = build_agent(config, fixture_knowledge, llm, store, client)
    escalate(agent, llm)
    client.thread_messages = [
        slack_message_event(UNKNOWN, ts=QUESTION_TS),
        agent_message("I'm unable to verify this answer", ts="1762790401.000200"),
        owner_reply("Enterprise merchants get 30 days.", ts="1762790500.000300"),
    ]

    event = reaction_event(user=OWNER_ZAM, ts=QUESTION_TS)
    result = agent.process_reaction(slack_envelope(event, event_id="Ev0RXN011"), event, added=True)

    assert result is not None
    assert "unable to verify" not in result.captured_answer
    assert result.captured_answer == "Enterprise merchants get 30 days."


def test_the_original_question_is_not_captured_as_the_answer(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    client = FakeSlackClient()
    agent = build_agent(config, fixture_knowledge, llm, store, client)
    escalate(agent, llm)
    client.thread_messages = [
        slack_message_event(UNKNOWN, ts=QUESTION_TS),
        owner_reply("30 days.", ts="1762790500.000300"),
    ]

    event = reaction_event(user=OWNER_ZAM, ts=QUESTION_TS)
    result = agent.process_reaction(slack_envelope(event, event_id="Ev0RXN012"), event, added=True)

    assert result is not None
    assert UNKNOWN not in result.captured_answer


def test_a_captured_answer_cannot_smuggle_in_a_mention_or_a_secret(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    client = FakeSlackClient()
    agent = build_agent(config, fixture_knowledge, llm, store, client)
    escalate(agent, llm)
    client.thread_messages = [
        owner_reply(
            "30 days <!channel> <@U0VICTIM01>, key sk-ant-api03-LEAKEDKEY123",
            ts="1762790500.000300",
        )
    ]

    event = reaction_event(user=OWNER_ZAM, ts=QUESTION_TS)
    result = agent.process_reaction(slack_envelope(event, event_id="Ev0RXN013"), event, added=True)

    assert result is not None
    assert "<!channel>" not in result.captured_answer
    assert "<@U0VICTIM01>" not in result.captured_answer
    assert "sk-ant-api03-LEAKEDKEY123" not in result.captured_answer
    assert "30 days" in result.captured_answer


def test_resolving_twice_is_a_no_op(config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore) -> None:
    client = FakeSlackClient()
    agent = build_agent(config, fixture_knowledge, llm, store, client)
    escalate(agent, llm)
    client.thread_messages = [owner_reply("30 days.", ts="1762790500.000300")]

    first_event = reaction_event(user=OWNER_ZAM, ts=QUESTION_TS)
    agent.process_reaction(slack_envelope(first_event, event_id="Ev0RXN014"), first_event, added=True)
    posts_after_first = len(client.posted)

    second_event = reaction_event(user=OWNER_THEME, ts=QUESTION_TS)
    second = agent.process_reaction(
        slack_envelope(second_event, event_id="Ev0RXN015"), second_event, added=True
    )

    assert second is not None and second.outcome == "already_resolved"
    assert len(client.posted) == posts_after_first


def test_a_duplicate_reaction_delivery_is_dropped(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    client = FakeSlackClient()
    agent = build_agent(config, fixture_knowledge, llm, store, client)
    escalate(agent, llm)
    client.thread_messages = [owner_reply("30 days.", ts="1762790500.000300")]

    event = reaction_event(user=OWNER_ZAM, ts=QUESTION_TS)
    body = slack_envelope(event, event_id="Ev0RXN016")
    first = agent.process_reaction(body, event, added=True)
    second = agent.process_reaction(body, event, added=True)

    assert first is not None and first.outcome == "resolved"
    assert second is None


def test_removing_the_reaction_reopens_the_gap(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    client = FakeSlackClient()
    agent = build_agent(config, fixture_knowledge, llm, store, client)
    escalate(agent, llm)
    client.thread_messages = [owner_reply("30 days.", ts="1762790500.000300")]
    key = question_key(UNKNOWN, "zam")

    add = reaction_event(user=OWNER_ZAM, ts=QUESTION_TS)
    agent.process_reaction(slack_envelope(add, event_id="Ev0RXN017"), add, added=True)
    assert store.knowledge_gap(key).resolved is True

    remove = reaction_event(user=OWNER_ZAM, ts=QUESTION_TS, event_type="reaction_removed")
    result = agent.process_reaction(slack_envelope(remove, event_id="Ev0RXN018"), remove, added=False)

    assert result is not None and result.outcome == "reopened"
    assert store.knowledge_gap(key).resolved is False
    assert "Reopened" in client.posted[-1]["text"]
    # Reopening must not re-ping the owner.
    assert f"<@{OWNER_ZAM}>" not in client.posted[-1]["text"]


def test_removing_a_reaction_from_an_unresolved_gap_does_nothing(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    client = FakeSlackClient()
    agent = build_agent(config, fixture_knowledge, llm, store, client)
    escalate(agent, llm)

    remove = reaction_event(user=OWNER_ZAM, ts=QUESTION_TS, event_type="reaction_removed")
    result = agent.process_reaction(slack_envelope(remove, event_id="Ev0RXN019"), remove, added=False)

    assert result is not None and result.outcome == "not_resolved"


def test_resolution_can_be_turned_off(fixture_knowledge, llm: FakeLLM, store: SQLiteStore) -> None:
    config = make_config(slack={"enable_slack_resolution": False})
    client = FakeSlackClient()
    agent = build_agent(config, fixture_knowledge, llm, store, client)
    escalate(agent, llm)

    event = reaction_event(user=OWNER_ZAM, ts=QUESTION_TS)
    result = agent.process_reaction(slack_envelope(event, event_id="Ev0RXN020"), event, added=True)

    assert result is not None and result.outcome == "disabled"
    assert store.knowledge_gap(question_key(UNKNOWN, "zam")).resolved is False


def test_dry_run_resolves_nothing_in_slack(fixture_knowledge, llm: FakeLLM, store: SQLiteStore) -> None:
    config = make_config(dry_run=True)
    client = FakeSlackClient()
    agent = build_agent(config, fixture_knowledge, llm, store, client)
    escalate(agent, llm)
    client.thread_messages = [owner_reply("30 days.", ts="1762790500.000300")]
    posts_before = len(client.posted)

    event = reaction_event(user=OWNER_ZAM, ts=QUESTION_TS)
    result = agent.process_reaction(slack_envelope(event, event_id="Ev0RXN021"), event, added=True)

    assert result is not None and result.outcome == "resolved"
    assert len(client.posted) == posts_before


def test_a_capture_failure_still_resolves_the_gap(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    """Slack being down must not block the owner from closing the gap."""

    client = FakeSlackClient()
    agent = build_agent(config, fixture_knowledge, llm, store, client)
    escalate(agent, llm)

    def explode(_channel: str, _thread: str):
        raise RuntimeError("slack unavailable")

    agent.resolution.thread_fetcher = explode

    event = reaction_event(user=OWNER_ZAM, ts=QUESTION_TS)
    result = agent.process_reaction(slack_envelope(event, event_id="Ev0RXN022"), event, added=True)

    assert result is not None and result.outcome == "resolved"
    assert result.captured_answer == ""


def test_a_resolved_question_can_be_escalated_again_later(
    config, fixture_knowledge, llm: FakeLLM, store: SQLiteStore
) -> None:
    """Resolving clears the cooldown, so an unfixed gap is raised again."""

    client = FakeSlackClient()
    agent = build_agent(config, fixture_knowledge, llm, store, client)
    escalate(agent, llm)
    client.thread_messages = [owner_reply("30 days.", ts="1762790500.000300")]

    event = reaction_event(user=OWNER_ZAM, ts=QUESTION_TS)
    agent.process_reaction(slack_envelope(event, event_id="Ev0RXN023"), event, added=True)

    second = escalate(agent, llm, ts="1762799000.000100", event_id="Ev0ESC002")
    assert second.tagged_owner is True


def test_the_manager_is_usable_without_slack() -> None:
    """ResolutionManager makes no Slack calls of its own."""

    store = SQLiteStore("sqlite://:memory:")
    config = make_config()
    key = question_key("q", "zam")
    store.record_escalation(
        question_key=key,
        channel_id=CHANNEL,
        thread_ts="1.000100",
        product="zam",
        owner_user_id=OWNER_ZAM,
        topic="t",
        question="q",
    )
    store.upsert_knowledge_gap(
        question_key=key, question="q", topic="t", product="zam", channel_id=CHANNEL, thread_ts="1.000100"
    )
    manager = ResolutionManager(config, store)  # no thread_lookup, no thread_fetcher

    result = manager.handle_reaction(reaction_event(user=OWNER_ZAM, ts="1.000100"), added=True)

    assert result.outcome == "resolved"
    assert result.captured_answer == ""
    store.close()


# --------------------------------------------------------------- draft output


def test_a_draft_document_is_written_for_review(tmp_path, config, fixture_knowledge, llm, store) -> None:
    client = FakeSlackClient()
    agent = build_agent(config, fixture_knowledge, llm, store, client)
    escalate(agent, llm)
    client.thread_messages = [owner_reply("Enterprise merchants get 30 days.", ts="1762790500.000300")]
    event = reaction_event(user=OWNER_ZAM, ts=QUESTION_TS)
    agent.process_reaction(slack_envelope(event, event_id="Ev0RXN024"), event, added=True)

    gap = store.knowledge_gap(question_key(UNKNOWN, "zam"))
    path = write_draft(gap, tmp_path, today=_dt.date(2026, 11, 10))
    text = path.read_text(encoding="utf-8")

    assert path.parent == tmp_path
    assert "status: draft" in text, "a captured answer must never be born verified"
    assert "Enterprise merchants get 30 days." in text
    assert UNKNOWN in text
    assert "product: zam" in text
    assert OWNER_ZAM in text
    assert "knowledge/zam/" in text


def test_a_draft_is_not_indexed_because_the_inbox_is_underscored() -> None:
    from zam_agent.knowledge.loaders.markdown_loader import MarkdownLoader

    from .helpers import FIXTURE_KNOWLEDGE

    documents = list(MarkdownLoader(directory=str(FIXTURE_KNOWLEDGE)).load())
    assert all(not doc.source.startswith("markdown:_inbox/") for doc in documents)


def test_a_draft_without_a_captured_answer_says_what_is_missing(tmp_path) -> None:
    from zam_agent.store.base import KnowledgeGap

    gap = KnowledgeGap(
        question_key="deadbeef1234",
        question="وش سياسة الاسترجاع للقوالب المدفوعة؟",
        topic="paid theme refunds",
        product="theme_market",
        occurrences=2,
        first_seen=time.time(),
        last_seen=time.time(),
        last_channel_id=CHANNEL,
        last_thread_ts=QUESTION_TS,
        resolved=True,
        resolved_at=time.time(),
        resolved_by=OWNER_THEME,
        resolution_note=None,
    )
    text = render_draft(gap, today=_dt.date(2026, 11, 10))

    assert "No answer was captured" in text
    assert "knowledge/theme-market/" in text
    path = write_draft(gap, tmp_path)
    assert path.exists()


def test_two_drafts_for_different_gaps_do_not_overwrite_each_other(tmp_path) -> None:
    from zam_agent.store.base import KnowledgeGap

    def gap(key: str) -> KnowledgeGap:
        return KnowledgeGap(
            question_key=key,
            question="same topic, different question",
            topic="shared topic",
            product="zam",
            occurrences=1,
            first_seen=time.time(),
            last_seen=time.time(),
            last_channel_id=CHANNEL,
            last_thread_ts=None,
            resolved=True,
            resolved_by=OWNER_ZAM,
            resolution_note="answer",
        )

    first = write_draft(gap("aaaaaaaa1111"), tmp_path)
    second = write_draft(gap("bbbbbbbb2222"), tmp_path)

    assert first != second
    assert first.exists() and second.exists()


def test_an_arabic_topic_falls_back_to_the_gap_key_for_the_filename() -> None:
    assert slugify("وش سياسة الاسترجاع", fallback="abc123") == "abc123"
    assert slugify("Theme Market pricing tiers!") == "theme-market-pricing-tiers"
