"""Document parsing, chunking, retrieval, audience scoping and conflict handling."""

from __future__ import annotations

import datetime as _dt

import pytest

from zam_agent.knowledge.documents import DocumentError, build_document, chunk_document
from zam_agent.knowledge.index import KnowledgeIndex, content_terms
from zam_agent.knowledge.ingest import KnowledgeBase, format_evidence_block
from zam_agent.knowledge.loaders.markdown_loader import MarkdownLoader

from .helpers import FIXTURE_KNOWLEDGE, TODAY, knowledge_config


def test_front_matter_is_parsed_and_normalised() -> None:
    doc = build_document(
        raw=(
            "---\n"
            "id: doc-1\n"
            "title: Pricing\n"
            "product: Theme Market\n"
            "status: verified\n"
            "updated: 2026-05-01\n"
            "tags: pricing, tiers\n"
            "---\n"
            "# Pricing\n\nThree tiers.\n"
        ),
        source="markdown:test.md",
    )
    assert doc.doc_id == "doc-1"
    assert doc.product == "theme_market"
    assert doc.updated == _dt.date(2026, 5, 1)
    assert doc.tags == ("pricing", "tiers")
    assert doc.is_verified


def test_unknown_audience_fails_closed_to_restricted() -> None:
    doc = build_document(
        raw="---\naudience: maybe-public\n---\nbody\n",
        source="markdown:test.md",
    )
    assert doc.audience == "restricted"


def test_unknown_status_fails_closed_to_draft() -> None:
    doc = build_document(raw="---\nstatus: looks-fine\n---\nbody\n", source="markdown:test.md")
    assert doc.status == "draft"
    assert not doc.is_verified


def test_strict_mode_rejects_bad_metadata() -> None:
    with pytest.raises(DocumentError):
        build_document(raw="---\nstatus: nope\n---\nbody\n", source="markdown:test.md", strict=True)


def test_empty_body_is_rejected() -> None:
    with pytest.raises(DocumentError):
        build_document(raw="---\ntitle: x\n---\n\n", source="markdown:test.md")


def test_missing_date_counts_as_stale() -> None:
    doc = build_document(raw="---\ntitle: x\n---\nbody\n", source="markdown:test.md")
    assert doc.updated is None
    assert doc.is_stale(365, TODAY) is True


def test_chunking_splits_on_headings() -> None:
    doc = build_document(
        raw="# A\n\nfirst\n\n## B\n\nsecond\n\n## C\n\nthird\n",
        source="markdown:test.md",
    )
    chunks = chunk_document(doc)
    assert [chunk.heading for chunk in chunks] == ["A", "B", "C"]
    assert "first" in chunks[0].text


def test_oversized_section_is_split_with_overlap() -> None:
    body = "# Big\n\n" + "\n\n".join(f"paragraph {i} " + "x" * 200 for i in range(12))
    doc = build_document(raw=body, source="markdown:big.md")
    chunks = chunk_document(doc, target_chars=500, overlap_chars=80)
    assert len(chunks) > 1
    assert all(len(chunk.text) < 1200 for chunk in chunks)


def test_markdown_loader_infers_product_from_directory_and_skips_underscores() -> None:
    documents = list(MarkdownLoader(directory=str(FIXTURE_KNOWLEDGE), strict=True).load())
    ids = {doc.doc_id for doc in documents}
    assert "zam-app-review" in ids
    assert "theme-market-pricing" in ids
    # tests/fixtures/knowledge/README.md must not be ingested as knowledge.
    assert not any("README" in doc.title for doc in documents)
    by_id = {doc.doc_id: doc for doc in documents}
    assert by_id["general-support-hours"].product == "general"
    assert by_id["theme-market-refunds"].product == "theme_market"


def test_content_terms_drop_stopwords_in_both_languages() -> None:
    assert "the" not in content_terms("what is the revenue share")
    assert "revenue" in content_terms("what is the revenue share")
    terms = content_terms("وش هي مدة مراجعة التطبيق في زام")
    assert "وش" not in terms
    assert "مراجعه" in terms


@pytest.mark.parametrize(
    ("query", "product", "expected_doc"),
    [
        ("How long does app review take?", "zam", "zam-app-review"),
        ("كم مدة مراجعة التطبيق", "zam", "zam-app-review"),
        ("what is the revenue share", "zam", "zam-revenue-share"),
        ("نسبة الإيرادات في زام", "zam", "zam-revenue-share"),
        ("Theme Market pricing tiers", "theme_market", "theme-market-pricing"),
        ("سياسة الاسترجاع للقوالب", "theme_market", "theme-market-refunds"),
        ("partner support hours", None, "general-support-hours"),
    ],
)
def test_retrieval_finds_the_right_document(
    fixture_knowledge: KnowledgeBase, query: str, product: str | None, expected_doc: str
) -> None:
    result = fixture_knowledge.retrieve(query, product=product, today=TODAY)
    assert result.evidence, f"nothing retrieved for {query!r}"
    assert result.evidence[0].document.doc_id == expected_doc


