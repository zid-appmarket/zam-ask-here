---
# Synced from https://docs.zid.sa/oauth-troubleshooting
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-oauth-troubleshooting
title: "OAuth Errors & Troubleshooting"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/oauth-troubleshooting
tags: [from-docs-site, partner-docs]
language: en
---

> OAuth Errors & Troubleshooting - Zid Docs
# OAuth Errors & Troubleshooting

Every way Zid can refuse an authorization request or an authenticated API call, what each

one actually means, and what to do about it.

Authorization fails in three different places, and each returns a **different format**.

Identify where you are before reading further:

# Where it failed What you see Jump to

1 **The authorize redirect** — the merchant clicked Install Browser lands on the merchant's dashboard with `?error_code=EC…` Install & authorize errors

2 **The token endpoint** — `POST https://oauth.zid.sa/oauth/token` A JSON error body Token endpoint errors

3 **An API call** — `https://api.zid.sa/v1/…` Zid's error envelope with a `message.code` API request errors

**If you are in a hurry:** go straight to the decision tree .

## Two response shapes you must handle #

### Zid's standard error envelope #

Used by every API endpoint, and by the token endpoint for most failures:

```
` {
"status" : "error" ,
"message" : {
"type" : "error" ,
"code" : "ERROR_SESSION_INVALID" ,
"name" : "Sorry" ,
"description" : "Invalid authentication"
}
} `
```

**`message.code` is what you branch on.** It is stable.

**`message.description` is not.** It is editorial, localised text. See

Your errors are in Arabic .

`code` and `name` are sometimes `null` — the table in each section says when.

### Validation errors use a different envelope #

HTTP `422` replaces `message` with a `validations` array and sets a different `status`:

```
` {
"status" : "validation_error" ,
"message" : {
"type" : "validation_errors" ,
"code" : "ERROR_POPUP_OK" ,
"name" : "Inputs" ,
"description" : "Input errors!" ,
"validations" : [
{ "field" : "email" , "errors" : [ "The email field is required." ] }
]
}
} `
```

A parser that assumes `message.description` is always the whole story will silently drop

the per-field detail. Check `status` first.

## 1. Install & authorize errors #

When the authorize step fails, Zid **does not** show your app an error. It redirects the

merchant's browser to their Zid dashboard with an `error_code` query parameter:

