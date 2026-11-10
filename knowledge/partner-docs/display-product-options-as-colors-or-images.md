---
# Synced from https://docs.zid.sa/display-product-options-as-colors-or-images-2264161m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-display-product-options-as-colors-or-images
title: "Display Product Options as Colors or Images"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/display-product-options-as-colors-or-images-2264161m0
tags: [from-docs-site, partner-docs]
language: en
---

> Display Product Options as Colors or Images - Zid Docs
## Best practices #

1 .

Prefer the shared V2 product-options renderer whenever possible; it owns the metadata and fallback logic.

2 .

Treat metadata as presentation only. The raw choice string remains the source of truth for selection.

3 .

Always provide a text fallback for incomplete or invalid metadata.

4 .

Do not attempt visual options in native `<select>` menus.

5 .

Validate the selected, unavailable, and responsive states before publishing your theme.
