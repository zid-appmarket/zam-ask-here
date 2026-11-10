---
# Synced from https://docs.zid.sa/events-1954903m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-events-d58d2e
title: "Events"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/events-1954903m0
tags: [from-docs-site, partner-docs]
language: en
---

> Events - Zid Docs
# Events

This page documents the tracking events available for **theme developers** to call manually.

All functions are available via **`window.zidTracking`**.

## Select Item #

**Function:** `zidTracking.sendGaSelectItemEvent(params)`

**Description:** Fires when a user clicks/selects a product from a product list (e.g., category page, search results, related products slider).

### Platforms #

Platform Event Name Sent

GA4 `select_item` Yes

GTM `select_item` Yes

GA Universal `ec:setAction click` Yes

### Arguments #

Parameter Type Required Description

`product` `object` Yes The product object

`listName` `string` No Name of the list (defaults to `"products"`)

`listId` `string` No Identifier for the list

`index` `number` No Position of the product in the list (0-based)

### Usage #

```
``
```

### Example: Product Card Click #

```
``
```

## View Cart #

**Function:** `zidTracking.sendGaCartDetailViewedEvent(params)`

**Description:** Fires when the cart is viewed. Use this **only** when your theme displays cart contents outside the cart page (e.g., mini-cart, cart drawer, cart modal).

**Important:** This event is automatically fired on the cart page. Do **not** call it on the cart page to avoid duplicate events.

### Platforms #

Platform Event Name Sent

GA4 `view_cart` Yes

GTM `view_cart` Yes

Facebook `ViewCart` Yes

### Arguments #

Parameter Type Required Description

`cart` `object` Yes The cart object

### Usage #

```
``
```

## Summary #

Event Function When to Use

`select_item` `sendGaSelectItemEvent` User clicks a product in a list

`view_cart` `sendGaCartDetailViewedEvent` Cart viewed outside cart page (mini-cart, drawer)

Modified at 2026-07-30 11:49:13

Previous

Options

Next

SDK Popups – Integration Guidelines