```
`https://web.zid.sa/…?error_code=EC3`
```

⚠️ **The merchant will not notice this.** The dashboard does not currently render a

message for `error_code`, so from the merchant's point of view the install button simply

did nothing. When a merchant reports "installing your app does nothing", **ask them to

paste the full URL from their address bar** — the `error_code` is the only diagnostic

signal that exists.

### The `EC` codes #

Code OAuth equivalent What actually happened What to do

**EC1** `invalid_scope` Your app is requesting a scope Zid does not recognise. Usually a scope that was renamed or retired while your app still had it granted. Open your app in the Partner Dashboard, re-save the scope list, and confirm every scope appears in the current scopes list. Contact Partner Support if a scope you need is missing.

**EC2** `invalid_grant` The `client_id` in the authorize URL does not belong to the app record Zid resolved. This is an identity-hijack guard. You are almost certainly mixing environments or apps — a staging `client_id` with a production authorize URL, or a copied URL from another app. Re-copy `client_id` from the Partner Dashboard for this app.

**EC3** `access_denied` Two distinct causes: **(a)** the merchant clicked **Decline** on the consent screen; **(b)** your app is not published and this store has no private grant for it. (a) Nothing to fix — ask the merchant to retry and approve. (b) Check your app's listing status. For testing, use a development store or request a private grant for the merchant's store.

**EC4** `access_denied` (Zid-specific) Your app has paid plans, and this store has **no active plan subscription** for it. The merchant must complete or renew the app subscription before the install can finish. Confirm the subscription state in the Partner Dashboard before debugging anything else.

**EC5** `invalid_request` `client_id` was missing, empty, or matched no app at all. Check the authorize URL actually carries `client_id=…`. A common cause is a templating bug emitting an empty value.

**UNKNOWN** — An OAuth error outside the mapped set. Capture the full redirect URL, the `client_id`, the store id, and the timestamp, and open a ticket.

**EC3 is the ambiguous one.** "Merchant declined" and "app not visible to this store"

produce the identical code. Rule out the listing/private-grant cause first, because it is

the one you can fix.

### Errors that are **not** redirects #

Three authorize-step failures render an **HTML error page** instead, so the merchant sees a

real message:

Situation What the merchant sees

Your app needs the **Direct Integration (APIs) add-on** and the store is not subscribed HTTP 403 page: "This app needs the Direct Integration (APIs) add-on. Subscribe to it to activate the app." — with a button to subscribe

The app requires an active **Mazeed** account that the store does not have HTTP 403 page: "This app requires your store to be activated in Mazeed. Please activate to complete the installation."

Your app is a **shipping app**, or the `client_id` resolved to no app HTTP error page carrying the real OAuth message and status, rather than an `EC` redirect

If a merchant sends you a screenshot of a Zid-branded error card rather than a dashboard,

you are in this group — read the message on the card; it is accurate.

### "Opening the authorize URL does nothing at all" #

No `error_code`, no error page, just the merchant's dashboard. **The merchant is not logged

in.** Zid redirects an unauthenticated merchant to their dashboard

(`…/apps/{app_id}`, or the shipping-providers page for shipping apps) rather than returning

an OAuth error.

**Fix:** have the merchant sign in to their Zid store in the same browser, then start the

install again.

### Install checklist #

Before debugging deeper, verify all five:

1 .

`client_id` matches this app in this environment.

2 .

`redirect_uri` **exactly** matches a registered allowed redirection URL — scheme, host,

port, path, trailing slash.

3 .

`response_type=code`.

4 .

The app's listing status permits this store to see it (published, or private-granted).

5 .

If the app has plans, this store has an active subscription.

## 2. Token endpoint errors #

`POST https://oauth.zid.sa/oauth/token`

⚠️ **Zid's token endpoint returns two different error shapes.** Most failures come back in

Zid's standard envelope with HTTP **400**. One specific failure comes back in the RFC 6749

shape. **Handle both** — branch on whether the body has a top-level `error` key.

### Shape A — Zid envelope (most failures) #

HTTP **400**, with `code` and `name` both `null`. The OAuth reason is in

`message.description`:

```
` {
"status" : "error" ,
"message" : {
"type" : "error" ,
"code" : null ,
"name" : null ,
"description" : "Client authentication failed"
}
} `
```

**Note on status codes:** these are returned as **400** even where RFC 6749 specifies a

different status — `invalid_client` and an invalid refresh token are both 400 here rather

than 401. Do not dispatch on the HTTP status alone at this endpoint; read the description.

`description` contains OAuth error Cause Fix

"Client authentication failed" `invalid_client` Wrong `client_id`, wrong `client_secret`, or mixed environments Re-copy both from the Partner Dashboard. Check for whitespace or newlines from copy-paste, and that your secret store isn't truncating.

"The request is missing a required parameter, includes an invalid parameter value, includes a parameter more than once, or is otherwise malformed." `invalid_request` **Six different problems return this one message.** Most often the authorization code was already used, or it expired. Work through the six causes , in order

"The refresh token is invalid." `invalid_request` The refresh token was rejected — reused, expired, revoked by an uninstall, or issued to another client Work through the four causes

"The authorization grant type is not supported" `unsupported_grant_type` Typo in `grant_type` Must be exactly `authorization_code` or `refresh_token`

"The requested scope is invalid, unknown, or malformed" `invalid_scope` Requested a scope your app does not hold Omit `scope` to receive your app's current grants, or request a subset of them

"The authorization server encountered an unexpected condition …" `server_error` Zid-side fault Retry with backoff; if it persists, open a ticket with the timestamp

