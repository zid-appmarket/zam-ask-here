---
# Synced from https://docs.zid.sa/404-not-found-jinja-1914530m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-404-not-found-jinja
title: "404_not_found.jinja"
product: theme_market
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/404-not-found-jinja-1914530m0
tags: [from-docs-site, partner-docs]
language: en
---

> 404_not_found.jinja - Zid Docs
# 404_not_found.jinja

**Path Operation:** `not_found`

Error page shown when content is not found.

## Variables #

Variable Type

`store` Store

`session` Session

## Example #

```
`{% extends "layout.jinja" %}

{% block main_content %}
<div class="error-page">
<h1>404</h1>
<p>{{ _("Page not found") }}</p>
<a href="{{ url_for('home') }}">{{ _("Go to Home") }}</a>
</div>
{% endblock %}`
```

Modified at 2026-07-30 11:49:13

Previous

shipping_payment.jinja

Next

brands.jinja
