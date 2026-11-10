---
# Synced from https://docs.zid.sa/region-language-popup-1861342m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-region-language-popup
title: "Region & Language Popup"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/region-language-popup-1861342m0
tags: [from-docs-site, partner-docs]
language: en
---

> Region & Language Popup - Zid Docs
# Region & Language Popup

The **Region & Language popup** allows customers to change the store language, country, and city within a modal dialog, without leaving the current page. This provides a smoother localization experience and ensures content, products, pricing, and delivery options are tailored to the selected region.

## About #

The region popup settings can be managed in the **Merchant Dashboard** on the inventory page:

**Path:** `https://dashboard.zid.sa/en-sa/stores/<store_id>/catalog/inventories`

By default, **Display products in your store based on the customer location** is disabled for all stores. When enabled:

The city selector becomes visible inside the popup.

If **Require customer to select city manually** is checked, the popup will be forced for all customers who haven't selected a city, otherwise a default city in the region that has a shipping option will be selected.

## Theme Usage Examples #

To enable the Region & Language popup in your theme, include the template and script in your `layout.jinja` file:

### `layout.jinja` #

```
`{% include "vitrin:shared/region_settings_dialog.jinja" %}

<script>
window.zidOpenRegionSettingDialog = () => {
region_settings_dialog.open();
}
</script>`
```

Now, you can use `region_settings_dialog` anywhere in your theme.

## Custom Styles Integration #

The popup supports the **Zid Custom Styles system**. You can override specific styles safely without affecting other dialogs.

### How to Use Custom Styles #

```
``
```

The component key for the checkout popup is **`region_settings_dialog`**.

To understand the complete flow of the Custom Styles system — including structure, validation, and advanced usage — please refer to the Custom Styles Guide for Theme Developers. (https://docs.zid.sa/custom-styles-guide-1702191m0)

## Custom Region and language popup #

If you want to create your own UI instead of using `region_settings_dialog`.

Zid provides APIs to replicate the same functionality.

Method Parameters Description

`zid.store.region.countries` none Returns the list of store countries store countries

`zid.store.region.setRegion` { language, city_id, country_code } Changes the store language, country, and city

`zid.store.region.languages` none Returns the store languages

### `countries` API #

The `countries` API returns countries depending on the Display products in your store based on the customer location switch in the inventory page:

**Path:** `https://dashboard.zid.sa/en-sa/stores/<store_id>/catalog/inventories`

Switch OFF: Returns only a list of countries (no cities).

```
``
```

**Response Example:**

```
` [
{
"id" : 184 ,
"name" : "Saudi Arabia" ,
"code" : "SA" ,
"country_code" : "+966" ,
"flag" : "https://zid-testing-907587157081.s3.eu-west-1.amazonaws.com/static/sa.svg" ,
"currency_code" : "SAR" ,
"iso_code_2" : "SA" ,
"iso_code_3" : "SAU" ,
"address_format" : "" ,
"postcode_required" : 0 ,
"names" : {
"en" : "Saudi Arabia" ,
"ar" : "السعودية"
}
}
] `
```

Switch ON: Returns countries with cities included. Default city selections are also provided.

**Response Example:**

```
` {
"countries" : [
{
"id" : 184 ,
"name" : "السعودية" ,
"code" : "SA" ,
"country_code" : null ,
"flag_icon" : "https://zid-testing-907587157081.s3.eu-west-1.amazonaws.com/static/sa.svg" ,
"cities" : [
{
"id" : 1 ,
"name" : "الرياض" ,
"country_code" : "SA"
} ,
{
"id" : 71 ,
"name" : "جدة" ,
"country_code" : "SA"
} ,
{
"id" : 76 ,
"name" : "مكة المكرمة" ,
"country_code" : "SA"
} ,
{
"id" : 24 ,
"name" : "الدمام" ,
"country_code" : "SA"
}
] ,
"flags" : {
"is_sms_enabled" : true
}
}
] ,
"default_cities" : {
"SA" : {
"id" : 1 ,
"name" : "الرياض" ,
"country_code" : "SA"
} ,
"AE" : {
"id" : 125 ,
"name" : "أبوظبي" ,
"country_code" : "AE"
} ,
"OM" : {
"id" : 193 ,
"name" : "مسقط" ,
"country_code" : "OM"
} ,
"BH" : {
"id" : 141 ,
"name" : "المنامة" ,
"country_code" : "BH"
}
}
} `
```

### `setRegion` API #

Use this API to change the store language, country, and city. `country_code` and `language` are required; `city_id` is optional.

```
``
```

### `languages` API #

Provides a list of store languages.

```
``
```

**Response Example:**

```
` [
{
"id" : 1 ,
"name" : "English" ,
"code" : "en" ,
"direction" : "ltr"
} ,
{
"id" : 2 ,
"name" : "العربيّة" ,
"code" : "ar" ,
"direction" : "rtl"
}
] `
```

## Best Practices #

Include the template in the `layout.jinja`.

Always use **optional chaining** when interacting with the API.

## API Reference Summary #

Method Parameters Description

`window.region_settings_dialog.open()` none Opens popup

`window.region_settings_dialog.close()` none Closes the popup

`zid.store.region.countries` none Returns the list of store countries store countries

`zid.store.region.setRegion` { language, city_id, country_code } Changes the store language, country, and city

`zid.store.region.languages` none Returns the store languages

## Summary #

Enabled by including `{% include "vitrin:shared/region_settings_dialog.jinja" %}`

Exposes `window.region_settings_dialog` global object

Fully style-able through `window.zidCustomStyles.region_settings_dialog`

Optional chaining recommended

Modified at 2026-07-30 11:49:13

Previous

Apple Pay Quick Checkout

Next

Dynamic Bundle Products
