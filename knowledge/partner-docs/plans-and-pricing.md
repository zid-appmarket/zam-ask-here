---
# Synced from https://docs.zid.sa/plans-and-pricing-2490911m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-plans-and-pricing
title: "Plans and pricing"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/plans-and-pricing-2490911m0
tags: [from-docs-site, partner-docs]
language: en
---

> Plans and pricing - Zid Docs
# Plans and pricing

Every app on Zid App Market is sold through plans. A plan sets what a merchant pays, how long it lasts, and what they get.

**This page applies to OAuth apps published in Zid App Market.**

Private apps are not sold through the market and cannot have plans. Shipping apps are priced differently — see their own guide.

## Before you submit your app for review #

Zid's review team needs a way to test your app. Before you submit, your app must have **one** of these:

a free plan, or

a paid plan with a free trial.

Free trials work the same way during review and after your app goes live, so you don't need to change anything once your app is approved.

Apps are not published as permanently free. A free plan exists so your app can be reviewed and tested — not as a way to offer your app at no cost.

## Plan types #

Type What the merchant pays How long it lasts Use it for

**Free** Nothing Renews automatically, so it does not expire Letting Zid review and test your app

**Recurring** A fixed price each period 1 to 11 months, or 1 year Most apps

**Usage-based** A one-time starting price, then charges you add based on what they use Open-ended — no end date, and it never renews Apps where the cost depends on consumption, such as messages sent or orders processed

You can also create a **private plan** — a custom plan for one specific merchant. See Private plans .

## **App Add-ons** #

App add-ons let you sell additional features or services separately from your application's subscription plans, such as extra message credits or a one-time setup service.

Add-ons are available in two billing types:

Type Description

**One-time** A single prepaid purchase for additional features or services.

**Monthly** A recurring purchase that renews monthly until cancelled.

You can offer add-ons as:

**Public add-ons:** Available to merchants who have installed your app, after Zid's approval.

**Targeted add-ons:** Offered to a specific merchant using their Store ID, without requiring Zid's review.

Merchants purchase add-ons through Zid's payment flow without changing their existing application subscription.

### Tracking Add-on Purchases #

Use the following integrations to manage add-on fulfillment:

Subscription and App Events (https://docs.zid.sa/subscription-and-app-events-2490915m0): Receive notifications about purchases, renewals, payment failures, cancellations, expirations, and refunds.

Add-on Purchases API (https://docs.zid.sa/add-on-purchases-46829438e0): Retrieve a merchant's purchased add-ons, payment history, and current purchase status.

**Note:** Add-ons are separate from subscription plans and do not change the rules governing recurring and usage-based plan types.

## Two rules to know before you start #

**1. All of your app's plans must be the same type.**

An app can have recurring plans or usage-based plans — not both. To switch from one to the other, you must remove the existing plans first.

**2. A merchant holds one subscription per app.**

A merchant can be on only one of your plans at a time. They can move between plans, but they cannot hold two at once. Merchants can also purchase separate add-ons without creating another application subscription.

## Limits #

Limit

Plans per app 8

Currency SAR only

## Common questions #

### Can merchants buy a one-time package on top of their subscription? #

**Yes.** Merchants can purchase one-time add-ons, such as additional message credits or setup services, without changing their existing subscription plan.

You can create **public add-ons** for all merchants who have installed your app or **targeted add-ons** for specific merchants.

Monthly add-ons are also available for recurring additional services.

For technical integration, see Subscription and App Events (https://docs.zid.sa/subscription-and-app-events-2490915m0) and Add-on Purchases API (https://docs.zid.sa/add-on-purchases-46829438e0).

### Can I charge a setup fee when a merchant first installs my app? #

Yes. Add an installation fee to a recurring plan. It is charged once per merchant, the first time they subscribe, and never again. See Creating a plan .

### Can I offer a free period or a discount? #

Yes, on recurring plans. You can add a free trial of up to 90 days, a discount of up to 60%, or a "subscribe for X, get Y free" offer. See Creating a plan .

### Can I change a plan later? #

Yes. Changes you make to your own plans — price, features, duration — are reviewed by Zid before they take effect.

If you mean a merchant moving from one of your plans to another, that is a different thing and it has its own rules about what happens to the time they already paid for. See Changing a plan .

### Can I set prices in another currency? #

No. All plans are priced in SAR.

Modified at 2026-11-10 14:19:13

Previous

Plans & billing

Next

Creating a plan
