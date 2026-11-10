---
# Synced from https://docs.zid.sa/checkout-as-a-popup-1806668m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-checkout-as-a-popup
title: "Checkout as a Popup"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/checkout-as-a-popup-1806668m0
tags: [from-docs-site, partner-docs]
language: en
---

> Checkout as a Popup - Zid Docs
# Checkout as a Popup

The checkout popup feature allows customers to display the checkout page inside a modal dialog instead of redirecting customers away from the current page. When enabled, this creates a smoother, faster checkout experience and allows customers to complete their purchase without losing context.

## Enabling the Feature #

The checkout popup becomes available when you include its template in your theme. No dashboard settings are required to activate it.

### How to Enable #

To enable the checkout popup in your theme, include the following template:

```
`{% include "vitrin:checkout/checkout_dialog.jinja" %}`
```

**Best Practice:**

It is recommended to use the checkout popup primarily on the Product Details Page (PDP), where the full product context (variants, quantity, options, etc.) is already available.

If you need to trigger the checkout popup from any other page, make sure you pass the exact same arguments required by the “Add Product” API, so the checkout receives the correct product data more on the add product api — Please refer add product guide for theme developers. (https://docs.zid.sa/cart-1475306m0#add-product)

## Global API Objects #

### `window.checkout_dialog` #

Including the checkout popup template adds a global `checkout_dialog` object to the `window`. This object exposes the following methods:

### Methods #

**open()** – Opens the checkout popup.

**close()** – Closes the checkout popup.

### Usage Examples #

```
``
```

### Theme Usage Examples #

`HTML`

```
``
```

`JS`

```
``
```

## Custom Styles Integration #

The Checkout Popup supports the Zid Custom Styles system. You can override specific styles in a safe, isolated way without affecting other dialogs.

### How to Use Custom Styles #

```
``
```

The component key for the checkout popup is **`checkout_dialog`**.

To understand the complete flow of the Custom Styles system — including structure, validation, and advanced usage — please refer to the Custom Styles Guide for Theme Developers. (https://docs.zid.sa/custom-styles-guide-1702191m0)

## Best Practices #

Include the template **only where checkout can be triggered** (product page).

Always use **optional chaining** when interacting with the API.

Prefer popup-based checkout for better conversion rates and reduced navigation friction.

If you need to run “Buy Now” or custom checkout flows, always pass a clear `source` identifier.

## API Reference Summary #

Method Parameters Description

`window.checkout_dialog.open()` none Opens the checkout popup

`window.checkout_dialog.close()` none Closes the checkout popup

## Summary #

Enabled by including `{% include "vitrin:checkout/checkout_dialog.jinja" %}`

Add only where checkout can be triggered in the product details page.

Exposes `window.checkout_dialog` global object

Supports custom flow types through `source`

Optional chaining recommended

Fully style-able through `window.zidCustomStyles.checkout_dialog`

Modified at 2026-07-30 11:49:13

Previous

Login as a Popup

Next

Apple Pay Quick Checkout
