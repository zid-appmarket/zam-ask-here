---
# Synced from https://docs.zid.sa/input-settings-1379345m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-input-settings
title: "Input Settings"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/input-settings-1379345m0
tags: [from-docs-site, partner-docs]
language: en
---

> Input Settings - Zid Docs
# Input Settings

Each item in settings represents a single input.

**Common fields**

Field Type Description

id string Unique identifier of the setting (e.g., "images", "title").

label object {ar,en} Input label shown to the merchant.

type string Input type (e.g., "text", "textarea", "image", "number", "color", "list").

default any Default value when none is provided.

icon text Optional reference to an icon (e.g. `fal fa-box`).

You can add more types as needed; keep IDs stable to avoid breaking existing themes.

### Text #

```
` {
"type" : "text" ,
"id" : "title" ,
"label" : {
"ar" : "المقدمة" ,
"en" : "Title"
} ,
"default" : <Optional>
} `
```

Output

### TextArea #

```
` {
"type" : "textarea" ,
"id" : "about" ,
"label" : {
"ar" : "نبذة" ,
"en" : "About"
} ,
"default" : <Optional>
} `
```

Output

### RichText #

```
` {
"type" : "richtext" ,
"id" : "about" ,
"label" : {
"ar" : "نبذة" ,
"en" : "About"
} ,
"default" : <Optional>
} `
```

### Number #

```
` {
"type" : "number" ,
"id" : "number_of_branches" ,
"label" : {
"ar" : "رقم الافرع" ,
"en" : "Number of Branches"
} ,
"default" : <Optional>
} `
```

### Color #

```
` {
"type" : "color" ,
"id" : "button_color" ,
"label" : {
"ar" : "لون الزر" ,
"en" : "Button Color"
} ,
"default" : "#000000"
} `
```

Modified at 2026-07-30 11:49:13

Previous

Schema files

Next

Media Settings
