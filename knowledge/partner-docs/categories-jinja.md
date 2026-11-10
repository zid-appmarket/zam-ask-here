---
# Synced from https://docs.zid.sa/categories-jinja-1914523m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-categories-jinja
title: "categories.jinja"
product: theme_market
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/categories-jinja-1914523m0
tags: [from-docs-site, partner-docs]
language: en
---

> categories.jinja - Zid Docs
# categories.jinja

**Route:** `/categories`

**Path Operation:** `list_categories`

## Variables #

Variable Type

`categories` List[Category]

`store` Store

`session` Session

## Category Properties #

Property Description

`category.id` ID

`category.name` Name

`category.slug` URL slug

`category.image` Image

`category.cover_image` Cover image

`category.sub_categories` Child categories

## Example #

```
`{% extends "layout.jinja" %}

{% block main_content %}
<div class="categories">
{% for category in categories %}
<div class="category-card">
{% if category.cover_image %}
<img src="{{ category.cover_image }}" alt="{{ category.name }}">
{% endif %}

<a href="{{ url_for('category_details', category_id=category.id, slug=category.slug) }}">
{{ category.name }}
</a>

{% if category.sub_categories %}
{% for sub in category.sub_categories %}
<a href="{{ url_for('category_details', category_id=sub.id, slug=sub.slug) }}">
{{ sub.name }}
</a>
{% endfor %}
{% endif %}
</div>
{% endfor %}
</div>
{% endblock %}`
```

Modified at 2026-07-30 11:49:13

Previous

products.jinja

Next

page.jinja
