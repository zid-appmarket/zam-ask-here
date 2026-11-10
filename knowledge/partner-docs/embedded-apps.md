---
# Synced from https://docs.zid.sa/embedded-apps-2168216m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-embedded-apps
title: "Embedded Apps"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/embedded-apps-2168216m0
tags: [from-docs-site, partner-docs]
language: en
---

> Embedded Apps - Zid Docs
# Embedded Apps

# Developer Guide #

Embedded Apps within the Merchant Dashboard offer a seamless integration experience for both Merchants and Zid Partners. These applications are integrated directly into the dashboard through an iframe, allowing merchants to access and interact with your app without leaving the Zid Merchant Dashboard.

## Benefits for Partners #

**Seamless Integration:** Embed your app within Zid Merchant Dashboard for a unified merchant experience.

**Enhanced Visibility:** Increase app exposure and engagement.

**Simplified Access:** No separate logins required, making it easier for merchants to use your app.

**Customer Loyalty:** A seamless experience fosters higher satisfaction and long-term use.

## Authentication Flow #

The embedded apps feature is designed to bypass standard logins. The flow consists of 6 mandatory steps:

### Step 1 — Merchant installs the app #

The merchant initiates installation from the Zid Merchant Dashboard. Zid redirects to your Redirect URL with an authorization code. Ensure you include the `embedded_apps_tokens_write` scope in your initial OAuth request. After your app completes the OAuth flow, redirect the merchant to the Zid Dashboard embedded app route to open the app inside the dashboard.:

```
``
```

### Step 2 — Exchange code for tokens #

Your callback endpoint receives `?code=...`. Exchange it for tokens:

```
``
```

Save the `access_token`, `authorization`, and `refresh_token` in your database, associated with this merchant's `store_id`.

### Step 3 — Register a lookup token with Zid #

Generate a **UUID (version 4)** on your server. Do **not** use the `authorization` JWT — JWTs are too long and will fail due to URL truncation when passed to the iframe.

Store this UUID in your database alongside the merchant's tokens, and register it with Zid:

```
``
```

### Step 4 — Configure the Application URL #

In your Zid Developer Dashboard, set the **Application URL** to a fixed endpoint on your server that will serve the iframe content (e.g., `https://your-app.com/embedded`).

### Step 5 — Merchant opens the embedded app #

When a merchant accesses your app, Zid loads your Application URL in an iframe, appending the UUID you registered:

```
``
```

### Step 6 — Identify the merchant and render #

Your Application URL handler must:

1 .

Read the `token` query parameter.

2 .

Look up the UUID in your database to retrieve the merchant's `store_id` and stored tokens.

3 .

Render the embedded page.

## Redirecting Merchants to the Embedded App After Installation #

After a merchant successfully installs your embedded app and your app completes the OAuth flow, you can redirect the merchant to the embedded app inside Zid Merchant Dashboard.

Use the following URL structure:

```
`https://dashboard.zid.sa/{language_code}/stores/{store_id}/apps/{app_id}/embedded`
```

Example:

```
`https://dashboard.zid.sa/ar-sa/stores/1/apps/4820/embedded`
```

### URL Behavior #

When redirecting merchants to the embedded app URL:

`{app_id}` must be your actual Zid app ID.

`{store_id}` can contain any valid value.

`{language_code}` can contain any supported dashboard language value, such as `ar-sa`.

Hermes automatically resolves the correct store ID and language based on the merchant’s dashboard session.

This means your app does not need to detect the merchant’s current dashboard language before redirecting. Zid will handle the final store and language context automatically.

### When to Use This URL #

Use this URL after your app completes the installation and authorization flow, especially when you want the merchant to continue using the app directly inside Zid Merchant Dashboard.

## Identifying the Merchant (Multi-Store) #

Each store that installs your app must get its own unique UUID lookup key.

**Recommended Database Schema:**

```
``
```

## Content Security Policy (CSP) #

For the security of embedded applications, Zid enforces CSP. Every page served inside the iframe must include these headers:

```
`Content-Security-Policy:
style-src 'self' 'unsafe-inline' *;
font-src 'self' 'unsafe-inline' data: *;
default-src 'self' *.zid.dev web.zid.sa dashboard.zid.sa;
script-src 'self' 'unsafe-inline' *;
frame-ancestors 'self' *.zid.dev web.zid.sa dashboard.zid.sa;
connect-src 'self' 'unsafe-inline' *`
```

**Note:** Without the `frame-ancestors` directive, Zid's dashboard will block the iframe.

## Token Management #

### Delete User Token #

When a merchant uninstalls the application, revoke their access by deleting the authorization token from Zid's system:

```
``
```

## Common Pitfalls & Security Recommendations #

1 .

**Do not use the JWT as the token parameter** — JWTs will cause URL truncation. Always map a short UUID to the JWT locally.

2 .

**URL encoding** — Use URL-safe characters for your token. UUIDs (hex + hyphens) are safe.

3 .

**Missing scope** — The `embedded_apps_tokens_write` scope must be present in the initial OAuth redirect.

4 .

**Re-installations** — When a merchant reinstalls, generate a new UUID. The old UUID stored at Zid becomes stale.

5 .

**Secure storage** — Store `access_token` and `authorization` securely on your server — never expose them to the browser or iframe HTML.

## Starter Project (Community Version) #

A simple reference implementation for the authorization flow:

**Zid Embedded App Starter — Authorization (https://github.com/akotb-zid/Zid-Embedded-App-Starter-Authorization)**

A minimal Flask starter for the Zid Embedded Apps OAuth authorization flow. Implements steps 1–6 of the Embedded Apps Authentication Flow — install, token exchange, UUID registration, and iframe rendering — so you can focus on building your app logic.

Community project — open source, open for improvements. This is not an official Zid package. Contributions and forks are welcome.

Modified at 2026-06-10 04:31:46

Previous

Rate Limiting

Next

StoreFront Events
