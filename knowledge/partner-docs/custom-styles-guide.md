---
# Synced from https://docs.zid.sa/custom-styles-guide-1702191m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-custom-styles-guide
title: "Custom Styles Guide"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/custom-styles-guide-1702191m0
tags: [from-docs-site, partner-docs]
language: en
---

> Custom Styles Guide - Zid Docs
# Custom Styles Guide

## Overview #

The Zid SDK allows you to customize the appearance of SDK components using custom CSS styles. This guide will help you write, test, and troubleshoot custom styles for your Zid store.

## Quick Start #

Add your custom styles to the `custom-styles.js` file:

```
``
```

## How It Works #

### Automatic Scoping #

All your custom styles are **automatically scoped** to their specific component to prevent conflicts with other parts of your store.

**Example:**

```
``
```

This ensures your styles only affect the gift dialog, not other dialogs in your application.

### Component Keys #

Each component has a unique key that you can use in your window.zidCustomStyles object. You can easily find this key from the template component key shown in the Custom Styles section of the template documentation or configuration panel.

## Writing Custom Styles #

### Rule 1: Use Flat Selectors Only #

**Correct:**

```
``
```

**Wrong:**

```
``
```

The SDK uses a flat CSS structure for performance and reliability. Nested selectors cause errors.

### Rule 2: Use camelCase for CSS Properties #

**Correct:**

```
``
```

**Wrong:**

```
``
```

JavaScript object notation requires camelCase property names.

### Rule 3: Start Selectors with Valid CSS Prefixes #

All selectors must start with one of these:

`.` (class selector) → `.my-button`

`#` (ID selector) → `#my-element`

`@` (at-rule) → `@media`, `@keyframes`

`:` (pseudo-class) → `:hover`, `:focus`

**Correct:**

```
``
```

**Wrong:**

```
``
```

### Rule 4: Don't Use Global Selectors #

Avoid global selectors such as:

`body`, `html`, `:root`, `*`

Use specific class selectors instead:

```
``
```

## Using MUI Classes #

When customizing MUI components, you can target classes using this pattern:

**Pattern:**

```
`.Mui[ComponentName]-[slotName]`
```

**Example:**

```
``
```

**Important Note:**

Avoid targeting any dynamically generated MUI classes that contain hashes, such as:

```
`.css-ae2u5c-MuiSlider-thumb`
```

These classes are not stable and may change between builds. Always use the standardized MUI pattern instead.

## Common Errors & Solutions #

### Forbidden Global Selector #

```
`[ZidError] Forbidden selector 'body' - Cannot scope global selectors`
```

**Fix:** Replace global selectors with component-specific ones.

### Nested Selector with `&` #

```
`[ZidError] Nested '&' not allowed. Use flat selectors.`
```

**Fix:** Flatten your selectors.

### Invalid CSS Structure #

```
`[ZidError] Invalid CSS structure at 'root'. Expected object, received string.`
```

**Fix:** Make sure each component key contains an object of selectors.

## Examples #

### Example 1: Modern Auth Dialog #

```
``
```

### Example 2: Minimalist Gift Dialog #

```
``
```

## Testing Your Styles #

1 .

Check the browser console for validation errors.

2 .

Inspect elements using DevTools to confirm applied scoping.

3 .

Test across devices, modes, and languages.

## Summary #

**DO:**

Use flat selectors

Use camelCase properties

Use valid MUI class names

Support responsive design

**DON’T:**

Use nested `&` selectors

Use hashed MUI classes

Use global selectors

Modified at 2026-07-30 11:49:13

Previous

SDK Popups – Integration Guidelines

Next

Gift Card as a Popup
