# Architecture

## Design constraints that shaped it

1. **Wrong answers are worse than no answer.** An internal support bot that
   invents a policy costs more than one that stays quiet. Every design choice
   below trades recall for verifiability.
2. **Slack gives you 3 seconds.** Events must be acknowledged before the model
   work starts, and retried deliveries must not double-post.
3. **The model is not the authority on its own correctness.** Self-reported
   confidence is a weak signal, so the decision is made by code reading
   checkable facts.
4. **Two languages, one of them with heavy orthographic variation.** Arabic
   needs normalisation for retrieval to work at all.

## Layers

```
┌──────────────────────────────────────────────────────────────────────┐
│ slackbot/        Slack Events API + Web API. The only Slack-aware    │
│                  code. Filters, de-duplicates, acks fast, posts.     │
├──────────────────────────────────────────────────────────────────────┤
│ pipeline.py      Orchestration. Takes an IncomingMessage, returns an │
│                  AgentDecision. Knows nothing about Slack's API.     │
├───────────────┬───────────────┬──────────────────┬───────────────────┤
│ prompts/ +    │ knowledge/    │ confidence.py    │ escalation.py     │
│ llm/          │ retrieval     │ the gate         │ human hand-off    │
├───────────────┴───────────────┴──────────────────┴───────────────────┤
│ store/ · security.py · language.py · triage.py · deflection.py ·     │
│ resolution.py · broadcast.py · observability/                        │
└──────────────────────────────────────────────────────────────────────┘
```

The pipeline being Slack-free is what makes the decision path testable without
a workspace: `tests/test_samples.py` drives it directly.

## Reaction path

Reactions take a separate, much shorter path than messages:

```
reaction_added / reaction_removed
   ├─ should_handle_reaction   message? watched channel? human? ──► drop
   ├─ claim_event              its own de-duplication key ──► drop retries
   └─ ResolutionManager
        ├─ is it 📣?  ──► BroadcastManager (approvers only, agent messages only)
        ├─ is it the resolve reaction?           ──► no: stop
        ├─ which thread is this message in?      (cheap case first, then one Slack call)
        ├─ is there an escalation for it?        ──► no: stop
        ├─ may this person resolve?              ──► no: count, log, stop
        ├─ capture the human replies after the thread root
        └─ resolve the gap, confirm in-thread
```

`ResolutionManager` makes no Slack calls: the thread lookup and thread fetch
are injected callables, so the whole decision path is testable without a
workspace — and a failure to read the thread degrades to "resolved with no
captured answer" rather than blocking the owner.

The capture cut-off is the thread's own root `ts`, not the wall-clock time the
escalation row was written. Both are Slack timestamps, so the comparison needs
no assumption that this process's clock agrees with Slack's.

## Extension points

Each is a `Protocol`, implemented at least twice (real + test double):

| Protocol | File | Swap it to… |
|---|---|---|
| `LLMClient` | `llm/base.py` | change AI provider, or stub it out |
| `KnowledgeLoader` | `knowledge/loaders/base.py` | add Confluence, a wiki, a database |
| `WebSource` | `knowledge/websync.py` | sync another documentation site |
| `EmbeddingBackend` | `knowledge/index.py` | add dense retrieval alongside BM25 |
| `Store` | `store/base.py` | move to Postgres for multi-process |

The store carries its own forward migration (`SQLiteStore.MIGRATIONS`): columns
added after a database was created are applied with `ALTER TABLE` on startup,
since SQLite has no `ADD COLUMN IF NOT EXISTS`. Row mappers tolerate a column
being absent, so a half-migrated database still reads.

## The three model calls

| Call | Model | Effort | Purpose |
|---|---|---|---|
| classify | `CLAUDE_CLASSIFIER_MODEL` | `low` | category, products, standalone query, restricted/injection flags |
| answer | `CLAUDE_MODEL` | `medium` | grounded draft, one claim per fact, source label per claim |
| grade | `CLAUDE_GRADER_MODEL` | `medium` | independent grounding verdicts |

All three use **structured outputs** (`output_config.format` with a JSON
Schema), so the pipeline receives typed objects rather than parsing prose. All
three put the frozen system prompt behind a `cache_control` breakpoint and the
volatile content (question, evidence) in the user turn, so the prompt cache
actually hits. Refusal fallbacks are enabled by default: a safety-classifier
decline on a support question would otherwise mean silence.

The grader is deliberately starved of context. It sees the passages, the
question, the draft and the claims — not the retrieval scores, not the
self-reported confidence, and no instruction to be helpful. Its system prompt
tells it that absence of a statement is `unsupported`, and that plausibility is
not support.

## Where the knowledge comes from

