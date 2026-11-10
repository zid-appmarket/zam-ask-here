---
# Synced from https://docs.zid.sa/dynamic-bundle-products-1893948m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-dynamic-bundle-products
title: "Dynamic Bundle Products"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/dynamic-bundle-products-1893948m0
tags: [from-docs-site, partner-docs]
language: en
---

> Dynamic Bundle Products - Zid Docs
# Dynamic Bundle Products

The Dynamic bundle products feature allows the customer to select products that they want in a bundle.

## Enabling the Feature #

The dynamic bundle products becomes available when you include its template in your theme and the product is a type dyanmic bundle you can create one from the products and and choose `Dynamic bundle`.

**Path:** `https://dashboard.zid.sa/en-sa/stores/<store_id>/catalog/products`

### How to Enable #

To enable the dynamic bundle products section in your theme, include the following template:

```
`{% if product.product_class == 'dynamic_bundle' %}
{% include 'vitrin:products/bundle-products.jinja' %}
{% endif %}`
```

**Best Practice:**

It is mandatory to add the dynamic bundle primarily on the Product Details Page (PDP), where the full product context and the `product_class` is available.

## Theme Usage Example: #

```
``
```

🔴 **Important:** The `vitrin:bundle-selections:updated` event will get trigger every time the customer change the selected product bundle so you will get the values of the selected bundle products and you need to store it for later because you will need to send it to the add product api -- Please refer add product guide for theme developers. (https://docs.zid.sa/cart-1475306m0#add-product)

#### **Example on how to add selected bundle product to cart** #

```
``
```

## Custom Styles Integration #

The Checkout Popup supports the Zid Custom Styles system. You can override specific styles in a safe, isolated way without affecting other dialogs.

### How to Use Custom Styles #

```
``
```

The component key for the checkout popup is **`bundle_selection`**.

To understand the complete flow of the Custom Styles system — including structure, validation, and advanced usage — please refer to the Custom Styles Guide for Theme Developers. (https://docs.zid.sa/custom-styles-guide-1702191m0)

## Best Practices #

Include the template in product details page.

Always use **optional chaining** when interacting with the API.

Add event listener to `vitrin:bundle-selections:updated` event so you can recevie the selected customer bundler.

## Events Reference Summary #

Events Description

`vitrin:bundle-selections:updated` This event is triggered on every change made by the customer within the dynamic bundle.

## Summary #

Allows customers to create and customize their own product bundles by selecting items dynamically.

Becomes available when the product type is set to Dynamic Bundle and the bundle template is included in the PDP.

Emits the `vitrin:bundle-selections:updated` event on every customer selection change.

Requires storing the emitted bundle payload and sending it with the add-to-cart request.

Supports Zid Custom Styles for safe and isolated UI customization.

Modified at 2026-04-16 11:17:28

Previous

Region & Language Popup

Next

Progressive Discounts
