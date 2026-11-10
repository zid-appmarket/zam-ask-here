---
# Synced from https://docs.zid.sa/progressive-discounts-2072813m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-progressive-discounts
title: "Progressive Discounts"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/progressive-discounts-2072813m0
tags: [from-docs-site, partner-docs]
language: en
---

> Progressive Discounts - Zid Docs
# Progressive Discounts

The Progressive Discount feature displays a tiered discount progress meter in the cart/checkout flow. It motivates customers to increase their cart value or quantity by showing how close they are to unlocking the next discount tier.

## Merchant Setup #

Go to Marketing → Discounts (https://dashboard.zid.sa/ar-sa/stores/423202/marketing/discounts) → Create, then select Progressive Discount.

**From there, the merchant configures:**

**Offer details** — name, start/end dates, offer scope (cart total or cart quantity), and discount type (percentage or fixed amount)

**Tiers** — 2 to 3 tiers, each with a minimum threshold and discount value. Thresholds and discount values must increase with each tier. A max discount cap is available when percentage is selected.

**Usage limits** (optional) — total redemptions and per-customer limits

Internal note (optional)

**Setting** **Details**

**Discount Basis** Cart total (SAR) or Cart quantity (item count)

**Benefit Types** Percentage off or Fixed amount off

**Tier Limits** Min 2, max 3 tiers per offer

**Active Offers** Only one progressive discount can be active at a time

**Product Scope** Applies to the entire cart — no product-level inclusion/exclusion

#### Stacking behavior: #

✅ Stacks automatically with automatic free shipping and wallet balance redemption

✅ Can stack with bundle offers and loyalty redemption — requires enabling a flag in the checkout page settings

❌ Does not stack with discount codes or other automatic discounts — the higher-value discount wins

## Theme Developer Integration #

To render the Progressive Discount component in your theme, add the following Jinja include to your cart page template:

```
`{% include 'vitrin:cart/progressive_discount.jinja' %}`
```

The component renders automatically when the feature is enabled and an active progressive discount rule exists.

### Component States #

#### ⌛️ Loading State #

Displays a skeleton loader while fetching cart data.

#### 🔁 In Progress State #

Shows:

A message indicating how much more the customer needs to reach the next tier

A progress bar reflecting current progress percentage

Tier markers in pending/reached states

Primary color scheme

#### ✅ All Tiers Completed State #

Shows:

A success message confirming all tiers are unlocked

A full (100%) progress bar

All tier markers with check icons

Green/success color scheme

### Customization #

You can override the default styles using the Zid SDK Custom Styles system via the `window.zidCustomStyles` object. The component key is `progressive_discount`.

#### Example #

```
``
```

### Full CSS Class Reference #

```
``
```

#### Class Reference Table #

Class Name Element Description

.zid-kit-progressive-discount` Root Main wrapper container

.zid-kit-progressive-discount-card` AppCard Card with primary border

.zid-kit-progressive-discount-content` StackColumn Content with dynamic background

.zid-kit-progressive-discount-message` StackColumn/AppTypography Message container

.zid-kit-progressive-discount-message-completed` AppTypography Completed state message

.zid-kit-progressive-discount-message-quantity` AppTypography Quantity-based message

.zid-kit-progressive-discount-message-total` AppTypography Total-based message

.zid-kit-progressive-discount-message-highlight` AppTypography Highlighted text in messages

.zid-kit-progressive-discount-progress-wrapper` Box Progress bar container

.zid-kit-progressive-discount-progress-bar` LinearProgress Progress bar element

.zid-kit-progressive-discount-tier` StackColumn Tier marker container

.zid-kit-progressive-discount-tier-reached` StackColumn Reached tier modifier

.zid-kit-progressive-discount-tier-pending` StackColumn Pending tier modifier

.zid-kit-progressive-discount-tier-avatar` Avatar Tier circle

.zid-kit-progressive-discount-tier-check` IconCheckLine Check icon (reached)

.zid-kit-progressive-discount-tier-benefit` AppTypography Benefit text (pending)

.zid-kit-progressive-discount-tier-label` AppTypography Label below tier

.zid-kit-progressive-discount-skeleton` StackColumn Skeleton container

.zid-kit-progressive-discount-skeleton-message` StackRow Skeleton message row

.zid-kit-progressive-discount-skeleton-text` Skeleton Skeleton text

.zid-kit-progressive-discount-skeleton-progress` Skeleton Skeleton progress bar

For complete Custom Styles documentation, see the **Custom Styles Guide for Theme Developers**. (https://docs.zid.sa/custom-styles-guide-1702191m0)

## Best Practices #

1 .

**Automatic cart updates** — The component listens to `cart:refetch` events and re-renders when the cart changes.

2 .

**Loading states** — A skeleton loader displays while cart data is being fetched, preventing layout shift.

3 .

**RTL support** — The progress bar handles RTL layouts automatically via CSS transforms.

4 .

**Dynamic tier positioning** — Tier markers are positioned proportionally based on tier count (2 or 3).

5 .

**Responsive design** — The component is designed to work across all screen sizes.

Modified at 2026-04-16 11:19:50

Previous

Dynamic Bundle Products

Next

Bank Discounts
