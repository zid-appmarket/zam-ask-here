---
# Synced from https://docs.zid.sa/usage-based-plans-2490913m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-usage-based-plans
title: "Usage-based plans"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/usage-based-plans-2490913m0
tags: [from-docs-site, partner-docs]
language: en
---

> Usage-based plans - Zid Docs
# Usage-based plans

A usage-based plan lets you charge a merchant for what they actually use, instead of a fixed price each month. Use it when the cost of running your app depends on consumption — messages sent, API calls made, orders processed, emails delivered.

## How it works #

1 .

You create a usage-based plan with a starting price and a usage type.

2 .

The merchant subscribes and pays the starting price. **This is a one-time payment** — it is charged when they subscribe and never again.

3 .

As the merchant uses your app, you add a charge through the API.

4 .

The merchant pays the charge from their Zid dashboard.

5 .

You repeat step 3 as usage continues.

A usage-based subscription has **no end date** and **never renews**. It stays active until a charge goes unpaid. There is no automatic renewal to switch on, and the starting price is not taken again — after the merchant subscribes, every amount you collect comes from the charges you add.

If a subscription does lapse because a charge defaulted and the merchant subscribes again, that is a new subscription and the starting price applies again.

## Before you start #

**Your app cannot mix plan types.** If your app already has recurring plans, you must remove them before adding usage-based plans. The reverse is also true.

**Usage-based plans do not support** free trials, installation fees, or offers.

**Usage-based plans cannot be combined with private plans.** If your app has a usage-based plan, you cannot create private plans for it.

## Creating the plan #

In the Partner Dashboard, under your app's **Plans** section, choose the usage-based plan type.

Field Rule

Price At least 1 SAR. A **one-time** amount, charged when the merchant subscribes and never repeated

Duration Fixed at 30 days — you cannot change it. **This is not a billing cycle.** It is the window used for the charge limits and overdue timings below; the subscription itself has no end date

Usage type Calls, messages, orders, emails, or Other

Custom usage label Required only if you choose Other. Up to 50 characters, in Arabic and English

The usage type tells the merchant what they are being billed for. Pick the one that matches your app. If none fit, choose Other and write your own label in both languages.

**Design your pricing around the charges, not the starting price.** The starting price is collected once. If you want a fixed monthly amount as well as metered usage, include it in the charge you post each month rather than expecting the starting price to recur.

## Adding a charge #

Call this endpoint when you want to bill the merchant for their usage.

**POST** `https://api.zid.sa/v1/managers/market/apps/plans/subscription-charge`

### Headers #

Header Value

`Authorization` `Bearer {your partner token}`

`X-Manager-Token` The merchant's token from OAuth

`Accept` `application/json`

`Content-Type` `application/json`

`Accept-Language` `ar` or `en`. Defaults to `en`

**Required scope:** `Subscription.read_write`

### Body #

Field Type Required Notes

`amount` number Yes In SAR. Minimum `0.01`. Decimals are allowed

`description` object Yes Must contain both `ar` and `en`

`description.ar` string Yes Up to 200 characters

`description.en` string Yes Up to 200 characters

```
` {
"amount" : 49.50 ,
"description" : {
"ar" : "استخدام 500 رسالة - أكتوبر" ,
"en" : "500 messages used - October"
}
} `
```

The description is shown to the merchant, so write something they will recognise on their invoice.

### Response #

```
` {
"status" : "object" ,
"charge" : {
"id" : "9eaac8b0-3530-4bdb-b2fb-34b4efe22179"
} ,
"message" : {
"type" : "object" ,
"code" : null ,
"name" : null ,
"description" : "Subscription charge was updated successfully"
}
} `
```

### Errors #

Status Meaning

401 Your credentials are missing, invalid or expired — **or** the merchant has no active usage-based subscription for your app

422 The amount or description failed validation

500 Server error

If you get a 401 and your token is valid, check that the merchant is actually subscribed to a usage-based plan. This endpoint only works for merchants on a usage-based plan.

## Limits you must design around #

**Two charges per merchant, per calendar month.**

This counts any unpaid charge plus any charge paid during the current month. Once you reach two, further calls are rejected until the next month begins. Plan your billing around one or two charges a month — this endpoint is not designed for charging on every transaction.

**Only one unpaid charge at a time.**

If the merchant already has an unpaid charge, calling the endpoint again does **not** create a second charge. It updates the existing one with your new amount and description.

**You can change an unpaid charge's amount once per calendar month.**

After that, further changes are rejected until the next month.

**SAR only.** There is no other currency.

## What happens when a merchant doesn't pay #

When What happens Event sent to your app

Charge created The merchant is notified and the charge is unpaid —

Merchant pays The charge is settled and the subscription stays active `usage_based.payment_success` and `subscription.renew`

Payment attempt fails The charge stays unpaid `usage_based.payment_failure`

30 days unpaid The charge becomes overdue `subscription.warning`

30 days after that The charge defaults and the subscription expires `subscription.expired`

Note that when a charge is paid, your app receives **two** events — `usage_based.payment_success` and `subscription.renew`. The amount paid appears in the `subscription.renew` payload, not in `usage_based.payment_success`. See Subscription events .

## Checking a merchant's charges #

Use the Subscription Details endpoint to see the current state of a merchant's subscription and charges.

**GET** `https://api.zid.sa/v1/market/app/subscription` — scope `Subscription.read`

Useful fields in the response:

Field Meaning

`is_usage_based` `1` if the merchant is on a usage-based plan

`pending_charges` Amount not yet settled

`settled_charges` Total amount settled so far

`charges` The individual charge records, with `id`, `amount`, `status` and `overdue_at`

Use this to confirm a charge was created or paid, rather than relying only on events.

## Things to keep in mind #

Charges are billed **after** usage, not prepaid. You cannot sell a merchant a pack of credits up front.

The merchant has to act. A charge is an amount they settle from their Zid dashboard, so allow time for them to pay it.

Keep your own record of usage. Zid stores the charge amount and description you send, not the underlying usage data.

Send one clear charge per billing period rather than many small ones. The two-per-month limit makes frequent charging impossible.

Modified at 2026-10-28 06:30:21

Previous

Creating a plan

Next

Private plans
