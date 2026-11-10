---
# Synced from https://docs.zid.sa/category-jinja-1914521m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-category-jinja
title: "category.jinja"
product: theme_market
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/category-jinja-1914521m0
tags: [from-docs-site, partner-docs]
language: en
---

> category.jinja - Zid Docs
# category.jinja

**Route:** `/categories/{category_id}/{slug}`

**Path Operation:** `category_details`

## Variables #

Variable Type

`category` Category

`products` ProductList

`store` Store

`session` Session

## Category Properties #

Property Description

`category.id` ID

`category.name` Name

`category.slug` URL slug

`category.description` Description

`category.image` Image

`category.sub_categories` Child categories

`category.parent_category` Parent category

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
<h1>{{ category.name }}</h1>

{% if category.sub_categories %}
{% for sub in category.sub_categories %}
<a href="{{ url_for('category_details', category_id=sub.id, slug=sub.slug) }}">
{{ sub.name }}
</a>
{% endfor %}
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

Modified at 2026-07-30 11:49:13

Previous

cart.jinja

Next

products.jinja
