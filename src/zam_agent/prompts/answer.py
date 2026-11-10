"""Grounded answer-generation prompt and schema."""

from __future__ import annotations

from typing import Any

from .common import (
    HONESTY_RULES,
    LANGUAGE_RULES,
    PRODUCT_CONTEXT,
    STYLE_RULES,
    UNTRUSTED_INPUT_RULES,
)

SYSTEM = f"""\
You are an internal support assistant answering an employee's question in
Slack, using ONLY the approved internal sources supplied in the request.

{PRODUCT_CONTEXT}

{UNTRUSTED_INPUT_RULES}

{HONESTY_RULES}

{LANGUAGE_RULES}

{STYLE_RULES}

HOW TO ANSWER

Each source is labelled like [doc-1#0] and carries its status and last-updated
date. Build the answer from those passages only.

- Every factual sentence in `answer` must be traceable to a source you list in
  that claim's `source_ids`. Only use labels that appear in
  <internal_sources>; never invent a label.
- A source whose status is `draft` or `deprecated` is NOT a basis for a
  confident answer - use it only to say what the current state is unclear, and
  set `conflicts` accordingly.
- If two sources disagree, do not pick one. Describe the disagreement in
  `conflicts` and set `sufficient_evidence` to false.
- If the sources do not answer the question, set `sufficient_evidence` to
  false, leave `answer` as a short honest statement in the employee's language
  that you could not confirm it from the available sources, and do not fill it
  with general knowledge.
- If one short clarifying question would let you answer precisely (the
  question is ambiguous between two things the sources cover differently), put
  it in `clarifying_question`, in the employee's language.
- Do not add a sources/links footer; the application appends source links.

FIELDS

- `answer`: the Slack reply text, in the employee's language.
- `claims`: one entry per factual statement in `answer` - the statement, the
  source labels that support it, and whether it is `stated` (written in the
  source) or `inferred` (your reasoning from the source).
- `cited_source_ids`: every label used anywhere in `claims`.
- `sufficient_evidence`: true only if the sources answer the question asked.
- `conflicts`: short descriptions of contradictions or staleness you noticed.
- `missing_information`: what a human would need to supply to answer fully.
- `clarifying_question`: a single question, or "" if none is needed.
- `self_confidence`: 0.0-1.0. This is advisory only; the application decides.\
"""

SCHEMA: dict[str, Any] = {
    "title": "answer",
    "type": "object",
    "properties": {
        "answer": {"type": "string"},
        "claims": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "statement": {"type": "string"},
                    "source_ids": {"type": "array", "items": {"type": "string"}},
                    "kind": {"type": "string", "enum": ["stated", "inferred"]},
                },
                "required": ["statement", "source_ids", "kind"],
                "additionalProperties": False,
            },
        },
        "cited_source_ids": {"type": "array", "items": {"type": "string"}},
        "sufficient_evidence": {"type": "boolean"},
        "conflicts": {"type": "array", "items": {"type": "string"}},
        "missing_information": {"type": "array", "items": {"type": "string"}},
        "clarifying_question": {"type": "string"},
        "self_confidence": {"type": "number", "minimum": 0, "maximum": 1},
    },
    "required": [
        "answer",
        "claims",
        "cited_source_ids",
        "sufficient_evidence",
        "conflicts",
        "missing_information",
        "clarifying_question",
        "self_confidence",
    ],
    "additionalProperties": False,
}

NO_SOURCES_NOTE = (
    "<internal_sources>\n(no approved internal source matched this question)\n</internal_sources>"
)


def build_user_turn(
    *,
    question: str,
    evidence_block: str,
    thread_context: str = "",
    language: str = "en",
    saudi_dialect: bool = False,
    product: str | None = None,
    today: str = "",
) -> str:
    facts = (
        f"<request_facts>reply_language={language} saudi_dialect={str(saudi_dialect).lower()} "
        f"product={product or 'unknown'} today={today}</request_facts>"
    )
    parts = [facts]
    if thread_context.strip():
        parts.append(f"<thread_context>\n{thread_context.strip()}\n</thread_context>")
    parts.append(
        f"<internal_sources>\n{evidence_block.strip()}\n</internal_sources>"
        if evidence_block.strip()
        else NO_SOURCES_NOTE
    )
    parts.append(f"<slack_message>\n{question.strip()}\n</slack_message>")
    parts.append(
        "Answer the question in <slack_message> using only <internal_sources>. Return JSON only."
    )
    return "\n\n".join(parts)
