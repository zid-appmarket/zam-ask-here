"""Lexical retrieval over knowledge chunks (BM25 + term coverage).

Why lexical rather than embeddings: the corpus here is internal FAQ/SOP text
in Arabic and English, queries reuse the corpus vocabulary, and a BM25 index
needs no extra vendor, no network call on the hot path, and -- crucially for
this agent -- produces an *interpretable* grounding signal (which query terms
were actually found) that the confidence gate can reason about.

``EmbeddingBackend`` is the extension point: implement it and pass it to
``KnowledgeIndex`` to add dense retrieval without touching anything else.
"""

from __future__ import annotations

import datetime as _dt
import math
from collections import Counter
from collections.abc import Iterable, Sequence
from dataclasses import dataclass
from typing import Protocol

from ..language import tokenize
from .documents import Chunk, Document

# Very high-frequency words carry no retrieval signal in either language.
STOPWORDS: frozenset[str] = frozenset(
    {
        # English
        "the", "and", "for", "are", "but", "not", "you", "all", "can", "has", "have",
        "was", "were", "with", "this", "that", "from", "they", "will", "would", "there",
        "their", "what", "when", "how", "why", "who", "which", "does", "did", "our",
        "any", "its", "his", "her", "them", "then", "than", "about", "into", "also",
        "been", "being", "some", "such", "only", "very", "just", "get", "got", "please",
        "hi", "hello", "hey", "team", "guys", "thanks", "thank",
        "is", "am", "be", "of", "to", "in", "on", "at", "by", "or", "if", "it",
        "as", "so", "we", "my", "me", "us", "no", "up", "do", "re", "vs", "etc",
        "need", "want", "know", "tell", "give", "see", "use", "one", "two",
        # Arabic (normalized forms)
        "في", "من", "على", "الى", "عن", "مع", "هذا", "هذه", "ذلك", "التي", "الذي",
        "ان", "انه", "كان", "كانت", "لكن", "او", "ثم", "قد", "كل", "بعد", "قبل",
        "عند", "عندي", "هل", "ما", "لا", "نعم", "يا", "ايش", "وش", "ليش", "كيف",
        "متى", "وين", "كم", "ممكن", "ابغى", "ودي", "يكون", "عليه", "به", "له",
        "الله", "يعطيكم", "العافيه", "شكرا", "مشكور", "السلام", "عليكم", "صباح",
        "مساء", "الخير", "تمام", "طيب", "فيه", "واحد", "شي", "شيء", "بس", "عشان",
    }
)

_PRODUCT_BOOST = 1.35
_VERIFIED_BOOST = 1.12
_DRAFT_PENALTY = 0.80
_DEPRECATED_PENALTY = 0.55
_TITLE_BOOST = 1.10


class EmbeddingBackend(Protocol):
    """Optional dense-retrieval plug-in. Not required for the agent to run."""

    def embed_documents(self, texts: Sequence[str]) -> Sequence[Sequence[float]]: ...

    def embed_query(self, text: str) -> Sequence[float]: ...


@dataclass(frozen=True)
class Evidence:
    """One retrieved chunk plus the scores the confidence gate reads."""

    chunk: Chunk
    score: float
    matched_terms: tuple[str, ...]

    @property
    def document(self) -> Document:
        return self.chunk.document

    @property
    def label(self) -> str:
        """Stable short id the model cites in its answer (S1, S2, ...)."""

        return self.chunk.chunk_id


@dataclass(frozen=True)
class RetrievalResult:
    query: str
    evidence: tuple[Evidence, ...]
    coverage: float
    query_terms: tuple[str, ...]
    matched_terms: tuple[str, ...]
    conflicts: tuple[str, ...]
    stale_doc_ids: tuple[str, ...]
    excluded_restricted: int
    resolution_notes: tuple[str, ...] = ()
    conflicting_doc_ids: frozenset[str] = frozenset()

    @property
    def is_empty(self) -> bool:
        return not self.evidence

    @property
    def top_score(self) -> float:
        return self.evidence[0].score if self.evidence else 0.0

    def documents(self) -> tuple[Document, ...]:
        seen: dict[str, Document] = {}
        for item in self.evidence:
            seen.setdefault(item.document.doc_id, item.document)
        return tuple(seen.values())


def content_terms(text: str) -> list[str]:
    """Query tokens that carry meaning -- stopwords removed, order preserved."""

    seen: set[str] = set()
    out: list[str] = []
    for token in tokenize(text):
        if token in STOPWORDS or len(token) < 2:
            continue
        if token in seen:
            continue
        seen.add(token)
        out.append(token)
    return out


