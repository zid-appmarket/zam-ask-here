---
# Synced from https://docs.zid.sa/form-controls-settings-1379347m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-form-controls-settings
title: "Form Controls Settings"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/form-controls-settings-1379347m0
tags: [from-docs-site, partner-docs]
language: en
---

> Form Controls Settings - Zid Docs
# Form Controls Settings

**Common fields**

Field Type Description

id string Unique identifier of the setting (e.g., "images", "title").

label object {ar,en} Input label shown to the merchant.

type string Input type (e.g., "text", "textarea", "image", "number", "color", "list").

default any Default value when none is provided.

icon text Optional reference to an icon (e.g. `fal fa-box`).

### Checkbox #

```
` {
"type" : "checkbox" ,
"id" : "hide_dots" ,
"label" : {
"ar" : "إخفاء النقاط" ,
"en" : "Hide dots"
} ,
"default" : true
} `
```

### Checkboxes #

**Extra fields**

Field Type Description

options list[object] Options to be displayed for the checkboxes. Each option needs to have a `value` and `label`.

```
` {
"type" : "checkboxes" ,
"id" : "options" ,
"label" : {
"ar" : "خيارات" ,
"en" : "Options"
} ,
"options" : [
{
"value" : "hide_search_bar" ,
"label" : {
"ar" : "إخفاء شريط البحث" ,
"en" : "Hide search bar"
}
} ,
{
"value" : "hide_language" ,
"label" : {
"ar" : "إخفاء اللغة" ,
"en" : "Hide language"
}
}
]
} `
```

### Radio #

**Extra fields**

Field Type Description

options list[object] Options to be displayed for the radio. Each option needs to have a `value` and `label`.

```
` {
"type" : "radio" ,
"id" : "logo_aligment" ,
"label" : {
"ar" : "محاذاة الشعار" ,
"en" : "Logo alignment"
} ,
"options" : [
{
"value" : "left" ,
"label" : {
"ar" : "يسار" ,
"en" : "Left"
}
} ,
{
"value" : "centered" ,
"label" : {
"ar" : "وسط" ,
"en" : "Centered"
}
}
] ,
"default" : "left"
} `
```

### Range #

**Extra fields**

Field Type Description

min int Minimum value for the range.

max int Maximum value for the range.

step int Increment/decrement value.

unit str Unit of measurement to show (e.g. "px", "seconds", etc.).

```
` {
"type" : "range" ,
"id" : "font_size" ,
"label" : {
"ar" : "حجم النص" ,
"en" : "Font size"
} ,
"min" : 12 ,
"max" : 24 ,
"step" : 1 ,
"unit" : "px" ,
"default" : 16
} `
```

### Select #

**Extra fields**

Field Type Description

options list[object] Options to be displayed for the radio. Each option needs to have a `value` and

```
` {
"type" : "select" ,
"id" : "fonts" ,
"label" : {
"ar" : "اسم الخط" ,
"en" : "Font name"
} ,
"options" : [
{
"value" : "Changa" ,
"label" : {
"ar" : "Changa" ,
"en" : "Changa"
}
} ,
{
"value" : "Cairo" ,
"label" : {
"ar" : "Cairo" ,
"en" : "Cairo"
}
}
]
} `
```

Modified at 2026-07-30 11:49:13

Previous

Media Settings

Next

Products Settings
