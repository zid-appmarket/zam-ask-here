---
# Synced from https://docs.zid.sa/products-jinja-1914522m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-products-jinja
title: "products.jinja"
product: theme_market
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/products-jinja-1914522m0
tags: [from-docs-site, partner-docs]
language: en
---

> products.jinja - Zid Docs
# products.jinja

**Route:** `/products`

**Path Operation:** `list_products`

## Variables #

Variable Type

`products` ProductList

`store` Store

`session` Session

## Products Properties #

Property Description

`products.results` Product list

`products.count` Total count

`products.page` Current page

`products.pages_count` Total pages

`products.filters` Available filters

## Example #

```
`{% extends "layout.jinja" %}

{% block main_content %}
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

Modified at 2026-07-30 11:49:13

Previous

category.jinja

Next

categories.jinja
