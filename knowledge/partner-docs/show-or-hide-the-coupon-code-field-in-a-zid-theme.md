---
# Synced from https://docs.zid.sa/show-or-hide-the-coupon-code-field-in-a-zid-theme-2283520m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-show-or-hide-the-coupon-code-field-in-a-zid-theme
title: "Show or Hide the Coupon Code Field in a Zid Theme"
product: theme_market
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/show-or-hide-the-coupon-code-field-in-a-zid-theme-2283520m0
tags: [from-docs-site, partner-docs]
language: en
---

> Show or Hide the Coupon Code Field in a Zid Theme - Zid Docs
# Show or Hide the Coupon Code Field in a Zid Theme

Use the `is_coupon_form_enabled` store setting to control whether the coupon code section appears in your Zid storefront theme.

When the value is `false`, your theme must not render any coupon-related interface. When the value is `true`, `null`, or missing, the coupon section must remain visible.

## Quick implementation #

Wrap the complete coupon section with this condition:

```
`{% set coupon_form_enabled = store.settings.checkout.is_coupon_form_enabled != false %}

{% if coupon_form_enabled %}
<div data-coupon-section>
{# Coupon input, apply button, applied coupon details, and remove button #}
</div>
{% endif %}`
```

That is the only change required to control the coupon section’s visibility.

No new JavaScript is required. However, existing JavaScript must handle cases where coupon elements are not rendered.

## Coupon form setting #

The setting is available in the theme’s store settings:

```
`store.settings.checkout.is_coupon_form_enabled`
```

Value Required theme behavior

`false` Do not render the coupon section

`true` Render the coupon section

`null` Render the coupon section

Missing Render the coupon section

Use `!= false` instead of a standard truthy check so the coupon section remains visible when the setting is `null` or unavailable.

```
`{% set coupon_form_enabled = store.settings.checkout.is_coupon_form_enabled != false %}`
```

Do not use:

```
`{% if store.settings.checkout.is_coupon_form_enabled %}`
```

A direct truthy check may incorrectly hide the coupon form when the value is `null` or missing.

## How merchants configure the coupon field #

Merchants can control the coupon code field from their Zid dashboard:

1 .

Open **Settings**.

2 .

Select **Checkout Options**.

3 .

Find **Show coupon code field**.

4 .

Turn the switch on or off.

5 .

Save the changes.

The setting is enabled by default.

Store settings may be cached for up to 10 minutes. After saving the setting, the storefront may take up to 10 minutes to reflect the change.

## Hide the complete coupon section #

When `is_coupon_form_enabled` is `false`, do not render any coupon-related interface.

This includes:

Coupon code input

Apply coupon button

Applied coupon code

Coupon discount details within the coupon section

Remove coupon button

Coupon validation messages

Coupon error messages

Do not hide only the input while leaving other coupon elements visible.

Example:

```
`{% set coupon_form_enabled = store.settings.checkout.is_coupon_form_enabled != false %}

{% if coupon_form_enabled %}
<section class="cart-coupon" data-coupon-section>
<label for="coupon-code">
Coupon code
</label>

<input
id="coupon-code"
name="coupon_code"
type="text"
data-coupon-input
>

<button type="button" data-apply-coupon>
Apply
</button>

{% if cart.coupon %}
<div data-applied-coupon>
<span>{{ cart.coupon.code }}</span>

<button type="button" data-remove-coupon>
Remove
</button>
</div>
{% endif %}
</section>
{% endif %}`
```

## Do not hide the coupon section with CSS #

Use a Jinja condition so the coupon HTML is not generated when the setting is disabled.

Do not use:

```
`<div
class="cart-coupon {% if store.settings.checkout.is_coupon_form_enabled == false %}hidden{% endif %}"
>
...
</div>`
```

Do not use:

```
``
```

Use:

```
`{% set coupon_form_enabled = store.settings.checkout.is_coupon_form_enabled != false %}

{% if coupon_form_enabled %}
<div class="cart-coupon">
...
</div>
{% endif %}`
```

Server-side conditional rendering prevents hidden coupon controls from remaining in the page HTML.

## Check existing coupon JavaScript #

No JavaScript is needed to read the setting or control the coupon section’s visibility.

However, existing theme scripts may assume that coupon elements are always available. Add a null check before accessing an element or attaching an event listener.

Do not use:

```
``
```

Use:

```
``
```

You can also stop coupon-related initialization when the complete section is unavailable:

```
``
```

## Update every coupon location #

Apply the condition everywhere your theme displays coupon functionality.

Depending on your theme, this may include:

Cart page

Cart drawer

Mini cart

Checkout popup

Mobile cart layout

Custom cart components

Any custom template that displays coupon information

Updating only the main cart page is not sufficient when another storefront component also contains a coupon form.

## Complete implementation example #

```
`{% set coupon_form_enabled = store.settings.checkout.is_coupon_form_enabled != false %}

{% if coupon_form_enabled %}
<section class="cart-coupon" data-coupon-section>
{% if cart.coupon %}
<div class="cart-coupon__applied" data-applied-coupon>
<span>
Applied coupon: {{ cart.coupon.code }}
</span>

<button
type="button"
data-remove-coupon
>
Remove coupon
</button>
</div>
{% else %}
<div class="cart-coupon__form">
<label for="coupon-code">
Coupon code
</label>

<input
id="coupon-code"
name="coupon_code"
type="text"
autocomplete="off"
data-coupon-input
>

<button
type="button"
data-apply-coupon
>
Apply coupon
</button>

<div
role="alert"
aria-live="polite"
data-coupon-message
></div>
</div>
{% endif %}
</section>
{% endif %}`
```

Adapt the markup and cart properties to match your theme’s existing coupon implementation.

## Test your implementation #

Test every cart surface before publishing the theme update.

### Setting enabled #

When `is_coupon_form_enabled` is `true`, confirm that:

The coupon form is rendered.

Customers can enter a coupon code.

The apply button works.

Applied coupon details are visible.

The remove coupon button works.

Coupon-related JavaScript runs without errors.

### Setting disabled #

When `is_coupon_form_enabled` is `false`, confirm that:

The coupon section is not present in the HTML.

The coupon input is not rendered.

The apply button is not rendered.

Applied coupon details are not rendered.

The remove coupon button is not rendered.

Coupon messages are not rendered.

The browser console contains no coupon-related errors.

### Setting unavailable #

When the value is `null` or the property is missing, confirm that:

The coupon section remains visible.

Existing coupon behavior continues to work.

### Multiple cart surfaces #

Confirm that the setting works consistently across:

Desktop cart

Mobile cart

Cart drawer

Mini cart

Checkout popup

Custom cart components

## Troubleshooting #

### The merchant disabled the setting, but the coupon form is still visible #

Store settings may be cached for up to 10 minutes.

Wait up to 10 minutes, refresh the storefront, and test again.

Also verify that:

The merchant saved the setting.

The theme reads `store.settings.checkout.is_coupon_form_enabled`.

The condition wraps the complete coupon section.

Another template or component is not rendering a separate coupon form.

### The coupon form disappeared even though the merchant did not disable it #

Check whether the theme uses a direct truthy condition:

```
`{% if store.settings.checkout.is_coupon_form_enabled %}`
```

Replace it with:

```
`{% set coupon_form_enabled = store.settings.checkout.is_coupon_form_enabled != false %}`
```

The form should be hidden only when the setting is explicitly `false`.

### JavaScript errors appear when the coupon form is disabled #

Your JavaScript may be accessing coupon elements without checking whether they exist.

Use a guard condition:

```
``
```

### The coupon form is hidden on one page but visible elsewhere #

Search the theme for every coupon input, apply button, remove button, and applied coupon label.

Apply the setting to every component that renders coupon functionality.

## Frequently asked questions #

### How do I hide the coupon field in a Zid theme? #

Read `store.settings.checkout.is_coupon_form_enabled` and wrap the complete coupon section in a Jinja `if` block.

```
`{% set coupon_form_enabled = store.settings.checkout.is_coupon_form_enabled != false %}

{% if coupon_form_enabled %}
{# Complete coupon section #}
{% endif %}`
```

### Should I use `if is_coupon_form_enabled`? #

No. Use `is_coupon_form_enabled != false`.

This keeps the coupon section visible when the value is `true`, `null`, or missing.

### Should I hide the coupon form using CSS? #

No. Use server-side conditional rendering so the coupon HTML is not generated.

### Do I need to update my JavaScript? #

You do not need JavaScript to control the setting. However, existing JavaScript must check whether coupon elements exist before accessing them.

### Should I hide an already-applied coupon? #

Yes. When the setting is `false`, hide the complete coupon area, including the applied coupon label and remove button.

### How long does the setting take to update? #

The storefront may take up to 10 minutes to reflect the saved setting because store settings are cached.

### Does this setting disable coupon APIs? #

This guide covers the visibility of the coupon interface in the storefront theme. It does not describe or change coupon API behavior.

## Implementation checklist #

Before publishing your theme update, confirm that:

The theme reads `store.settings.checkout.is_coupon_form_enabled`.

Only an explicit `false` value hides the coupon section.

The complete coupon section is wrapped in the condition.

The section is not hidden using CSS.

Existing JavaScript handles missing coupon elements.

Every cart and checkout surface has been updated.

The implementation works for `true`, `false`, `null`, and a missing value.

The storefront has been retested after the cache period.

## Summary #

Use the following condition around every coupon section in your Zid theme:

```
`{% set coupon_form_enabled = store.settings.checkout.is_coupon_form_enabled != false %}

{% if coupon_form_enabled %}
{# Complete coupon section #}
{% endif %}`
```

Hide the complete coupon interface only when the setting is explicitly `false`. Keep it visible when the value is `true`, `null`, or missing.

Modified at 2026-08-04 09:37:54

Previous

Display Product Options as Colors or Images

Next

New Gifting Experience
