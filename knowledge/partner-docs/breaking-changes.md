---
# Synced from https://docs.zid.sa/breaking-changes-1379320m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-breaking-changes
title: "Breaking Changes"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/breaking-changes-1379320m0
tags: [from-docs-site, partner-docs]
language: en
---

> Breaking Changes - Zid Docs
# Breaking Changes

# Migration Notes: Syntax & Template Renames (Copyable Markdown) #

Syntax changes

For syntax differences between Twig and Jinja, see:

Twig to Jinja

Jinja Basics

## Templates Renamed #

Some template names were **standardized to use underscores** instead of dashes.

Old (Twig) New (Jinja)

`shipping-and-payment.twig` `shipping_payment.jinja`

`404.twig` `404_not_found.jinja`

`products-questions.twig` `questions.jinja`

Deprecated Templates

The following templates will not be allowed to be overriden by themes, but instead provided by zid's storefront system:

(`account-addresses.twig`,`account-profile.twig`,`account-orders.twig`,`account-wishlist.twig`)

## Templates renamed #

#### some templates names were standardazed to use underscore instead of dashes #

`shipping-and-payment.twig` is now `shipping_payment.jinja` (https://0qyg3ujwfd.apidog.io/shipping-payment-jinja-1370855m0)

`404.twig` was renamed to `404_not_found.jinja` (https://0qyg3ujwfd.apidog.io/shipping-payment-jinja-1370855m0)

`account-addresses.twig` was renamed to `account_addresses.jinja` (https://0qyg3ujwfd.apidog.io/shipping-payment-jinja-1370855m0)

`account-profile.twig` was renamed to `account_profile.jinja` (https://0qyg3ujwfd.apidog.io/shipping-payment-jinja-1370855m0)

`account-orders.twig` was renamed to `account_orders.jinja` (https://0qyg3ujwfd.apidog.io/shipping-payment-jinja-1370855m0)

`account-wishlist.twig` was renamed to `account_wishlist.jinja` (https://0qyg3ujwfd.apidog.io/shipping-payment-jinja-1370855m0)

`products-questions.twig` was renamed to `questions.jinja` (https://0qyg3ujwfd.apidog.io/shipping-payment-jinja-1370855m0)

### Global variables #

`window.zid.store` is deprecated. You can use `window.zid `instead.

Auth state has been simplified, now you can use `window.isAuthenticated` and `window.isGuest` to check the auth state of a user.

## Variables #

`product.unavailable` is deprecated. You can use `not product.in_stock` instead.

using `request.query` is deprecated. Use `session.query_params`.

Modified at 2026-07-30 11:49:13

Previous

Twig to Jinja

Next

Store Settings Mapping
