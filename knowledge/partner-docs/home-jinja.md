---
# Synced from https://docs.zid.sa/home-jinja-1914518m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-home-jinja
title: "home.jinja"
product: theme_market
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/home-jinja-1914518m0
tags: [from-docs-site, partner-docs]
language: en
---

> home.jinja - Zid Docs
# home.jinja

**Route:** `/`

**Path Operation:** `home`

## Variables #

Variable Type

`store` Store

`session` Session

## Example #

```
`{% extends "layout.jinja" %}

{% block main_content %}
<div class="home">
{% template_components %}
</div>
{% endblock %}`
```

## Notes #

`{% template_components %}` renders sections from Theme Editor

Configure sections via `home.json` schema

Modified at 2026-07-30 11:49:13

Previous

Template Replacements

Next

product.jinja
