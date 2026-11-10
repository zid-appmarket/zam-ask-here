"""Independent grounding verification ("does the evidence actually say this?").

This is the second opinion that makes the confidence gate meaningful. The
grader is given the drafted answer and the source passages, and nothing else -
no retrieval scores, no self-reported confidence, no instruction to be helpful.
Its only job is to decide whether each claim is actually in the sources.
"""

from __future__ import annotations

from typing import Any

from .common import UNTRUSTED_INPUT_RULES

SYSTEM = f"""\
You are a strict grounding verifier. You are given source passages and a
draft answer broken into claims. For each claim, decide whether the passages
actually support it.

{UNTRUSTED_INPUT_RULES}

VERDICTS

- "supported": the passages state the claim, or state it in different words.
- "partial": the passages support part of the claim but not all of it, or
  support it only for a narrower case than the claim states.
- "unsupported": the passages do not state it. This includes claims that are
  plausible, that you believe to be true in general, or that merely are not
  contradicted. Absence of a statement is "unsupported".
- "contradicted": the passages state something incompatible with the claim.

You are not helpful here and you are not lenient. A claim that a reader could
not confirm by reading the passages is not "supported". Do not use outside
knowledge. Do not reward confident phrasing.

Also report:
- `answer_contains_uncited_facts`: true if the draft answer text asserts a
  specific fact (a number, date, name, limit, policy, step) that does not
  appear in any claim.
- `sources_contradict_each_other`: true if the passages disagree with each
  other on the point at issue.
- `verdict_note`: one short English sentence on the weakest part.\
"""

SCHEMA: dict[str, Any] = {
    "title": "grade",
    "type": "object",
    "properties": {
        "claims": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "statement": {"type": "string"},
                    "verdict": {
                        "type": "string",
                        "enum": ["supported", "partial", "unsupported", "contradicted"],
                    },
                    "evidence_quote": {"type": "string"},
                },
                "required": ["statement", "verdict", "evidence_quote"],
                "additionalProperties": False,
            },
        },
        "answer_contains_uncited_facts": {"type": "boolean"},
        "sources_contradict_each_other": {"type": "boolean"},
        "verdict_note": {"type": "string"},
    },
    "required": [
        "claims",
        "answer_contains_uncited_facts",
        "sources_contradict_each_other",
        "verdict_note",
    ],
    "additionalProperties": False,
}


def build_user_turn(*, question: str, answer: str, claims: list[dict[str, Any]], evidence_block: str) -> str:
    claim_lines = "\n".join(
        f"{idx + 1}. {claim.get('statement', '').strip()} "
        f"(claimed sources: {', '.join(claim.get('source_ids') or []) or 'none'})"
        for idx, claim in enumerate(claims)
    ) or "(the draft answer listed no claims)"
    return "\n\n".join(
        [
            f"<internal_sources>\n{evidence_block.strip() or '(no sources were supplied)'}\n</internal_sources>",
            f"<question>\n{question.strip()}\n</question>",
            f"<draft_answer>\n{answer.strip()}\n</draft_answer>",
            f"<claims>\n{claim_lines}\n</claims>",
            "Grade every claim in <claims>. Return JSON only.",
        ]
    )
