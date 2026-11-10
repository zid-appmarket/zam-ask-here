---
# Synced from https://docs.zid.sa/subscription-and-app-events-2490915m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-subscription-and-app-events
title: "Subscription and app events"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/subscription-and-app-events-2490915m0
tags: [from-docs-site, partner-docs]
language: en
---

> Subscription and app events - Zid Docs
# Subscription and app events

Zid sends your app an event whenever something changes about a merchant's installation or subscription — authorization, installation, activation, renewal, expiry, uninstallation. Use these to keep your own records in sync: activating features, blocking access, or updating a merchant's status on your side.

**This page applies to OAuth apps published in Zid App Market.**

Shipping apps receive a different set of events — installation, order and product events, but no subscription events. Private apps are not sold through the market and have no subscriptions.

## Two ways to track a subscription #

There are two ways to know what a merchant's subscription looks like, and most apps need both.

**Events (push).** Zid sends a request to your endpoint the moment something changes. You subscribe once per app, and it covers every merchant who installs you.

**The Subscription Details endpoint (pull).** You call `GET /v1/market/app/subscription` with a merchant's token and get their current subscription back. You decide when to ask. Full details are in Reference: the Subscription Details endpoint below.

Events Subscription Details endpoint

Tells you That something changed , as it happens What is true right now

Setup Subscribe to each event in the Partner Dashboard Request the `Subscription.read` scope

Covers All your merchants, through one endpoint One merchant per call

Charge details Not included in the usage-based payloads Full charge records — id, amount, status, overdue date, and pending and settled totals

Depends on Your endpoint being reachable when Zid calls You remembering to call it

After a merchant uninstalls You still receive the `uninstall` event **Stops working** — see below

### Why you need events, not just the endpoint #

**You cannot detect an uninstall by polling.** When a merchant uninstalls your app, Zid deletes their `X-Manager-Token` and revokes your OAuth access and refresh tokens for that store. Your next call fails — and a failed call looks the same as a network problem or an expired token. The `app.market.application.uninstall` event is the only reliable way to learn that it happened, and it is the signal that tells you to stop serving that merchant.

**Polling does not scale.** The endpoint returns one merchant at a time. With a few hundred merchants, checking everyone regularly means a few hundred requests each time, against your rate limit.

**Polling misses the moment.** The endpoint tells you the state today, not that it changed overnight. If you need to act when a subscription activates or expires — unlocking features, sending a welcome message, cutting off access — you would have to poll frequently and compare against your own copy to spot the change.

### Why you need the endpoint, not just events #

**It is the source of truth.** A delivery can fail if your endpoint is down. Before you grant or remove access, confirm the current state with the endpoint rather than trusting your last received event.

**Usage-based charge details only live there.** The usage-based payment events carry no charge id and no paid amount, so the endpoint is where you read the amount, status and overdue date of each charge.

### A good pattern #

Subscribe to the events you care about, and treat each one as a prompt to call the endpoint and refresh your own record. At minimum, subscribe to `uninstall` and `expired` — those are how you learn to stop serving a merchant.

## Subscribing to events #

Events are **not** sent automatically. You subscribe to each one in the Partner Dashboard.

1 .

