---
# Synced from https://docs.zid.sa/products-settings-1379348m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-products-settings
title: "Products Settings"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/products-settings-1379348m0
tags: [from-docs-site, partner-docs]
language: en
---

> Products Settings - Zid Docs
# Products Settings

**Common fields**

Field Type Description

id string Unique identifier of the setting (e.g., "images", "title").

label object {ar,en} Input label shown to the merchant.

type string Input type (e.g., "text", "textarea", "image", "number", "color", "list").

default any Default value when none is provided.

icon text Optional reference to an icon (e.g. `fal fa-box`).

### Products #

```
` {
"type" : "products" ,
"id" : "products" ,
"label" : {
"ar" : "اختر قائمة المنتجات" ,
"en" : "Select category products"
}
} `
```

### Product #

### Category #

```
` {
"type" : "category" ,
"id" : "category" ,
"label" : {
"ar" : "اختر التصنيف" ,
"en" : "Select category"
}
} `
```

### Category Products #

```
` {
"type" : "category_products" ,
"id" : "category_products_1" ,
"label" : {
"ar" : "اختر منتجات التصنيف" ,
"en" : "Select category products"
}
} `
```

Modified at 2026-07-30 11:49:13

Previous

Form Controls Settings

Next

Additional Settings
