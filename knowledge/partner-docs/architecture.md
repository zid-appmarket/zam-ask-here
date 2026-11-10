---
# Synced from https://docs.zid.sa/architecture-1379322m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-architecture
title: "Architecture"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/architecture-1379322m0
tags: [from-docs-site, partner-docs]
language: en
---

> Architecture - Zid Docs
# Architecture

A **theme** defines how a Zid storefront looks, works, and stays organized. Themes are built with **Jinja templates** plus **JSON schema files** for editable settings, all arranged in a consistent folder structure.

## Directory Structure #

All Zid themes must follow this structure:

```
`├── locale/ar/LC_MESSAGES/messages.po
├── assets/
├── sections/
│ ├── slider.jinja
│ └── slider.schema.json
├── components/
│ └── pagination.jinja
└── templates/
│ ├── home.jinja
│ ├── cart.jinja
│ └── product.jinja
├── layout.jinja
├── layout.schema.json
├── footer.jinja
├── footer.schema.json
├── header.jinja
└── header.schema.json

`
```

## Theme Hierarchy #

The storefront is assembled in layers, starting from the layout and breaking down into reusable parts.

1 .

**`Layout`**

Defines base HTML wrappers which inject shared `<head>` tags, header/footer, and global scripts. Templates extend these layouts. Needs to include vitrin tags (https://app.apidog.com/project/613905#docId1379315-base-layout).

2 .

**`Section`**

Contains the main page blocks, each split into a `.jinja` markup file and a companion `.json` schema. The schema surfaces settings in the Theme Editor, and the section can render **multiple components** to build complex layouts.

3 .

**`Component`**

Reusable modules of content that are consumed by sections. Every component has its own `.jinja` markup and `.json` schema so that it can be customized by merchants.

## Assets #

Stored in `assets/`

Includes CSS, JS, images, and fonts.

All assets are fingerprinted and served via Zid CDN.

Reference any file with the `asset_url` filter to output its cache‑busted CDN URL:

```
``
```

## Templates #

Map storefront routes to actual pages.

Example routes:

/ → `home.jinja`

/p/{product} → `product.jinja`

/cart → `cart.jinja`

Each template references a layout and one or more sections.

**👉 Read more:** Templates Overview (https://docs.zid.sa/overview-1379323m0)

## Gettext Localization #

Stored in `locale/{locale}/LC_MESSAGES/messages.po`

Plain-text file storing translations: `msgid` → `msgstr`.

Natural language keys.

Compiled into `.mo` files (machine-readable) for performance.

localization msgid

make sure that the msgid is unique in the .po translation file, otherwise file won't be compiled properly

**👉 Read more:** Localization (https://docs.zid.sa/localization-jinja-v-twig-1379352m0)

Modified at 2026-07-30 11:49:13

Previous

Store Settings Mapping

Next

Overview
