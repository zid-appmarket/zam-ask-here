---
# Synced from https://docs.zid.sa/customer-wallet-cashback-2072778m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-customer-wallet-cashback
title: "Customer Wallet & Cashback"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/customer-wallet-cashback-2072778m0
tags: [from-docs-site, partner-docs]
language: en
---

> Customer Wallet & Cashback - Zid Docs
# Customer Wallet & Cashback

The **Customer Wallet (Cashback)** feature displays a cashback progress meter and wallet available balance in the cart and checkout flows. It motivates customers to complete their purchase or add more items by showing how close they are to earning cashback rewards.

## Merchant Setup #

Go to Loyalty (https://dashboard.zid.sa/ar-sa/stores/3/marketing/loyalty-programs) → Customer Wallet → Activate

**From there, the merchant manages customer wallets and configures order cashback offers:**

**Setting** **Details**

**Details** offer name (internal, not shown to customers), start date, and optional end date

**Cashback value** Percentage of order total (with optional max cap) or Fixed amount

**Calculation Basis** Order value, excluding shipping fees

**Min Order Amount** Optional threshold to qualify

**Cashback Validity** Optional expiry in days from order creation

### Plan Availability #

Plan Access

**Elite / Professional** Included for free

**All other plans** Requires a paid monthly subscription, available as an add-on

## Theme Developer Integration #

To render the Customer Wallet Progress component in your theme, add the following Jinja include to your cart page template:

```
`{% include 'vitrin:cart/customer_wallet_progress.jinja' %}`
```

The component renders automatically when the feature is enabled.

### Component States #

The component displays different states based on the customer's cart value and authentication status:

State Description

Guest (Not Eligible) Progress toward cashback with a login prompt

Guest (Eligible) Full progress with login prompt to claim cashback

Logged-in (Not Eligible) Progress toward the cashback threshold

Logged-in (Eligible) Completed progress with cashback amount earned

#### ⌛️ Loading State #

Displays a skeleton loader while fetching cart and wallet data.

#### 🔁 Not Eligible State #

Shows:

Wallet icon with primary color

Progress bar indicating how much more is needed

Gift icon on the progress bar

Remaining amount to reach the cashback threshold

Login button (guests) or current wallet balance (logged-in users)

Primary color scheme

#### ✅ Eligible State #

Shows:

Wallet icon with success (green) color

Completed (100%) progress bar

Check icon on the progress bar

Success badge with the cashback amount

Login button (guests) or current wallet balance (logged-in users)

Green/success color scheme

### Cashback Types #

The wallet supports two types of cashback rules:

**Percentage-based** - Customer earns a percentage of their order value (e.g., 5%)

**Fixed Amount** - Customer earns a fixed amount (e.g., 10 SAR)

### Login Integration #

The component integrates with the Login Popup so users authenticate without leaving the cart page.

**User flow:**

1 .

Guest adds items to cart

2 .

Wallet progress shows: "Add X more to earn Y cashback"

3 .

User clicks the **Login** button

4 .

Login popup opens (if enabled)

5 .

On success, the `vitrin:auth:success` event fires

6 .

The component automatically updates to the logged-in state, fetches the wallet balance, and refreshes progress/eligibility

**Why it matters:**

**No Page Reload** - Users stay on the cart/checkout page

**Seamless Experience** - Login happens in a popup without navigation

**Automatic Updates** - Wallet data refreshes automatically after login

**Encourages Conversion** - Easy login flow reduces cart abandonment

### Customization #

You can override the default styles using the Zid SDK Custom Styles system via the `window.zidCustomStyles` object. The component key is `customer_wallet_progress`.

#### Example #

```
``
```

In the example above, the **component key** for the wallet progress is `customer_wallet_progress`

You can use this key in your `window.zidCustomStyles` object to apply any style overrides specific to the wallet progress component.

### Full CSS Class Reference #

```
``
```

#### Class Reference Table #

Class Name Element Description

`zid-kit-customer-wallet` Root Main wrapper container

`zid-kit-customer-wallet-card` AppCard Card with dynamic background color

`zid-kit-customer-wallet-content` StackColumn Main content layout

`zid-kit-customer-wallet-header-row` StackRow Icon and header container

`zid-kit-customer-wallet-icon-container` StackRow Wallet icon wrapper

`zid-kit-customer-wallet-header` StackColumn Title and description wrapper

`zid-kit-customer-wallet-title-row` StackRow Title and badge row

`zid-kit-customer-wallet-title` AppTypography Title text

`zid-kit-customer-wallet-badge` Status Eligible status badge

`zid-kit-customer-wallet-description` AppTypography Description text

`zid-kit-customer-wallet-progress-container` Box Progress section wrapper

`zid-kit-customer-wallet-progress-bar` StackColumn Progress bar outer wrapper

`zid-kit-customer-wallet-progress-bar-wrapper` Box Progress bar inner wrapper

`zid-kit-customer-wallet-linear-progress` LinearProgress Progress bar element

`zid-kit-customer-wallet-check-icon` StackRow Check icon (active state)

`zid-kit-customer-wallet-gift-icon` StackRow Gift icon (inactive state)

`zid-kit-customer-wallet-guest-actions` Box Guest actions container

`zid-kit-customer-wallet-login-button` AppButton Login button

`zid-kit-customer-wallet-balance` AppTypography Balance text

`zid-kit-customer-wallet-balance-amount` AppTypography Balance amount

`zid-kit-customer-wallet-skeleton` AppCard Skeleton card

`zid-kit-customer-wallet-skeleton-*` Skeleton Various skeleton elements

For complete Custom Styles documentation, see the **Custom Styles Guide for Theme Developers**. (https://docs.zid.sa/custom-styles-guide-1702191m0)

## Best Practices #

1 .

**Login popup integration** — Ensure the Login Popup feature is enabled for the best experience. The component uses it automatically when available, and falls back to the `/auth/login` redirect if `window.auth_dialog` is not available.

2 .

**No manual event handling** — The component handles the `vitrin:auth:success` event internally; no extra listeners are needed for wallet updates.

3 .

**Automatic cart updates** — The component listens to `cart:refetch` events and re-renders when the cart changes.

4 .

**Loading states** — A skeleton loader displays while data is being fetched, preventing layout shift.

5 .

**RTL support** — The progress bar handles RTL layouts automatically via CSS transforms.

Modified at 2026-09-01 20:20:38

Previous

Bank Discounts

Next

Add Preorder Support to Your Theme