class KnowledgeIndex:
    """In-memory BM25 index. Rebuild on ingest; it is cheap and deterministic."""

    def __init__(
        self,
        chunks: Iterable[Chunk] = (),
        *,
        k1: float = 1.5,
        b: float = 0.75,
        embeddings: EmbeddingBackend | None = None,
    ) -> None:
        self.k1 = k1
        self.b = b
        self.embeddings = embeddings
        self._chunks: list[Chunk] = []
        self._tokens: list[Counter[str]] = []
        self._lengths: list[int] = []
        self._df: Counter[str] = Counter()
        self._avg_len = 1.0
        self.add(chunks)

    # ---------------------------------------------------------------- building

    def add(self, chunks: Iterable[Chunk]) -> None:
        for chunk in chunks:
            text = f"{chunk.document.title}\n{' '.join(chunk.document.tags)}\n{chunk.text}"
            counts = Counter(tokenize(text))
            if not counts:
                continue
            self._chunks.append(chunk)
            self._tokens.append(counts)
            self._lengths.append(sum(counts.values()))
            for term in counts:
                self._df[term] += 1
        if self._lengths:
            self._avg_len = sum(self._lengths) / len(self._lengths)

    def __len__(self) -> int:
        return len(self._chunks)

    @property
    def documents(self) -> tuple[Document, ...]:
        seen: dict[str, Document] = {}
        for chunk in self._chunks:
            seen.setdefault(chunk.doc_id, chunk.document)
        return tuple(seen.values())

    # --------------------------------------------------------------- retrieval

    def _idf(self, term: str) -> float:
        n = len(self._chunks)
        df = self._df.get(term, 0)
        if df == 0:
            return 0.0
        return math.log(1.0 + (n - df + 0.5) / (df + 0.5))

    def _idf_ceiling(self, term: str) -> float:
        """The idf this term would have if it were in the corpus exactly once.

        Used for score normalisation. A term the corpus does not contain must
        still count against the denominator, otherwise a document that matches
        only the two common words of a five-word question scores a perfect 1.0.
        """

        df = self._df.get(term, 0)
        if df:
            return self._idf(term)
        n = len(self._chunks)
        return math.log(1.0 + (n - 1 + 0.5) / 1.5)

    def _bm25(self, idx: int, terms: Sequence[str]) -> tuple[float, list[str]]:
        counts = self._tokens[idx]
        length = self._lengths[idx] or 1
        score = 0.0
        matched: list[str] = []
        for term in terms:
            tf = counts.get(term, 0)
            if tf == 0:
                continue
            matched.append(term)
            idf = self._idf(term)
            denom = tf + self.k1 * (1 - self.b + self.b * length / self._avg_len)
            score += idf * (tf * (self.k1 + 1)) / denom
        return score, matched

    def search(
        self,
        query: str,
        *,
        top_k: int = 6,
        min_score: float = 0.0,
        product: str | None = None,
        allowed_audiences: Sequence[str] = ("all",),
        max_age_days: int = 365,
        today: _dt.date | None = None,
    ) -> RetrievalResult:
        terms = content_terms(query)
        today = today or _dt.date.today()

        if not terms or not self._chunks:
            return RetrievalResult(
                query=query,
                evidence=(),
                coverage=0.0,
                query_terms=tuple(terms),
                matched_terms=(),
                conflicts=(),
                stale_doc_ids=(),
                excluded_restricted=0,
            )

        max_possible = sum(self._idf_ceiling(t) for t in terms) or 1.0

        scored: list[Evidence] = []
        excluded_restricted = 0
        for idx, chunk in enumerate(self._chunks):
            doc = chunk.document
            if doc.audience not in allowed_audiences:
                excluded_restricted += 1
                continue
            raw, matched = self._bm25(idx, terms)
            if raw <= 0:
                continue
            weight = 1.0
            if product and doc.product == product:
                weight *= _PRODUCT_BOOST
            elif product and doc.product not in (product, "general"):
                weight *= 0.85
            if doc.status == "verified":
                weight *= _VERIFIED_BOOST
            elif doc.status == "draft":
                weight *= _DRAFT_PENALTY
            else:
                weight *= _DEPRECATED_PENALTY
            title_terms = set(tokenize(doc.title))
            if title_terms & set(matched):
                weight *= _TITLE_BOOST
            normalized = min(1.0, (raw / max_possible) * weight)
            scored.append(Evidence(chunk=chunk, score=round(normalized, 6), matched_terms=tuple(matched)))

        scored.sort(key=lambda ev: (-ev.score, ev.chunk.chunk_id))
        scored, resolution_notes = resolve_supersession(scored)
        kept = [ev for ev in scored[: max(top_k, 0)] if ev.score >= min_score]

        matched_union: set[str] = set()
        for ev in kept:
            matched_union.update(ev.matched_terms)
        coverage = len(matched_union) / len(terms) if terms else 0.0

        conflicts, conflicting_doc_ids = detect_conflicts(kept)
        return RetrievalResult(
            query=query,
            evidence=tuple(kept),
            coverage=round(coverage, 4),
            query_terms=tuple(terms),
            matched_terms=tuple(sorted(matched_union)),
            conflicts=conflicts,
            stale_doc_ids=tuple(
                doc.doc_id for doc in {ev.document.doc_id: ev.document for ev in kept}.values()
                if doc.is_stale(max_age_days, today)
            ),
            excluded_restricted=excluded_restricted,
            resolution_notes=tuple(resolution_notes),
            conflicting_doc_ids=frozenset(conflicting_doc_ids),
        )


