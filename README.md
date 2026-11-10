# ZAM Ask Here

A Slack support agent for **ZAM** (Zid App Market) and **Theme Market**.

It watches a configured company channel, answers employees' questions in Arabic
(including Saudi dialect) or English using only approved internal
documentation, cites its sources — and **mentions a designated human whenever it
cannot verify an answer**, instead of guessing.

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
   ├─ 3. Classify (Claude)  category · products · standalone query · restricted? · injection?
   ├─ 4. Retrieve           BM25 over approved documents, scoped to the channel's audience
   ├─ 5. Draft (Claude)     answer + one claim per fact + the source label behind each
   ├─ 6. Verify (Claude)    a separate call that sees ONLY the passages and the claims
   └─ 7. Confidence gate    deterministic rules ──► answer │ clarify │ escalate
```

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
6. Copy the channel ID (channel name → **View channel details** → ID at the
   bottom, starts with `C`) into `SLACK_CHANNEL_ID`.
7. Copy the owner's member ID (profile → **⋮** → *Copy member ID*, starts with
   `U`; a user group ID starting with `S` also works) into
   `ESCALATION_USER_ID`.

**Scopes the agent uses, and why — nothing more:**

| Scope | Why |
|---|---|
| `channels:history` | Read messages in the watched public channel. |
| `channels:read` | Channel metadata for logs and escalation context. |
| `chat:write` | Post answers and escalations. |
| `app_mentions:read` | Let employees address the agent directly. |
| `reactions:write` | Only used when `ADD_ACK_REACTION=true`. |

Events subscribed: `message.channels`, `app_mention`.

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
  `GOOGLE_DRIVE_FOLDER_IDS`. Share the approved folder with the service
  account's e-mail. Metadata comes from Drive `appProperties` or the file
  description, using the same keys as Markdown front matter.

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
python scripts/report_gaps.py --interactions  # the recent decision log
python scripts/report_gaps.py --resolve <key> # after adding the answer to knowledge/
python scripts/report_gaps.py --prune 30      # drop telemetry older than 30 days
python scripts/ingest.py --stale              # documents past KNOWLEDGE_MAX_AGE_DAYS
```

**The maintenance loop.** Escalations are not failures, they are the backlog.
Each week: read `report_gaps.py`, write the answers into `knowledge/`, run
`ingest.py --validate --query "<the question>"` to confirm the agent now finds
it, and `--resolve` the gap. Run `ingest.py --stale` monthly and re-date or
retire what has aged out.

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

283 tests, no network access: Claude is replaced by a scripted `FakeLLM` and
Slack by a `FakeSlackClient`.

[`tests/fixtures/sample_messages.yaml`](tests/fixtures/sample_messages.yaml) is
the readable contract — sample Slack messages and the outcome the agent must
produce — and `tests/test_samples.py` runs every row through the real pipeline.
It covers verified ZAM and Theme Market questions, Arabic and Saudi dialect,
unanswerable questions that must tag a human, hallucinated facts, fabricated
citations, conflicting and outdated documentation, approval requests,
restricted information, ambiguity, irrelevant chatter, acknowledgements and
prompt injection.

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

- The real channel ID, and the owner IDs for ZAM and Theme Market.
- Whether `RESTRICTED_CHANNEL_IDS` should ever be non-empty, or whether
  restricted documents should simply not be in the index at all.
- Whether answers should also appear in the channel (not only in-thread) for
  high-traffic questions.
- Whether the owner should be able to resolve a gap from Slack (a reaction or a
  slash command) rather than via `scripts/report_gaps.py --resolve`.
