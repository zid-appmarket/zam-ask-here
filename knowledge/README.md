# Knowledge base

This directory is the agent's source of truth. **If a fact is not in here (or
in a configured Notion / Google Drive source), the agent will not state it** —
it escalates to a human instead. That is the whole design: the bot is only ever
as confident as the documents it can cite.

Everything here is reviewed like code. A pull request that changes a document
changes what the bot is allowed to say.

> This repository ships **no company content**. The directories below are empty
> on purpose — nobody should add ZAM or Theme Market facts except the people who
> own them. `_examples/` shows the shape of a document; it is skipped by the
> loader and must not be treated as real information.

## Layout

```
knowledge/
├── zam/            # ZAM (Zid App Market) documents  -> product: zam
├── theme-market/   # Theme Market documents          -> product: theme_market
├── general/        # company-wide documents           -> product: general
└── _examples/      # format examples, never ingested
```

The directory name sets the default `product`. Front matter on the file always
wins. Files and directories whose names start with `_` or `.` are **ignored**,
so drafts and notes can sit next to live content.

Accepted extensions: `.md`, `.markdown`, `.mdx`, `.txt`.

## Document format

YAML front matter, then Markdown:

```markdown
---
id: zam-app-review-sla          # stable, unique, kebab-case. Never reuse.
title: ZAM app review SLA       # shown in the Slack "Source:" footer
product: zam                    # zam | theme_market | general
audience: all                   # all | internal | restricted
status: verified                # verified | draft | deprecated
updated: 2026-11-01             # YYYY-MM-DD. Required for a confident answer.
owner: "@name-or-team"          # who to ask about this document
source_url: https://…           # canonical doc; becomes the Slack source link
tags: [review, sla, publishing]
supersedes: [zam-app-review-sla-2024]   # optional
language: en                    # en | ar | mixed (informational)
---

## A heading per question or topic

Content under the heading.
```

### Field reference

| Field | Required | Effect on the agent |
|---|---|---|
| `id` | recommended | Citation key and de-duplication key. Without one it is derived from the file path, so renaming the file changes the id. |
| `title` | recommended | Displayed in the source footer. Falls back to the first heading. |
| `product` | no | Boosts retrieval for that product; defaults from the directory. |
| `audience` | no | `all` = any watched channel. `internal` = only `INTERNAL_CHANNEL_IDS`. `restricted` = only `RESTRICTED_CHANNEL_IDS`. **An unrecognised value is treated as `restricted`** (fail closed). |
| `status` | no | Only `verified` can support a confident answer. `draft` and `deprecated` are retrieved but force escalation. **An unrecognised value becomes `draft`.** |
| `updated` | **yes, in practice** | A document with no date, or older than `KNOWLEDGE_MAX_AGE_DAYS`, counts as stale. If every source behind an answer is stale, the agent escalates. |
| `owner` | no | Carried into operational reports. |
| `source_url` | no | Rendered as the source link in Slack. Without it only the title is shown. |
| `tags` | no | Retrieval signal, and used for conflict detection between documents on the same topic. |
| `supersedes` | no | If both documents are retrieved, the agent reports a conflict rather than guessing. |

### Writing documents the agent can actually use

The retrieval layer is lexical (BM25 with Arabic normalisation), so the words
matter:

- **One heading per question.** Headings are chunk boundaries; a heading that
  reads like the question employees ask retrieves far better than "Overview".
- **Use the words people use**, including Arabic and Saudi dialect, and include
  both forms when both are in use (`القوالب` / "themes", `نسبة الإيرادات` /
  "revenue share"). A bilingual document is fine and recommended.
- **State facts explicitly.** The verifier marks anything it cannot read in the
  passage as unsupported, so "within 5 business days" works and "promptly"
  does not.
- **Keep sections self-contained.** A chunk is retrieved alone; a section that
  says "as described above" loses its meaning.
- **Never leave two live documents disagreeing.** Mark the old one
  `status: deprecated` and add `supersedes:` to the new one. Until you do, the
  agent detects the conflict and escalates — which is correct, but noisy.

## Workflow

1. Add or edit a document in a branch; have the owner review it.
2. `python scripts/ingest.py --validate` — fails on malformed front matter.
3. `python scripts/ingest.py --query "the question an employee would ask"` —
   check the right document comes back.
4. Merge and restart (or re-run ingestion) so the index picks it up.

`python scripts/report_gaps.py` lists the questions that got escalated, most
frequent first. That list is the backlog for this directory.
