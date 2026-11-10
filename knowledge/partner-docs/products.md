---
# Synced from https://docs.zid.sa/products-1475307m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-products
title: "Products"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/products-1475307m0
tags: [from-docs-site, partner-docs]
language: en
---

> Products - Zid Docs
# Products

This page documents the **new** Vitrin product functions and explains the arguments needed to use them (with the matching old Zid call where relevant).

All functions are available via **`window.zid.products`**.

## Get Product #

**New:** `zid.products.get(product_id)`

**Old:** `zid.store.product.fetch(id)`

**Description:** Retrieve the product by id

## Get Product Options #

**New:** `zid.products.getProductOptions(product_id, params?)`

### Arguments #

**`product_id`** (string, required) — Product identifier.

**`params`** (object, optional) :

**`attributes`** (object) — Map of `attribute_id` → `attribute_value_id` (UUIDs).

**`option_fields`** (object) — Map of `option_group_id` → array of selected `option_id`s (UUIDs).

**`input_fields`** (string[]) — Array of `input_field_id`s (UUIDs) that currently have values.

Response returns an updated **ProductObject** (resolved variant, price, stock) based on your selections.

### Example params (placeholders) #

```
``
```

IDs come from the product object (all are UUIDs).

## Reviews (Read) #

**New:** `zid.products.reviews(product_id, { page?, page_size? })`

**Old:** `zid.store.product.getReviews(id, page)`

### Arguments #

**`product_id`** (string, required)

**`params`** (object, optional) :

`page?` (number)

`page_size?` (number)

## Reviews (Create) #

**New:** `zid.products.createReview(product_id, payload)`

**Old:** `zid.store.product.addReview(id, reviewForm, rating, is_anonymous)`

### Arguments #

**`product_id`** (string, required)

**`payload`** (object, required) :

`rating` (number, required) — 1..5

`comment?` (string)

`is_anonymous?` (boolean)

`order_id?` (string)

`images?` (File[])

## Customer Reviews (Mine) #

**New:** `zid.products.getCustomerReviews({ product_id })`

**Old:** `zid.store.product.getCustomerReviews(id, orderId)`

### Arguments #

**`params`** (object, required) :

`product_id` (string, required)

**Change:** `orderId` is not used in the new API.

## Questions (List) #

**New:** `zid.products.questions(product_id, params?)`

**Description:** Retrieve all questions asked about a product.

### Parameters #

**`product_id`** (string, required) — Product identifier.

**`params`** (object, optional) — Optional query parameters:

**`page`** (number) — Page number for pagination.

**`page_size`** (number) — Number of questions per page.

**Usage**

```
``
```

## Questions (Create) #

**New:** `zid.products.createQuestion(product_id, payload)`

**Old (used):** `zid.store.product.addQuestion(id, question, name, email, is_anonymous)`

### Arguments #

**`product_id`** (string, required)

**`payload`** (object, required) :

`name` (string, required)

`email` (string, required)

`question` (string, required)

`is_anonymous?` (boolean)

## Bundle Offer (List) #

**New:** `zid.products.bundleOffers(params?)`

**Old (used):** `zid.store.product.getProductBundleOffer(id)`

### Arguments #

**`params`** (object, optional) :

`product_ids` (array, optional)

### Example params (placeholders) #

```
``
```

## Stock Alerts #

**New:** `zid.products.stockAlerts({ product_id }, payload)`

**Description:** Subscribe to stock alerts for a product. Customers will be notified when the product is back in stock.

### Parameters #

**`product_id`** (string, required) — Product identifier.

**`payload`** (object, required) — Subscription details containing customer information.

### Payload Structure #

**`customer_email`** (string, required) — Customer's email address for notifications.

**`customer_phone_number`** (string, optional) — Customer's phone number.

**`customer_name`** (string, optional) — Customer's name.

**Usage**

```
``
```

## Get Bundle Offer (Single Product) #

**New:** `zid.products.getBundleOffer(product_id)`

**Description:** Get bundle offers specifically for a single product.

### Parameters #

**`product_id`** (string, required) — Product identifier.

**Usage**

```
``
```

## Notes #

Keep calls minimal: pass only the arguments you need.

All IDs (`attributes`, `option_fields`, `input_fields`) are **UUIDs from the product object**. They are provided dynamically, you don’t hardcode them.

Modified at 2026-07-30 11:49:13

Previous

Cart

Next

Categories
