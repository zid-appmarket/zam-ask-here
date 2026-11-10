---
# Synced from https://docs.zid.sa/migrating-twig-settings-schema-1379351m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-migrating-twig-settings-schema
title: "Migrating twig settings schema"
product: theme_market
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/migrating-twig-settings-schema-1379351m0
tags: [from-docs-site, partner-docs]
language: en
---

> Migrating twig settings schema - Zid Docs
# Migrating twig settings schema

When migrating old twig settings schema to the new vitrin schema, a few breaking changes need to be taken into consideration

## Reference the template path for each section #

This is necessary so that the section can be rendered correctly, example:

```
` "sections" : [
{
"label" : {
"ar" : "Image Slider" ,
"en" : "Image Slider"
} ,
"template" : "sections/image_slider.jinja" , `
```

## List order #

There is no `“order”: N` key value to handle sorting items, each time the user changes the order of the items in a list (sections, images, etc.) the whole list shall be updated to preserve the new order.

## `noLabel` is deprecated #

Like in this instance

```
` "hide_dots" : {
"type" : "checkbox" ,
"label" : {
"ar" : " " ,
"en" : " "
} ,
"option" : {
"ar" : "إخفاء النقاط" ,
"en" : "Hide dots"
} ,
"noLabel" : true
} `
```

Would now become:

```
` {
"type" : "checkbox" ,
"id" : "hide_dots" ,
"label" : {
"ar" : "إخفاء النقاط" ,
"en" : "Hide dots"
}
} `
```

If you want a setting to not have a label, you can simply keep the label values as empty strings in the label object.

Modified at 2026-07-30 11:49:13

Previous

Conditional Visibility

Next

localization (jinja v. twig)
