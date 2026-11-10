---
# Synced from https://docs.zid.sa/shipping-payment-jinja-1914529m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-shipping-payment-jinja
title: "shipping_payment.jinja"
product: theme_market
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/shipping-payment-jinja-1914529m0
tags: [from-docs-site, partner-docs]
language: en
---

> shipping_payment.jinja - Zid Docs
# shipping_payment.jinja

**Route:** `/shipping-and-payment`

**Path Operation:** `shipping_payment`

## Variables #

Variable Type

`shipping_methods` List[ShippingMethod]

`payment_methods` List[PaymentMethod]

`banks` List[Bank]

`store` Store

`session` Session

## Shipping Method Properties #

Property Description

`shipping_method.id` ID

`shipping_method.name` Name

`shipping_method.image` Logo

`shipping_method.delivery_option_cities` Covered cities

`shipping_method.cost` Cost breakdown

`shipping_method.cod_enabled` COD available

`shipping_method.cod_fee` COD fees

## Payment Method Properties #

Property Description

`payment_method.icons` Payment icons

## Bank Properties #

Property Description

`bank.bank.name` Bank name

`bank.bank.logo` Bank logo

`bank.beneficiary_name` Account holder

`bank.iban` IBAN

`bank.account_number` Account number

## Example #

```
`{% extends "layout.jinja" %}

{% block main_content %}
<h2>{{ _("Shipping Options") }}</h2>
{% for method in shipping_methods %}
<div>
<img src="{{ method.image }}" alt="{{ method.name }}">
<span>{{ method.name }}</span>
</div>
{% endfor %}

<h2>{{ _("Payment Options") }}</h2>
{% for method in payment_methods %}
{% if method.icons %}
<img src="{{ method.icons[0] }}">
{% endif %}
{% endfor %}

<h2>{{ _("Bank Accounts") }}</h2>
{% for bank in banks %}
<div>
<strong>{{ bank.bank.name }}</strong>
<p>{{ _("IBAN") }}: {{ bank.iban }}</p>
</div>
{% endfor %}
{% endblock %}`
```

Modified at 2026-07-30 11:49:13

Previous

questions.jinja

Next

404_not_found.jinja
