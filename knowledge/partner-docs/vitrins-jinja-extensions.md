---
# Synced from https://docs.zid.sa/vitrins-jinja-extensions-1379354m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-vitrins-jinja-extensions
title: "Vitrin's Jinja Extensions"
product: theme_market
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/vitrins-jinja-extensions-1379354m0
tags: [from-docs-site, partner-docs]
language: en
---

> Vitrin's Jinja Extensions - Zid Docs
# Vitrin's Jinja Extensions

Our theme templating is based on **Jinja (https://jinja.palletsprojects.com/en/stable/api/#basics)** with a small set of **platform tags, filters, and macros** layered on top to make theme development fast, safe, and consistent.

## Overview #

**Base layout:** all templates **must** extend `layout.jinja` (provided by the system).

**Defaults:** any missing template/section falls back to Zid’s default theme.

**Settings:** never hardcode styles or copy; read from `settings` (JSON Schema).

**Components:** use platform **macros** (primitive UI) instead of custom markup.

**Versioning:** features are versioned; no breaking changes within a major version.

**Errors:** server errors are handled by the SDK, not by themes.

## Tags #

Quick helpers available in templates.

Tag Purpose Status Type

`url_for` Build a canonical URL for a route Macro

`asset_url` Resolve a theme asset CDN URL filter

`image_url` Resolve and resize images CDN URL Macro

### using `url_for` #

Build URLs without hardcoding paths; instead using an operation name. this respects locale and routing rules.

```
``
```

### existing Operation names #

the required path variables can be found with the endpints documentation

Constant Value

CHANGE_LOCALE `change_locale`

LIST_PRODUCTS `list_products`

PRODUCT_REVIEWS `product_reviews`

ADD_PRODUCT_REVIEW `add_product_review`

PRODUCT_QUESTIONS `product_questions`

ADD_QUESTION `add_question`

PRODUCT_DETAILS `product_details`

LIST_CATEGORIES `list_categories`

CATEGORY_DETAILS `category_details`

PROFILE `profile`

UPDATE_PROFILE_PAGE `update_profile_page`

ORDERS `orders`

ADDRESSES `addresses`

WISHLIST `wishlist`

LOYALTY_PROGRAM `loyalty_program`

ADD_ADDRESS `add_address`

EDIT_ADDRESS `edit_address`

UPDATE_EMAIL_PAGE `update_email_page`

REGISTER_PAGE `register_page`

LOGIN_PAGE `login_page`

VERIFICATION_PAGE `verification_page`

CART_PAGE `cart_page`

SINGLE_PAGE_CHECKOUT `single_page_checkout`

CHOOSE_SHIPPING `choose_shipping`

CHOOSE_PAYMENT `choose_payment`

ORDER_INVOICE `order_invoice`

ORDER_COMPLETED `order_completed`

TRANSACTION_SLIP_UPLOAD `transaction_slip_upload`

HOME `home`

PAGES `pages`

BLOGS `blogs`

FAQS `faqs`

SHIPPING_PAYMENT `shipping_payment`

LANDING_PAGE `landing_page`

AFFILIATE_REPORTS `affiliate_reports`

SITEMAP_XML `sitemap_xml`

PRODUCTS_FEED `products_feed`

PRODUCTS_REVIEWS_FEED `products_reviews_feed`

**Params**

### `asset_url` #

Return a versioned CDN URL for an asset.

```
``
```

```
``
```

**Returns:** string (URL)

Modified at 2026-07-30 11:49:13

Previous

Jinja Basics

Next

Introduction
