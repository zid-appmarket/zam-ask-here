---
# Synced from https://docs.zid.sa/private-plans-2490914m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-private-plans
title: "Private plans"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/private-plans-2490914m0
tags: [from-docs-site, partner-docs]
language: en
---

> Private plans - Zid Docs
# Private plans

A private plan is a custom plan you create for **one specific merchant**. Only that merchant can see it and subscribe to it. Use it when a merchant needs terms your public plans don't cover — a larger volume, a longer period, or a negotiated price.

**A private plan is not the same as a private app.**

A **private plan** is a custom plan on your public app, for one merchant. That's what this page covers.

A **private app** is an app that is not listed in Zid App Market and installs on a single store. Private apps are not sold through the market, so they cannot have plans at all — public or private.

## How it works #

1 .

A merchant opens your app in the Zid App Market and requests a private plan, with a note explaining what they need.

2 .

Your app receives the `app.market.private.plan.request` event.

3 .

You create a private plan for that merchant in the Partner Dashboard.

4 .

The merchant sees the plan and subscribes to it.

You can turn private plan requests on or off for each of your apps in the Partner Dashboard. If you turn them off, merchants will not be able to request one.

## Creating a private plan #

In the Partner Dashboard, open your app's **Plans** section and go to private plans. You will see any pending requests there.

Field Rule

Merchant The store the plan is for. One private plan per merchant, per app

Price Greater than 0

Duration At least 1 day

Description Optional. Arabic and English

Features **Required.** Arabic and English

## Rules to know #

**The price must be higher than your cheapest public plan.**

Zid compares the daily rate, not the total. Your private plan's price divided by its duration must be **greater** than the lowest price-per-day across your public plans. A private plan cannot undercut what you already offer publicly.

For example, if your cheapest public plan is 300 SAR for 30 days — 10 SAR per day — then a 90-day private plan must cost more than 900 SAR.

**One private plan per merchant, per app.**

If a merchant already has a private plan for your app, you cannot create another one for them. Edit the existing plan instead.

**You cannot create a private plan while a request is pending.**

If the merchant has an open request, respond to that request rather than creating a plan separately.

**You cannot edit a private plan once the merchant is subscribed to it.**

Edit it before the merchant subscribes, or wait until their subscription ends.

**Private plans are not available for usage-based apps.**

If your app has any usage-based plan, you cannot create private plans for it.

**A merchant part-way through an offer can only move to a more expensive plan.**

If the merchant is on a plan they bought with an offer, or has a paused plan waiting behind their current one, they can only move to a plan that is both **longer or equal in duration** and **higher in price** than the one they are on. A private plan is still a plan, so this applies to it too: a cheaper private plan is refused as a downgrade, even though you created it for that merchant.

This matters if you are using a private plan to settle a billing question. You cannot price one to collect only the difference between two plans — the merchant pays the private plan's full price, like any other plan change. See Changing a plan .

## Free private plans are not possible #

A private plan's price must be greater than 0, and it must beat your cheapest public plan's daily rate. If you need to give a merchant free access, use a free trial on a public plan instead.

Modified at 2026-10-28 06:30:49

Previous

Usage-based plans

Next

Subscription and app events
