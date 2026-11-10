"""Turn a resolved knowledge gap into a document somebody can review.

When an owner answers in Slack and marks the gap resolved, the answer is
captured but not yet trusted. This writes it into ``knowledge/_inbox/`` as
``status: draft`` — retrievable only after a human promotes it to ``verified``.

``_inbox`` begins with an underscore, so the loader ignores the whole folder.
A draft therefore cannot be quoted by the agent until it is reviewed, given a
proper ``id`` and ``updated`` date, and moved into the product directory. That
is the point: the Slack loop makes capture easy without making publication
automatic.
"""

from __future__ import annotations

import datetime as _dt
import re
from pathlib import Path

from ..store.base import KnowledgeGap

_SLUG_STRIP = re.compile(r"[^a-z0-9]+")
_PRODUCT_DIRECTORY = {"zam": "zam", "theme_market": "theme-market", "general": "general"}


def slugify(text: str, *, fallback: str = "gap", max_length: int = 48) -> str:
    """A filesystem-safe stem. Arabic questions fall back to the gap key."""

    slug = _SLUG_STRIP.sub("-", text.lower()).strip("-")
    slug = slug[:max_length].strip("-")
    return slug or fallback


def render_draft(gap: KnowledgeGap, *, today: _dt.date | None = None) -> str:
    """The draft document body, with the owner's own words preserved."""

    today = today or _dt.date.today()
    product = gap.product or "general"
    answer = (gap.resolution_note or "").strip()
    asked = _dt.datetime.fromtimestamp(gap.last_seen).strftime("%Y-%m-%d")
    thread = ""
    if gap.last_channel_id and gap.last_thread_ts:
        thread = f"<#{gap.last_channel_id}> thread `{gap.last_thread_ts}`"

    body_answer = answer or (
        "<!-- No answer was captured from the Slack thread. Write it here. -->"
    )

    return f"""---
# DRAFT captured from Slack. Review every line, then:
#   1. set a stable `id` and a real `title`
#   2. confirm the answer with the owner
#   3. set `status: verified` and today's `updated` date
#   4. move this file to knowledge/{_PRODUCT_DIRECTORY.get(product, "general")}/
# Until then the agent cannot cite it: knowledge/_inbox/ is not indexed.
id: draft-{slugify(gap.topic or gap.question, fallback=gap.question_key[:12])}
title: "[DRAFT] {(gap.topic or gap.question).strip()[:80]}"
product: {product}
audience: all
status: draft
updated: {today.isoformat()}
owner: "{gap.resolved_by or "unassigned"}"
tags: [from-slack]
language: unknown
---

## {gap.question.strip()[:200]}

{body_answer}

<!--
Captured automatically.
  asked {gap.occurrences} time(s), most recently {asked}
  {thread or "no thread recorded"}
  marked confirmed by {gap.resolved_by or "unknown"}
  gap key: {gap.question_key}

Before promoting this document:
  - Does it answer the question as asked, with concrete values (numbers,
    days, names, limits)? The verifier rejects hedged wording.
  - Add the question in the other language too, in the words employees use.
  - Set `source_url` if a canonical document exists.
-->
"""


def write_draft(
    gap: KnowledgeGap,
    directory: str | Path,
    *,
    today: _dt.date | None = None,
    overwrite: bool = False,
) -> Path:
    """Write the draft and return its path. Never silently clobbers a review."""

    target_dir = Path(directory)
    target_dir.mkdir(parents=True, exist_ok=True)
    stem = slugify(gap.topic or gap.question, fallback=gap.question_key[:12])
    path = target_dir / f"{stem}.md"
    if path.exists() and not overwrite:
        path = target_dir / f"{stem}-{gap.question_key[:8]}.md"
    path.write_text(render_draft(gap, today=today), encoding="utf-8")
    return path
