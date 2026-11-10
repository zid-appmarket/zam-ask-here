# ZAM Ask Here

A Slack support agent for **ZAM** (Zid App Market) and **Theme Market**.

It watches **#zam-ask-here** (`C0204TKHWSZ`), answers employees' questions in
Arabic (including Saudi dialect) or English using only approved internal
documentation, cites its sources — and **mentions a designated human whenever it
cannot verify an answer**, instead of guessing. When an owner answers in the
thread and ticks it off, the agent keeps that answer for the knowledge base.

```
Employee: وش مدة مراجعة التطبيق في زام؟
   Agent: مراجعة التطبيق تاخذ 4 أيام عمل من وقت الرفع.
          المصدر: ZAM app review process

Employee: What is the enterprise uninstall-refund SLA?
   Agent: I'm unable to verify this answer from the available sources, and I
          don't want to provide inaccurate information. @zam-owner, could you
          please confirm this?
          What needs confirming:
          • no approved internal source matched the question

Employee: any update on https://zid.atlassian.net/browse/ZAMCASE-4821 ?
   Agent: This looks like a technical issue, and this channel is for ZAM and
          Theme Market questions only. Please raise it as a HubSpot ticket so
          it gets tracked and picked up by the team that owns it.
```

> **This repository ships no company content.** `knowledge/` is empty by
> design — see [Fill the knowledge base](#4-fill-the-knowledge-base). Until
> somebody adds documents, the agent escalates every question, which is the
> correct behaviour for an agent with nothing to cite.

---

## Contents

- [How it decides](#how-it-decides)
- [Architecture](#architecture)
- [Setup](#setup)
- [Running it](#running-it)
- [Deployment](#deployment)
- [Operating it](#operating-it)
- [Configuration reference](#configuration-reference)
- [Testing](#testing)
- [Security notes](#security-notes)
- [Assumptions and open questions](#assumptions-and-open-questions)

---

## How it decides

Every message goes through the same pipeline. Each stage can stop it.

```
Slack event
   │
   ├─ 1. Intake filter      bot? self? wrong channel? edit/join? duplicate? ──► drop
   ├─ 2. Cheap prefilter    acknowledgement, or no question and no product word ──► drop
   ├─ 2b. Ticket detector   HubSpot or Jira link ──► redirect to HubSpot, stop
   ├─ 3. Classify (Claude)  category · products · standalone query · restricted? · injection?
   ├─ 4. Retrieve           BM25 over approved documents, scoped to the channel's audience
   ├─ 5. Draft (Claude)     answer + one claim per fact + the source label behind each
   ├─ 6. Verify (Claude)    a separate call that sees ONLY the passages and the claims
   └─ 7. Confidence gate    deterministic rules ──► answer │ clarify │ escalate
```

A reply lands **in the thread** of the question. It reaches the channel only
when an approver pushes it there — see
[Sharing an answer with the channel](#sharing-an-answer-with-the-channel).

### The confidence gate

This is the part that matters, so it is plain code in
[`src/zam_agent/confidence.py`](src/zam_agent/confidence.py), not a model
judgement. The model's own `self_confidence` is capped at **10%** of the score.

**Hard rules — any one of these escalates, whatever the score says:**

| Rule | Why |
|---|---|
| Nothing was retrieved | There is no basis for an answer. |
| The answer cites a label that was not retrieved | A fabricated citation is a hallucination, not a low score. |
| The verifier marked any claim `unsupported` or `contradicted` | "Plausible" and "not contradicted" are not support. |
| The verifier found facts in the answer that no claim covers | Smuggled-in detail. |
| The sources conflict, or only a deprecated document matched | Contradictory documentation is not a tie to break. |
| Every source behind the answer is past the freshness limit | Stale is not verified. |
| No `verified` source backs the answer (only `draft`/`deprecated`) | Unreviewed is not verified. |
| Key-term coverage is below `MIN_EVIDENCE_COVERAGE` | The retrieval probably matched the wrong thing. |
| Grounding verification did not run (API failure) | Unverified means not answerable. |
| The request needs a human decision or approval | Not the agent's to give. |
| The request may involve restricted information | Scoped to people, not to a channel. |

**Otherwise a weighted score decides:**

| Signal | Weight | What it measures |
|---|---:|---|
| Grounding | 35% | Share of claims the independent verifier confirmed. |
| Evidence coverage | 30% | Share of the question's meaningful terms actually present in the passages. |
| Retrieval strength | 15% | Top BM25 score. |
| Source quality | 10% | `verified` vs `draft` vs `deprecated`, discounted for staleness. |
| Model self-report | 10% | Advisory only. |

- **≥ `CONFIDENCE_THRESHOLD`** → answer in-thread, with a source link.
- **≥ `MEDIUM_CONFIDENCE_THRESHOLD`** → ask one clarifying question if that can
  resolve it; otherwise escalate. Ambiguity never overrides an accuracy
  failure: a contradiction or a bad citation always escalates.
- **below that** → escalate.

### Escalation behaviour

- The owner is tagged by **configured Slack ID**: `ESCALATION_USER_ID`, or
  `ZAM_ESCALATION_USER_ID` / `THEME_MARKET_ESCALATION_USER_ID` per product. The
  agent never guesses a username.
- A **second message** explains the context: the question, who asked, a
  permalink, and why the agent did not answer.
- The same question is **not re-tagged** within `ESCALATION_COOLDOWN_HOURS`.
  The agent replies without a ping and says it is already with the owner.
- A verified answer **never** tags anyone.
- Every escalation is recorded as a knowledge gap, so
  `scripts/report_gaps.py` is the backlog for `knowledge/`.

### Closing the loop from Slack

Owners never need the CLI to close a question:

```
employee asks ──► agent escalates ──► owner answers in the thread
                                        └─► owner adds ✅
                                              │
                      agent saves that answer, marks the gap resolved,
                      and confirms in-thread (in the question's language)
```

Then `python scripts/report_gaps.py --draft-all` turns each saved answer into a
document in `knowledge/_inbox/` — pre-filled, `status: draft`, with a review
checklist. Promotion stays manual: `_inbox` is not indexed, so a captured answer
cannot be quoted until somebody confirms it, dates it and moves it into the
product directory. Capture is effortless; publication is not.

Who may resolve: the three escalation owners plus `KNOWLEDGE_EDITOR_USER_IDS`.
Anyone can add a reaction in a public channel, so that list *is* the
authorisation — a reaction from anyone else is logged and ignored (silently;
publicly correcting a colleague for clicking an emoji is worse than doing
nothing). Removing the reaction reopens the gap without re-pinging anybody.

### Sharing an answer with the channel

Answers stay in the thread of the question that prompted them, so the channel
stays readable. When an answer deserves everyone's attention, **Ola Rasheed**
(`U04FCR4PULQ`) or **Nora Alareer** (`U09FXC4B2N4`) reacts 📣 (`:mega:`) on it
and the agent re-posts it at channel level with the original question for
context and a link back to the thread.

- Only `BROADCAST_APPROVER_USER_IDS` may do this — not escalation owners, not
  knowledge editors, not whoever asked. The list fails closed: empty means
  nothing is ever broadcast.
- Only the **agent's own** answers can be amplified. Reacting 📣 on an
  employee's message does nothing; broadcasting it would put words in their
  mouth at channel level.
- An answer is broadcast once, however many approvers react. Removing 📣 does
  nothing, since a channel message cannot be un-sent.

**Why a person decides, and not a signal.** Every automatic proxy for "this was
useful" is a bad one: a 👍 means one reader liked it, a long thread usually
means the answer was *unclear*, and repeat asks only arrive after several
people were already confused. One deliberate click from someone who owns the
channel beats all of them. (Repeat-ask counts are still recorded — but a
question asked five times is a sign the answer should be easier to *find*, not
that it should be announced.)

### Keeping technical issues out of the channel

The channel's topic asks people to keep technical issues and merchant incidents
elsewhere. The agent helps enforce that:

| What was posted | What the agent says |
|---|---|
| A **HubSpot** link | "Since this is already a HubSpot ticket, please follow it up there rather than in this channel." |
| A **Jira** link or issue key (`ZAMCASE-4821`) | "Please raise it as a HubSpot ticket so it gets tracked", with a link to the form. |
| A broken thing described with no link | Same, once the classifier recognises it as an incident. |

Link detection is a string match, not a model call — so it is instant, free,
and impossible to argue out of. It runs *before* classification, which is why a
ticket link never reaches the answering path even when it also mentions a
product. Only an unlinked description needs the classifier's judgement.

These nudges **post immediately** and are not gated on a 📣: they state no
facts and cannot be wrong about policy, and gating them would leave the channel
cluttered until a human intervened — the opposite of the point. They never tag
anyone, and they always go in-thread.

---

## Architecture

```
src/zam_agent/
├── config.py              env → validated settings (fails fast, never logs secrets)
├── language.py            ar/en detection, Arabic normalisation, question detection
├── pipeline.py            the orchestration above; Slack-free, so it is testable
├── confidence.py          the gate: hard rules + weighted score
├── escalation.py          owner routing, bilingual wording, cooldown
├── security.py            mention stripping, mrkdwn escaping, audience scoping
├── prompts/               frozen system prompts (classifier · answer · grader)
├── llm/                   LLMClient protocol · Claude impl · FakeLLM for tests
├── knowledge/
│   ├── documents.py       front matter → Document, heading-aware chunking
│   ├── index.py           BM25 + coverage + conflict/supersession resolution
│   ├── ingest.py          loaders → index, atomic swap, audit snapshot
│   └── loaders/           markdown (default) · notion · gdrive
├── slackbot/
│   ├── filters.py         what the agent may act on; de-duplication keys
│   ├── app.py             Bolt wiring, async processing, posting
│   ├── retry.py           rate limits, Retry-After, fatal vs transient
│   └── thread_context.py  thread history for follow-up questions
├── store/                 SQLite: processed events · escalations · interactions · gaps
├── observability/         JSON logging with secret redaction, counters
├── runtime.py             composition root; WSGI app with /health and /metrics
└── wsgi.py                gunicorn entry point
```

Each boundary is a protocol, so the parts are genuinely swappable:
`LLMClient` (AI provider), `KnowledgeLoader` (sources), `Store`
(persistence), `EmbeddingBackend` (dense retrieval). More detail in
[docs/architecture.md](docs/architecture.md).

**Why lexical retrieval rather than embeddings.** The corpus is internal
FAQ/SOP text, queries reuse its vocabulary, and BM25 needs no second vendor and
no network call on the hot path. More importantly it yields an *interpretable*
grounding signal — which of the question's terms were actually found — that the
confidence gate can reason about. `EmbeddingBackend` is the hook if you later
want dense retrieval too.

---

## Setup

### 1. Create the Slack app

1. Go to <https://api.slack.com/apps> → **Create New App** → **From an app
   manifest**, pick the workspace, and paste
   [`deploy/slack-app-manifest.yaml`](deploy/slack-app-manifest.yaml).
2. **Basic Information → App-Level Tokens** → *Generate Token and Scopes* →
   add the `connections:write` scope → copy the `xapp-…` token into
   `SLACK_APP_TOKEN`.
3. **OAuth & Permissions** → *Install to Workspace*. If your workspace requires
   admin approval, the request goes to a Workspace Owner/Admin — send them the
   app's name, the scope list below, and the channel it will watch.
4. Copy the **Bot User OAuth Token** (`xoxb-…`) into `SLACK_BOT_TOKEN`.
5. **Invite the bot to the channel**: `/invite @ZAM Ask Here`. Without this it
   receives no events, whatever the scopes say.
6. Set `SLACK_CHANNEL_ID`. For this deployment that is `C0204TKHWSZ`
   (**#zam-ask-here**); for any other channel, copy it from channel name →
   **View channel details** → the ID at the bottom.
7. Copy the owner's member ID (profile → **⋮** → *Copy member ID*, starts with
   `U`; a user group ID starting with `S` also works) into
   `ESCALATION_USER_ID`, and ideally `ZAM_ESCALATION_USER_ID` and
   `THEME_MARKET_ESCALATION_USER_ID` too. Add anyone else who should be able to
   close a gap to `KNOWLEDGE_EDITOR_USER_IDS`.

**Scopes the agent uses, and why — nothing more:**

| Scope | Why |
|---|---|
| `channels:history` | Read messages in the watched public channel. |
| `channels:read` | Channel metadata for logs and escalation context. |
| `chat:write` | Post answers and escalations. |
| `app_mentions:read` | Let employees address the agent directly. |
| `reactions:read` | Let an owner close a gap by reacting to the thread. |
| `reactions:write` | Only used when `ADD_ACK_REACTION=true`. |

Events subscribed: `message.channels`, `app_mention`, `reaction_added`,
`reaction_removed`.

For a **private** channel add `groups:history` and `groups:read` and the
`message.groups` event. Prefer a public channel: answers in a private channel
cannot be audited by the people who own the documentation.

### 2. Choose a connection mode

| | Socket Mode (default) | HTTP Events API |
|---|---|---|
| Public URL | not needed | required, HTTPS |
| Config | `SLACK_MODE=socket` + `SLACK_APP_TOKEN` | `SLACK_MODE=http` + `SLACK_SIGNING_SECRET` |
| Request URL | — | `https://<host>/slack/events` |
| Best for | almost everything | when outbound WebSockets are blocked |

Slack requires a 2xx **within 3 seconds** or it retries the delivery. The agent
acknowledges immediately and does the model work on a worker thread; retried
deliveries are discarded by an atomic claim in the database, so a retry that
arrives mid-processing is dropped rather than answered twice.

### 3. Install and configure

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -e '.[dev]'
cp .env.example .env     # then fill it in
```

`.env.example` documents every variable. Required:
`SLACK_BOT_TOKEN`, `SLACK_CHANNEL_ID`, `ESCALATION_USER_ID`,
`ANTHROPIC_API_KEY`, plus `SLACK_APP_TOKEN` (socket) or
`SLACK_SIGNING_SECRET` (http). Startup fails with a specific message if one is
missing or malformed — including a Slack ID that does not look like one.

### 4. Fill the knowledge base

The agent can only say what it can cite. Read
[`knowledge/README.md`](knowledge/README.md) for the document format, then:

```bash
cp knowledge/_TEMPLATE.md knowledge/zam/app-review.md   # edit it
python scripts/ingest.py --validate --list
python scripts/ingest.py --query "كم مدة مراجعة التطبيق؟"
```

The `--query` output shows exactly what the agent would retrieve, which term
coverage it got, and whether it would escalate. That loop — write a document,
check the query, repeat — is how this agent gets good.

Optional sources, both read-only and both limited to explicitly listed
targets:

- **Notion** — `NOTION_API_KEY` plus `NOTION_DATABASE_IDS` / `NOTION_PAGE_IDS`.
  Share those pages with the integration. The loader never crawls a workspace.
  A Notion `Status` of anything but Verified/Approved/Published is treated as a
  draft, so it cannot support a confident answer.
- **Google Drive** — `pip install '.[gdrive]'`, then
  `GOOGLE_DRIVE_CREDENTIALS_FILE` (a read-only service account) plus
  `GOOGLE_DRIVE_FOLDER_IDS` for whole folders and/or `GOOGLE_DRIVE_FILE_IDS`
  for individually approved documents — useful when the canonical source is a
  single Doc, like the *ZAM & Theme Market guideline* linked in the channel
  topic. Share the folder or document with the service account's e-mail.
  Metadata comes from Drive `appProperties` or the file description, using the
  same keys as Markdown front matter.

---

## Running it

```bash
python -m zam_agent            # start (Socket Mode by default)
python -m zam_agent --health   # print the health payload and exit
```

**Start with `DRY_RUN=true`.** The agent processes real messages, logs the full
decision — action, confidence score, every component, every reason, the exact
reply it would have posted — and sends nothing to Slack. Watch it for a day in
the real channel before letting it speak.

```bash
# Try one question against the real pipeline, without Slack:
python scripts/simulate.py "What are the Theme Market pricing tiers?"

# Simulate a follow-up:
python scripts/simulate.py "وللقوالب المدفوعة؟" \
  --thread "[employee:U0…] what are the Theme Market pricing tiers?"
```

`make help` lists the rest.

---

## Deployment

### Docker (recommended)

```bash
cp .env.example .env     # fill it in
docker compose up --build
```

**The `/data` volume is not optional.** It holds event de-duplication and
escalation state; losing it means the agent re-answers messages after a restart
and re-pings owners about questions already in flight.

### A process manager (systemd, Procfile, PaaS)

`Procfile` has both forms:

```
worker: python -m zam_agent
web:    gunicorn --workers 1 --threads 8 --timeout 120 --bind 0.0.0.0:$PORT zam_agent.wsgi:application
```

Socket Mode runs as a `worker` with no inbound port. For HTTP mode use the
`web` form and point the Slack **Request URL** at `https://<host>/slack/events`.

**Run one process, scale with threads.** The knowledge index is in-process, and
a single writer keeps SQLite straightforward. If you genuinely need several
processes, implement `Store` against Postgres first — otherwise de-duplication
and escalation state fragment.

### Hosting checklist

- [ ] Secrets come from a secrets manager, not a file in the image.
- [ ] A durable volume is mounted at the `DATABASE_URL` path.
- [ ] `/health` is wired to the platform's health check (HTTP mode), or the
      container `HEALTHCHECK` is enabled (Socket Mode). It reports `degraded`
      when the knowledge base is empty.
- [ ] Logs ship somewhere searchable — they are one JSON object per line.
- [ ] `LOG_LEVEL=INFO` in production. `DEBUG` makes the SDKs verbose.
- [ ] Ingestion re-runs when `knowledge/` changes (on deploy, or a cron job).

---

## Operating it

```bash
python scripts/report_gaps.py                 # unanswered questions, most frequent first
python scripts/report_gaps.py --escalations   # what is still waiting on a human
python scripts/report_gaps.py --resolved      # answers owners confirmed in Slack
python scripts/report_gaps.py --draft-all     # turn those answers into draft documents
python scripts/report_gaps.py --interactions  # the recent decision log
python scripts/report_gaps.py --reopen <key>  # undo a resolution
python scripts/report_gaps.py --prune 30      # drop telemetry older than 30 days
python scripts/ingest.py --stale              # documents past KNOWLEDGE_MAX_AGE_DAYS
```

**The maintenance loop.** Escalations are not failures, they are the backlog.
Owners close them in Slack with a ✅ as they answer; nobody has to remember a
command. Then, weekly:

```bash
python scripts/report_gaps.py --draft-all     # captured answers -> knowledge/_inbox/
# review each draft: confirm it, set status: verified and a date, move it into
# knowledge/zam|theme-market|general/
python scripts/ingest.py --validate --query "<the question an employee asked>"
```

Anything owners did *not* close still shows up in `report_gaps.py`. Run
`ingest.py --stale` monthly and re-date or retire what has aged out.

**When the agent gets something wrong**, the fix is almost always a document,
not a threshold. Raise `CONFIDENCE_THRESHOLD` if it answers when it should
ask; lower it only after `simulate.py` shows the evidence really was there.

`/health` and `/metrics` (HTTP mode) expose the knowledge index state, store
counts and in-process counters — including `pipeline.action.*`,
`pipeline.escalated`, `llm.*` and `slack.*`. More in
[docs/operations.md](docs/operations.md).

---

## Configuration reference

Every variable is documented inline in
[`.env.example`](.env.example). The ones worth a second thought:

| Variable | Default | Notes |
|---|---|---|
| `CONFIDENCE_THRESHOLD` | `0.68` | At or above this the agent answers alone. |
| `MEDIUM_CONFIDENCE_THRESHOLD` | `0.40` | Below this it always escalates. |
| `MIN_EVIDENCE_COVERAGE` | `0.34` | Hard gate on key-term coverage. |
| `MIN_SUPPORTED_CLAIM_RATIO` | `0.75` | Hard gate on verified grounding. |
| `MAX_UNSUPPORTED_CLAIMS` | `0` | Raise this only deliberately. |
| `KNOWLEDGE_MAX_AGE_DAYS` | `365` | Older, or undated, counts as stale. |
| `ESCALATION_COOLDOWN_HOURS` | `24` | Re-ping window for the same question. |
| `ENABLE_SLACK_RESOLUTION` | `true` | Owners can close a gap with a reaction. |
| `RESOLVE_REACTION` | `white_check_mark` | The reaction that means "confirmed". |
| `KNOWLEDGE_EDITOR_USER_IDS` | *(empty)* | Extra people allowed to resolve, beyond the three owners. |
| `ENABLE_BROADCAST` | `true` | 📣 pushes an answer to the channel. |
| `BROADCAST_REACTION` | `mega` | 📣. |
| `BROADCAST_APPROVER_USER_IDS` | *(empty)* | **The only people who may broadcast.** Empty = never. |
| `DEFLECT_TECHNICAL_ISSUES` | `true` | Redirect ticket links and incidents to HubSpot. |
| `HUBSPOT_TICKET_URL` | *(empty)* | The form the nudge links to. |
| `PREFILTER_ENABLED` | `true` | Skips the classifier for messages with no question and no product keyword. Set `false` to classify everything (more cost, slightly better recall). |
| `ESCALATE_GENERAL_QUESTIONS` | `false` | Keep false: otherwise unrelated company chatter pings an owner. |
| `RESTRICTED_CHANNEL_IDS` | *(empty)* | Leave empty for a company-wide channel. |
| `CLAUDE_MODEL` | `claude-opus-5-5` | `CLAUDE_CLASSIFIER_MODEL` / `CLAUDE_GRADER_MODEL` default to it; point them at a cheaper model only after checking quality. |
| `DRY_RUN` | `false` | Decide and log, post nothing. |

---

## Testing

```bash
make check          # ruff + mypy + pytest
pytest -q
pytest -k samples   # the sample-message acceptance table
```

379 tests, no network access: Claude is replaced by a scripted `FakeLLM` and
Slack by a `FakeSlackClient`.

[`tests/fixtures/sample_messages.yaml`](tests/fixtures/sample_messages.yaml) is
the readable contract — sample Slack messages and the outcome the agent must
produce — and `tests/test_samples.py` runs every row through the real pipeline.
It covers verified ZAM and Theme Market questions, Arabic and Saudi dialect,
unanswerable questions that must tag a human, hallucinated facts, fabricated
citations, conflicting and outdated documentation, approval requests,
restricted information, ambiguity, irrelevant chatter, acknowledgements,
prompt injection, and HubSpot/Jira links that must be redirected.

`tests/test_broadcast.py` covers who may push an answer to the channel (only
the named approvers — not owners, not editors, not the asker), that only the
agent's own answers can be amplified, single-broadcast-per-answer, and mention
stripping. `tests/test_deflection.py` covers link detection including the
false-positive cases (`COVID-19`, `RFC-2119`, `ISO-8601`), both nudge wordings,
and that an incident neither answers nor escalates.

`tests/test_resolution.py` covers the Slack resolve loop: who may and may not
close a gap, capture that excludes the agent's own messages and the original
question, mention/secret stripping inside a captured answer, reopening,
duplicate reaction deliveries, and that a captured answer is always written as
`status: draft`.

The rest of the suite covers duplicate Slack deliveries, self-reply and loop
prevention, every ignored event subtype,
[real Slack event payloads](tests/fixtures/slack_events/), thread follow-ups,
Claude timeouts / rate limits / refusals / malformed output, Slack rate limits
and `Retry-After`, config validation, audience scoping, and secret redaction.

All knowledge used in tests is **fictional** and lives in
`tests/fixtures/knowledge/`.

---

## Security notes

Full detail in [docs/security.md](docs/security.md). The short version:

- **Least privilege.** Five bot scopes, two events, one channel. No
  `users:read`, no `files:read`, no user token.
- **Secrets** come from the environment or a secrets manager, never from source
  or a commit. A redaction filter masks token-shaped strings and sensitive keys
  in every log record, and provider error bodies are never logged (they echo
  the prompt).
- **Untrusted input.** Slack messages, thread history and retrieved documents
  are wrapped in explicit delimiters and labelled as data in all three prompts.
  Instructions embedded in them are not followed, and the confidence gate is
  code, so no message can talk its way past it.
- **Mention control.** Model output is stripped of every mention and broadcast
  form (`<@U…>`, `<!here>`, `<!channel>`, `@everyone`, user groups) before
  posting. Only the agent, using a configured ID, can tag anyone.
- **Access scoping.** Documents are labelled `all` / `internal` / `restricted`
  and filtered by channel. An unrecognised audience or status **fails closed**
  (`restricted` / `draft`). A request for confidential information is escalated
  rather than answered in a public channel.
- **Outbound data.** The only external calls are to Slack, the Claude API, and
  any knowledge source you explicitly configure. Nothing is sent anywhere else.
- **Reaching the channel is authorised, not implied.** Answers land in a
  thread; only `BROADCAST_APPROVER_USER_IDS` can push one to channel level, and
  only the agent's own messages can be pushed. Both checks fail closed.
- **Resolution is authorised, not implied.** Closing a knowledge gap requires
  a configured owner or knowledge editor. A reaction from anyone else changes
  nothing. A captured answer passes through the same sanitiser as any other
  text, and lands as `status: draft` in a folder the loader ignores — so a
  Slack message can never become a citable source without human review.
- **No autonomous authority.** The agent never approves, commits or decides on
  anyone's behalf; those requests go straight to a human.

---

## Assumptions and open questions

Stated explicitly, because the brief left them open:

1. **Python 3.11+ with `slack-bolt` and the official `anthropic` SDK.** No
   language was specified; Bolt and the Claude SDK are the supported paths.
2. **Socket Mode is the default.** It needs no public URL or TLS termination,
   which makes the first deployment much simpler. HTTP mode is fully
   implemented for environments that block outbound WebSockets.
3. **Retrieval is lexical (BM25) with Arabic normalisation**, for the reasons
   above. There is no embedding provider, so none is required; the
   `EmbeddingBackend` protocol is the hook if you want one.
4. **SQLite is the bundled store.** Durable de-duplication and escalation state
   with no database server to run. `Store` is the protocol to implement for
   Postgres.
5. **`knowledge/` is empty and ships no company facts.** Nobody should be
   writing down ZAM or Theme Market policy except the people who own it.
6. **`ESCALATE_GENERAL_QUESTIONS=false`** by default, so a general company
   question with no matching document is ignored rather than pinged at an
   owner. Flip it if a human should triage those.
7. **Classification and grounding verification default to `CLAUDE_MODEL`**
   (`claude-opus-5-5`) rather than silently downgrading to a cheaper model. The
   knobs are there; the choice is yours.

Worth confirming before rollout, none of which blocks it:

- The owner IDs for ZAM and Theme Market, and who belongs in
  `KNOWLEDGE_EDITOR_USER_IDS`.
- Whether `RESTRICTED_CHANNEL_IDS` should ever be non-empty, or whether
  restricted documents should simply not be in the index at all.
- Whether `ZAMCASE` is the only Jira project worth recognising by bare key, or
  whether other prefixes appear in the channel.

The channel is **#zam-ask-here** (`C0204TKHWSZ`), and its topic says to keep
technical issues, merchant incidents and escalations out of it. The agent's
hand-off is a "please confirm this" ping, not an incident report, so it fits —
but it is worth saying so when the bot is introduced, so nobody reads a ✅
request as an incident.

### Feeding it knowledge

Four ways, in rough order of effort:

1. **Paste or upload the content in a session with me** and I will write it as
   properly formatted documents, check the retrieval, and commit them.
2. **Write the files yourself** into `knowledge/zam|theme-market|general/`.
   `knowledge/README.md` has the format, `knowledge/_TEMPLATE.md` a starting
   point, and `scripts/ingest.py --query "…"` shows what the agent would find.
3. **Point it at Google Drive** — `GOOGLE_DRIVE_FILE_IDS` takes individual
   approved Docs, which is how to connect the *ZAM & Theme Market guideline*
   linked in the channel topic.
4. **Let the channel teach it.** #zam-ask-here has years of questions already
   answered by humans. Those are the highest-value documents you could write,
   because they are provably the questions people ask.
