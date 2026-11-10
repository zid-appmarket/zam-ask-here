---
# Synced from https://docs.zid.sa/login-checkout-via-page-views-2258377m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-login-checkout-via-page-views
title: "Login & Checkout via Page Views"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/login-checkout-via-page-views-2258377m0
tags: [from-docs-site, partner-docs]
language: en
---

> Login & Checkout via Page Views - Zid Docs
# Login & Checkout via Page Views

The Storefront APIs do **not** provide endpoints for login or checkout.

Mobile apps must handle both flows by opening the storefront **web pages** (e.g. in a WebView) instead of calling an API.

📌

This applies to the **login page** and the **checkout page** only. All other storefront functionality remains available through the APIs.

## Session Cookie #

When opening the page view, you must pass the **session cookie** along with the request.

The page uses this cookie to attach the logged-in session to it.

The same cookie is then used across **all API requests**, keeping the web session and your API calls in sync.

Make sure your WebView shares its cookie store with your API client so the session stays consistent in both directions.

## Required Header #

Always send the following header with **every request** you make — page views and API calls alike:

```
`Zid-Client-Platform: mobile-app`
```

1

1. Open the page

When the user needs to log in or check out, open the corresponding storefront page in a WebView.

2

2. Pass the session cookie

Include the session cookie with the page view request so the logged-in session is attached to it.

3

3. Include the platform header

Send `Zid-Client-Platform: mobile-app` with the page view and all subsequent API requests.

Modified at 2026-07-15 14:30:15

Previous

Scripts

Next

Theme Sections Settings