def resolve_supersession(
    evidence: Sequence[Evidence], *, marginal_ratio: float = 0.5
) -> tuple[list[Evidence], list[str]]:
    """Remove evidence that is already resolved, keep what still conflicts.

    Two cases are resolved and dropped silently:

    * A document another retrieved document explicitly ``supersedes``. The
      maintainer already decided which one is current, so this is not a
      contradiction.
    * A deprecated document that only matched marginally (its best score is
      under ``marginal_ratio`` of the top score). Flagging it would make the
      agent escalate every question that brushes past a retired document.

    A deprecated document that is a *substantial* part of the evidence is kept,
    so :func:`detect_conflicts` can flag it and the confidence gate can
    escalate. That is the intended behaviour for outdated documentation.
    """

    items = list(evidence)
    if not items:
        return items, []

    best_by_doc: dict[str, float] = {}
    docs: dict[str, Document] = {}
    for item in items:
        docs.setdefault(item.document.doc_id, item.document)
        best_by_doc[item.document.doc_id] = max(best_by_doc.get(item.document.doc_id, 0.0), item.score)
    top_score = max(best_by_doc.values()) or 1.0

    notes: list[str] = []
    drop: set[str] = set()

    for doc in docs.values():
        for superseded_id in doc.supersedes:
            if superseded_id in docs and superseded_id != doc.doc_id:
                drop.add(superseded_id)
                notes.append(f"'{docs[superseded_id].title}' was replaced by '{doc.title}'")

    for doc_id, doc in docs.items():
        if doc_id in drop or not doc.is_deprecated:
            continue
        if best_by_doc[doc_id] < marginal_ratio * top_score:
            drop.add(doc_id)
            notes.append(f"deprecated document '{doc.title}' matched only weakly and was set aside")

    if not drop:
        return items, notes
    remaining = [item for item in items if item.document.doc_id not in drop]
    # Never return an empty set just because everything was superseded.
    return (remaining or items), notes


def detect_conflicts(
    evidence: Sequence[Evidence], *, marginal_ratio: float = 0.5
) -> tuple[tuple[str, ...], set[str]]:
    """Structural contradictions the agent must not paper over.

    Returns the descriptions plus the document ids involved, so the confidence
    gate can ignore a disagreement between documents the answer never used.

    Only documents that are a substantial part of the evidence are considered
    (best score at or above ``marginal_ratio`` of the top score). Without that
    bound, two unrelated documents that disagree with each other would block
    every question whose retrieval happened to brush past them.

    Cases a maintainer has already resolved (``supersedes``, a weakly matching
    deprecated document) are handled by :func:`resolve_supersession` and never
    appear here.
    """

    best_by_doc: dict[str, float] = {}
    docs: dict[str, Document] = {}
    for item in evidence:
        docs.setdefault(item.document.doc_id, item.document)
        best_by_doc[item.document.doc_id] = max(best_by_doc.get(item.document.doc_id, 0.0), item.score)
    if not docs:
        return (), set()

    top_score = max(best_by_doc.values()) or 1.0
    considered = [
        doc for doc_id, doc in docs.items() if best_by_doc[doc_id] >= marginal_ratio * top_score
    ]

    conflicts: list[str] = []
    involved: set[str] = set()

    for doc in considered:
        if doc.is_deprecated:
            involved.add(doc.doc_id)
            conflicts.append(
                f"the only documentation found, '{doc.title}', is marked deprecated"
                if len(considered) == 1
                else f"document '{doc.title}' is marked deprecated and no current replacement was found"
            )

    # Two documents that both claim to be current on the same topic, written
    # far apart in time: one of them is almost certainly stale.
    for i, left in enumerate(considered):
        for right in considered[i + 1 :]:
            if left.is_deprecated or right.is_deprecated:
                continue
            if left.product != right.product or left.product == "general":
                continue
            if not (set(left.tags) & set(right.tags)):
                continue
            if left.updated and right.updated:
                gap = abs((left.updated - right.updated).days)
                if gap > 365:
                    involved.update({left.doc_id, right.doc_id})
                    conflicts.append(
                        f"'{left.title}' and '{right.title}' cover the same topic but were "
                        f"last updated {gap} days apart"
                    )
    return tuple(dict.fromkeys(conflicts)), involved
