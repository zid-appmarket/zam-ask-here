---
# Synced from https://docs.zid.sa/overview-1341008m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-overview-831465
title: "Overview"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/overview-1341008m0
tags: [from-docs-site, partner-docs]
language: en
---

> Overview - Zid Docs
# Overview

This section describes the Webhook endpoint used to send events to Zid Payments. It outlines all the necessary webhook events and their specifications.

**Path:**

/api/webhook/v1/thirdpartywebhook

**Request Model:**

Input Parameter Type Description Required

type string Event type Types: “merchant_linked”, “payment_paid”, “refund_status_changed” Y

thirdPartyId string Provider Unique ID, Which is assigned to each provider on the initial phases of the integration Y

merchantId string Merchant ID on the provider side Y

data Object Each Event has its own object dto, Examples: Link Merchant Event (https://docs.zid.sa/api-17956108), Payment Paid Event (https://docs.zid.sa/api-17956148), Refund Event (https://docs.zid.sa/api-17956149) Y

Modified at 2026-07-30 11:49:13

Previous

Request Refund

Next

Link Merchant Event
