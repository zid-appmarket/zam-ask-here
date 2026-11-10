---
# Synced from https://docs.zid.sa/faqs-jinja-1914526m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-faqs-jinja
title: "faqs.jinja"
product: theme_market
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/faqs-jinja-1914526m0
tags: [from-docs-site, partner-docs]
language: en
---

> faqs.jinja - Zid Docs
# faqs.jinja

**Route:** `/faqs`

**Path Operation:** `faqs`

## Variables #

Variable Type

`faqs` List[FAQ]

`store` Store

`session` Session

## FAQ Properties #

Property Description

`faq.question` Question text

`faq.answer` Answer (HTML)

## Example #

```
`{% extends "layout.jinja" %}

{% block main_content %}
<div class="faqs">
{% for faq in faqs %}
<div class="faq-item">
<h3>{{ faq.question }}</h3>
<div>{{ faq.answer | safe }}</div>
</div>
{% endfor %}
</div>
{% endblock %}`
```

Modified at 2026-07-30 11:49:13

Previous

blog.jinja

Next

reviews.jinja
