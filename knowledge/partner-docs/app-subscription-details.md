---
# Synced from https://docs.zid.sa/app-subscription-details
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-app-subscription-details
title: "Subscription Details"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/app-subscription-details
tags: [from-docs-site, partner-docs]
language: en
---

> Subscription Details - Zid Docs
# Subscription Details

GET

https://api.zid.sa/ v1/market/app/subscription

This endpoint returns the current state of a merchant's subscription to your app: the plan they are on, its status, its dates, and — for usage-based plans — their charges.

🔑Scopes

`Subscription.read` - Subscription Read Tokens carry this scope internally as `third_subscription_read`. If you are inspecting a token's scopes while debugging, that is the name you will see.

**No parameters are needed.** Your app is identified from the `Authorization` token and the merchant from their `X-Manager-Token`. Do not send an app id.

### What it returns #

The merchant's **most recent** subscription to your app, which is not necessarily an active one — it can be expired, cancelled or refunded. Always check `subscription_status` before treating it as current.

`subscription` is returned **empty** (`"subscription": []`) when the merchant has not activated a plan. Installing your app is not enough on its own: the merchant has to activate a free plan, start a trial, or pay for a plan before a subscription exists. An app with no plans will always return empty here, so this endpoint cannot be used to confirm an installation — use the `app.market.application.install` event for that.

### Usage-based plans only #

`pending_charges`, `settled_charges` and `charges` are returned **only when `is_usage_based` is `1`**. On a free or recurring plan they are not in the response at all.

`pending_charges` — the outstanding charge's amount in SAR, covering a charge that is either pending or overdue. `0.0` when there is none.

`settled_charges` — the total of every charge paid on this subscription, in SAR, for its whole lifetime.

`charges` — the **10 most recent** charges, newest first. Older charges are not returned, so do not rely on this list for complete billing history.

### Amounts #

A charge carries its amount twice, in two different units:

`amount` is in **SAR** — for example `345.00`

`amount_details.amount` is in **halalas** — for example `34500`

`amount_details` is returned empty when the amount is zero. Its `currency` reflects the store's currency, which is not always SAR.

### What this endpoint does not return #

`plan_id`, `plan_type`, `store_uuid`, and any trial information. In particular:

If you key merchants on `store_uuid` from webhook events, you cannot match that against this response — it only carries the numeric `store_id`. Store both.

There is no field telling you whether a merchant is on a free trial or whether a trial is still running. Calculate it from `start_date` plus the trial length you set on the plan.

### Related #

Webhook events tell you when a subscription changes ; this endpoint tells you what is true now . Most apps need both — see **Subscription and app events**.

## Request

Header Params

###

## Responses

🟢 200 OK

application/json

Body application/json

###

🟠 401 Unauthorized

🔴 500 Internal Server error

Request Request Example

Shell

JavaScript

Java

Swift

```
` curl --location 'https://api.zid.sa/v1/market/app/subscription' \
--header 'Authorization: {{Autherization}}' \
--header 'X-Manager-Token: {{Access-Token}}' \
--header 'Accept-Language: en' \
--header 'Accept: application/json' `
```

Response Response Example

200 - Example 1

```
` {
"status" : "object" ,
"subscription" : {
"app_id" : 2376 ,
"store_id" : 26520 ,
"store_url" : "https://example.zidtest.com/" ,
"plan_name" : "1استخدام" ,
"subscription_status" : "active" ,
"start_date" : "2025-02-04T15:55:07.000000Z" ,
"end_date" : null ,
"merchant_phone_no" : "+201063989603" ,
"merchant_email" : "m.example@zid.sa" ,
"is_usage_based" : 1 ,
"pending_charges" : 100 ,
"settled_charges" : 1 ,
"charges" : [
{
"id" : "9eaac8b0-3530-4bdb-b2fb-34b4efe22179" ,
"subscription_id" : 333 ,
"amount" : 300 ,
"amount_details" : {
"amount" : 34500 ,
"currency" : "SAR" ,
"formatted" : "ر.س‎ 345.00"
} ,
"status" : "pending" ,
"overdue_at" : null ,
"created_at" : "2025-04-13T16:58:06.000000Z"
}
]
} ,
"message" : {
"type" : "object" ,
"code" : null ,
"name" : null ,
"description" : "Store subscription details of the provided token"
}
} `
```

Modified at 2026-10-21 14:29:00

Previous

Update Usage-Based Charges

Next

Add-on Purchases
