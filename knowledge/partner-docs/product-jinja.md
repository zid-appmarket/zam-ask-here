---
# Synced from https://docs.zid.sa/product-jinja-1914519m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-product-jinja
title: "product.jinja"
product: theme_market
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/product-jinja-1914519m0
tags: [from-docs-site, partner-docs]
language: en
---

> product.jinja - Zid Docs
# product.jinja

**Route:** `/products/{slug}`

**Path Operation:** `product_details`

## Variables #

Variable Type

`product` Product

`store` Store

`session` Session

## Product Properties #

Property Description

`product.id` Product ID

`product.name` Name

`product.slug` URL slug

`product.description` Full description (HTML)

`product.short_description` Brief description

`product.selected_product` Current variant

`product.selected_product.formatted_price` Price

`product.selected_product.formatted_sale_price` Sale price

`product.selected_product.quantity` Stock

`product.selected_product.in_stock` Availability

`product.selected_product.sku` SKU

`product.selected_product.media` Images/videos

`product.variants` Variants

`product.options` Options (size, color)

`product.rating` Rating

`product.reviews` Reviews

`product.questions` Q&A

`product.related_products` Related products

`product.bundle_offer` Bundle offer

`product.brand` Brand assigned to the product

`product.brand.name` Brand name

`product.brand.logo` Brand logo

## Brand #

The `product.brand` object contains the brand information assigned to the product. Use it to display the brand name or logo on the product details page.

Property Description

`product.brand.name` Brand name

`product.brand.logo` Brand logo

### Example #

```
`{% if product.brand %}
<div class="product-brand">
{% if product.brand.logo %}
<img src="{{ product.brand.logo }}" alt="{{ product.brand.name }}">
{% endif %}

{% if product.brand.name %}
<span>{{ product.brand.name }}</span>
{% endif %}
</div>
{% endif %}
-----`
```

## Bank Discounts #

To display available bank and card discounts on the product details page, include the Bank Discounts shared template:

```
``
```

Place the Bank Discounts component above the product payment widgets:

```
``
```

Bank Discounts require ZidPay. The component displays Bank Discount offers that the merchant has configured to appear on the product details page.

If the component is not included, available Bank Discounts will not appear on the product details page.

See **Bank Discounts** (https://docs.zid.sa/bank-discounts-2332488m0) for the complete integration requirements.

## Example #

```
`{% extends "layout.jinja" %}

{% block main_content %}
<h1>{{ product.name }}</h1>

{% if product.selected_product.media %}
<img src="{{ product.selected_product.media[0].image.full_size }}" alt="{{ product.name }}">
{% endif %}

<div class="price">
{% if product.selected_product.formatted_sale_price %}
<span>{{ product.selected_product.formatted_sale_price }}</span>
<del>{{ product.selected_product.formatted_price }}</del>
{% else %}
{{ product.selected_product.formatted_price }}
{% endif %}
</div>

{{ product.description | safe }}

{% include 'vitrin:products/variants_list.jinja' %}

{% include 'vitrin:shared/bank_discounts.jinja' %}

<button onclick="zid.cart.addProduct({form_id: 'product-form'})">
{{ _("Add to Cart") }}
</button>
{% endblock %}`
```

Modified at 2026-09-15 09:52:54

Previous

home.jinja

Next

cart.jinja
