---
# Synced from https://docs.zid.sa/bundle-progress-2470540m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-bundle-progress
title: "Bundle Progress"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/bundle-progress-2470540m0
tags: [from-docs-site, partner-docs]
language: en
---

> Bundle Progress - Zid Docs
# Bundle Progress

The **Bundle Progress** component shows customers how close they are to completing a **set-price bundle offer** (for example, "Any 3 for 100 SAR"). It appears on product listing pages once the customer adds a product from the offer to the cart, tracks how many of the set's items are already in the cart, and confirms when the offer price is applied.

## About #

The bundle progress is driven by the **Bundle Offers** configured in the **Merchant Dashboard**.

**Path:** `https://dashboard.zid.sa/en-sa/stores/<store_id>/marketing/bundle-offers/create/fixed-price`

**No set-price offer on the page's products:** The component renders nothing.

**Set-price offer exists:**

The component stays hidden until the customer adds at least one product from the offer to the cart

A progress card shows how many of the set's items are in the cart (e.g. `2 of 3 in your cart`)

When the set is complete, the card switches to a success message with the amount saved

Each matching offer gets its own card, so several offers can be tracked on the same page

Only offers with the **set price** mode are tracked. Standard bundle offers are ignored by this component.

## Features #

### Progress Tracking #

Segmented progress bar: one segment per item in the set, filled segments for items already in the cart

Progress label: `{current} of {total} in your cart` / `{current} من {total} في سلتك`

The count never exceeds the set size

### Set Completion #

When a full set is in the cart, the card shows a success state:

With a saving: `You got the offer price and saved {amount}` / `حصلت على سعر العرض ووفّرت {amount}`

Without a saving amount: `You got the offer price` / `حصلت على سعر العرض`

The saving amount comes formatted from the cart (`discount_total_string`) in the store's currency

### Offer Details #

Offer name shown as a tag chip

Offer description shown under the name when the merchant sets one

### Live Cart Sync #

The cards update when the theme refreshes the cart through `window.zid.cart` — no page reload needed (see Cart Events )

## Theme Usage Examples #

The Bundle Progress is rendered by the **`bundle_progress.jinja`** template. Include it in a page template that has `products` (the page's product list) in its context, such as a category or products listing page.

### Basic Example #

```
`{% include "vitrin:products/bundle_progress.jinja" %}`
```

The template reads the IDs from `products.results` and passes them to the component. If the page has no products, nothing is rendered.

The component can only be rendered **once per page**. A second include on the same page is ignored, and a warning is logged in the console.

### Keeping the Progress in Sync #

The component listens to the cart updates that `window.zid.cart` dispatches. After adding a product to the cart, fetch the cart again so the progress updates:

```
``
```

If your theme updates the cart without calling `window.zid.cart.get()`, ask the component to refetch the cart itself:

```
``
```

## Custom Styles Integration #

The component supports the **Zid Custom Styles system**. You can override specific styles safely without affecting other components.

### How to Use Custom Styles #

```
``
```

The component key for the Bundle Progress is **`bundle_progress`**.

### Available Class Names #

Class Element

`.zid-kit-bundle-progress-list` Wrapper for all offer cards

`.zid-kit-bundle-progress-card` A single offer card

`.zid-kit-bundle-progress-details` Offer name and description column

`.zid-kit-bundle-progress-title` Offer name chip

`.zid-kit-bundle-progress-description` Offer description

`.zid-kit-bundle-progress-bar` Progress row (label + segments, or success message)

`.zid-kit-bundle-progress-bar-label` Progress label (`2 of 3 in your cart`)

`.zid-kit-bundle-progress-segments` Segments container

`.zid-kit-bundle-progress-segment` A single segment

`.zid-kit-bundle-progress-success` Set completed message

To understand the complete flow of the Custom Styles system — including structure, validation, and advanced usage — please refer to the Custom Styles Guide for Theme Developers. (https://docs.zid.sa/custom-styles-guide-1702191m0)

## JavaScript API #

The Bundle Progress has **no** `open()` / `close()` methods — it is an inline component that shows and hides itself based on the cart. You interact with it through the cart API and events.

### Cart Methods #

Method Effect on Bundle Progress

`window.zid.cart.get()` Updates the progress with the returned cart

`window.zid.cart.refreshProducts()` Updates the progress with the returned cart

`window.zid.cart.empty()` Clears the progress (hides all cards)

`window.zid.cart.remove()` Clears the progress (hides all cards)

`window.zid.cart.refetchCartAPI()` The component fetches the cart itself and updates

`window.zid.cart.addProduct()` does **not** update the progress on its own. Call `window.zid.cart.get()` after it.

### Cart Events #

**Event:** `vitrin:cart:bundle-offers-updated`

Dispatched on `window` every time the cart methods above return bundle offers. You can listen to it to build your own bundle UI:

```
``
```

**Event Detail Structure:**

```
``
```

### Offers Endpoint #

The component loads the offers that apply to the page's products from:

```
`GET /api/v1/products/bundle-offers?product_ids=<id>&product_ids=<id>`
```

**Response Structure:**

```
``
```

## Component Behavior #

### Visibility Rules #

A card is shown for an offer only when **all** of the following are true:

1 .

The page has products, and at least one of them belongs to the offer

2 .

The offer uses the **set price** mode and has a set size (`products_quantity`)

3 .

The customer has at least one item toward the set in the cart, **or** has completed a set

The cart is only fetched when the page has a set-price offer, so pages without one make no extra cart request.

### In Progress #

1 .

The customer adds a product from the offer to the cart

2 .

The card appears with the progress label and segments

3 .

Each new item fills one more segment

### Set Completed #

1 .

The customer adds the last item of the set

2 .

The segments are replaced by the success message and the saving amount

3 .

If the customer starts a new set (adds another item after completing one), the card goes back to the progress state for the next set

### Responsive Layout #

**Desktop:** Offer details on one side, a fixed-width (236px) progress bar on the other

**Mobile:** The card wraps and the progress bar takes the full width

## Best Practices #

1 .

**Include the template only on listing pages** that have `products` in context — it renders nothing elsewhere

2 .

**Include it once per page** — duplicate includes are ignored

3 .

**Call `window.zid.cart.get()` after cart changes** so the progress stays in sync

4 .

**Use `window.zid.cart.refetchCartAPI()`** if your theme changes the cart outside `window.zid.cart`

5 .

**Test both states** (in progress and set completed) in Arabic and English to ensure proper styling

## API Reference Summary #

Method/Event Description

`{% include "vitrin:products/bundle_progress.jinja" %}` Renders the component on a listing page

`window.zid.cart.get()` Refreshes the cart and updates the progress

`window.zid.cart.refetchCartAPI()` Makes the component refetch the cart

`vitrin:cart:bundle-offers-updated` Window event with the cart's bundle offers

## Summary #

Shows progress for **set-price bundle offers** configured in the dashboard

Rendered on listing pages through `vitrin:products/bundle_progress.jinja`

Hidden until the customer adds a product from the offer to the cart

Shows a segmented progress bar, then a success message with the amount saved

Supports multiple offers on the same page, one card per offer

Stays in sync with `window.zid.cart` through the `vitrin:cart:bundle-offers-updated` event

Fully customizable through `window.zidCustomStyles.bundle_progress`

Responsive layout for desktop and mobile

Modified at 2026-10-28 09:34:45

Previous

New Gifting Experience

Next

Scripts
