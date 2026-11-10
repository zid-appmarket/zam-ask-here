---
# Synced from https://docs.zid.sa/scripts-1758413m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-scripts
title: "Scripts"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/scripts-1758413m0
tags: [from-docs-site, partner-docs]
language: en
---

> Scripts - Zid Docs
# Scripts

## JS Apps API #

Expose a manifest of approved scripts for your app to consume.

Use this to know **what to load** and **where it’s intended to run** inside your hybrid / mobile setup.

📌

This endpoint does not execute anything by itself.

It only returns configuration and script sources for your app to use.

## GET `/api/v1/scripts` #

**Auth:** Project-specific

**Content-Type:** `application/json`

**Returns:**

`external_scripts` — remote script URLs.

`app_scripts_bundle` — inline snippets and reserved keys indicating where scripts are meant to be used.

## Example Response #

```
` {
"external_scripts" : [
{
"id" : 101 ,
"src" : null ,
"url" : "https://cdn.example.com/scripts/tracking-abc123.js" ,
"status" : 2 ,
"app_id" : 5001 ,
"version" : 3
}
] ,
"app_scripts_bundle" : {
"scripts" : {
"head" : [
"<script type=\"text/javascript\">\n(function () {\n var s = document.createElement('script');\n s.async = true;\n s.src = 'https://widgets.example.com/support.js';\n document.head.appendChild(s);\n})();\n</script>"
] ,
"global_head_script" : [
"<script type=\"text/javascript\">\n(function (w,d,s,u) {\n var js = d.createElement(s);\n js.async = true;\n js.src = u;\n d.head.appendChild(js);\n})(window,document,'script','https://cdn.example-analytics.com/sdk.js');\n</script>"
]
} ,
"params" : {
"snapchatPixelId" : "..." ,
...
}
}
} `
```

## Field Details #

### `external_scripts` #

Remote JS files hosted and approved by the platform.

`url` — absolute URL to the script file.

Other fields (`id`, `status`, `app_id`, `version`) support identification and versioning.

Intended usage: load these URLs as normal script files in your chosen runtime.

### `app_scripts_bundle` #

Inline scripts plus reserved keys.

`scripts.head`

Inline snippets intended for a `<head>`-like context (early load).

`global_head_script`

Snippets intended to run once globally (shared initialization, loaders, etc.).

`purchase_event`

Snippets intended to run once a purchase is completed.

`product_details_event`

Snippets intended to run once a product's detail page is viewed.

`add_to_cart_event`

Snippets intended to run once add to cart is executed.

`remove_from_cart_event`

Snippets intended to run once remove item from cart is executed.

`start_checkout_event`

Snippets intended to run once the checkout page is started. These should already be covered by the existing checkout page HTML.

`params`

Contains identifiers like pixel ids or app ids.

These map to function or event names in JavaScript. At this stage they serve as predefined wiring points; dedicated tracking/analytics scripts will be provided separately via URLs and can be obtained through this manifest when available.

## Integration Overview #

Hybrid / WebView

React Native (and similar)

Fetch `/api/v1/scripts` from your native code.

Load `external_scripts` URLs and inline snippets inside your WebView (e.g. via injected scripts or startup HTML).

Use `head` / `global_head_script` placement semantics as guidance for when those scripts should run.

1

1. Call the endpoint

Retrieve `/api/v1/scripts` during your app's initialization or configuration phase.

2

2. Read the manifest

Inspect `external_scripts` and `app_scripts_bundle` to see which scripts and reserved keys are available.

3

3. Apply to your runtime

Inject or reference these scripts according to your app’s architecture (hybrid WebView or JS-based).

Future tracking scripts can be added via new URLs surfaced by the same manifest.

Modified at 2026-07-30 11:49:13

Previous

Bundle Progress

Next

Login & Checkout via Page Views
