---
# Synced from https://docs.zid.sa/storefront-events-649611m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-storefront-events
title: "StoreFront Events"
product: theme_market
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/storefront-events-649611m0
tags: [from-docs-site, partner-docs]
language: en
---

> StoreFront Events - Zid Docs
# StoreFront Events

Zid App Scripts allow merchants to inject custom JavaScript directly into their storefront through the Partner Dashboard (https://partner.zid.sa). This enables dynamic user interactions and personalized experiences.

This documentation outlines the process of injecting global scripts and implementing event-specific scripts that respond to user actions in real-time.

### Recommended Use Case #

Tracking Storefront Events (for Apps)

If you are building an app inside the Zid Dashboard (either embedded app or external) and need to track storefront events via an injected JavaScript snippet, use the following supported storefront events.

These events are officially exposed for client-side tracking and integration.

## Global and Customer Object Scripting #

Zid's API supports global objects for advanced scripting that load upon page initialization.

### Global Objects #

**Object** **Description**

`window.customer` Contains details of the logged-in customer. Empty if no user is logged in.

`window.customerAuthState` Authentication state object (available immediately on page load).

`window.customerAsync` A Promise that resolves with the customer data once fetched. Useful for async operations when `window.customer` is not yet available.

### Customer Object Blueprint: #

**Parameter** **Description**

`id` Unique identifier for the customer

`name` Full name of the customer

`firstname` First name (derived from full name)

`lastname` Last name (derived from full name)

`mobile` Mobile number of the customer

`email` Email address of the customer

### customerAuthState Object: #

**Parameter** **Description**

`isAuthenticated` `true` if the user is logged in, `false` otherwise

`isGuest` `true` if the user is a guest, `false` otherwise

These global objects enable dynamic interactions and personalized user experiences.

## Event-Driven Scripting #

Zid supports event-driven scripting, allowing JavaScript execution in response to specific storefront events. These events trigger JavaScript functions to track user interactions and enhance engagement.

**Supported Events:**

1 .

Purchase Event

2 .

Product View Event

3 .

Add to Cart Event

4 .

Remove from Cart Event

5 .

Start Checkout Event

6 .

View Item List Event (New)

7 .

Select Item Event (New)

(Please note that `productCart` refers to the product in the cart, and `productViewd` refers to the viewed product. The unconventional spelling is consistent with the codebase.)

### 1. Purchase Event #

Parameter Description

`order` The full order object containing all order details.

`transaction_id` Order ID.

`value` Total order value.

`currency` Currency code (e.g., SAR).

`items` Array of purchased items (see below).

**Items Array:**

Parameter Description

--- ---

`item_id` Product ID

`item_name` Product Name

`item_sku` Product SKU code

`price` Product Price

`quantity` Product Quantity

`item_category` Product Category Name (if available)

#### Legacy System #

In the old system, `transactionItems` was passed as a flat array of products:

Parameter Description

transactionItems List of products the user purchased.

id Order Id

product id Product Id

name Product Name

sku Product Sku code

category Product Category Name

price Product Price

quantity Product Quantity

currency currency

total Product Total

### 2. Product View Event #

Parameter Description

productViewd Single product details object.

id Product Id

name Product Name

sku Product SKU code

category Product Category Name

price Product Price

position Display Order

### 3. Add to Cart Event #

Parameter Description

productCart Single product cart object.

id Product Id

name Product Name

sku Product SKU code

category Product Category Name

price Product Price

position Display Order

quantity Product Quantity

### 4. Remove from Cart Event #

Parameter Description

productCart Single product cart object.

id Product Id

name Product Name

sku Product SKU code

category Product Category Name

price Product Price

position Display Order

quantity Product Quantity

### 5. Start Checkout Event #

The start checkout event now receives the full `cart` object:

**Parameter** **Description**

`id` Unique identifier for the shopping cart.

`session_id` Session identifier.

`products` Array of cart products (see below).

`products_count` Total number of products in the cart.

`products_subtotal` Subtotal of all products before discounts/shipping.

`totals` Array of totals (subtotal, tax, shipping, total).

`currency` Currency object with `cart_currency.code`.

`coupon` Applied coupon object (if any).

**Cart Products Array:**

**Parameter** **Description**

------------------------ -------------------------------------------------------

`product_id` Product ID.

`name` Product name.

`sku` Product SKU code.

`price` Product price.

`quantity` Quantity in cart.

#### Legacy System #

In the old system, the event received flat parameters:

**Parameter** **Description**

`cart_id` Unique identifier for the shopping cart.

`cart_total` Total value of the cart.

`currency` Currency used for the transaction.

`items` List of items in the cart, each represented by its own object.

`item_id` Unique identifier for each product in the cart.

`item_name` Name of the product.

`item_price` Price of the product.

`item_quantity` Quantity of the product in the cart.

`item_category` Category of the product.

`user_id` Unique identifier of the user (if logged in).

`session_id` Unique identifier for the session (if user is not logged in).

`cart_discount` Any discount applied to the cart.

`shipping_cost` Estimated shipping cost for the cart.

`checkout_step` Current step in the checkout process (e.g., shipping, payment, confirmation).

`payment_method` Selected payment method (if chosen).

### 6. View Item List Event (New) #

Fired when a user views a list of products (e.g., category page, search results, product listing).

**Parameter** **Description**

`listName` Name of the list (e.g., category name, "all_products").

`products` Array of products in the list (see below).

**Products Array:**

**Parameter** **Description**

------------------------ -------------------------------------------------------

`item_id` Product ID.

`item_name` Product name.

`item_sku` Product SKU code.

`currency` Currency code.

`price` Product price.

`quantity` Product quantity.

`item_category` Product category name (if available).

### 7. Select Item Event (New) #

Fired when a user clicks on a product in a list to view its details.

**Parameter** **Description**

`product` Product object (same structure as productViewd).

`listName` Name of the list where the product was selected.

## Script Injection for App Partners #

Custom Snippets allow you to inject scripts into stores where your app is installed, enabling enhanced functionality, better store customization, and seamless integration. This feature provides flexibility to optimize the merchant experience without requiring them to manually modify their store's code.

### How to Enable Custom Snippets #

Before publishing, always test your changes in a development store to ensure smooth functionality. Optimize scripts for performance to prevent any impact on storefront loading times.

1 .

Open the Partner Dashboard (https://partner.zid.sa/applications) and navigate to the General Settings of your app.

2 .

Click on Add Snippet and enter your JavaScript or CSS snippet in the provided field.

3 .

Define the snippet's placement and configure any required parameters.

4 .

Submit your changes for review and approval. You can modify or remove the snippet from your app at any time.

Modified at 2026-07-30 11:49:13

Previous

Embedded Apps

Next

Zid MUI
