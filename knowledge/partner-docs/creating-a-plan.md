---
# Synced from https://docs.zid.sa/creating-a-plan-2490912m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-creating-a-plan
title: "Creating a plan"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/creating-a-plan-2490912m0
tags: [from-docs-site, partner-docs]
language: en
---

> Creating a plan - Zid Docs
# Creating a plan

You create and edit plans in the Partner Dashboard, under your app's **Plans** section.

## Before you submit for review #

Check all of these before sending your app to Zid for review:

Your app has a free plan, **or** a paid plan with a free trial, so the review team can test it

Every plan has a name, description and at least one feature, in both Arabic and English

Your app has no more than 8 plans

All plans are the same type — either all recurring, or all usage-based

You have decided how your app will track subscriptions — webhook events, the Subscription Details endpoint, or both. See Subscription and app events

## Step 1: Choose the plan type #

Pick one of three types. The fields you fill in depend on which you choose.

**Free** — no payment. Use it so Zid can review and test your app.

**Recurring** — a fixed price per period. Use it for most apps.

**Usage-based** — a starting price plus charges based on consumption.

Remember: all of your app's plans must be the same type. A free plan can sit alongside recurring plans, but recurring and usage-based plans cannot be mixed.

## Step 2: Fill in the shared fields #

Every plan needs these, in **both Arabic and English**:

Field Rule

Plan name Up to 50 characters. The Arabic name must be written in Arabic, the English name in English. Letters, numbers, spaces and `. | - ( )` only.

Description Between 50 and 300 characters.

Features Between 1 and 5 lines. Each line up to 50 characters.

Each feature is a pair — write it in Arabic and English together.

## Step 3: Fill in the fields for your plan type #

### Free plan #

Nothing more to fill in. A free plan has no price, duration, trial, installation fee or offer. It renews automatically, so it does not expire.

### Recurring plan #

Field Rule

Price At least 1 SAR, up to 120,000 SAR

Duration Choose from the list: 1 to 11 months, or 1 year

Free trial Optional. Up to 90 days

Installation fee Optional. At least 1 SAR. See below

Offer Optional. See Offers below

### Usage-based plan #

Field Rule

Price At least 1 SAR. A **one-time** amount, charged when the merchant subscribes and never repeated

Duration Fixed at 30 days — you cannot change it. **Not a billing cycle** — the subscription has no end date

Usage type Calls, messages, orders, emails, or Other

Custom usage label Required only if you choose Other. Up to 50 characters, in both languages

Usage-based plans do not support free trials, installation fees or offers. A usage-based subscription has no end date and never renews — it continues until a charge goes unpaid, and the starting price is never charged a second time. See Usage-based plans .

## Installation fee (one-time fee) #

In the dashboard this field is described as "the additional charges required at the first time of your app installation" . It adds a one-off amount on top of the plan price, charged when a merchant first subscribes to your app.

**It is charged once per merchant, ever.**

Once a merchant has paid your app's installation fee, they will never be charged it again — not when they renew, not when they switch plans, and not when they resubscribe later.

Things to know:

Creating a new plan with a new installation fee does **not** let you charge an existing merchant again.

Deleting a plan and creating it again does **not** reset the fee.

Merchants who subscribed before you added the fee are never charged it.

If the fee is owed and has not been paid, the subscription does not activate.

Do not use the installation fee to sell packages or repeat purchases. It only works once per merchant.

## Offers #

Offers are available on **recurring plans only**. Choose one of two kinds:

**Buy X, get Y free** — the merchant subscribes for the plan period and gets extra free time. The free period must be a whole number of months, or exactly 1 year, and it cannot be longer than the plan's own duration.

**Discount** — a percentage off the plan price, up to 60%.

Offers cannot be added to free plans or usage-based plans.

## Step 4: Submit your changes #

Plan changes are sent to Zid for review before they go live. You can save your work as a draft first and submit when you're ready.

## All limits at a glance #

Limit

Plans per app 8

Plan name 50 characters

Description 50 to 300 characters

Features 1 to 5 lines, 50 characters each

Price 1 to 120,000 SAR

Duration (recurring) 1 to 11 months, or 1 year

Duration (usage-based) Fixed at 30 days

Free trial Up to 90 days

Installation fee At least 1 SAR, charged once per merchant

Discount offer Up to 60%

Currency SAR only

Modified at 2026-10-28 06:29:26

Previous

Plans and pricing

Next

Usage-based plans
