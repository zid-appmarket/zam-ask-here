---
# Synced from https://docs.zid.sa/brand-jinja-2427123m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-brand-jinja
title: "brand.jinja"
product: theme_market
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/brand-jinja-2427123m0
tags: [from-docs-site, partner-docs]
language: en
---

> brand.jinja - Zid Docs
# brand.jinja

**Route:** `/brands/{slug_brand}`

**Path Operation:** Not supported by `url_for()`

## Variables #

Variable Type

`brand` Brand

`products` ProductList

`store` Store

`session` Session

## Brand Properties #

Property Description

`brand.id` Brand ID

`brand.name` Brand name

`brand.slug` Brand URL slug

`brand.description` Brand description

`brand.logo` Brand logo

## Products Properties #

Property Description

`products.results` List of products assigned to the brand

`products.count` Total number of products

`products.page` Current page

`products.pages_count` Total number of pages

`products.filters` Available product filters

## Example #

```
`{% extends "layout.jinja" %}

{% block main_content %}
<h1>{{ brand.name }}</h1>

{% if brand.logo %}
<img src="{{ brand.logo }}" alt="{{ brand.name }}">
{% endif %}

{% if brand.description %}
<p>
{{ brand.description }}
</p>
{% endif %}

{% if products.filters | length > 0 %}
{% include 'vitrin:products/filters.jinja' %}
{% endif %}

<div class="products">
{% for product in products.results %}
{% include 'components/product-card.jinja' %}
{% endfor %}
</div>

{% include 'components/pagination.jinja' %}
{% endblock %}`
```

Modified at 2026-09-15 09:46:31

Previous

brands.jinja

Next

Schema files
