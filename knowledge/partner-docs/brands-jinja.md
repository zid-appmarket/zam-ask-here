---
# Synced from https://docs.zid.sa/brands-jinja-2427114m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-brands-jinja
title: "brands.jinja"
product: theme_market
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/brands-jinja-2427114m0
tags: [from-docs-site, partner-docs]
language: en
---

> brands.jinja - Zid Docs
# brands.jinja

**Route:** `/brands`

**Path Operation:** Not supported by `url_for()`

## Variables #

Variable Type

`brands` Brand list

`store` Store

`session` Session

## Brands Properties #

Property Description

`brands.results` List of brands

`brands.count` Total number of brands

`brands.page` Current page

## Brand Properties #

Property Description

`brand.id` Brand ID

`brand.name` Brand name

`brand.description` Brand description

`brand.slug` Brand URL slug

`brand.logo` Brand logo

`brand.products_count` Number of products assigned to the brand

## Example #

```
`{% extends "layout.jinja" %}

{% block main_content %}
<div class="brands">
{% for brand in brands.results %}
<div class="brand-card">

{% if brand.logo %}
<img src="{{ brand.logo }}" alt="{{ brand.name }}">
{% endif %}

<a href="/brands/{{ brand.slug }}">
{{ brand.name }}
</a>

{% if brand.description %}
<p class="text-foreground text-sm line-clamp-2">
{{ brand.description | striptags | truncate(160) }}
</p>
{% endif %}

</div>
{% endfor %}
</div>
{% endblock %}`
```

## Note #

Brand routes are not currently supported by `url_for()`. To link to an individual brand page, use `/brands/{{ brand.slug }}`.

See also: **brand.jinja** (https://docs.zid.sa/brand-jinja-2427123m0) for displaying a specific brand and its products.

Modified at 2026-09-15 10:00:26

Previous

404_not_found.jinja

Next

brand.jinja
