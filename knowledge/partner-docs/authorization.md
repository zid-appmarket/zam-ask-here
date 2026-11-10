---
# Synced from https://docs.zid.sa/authorization
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-authorization
title: "Authorization"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/authorization
tags: [from-docs-site, partner-docs]
language: en
---

> Authorization - Zid Docs
# Authorization

OAuth 2.0 is the industry-standard protocol for authorizing apps, allowing secure access to resources without exposing sensitive data like passwords. It differs from authentication, which verifies the identity of the user or app.

## Understanding OAuth 2.0 at Zid #

At Zid, we use the **authorization code grant** (https://datatracker.ietf.org/doc/html/rfc6749#section-4.1)

type, which is ideal for confidential clients. This method involves redirecting the user to

an authorization server, where they grant permissions to your app. Your server-side app

must handle this process, as it requires securely managing the Client Secret.

**PKCE is not used.** Zid's authorization code grant is for confidential clients only.

Do not send `code_challenge` / `code_verifier` — they are ignored. Protect the

authorization request with the `state` parameter instead (see step 2).

## Key Concepts in Zid's OAuth 2.0 Flow #

**Authorization Token** — grants your app access to the Zid API. Sent as

`Authorization: Bearer <token>`.

**X-MANAGER-TOKEN** — grants access to one specific store on the Zid platform. It adds an

extra layer of security when interacting with store-specific resources.

**Access-Token** — the same value as `X-MANAGER-TOKEN`. The token endpoint returns it under

the JSON key `access_token`, and Product-component endpoints accept it under the header

name `Access-Token` for historical reasons.

**One value, three names.** The token endpoint returns it as `access_token`. Send it as

`X-Manager-Token` (preferred) **or** `Access-Token` — the API checks for

`X-MANAGER-TOKEN` first and falls back to `Access-Token`. Never send both with different

values.

## Important Requirements #

💡 Your app must run server-side because it needs to securely store the Client Secret

during this process.

💡 Almost every API request requires **both** the `Authorization` and `X-Manager-Token`

headers. One without the other fails.

💡 Always send `Accept-Language: en` (or `ar`) explicitly. **If the header is missing or

holds any other value, Zid replies in Arabic** — including error messages. Only `ar` and

`en` are recognised.

#### What's the difference between Authorization token and X-MANAGER-TOKEN? #

The Authorization token permits you to access the Zid API; X-MANAGER-TOKEN permits you to

access a particular store.

#### What's the difference between X-MANAGER-TOKEN and Access-Token? #

There is no difference between them. We use `Access-Token` with Product-component API

endpoints for technical reasons.

## Base URIs #

When developing apps on Zid, you'll work with two main URIs:

1 .

**Base API URL** — for resources like orders, products and coupons:

`https://api.zid.sa/v1`

2 .

**Base OAuth Server URL** — for app authorization:

`https://oauth.zid.sa`

💡 The latest version of our API is v1. Older versions are deprecated and should not be used.

### Benefits of Using OAuth 2.0 with Zid #

**Secure Access** — your app accesses Zid resources without ever handling merchant passwords.

**Scoped Permissions** — scopes define exactly what your app may touch, and the merchant

sees and approves that list.

**Token-Based Authentication** — tokens are time-limited and individually revocable.

Merchants can revoke access at any time by uninstalling your app.

## Implement OAuth 2.0 in your app #

### 1 — Generate Client ID and Client Secret #

Your **Client ID** and **Client secret** identify your app during the authorization

process. You get them when you create an app, and you can retrieve them at any time

afterwards.

**For a new app**

1 .

Log in to your Partner Dashboard (https://partners.zid.sa).

2 .

Go to **Apps → All Apps → Create Application**.

3 .

Choose the type of app you want to create, enter the app name, app URL, and allowed

redirection URLs, then create the app.

4 .

Open the **General settings** tab and scroll to **API keys**.

**For an app that already exists**

1 .

Go to **Apps → All Apps**.

2 .

Click the **edit (pencil) icon** on the app's row.

3 .

Open the **General settings** tab and scroll to **API keys**.

Under **API keys** you will find three values:

Field What it is

**OAuth 2.0 endpoint** `https://oauth.zid.sa` — the base OAuth Server URL

**Client ID** Your `client_id`

**Client secret** Your `client_secret`. Masked by default; use the eye icon to reveal it and the copy icon to copy it.

Use the copy icon rather than selecting the text by hand — these values are long, and a

truncated or whitespace-padded secret fails at the token exchange with a generic

"Client authentication failed".

**The `redirect_uri` you send later must match one of the allowed redirection URLs

exactly** — scheme, host, port, path, and trailing slash. A mismatch fails at the token

exchange, not at the redirect, which makes it easy to misdiagnose. See

Authorization Errors & Troubleshooting (https://docs.zid.sa/oauth-troubleshooting).

### 2 — Redirect (Ask for merchant permission) #

The installation process starts in your application via the redirection URL, followed by

these steps:

1 .

The browser is redirected to the Authorize endpoint of the OAuth Server (Zid AppMarket).

2 .

If the merchant isn't authenticated, the OAuth Server redirects to the Login page.

3 .

The merchant authenticates and is redirected back to the OAuth Server.

4 .

The merchant sees the scopes your application is requesting and approves (or declines).

5 .

The OAuth Server issues a one-time token called an **Authorization Code**, which is sent

to your application in the next step.

```
``
```

Parameters:

Parameter Required Description

`client_id` yes Your application's client id from the Partner Dashboard

`redirect_uri` yes An endpoint your application implements; must exactly match an allowed redirection URL

`response_type` yes `code`

`state` **strongly recommended** Opaque random value. Zid returns it unchanged on both approval and denial. Compare it in your callback to reject forged requests.

**If nothing happens when you open the authorize URL**, the merchant is probably not

logged in. Zid redirects an unauthenticated merchant to their dashboard

(`…/apps/{app_id}`, or the shipping-providers page for shipping apps) rather than

returning an error. Have the merchant sign in to their store first, then retry.

Zid AppMarket supports many scopes. Select the ones your application needs on your

application page in the Partner Dashboard.

**Changing scopes after merchants have installed your app has consequences.** Adding a

scope puts every existing installation into a pending consent state until that merchant

re-approves. Endpoints covered by already-approved scopes keep working; endpoints needing

the new scope return `403 APP_PERMISSIONS_PENDING_APPROVAL`. **If your app holds a

wildcard token, adding a scope withholds the app entirely for that merchant** until they

re-approve.

**The merchant re-approves by deactivating and reactivating your app** from their

dashboard. Reactivation issues a fresh token pair carrying every current scope, so **you

must be ready to receive and store new tokens** at that moment. See

Authorization Errors & Troubleshooting (https://docs.zid.sa/oauth-troubleshooting).

### 3 — Callback Method (Get the tokens) #

1 .

Our OAuth server sends the code to your pre-defined callback method.

2 .

Your app backend makes a `POST` request to the Token endpoint with the Authorization

Code and your Client Credentials.

3 .

The OAuth Server validates the code and the credentials, and returns an access token

and a refresh token.

4 .

Your app stores the returned tokens for future use.

⏱️ **The authorization code is valid for 10 minutes and can be used once.** Exchange it

immediately in the callback request. Do not queue the exchange for a background worker,

and do not retry with the same code after a failure — request a fresh one by restarting

the flow.

```
``
```

```
``
```

```
``
```

**Note:** In all examples the payload is sent in the request body, not as query parameters.

The response holds everything you need to authenticate against that merchant's store:

```
` {
"token_type" : "Bearer" ,
"expires_in" : 94608000 ,
"authorization" : "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9..." ,
"access_token" : "eyJpdiI6Ii8vZ..." ,
"refresh_token" : "def5020035c1f..."
} `
```

Field What it is Where it goes

`authorization` The Authorization token (a JWT) `Authorization: Bearer <authorization>`

`access_token` The store's manager token `X-Manager-Token: <access_token>`

`refresh_token` Used to obtain a new token pair Your token store only

`expires_in` Lifetime of `authorization` **in seconds** Compute the expiry and persist it

`token_type` Always `Bearer` —

⚠️ **`expires_in` is a number of seconds, not a date.** Newly issued Authorization

tokens are valid for **3 years** (`31536000` × 3 = `94608000` seconds). Still persist

`now + expires_in` from the response you actually received rather than hard-coding the

number — tokens issued before mid-2025 carry a shorter 1-year expiry, and the value can

change again.

#### Authorization token #

The Authorization token is generated by our OAuth 2.0 server: once a merchant installs your

application you receive it via the callback. Send it as the `Authorization` header on every

outgoing request.

All API requests must be made over HTTPS. Calls made over plain HTTP will fail. API

requests without authentication will also fail — see

Authorization Errors & Troubleshooting .

#### X-Manager-Token (access_token) #

This token is an extra layer of security and must be sent alongside the `Authorization`

token:

```
``
```

Pass the content of `access_token` under the name `X-Manager-Token`, together with

`Authorization`, on every request.

The manager token is issued with the **same expiry as the Authorization token** — 3 years

for newly issued tokens. Treat `expires_in` from the token response as authoritative for

both, and store both together.

The data returned by this endpoint must be kept in secure storage. Abusing tokens may

result in your app being blocked.

#### Token lifetimes #

Token Lifetime Notes

Authorization code **10 minutes**, single use Exchange it immediately

`authorization` (access token) **3 years** Tokens issued before mid-2025 carry 1 year — always read `expires_in`

`access_token` (X-Manager-Token) Same expiry as the Authorization token Reissued on every refresh

`refresh_token` **1 year** **Expires two years before the access token**

🚨 **The refresh token expires two years before the access token. This is the single most

common way Zid integrations die.**

A partner who refreshes "reactively, when a request returns 401" **never refreshes at

all.** The access token is still perfectly valid at month 12, so no 401 ever arrives —

while the refresh token silently expires. Two years later the access token dies too, and

by then there is no way to recover the installation: the only path back is asking every

affected merchant to reinstall your app.

**Refresh on a schedule, not on an error.** Run a cron job that refreshes every merchant

roughly **every 10 months**, regardless of whether anything has failed. This is the single

### 4 — Refresh #

Sooner or later your tokens expire. Refresh them well before they do:

```
``
```

The response has the same shape as the authorization-code response. Three rules:

1 .

**A refresh returns a new `refresh_token`, and revokes the old one.** Persist the whole

new token set atomically. If you keep the old refresh token, your next refresh fails.

2 .

**It also returns a new `access_token` (X-Manager-Token).** Replace the stored manager

token too, not just the `authorization` value.

3 .

**A failed refresh is not always retryable.** If it fails because the merchant

uninstalled your app, retrying will never succeed — see

Authorization Errors & Troubleshooting (https://docs.zid.sa/oauth-troubleshooting).

## Handling Errors #

Authorization can fail at three different places, each with its own error format:

Where What you get

The authorize redirect The merchant's browser lands on their dashboard with `?error_code=EC1`…`EC5`

The token endpoint A JSON error body — in **two possible shapes**

An API request Zid's standard error envelope with a `message.code`

Every code, its cause, and the exact fix are documented in

**Authorization Errors & Troubleshooting (https://docs.zid.sa/oauth-troubleshooting)**.

The three you will hit most often:

**`401` with no `message.code` and a "scope" message** — your token is missing a scope.

**Do not refresh**; refreshing returns a token with the same missing scope and loops.

**`403 APP_PERMISSIONS_PENDING_APPROVAL`** — you added a scope and this merchant has not

approved it yet. Only the merchant can clear this.

**`401 ERROR_SESSION_INVALID` that survives a refresh** — the merchant uninstalled your

app. Stop retrying and mark the installation inactive.

When a merchant uninstalls your app we send an `app.market.application.uninstall`

webhook, and **every token you hold for that store is revoked immediately** — the

Authorization token, the refresh token, and the X-Manager-Token.

## Security and Best Practices #

**Validate `state`** — generate a random `state` per authorization request and reject any

callback whose `state` does not match. The live Zid OAuth server echoes it back for exactly

this purpose.

**Keep the Client Secret server-side** — never ship it in a browser bundle, a mobile app, or

a public repository. Rotate it immediately if it leaks.

**X-MANAGER-TOKEN** — keep it as secure as the Authorization token; it grants access to a

specific store's resources.

**Secure Storage** — encrypt tokens at rest. One store's token compromise is one merchant's

data breach.

**Refresh on a calendar, not on a 401** — see the warning in step 3. This is the most

**Store tokens per merchant, keyed by store id** — a refresh replaces the whole token set

for one store only.

**Branch on `message.code`, never on `message.description`** — descriptions are localised

(Arabic by default) and are editorial text that can change. The codes are stable.

**Handle 429** — the API rate-limits per app **per store**. Respect the `Retry-After`

response header. See Rate Limiting (https://docs.zid.sa/rate-limiting-644369m0).

## Sample OAuth Clients #

We have developed sample starter apps to help you kick-start your integration:

1 .

Laravel App Sample (https://github.com/zidsa/laravel-sample-app)

2 .

Node.js + Express App Sample (https://github.com/zidsa/express-sample-app)

Modified at 2026-10-19 15:06:52

Previous

Authorization

Next

Public Apps OAuth Requirements
