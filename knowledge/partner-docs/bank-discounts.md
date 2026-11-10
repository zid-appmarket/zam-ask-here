---
# Synced from https://docs.zid.sa/bank-discounts-2332488m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-bank-discounts
title: "Bank Discounts"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/bank-discounts-2332488m0
tags: [from-docs-site, partner-docs]
language: en
---

> Bank Discounts - Zid Docs
# Bank Discounts

Bank Discounts allow merchants to offer automatic discounts to customers who pay using eligible bank cards. Merchants can configure discounts for specific Saudi banks and supported card networks, including **Mada**, **Visa**, and **Mastercard**.

Bank Discounts require **ZidPay**.

Theme developers must add the Bank Discounts component to the **product details** and **cart** templates for these offers to appear on the storefront.

Bank Discounts are applied automatically during checkout when the customer's bank and card network match an eligible discount. **Apple Pay payments are excluded.**

## How Bank Discounts Work #

Merchants configure Bank Discounts from **Marketing → Bank Discounts** in the Zid dashboard.

A Bank Discount can define:

Setting Description

Bank The Saudi bank whose cards are eligible for the discount.

Card type One or more supported card networks: Mada, Visa, or Mastercard.

Discount type Percentage or fixed amount.

Discount value The percentage or fixed amount deducted from the order.

Start date The date from which the discount becomes available.

End date An optional date after which the discount is no longer available.

Minimum order value An optional minimum order total required to receive the discount.

Maximum discount value An optional maximum amount that can be discounted.

Display location Determines whether the Bank Discount banner appears on the product details page, cart page, or both.

No coupon code is required. Zid automatically evaluates the customer's payment card during checkout and applies an eligible Bank Discount.

## Theme Developer Integration #

Use the following shared template to display Bank Discounts:

```
`{% include 'vitrin:shared/bank_discounts.jinja' %}`
```

Add the component to both:

`templates/product.jinja`

`templates/cart.jinja`

The component renders the Bank Discount offers that the merchant has configured to appear on the corresponding page.

If the component is not included, Bank Discounts will **not be displayed on that page**, even when the merchant has configured eligible offers.

## Product Details Page #

Add the Bank Discounts component to `templates/product.jinja`.

Place it **above the product payment widgets**, so Bank Discounts appear before payment widgets such as Tabby or Tamara.

```
`{% include 'vitrin:shared/bank_discounts.jinja' %}

{% include 'vitrin:products/payment_widgets.jinja' %}`
```

### Example #

```
`{% extends "layout.jinja" %}

{% block main_content %}
<h1>{{ product.name }}</h1>

{% if product.selected_product.media %}
<img
src="{{ product.selected_product.media[0].image.full_size }}"
alt="{{ product.name }}"
>
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

{% include 'vitrin:products/payment_widgets.jinja' %}

<button onclick="zid.cart.addProduct({form_id: 'product-form'})">
{{ _("Add to Cart") }}
</button>
{% endblock %}`
```

See **product.jinja** for the complete product template reference.

## Cart Page #

Add the same Bank Discounts component to `templates/cart.jinja`.

Place it **above the cart payment widgets**, so Bank Discounts appear before payment widgets such as Tabby or Tamara.

```
`{% include 'vitrin:shared/bank_discounts.jinja' %}

{% include 'vitrin:cart/payment_widgets.jinja' %}`
```

### Example #

```
`{% extends "layout.jinja" %}

{% block main_content %}
{% if cart.products_count > 0 %}
<h1>{{ _("Cart") }}</h1>

{% include 'vitrin:cart/products_list.jinja' %}

{% include 'vitrin:shared/bank_discounts.jinja' %}

{% include 'vitrin:cart/payment_widgets.jinja' %}

<div class="totals">
{% for total in cart.totals %}
<div>{{ total.title }}: {{ total.value_string }}</div>
{% endfor %}
</div>

{% if session.is_guest %}
<a href="/auth/login?redirect_to=/checkout">
{{ _("Complete Order") }}
</a>
{% else %}
<a href="/checkout">
{{ _("Complete Order") }}
</a>
{% endif %}
{% else %}
<p>{{ _("Cart is empty") }}</p>
<a href="/">{{ _("Continue shopping") }}</a>
{% endif %}
{% endblock %}`
```

See **cart.jinja** for the complete cart template reference.

## Bank Discount Banner #

The Bank Discounts component displays the available offers configured by the merchant.

Each Bank Discount banner can show:

Bank logo

Discount name

Eligible card type

Discount type

When more than three Bank Discounts are available, the component supports scrolling through the available offers automatically.

The merchant controls whether each Bank Discount is displayed on the product details page, cart page, or both.

## Checkout Behavior #

No theme changes are required for checkout because the checkout page is rendered and managed by Zid.

During checkout, Zid evaluates the customer's payment card against the available Bank Discounts.

When the card matches an eligible bank and card network:

1 .

The applicable Bank Discount is highlighted.

2 .

The discount is added to the payment summary.

3 .

The order total is recalculated automatically.

The discount appears in the payment summary using the following format:

```
`[Bank name] Discount – [Card type] [Discount type]`
```

If the customer changes to a card that is not eligible for the discount, Zid removes the discount and recalculates the order total.

**Apple Pay payments are not eligible for Bank Discounts.**

## Fetch Bank Discounts Programmatically #

Apps and custom storefront integrations can retrieve Bank Discounts using the Checkout API:

```
``
```

The endpoint provides information about configured Bank Discounts, including the bank, eligible card networks, discount value and type, display settings, date range, conditions, and current status.

See **List Bank Discounts** in the Checkout API reference for the complete response schema.

## Implementation Checklist #

Add `{% include 'vitrin:shared/bank_discounts.jinja' %}` to `templates/product.jinja`.

Place it above `vitrin:products/payment_widgets.jinja`.

Add `{% include 'vitrin:shared/bank_discounts.jinja' %}` to `templates/cart.jinja`.

Place it above `vitrin:cart/payment_widgets.jinja`.

Verify Bank Discounts appear when the merchant has enabled them for the corresponding page.

Verify product and cart layouts when multiple Bank Discounts are available.

No checkout template changes are required.

Modified at 2026-08-20 10:17:20

Previous

Progressive Discounts

Next

Customer Wallet & Cashback
