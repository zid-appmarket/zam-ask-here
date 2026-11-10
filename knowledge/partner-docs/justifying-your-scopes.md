---
# Synced from https://docs.zid.sa/justifying-your-scopes-2490953m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-justifying-your-scopes
title: "Justifying your scopes"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/justifying-your-scopes-2490953m0
tags: [from-docs-site, partner-docs]
language: en
---

> Justifying your scopes - Zid Docs
# Justifying your scopes

A scope is a permission your app asks a merchant to approve. When you submit your app, Zid reviews every scope you selected against what your app actually does.

**Every scope you request must be used by a feature in your app.**

If you select a scope your app does not use — no feature needs it, no endpoint calls it — your app will be **rejected**.

## Where you write your reason #

In the Partner Dashboard, in your app's **Scopes** section, there is a description field below the scope list. Write your reason there before you submit.

How many One description covering your whole selection

Length Between 50 and 200 characters

Required Yes — you cannot submit without it

It is short on purpose. Name the features, not the scopes.

## What a good reason looks like #

A reviewer is checking one thing: does each scope you selected connect to something your app actually does?

**Good**

Syncs orders and customers to the merchant's CRM, and creates discount coupons for abandoned-cart recovery emails.

Three scopes are implied and each is tied to a real feature.

**Too vague — expect questions or rejection**

Our app needs these permissions to work properly and give merchants the best experience.

It names no feature, so a reviewer cannot match it to anything.

**A common mistake**

Full access so we can add more features later.

Request scopes when you build the feature, not before. You can add a scope later — see Adding a scope after launch below.

## Scopes that always need a clear reason #

All scopes are reviewed, but these get the closest look because of what they expose. If you request one, make sure your description names the feature that uses it.

### Customer and merchant personal data #

Covered by Saudi Arabia's Personal Data Protection Law. You are responsible for how you store and use anything you read.

Scope group Why it is sensitive Your reason should show

Customers Names, phone numbers, emails, addresses Which feature needs customer records, and what you do with them

Orders Customer details plus purchase history Why order data must leave the store

Abandoned Carts Contact details of people who did not buy The exact recovery feature, and how merchants control it

Account, Account Identity The merchant's own account and identity details Why your app needs the merchant's identity, not just their store

Customer Wallet Customer balances and transactions The wallet feature you provide

Customer Referrals Customer relationships and referral data The referral feature you provide

### Money and pricing #

Scope group Why it is sensitive Your reason should show

Coupons Creates discounts that cost the merchant money What creates coupons, and what limits it

Bundle Offers Changes pricing shown to shoppers The offer feature you provide

Loyalty Issues and spends loyalty value The loyalty feature you provide

Order Create Creates real orders on the store Where the orders come from

Payments Reads which payment methods are enabled Why your app needs to know

### Code and content on the storefront #

Scope group Why it is sensitive Your reason should show

Extra Addons Adds JavaScript that runs on the merchant's storefront What the script does, and what it sends anywhere else

Catalog Changes what shoppers see in the store Which part of the storefront your app changes

### Store configuration #

Scope group Why it is sensitive Your reason should show

Store Core Details, Store Business Details Store and business settings Which settings your app reads or changes, and why

Store Domain The store's domain Why your app needs domain access

Languages & Currencies How prices and content are shown The feature that depends on it

### Data delivery #

Scope group Why it is sensitive Your reason should show

Webhooks Subscribes your app to a stream of store data Which events you subscribe to and why

## Read or read & write #

Each group has an access level. Ask for **read** when your app only needs to see the data. Requesting **read & write** when your app never changes anything is one of the most common reasons a scope gets questioned.

## Adding a scope after launch #

You can change your scopes later, and Zid reviews the change the same way. Merchants who already installed your app must approve the new permission before it works — until they do, calls needing it fail with **403**, and your app should prompt them to reauthorize.

This is why requesting scopes early "just in case" does not help: it costs you installs now and saves you nothing later.

## Before you submit #

Every scope you selected is used by a feature that exists today

You removed any scope left over from an earlier version of your app

You chose read rather than read & write wherever your app only reads

Your description names the features, not the scopes

Your description is between 50 and 200 characters

Modified at 2026-10-21 15:16:30

Previous

Create your First App

Next

Test your app before you submit