#### Six causes behind the generic parameter error #

This is the failure you are most likely to meet, and **the response does not tell you which

of six problems you have**. Every authorization-code failure returns the same sentence:

```
` {
"status" : "error" ,
"message" : {
"type" : "error" ,
"code" : null ,
"name" : null ,
"description" : "The request is missing a required parameter, includes an invalid parameter value, includes a parameter more than once, or is otherwise malformed."
}
} `
```

Work through the causes in this order — they are sorted by how often each one turns out to

be the real problem:

1 .

**The code was already used.** Authorization codes are **single use**. The moment one is

exchanged successfully it is spent, and any second exchange of the same code fails. See

the callout below — this is the cause most people hit first.

2 .

**The code expired.** Codes are valid for **10 minutes**. If you hand the callback off to

a queue or a background worker, you will hit this intermittently and inconsistently.

Exchange the code synchronously, inside the callback request.

3 .

**`redirect_uri` mismatch.** The `redirect_uri` sent to `/oauth/token` must be

byte-identical to the one sent to `/oauth/authorize`, and both must match a registered

allowed redirection URL. `https://x.com/cb` and `https://x.com/cb/` are different values.

4 .

**The code was issued to another client.** The `client_id` exchanging the code is not the

one that obtained it — the classic staging/production mix-up.

5 .

**A required parameter is missing or empty.** All five fields — `grant_type`,

`client_id`, `client_secret`, `redirect_uri`, `code` — must be present in the **request

body**, not the query string. An empty string counts as missing.

6 .

**The code is malformed or cannot be decrypted.** Usually truncation or re-encoding.

Authorization codes are very long; a database column that is too short, a URL-decode

applied twice, or a copy-paste that clipped the end all land here.

⚠️ **Reloading the callback page produces this error.**

The authorization code is spent by the first successful exchange. If you then press

refresh, use the browser's Back button, or reopen the callback URL from your history, the

same code is submitted a second time and the request fails with the generic message above

— **even though the first attempt succeeded and the tokens it returned are perfectly

valid.**

This is a normal refusal, not a broken integration. If you captured the tokens from the

first attempt, keep them. If you did not, **start a new authorization from the beginning**

to get a fresh code. Never re-submit a code that has already been sent.

This is especially easy to trigger while testing with

