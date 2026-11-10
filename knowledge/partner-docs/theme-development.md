---
# Synced from https://docs.zid.sa/theme-development
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-theme-development
title: "Theme Development"
product: theme_market
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/theme-development
tags: [from-docs-site, partner-docs]
language: en
---

> Theme Development - Zid Docs
# Theme Development

Developing a theme in Zid means combining **Jinja templates**, **settings schemas**, and **assets** to create a storefront experience that merchants can customize and publish.

This page walks you through the **flow of theme development**, references key documentation, and provides resources to help you build faster.

## Theme Development Flow #

Follow this roadmap when building your theme:

1

Understand the Theme Architecture

Before coding, get familiar with how themes are structured in Zid:

Theme Architecture (https://docs.zid.sa/architecture-1379322m0) — high-level design and concepts

2

Learn the Templating Basics

Themes are built on **Jinja**. Developers should review:

Jinja Basics (https://docs.zid.sa/jinja-basics-1379353m0) — syntax for variables, loops, and conditions

Vitrin’s Jinja Extensions (https://docs.zid.sa/vitrins-jinja-extensions-1379354m0) — Zid’s custom tags, filters, and macros

Objects Reference (https://docs.zid.sa/objects-reference-1379355m0) — available objects (e.g., `product`, `cart`, `store`, `settings`)

3

Explore Available Templates

Get to know the templates you can implement or override:

Template Documentation (https://docs.zid.sa/overview-1379323m0) — all supported templates with routes

Template Library — code and UI examples for each template

4

Build with Sections, Settings & Locales

Make your theme flexible and multilingual:

Sections (https://docs.zid.sa/sections-1379344m0) — break pages into reusable, configurable parts

Settings Schema (https://docs.zid.sa/input-settings-1379345m0) — define configurable options for merchants

Locales (https://docs.zid.sa/localization-jinja-v-twig-1379352m0) — support translations using gettext and `.po` files

5

Develop Locally

Choose your development workflow:

Vitrin CLI (https://docs.zid.sa/introduction-1379356m0) — create, preview, package, and publish themes faster

Or, manually upload your theme via the Partner Dashboard (https://partner.zid.sa/my-themes)

6

Validate, Publish & Test

Before release, ensure your theme meets requirements:

Theme Publishing Guide (https://docs.zid.sa/introduction-1379356m0) — submission steps and criteria

Vitrin CLI Commands (https://docs.zid.sa/cli-commands-1390556m0) — validate and package your theme

Theme Test Tool (https://docs.zid.sa/theme-development#theme-testing) — automated checks for schema and template rules

Explore this **ready-to-use sample theme (https://github.com/zidsa/soft-theme-vitrin)** that showcases the **full folder structure, templates, settings schema, and macros**.

## Theme Development Guidelines #

Follow these rules to ensure your theme works seamlessly with our system, stays compatible with future updates, and delivers the best experience for merchants.

### Base Layout #

Templates **must** extend your base layout:

```
``
```

Your base layout must also include two required tags `vitrin_head` and `vitrin_body`, like the following example:

```
``
```

This ensures all themes maintain a consistent HTML structure and compatibility with Zid features.

### Default Template Fallbacks #

If you do not implement a template or component, our system automatically uses the default template from Zid’s default theme.

This means you can choose to only customize certain pages (e.g., home, header, footer) and rely on defaults for the rest.

### Theme Settings #

It is better to never hardcode styling values (colors, fonts, spacing) inside templates. Always pull from the theme settings schema.

Example:

```
``
```

This ensures store owners can change styles without editing code.

### Versioning & API Changes #

All major features and API changes will be versioned, fully documented, and released as **versioned release candidates**. Theme partners will be notified through our changelog (https://changelog.partner.zid.sa/) about any upcoming changes in advance.

Theme developers will be able to Version their themes in a way that allows them to add braeaking change without affecting existing stores using the theme.

No breaking changes will be introduced in the same major API/Theme version.

### Schema Standards #

Theme schemas must follow the JSON Schema (https://0qyg3ujwfd.apidog.io/sections-1268221m0) standard.

### Theme Testing #

Before submission, a Theme Test tool is provided to validate your theme files. You can use this view throughout development to make sure you are on the right track.

In order to access your theme's validation report, simply add `/validate` to the end of your preview link.

For example:

```
`https://my-preview?theme={themeId}`
```

Your validation report will be accessible at:

```
`https://my-preview/validate?theme={themeId}`
```

#### (Bonus) Validate your .PO files #

You can validate that your .PO files compile correctly before uploading them by running the following command which should show any errors for you in the command line

```
`msgfmt --check -o output.mo input.po 2>&1`
```

Do not upload the `output.mo`. It will be ignored.

### Error Handling #

Server error messages are handled by the SDK. Themes must never implement custom error rendering for server responses.

### Template Context Size #

Keep the template context payload within platform size limits. Large contexts slow rendering and increase bandwidth usage.

### Sample template #

You can view and build on top of our latest sample theme Growth (https://github.com/zidsa/growth-theme).

Modified at 2026-05-03 15:59:03

Previous

Introduction

Next

Bnfsj Landing Page Development
