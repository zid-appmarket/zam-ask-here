---
# Synced from https://help-partner.zid.sa/en/articles/11311085-understanding-the-zid-app-scripts-and-event-layer
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: ph-understanding-the-zid-app-scripts-and-event-layer
title: "Understanding the Zid App Scripts and Event Layer"
product: zam
audience: all
status: verified
updated: 2025-05-07
source_url: https://help-partner.zid.sa/en/articles/11311085-understanding-the-zid-app-scripts-and-event-layer
tags: [from-docs-site, partner-help-center]
language: en
---
# What Are App Scripts?

App Scripts allow Zid apps to insert JavaScript directly into merchant storefronts without requiring manual code changes by the merchant. This enables a wide range of features, including:

- Dynamic personalization

- Conversion tracking

- Analytics enhancement

- Storefront interaction customization

**Zid App Scripts support two main script types:**

- **Global Scripts** – loaded on every page

- **Event-Driven Scripts** – triggered by user interactions such as product views, add-to-cart actions, or purchases

(https://downloads.intercomcdn.com/i/o/u7vuis4c/1512104904/e8dd02f85f585157fed6c848e223/image+%281%29.png?expires=1794345300&signature=48512ce0e14cf01d3b9ab69ea046e78796dd0cd45c0470c8fc19626e45280732&req=dSUmFMh%2BmYhfXfMW1HO4zUoZJY0i8Bqck5fZG4hCsnyjGReSD%2FdjuPinnH4R%0AWEPg%2Brjg5YXZKnCFxvU%3D%0A)

## Accessing the Global & Customer Objects

When using Zid App Scripts, developers gain access to special global objects in the browser’s `window` scope. These objects contain useful information that enables contextual behavior based on the user or session.

## Global Object

The `window.customer` object is automatically available on every page. If a customer is logged in, their details are included. If not, the object remains empty.

### Example:

```
console.log(window.customer);
```

## Customer Object Structure

**Parameter**

**Description**

`id`

Unique customer identifier

`name`

Full name of the customer

`mobile`

Mobile number

`email`

Email address

These values allow your scripts to tailor messaging or behavior per customer.

## Tracking Storefront Events

Zid supports a series of predefined **frontend events** that you can hook into using JavaScript. These are triggered automatically based on user behavior.

💡 **Note: **Some variable names like productCart and productViewd follow Zid’s internal naming conventions and may appear unconventional — this is intentional and consistent across the codebase.

# Purchase Event

Triggered after a successful transaction is completed.

## **Event Object:**

```
{ transactionItems: [ { id: "product-1", name: "Product Name", sku: "SKU-123", category: "Category Name", price: 99.99, quantity: 1, currency: "SAR", total: 99.99 } ], id: "order-123" }
```

# Product View Event

Triggered when a user views a product.

## **Event Object:**

```
{ productViewd: { id: "product-1", name: "Product Name", category: "Category Name", price: 99.99, position: 3 } }
```

# Add to Cart Event

Fires when a product is added to the cart.

## **Event Object:**

```
{ productCart: { id: "product-1", name: "Product Name", category: "Category Name", price: 99.99, position: 2, list: "Homepage", quantity: 1 } }
```

# Remove from Cart Event

Fires when a product is removed from the cart.

## **Event Object:**

```
{ productCart: { id: "product-1", name: "Product Name", category: "Category Name", price: 99.99, position: 2, list: "Homepage", quantity: 1 } }
```

# Start Checkout Event

Triggered when the user initiates the checkout process.

## **Event Object:**

```
{ cart_id: "cart-456", cart_total: 199.99, currency: "SAR", cart_discount: 20, shipping_cost: 15, checkout_step: "shipping", payment_method: "credit_card", user_id: "user-123", session_id: "guest-456", items: [ { item_id: "product-1", item_name: "Product A", item_price: 99.99, item_quantity: 2, item_category: "Electronics" } ] }
```

# Injecting App Scripts via Snippets

As a Zid app partner, you can deliver your code to all stores using **Custom Snippets**. These snippets ensure your app's logic is seamlessly applied without manual merchant configuration.

## How to Add Snippets

(https://downloads.intercomcdn.com/i/o/u7vuis4c/1512105860/b1d94a081954eacb50eaa34a3433/image+%282%29.png?expires=1794345300&signature=b8a97ca3dd30bcfef3fafaf5dfb7c3249224bef6c2e18160e1fe02c86d093a13&req=dSUmFMh%2BmIlZWfMW1HO4zb8jFCchGMHONd69CmyDmMrIjjZIuXW62HtI4vsy%0AxJBIVYf12a45nGaQopY%3D%0A)

- Open the **Partner Dashboard**

- Navigate to **General Settings** of your app

- Click **Add Snippet**

- Paste your JavaScript or CSS

- Select snippet **placement** (header, footer, etc.)

- Submit for review and approval

Best Practice: Test all scripts in a staging store before pushing them live. Optimize for performance to avoid impacting store load speed.

## Final Notes

Zid’s App Scripts and event layer open powerful customization possibilities for app partners. With access to real-time storefront events, global objects, and code injection via the dashboard, you can:

- Track customer journeys

- Deliver personalized UX

- Enable analytics and marketing use cases

- Provide dynamic store interactions with minimal setup

Start building with App Scripts today and extend what’s possible for Zid merchants.

Related Articles

- App type and appearance

(https://help-partner.zid.sa/en/articles/8637255-app-type-and-appearance)

- Zid App Market: App Review Requirements Checklist

(https://help-partner.zid.sa/en/articles/10658329-zid-app-market-app-review-requirements-checklist)

- Introduction to Landing Pages on Zid

(https://help-partner.zid.sa/en/articles/11642766-introduction-to-landing-pages-on-zid)

- Oddo Integration - Arabic session on how to connect Odoo with Zid App Market APIs

(https://help-partner.zid.sa/en/articles/12867648-oddo-integration-arabic-session-on-how-to-connect-odoo-with-zid-app-market-apis)

- Guide to Integrating Shipping Systems with the Zid Platform

(https://help-partner.zid.sa/en/articles/15544622-guide-to-integrating-shipping-systems-with-the-zid-platform)
