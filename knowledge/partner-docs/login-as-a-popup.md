---
# Synced from https://docs.zid.sa/login-as-a-popup-1702155m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-login-as-a-popup
title: "Login as a Popup"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/login-as-a-popup-1702155m0
tags: [from-docs-site, partner-docs]
language: en
---

> Login as a Popup - Zid Docs
# Login as a Popup

The login popup feature allows users to authenticate without leaving the current page. When enabled, it provides a modal dialog for user login, creating a smoother and more seamless user experience.

## Enabling the Feature #

The login popup feature can be enabled or disabled through the Merchant Dashboard settings under the following path:

**Path:** `https://dashboard.zid.sa/en-sa/stores/<store_id>/settings/checkout`

By default, the **Login Popup Feature** is **enabled** for all stores. When enabled, the platform will automatically inject the necessary functionality into your store.

## Global API Objects #

### `window.auth_dialog` #

When the login popup feature is enabled, a global object `auth_dialog` is added to the window object with the following methods:

#### Methods #

**`open()`** - Opens the login popup dialog

**`close()`** - Closes the login popup dialog

#### Usage Example #

```
``
```

### `window.customerAuthState` #

An object that tracks the authentication state of the current user. This object contains two boolean properties:

**`isAuthenticated`** - `true` when the user is logged in, `false` otherwise

**`isGuest`** - `true` when the user is a guest (not logged in), `false` otherwise

#### Important Note #

The `customerAuthState` values are updated automatically after a page reload. However, they **do NOT update dynamically** after a user logs in via the popup. Theme developers must manually update these values after a successful login.

#### Usage Example #

```
``
```

## Events #

### `vitrin:auth:success` Event #

This event is fired immediately after a successful login through the popup. Theme developers can listen to this event to update the DOM, fetch customer data, or simply reload the page.

If you don't need to perform any UI updates, you can **just reload the page**. However, it’s **recommended** to update the UI dynamically without reload for a smoother user experience.

#### Event Usage Example #

```
``
```

💡 **Tip:** You can skip dynamic updates entirely and just use `window.location.reload()` if reloading the page is sufficient for your theme’s flow.

## Redirect Functionality #

The login popup supports redirecting users to a specific page after successful login. This is particularly useful for scenarios like checkout flows or protected pages.

### How Redirect Works #

1 .

**Add `redirect_to`** query parameter - When opening the login popup, add the destination URL as a query parameter.

2 .

**After successful login** - The popup itself **does not redirect automatically**. Theme developers must handle the redirect manually from the `vitrin:auth:success` event.

3 .

**If popup is closed without login** - The popup will **automatically remove the `redirect_to`** parameter from the URL to keep the page clean and prevent unwanted redirects.

### Implementation Example #

```
``
```

### Handling Redirect in `vitrin:auth:success` Event #

After successful login, you must handle the redirect logic manually from the event listener:

```
``
```

## Helper Function Example #

```
``
```

## Custom Styles Integration #

You can customize the look and feel of the **Login Popup** using the Zid SDK Custom Styles system. This allows you to apply your own CSS overrides for specific components without affecting other areas of the store.

## How to Use Custom Styles #

You can define your custom styles globally using the `window.zidCustomStyles` object. The SDK will automatically apply these styles to the corresponding components, ensuring proper scoping and isolation.

### Example #

```
``
```

In the example above, the **component key** for the login popup is clearly shown as:

```
`auth_dialog`
```

You can use this key in your `window.zidCustomStyles` object to apply any style overrides specific to the login popup.

To understand the complete flow of the Custom Styles system — including structure, validation, and advanced usage — please refer to the **Custom Styles Guide for Theme Developers**. (https://docs.zid.sa/custom-styles-guide-1702191m0)

## Best Practices #

1 .

**Check authentication state first** - Always check `window.customerAuthState.isAuthenticated` before attempting to open the login popup.

2 .

**Update `customerAuthState`** manually - Update it in your `vitrin:auth:success` listener if you handle UI updates without reload.

3 .

**Use `window.location.reload()`** if needed - If your flow doesn’t require dynamic UI changes, simply reload the page.

4 .

**Handle redirect manually** - The popup does **not** automatically redirect after login; handle it from the `vitrin:auth:success` event.

5 .

**Redirect cleanup** - The popup automatically removes `redirect_to` when closed without login.

6 .

**Handle fallback scenarios** - Always provide a fallback to traditional login redirects in case `auth_dialog` isn’t available.

## Summary #

Login popup is enabled/disabled via MD settings (`https://dashboard.zid.sa/en-sa/stores/<store_id>/settings/checkout`)

The feature is **enabled by default**

Provides `window.auth_dialog` object with `open()` and `close()` methods

Fires `vitrin:auth:success` event on successful login

Allows manual UI updates or simple reload after login

Supports redirecting via `redirect_to` query parameter

Popup does not redirect automatically after login; developers must handle it manually**

**Popup automatically removes `redirect_to`** if closed without login

Always use optional chaining for safer window checks

Recommended: update UI dynamically without reload for smoother UX

Modified at 2026-07-30 11:49:13

Previous

Addresses as a Popup

Next

Checkout as a Popup
