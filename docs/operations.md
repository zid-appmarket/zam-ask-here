# Operations

## The loop

Escalations are the backlog, not failures. Most of it happens in Slack.

**Owners, in the channel.** When the agent tags you, answer in the thread and
add :white_check_mark: (`RESOLVE_REACTION`). The agent saves what you wrote,
marks the gap closed and confirms in the thread. Removing the reaction reopens
it. That is the whole owner-facing workflow — no CLI.

**Approvers (Ola, Nora), in the channel.** Answers stay in their thread. React
📣 on one to put it in front of the whole channel. Nobody else's 📣 does
anything, and only the agent's own answers can be pushed.

**Whoever maintains the knowledge base, weekly:**

```bash
python scripts/report_gaps.py --resolved    # what owners confirmed, with their answers
python scripts/report_gaps.py --draft-all   # write each one into knowledge/_inbox/
# review each draft: confirm the wording, set `status: verified` and a date,
# then move it into knowledge/zam|theme-market|general/
python scripts/ingest.py --validate --query "<the question an employee asked>"
python scripts/report_gaps.py              # whatever nobody closed
```

A draft in `knowledge/_inbox/` is **not** retrievable — the loader skips any
path starting with `_`. So a captured Slack answer cannot be quoted by the
agent until a human promotes it. Review the wording while you do: the verifier
rejects hedging, so "promptly" has to become "within N business days" before
the agent will state it confidently.

Monthly:

```bash
python scripts/sync_docs.py --dry-run  # what changed in the help centres
python scripts/sync_docs.py            # take the changes, review the diff
python scripts/ingest.py --validate
python scripts/ingest.py --stale       # documents past KNOWLEDGE_MAX_AGE_DAYS
python scripts/report_gaps.py --prune 90
```

The sync is the cheapest maintenance there is: when the docs team updates a
page, re-running it brings the agent along, and the diff tells you exactly what
changed. Worth a scheduled job once you trust it.

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
| `resolution.resolved` / `.reopened` | owners closing gaps from Slack |
| `resolution.unauthorized` | someone without permission tried to close one |
| `broadcast.posted` | answers pushed to the channel by an approver |
| `broadcast.unauthorized` | a 📣 from someone who is not an approver |
| `pipeline.deflected.*` | ticket links and incidents redirected to HubSpot |
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
| A ✅ does nothing | the reactor is not an owner or editor | add them to `KNOWLEDGE_EDITOR_USER_IDS` |
| A 📣 does nothing | the reactor is not in `BROADCAST_APPROVER_USER_IDS`, or that list is empty | add them; the startup warning names this |
| A 📣 on someone's question does nothing | only the agent's own answers can be broadcast | react on the agent's reply instead |
| A real question gets the HubSpot nudge | it contained a ticket link, which always wins | ask it without the link, or set `DEFLECT_TECHNICAL_ISSUES=false` |
| A ticket link is not deflected | an unrecognised host | check `pipeline.deflected.*`; the host list is in `src/zam_agent/triage.py` |
| The sync fetches nothing | the three documentation hosts are not reachable | they are allowed on the `zam-ask-here` cloud environment; locally no setup is needed |
| A synced page reads as navigation | the site changed its markup | `python scripts/sync_docs.py --url <page> --preview` shows the extraction |
| An answer quotes a stale synced page | the upstream page is old | fix it upstream, or add a hand-written document that `supersedes:` the synced id |
| A ✅ does nothing, and `slack.reaction_filtered.*` is rising | `reactions:read` missing, or events not subscribed | re-check the manifest, reinstall |
| `--draft-all` says nothing to draft | owners resolved without writing an answer in the thread | the reply has to be *in the thread*, after the question |
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

The only durable state is the SQLite file — which now also holds the answers
owners wrote in Slack, until somebody folds them into `knowledge/`. Draft them
out (`--draft-all`) rather than leaving them only in the database. Back it up with
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
