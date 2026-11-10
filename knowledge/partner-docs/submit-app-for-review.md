---
# Synced from https://docs.zid.sa/submit-app-for-review
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-submit-app-for-review
title: "Submitting your app for review"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/submit-app-for-review
tags: [from-docs-site, partner-docs]
language: en
---

> Submitting your app for review - Zid Docs
# Submitting your app for review

Zid reviews every app before it goes live in Zid App Market. This page covers everything that has to be in place, what reviewers check, and the issues that most often lead to an app being returned.

**This page applies to OAuth apps published in Zid App Market.** Private apps are not listed in the market and do not go through review.

## Part 1: Your account #

These are set once and apply to every app you publish. **Your app cannot be submitted until they are complete.**

### 1. Partnership details #

Partner Dashboard → **Partnership** → **Onboarding**

Onboarding is a three-step wizard: **Authorized Member → Contact Info → Business Details**.

First choose your business type, because it determines what you need to provide.

**If you are a company**

Field Requirement

Company name (Arabic) Required

Company name (English) Required

Commercial Registration Number Required — Saudi CR numbers must be exactly 10 digits

CR Certificate Required — PDF, JPG or PNG, up to 5 MB

Is your company VAT-registered? Required for companies resident in Saudi Arabia

VAT Registration Number If VAT-registered — 15 digits, starting and ending with 3

VAT Certificate PDF, JPG or PNG, up to 5 MB

Country, City Required

Address Line 1, Building Number, District Required

Postal Code Required — 5 digits

Address line 2 Optional

Work field, Customer count Optional

**If you are an individual**

Field Requirement

ID document Required — PDF, JPG or PNG, up to 5 MB

Freelancer document Optional

Country, City Required

Address fields Optional

**Document verification is separate from review.** Your documents carry a verification state shown at the top of the Partnership page. Until finance verifies them, **payouts cannot be settled** — but an unverified state does not block you from submitting an app.

### 2. Contact people #

Partner Dashboard → **Partnership** → **Onboarding** → **Contact Info**

Field Requirement

Partnership Officer — Full Name (Arabic) Required

Partnership Officer — Full Name (English) Required

Partnership Officer — Email Address Required

Partnership Officer — Mobile Number Required — format `+966 5X XXX XXXX`

Add a Financial Officer Optional toggle — a separate person who receives financial correspondence

Please keep these current. They are how Zid reaches you about your review, and an out-of-date address is a common reason a review stalls without a reply.

### 3. Bank account #

Partner Dashboard → **Payments** → **Bank Account**

`/partner/{id}/bank-account`

Required before submission, even if your app is free — a free app can add paid plans later, and the account must exist first.

Field Requirement

Bank name Required

Account holder name Required

Country Required — detected from your IBAN if you leave it blank

IBAN Required if your country uses IBAN. Letters and digits only, validated

SWIFT / BIC code **Always required** — 8 or 11 characters, letters and digits only

Account number Shown instead of IBAN if your country does not use IBAN — 4 to 17 characters

Routing number Required for US banks

Tax document PDF, PNG or JPEG, up to 5 MB

**Your VAT answer and your tax document must agree.** You declare whether you are VAT-registered in Partnership → Business Details, while the certificate is uploaded on the Bank account page, where the field is labelled optional. Reviewers compare the two, and a mismatch is one of the most common finance queries we raise.

### 4. Sign the partnership agreement #

Partner Dashboard → **Partnership** → agreements

Each app needs a signed agreement before it can be submitted. You can preview the agreement before signing.

**An unsigned agreement prevents submission.** It is the most common reason a submission cannot proceed to review.

## Part 2: Your app listing #

Partner Dashboard → **Apps** → **Create application**.

### Step 1: Choose the app type #

**Public app** Published to Zid App Market. Merchants discover, install and rate it. Requires review before going live

**Private app** Offered to a single merchant store by invitation. Not reviewed, not listed

Choose **Public app**.

### Step 2: Name and categorise it #

