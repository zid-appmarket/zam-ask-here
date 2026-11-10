---
# Synced from https://docs.zid.sa/apple-pay-quick-checkout-1859764m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-apple-pay-quick-checkout
title: "Apple Pay Quick Checkout"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/apple-pay-quick-checkout-1859764m0
tags: [from-docs-site, partner-docs]
language: en
---

> Apple Pay Quick Checkout - Zid Docs
# Apple Pay Quick Checkout

The **Apple Pay Quick Checkout** feature allows customers to complete their purchase quickly using Apple Pay.

The behavior of the button depends on **where you include the template**:

1 .

**Product Details Page** → Apple Pay sells **a single product** (does NOT affect the regular cart).

2 .

**Any Other Page (e.g., Cart Page)** → Apple Pay sells the **entire existing cart**.

## Modes & Page Placement #

### 1. Product Page – Buy a Single Product #

When you include the template **inside the product details page**, Apple Pay will:

Sell **only the selected product**.

**Not modify** the store’s regular cart (no add/remove).

This is ideal for **“Buy Now”** style flows from the product page.

If you are using:

The default quantity input (with the standard id),

The default custom fields templates,

then **no extra work is required** from your side.

If you are using a fully custom UI, see the sections below for how to keep `selected_quantity` and `custom_fields_payload` updated.

### 2. Cart Page / Other Pages – Buy the Entire Cart #

When you include the same template **inside any other page** (for example, the **cart page**) the button will:

Sell the **entire existing cart**.

Require that the cart already contains products.

In this mode, Apple Pay represents a **“Pay for current cart”** action.

#### Important Requirement (Cart Mode) #

Before showing the Apple Pay button in cart mode, you **must ensure there are products in the cart**.

If the cart is empty, you should **hide** the Apple Pay button.

You can use your existing cart logic or Zid APIs to:

Check cart line items count

Decide whether to render the button or not

### 3. Single Instance per Page #

You must **not include the Apple Pay Quick Checkout template more than once on the same page.**

If the template is included **twice**:

The system will log a **warning**.

**Only the first instance** of the template will be rendered and used.

Additional instances will be ignored.

**Best Practice:** Ensure that each page includes the Apple Pay template **once only** – either:

Once on the **product page** (single product mode), or

Once on the **cart / other page** (cart mode).

## Integration #

Include the Apple Pay Quick Checkout template in your page:

```
`{% include 'vitrin:checkout/apple-pay-quick-checkout.jinja' %}`
```

How it works based on placement:

**Inside Product Details Page**

Mode: **Buy a Single Product**

Uses `window.productObj.selected_product`

Does **not** affect the regular cart

**Inside Cart Page or Any Other Page**

Mode: **Sell Existing Cart**

Uses the current cart content

Requires **cart to have items** before showing the button

## Global Product Object (Product Page Mode) #

If your theme is using:

1 .

**The default quantity input**, which:

Has the expected id (e.g., `product-quantity`)

Uses the standard input/select behavior

2 .

**The default Vitrin custom fields templates**

…then everything works automatically without any additional code.

However, if your theme uses a **fully custom UI** for quantity or custom fields, you only need to keep **two values** updated inside:

```
``
```

The required fields are:

`selected_quantity`

`custom_fields_payload`

`window.productObj.selected_product` is always defined on the product details page.

your responsibility is simply to keep these two values updated whenever the user changes them.

## Testing #

1 .

**Product Page Mode (Single Product)**

Open the product page in **Safari** (macOS / iOS).

In the browser console, inspect the selected product:

```
``
```

Change:

Quantity

Custom fields

Confirm that:

`selected_quantity` reflects the latest quantity.

`custom_fields_payload` contains the expected values.

Click the Apple Pay button and complete a test transaction:

The correct product and quantity are used.

Custom fields and bundle items are sent as expected.

The regular cart is **not changed**.

2 .

**Cart Mode (Entire Cart)**

Open the cart page (or any other page where you include the template).

Make sure the cart has products.

Ensure your logic hides the button when the cart is empty.

Click the Apple Pay button and confirm:

The entire cart is sold.

Behavior matches your expected cart flow.

## Summary #

Placement determines behavior:

**Product Page** → Apple Pay sells **a single product** (does not affect the cart).

**Cart / Other Page** → Apple Pay sells the **entire existing cart**.

In product page mode:

Default templates: **no extra work** for quantity/custom fields.

Custom themes must:

Update `selected_quantity` on quantity change.

Update `custom_fields_payload` on custom field change (same as Add to Cart).

In cart mode:

Button requires a **non-empty cart**.

Theme should **hide or disable** the button when the cart is empty.

Template must be included **only once per page**:

Multiple inclusions trigger a warning.

Only the **first instance** will be rendered.

Apple Pay reads values at click time, always ensure `selected_product` (product page) and cart (cart mode) are up to date.

Modified at 2026-07-30 11:49:13

Previous

Checkout as a Popup

Next

Region & Language Popup
