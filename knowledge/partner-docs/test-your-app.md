---
# Synced from https://docs.zid.sa/test-your-app
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-test-your-app
title: "Test your app before you submit"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/test-your-app
tags: [from-docs-site, partner-docs]
language: en
---

> Test your app before you submit - Zid Docs
# Test your app before you submit

Run these tests before you send your app to review. Work through them on a development store, with every setting pointing to production, using your app as a merchant would.

## Submit only when your app is ready #

A reviewer installs your app on a store and uses it as a merchant would, so the review reflects your app exactly as it is on the day you submit.

A broken link, a webhook that does not arrive, or a crash on an Arabic product name all have to be returned to you. You then resolve the issue and submit again, and the review begins again from the start.

We would much rather approve your app on its first submission. Working through the items below that apply to your app is the fastest way to get there.

## Start here: install your app on a development store #

We check this first, and your app needs at least **one installation**.

Our review is hands-on: a reviewer opens your app on a store and uses it as a merchant would, and the installation is what makes this possible. Without one we cannot begin, so we return the app for you to install first.

This is not a judgment about your app or your work. It means only that the review has not started, so we have no findings to share yet on your scopes, your listing, or anything else. Once your app is installed, we review it in full.

## How to use this page #

Not every section applies to every app.

**Parts 1 to 5 apply to all apps.**

**Part 6 is organised by app type.** Work through only the sections that match what your app does.

