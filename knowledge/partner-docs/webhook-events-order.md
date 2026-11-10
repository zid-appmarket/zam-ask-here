---
# Synced from https://docs.zid.sa/webhook-events-order
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-webhook-events-order
title: "Order"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/webhook-events-order
tags: [from-docs-site, partner-docs]
language: en
---

> Order - Zid Docs
# Order

**Currency Handling for Orders**

When the store currency, order currency, and the currency of the shipping address (for cash on delivery) are different, partners must convert the order total to the appropriate currency. The order details already provide both the currency type and the conversion rate, making it easy to apply the conversion when necessary. This ensures that the correct amount is processed smoothly, even when multiple currencies are involved.

**Email Handling in Webhook Payloads for Shipping Partners**

Some webhook payloads may include `placeholder email` addresses that are `not deliverable`. These addresses are operational placeholders and will not reach customers.

Order

###

Modified at 2026-07-30 11:49:13

Previous

Webhook Health Tracking

Next

Product
