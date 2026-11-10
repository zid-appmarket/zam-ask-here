---
# Synced from https://docs.zid.sa/new-gifting-experience-2381965m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-new-gifting-experience
title: "New Gifting Experience"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/new-gifting-experience-2381965m0
tags: [from-docs-site, partner-docs]
language: en
---

> New Gifting Experience - Zid Docs
# New Gifting Experience

The **Gifting Experience** allows customers to add gifting options and personalized gift details to their order.

The gifting experience itself is fully managed by Zid. Theme developers only need to integrate the provided dialog and add an entry point to open it.

## Integration Requirements #

### 1. Check Feature Availability and Include the Template #

Before using the gifting experience, make sure it is enabled in the store settings.

If the feature is enabled, include the gifting template in your cart page:

```
`{% if safeget(store, "settings.checkout.gift_order_settings.is_gift_order_enabled", False) == '1' %}
{% include 'vitrin:cart/gift-card.jinja' %}
{% endif %}`
```

The template renders the Zid-managed gifting dialog. No additional implementation inside the dialog is required.

Merchants can enable or disable gifting from:

**Dashboard → Settings → Gifting**

URL pattern:

```
`https://dashboard.zid.sa/en-sa/stores/<store_id>/settings/gifting`
```

### 2. Add a Gifting Entry Point #

Add an entry point in the cart page that customers can use to open the gifting dialog.

Example:

```
``
```

To open the dialog programmatically:

```
``
```

You can also close it manually if needed:

```
``
```

The dialog automatically closes after a successful submission.

### 3. Listen for Gift Submission #

When the gifting form is successfully submitted, Zid triggers the following custom event:

```
``
```

`event.detail.data` returns the updated cart object.

You do not need to refetch the cart after submission.

Use the returned cart data to update your cart UI.

### 4. Display Gift Details in the Cart #

You can use the `gift_card_details` object from the cart data to display the current gift information.

Example:

```
``
```

You can use this data to display a gift summary, banner, or other cart UI if needed.

## Custom Styling #

The gifting dialog uses Zid's native experience and styling.

If your theme requires supported style adjustments, you can target the gifting dialog using the following component key in the Zid Custom Styles system:

```
`gift_dialog`
```

For implementation details, see the Custom Styles Guide for Theme Developers (https://docs.zid.sa/custom-styles-guide-1702191m0).

## Summary #

Action Description

Check availability `safeget(store, "settings.checkout.gift_order_settings.is_gift_order_enabled", False)` must return `'1'`

Include template `{% include 'vitrin:cart/gift-card.jinja' %}`

Open dialog `window.gift_dialog.open()`

Close dialog `window.gift_dialog.close()`

Listen for submission `vitrin:gift:submitted`

Updated cart Available in `event.detail.data`

Gift details Available in `cart.gift_card_details`

Custom styles key `gift_dialog`

The gifting experience itself is managed by Zid. Themes should integrate the provided component rather than recreate the gifting flow.

Modified at 2026-09-28 09:15:23

Previous

Coupon Form Visibility

Next

Bundle Progress