This page covers **whether your app works**. Your listing is reviewed separately: names, URLs, screenshots, scopes, plans, and bank details are all covered in Submitting your app for review (https://docs.zid.sa/submit-app-for-review). You need both pages.

Completing this page is not an approval in itself. It resolves the issues that return most apps.

## Part 1: Before you start testing #

Please put these in place before you begin. Without them, your results will not reflect what a merchant experiences.

**Every setting points to production.** This includes API keys, the OAuth server, redirect and callback URLs, webhook listeners, and any third-party service your app depends on. Development, staging, and tunnel addresses must all be replaced.

**No development hosts appear in any URL field.** Reviewers check for `ngrok`, `localhost`, `*.vercel.app`, `*.supabase.co`, `*.railway.app`, `*.herokuapp.com`, and any hostname beginning with `dev.`, `staging.`, or `test.`

**Your app is installed on a development store** that you can install and uninstall freely, as described above.

**You are testing a fresh installation**, rather than the account you built your app with. Data left over from development conceals the problems a new merchant will encounter.

## Part 2: Permissions #

**Your app should request as few scopes as possible.** Selecting every scope during development is common, so please review your selection carefully before you submit.

**Every scope corresponds to a feature.** If you cannot name the feature that requires `Product.write`, remove it.

**Read-only apps request read-only scopes.** If your app only displays data, no write scope should be selected.

**Your app works with only the scopes you requested.** Remove a scope, reinstall, and confirm your app no longer calls the endpoints that scope allowed.

**Your app explains permission errors.** When a request is refused because a scope is missing, the merchant sees a clear message rather than a blank screen or a spinner that does not resolve.

Each scope group has a read level and a write level, written as `Product.read` and `Product.write`. See Justifying your scopes (https://docs.zid.sa/justifying-your-scopes-2490953m0).

## Part 3: Activation, connection, and uninstall #

This section accounts for more returned apps than any other, so we recommend giving it the most attention. The full requirements are in Public Apps OAuth Requirements (https://docs.zid.sa/oauth-requirements).

**Activation**

**OAuth begins as soon as the merchant selects Activate.** No signup form, no login screen, and no marketing page may appear between Activate and the Zid consent screen.

**The merchant is never asked to enter credentials.** Your app must not request a token, API key, client secret, Store ID, or store URL. It identifies the store through OAuth.

**The authorization code is exchanged within the callback request.** The code is valid for 10 minutes and can be used once, so passing it to a background job will fail.

**A `state` value is created for every request**, stored with the session, and validated before the callback is accepted. Zid does not support PKCE, so `state` is your only protection against request forgery.

**A cancelled authorization is handled.** If the merchant declines, Zid does not call your callback at all and returns the merchant to their dashboard with an `error_code`. Treat an activation that begins without a callback as an expected outcome, and confirm that a second attempt does not create a duplicate connection.

**Connection**

**Tokens are stored securely and kept separate for each store.** Install your app on two stores and confirm that neither can access the other's data.

**The store remains connected throughout setup.** The merchant may sign up, sign in, or change settings during this time. The connection must not switch to another store or be lost, and the merchant must never need to restart activation.

**Accounts are never linked on a matching email address alone.** Authenticate the merchant into the partner-side account, then confirm the link to the store explicitly.

**Tokens and secrets remain private.** Keep access tokens, refresh tokens, client secrets, and authorization codes out of page content, URLs, browser storage, analytics, and logs.

**Token refresh works.** Allow an access token to expire, then confirm your app refreshes it without any action from the merchant.

**Opening, uninstalling, and reinstalling**

**Open app works.** When the merchant selects Open app , they arrive at a working page, signed in to the correct store.

**Uninstall is handled.** The merchant can remove your app without errors, and your app stops serving that store. Subscribe to `app.market.application.uninstall`, which is the only reliable way to learn that an uninstall has taken place.

**Reinstall is handled.** A merchant who has uninstalled your app can install it again and use it without any manual work on your side.

**Reinstalling after a scope change stores the new tokens.** When you add a scope, every merchant must deactivate and reactivate your app to approve it, which issues **new tokens for a store you already know**. If your app treats this as a duplicate installation and keeps the previous tokens, it will remain disconnected, and the merchant will see only that the approval did not succeed.

**No values are hardcoded.** Review your code for fixed values such as `store_id = 123`, `category_id = 14`, `store_url = xyz.zid.store`, or `currency = SAR`. Every value must come from the merchant's own data.

## Part 4: Subscription and billing #

**Paid apps only.** Without these events your app cannot know when a merchant's subscription changes. The full list, with the timing of each event, is in Subscription and app events (https://docs.zid.sa/subscription-and-app-events-2490915m0).

**`app.market.subscription.active`** grants the merchant access after payment.

**`app.market.subscription.renew`** continues access. This event arrives **after** the renewal, never before it.

**`app.market.subscription.upgrade`** adjusts the merchant's features to match the new plan, whether they move to a higher or a lower one.

**`app.market.subscription.expired` and `.suspended`** withdraw access. Confirm the merchant can no longer use paid features.

**`app.market.subscription.refunded`** is handled, so the merchant does not remain on a paid plan after a refund.

**The free trial ends correctly.** Confirm what the merchant sees on the day a trial converts to a paid plan, and on the day it ends without payment.

**Events are identified by `event_name`, not `status`.** When a merchant has no subscription, `status` falls back to the final part of the event name, so it cannot be relied on.

## Part 5: Webhooks and data #

This section applies to any app that receives webhooks.

**Your endpoint is publicly reachable over HTTPS**, presents a valid certificate, and responds promptly.

**No secret appears in the URL.** A token or secret in the `target_url` is not accepted. Send it in a header instead.

**No placeholder remains in the URL.** Replace values such as `YOUR_WEBHOOK_SECRET` with the real one.

**Repeated events are handled safely.** If Zid delivers the same event twice, your app must not create a second record, send a second message, or charge the merchant twice.

**Events arriving out of order are handled.** An update may reach you before the record it belongs to, and this must not corrupt your data.

**Empty fields do not cause errors.** Test with products and orders in which optional fields have no value.

**Rate limits are respected.** When you receive a `429` response, wait before retrying rather than sending the request again immediately. See Rate Limiting (https://docs.zid.sa/rate-limiting-644369m0).

**Large stores are supported.** Test against a store with enough products or orders to require more than one page of results.

## Part 6: By app type #

Work through the sections that match what your app does.

### 6.1 Products #

**Products load correctly.** If you retrieve the product list when a merchant activates your app, confirm that every detail is accurate: name, description, price, and images.

**Products with variants are handled correctly** wherever they appear in your app, including display, selection, and anything your app writes back.

**Arabic and English data are both supported.** Test with Arabic names, descriptions, and categories, and confirm they display and save correctly.

**Products with missing fields are handled.** Confirm your app behaves correctly when optional fields such as the description or images are empty.

**Your changes reach Zid.** If your app updates a price or a product detail, confirm the change appears correctly in the merchant's dashboard.

**Stock changes are accurate.** If your app adjusts stock levels, confirm the resulting quantity in Zid matches what your app intended, for both increases and decreases.

**Changes made in Zid reach your app.** If the merchant edits a product in their dashboard, confirm your app receives the update.

### 6.2 Orders #

**Orders load correctly.** Orders with any combination of shipping and payment status display correctly in your app.

**`order.create`** arrives when a merchant receives a new order.

**`order.status.update`** arrives for every status change: Preparing, Ready, In delivery, Shipped, and Cancelled.

**`order.payment_status.update`** arrives when payment changes between Paid and Unpaid.

**Place a real order for each product type** and confirm it completes:

Single product

Grouped product

Digital file

Dynamic bundle

### 6.3 Messaging and notification apps #

These apps convert webhooks into messages. Confirm both that the event arrives and that the message reaches the connected platform.

**`order.create`** sends a message.

**`order.status.update`** sends a message for each status: Preparing, Ready, In delivery, Shipped, and Cancelled.

**`order.payment_status.update`** sends a message for Paid and Unpaid.

**`abandoned_cart.created`** sends a message.

**`customer.create`** sends a message.

**Each event selects the correct template.**

**Variables resolve correctly.** Confirm that `{{customer_name}}`, `{{order_id}}`, and `{{total_amount}}` take their values from the Zid payload.

**Empty fields do not reach the customer.** A message must never be sent reading `Hello {{customer_name}}` or `Hello undefined`.

**Arabic messages display correctly** on the platform that receives them.

### 6.4 Marketing and coupon apps #

**Coupon details are accurate** in the merchant's dashboard after your app creates a coupon.

**The coupon is active** and applies correctly at checkout.

**Expiry dates and usage limits behave** as the merchant configured them.

### 6.5 Storefront JavaScript apps #

**Your storefront element displays correctly.**

**Its position holds across themes.** Test on more than one theme, including Vitrin and Legacy themes (https://docs.zid.sa/supporting-both-vitrin-and-legacy-themes-1596866m0).

**It survives a change of country or language.** Switch the customer's country and language, then confirm it still displays correctly, including right-to-left layout in Arabic.

**It does not affect the storefront.** Confirm there are no console errors, no blocked page rendering, and no noticeable slowdown.

### 6.6 Embedded apps #

**Your app opens inside the Zid dashboard** rather than in a new tab.

**Your app is responsive** at every width the dashboard provides.

**Your embedded setting matches your app.** If you requested the `embedded_apps_tokens_write` scope, your app must provide an embedded experience. A mismatch between the two is one of the most common reasons an app is returned.

## Final checklist #

Please confirm each of these before you submit.

**Your app is installed on a development store** — we check this first, and the review cannot begin without it ☐

Every setting points to production: keys, URLs, and webhooks ☐

Every scope corresponds to a feature your app provides today ☐

OAuth begins as soon as the merchant selects Activate ☐

Installing, uninstalling, and reinstalling all work, including after a scope change ☐

Tokens are kept separate for each store and are never exposed ☐

Subscription events are handled — paid apps only ☐

Webhooks arrive, and repeated events are handled safely ☐

Arabic data and Arabic screens are both supported ☐

No values are hardcoded ☐

Every section above that applies to your app passes ☐

Once all of this is true, review the listing requirements in Submitting your app for review (https://docs.zid.sa/submit-app-for-review).

## Submit your app for review #

When you have worked through this page and resolved everything you found, submit your app. The same steps apply if your app was returned to you previously.

1 .

Open your app and select the **Publish** tab.

2 .

Confirm your status reads **Draft** or **Rejected**.

3 .

Submit your app for review.

Your status changes to **Request to publish**, and your app enters the review queue.

**Please resolve every issue before you submit.** Each submission receives a complete review, so an app that is only partly corrected is usually returned for the same reasons. One thorough pass through this page is considerably faster than several rounds of review.

Modified at 2026-10-21 20:08:04

Previous

Justifying your scopes

Next

Submitting your app for review
