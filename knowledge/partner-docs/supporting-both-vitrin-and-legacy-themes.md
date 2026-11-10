---
# Synced from https://docs.zid.sa/supporting-both-vitrin-and-legacy-themes-1596866m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-supporting-both-vitrin-and-legacy-themes
title: "Supporting both Vitrin and Legacy themes"
product: theme_market
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/supporting-both-vitrin-and-legacy-themes-1596866m0
tags: [from-docs-site, partner-docs]
language: en
---

> Supporting both Vitrin and Legacy themes - Zid Docs
# Supporting both Vitrin and Legacy themes

This page is for JS app developers

If you are developing a new theme you wil only be using the new SDK which is detailed in the next pages

## Detecting Vitrin at runtime #

To ensure you JS apps work on both Vitrin and legacy themes, you can use the `windows.vitrin` object. It will be set to `true` only if the store is running vitrin.

Example:

```
``
```

## Alternative for remote scripts (via query param) #

If you host a remote script that already uses query params, you’ll now receive `?vitrin=true` when the store is on Vitrin. You can serve a newer script version without checking window.vitrin in the script itself.

New:

```
` { script_url } ?store= { store_uuid } &vitrin= true `
```

Legacy:

```
` { script_url } ?store= { store_uuid } `
```

Modified at 2026-07-30 11:49:13

Previous

Performance

Next

Responses & Errors
