---
# Synced from https://docs.zid.sa/page-jinja-1914524m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-page-jinja
title: "page.jinja"
product: theme_market
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/page-jinja-1914524m0
tags: [from-docs-site, partner-docs]
language: en
---

> page.jinja - Zid Docs
# page.jinja

**Route:** `/pages/{slug}`

**Path Operation:** `pages`

## Variables #

Variable Type

`page` Page

`store` Store

`session` Session

## Page Properties #

Property Description

`page.title` Page title

`page.content` Page content (HTML)

## Example #

```
`{% extends "layout.jinja" %}

{% block main_content %}
<div class="page">
<h1>{{ page.title }}</h1>
<div class="content">
{{ page.content | safe }}
</div>
</div>
{% endblock %}`
```

Modified at 2026-07-30 11:49:13

Previous

categories.jinja

Next

blogs.jinja
