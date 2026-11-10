# Operations

## The weekly loop

Escalations are the backlog, not failures.

```bash
python scripts/report_gaps.py          # unanswered questions, most frequent first
# → write the answers into knowledge/ (see knowledge/README.md)
python scripts/ingest.py --validate --query "<the question an employee asked>"
python scripts/report_gaps.py --resolve <question_key>
```

Monthly:

```bash
python scripts/ingest.py --stale       # documents past KNOWLEDGE_MAX_AGE_DAYS
python scripts/report_gaps.py --prune 90
```

A document past the freshness limit cannot support a confident answer, so an
un-refreshed knowledge base degrades into an escalation machine. Re-date what
is still true; mark the rest `deprecated` and add `supersedes:` on the
replacement.

## Rolling it out

1. `DRY_RUN=true` in the real channel for a day. The logs contain every
   decision with the exact reply the agent would have posted.
2. Read the `action` distribution. Mostly `escalate` means the knowledge base
   is thin, not that thresholds are wrong.
3. Fill the obvious gaps, then flip `DRY_RUN=false`.
4. Tell the channel what it is, what it will not do, and who to ask when it
   escalates.

## Health and metrics

`python -m zam_agent --health`, or `GET /health` and `GET /metrics` in HTTP
mode.

`/health` reports `degraded` (HTTP 503) when the knowledge index is empty — an
agent with nothing to cite can only escalate, and that should page someone.

Counters worth watching:

| Counter | Meaning |
|---|---|
| `pipeline.action.answer` / `.escalate` / `.ignore` / `.clarify` | the decision mix |
| `pipeline.escalation_suppressed` | repeat asks inside the cooldown |
| `pipeline.unhandled_error` | a bug — should be flat at zero |
| `llm.timeout` / `llm.rate_limited` / `llm.refusal` | Claude-side trouble |
| `slack.duplicate_event` | retries being dropped correctly |
| `slack.ratelimited` / `slack.post_failed` | Slack-side trouble |
| `slack.fatal.*` | a scope or install problem; it will not fix itself |
| `security.injection_attempt` | someone is probing the agent |
| `pipeline.latency_ms` | end-to-end decision time |

Logs are one JSON object per line with a `context` object. Useful queries:
`action=escalate` for the backlog, `confidence_level=medium` for threshold
tuning, `reason=…` for why a message was skipped.

## Things that will go wrong

| Symptom | Cause | Fix |
|---|---|---|
| Silence in the channel | the bot was never invited | `/invite @ZAM Ask Here` |
| Silence, logs show `channel_not_watched` | wrong `SLACK_CHANNEL_ID` | copy it from channel details |
| `slack.fatal.missing_scope` | a scope was not granted at install | add it, then reinstall the app |
| `slack.fatal.not_in_channel` | removed from the channel | re-invite |
| Everything escalates | empty or stale knowledge base | `ingest.py --list`, `--stale` |
| Duplicate answers after a restart | the database path is not on a volume | mount `DATABASE_URL`'s directory |
| Answers in the wrong language | the question is mixed-script | expected: it follows the dominant script |
| An owner pinged repeatedly | `ESCALATION_COOLDOWN_HOURS=0` | raise it |
| Costs higher than expected | `PREFILTER_ENABLED=false`, or a busy channel | re-enable the prefilter; check `llm.calls` |
| `llm.refusal` climbing | safety classifier declines | fallbacks are on by default; check `CLAUDE_ENABLE_REFUSAL_FALLBACK` |

## Tuning the thresholds

Change documents before changing numbers. When you do change numbers:

- **It answers when it should ask** → raise `CONFIDENCE_THRESHOLD` (0.68 → 0.78).
- **It escalates things that are genuinely in the docs** → check
  `simulate.py` first. If coverage is low, the document's wording does not match
  how people ask; fix the document. Only lower `MIN_EVIDENCE_COVERAGE` if the
  wording is already right.
- **It escalates on grounding** → read `verdict_note` in the diagnostics. A
  verifier that keeps saying `partial` usually means the document hedges
  ("promptly" rather than "within 5 business days").
- Never raise `MAX_UNSUPPORTED_CLAIMS` above 0 without a specific reason. It is
  the rule that stops invented facts from being posted.

## Backup and recovery

The only durable state is the SQLite file. Back it up with
`sqlite3 <path> ".backup out.db"` (safe while running, unlike `cp`). Losing it
is survivable: the agent re-answers any message Slack redelivers and may
re-ping owners about open questions. The knowledge base lives in git.

## Cost

Three Claude calls per handled message: classify (`low` effort, ~1k tokens),
answer (`medium`), grade (`medium`). The prefilter keeps chatter from costing
anything, and acknowledgements cost nothing at all. The frozen system prompts
sit behind a cache breakpoint, so repeated traffic reads them from cache —
check `llm.calls` against `pipeline.action.*` to confirm the ratio is what you
expect.