Only four details are requested at this stage. Everything else is edited once your app exists.

Field Requirement

App name (Arabic) Required — 3 to 24 characters, must contain Arabic, unique across the market

App name (English) Required — 3 to 24 characters, must not contain Arabic, unique across the market

Category Required

Tags Optional

Categories are grouped into **Marketing & Growth**, **Sales & Conversion** and **Operations & Store Management**. Choose the one a merchant would browse to find your app.

### Step 3: The app editor #

Your app opens on a six-tab editor, and its status starts as **Draft**:

**General settings · App details · Webhooks · Plans · Publish · Activation**

#### General settings #

This tab holds your **API keys** (OAuth 2.0 endpoint, Client ID, Client secret) and the **Developer Bridge**, which lets you test your OAuth flow before going live.

Below that are **Scopes**. Each group offers up to three levels — **None**, **Read**, **Read and Write** — and groups with a single available level are selected automatically and cannot be changed.

Below the scope list is the justification field, labelled "Why does your app need these scopes?" — see Justifying your scopes (https://docs.zid.sa/justifying-your-scopes-2490953m0) for what reviewers expect in it:

Briefly explain (50–200 characters) why your app needs the selected scopes — reviewers use this to validate the request.

The same tab also holds **Embedded experience** (run your app inside the dashboard sidebar instead of a new tab) and **Storefront snippets** (HTML or JavaScript injected at well-known storefront events).

#### App details #

This tab holds everything merchants see in your listing.

**Basic info**

Field Requirement

App name (Arabic / English) As above

Developer name (Arabic) Required — Arabic letters and spaces only

Developer name (English) Required — Latin letters, spaces and hyphens only

App URL Required — must start with `https://`

Video URL Optional — **public YouTube link only**, other providers are not supported

Category, Tags Category required

**Application links**

Field Requirement

Application website Optional — your public marketing site, if different from the App URL

Redirection URL Required — where Zid sends merchants after install to start the OAuth flow

Callback URL Required — where Zid returns the OAuth code after the merchant authorizes your app

Maintainer email Required — reviewers and Zid support reach you here

**Support & Policies**

Field Requirement

Phone number Required if no support channel URL

Support channel URL Required if no phone number — WhatsApp, Telegram or a support portal are all accepted

FAQ URL Optional

Privacy policy URL **Required for review**

A WhatsApp or Telegram link is accepted as your **support channel**, but not as your **privacy policy**, which must be a published policy page.

**Descriptions**

Field Limit

Short description (Arabic / English) 100 characters each

Description (Arabic / English) 4,000 characters each

**App icon** — PNG or JPG, exactly square (1:1), maximum 250 × 250 pixels, up to 2 MB.

**Screenshots** — up to 10 each, PNG or JPG.

Screenshots (Arabic) **Required.** You cannot save your listing without at least one

Screenshots (English) Optional — shown to merchants viewing your listing in English

#### Testing before you submit #

At the bottom of App details is **Development store**. Install your app on one of your development stores and work through the merchant experience yourself before sending it to review.

**This installation is required, and we check it first.** Our review is hands-on: a reviewer opens your app on a store and uses it as a merchant would, and the installation is what makes this possible. Without one we cannot begin, so we return the app for you to install first.

This is not a judgment about your app or your work. It means only that the review has not started, so we have no findings to share yet. Once your app is installed, we review it in full.

Your app needs at least one installation. The full set of tests to run while you are there is on **Test your app before you submit**.

#### Plans #

Public plans and private plans sit on separate tabs. You can offer **up to eight public plans**.

Each plan is **Free**, **Recurring** or **Usage-based**, and takes a name and description in both languages (300 characters each) plus **1 to 5 features**, where every feature row has an Arabic and an English variant. If you charge by consumption, read Usage-based plans (https://docs.zid.sa/usage-based-plans-2490913m0) first — an app cannot mix usage-based and recurring plans. Custom pricing for a single merchant is covered in Private plans (https://docs.zid.sa/private-plans-2490914m0).

See Creating a plan (https://docs.zid.sa/creating-a-plan-2490912m0) for every field and limit, and Plans and pricing (https://docs.zid.sa/plans-and-pricing-2490911m0) for choosing between the models. Before review, your app needs either a free plan or a paid plan with a free trial so reviewers can test it.

#### Webhooks #

Events are organised into **webhook groups**. Each group sends every event you select to the same HTTPS endpoint with the same headers.

See Subscription and app events (https://docs.zid.sa/subscription-and-app-events-2490915m0) for the full event list, when each one fires, and both payload shapes.

### Step 4: Submit #

The **Publish** tab shows your current status and the submit button. Zid's description of what happens next:

When you're ready, send this app to our reviewers. They will check the listing details, scopes, and webhooks before publishing it to the App Market.

Your app moves through these states:

State Meaning

Draft Not yet submitted. Only you can see it

Request to publish Submitted, waiting for review

Published Live in the market

Rejected Not approved. Zid sends you the reason

Unpublished Was live, now withdrawn

You can return a published listing to draft at any time to make changes.

## Part 3: What reviewers check #

Reviewers work through the same set of checks on every app.

### 1. Names #

Your Arabic and English names must each read as a real product name in that language. A placeholder, an internal code name, or a name that is really a company abbreviation will be returned to you. This includes the **developer name**, which merchants see on your listing.

### 2. URLs #

Every URL must be a real, public, production address.

**No test or staging hosts.** A redirect or installation URL pointing to a sandbox, a proxy, or a `-test` hostname is not accepted.

**The privacy policy must be a real privacy policy page.** A link to a chat app, a social media profile, or a PDF in a file-sharing folder does not qualify.

Every URL must still resolve over HTTPS with a current TLS certificate at the time of review, not only when you first saved it.

### 3. Screenshots #

Arabic screenshots are required. Reviewers look for screenshots that show your app working inside the merchant's dashboard, rather than a marketing banner, your own website, or an empty state.

### 4. Category #

Your category must match what the app does, because it determines where merchants find you.

### 5. Descriptions #

Both descriptions must explain, in their own language, **what a merchant does with your app**. Two issues come up often:

A single vague sentence in each language that never explains how the app is used.

A description that promises features your app cannot deliver, because the scopes for them were never requested. Reviewers read your description against your scopes — if you describe pushing products and stock, you need the matching write scopes.

Smaller details are also noted, such as a description beginning with a stray character, or English text in a field intended for Arabic.

### 6. Scopes #

This is the most common reason an app is returned. Reviewers compare every scope against your features. Requesting write access for a read-only app, or scopes for features your app does not provide, is not accepted. Justifying your scopes (https://docs.zid.sa/justifying-your-scopes-2490953m0) covers what your description has to show.

A read-only analytics app that requests write scopes across the platform will be returned.

### 7. Plans #

**Your pricing must match what you charge everywhere else.**

If your app is sold on other platforms, or priced on your own website, your Zid plans must match that pricing. A different price on Zid is not accepted.

Also checked:

Every plan has a description in **both** languages. An empty English plan description will be returned.

No stray characters at the start of a plan name or description.

No leftover test plans in the list.

Creating a plan (https://docs.zid.sa/creating-a-plan-2490912m0) lists every field and limit.

### 8. Webhook events #

A paid app with no webhook subscriptions raises a query, because it has no way to know when a merchant's subscription changes. Reviewers look for the full subscription lifecycle rather than only the successful path. An app that handles activation, renewal and expiry but not suspension, warning, upgrade and refund will be asked to complete the set.

Free apps are not expected to subscribe to subscription events. The full list, with the timing of each event, is in Subscription and app events (https://docs.zid.sa/subscription-and-app-events-2490915m0).

### 9. Bank account and agreement #

Bank account present, with tax status matching the uploaded document.

Partnership agreement **signed**.

Commercial terms agreed with your partnership manager.

### 10. Your OAuth and activation flow #

Reviewers install your app on a test store and work through it exactly as a merchant would. How your app connects is reviewed as closely as what your listing says, and it is a frequent reason an app is returned — the full rules are in Public Apps OAuth Requirements (https://docs.zid.sa/oauth-requirements).

**Your app must start OAuth the moment the merchant clicks Activate.** Any paid Zid plan is settled before that point, so nothing should appear between Activate and the consent screen.

Three activation flows are not accepted:

Flow What to do instead

**Signup or login before OAuth** — the merchant reaches your registration form before they ever see Zid's consent screen Start OAuth immediately, then link the account after the callback

**Generic homepage or manual discovery** — the merchant lands on your marketing site or settings area and has to search for the Zid integration Open OAuth directly, or your approved dedicated setup journey

**Manual credentials or manual store identification** — asking the merchant to paste tokens, API keys, client secrets, a Store ID or a store URL Identify the store automatically through OAuth and exchange the code on your server

The reviewer also checks the following while working through your app:

**The connection is preserved through setup.** The verified store must not change or be lost during signup, sign-in, configuration or account linking, and the merchant must never have to restart activation to recover it.

**Accounts are never linked on a matching email address alone.** Authenticate the external account and confirm the store-to-account association explicitly.

**Nothing is exposed.** Access tokens, refresh tokens, client secrets and authorization codes must not appear in page content, URLs, client-side storage, analytics or logs.

**A ready state means the app is ready.** Do not display a service-ready state, or begin background syncing, while required setup is incomplete.

**A declined authorization is handled.** If the merchant cancels, your callback is not called at all, and Zid returns them to their dashboard with an `error_code`. Treat an activation that begins without a callback as an expected outcome, and confirm that a retry does not create a duplicate connection.

Two implementation details account for a number of quiet failures:

**The authorization code lasts 10 minutes and works once.** Exchange it within the callback request. Passing it to a background worker, or retrying after a failed exchange, will both fail.

**PKCE is not supported.** Zid's Authorization Code flow is for confidential clients. `code_challenge` and `code_verifier` are ignored, so your protection against request forgery is the `state` parameter — generated per request, bound to the session, and validated before you accept the callback.

One further detail affects apps after they go live. When you **add a scope**, each merchant re-approves by deactivating and reactivating your app. That issues a **new token pair for a store you already have**. If your app treats a known store as a duplicate installation and discards the new tokens, it will remain disconnected, and the merchant will see only that the re-approval did not succeed.

If your service genuinely needs setup before a store can be connected, there is an exception path, **Partner-managed setup**, but it requires Zid's prior written approval. Removing your Zid plans does not grant it.

## Errors the dashboard will show you #

Some issues are caught before your app reaches a reviewer. These are the three you are most likely to encounter:

**"The justification must be at least 50 characters."** — your scope description is too short. The counter under the field shows your length out of 200.

**"URL must start with https://."** — every URL field rejects plain HTTP inline, before saving.

**"Add at least one screenshot."** — saving App details is blocked until you have at least one Arabic screenshot.

Beyond these, each URL is checked live over TLS 1.2 or 1.3 with a five-second timeout when you save. A URL that is unreachable, or that serves an expired or outdated certificate, will not be accepted.

## Common reasons apps are returned #

**Before any of these: your app must be installed on a development store.** Without an installation we cannot begin the review, so none of the points below are assessed. It is the one requirement that must be met before the rest can be considered.

In rough order of how often they come up:

1 .

**Scopes that do not match the app.** Write access on a read-only app, or scopes for features that do not exist.

2 .

**An activation flow that does not start with OAuth** — a signup gate, a generic homepage, or a form asking the merchant to paste credentials.

3 .

**Unsigned partnership agreement.**

4 .

**Test or non-production URLs** in the redirect or installation fields.

5 .

**A privacy policy URL that does not lead to a policy page** — a chat link, a social profile, or a shared file.

6 .

**Descriptions** that do not explain how a merchant uses the app.

7 .

**Pricing that differs** from the partner's own website or another platform.

8 .

**Missing plan descriptions**, usually the English one.

9 .

**Incomplete webhook coverage** on a paid app.

10 .

**Stray characters** at the start of a name or description, or the wrong language in a language-specific field.

11 .

**Missing or mismatched bank and tax details.**

## Before you submit #

**Your app is installed on a development store** — we check this first, and the review cannot begin without it

Partnership details complete, with documents uploaded

Partnership officer details are up to date, and the email is one you actually monitor — it is how Zid reaches you about the review

Bank account saved, and your VAT answer matches the certificate you uploaded

Partnership agreement signed

Both app names read as real product names, and so does the developer name

Every URL is production, HTTPS, and live

Privacy policy is a real policy page

At least one support channel: phone number or support URL

Arabic screenshots show the app working inside the dashboard

Both descriptions explain how merchants use the app

Every scope is used by a feature that exists today

Plan prices match your website and any other platform you sell on

Every plan has an Arabic and English description

A free plan or a free trial exists so reviewers can test

Webhook events cover the whole subscription lifecycle

Activation starts OAuth immediately, with no signup gate, no homepage step, and no pasted credentials

A cancelled authorization, a retry and a reinstall all leave your app in a correct state

Reactivation after a scope change overwrites the stored tokens instead of discarding them

No test plans, test URLs or placeholder text anywhere

## Documentation you'll need #

**Before you build**

Start Here (https://docs.zid.sa/start-here) — the platform in overview

Create your First App (https://docs.zid.sa/create-first-app) — the walkthrough

**Connecting your app**

Public Apps OAuth Requirements (https://docs.zid.sa/oauth-requirements) — the activation and security rules reviewers apply

Authorization (https://docs.zid.sa/authorization) — the OAuth technical reference

OAuth Errors & Troubleshooting (https://docs.zid.sa/oauth-troubleshooting) — error codes, denial handling, the consent lifecycle

Zid Bridge Tool (https://docs.zid.sa/zid-bridge) — test your authorization flow before going live

**Pricing and billing**

Plans and pricing (https://docs.zid.sa/plans-and-pricing-2490911m0) — the models available and how to choose

Creating a plan (https://docs.zid.sa/creating-a-plan-2490912m0) — every field and limit

Usage-based plans (https://docs.zid.sa/usage-based-plans-2490913m0) — charging for consumption

Private plans (https://docs.zid.sa/private-plans-2490914m0) — custom plans for one merchant

Subscription Details (https://docs.zid.sa/app-subscription-details) — read a merchant's current subscription

Update Usage-Based Charges (https://docs.zid.sa/update-usage-based-charges-13896680e0) — post a usage charge

**Scopes and permissions**

Justifying your scopes (https://docs.zid.sa/justifying-your-scopes-2490953m0) — what reviewers expect in your description

**Reacting to merchants**

Subscription and app events (https://docs.zid.sa/subscription-and-app-events-2490915m0) — install, uninstall and the subscription lifecycle

Webhooks (https://docs.zid.sa/webhooks) — store data webhooks, which are a separate system

**Building the experience**

Embedded Apps (https://docs.zid.sa/embedded-apps-2168216m0) — running inside the merchant dashboard

StoreFront Events (https://docs.zid.sa/storefront-events-649611m0) — hooks available on the storefront

Zid MUI (https://docs.zid.sa/zid-mui-1973669m0) — Zid's component library

Zid SDKs (https://docs.zid.sa/zid-sdks-2008123m0) — official client libraries

**Working with the APIs**

Responses (https://docs.zid.sa/responses) — the response envelope and error shapes

Rate Limiting (https://docs.zid.sa/rate-limiting-644369m0) — the limits your app has to respect

Merchant APIs (https://docs.zid.sa/app-management-3013257f0) — everything your app can read and change

Modified at 2026-10-21 20:22:30

Previous

Test your app before you submit

Next

Plans & billing