Zid Bridge (https://docs.zid.sa/zid-bridge), because the callback URL stays in your

browser's address bar.

**Why all six look identical.** Zid's authorization server does determine a specific

reason internally — "Authorization code has been revoked", "Authorization code has

expired", and so on — but that detail is not currently included in the response. Expect to

diagnose these by elimination rather than by reading the error.

#### Four causes behind an invalid refresh token #

A different message, with its own set of causes. Work through them in this order:

1 .

**The refresh token was already used.** A successful refresh **revokes the old refresh

token** and issues a new one. If your token write is not atomic, or two workers refresh

the same merchant concurrently, one of them is left holding a dead token. Serialise

refreshes per store with a lock, and persist the whole new token set in one transaction.

2 .

**The refresh token expired.** Refresh tokens are valid for **one year**. This is the

failure a scheduled refresh job exists to prevent — see the

preventive checklist .

3 .

**The merchant uninstalled your app.** Uninstalling revokes the refresh token along with

everything else. If the app is no longer installed, no retry will ever succeed — mark the

installation inactive and wait for a reinstall.

4 .

**The token belongs to a different client.** The refresh token was issued to another

`client_id` — again, usually a staging/production mix-up.

### Shape B — RFC 6749 shape (one specific failure) #

HTTP **400**, with a top-level `error` key:

```
` {
"error" : "invalid_request" ,
"error_description" : "App installation is not allowed"
} `
```

**Cause:** your app has paid plans, but the store has no active plan subscription for it.

**This happens after the credentials were accepted** — the token was minted and then

immediately revoked, so any token value you may have captured from an earlier log line is

already dead.

**Fix:** the merchant must activate or renew the app subscription, then install again. This

is the token-endpoint sibling of `EC4` ; seeing both for one merchant is

consistent, not contradictory.

## 3. API request errors #

`https://api.zid.sa/v1/…` with `Authorization` + `X-Manager-Token`.

All of these use Zid's standard envelope except `422`.

### 401 — authentication #

`message.code` `description` (en) Cause What to do

`ERROR_SESSION_MISSING` "Please login first." Neither `X-Manager-Token` nor `Access-Token` was sent Add the `X-Manager-Token` header with the `access_token` value from the token response

`ERROR_SESSION_INVALID` "Invalid authentication" The manager token could not be decrypted — it is corrupted, truncated, re-encoded, or from a different environment Send the `access_token` value **verbatim**. Do not URL-encode, re-encrypt, trim, or pass it through a JSON round-trip that may mangle it. Check your column is wide enough — these tokens are long.

`ERROR_SESSION_INVALID` "Login session expired. Please login again." The manager token is past its expiry, **or its underlying record no longer exists** Refresh. **If a successful refresh does not fix it, the merchant uninstalled your app** — see the decision tree .

`ERROR_SESSION_INVALID` "The authentication token has been revoked" The Authorization token was explicitly revoked Do not retry. Treat as uninstalled until the merchant reinstalls.

`null` "Unauthenticated" The `Authorization` bearer token was rejected outright — missing, malformed, expired, or revoked Check the header is `Authorization: Bearer <authorization>` (the `authorization` field, **not** `access_token`). Then refresh.

`null` a message mentioning the required **scope** **Your token is missing a required scope.** **Do not refresh.** See the warning below.

🚨 **A missing scope returns 401, not 403.**

This is the single most expensive trap in Zid's auth surface. The natural reaction to a

401 is "token expired → refresh" — but the refreshed token carries the same scopes, so

the next call 401s again, and your client loops until it trips the rate limiter and starts

returning 429 instead.

**How to tell it apart from a real expiry:** a scope 401 has `message.code: null` and a

description naming a scope, and **it does not go away after a successful refresh**.

**Defensive rule:** never retry a 401 more than once per token. Refresh at most once, and

if the same endpoint 401s again with the new token, stop and treat it as a scope problem.

**Fix:** add the scope to your app in the Partner Dashboard. Existing merchants must then

re-approve it — see Scope and consent errors .

### 403 — authorized, but not allowed #

`message.code` `description` (en) Cause What to do

`APP_PERMISSIONS_PENDING_APPROVAL` "Permissions pending merchant approval." You added scopes; **this merchant has not approved them yet** Only the merchant can clear it — by **deactivating and reactivating your app**. Their subscription is not affected. See below .

`APP_PERMISSION_REMOVED` "This app no longer has the permission this request needs." A scope was removed from your app after the token was issued Restore the scope in the Partner Dashboard, or stop calling the endpoint. Note: enforcement of this is currently gated — today you are more likely to see the 401 scope error above.

`ERROR_POPUP_OK` "Subscription is not active." The **merchant's own Zid store subscription** has lapsed — nothing to do with your app Not fixable by you. The merchant must renew their Zid plan. Pause syncs for that store and retry later.

`ERROR_POPUP_OK` "This action is not allowed on demo store" You sent a non-`GET` request to a demo store Demo stores are **read-only**. Only `GET` requests succeed.

`ERROR_POPUP_BACK` "Store mobile isn't verified" The merchant has not verified their mobile (or email, for non-KSA stores) The merchant must verify in their dashboard

`ERROR_POPUP_BACK` "Store readiness isn't completed" The store has not finished onboarding The merchant must complete store setup

`ERROR_POPUP_OK` "Permission Denied" The merchant user your token belongs to lacks the role permission this endpoint requires Usually means the token was issued to a sub-user, not the store owner. Have the owner authorize, or have them grant the permission.

**The 403s split cleanly into two groups.** `APP_PERMISSIONS_PENDING_APPROVAL` and

`APP_PERMISSION_REMOVED` are **your** problem (scope configuration). Everything else is

**the merchant's** account state and no amount of retrying or re-authorizing will change

it. Surface those to the merchant rather than to your error logs.

### 404, 422, 429, 500 #

HTTP `message.code` Cause What to do

`404` `ERROR_SESSION_INVALID` "Store not found." The user behind the token has no store Mark the installation broken and open a ticket with the store id — this should not normally happen

`422` `ERROR_POPUP_OK` Validation failure — **uses the validation envelope ** Read `message.validations[]` for per-field detail

`429` `MSG_HIDDEN` Rate limit exceeded Honour the **`Retry-After`** response header. See below .

`500` `ERROR_POPUP_OK` "Something went wrong" — server-side fault Retry with exponential backoff. If persistent, open a ticket with the timestamp and `X-Request-Id`.

## Scope and consent errors #

Zid enforces scopes **per request, against the app's current configuration** — not against

whatever was frozen into the token at issue time. Two consequences:

### When you add a scope to a live app #

Every existing installation is flagged pending consent for the newly added scope.

Per request, Zid subtracts the un-approved scopes from the live token:

endpoints covered by **already-approved** scopes → keep working normally;

endpoints needing the **new** scope → `403 APP_PERMISSIONS_PENDING_APPROVAL`.

Until the merchant re-approves, that specific capability is unavailable for that specific

merchant. Different merchants will be in different states at the same time — your code must

tolerate this per-store.

#### How the merchant re-approves #

**The merchant deactivates your app, then activates it again**, from their Zid dashboard.

There is no separate "approve new permissions" prompt — reactivation is the approval

step, because the merchant sees the full, current scope list on the way back in.

Tell the merchant this plainly, and reassure them about the thing they will worry about:

**Deactivating does not cancel your subscription.** If the store has a paid subscription

to the app, deactivating leaves it untouched — the merchant can reactivate at any time

while the subscription is still valid, at no extra cost.

**What you must handle:** reactivation issues a **fresh token pair** carrying every current

scope, delivered the same way the original install was. Your app must accept and persist

new tokens for a store that is already installed — overwrite the stored

`authorization`, `access_token` and `refresh_token` for that store rather than rejecting

the callback as a duplicate install.

A reactivation is therefore not a new customer; it is the same installation with new

credentials. If your code keys on "first install only", the merchant will reactivate,

your app will discard the new tokens, and the 403s will continue — which looks to everyone

like the re-approval didn't work.

🚨 **If your app uses a wildcard token, adding a scope takes the whole integration down

for that merchant.** A wildcard token cannot express "everything except these two", so

Zid withholds the app **entirely** — every endpoint returns

`403 APP_PERMISSIONS_PENDING_APPROVAL` — until the merchant re-approves.

Plan wildcard-token scope changes like a release: notify merchants first, expect a

re-consent window, and do not ship on a Friday.

### When a scope is removed from your app #

Removed scopes are subtracted the same way, surfacing as `403 APP_PERMISSION_REMOVED` with

the offending scopes listed in the response. **Enforcement is currently behind a feature

flag and is off by default**, so today a removed scope more commonly shows up as the

401 scope error . Write your handler to treat both the same way.

### Handling consent states well #

Signal Meaning Right response

`403 APP_PERMISSIONS_PENDING_APPROVAL` on **some** endpoints Partial consent Degrade that feature; keep the rest running. Ask the merchant to deactivate and reactivate the app.

`403 APP_PERMISSIONS_PENDING_APPROVAL` on **every** endpoint Wildcard token, consent pending Pause the integration for that store; ask the merchant to deactivate and reactivate the app

`403 APP_PERMISSION_REMOVED` Scope config drift Fix your app config; alert your own team, not the merchant

Never auto-retry a consent 403 on a timer. It resolves only when a human merchant acts.

**Message you can send the merchant, as-is:**

To finish updating the app's permissions, please open your Zid dashboard, **deactivate**

the app and then **activate** it again. Your subscription is not affected — you can

reactivate at any time while it is valid, at no extra cost.

## 429 — rate limiting #

Zid rate-limits app requests **per app, per store** — the default is **60 requests per 60

seconds** for each store your app serves. Per-app and per-store limits can be configured by

Zid, so treat 60/60s as a floor, not a contract.

Response: HTTP `429`, `message.code` = `MSG_HIDDEN`, plus a **`Retry-After`** header giving

the seconds until the window resets.

**Handle it like this:**

1 .

Read `Retry-After` and wait that long. Do not use a fixed sleep.

2 .

Back off **per store**, not globally — one busy merchant should not stall the others.

3 .

Serialise bulk work per store rather than fanning out concurrently.

**The most common cause of a 429 is not traffic volume.** It is the

401 refresh loop : a missing scope returns 401, your client refreshes

and retries, the new token is missing the same scope, and the loop consumes the whole

window in seconds. If you see 429s with low real throughput, look for a scope error

underneath.

See also: Rate Limiting (https://docs.zid.sa/rate-limiting-644369m0).

## Your errors are in Arabic #

**If you omit the `Accept-Language` header — or send anything other than `ar` or `en` —

Zid replies in Arabic.** Arabic is the default locale, not a fallback to English.

```
``
```

Partners commonly hit this when a staging environment sets the header and production does

not, producing error strings their log parsers have never seen.

**The durable fix is not the header.** Branch your logic on `message.code`, never on

`message.description`. Codes are stable identifiers; descriptions are localised editorial

text in two languages and can be reworded at any time.

## Uninstalls, revocation, and propagation delay #

When a merchant uninstalls your app, Zid:

1 .

sends you an `app.market.application.uninstall` webhook;

2 .

**deletes** the manager-token records for your app on that store;

3 .

**revokes** the Authorization tokens and their refresh tokens;

4 .

clears the token caches.

**Nothing you hold for that store still works, and refresh cannot recover it.** The only

path back is the merchant installing your app again, which starts a fresh authorization

flow.

**An uninstalled app and an expired session return the identical error** — `401` with

`ERROR_SESSION_INVALID` and "Login session expired." The distinguishing test is whether a

refresh fixes it. See the decision tree .

**Propagation delay.** Token state is cached for up to **5 minutes**. A token can keep

working for a short window after revocation, and conversely a freshly-fixed permission can

take a few minutes to take effect. When testing revocation behaviour, wait 5 minutes before

concluding anything.

**Treat the uninstall webhook as authoritative** and mark the installation inactive on

receipt, rather than discovering it later through 401s.

**One webhook caveat:** `app.market.application.authorized` is dispatched during the

authorize step, **before** the token exchange completes. An install can therefore fail

after you have already received `authorized`. Use `app.market.application.install` as

your signal that an installation is real and usable.

## The decision tree #

```
`A request failed. Where?
│
├─ The merchant clicked Install and landed on their dashboard
│ └─ Read ?error_code= from the URL they paste → §1 EC table
│ ├─ no error_code at all → merchant was not logged in
│ └─ a Zid-branded error card instead → read the card; it's accurate
│
├─ POST /oauth/token returned an error
│ ├─ body has a top-level "error" key
│ │ └─ "App installation is not allowed" → no active app subscription; merchant must
│ │ subscribe, then reinstall
│ └─ body is Zid's envelope (code: null) → read message.description
│ ├─ "Client authentication failed"
│ │ → client_id / client_secret / wrong environment
│ ├─ "...missing a required parameter..."
│ │ → the generic message. SIX causes share it; work them in order.
│ │ Most often the code was already used — did you reload the
│ │ callback page? — or it expired (10-minute limit).
│ └─ "The refresh token is invalid."
│ → reused / expired (1y) / uninstalled / wrong client.
│ App still installed? Restart the install flow.
│ Not installed? Mark the installation inactive.
│
└─ An API call to api.zid.sa failed
│
├─ 429 → honour Retry-After, back off per store.
│ Low real traffic? Look for a 401 loop underneath.
│
├─ 403 → is message.code APP_PERMISSIONS_PENDING_APPROVAL / APP_PERMISSION_REMOVED?
│ ├─ yes → YOUR scope config. Do NOT retry on a timer.
│ │ PENDING_APPROVAL → merchant deactivates + reactivates the app
│ │ (subscription unaffected). Be ready to store the NEW tokens.
│ │ PERMISSION_REMOVED → restore the scope in the Partner Dashboard.
│ └─ no → MERCHANT account state (subscription, verification, readiness,
│ permissions, demo store). Not fixable by you — surface it to them.
│
├─ 422 → validation envelope; read message.validations[]
│
├─ 404 ERROR_SESSION_INVALID → store missing; open a ticket with the store id
│
└─ 401 → Refresh the token ONCE.
│
├─ Refresh succeeded, call now works
│ → ordinary expiry. You are refreshing too late:
│ move to a scheduled refresh (~every 10 months).
│
├─ Refresh succeeded, call still 401s
│ → MISSING SCOPE. Stop retrying immediately.
│ Add the scope; existing merchants must re-approve.
│
└─ Refresh itself failed
→ the merchant uninstalled (or tokens were revoked).
Mark the installation inactive. Wait for a reinstall.`
```

## Preventive checklist #

Most authorization tickets Zid receives are one of these seven things. Ship all seven:

1 .

**Refresh on a schedule, not on a 401.** Roughly every 10 months, per merchant, from a

cron job. The refresh token lasts **1 year** while the access token lasts **3** — so a

reactive strategy never fires at all: no 401 arrives in year one, the refresh token

expires unnoticed, and two years later the integration dies with no way back except

asking every affected merchant to reinstall.

2 .

**Persist the full token set atomically on every refresh** — new `authorization`, new

`access_token`, **new `refresh_token`**, new expiry. The old refresh token is revoked the

moment the new one is issued.

3 .

**Lock refreshes per store.** Two concurrent refreshes for one merchant leave one worker

holding a revoked token.

4 .

**Exchange the authorization code once, synchronously, inside the callback.** Never queue

it, never retry the same code, and make the callback safe to re-open — a reload must not

look like a failed install.

5 .

**Cap 401 retries at one per token.** This single rule prevents the scope-error refresh

loop and the 429s it causes.

6 .

**Branch on `message.code`, never on `message.description`.** Descriptions are localised

(Arabic by default) and editorial.

7 .

**Act on the uninstall webhook immediately** — mark the installation inactive rather than

discovering it through failed calls days later. And **accept new tokens for a store you

already know**: a merchant reactivating your app sends a fresh token pair for an existing

installation, so overwrite the stored tokens instead of discarding the delivery as a

duplicate install.

## Getting help #

When opening a ticket, include:

the **store id** and your **app id**;

the **UTC timestamp** of the failed request;

the `X-Request-Id` response header, if you captured it;

the **full HTTP status and response body**, including `message.code`;

for install failures, the **complete redirect URL** including `error_code`;

what you have already ruled out from this page.

Channels: Partner Help Center (https://help-partner.zid.sa/en/) , Zid Partners Telegram Community (https://t.me/zidpartnersthemes)

## Related #

Authorization (https://docs.zid.sa/authorization) — the OAuth 2.0 flow itself

Public Apps OAuth Requirements (https://docs.zid.sa/oauth-requirements) — the activation journey and security rules app review checks

Zid Bridge (https://docs.zid.sa/zid-bridge) — generate tokens for testing without writing code

Responses (https://docs.zid.sa/responses) — the general response envelope

Rate Limiting (https://docs.zid.sa/rate-limiting-644369m0)

Webhooks Overview (https://docs.zid.sa/webhooks)

Modified at 2026-10-27 11:18:40

Previous

Public Apps OAuth Requirements

Next

Zid Bridge Tool
