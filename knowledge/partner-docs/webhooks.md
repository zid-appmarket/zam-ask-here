---
# Synced from https://docs.zid.sa/webhooks
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-webhooks
title: "Overview"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/webhooks
tags: [from-docs-site, partner-docs]
language: en
---

> Overview - Zid Docs
# Overview

Webhooks allow you to receive real-time data updates for various events. These events can range from order creation to customer login activities. This page serves as a comprehensive guide to understanding the supported webhook events, their payloads, and any conditions that can be applied to them.

# How to Subscribe #

To subscribe to these webhook events, follow these steps:

1 .

Choose the event(s) you would like to subscribe to from the list of Supported Webhook Events below.

2 .

(Optional) If the event supports `conditions`, check out the Event Conditions section to learn how to populate the `conditions` field.

3 .

Use the Merchant API to make a request to the Create a Webhook endpoint (Link to API documentation (https://docs.zid.sa/create-a-webhook?nav=1)).

In case you require an event or a condition that is not yet supported, please send your suggestion to the Zid App Market Support .

# Merchant Events #

The tables below provide a list of merchant events, including their names, descriptions, and hyperlinks to the data structure (schema) of each event's payload. Event names that support conditions are linked to the section detailing their supported conditions.

## Order Events #

Event Name Description Payload Schema

order.create (Supports `conditions`) Triggered when a new order is created. Order schema

order.status.update (Supports `conditions`) Triggered when an order's status is updated. Order schema

order.payment_status.update Triggered when an order's payment status changes to `paid` or `unpaid`. Note that `unpaid` includes `pending`, `refunded`, and `voided` statuses. Order schema

## Product Events #

Event Name Description Payload Schema

product.create Triggered when a new product is created. Product schema

product.update Triggered when a product's details are updated. Product schema

product.publish Triggered when a product is published. Product schema

product.delete Triggered when a product is deleted. Product deleted schema

## Abandoned Cart Events #

Event Name Description Payload Schema

abandoned_cart.created Triggered when a shopping cart is abandoned. Abandoned Cart schema

abandoned_cart.completed Triggered when an abandoned cart is completed. Abandoned Cart schema

## Customer Events #

Event Name Description Payload Schema

customer.create Triggered when a new customer account is created. Customer schema

customer.update Triggered when a customer's details are updated. Customer schema

customer.merchant.update Triggered when a merchant's details related to a customer are updated. Payload

customer.login Triggered when a customer logs in. Customer schema

## Product Category Events #

Event Name Description Payload Schema

category.create Triggered when a new category is created. Category schema

category.update Triggered when a category's details are updated. Category schema

category.delete Triggered when a category is deleted. Category schema

# Event Conditions #

The `conditions` field in the request body allows you to specify additional criteria for your webhook subscription. By setting conditions, you can filter the events that trigger the webhook. For instance, you may want to receive notifications only when an order's status changes to 'delivered' or if the payment method is 'Cash On Delivery'.

**Note:** Conditions are currently supported only for the `order.create` and `order.status.update` events.

## Supported Conditions #

Condition Key Data Type Description Possible Values

`delivery_option_id` Integer The delivery option ID in Zid. Any valid delivery option ID

`status` String Filters the event based on the status of the order. `new`, `preparing`, `ready`, `inDelivery`, `delivered`, `cancelled`

`payment_method` String Filters the event based on the payment method used. `Cash On Delivery`, `Credit Card`, `Bank Transfer`

## Example Usage #

To set conditions, include the `conditions` field in the request body when creating or updating a webhook subscription. Here's an example:

```
` {
"conditions" : {
"delivery_option_id" : "55" ,
"payment_method" : "Cash On Delivery"
}
}
`
```

Modified at 2026-07-30 11:49:13

Previous

List

Next

Webhook Health Tracking