Most documents are synced from Zid's public help centres by
`scripts/sync_docs.py` (`knowledge/websync.py`), not fetched at runtime.

That is a deliberate trade. A runtime crawl would always be current, but
nobody would review what the agent may say, a site outage would become an agent
outage, and a silent upstream edit would silently change answers. Files in git
keep the normal gate — a sync produces a diff, somebody reads it, CI validates
it — and re-running the sync is itself the "what changed upstream" report.

The extractor is dependency-free and generic on purpose. Per-site CSS selectors
break on the next redeploy, so instead it prefers `<article>`/`<main>`, then a
container whose class looks like content, and scores candidates by
**text length discounted by link density** — navigation approaches 1.0 link
density, prose does not. Then it trims to the first `<h1>`. That combination is
what keeps a documentation sidebar out of the document.

Fetched HTML is untrusted input: it is converted to text, never executed, and
the documents it produces are reviewed before they can be cited.

## Retrieval

```
Document (front matter + markdown)
   └─ heading-aware chunking, then size-based splitting with overlap
        └─ BM25 (k1=1.5, b=0.75) over normalised tokens
             ├─ × product match boost
             ├─ × status weight (verified / draft / deprecated)
             ├─ × title-hit boost
             └─ normalised against the best score the query could achieve
```

Two details that matter:

- **Normalisation.** Tashkeel and tatweel are stripped; alef variants, taa
  marbuta, alef maqsura, hamza carriers and Arabic-Indic digits are folded.
  Without this, `سياسة الإسترجاع` and `سياسه الاسترجاع` are different queries.
- **Honest normalisation of the score.** The denominator counts the idf a term
  *would* have if the corpus contained it once, so a query with terms the
  corpus does not contain cannot score 1.0 by matching only its common words.

### Coverage, the grounding signal

`coverage` is the share of the question's meaningful terms (stopwords removed)
that appear anywhere in the retrieved passages. It is cheap, interpretable and
hard to fool, and it is 30% of the confidence score plus a hard gate. When
coverage is low the retrieval probably matched something adjacent rather than
the answer.

### Conflicts and supersession

Three distinct cases, kept distinct on purpose:

| Situation | Behaviour |
|---|---|
| Document B lists `supersedes: [A]` and both are retrieved | A is dropped. The maintainer already decided. |
| A deprecated document matched only weakly (< 50% of the top score) | Dropped quietly. Otherwise every question brushing past a retired document would escalate. |
| A deprecated document is a substantial part of the evidence | Kept and flagged → escalate. |
| Two `verified` documents, same product, overlapping tags, > 365 days apart | Flagged → escalate. |

A flagged conflict only blocks the answer if it touches a document the answer
actually **cited**. Two unrelated documents disagreeing with each other is not
a reason to withhold an answer that did not use either.

## De-duplication

`Store.claim_event` is an `INSERT OR IGNORE` returning whether the row was new.
That is atomic, so a retry arriving while the first delivery is still being
processed loses the race and is dropped — not merely "checked and found
missing". The key is Slack's `event_id`, falling back to `client_msg_id`, then
`channel:ts`.

On a **transient** failure (Claude timeout or rate limit) the claim is
*released*, so Slack's own retry can succeed. On a permanent failure it is kept,
so the agent does not retry a request that will fail the same way.

## Concurrency

One process. Bolt acknowledges the event, then the work runs on a
`ThreadPoolExecutor` (`WORKER_THREADS`, default 4). The knowledge index is
immutable once built and swapped atomically on reload, so readers never see a
half-built index. SQLite runs in WAL mode with a busy timeout.

## Known gap: the market catalogue

The most common question in #zam-ask-here is "do we have an app that does X?",
closely followed by "is app X still available?". Neither is a documentary
question, so no amount of help-centre syncing will answer them: the help
centres describe how the market works, not its current contents.

Answering them needs a catalogue source — published apps and themes, what each
does, its status and price — behind a `KnowledgeLoader`. That loader would
differ from the others in one important way: a catalogue is a *live* fact, not
a reviewed document, so it should be fetched with a short cache rather than
synced into git, and its documents should carry a same-day `updated` date.
Everything downstream (retrieval, grounding, the confidence gate) works
unchanged.

Until then the agent escalates those questions, which is the correct behaviour
and is why the escalation path got as much attention as the answering path.

## What is deliberately absent

- **No conversation memory beyond the thread.** Context comes from
  `conversations.replies` on demand. There is no per-user state to go stale or
  leak.
- **No fine-tuning, no vector database, no agent framework.** Three API calls
  and a scoring function are easier to reason about, and the failure modes are
  visible in the logs.
- **No write access to anything.** The agent posts messages. It does not edit
  documents, approve requests, or change its own configuration.
