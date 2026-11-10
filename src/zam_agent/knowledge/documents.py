"""Knowledge document model and front-matter parsing.

A knowledge source is any text with metadata. Markdown files carry metadata in
YAML front matter; Notion and Drive loaders map their own properties onto the
same fields so the retrieval and confidence layers never care where a document
came from.
"""

from __future__ import annotations

import datetime as _dt
import hashlib
import re
from collections.abc import Iterable, Mapping
from dataclasses import dataclass, field
from typing import Any

import yaml

PRODUCTS = ("zam", "theme_market", "general")
AUDIENCES = ("all", "internal", "restricted")
STATUSES = ("verified", "draft", "deprecated")


class DocumentError(ValueError):
    """Raised when a knowledge document cannot be parsed."""


_FRONT_MATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n?", re.DOTALL)
_HEADING = re.compile(r"^(#{1,6})\s+(.*\S)\s*$", re.MULTILINE)

_PRODUCT_ALIASES = {
    "zam": "zam",
    "app market": "zam",
    "app_market": "zam",
    "zid app market": "zam",
    "apps": "zam",
    "theme market": "theme_market",
    "theme_market": "theme_market",
    "thememarket": "theme_market",
    "themes": "theme_market",
    "theme": "theme_market",
    "general": "general",
    "company": "general",
    "both": "general",
}


def normalize_product(value: Any) -> str:
    if value is None:
        return "general"
    if isinstance(value, (list, tuple)):
        mapped = {normalize_product(item) for item in value}
        mapped.discard("general")
        return mapped.pop() if len(mapped) == 1 else "general"
    key = str(value).strip().lower().replace("-", " ")
    return _PRODUCT_ALIASES.get(key, "general")


def _coerce_date(value: Any) -> _dt.date | None:
    if value is None:
        return None
    if isinstance(value, _dt.datetime):
        return value.date()
    if isinstance(value, _dt.date):
        return value
    text = str(value).strip()
    if not text:
        return None
    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%Y/%m/%d", "%d-%m-%Y"):
        try:
            return _dt.datetime.strptime(text, fmt).date()
        except ValueError:
            continue
    try:  # ISO 8601 with time / timezone
        return _dt.datetime.fromisoformat(text.replace("Z", "+00:00")).date()
    except ValueError:
        return None


def _coerce_tuple(value: Any) -> tuple[str, ...]:
    if value is None:
        return ()
    if isinstance(value, str):
        return tuple(part.strip() for part in value.split(",") if part.strip())
    if isinstance(value, Iterable):
        return tuple(str(item).strip() for item in value if str(item).strip())
    return (str(value),)


@dataclass(frozen=True)
class Document:
    doc_id: str
    title: str
    body: str
    source: str
    product: str = "general"
    audience: str = "all"
    status: str = "verified"
    updated: _dt.date | None = None
    source_url: str | None = None
    owner: str | None = None
    tags: tuple[str, ...] = ()
    supersedes: tuple[str, ...] = ()
    language: str = "unknown"
    extra: Mapping[str, Any] = field(default_factory=dict)

    @property
    def is_verified(self) -> bool:
        return self.status == "verified"

    @property
    def is_deprecated(self) -> bool:
        return self.status == "deprecated"

    def age_days(self, today: _dt.date | None = None) -> int | None:
        if self.updated is None:
            return None
        today = today or _dt.date.today()
        return max(0, (today - self.updated).days)

    def is_stale(self, max_age_days: int, today: _dt.date | None = None) -> bool:
        age = self.age_days(today)
        if age is None:
            # No date means we cannot vouch for freshness.
            return True
        return age > max_age_days

    def reference(self) -> str:
        """Short human-facing reference used in Slack replies."""

        if self.source_url:
            return f"<{self.source_url}|{self.title}>"
        return self.title


@dataclass(frozen=True)
class Chunk:
    chunk_id: str
    doc_id: str
    text: str
    heading: str | None
    position: int
    document: Document

    @property
    def display_source(self) -> str:
        if self.heading:
            return f"{self.document.title} › {self.heading}"
        return self.document.title


def parse_front_matter(raw: str) -> tuple[dict[str, Any], str]:
    """Split YAML front matter from the body. Missing front matter is allowed."""

    match = _FRONT_MATTER.match(raw)
    if not match:
        return {}, raw
    try:
        loaded = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError as exc:
        raise DocumentError(f"invalid YAML front matter: {exc}") from exc
    if not isinstance(loaded, dict):
        raise DocumentError("front matter must be a YAML mapping")
    return loaded, raw[match.end() :]


def _fallback_title(body: str, source: str) -> str:
    heading = _HEADING.search(body)
    if heading:
        return heading.group(2)
    for line in body.splitlines():
        if line.strip():
            return line.strip()[:120]
    return source.rsplit("/", 1)[-1]