Go to the Webhooks (https://partner.zid.sa/create-application-steps/webhook-management) section when creating or editing your app.

2 .

Provide the endpoint where notifications should be sent.

3 .

Choose one or more events from the list.

4 .

Add any headers you need for authentication.

5 .

Save and submit. You can come back later to edit or add more events.

If you don't subscribe to an event, your app receives nothing when it happens — there is no error and no retry. Subscribing to one event does not subscribe you to the rest.

## Testing with a development store #

1 .

Use one of your development stores to simulate real events.

2 .

Perform the action in the store that triggers the event you subscribed to.

3 .

Check your app's webhook logs in the Partner Dashboard for successful deliveries or errors.

## Event reference #

### Installation and app events #

Event When it fires

`app.market.application.authorized` The merchant grants your app its permissions, before installing

`app.market.application.install` The merchant installs your app

`app.market.application.uninstall` The merchant removes your app

`app.market.application.rated` The merchant leaves a rating or review

`app.market.private.plan.request` The merchant requests a private plan

### Subscription events #

Event When it fires

`app.market.subscription.active` A subscription becomes active after payment

`app.market.subscription.warning` See the timing table below

`app.market.subscription.suspended` 1 day after a recurring subscription ends

`app.market.subscription.expired` See the timing table below

`app.market.subscription.renew` **After** a renewal or extension completes. Also fires on free-plan renewal, when a paused subscription resumes, and when a usage-based charge is paid. A resume carries the **older, cheaper** plan — see Changing a plan

`app.market.subscription.upgrade` The merchant moves to a different plan

`app.market.subscription.refunded` A payment is refunded to the merchant

`app.market.subscription.usage_based.payment_success` A usage-based charge is paid

`app.market.subscription.usage_based.payment_failure` A usage-based charge payment fails

**`renew` does not warn you before a renewal.** It always fires after the fact. No event is sent before a subscription renews or expires — use `warning` for advance notice.

### Timings depend on the plan type #

`warning` and `expired` are used for both recurring and usage-based plans, but they mean different things and arrive at different times.

Event Recurring plans Usage-based plans

`warning` 3 days **before** the subscription ends 30 days after a charge is left unpaid

`suspended` 1 day **after** the subscription ends Not used

`expired` 5 days **after** the subscription ends 30 days after the charge became overdue

Check `plan_type` in the payload if you need to tell them apart.

### Add-on Events #

App add-on webhook events notify your application when a merchant purchases, renews, cancels, or receives a refund for an add-on, or when a monthly add-on expires or its renewal payment fails.

Subscribe to these events through your application's **Webhooks** section in the Partner Dashboard. Each event is delivered only to the application that sold the add-on. Subscriptions also cover stores that have already installed your application.

Event Name When It Fires

`app.market.addon.purchased` A merchant purchases a one-time add-on or pays for the first month of a monthly add-on. Each new purchase triggers a separate event.

`app.market.addon.renewed` A monthly add-on is successfully renewed through an automatic payment or a merchant-initiated payment.

`app.market.addon.payment_failed` An automatic monthly renewal payment fails. The add-on remains active during the 5-day grace period while payment is retried.

`app.market.addon.cancelled` A monthly add-on is cancelled by the merchant, the app is uninstalled, or the merchant's app subscription ends.

`app.market.addon.expired` A cancelled monthly add-on reaches the end of its paid period, or an unpaid add-on passes the 5-day grace period.

`app.market.addon.refunded` Zid refunds an add-on payment.

**Note:** Add-on events use a separate purchase-based payload containing the add-on, purchase, billing period, and payment details. They do not use the standard application subscription event payload.

### Add-on Event Payload #

All six add-on webhook events use the same purchase-based payload structure. Each event returns the add-on purchase's updated state and, where applicable, the associated payment.

#### Payload Fields #

Field Type Description

`event_name` string The add-on webhook event name.

`addon_purchase_id` UUID Unique purchase identifier. Remains the same across monthly renewals.

`addon_id` UUID Identifier of the purchased add-on.

`app_id` integer Application ID.

`store_id` integer Purchasing store's ID.

`store_uuid` UUID Purchasing store's UUID.

`name` object Localized add-on name (`ar`, `en`).

`type` string `one_time` or `monthly`.

`is_targeted` boolean Whether the add-on targets a specific merchant.

`unit` object or null Localized unit information, if configured.

`quantity` integer or null Purchased quantity, if configured.

`status` string `active`, `cancelled`, `expired`, or `refunded`.

`period_start` ISO 8601 or null Start of the monthly billing period.

`period_end` ISO 8601 or null End of the monthly billing period.

`cancelled_at` ISO 8601 or null Cancellation timestamp.

`expired_at` ISO 8601 or null Expiration timestamp.

`refunded_at` ISO 8601 or null Refund timestamp.

`created_at` ISO 8601 Purchase creation timestamp.

`payment` object or null Associated payment details, when applicable.

`next_attempt_at` ISO 8601 or null Next retry timestamp for failed renewal payments.

#### Payment Object #

When a payment is included, the `payment` object contains:

Field Type Description

`purchase_id` UUID Zid payment/invoice identifier.

`kind` string `initial` or `renewal`.

`amount_paid` string Amount paid, including VAT.

`currency` string Currency code, such as `SAR`.

`period_start` ISO 8601 or null Billing period start for monthly payments.

`period_end` ISO 8601 or null Billing period end for monthly payments.

`paid_at` ISO 8601 Payment timestamp.

`refunded_at` ISO 8601 or null Payment refund timestamp.

**Note:** The `payment` object is null for `cancelled`, `expired`, and `payment_failed` events.

### Example: app.market.addon.purchased (monthly add-on) #

```
``
```

### Webhook Delivery and Retries #

Add-on events use the existing App Market webhook delivery mechanism.

**Method:** POST

**Destination:** The target URL configured in your application's Webhooks settings.

**Body:** JSON containing the add-on event payload directly, without an additional wrapper.

**Headers:** Any custom headers configured for the webhook subscription.

**Retry behavior**

If delivery fails due to a connection error, HTTP 5xx, or HTTP 429, Zid retries after 1, 5, 15, and 60 minutes, for up to five delivery attempts including the initial attempt.

Other HTTP 4xx responses are not retried.

**Important:** Events may arrive more than once or out of order. Design your webhook handler to safely process duplicate deliveries.

### Handling Add-on Events #

Use the event name and purchase status to determine how to update the merchant's add-on access.

Event Recommended Action

`purchased` Grant access to the purchased add-on.

`renewed` Extend access to the updated `period_end`.

`payment_failed` Keep access during the 5-day grace period while payment is retried.

`cancelled` Stop future renewals and retain access until the paid `period_end`.

`expired` Remove add-on access.

`refunded` Reconcile access based on the refunded billing period.

#### Monthly Billing Considerations #

Monthly subscriptions renew according to their original purchase date.

Merchants are notified by Zid three days before renewal and when a renewal payment fails.

Failed payments enter a five-day grace period after `period_end`.

Cancelling a monthly add-on stops future charges, but existing paid access continues until the relevant period ends.

When the application's subscription is suspended, automatic add-on card renewals are paused. They resume when the subscription is renewed. No separate pause event is sent.

#### Handling Refunds #

Refund behavior depends on the refunded payment:

Refunded Payment Required Action

One-time add-on Revoke the purchased entitlement.

Current monthly period Remove access immediately.

Previously completed period Keep the current purchase access unchanged.

Future prepaid period Adjust access to the updated `period_end`.

### Preventing Duplicate Processing #

Use `addon_purchase_id` to identify an add-on purchase and `payment.purchase_id` to identify individual payments.

For reliable processing:

1 .

Store the latest purchase status and billing period.

2 .

Check whether a payment or event has already been processed.

3 .

Handle events that arrive out of order.

4 .

Use the Add-on Purchases API to reconcile the merchant's latest purchase state if an event is missed.

The Add-on Purchases API is documented separately and returns the complete purchase history for the authenticated store and application.

## Payload: the 12 standard events #

All five installation and app events, plus `active`, `warning`, `suspended`, `expired`, `renew`, `upgrade` and `refunded`, share one payload shape.

```
` {
"app_id" : 1292 ,
"store_id" : 507530 ,
"store_uuid" : "d78468cd-4b44-4fee-a00d-76561f35787c" ,
"store_url" : "https://wyatt.com.sa/" ,
"plan_name" : "النمو" ,
"plan_id" : 904 ,
"plan_type" : "Paid" ,
"status" : "active" ,
"start_date" : "2025-02-21T08:05:29.000000Z" ,
"end_date" : "2025-03-22T08:05:29.000000Z" ,
"amount_paid" : 79.01 ,
"old_plan_name" : null ,
"merchant_email" : "info@ehmp.com.sa" ,
"merchant_phone_no" : "966554349999" ,
"event_name" : "app.market.subscription.active" ,
"payment_date" : "2025-02-21T08:05:29.000000Z"
} `
```

Field Notes

`app_id` Your app's ID

`store_id` Internal numeric store ID

`store_uuid` **Use this to identify the store**, not `store_id`

`store_url` The merchant's storefront URL

`plan_name` The plan the merchant is on. `null` if they have no subscription

`plan_id` The plan's ID

`plan_type` One of `Paid`, `Free`, `Free Trial`, `Usage Based`, `Free (Without Plan)`. See Identifying free trials

`status` The subscription's status. **Not a reliable way to tell events apart — use `event_name`.** See below

`start_date` When the subscription started

`end_date` When it ends. **Always `null` for usage-based plans**, which have no end date

`amount_paid` Amount paid, **including VAT**. `0` on many events — see below

`old_plan_name` The previous plan's name. Only set on `active`, `renew` and `upgrade`; `null` otherwise

`merchant_email` The merchant's email

`merchant_phone_no` The merchant's phone number

`event_name` The event. **Use this to identify what happened**

`payment_date` For a usage-based charge, when the charge was paid. Otherwise the subscription start date

### What differs between events #

The shape is the same, but not every event carries every value. Two differences catch people out:

Events `amount_paid` `status`

`active`, `renew`, `upgrade`, `refunded` The actual amount paid, including VAT The subscription's status

`warning`, `suspended`, `expired` Always `0` `warning`, `suspend`, `expire`

`authorized`, `install`, `uninstall`, `rated`, `private.plan.request` Always `0` The merchant's **current** subscription status, not the event name

So do **not** read `amount_paid` from an `install` or `authorized` event — it is always zero. Read it from `active`, `renew` or `upgrade`.

### About the `status` field #

`status` reports the subscription's status at the moment the event was built. Its possible values are:

`inactive`, `active`, `warning`, `suspend`, `frozen`, `expire`, `renew`, `upgrade`, `cancel`, `refund`

Note that several are shortened — `suspend` not "suspended", `expire` not "expired", `cancel` not "cancelled", `refund` not "refunded".

`frozen` means **paused, not cancelled**. It happens when a merchant moves to a plan that has an offer: their previous plan is held, with its remaining days intact, and comes back automatically when the new one ends. The merchant has no access on a frozen plan while it is paused, but they will get it back. See Changing a plan .

When the merchant has no subscription at all, `status` falls back to the last part of the event name (for example `authorized` for `app.market.application.authorized`). Because of this, `status` is not a dependable event discriminator. **Always branch on `event_name`.**

## Identifying free trials #

To tell whether a merchant is on a free trial, check `plan_type`:

```
` {
"app_id" : 6528 ,
"store_id" : 3104452 ,
"store_uuid" : "b2052c72-ddaa-411f-a428-748dcd885a6e" ,
"store_url" : "https://xle6e8.zid.store/" ,
"plan_name" : "Test Plan With Trial" ,
"plan_id" : 3329 ,
"plan_type" : "Free Trial" ,
"status" : "active" ,
"start_date" : "2026-06-14T08:05:40.000000Z" ,
"end_date" : "2026-07-04T08:05:40.000000Z" ,
"amount_paid" : 0 ,
"old_plan_name" : null ,
"merchant_email" : "bv3e7xxnx5@zam-partner.email" ,
"merchant_phone_no" : "+201101050117" ,
"event_name" : "app.market.subscription.active" ,
"payment_date" : "2026-06-14T08:05:40.000000Z"
} `
```

`plan_type` is `"Free Trial"` here, so this subscription includes a trial.

**`plan_type` tells you the subscription has a trial, not that the trial is still running .**

A subscription keeps the `"Free Trial"` value for as long as that subscription record exists, including after the trial converts to paid. The payload does not include the trial end date.

The Subscription Details endpoint does not help here either — it returns no `plan_type` and no trial dates. To know whether a trial is still running, work it out yourself: you set the trial length on the plan, so add it to `start_date`.

## Payload: the two usage-based payment events #

`usage_based.payment_success` and `usage_based.payment_failure` use a **different shape**. None of the fields above apply.

```
` {
"action" : "usage_based_subscription_payment_success" ,
"envelope" : {
"store_id" : 12345 ,
"app" : {
"app_id" : 67 ,
"app_name" : "My App"
} ,
"subscription" : {
"plan" : "Professional" ,
"plan_price" : 99.00
}
}
} `
```

The failure event is identical except for `action`:

```
` {
"action" : "usage_based_subscription_payment_failure" ,
"envelope" : {
"store_id" : 12345 ,
"app" : {
"app_id" : 67 ,
"app_name" : "My App"
} ,
"subscription" : {
"plan" : "Professional" ,
"plan_price" : 99.00
}
}
} `
```

Field Type Description

`action` string Either `usage_based_subscription_payment_success` or `usage_based_subscription_payment_failure`

`envelope.store_id` integer The store where the charge was attempted

`envelope.app.app_id` integer Your app's ID

`envelope.app.app_name` string Your app's name

`envelope.subscription.plan` string The plan's name

`envelope.subscription.plan_price` number The plan's price

Two limitations to design around:

**There is no charge ID and no paid amount.** `plan_price` is the plan's own price, not the amount the merchant just paid.

**There is no `store_uuid`** — only the numeric `store_id`.

Both events are delivered asynchronously, after the payment attempt resolves.

## Handling a paid usage-based charge #

When a merchant pays a usage-based charge, your app receives **two** events:

1 .

`app.market.subscription.usage_based.payment_success` — tells you a payment succeeded

2 .

`app.market.subscription.renew` — carries the amount in `amount_paid` and the date in `payment_date`

If you need the amount, read it from the `renew` event, or call the Subscription Details endpoint.

When a payment **fails**, only `usage_based.payment_failure` is sent, and it does not tell you which charge failed or for how much. Call Subscription Details to find out.

## Reference: the Subscription Details endpoint #

The companion to these events. Use it to confirm a merchant's current subscription, and to read usage-based charge details that the events don't carry.

**GET** `https://api.zid.sa/v1/market/app/subscription`

**Required scope:** `Subscription.read`

### Headers #

Header Value

`Authorization` `Bearer {your partner token}`

`X-Manager-Token` The merchant's token from OAuth

`Accept` `application/json`

`Accept-Language` `ar` or `en`. Defaults to `en`. Controls the language of `plan_name`

### Parameters #

None. Your app is identified from your token, and the merchant from their `X-Manager-Token`. You do not send an app id.

### Response #

This example is a merchant on a usage-based plan:

```
` {
"status" : "object" ,
"subscription" : {
"app_id" : 2376 ,
"store_id" : 26520 ,
"store_url" : "https://example.zid.store/" ,
"plan_name" : "Pay as you go" ,
"subscription_status" : "active" ,
"start_date" : "2025-02-04T15:55:07.000000Z" ,
"end_date" : null ,
"merchant_phone_no" : "+9665XXXXXXX" ,
"merchant_email" : "merchant@example.com" ,
"is_usage_based" : 1 ,
"pending_charges" : 345.00 ,
"settled_charges" : 1200.00 ,
"charges" : [
{
"id" : "9eaac8b0-3530-4bdb-b2fb-34b4efe22179" ,
"subscription_id" : 333 ,
"amount" : 345.00 ,
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

Field Notes

`app_id` Your app's ID

`store_id` The merchant's store ID

`store_url` The merchant's storefront URL

`plan_name` The plan's name, in the language from `Accept-Language`

`subscription_status` One of `inactive`, `active`, `warning`, `suspend`, `frozen`, `expire`, `renew`, `upgrade`, `cancel`, `refund`

`start_date` When the subscription started

`end_date` When it ends. **Always `null` for usage-based plans**

`merchant_phone_no` The merchant's phone number

`merchant_email` The merchant's email

`is_usage_based` `1` for a usage-based plan, `0` otherwise

### Usage-based plans only #

These three fields appear **only when `is_usage_based` is `1`**. On a recurring or free plan they are not in the response at all.

Field Notes

`pending_charges` The unpaid charge's amount, in SAR. `0.0` if there is none

`settled_charges` Total settled so far, in SAR

`charges` The charge records, newest first

Each entry in `charges`:

Field Notes

`id` The charge's ID. This is the id the events do not give you

`subscription_id` The subscription the charge belongs to

`amount` The amount **in SAR** — for example `345.00`

`amount_details.amount` The same amount **in halalas** — for example `34500`

`amount_details.currency` Currency code

`amount_details.formatted` The amount formatted for display

`status` One of `pending`, `paid`, `overdue`, `defaulted`

`overdue_at` When the charge became overdue, or `null`

`created_at` When you created the charge

**Two fields named `amount`, two different units.** `amount` is in SAR; `amount_details.amount` is in halalas. Don't mix them up.

`amount_details` is empty when the amount is zero.

### Things to know #

**It returns the merchant's most recent subscription, which may not be active.** Check `subscription_status` before treating it as current.

**`subscription` comes back empty if the merchant has not activated a plan.** You get `"subscription": []` — an empty value, not an object with empty fields. Installing your app is not enough on its own: a merchant activates a free plan, starts a trial, or pays for a plan, and only then does a subscription exist. An app with no plans at all will always return empty here.

**It returns less than the events do.** This response has no `plan_id`, no `plan_type` and no `store_uuid`. If you key merchants on `store_uuid` from events, you cannot match that against this response — use `store_id` as well, or store both.

**It stops working once the merchant uninstalls.** Their token is revoked, so this is not a way to detect an uninstall — see Two ways to track a subscription .

### Errors #

Status Meaning

401 Credentials missing, invalid or expired

500 Server error

For the full specification, see Subscription Details (https://docs.zid.sa/app-subscription-details).

## Recommended practice #

**Branch on `event_name`, not `status`.** `status` is ambiguous across events and uses shortened values.

**Treat events as a signal, not your source of truth.** Confirm the current state with the Subscription Details endpoint before granting or removing access.

**Handle repeats.** The same event can arrive more than once. Make your handler safe to run twice with the same payload.

**Respond quickly.** Return a success response first, then do your processing.

**Subscribe to `uninstall` and `expired`.** These are how you learn to stop serving a merchant. Without them your app keeps working for merchants who no longer have access.

## Checking deliveries #

Zid records every delivery attempt for your app's events. Review them in the Partner Dashboard under your app's webhook logs, where you can also send a test delivery.

## App events are not store webhooks #

These are two separate systems. Don't mix them up:

App events (this page) Store data webhooks

What they tell you Your app was installed, a subscription changed A merchant's order, product or customer changed

Event names `app.market.*` `order.*`, `product.*`, `customer.*`, `category.*`

How you subscribe Once per app, in the Partner Dashboard Per store, with the Create Webhook API

Scope needed None — it's dashboard configuration `third_webhook_write`

See Webhooks for store data webhooks.

Modified at 2026-11-10 13:47:45

Previous

Private plans

Next

Changing a plan
