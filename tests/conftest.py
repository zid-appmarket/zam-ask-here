"""Shared pytest fixtures.

Nothing in the suite reaches the network: the Claude client is replaced by
``FakeLLM`` and the Slack client by ``FakeSlackClient``. The knowledge base is
built from ``tests/fixtures/knowledge``, whose contents are fictional.
"""

from __future__ import annotations

from collections.abc import Iterator

import pytest

from zam_agent.config import AppConfig
from zam_agent.knowledge.ingest import KnowledgeBase
from zam_agent.llm.fake import FakeLLM
from zam_agent.pipeline import SupportPipeline
from zam_agent.store.sqlite_store import SQLiteStore

from .helpers import TODAY, build_pipeline, knowledge_config, make_config


@pytest.fixture
def config() -> AppConfig:
    return make_config()


@pytest.fixture
def store() -> Iterator[SQLiteStore]:
    instance = SQLiteStore("sqlite://:memory:")
    yield instance
    instance.close()


@pytest.fixture(scope="session")
def fixture_knowledge() -> KnowledgeBase:
    knowledge = KnowledgeBase(knowledge_config(), strict=True)
    knowledge.reload(today=TODAY)
    return knowledge


@pytest.fixture
def llm() -> FakeLLM:
    return FakeLLM()


@pytest.fixture
def pipeline(
    config: AppConfig,
    fixture_knowledge: KnowledgeBase,
    llm: FakeLLM,
    store: SQLiteStore,
) -> SupportPipeline:
    return build_pipeline(config, fixture_knowledge, llm, store)
