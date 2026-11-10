---
# Synced from https://docs.zid.sa/cart-jinja-1914520m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-cart-jinja
title: "cart.jinja"
product: theme_market
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/cart-jinja-1914520m0
tags: [from-docs-site, partner-docs]
language: en
---

> cart.jinja - Zid Docs
# cart.jinja

**Route:** `/cart`

**Path Operation:** `cart_page`

## Variables #

Variable Type

`cart` Cart

`store` Store

`session` Session

## Cart Properties #

Property Description

`cart.products` Cart items

`cart.products_count` Item count

`cart.totals` Total lines

`cart.coupon` Applied coupon

`cart.gift_card_details` Gift card info

`cart.free_shipping_rule` Free shipping rule

## Coupon Form Visibility #

When adding a custom coupon section to `cart.jinja`, check the `store.settings.checkout.is_coupon_form_enabled` setting before rendering it.

```
`{% set coupon_form_enabled = store.settings.checkout.is_coupon_form_enabled != false %}

{% if coupon_form_enabled %}
{# Complete coupon section #}
{% endif %}`
```

When the setting is `false`, do not render the coupon input, apply button, applied coupon details, remove button, or coupon-related messages.

See **Coupon Form Visibility (https://docs.zid.sa/show-or-hide-the-coupon-code-field-in-a-zid-theme-2283520m0)** for the complete implementation, JavaScript safeguards, testing steps, and troubleshooting guidance.

## Bank Discounts #

To display available bank and card discounts on the cart page, include the Bank Discounts shared template:

```
`{% include 'vitrin:shared/bank_discounts.jinja' %}`
```

The component displays Bank Discount offers that the merchant has configured to appear on the cart page.

If your cart template includes payment widgets such as Tabby or Tamara, place the Bank Discounts component **above the cart payment widgets**:

```
`{% include 'vitrin:shared/bank_discounts.jinja' %}

{% include 'vitrin:cart/payment_widgets.jinja' %}`
```

If the Bank Discounts component is not included, available Bank Discounts will not appear on the cart page.

Bank Discounts require **ZidPay**.

See **Bank Discounts (https://docs.zid.sa/bank-discounts-2332488m0)** for the complete integration requirements.

## Example #

```
`{% extends "layout.jinja" %}

{% block main_content %}
{% if cart.products_count > 0 %}
<h1>{{ _("Cart") }}</h1>

{% include 'vitrin:cart/products_list.jinja' %}

{% include 'vitrin:shared/bank_discounts.jinja' %}

<div class="totals">
{% for total in cart.totals %}
<div>{{ total.title }}: {{ total.value_string }}</div>
{% endfor %}
</div>

{% if session.is_guest %}
<a href="/auth/login?redirect_to=/checkout">{{ _("Complete Order") }}</a>
{% else %}
<a href="/checkout">{{ _("Complete Order") }}</a>
{% endif %}
{% else %}
<p>{{ _("Cart is empty") }}</p>
<a href="/">{{ _("Continue shopping") }}</a>
{% endif %}
{% endblock %}`
```

Modified at 2026-08-20 10:32:37

Previous

product.jinja

Next

category.jinja
