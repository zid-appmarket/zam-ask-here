# Draft inbox — not indexed

`scripts/report_gaps.py --draft <key>` writes a document here whenever an owner
answers an escalated question in Slack and marks it confirmed.

**Nothing in this folder is retrievable.** The loader skips any path whose name
starts with `_`, so a draft cannot be quoted by the agent until a human:

1. gives it a stable `id` and a real `title`,
2. confirms the answer is correct and concretely worded,
3. sets `status: verified` and today's `updated` date,
4. moves it into `knowledge/zam/`, `knowledge/theme-market/` or
   `knowledge/general/`.

That separation is deliberate: capturing an answer from Slack should be
effortless, publishing one should not be.
