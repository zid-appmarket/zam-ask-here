---
# Synced from https://docs.zid.sa/reviews-jinja-1914527m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-reviews-jinja
title: "reviews.jinja"
product: theme_market
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/reviews-jinja-1914527m0
tags: [from-docs-site, partner-docs]
language: en
---

> reviews.jinja - Zid Docs
# reviews.jinja

**Route:** `/products/{slug}/reviews`

**Path Operation:** `product_reviews`

## Variables #

Variable Type

`product` Product

`reviews` ReviewList

`store` Store

`session` Session

## Product Properties #

Property Description

`product.name` Product name

`product.slug` URL slug

`product.main_image` Main image

`product.rating` Rating object

`product.reviews` Paginated reviews

## Review Properties #

Property Description

`review.rating` Star rating (1-5)

`review.comment` Review text

`review.customer_name` Reviewer name

`review.images` Review images

## Example #

```
`{% extends "layout.jinja" %}

{% block main_content %}
<a href="{{ url_for('product_details', slug=product.slug) }}">
<h1>{{ product.name }}</h1>
</a>

{% if product.rating %}
<div>{{ product.rating.average }} ({{ product.rating.total_count }})</div>
{% endif %}

{% for review in product.reviews.results %}
<div class="review">
<strong>{{ review.customer_name }}</strong>
<div>{{ review.rating }} stars</div>
<p>{{ review.comment }}</p>
</div>
{% endfor %}

{% include 'components/pagination.jinja' %}
{% endblock %}`
```

Modified at 2026-07-30 11:49:13

Previous

faqs.jinja

Next

questions.jinja
