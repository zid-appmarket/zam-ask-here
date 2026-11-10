---
# Synced from https://docs.zid.sa/cart-1475306m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-cart
title: "Cart"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/cart-1475306m0
tags: [from-docs-site, partner-docs]
language: en
---

> Cart - Zid Docs
# Cart

This page documents the **new** Vitrin cart functions and, under each item, shows the **old Zid** function it replaces.

All functions are available via **`window.zid.cart`**.

## Fetch Cart #

**New:** `zid.cart.get()`

**Old:** `zid.store.cart.fetch()`

**Description:** Get the current cart object (products, totals, coupon, etc.).

**Usage**

```
``
```

**Usage with Tracking Event (Cart Drawer / Sidebar)**

```
``
```

**Notes:**

The `view_cart` event is fired automatically on the cart page `/cart`, so **DON'T** manually call it in the cart page.

For cart drawers or sidebars, call `sendGaCartDetailViewedEvent `manually after fetching the cart.

## Add Product #

**New:** `zid.cart.addProduct(payload)`

**Old:** `zid.store.cart.addProduct({ productId, quantity, ... })`

**Description:** Add a product to the cart. Supports custom options/fields.

### Parameters #

**`product_id`** (required) — Product identifier.

**`quantity`** (required) — Number of units (> 0).

**`custom_fields`** (optional) — Array of selected customizations (only send if the product has options like size, color, add-ons, or extra inputs).

### Custom Fields — Detailed Explanation #

The `custom_fields` parameter allows you to send product customizations (e.g., size, color, engraving text, file uploads) to the backend. It is an **optional** array, and each entry represents one selected option or filled input.

#### Structure of Each Field #

```
`{
price_settings: string | null; // unique ID linking the choice to backend pricing/variants
group_name: string | null; // label of the group (e.g., "Color", "Add-ons")
group_id: string | null; // unique group identifier
name: string | null; // field/option label or name
value: string | null; // user’s input or selected option
type: 'CHECKBOX' | 'DROPDOWN' | 'TEXT' | 'NUMBER' | 'FILE' | 'IMAGE' | 'TEXTAREA';
}`
```

**Note:** `custom_fields` are optional. Only include them if the product has custom options.

#### Option Fields — Checkboxes #

If a customer selects multiple add-ons from a group named Extras :

```
` {
"price_settings" : "5dd00588-2d18-4613-a991-3e23522b1052" ,
"group_name" : "Extras" ,
"group_id" : "4fba4318-e399-4343-ba5f-e70728b419c5" ,
"name" : "Gift Wrap" ,
"value" : "✔" ,
"type" : "CHECKBOX"
} `
```

Each checked option generates a separate object.

#### Option Fields — Dropdowns #

If a customer selects “Red” from a dropdown named Color :

```
` {
"price_settings" : "64c73acb-9d8f-4f1c-afdb-a175bf50ac53" ,
"group_name" : "Color" ,
"group_id" : "bc9b1ba1-3b83-4edd-bb36-1dbf9ca9aaac" ,
"name" : "Red" ,
"value" : "✔" ,
"type" : "DROPDOWN"
} `
```

#### How the Backend Uses `custom_fields` #

1 .

**Price Calculation** – Uses `price_settings` IDs to apply extra charges (e.g., engraving +120 SAR, image upload +150 SAR, color red +234 SAR → total +504 SAR).

2 .

**Validation** – Ensures required fields are filled and option limits are respected.

3 .

**Order Processing** – Saves customization details for fulfillment.

4 .

**Inventory/Variants** – Associates choices with stock and variant tracking.

**Key Point:** `price_settings` is the unique identifier that connects each customization in the cart to backend pricing and inventory logic.

## Update Product #

**New:** `zid.cart.updateProduct({ product_id, quantity })`

**Old:** `zid.store.cart.updateProduct(cart_product_id, quantity, product_id)`

**Description:** Update the quantity for a product **by** its **cart product id** (not the product_id). This is the `id` field from `cart_response.products[index].id`.

**Usage**

```
``
```

## Remove Product #

**New:** `zid.cart.removeProduct({ product_id })`

**Old:** `zid.store.cart.removeProduct(cart_product_id, product_id)`

**Description:** Remove a product **by** its **cart product id** (from `cart_response.products[index].id`).

**Usage**

```
``
```

## Apply Coupon #

**New:** `zid.cart.applyCoupon({ coupon_code })`

**Old:** `zid.store.cart.redeemCoupon(coupon_code)`

**Usage**

```
``
```

## Remove Coupon #

**New:** `zid.cart.removeCoupons()`

**Old:** `zid.store.cart.removeCoupon()`

**Usage**

```
``
```

## Empty / Remove Cart #

**New:**

`zid.cart.empty()` – remove all items (keep cart session)

`zid.cart.remove()` – delete cart session entirely

**Old:**

`zid.store.cart.removeProducts(with_cart_delete)`

**Usage**

```
``
```

## Add Gift Card #

**New:** `zid.cart.addGiftCard(payload)`

**Description:** Add a gift card to the cart with customization details.

### Parameters #

**`receiver_name`** (required) — Name of the gift card recipient.

**`sender_name`** (required) — Name of the person sending the gift card.

**`media_link`** (optional) — URL to an image or media associated with the gift card.

**`gift_message`** (optional) — Personal message to include with the gift card.

**`card_design`** (optional) — Design template url from the store settings.

**Usage**

```
``
```

## Remove Gift Card #

**New:** `zid.cart.removeGiftCard()`

**Description:** Remove the gift card from the cart.

**Usage**

```
``
```

## Get Calculated Points #

**New:** `zid.cart.getCalculatedPoints(cartTotal)`

**Description:** Calculate how many loyalty points the customer will earn for a given cart total.

### Parameters #

**`cartTotal`** (required) — The cart total amount as a number.

**Usage**

```
``
```

## Get Redemption Methods #

**New:** `zid.cart.getRedemptionMethods(currency)`

**Description:** Get available loyalty points redemption methods for the specified currency.

### Parameters #

**`currency`** (optional) — Currency code (default: 'SAR').

**Usage**

```
``
```

## Get Wallet Points Info #

**New:** `zid.cart.getWalletPointsInfo()`

**Description:** Get detailed information about the customer's loyalty wallet and available points.

**Usage**

```
``
```

## Add Redemption Method #

**New:** `zid.cart.addRedemptionMethod({ id: 'redemption_method_123' })`

**Description:** Apply a loyalty redemption method to the current cart to redeem points for discounts or rewards.

### Parameters #

**`id`** (required) — The redemption method identifier.

**Usage**

```
``
```

## Remove Redemption Method #

**New:** `zid.cart.removeRedemptionMethod()`

**Description:** Remove the applied loyalty redemption method from the cart.

**Usage**

```
``
```

## Get Customer Loyalty Points #

**New:** `zid.cart.getCustomerLoyaltyPoints()`

**Description:** Get the customer's current loyalty points balance.

**Usage**

```
``
```

## Notes & Differences #

`id` (cart product id) replaces `cart_product_id` for update/remove operations.

Coupon naming changed from `redeemCoupon` → `applyCoupon` and `removeCoupon` → `removeCoupons`.

Additional helpers available: `empty()` vs `remove()` for different clearing behaviors.

For product/variant selection rules and complex products, see the **Products** page.

Modified at 2026-07-30 11:49:13

Previous

Responses & Errors

Next

Products
