---
# Synced from https://docs.zid.sa/theme-sections-settings-2258380m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-theme-sections-settings
title: "Theme Sections Settings"
product: theme_market
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/theme-sections-settings-2258380m0
tags: [from-docs-site, partner-docs]
language: en
---

> Theme Sections Settings - Zid Docs
# Theme Sections Settings

# Theme Settings #

Template settings are now accessible through the Storefront APIs:

```
`GET api/v1/template-settings?template=home`
```

📌

This is an **early version** and is subject to change. Give it a try and share your feedback with us.

## Section `meta.type` #

We are testing a new field on sections to help developers build sections that are more **mobile-compatible**.

In the `template-settings` response, each section now includes a `meta.type` field specifying the type of module it is. This removes the need to rely on specific section file names (e.g. `main-slider.twig`, `main_slider2.twig`, `slider.twig`) — theme developers can simply declare the type in their file schema:

```
` {
...

"meta" : {
"type" : "slider"
}
} `
```

## Testing #

The `meta.type` field is currently applied only to Soft Theme Vitrin (https://github.com/zidsa/soft-theme-vitrin/commit/08d9a76ba210754dded472e46c2240939e0c4412).

1

1. Open the online theme editor

Use a store running Soft Theme Vitrin.

2

2. Refresh each section

Make any update to each section — no need to delete it — so its schema refreshes.

3

3. Call the endpoint

Request `api/v1/template-settings?template=home` and inspect the `meta.type` field on each section.

Modified at 2026-07-15 14:33:15

Previous

Login & Checkout via Page Views

Next

Logout
