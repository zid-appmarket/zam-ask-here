---
# Synced from https://docs.zid.sa/addresses-as-a-popup-1706785m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-addresses-as-a-popup
title: "Addresses as a Popup"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/addresses-as-a-popup-1706785m0
tags: [from-docs-site, partner-docs]
language: en
---

> Addresses as a Popup - Zid Docs
# Addresses as a Popup

## Overview #

The address dialog feature allows users to add or edit their shipping addresses without leaving the current page. When enabled, it provides a modal dialog for address management, creating a smoother and more seamless user experience.

## Enabling the Feature #

The address dialog feature is enabled by including the template in your theme. There are no dashboard settings required.

### How to Enable #

To enable the address dialog in your theme, include the following template:

```
`{% include "vitrin:account/address_dialog.jinja" %}`
```

**Best Practice:** Include this template **only on pages that contain the address section in the customer profile**, such as the account address management page. Avoid including it globally in the main layout file, as it is not needed across all pages.

## Global API Objects #

### `window.address_dialog` #

When the address dialog template is included, a global object `address_dialog` is added to the `window` object with the following methods:

### Methods #

**open(data?)** – Opens the address dialog.

Without data → Opens in "Add New Address" mode

With `{ addressId: number }` → Opens in "Edit Address" mode with the specified address

**close()** – Closes the address dialog

### Usage Examples #

```
``
```

## Events #

### `vitrin:address:submitted` Event #

This event is fired immediately after a successful address submission (add or edit) through the dialog. Theme developers can listen to this event to update the DOM, refresh the address list, or reload the page.

**Event Detail Structure:**

```
``
```

**Event Usage Example:**

```
``
```

💡 **Tip:** You can skip dynamic updates entirely and just use `window.location.reload()` if reloading the page is sufficient for your theme's flow.

## Custom Styles Integration #

You can customize the look and feel of the Address Dialog using the Zid SDK Custom Styles system. This allows you to apply your own CSS overrides for specific components without affecting other areas of the store.

### How to Use Custom Styles #

```
``
```

The component key for the Address Dialog is `address_dialog`. Use this key to apply scoped style overrides.

To understand the complete flow of the Custom Styles system — including structure, validation, and advanced usage — please refer to the **Custom Styles Guide for Theme Developers**. (https://docs.zid.sa/custom-styles-guide-1702191m0)

## Best Practices #

Include the template **only in the address section pages**, not globally.

Always use **optional chaining** (`window?.address_dialog?.open`).

Listen to **`vitrin:address:submitted`** event for updates.

Support both **add** and **edit** modes.

Prefer **dynamic updates** for better UX.

## API Reference Summary #

Method Parameters Description

`window.address_dialog.open()` none Opens dialog in "Add New Address" mode

`window.address_dialog.open(data)` `{ addressId: number }` Opens dialog in "Edit Address" mode

`window.address_dialog.close()` none Closes the address dialog

### Events #

Event Name Detail Structure Description

`vitrin:address:submitted` `{ addressId?: number, isEditMode: boolean }` Fired after successful address submission

## Summary #

Enabled by including `{% include "vitrin:account/address_dialog.jinja" %}`

Should be included **only in customer profile pages that have the address section**

No dashboard settings required

Provides global `window.address_dialog` object

Supports **Add** and **Edit** address modes

Fires **`vitrin:address:submitted`** event on success

Safe with **optional chaining**

Fully customizable via `window.zidCustomStyles.address_dialog`

Modified at 2026-07-30 11:49:13

Previous

Gift Card as a Popup

Next

Login as a Popup