def test_retrieval_returns_nothing_for_an_unrelated_query(fixture_knowledge: KnowledgeBase) -> None:
    result = fixture_knowledge.retrieve("office parking permit renewal", today=TODAY)
    assert result.is_empty or result.coverage < 0.34


def test_internal_documents_need_an_internal_channel(fixture_knowledge: KnowledgeBase) -> None:
    public = fixture_knowledge.retrieve(
        "who is paged for a ZAM outage", product="zam", allow_internal=False, today=TODAY
    )
    assert all(ev.document.audience != "internal" for ev in public.evidence)

    internal = fixture_knowledge.retrieve(
        "who is paged for a ZAM outage", product="zam", allow_internal=True, today=TODAY
    )
    assert any(ev.document.doc_id == "zam-internal-matrix" for ev in internal.evidence)


def test_restricted_documents_are_withheld_unless_explicitly_allowed(
    fixture_knowledge: KnowledgeBase,
) -> None:
    withheld = fixture_knowledge.retrieve(
        "per-partner revenue figures for Partner Alpha", product="zam", today=TODAY
    )
    assert all(ev.document.audience != "restricted" for ev in withheld.evidence)
    assert withheld.excluded_restricted > 0

    allowed = fixture_knowledge.retrieve(
        "per-partner revenue figures for Partner Alpha",
        product="zam",
        allow_restricted=True,
        today=TODAY,
    )
    assert any(ev.document.doc_id == "zam-restricted-partner-revenue" for ev in allowed.evidence)


def test_deprecated_only_result_is_reported_as_a_conflict(fixture_knowledge: KnowledgeBase) -> None:
    result = fixture_knowledge.retrieve("when are ZAM payouts issued", product="zam", today=TODAY)
    assert any(ev.document.doc_id == "zam-payouts-2024" for ev in result.evidence)
    assert result.conflicts, "a deprecated-only answer must be flagged"


def test_two_current_documents_far_apart_in_time_conflict(fixture_knowledge: KnowledgeBase) -> None:
    result = fixture_knowledge.retrieve("Vitrin submission checklist checks", product="theme_market", today=TODAY)
    doc_ids = {ev.document.doc_id for ev in result.evidence}
    assert {"theme-vitrin-a", "theme-vitrin-b"} <= doc_ids
    assert result.conflicts


def test_stale_documents_are_reported(fixture_knowledge: KnowledgeBase) -> None:
    result = fixture_knowledge.retrieve("how do I get a sandbox store", product="zam", today=TODAY)
    assert "zam-sandbox-stale" in result.stale_doc_ids


def test_supersession_replaces_rather_than_conflicts() -> None:
    old = build_document(
        raw="---\nid: old\ntitle: Old\nproduct: zam\nstatus: deprecated\nupdated: 2023-01-01\n"
        "tags: [payouts]\n---\n# Payouts\n\nPayouts on the 1st.\n",
        source="markdown:old.md",
    )
    new = build_document(
        raw="---\nid: new\ntitle: New\nproduct: zam\nstatus: verified\nupdated: 2026-10-01\n"
        "tags: [payouts]\nsupersedes: [old]\n---\n# Payouts\n\nPayouts on the 15th.\n",
        source="markdown:new.md",
    )
    index = KnowledgeIndex([c for doc in (old, new) for c in chunk_document(doc)])
    result = index.search("when are payouts issued", top_k=5, product="zam", today=TODAY)
    assert {ev.document.doc_id for ev in result.evidence} == {"new"}
    assert result.conflicts == ()
    assert result.resolution_notes


def test_evidence_block_carries_labels_and_metadata(fixture_knowledge: KnowledgeBase) -> None:
    result = fixture_knowledge.retrieve("how long does app review take", product="zam", today=TODAY)
    block = format_evidence_block(result.evidence)
    assert f"[{result.evidence[0].label}]" in block
    assert "status=" in block and "updated=" in block


def test_duplicate_ids_keep_the_first_document(tmp_path) -> None:
    for name in ("a.md", "b.md"):
        (tmp_path / name).write_text(
            f"---\nid: same-id\ntitle: {name}\nstatus: verified\nupdated: 2026-01-01\n---\nbody {name}\n",
            encoding="utf-8",
        )
    knowledge = KnowledgeBase(
        knowledge_config(str(tmp_path)),
        loaders=[MarkdownLoader(directory=str(tmp_path))],
    )
    report = knowledge.reload(today=TODAY)
    assert report.documents == 1
    assert report.duplicate_doc_ids == ["same-id"]