def build_document(
    *,
    raw: str,
    source: str,
    defaults: Mapping[str, Any] | None = None,
    strict: bool = False,
) -> Document:
    """Turn raw text (+ optional front matter) into a :class:`Document`."""

    meta, body = parse_front_matter(raw)
    merged: dict[str, Any] = dict(defaults or {})
    merged.update({str(k).strip().lower(): v for k, v in meta.items()})

    body = body.strip()
    if not body:
        raise DocumentError(f"{source}: document body is empty")

    title = str(merged.get("title") or _fallback_title(body, source)).strip()
    doc_id = str(
        merged.get("id")
        or merged.get("doc_id")
        # Not a security primitive: a short stable id derived from the path.
        or hashlib.sha256(source.encode("utf-8")).hexdigest()[:12]
    ).strip()

    audience = str(merged.get("audience", "all")).strip().lower()
    if audience not in AUDIENCES:
        if strict:
            raise DocumentError(f"{source}: audience must be one of {AUDIENCES}, got {audience!r}")
        audience = "restricted"  # fail closed on an unknown audience label

    status = str(merged.get("status", "verified")).strip().lower()
    if status not in STATUSES:
        if strict:
            raise DocumentError(f"{source}: status must be one of {STATUSES}, got {status!r}")
        status = "draft"  # fail closed: unknown status is not "verified"

    known = {
        "title", "id", "doc_id", "product", "audience", "status", "updated",
        "last_updated", "source_url", "url", "owner", "tags", "supersedes", "language",
    }
    return Document(
        doc_id=doc_id,
        title=title,
        body=body,
        source=source,
        product=normalize_product(merged.get("product")),
        audience=audience,
        status=status,
        updated=_coerce_date(merged.get("updated") or merged.get("last_updated")),
        source_url=(str(merged["source_url"]).strip() if merged.get("source_url") else None)
        or (str(merged["url"]).strip() if merged.get("url") else None),
        owner=str(merged["owner"]).strip() if merged.get("owner") else None,
        tags=_coerce_tuple(merged.get("tags")),
        supersedes=_coerce_tuple(merged.get("supersedes")),
        language=str(merged.get("language", "unknown")).strip().lower(),
        extra={k: v for k, v in merged.items() if k not in known},
    )


def chunk_document(
    document: Document,
    *,
    target_chars: int = 1200,
    overlap_chars: int = 160,
) -> list[Chunk]:
    """Split a document on Markdown headings, then on size.

    Heading-aware chunking keeps an FAQ answer with its question, which matters
    much more for grounding quality than any clever embedding would.
    """

    sections = _split_by_heading(document.body)
    chunks: list[Chunk] = []
    position = 0
    for heading, text in sections:
        for piece in _split_by_size(text, target_chars, overlap_chars):
            piece = piece.strip()
            if not piece:
                continue
            chunks.append(
                Chunk(
                    chunk_id=f"{document.doc_id}#{position}",
                    doc_id=document.doc_id,
                    text=piece,
                    heading=heading,
                    position=position,
                    document=document,
                )
            )
            position += 1
    if not chunks:
        chunks.append(
            Chunk(
                chunk_id=f"{document.doc_id}#0",
                doc_id=document.doc_id,
                text=document.body.strip(),
                heading=None,
                position=0,
                document=document,
            )
        )
    return chunks


def _split_by_heading(body: str) -> list[tuple[str | None, str]]:
    matches = list(_HEADING.finditer(body))
    if not matches:
        return [(None, body)]
    sections: list[tuple[str | None, str]] = []
    preamble = body[: matches[0].start()].strip()
    if preamble:
        sections.append((None, preamble))
    for idx, match in enumerate(matches):
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(body)
        heading = match.group(2)
        text = body[match.end() : end].strip()
        if text:
            sections.append((heading, f"{heading}\n{text}"))
        else:
            sections.append((heading, heading))
    return sections


def _split_by_size(text: str, target: int, overlap: int) -> list[str]:
    if len(text) <= target:
        return [text]
    paragraphs = [p for p in re.split(r"\n\s*\n", text) if p.strip()]
    out: list[str] = []
    current = ""
    for para in paragraphs:
        if current and len(current) + len(para) + 2 > target:
            out.append(current)
            tail = current[-overlap:] if overlap else ""
            current = (tail + "\n\n" + para).strip() if tail else para
        else:
            current = f"{current}\n\n{para}".strip() if current else para
    if current:
        out.append(current)
    # A single oversized paragraph still needs hard splitting.
    final: list[str] = []
    for piece in out:
        while len(piece) > target * 2:
            final.append(piece[:target])
            piece = piece[max(0, target - overlap) :]
        final.append(piece)
    return final
