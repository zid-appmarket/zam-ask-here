---
# Synced from https://docs.zid.sa/gift-card-as-a-popup-1697835m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-gift-card-as-a-popup
title: "Gift Card as a Popup"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/gift-card-as-a-popup-1697835m0
tags: [from-docs-site, partner-docs]
language: en
---

> Gift Card as a Popup - Zid Docs
# Gift Card as a Popup

The **Gift Card** feature allows customers to add personalized gift details such as sender name, receiver name, message, and optional media links.

To enable this feature, you need to include the provided dialog template and implement a button to open it.

## Integration Requirements #

### 1. Check Feature Availability #

Before including or using the gift card feature, ensure it is **enabled** in the store settings.

If the flag is disabled, the feature will not work even if the template is included.

```
`{% if safeget(store, "settings.checkout.gift_order_settings.is_gift_order_enabled", False) == '1' %}
{% include 'vitrin:cart/gift-card.jinja' %}
{% endif %}`
```

This flag can be managed by the merchant in the store’s **Dashboard → Settings → Gifting** section.

URL pattern:

```
`https://dashboard.zid.sa/en-sa/stores/<store_id>/settings/gifting`
```

### 2. Include Gift Card Template #

If the feature is enabled, include the following template in your cart page:

```
`{% include 'vitrin:cart/gift-card.jinja' %}`
```

This template is responsible for rendering the gift dialog. No additional implementation inside the template is required.

### 3. Add Toggle Button #

Add a button anywhere in the cart page to allow users to open the gift card dialog.

Example:

```
``
```

You can also close the dialog manually if needed using:

```
``
```

The dialog automatically closes after successful submission.

### 4. Listen for Gift Submission Event #

When the gift card form is successfully submitted, a custom event is triggered:

```
``
```

**`event.detail.data`** returns the **updated cart object**.

No need to refetch the cart — simply update your DOM with the new cart data.

### 5. Display Gift Card Details in Cart #

You can use the `gift_card_details` object from the cart data to display the current gift information:

```
``
```

Use this data to show a summary card or banner inside your cart if desired.

## Custom Styles Integration #

You can customize the look and feel of the **Gift Dialog** using the Zid SDK Custom Styles system. This allows you to apply your own CSS overrides for specific components without affecting other areas of the store.

## How to Use Custom Styles #

You can define your custom styles globally using the `window.zidCustomStyles` object. The SDK will automatically apply these styles to the corresponding components, ensuring proper scoping and isolation.

### Example #

```
``
```

In the example above, the **component key** for the gift dialog is clearly shown as:

```
`gift_dialog`
```

You can use this key in your `window.zidCustomStyles` object to apply any style overrides specific to the gift feature.

To understand the complete flow of the Custom Styles system — including structure, validation, and advanced usage — please refer to the **Custom Styles Guide for Theme Developers**. (https://docs.zid.sa/custom-styles-guide-1702191m0)

## Summary #

Action Description

Check flag `safeget(store, "settings.checkout.gift_order_settings.is_gift_order_enabled", False)` must return `'1'`

Include template `{% include 'vitrin:cart/gift-card.jinja' %}` in cart page

Open dialog `window.gift_dialog.open()`

Close dialog `window.gift_dialog.close()` (optional)

Listen for event `vitrin:gift:submitted` → returns updated cart

Gift details Available in `cart.gift_card_details`

## Notes #

Ensure the flag `safeget(store, "settings.checkout.gift_order_settings.is_gift_order_enabled", False)` returns `'1'` before including the template.

Merchants can enable or disable the feature from the **Dashboard → Settings → Gifting** section.

URL pattern: `https://dashboard.zid.sa/en-sa/stores/<store_id>/settings/gifting`

Include `vitrin:cart/gift-card.jinja` in your theme’s cart page to enable the feature.

Use `window.gift_dialog.open()` and `window.gift_dialog.close()` to control the dialog.

The dialog automatically closes on successful submission.

Listen to the `vitrin:gift:submitted` event to update your cart dynamically without refetching.

Use `cart.gift_card_details` to display existing gift details in the cart.

Modified at 2026-07-30 11:49:13

Previous

Custom Styles Guide

Next

Addresses as a Popup
