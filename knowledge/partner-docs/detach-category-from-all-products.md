---
# Synced from https://docs.zid.sa/detach-category-from-all-products
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-detach-category-from-all-products
title: "Detach Category from All Products"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/detach-category-from-all-products
tags: [from-docs-site, partner-docs]
language: en
---

> Detach Category from All Products - Zid Docs
# Detach Category from All Products

DELETE

https://api.zid.sa/ v1/managers/store/categories/{category_id}/products/delete

Detach a specified category from all products in the store. This essentially

disassociates the category from all products it was linked to, but does not delete the category itself.

🔑Scopes

`products.read_write` - Products Read & Write

## Request

Path Params

###

Header Params

###

## Responses

🟢 200 OK

application/json

Body application/json

###

🟠 401 Unauthorized

🔴 500 Internal Server error

Request Request Example

Shell

JavaScript

Java

Swift

```
` curl --location --request DELETE 'https://api.zid.sa/v1/managers/store/categories/1473477/products/delete' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Authorization: {{Autherization}}' \
--header 'Store-Id: {{StoreId}}' \
--header 'Role: Manager' `
```

Response Response Example

200 - Success

```
` {
"status" : "object" ,
"category" : {
"id" : 1473477 ,
"name" : "تصنيف فرعي" ,
"uuid" : "8cc71774-bf3e-4383-9778-64d50d965dc7" ,
"slug" : "تصنيف-فرعي" ,
"SEO_category_title" : "تصنيف فرعي" ,
"SEO_category_description" : "تصنيف فرعي1" ,
"i18n_SEO_category_title" : {
"ar" : "تصنيف فرعي" ,
"en" : "test sub"
} ,
"i18n_SEO_category_description" : {
"ar" : "تصنيف فرعي1" ,
"en" : "Sub category 1"
} ,
"names" : {
"en" : "test sub" ,
"ar" : "تصنيف فرعي"
} ,
"description" : {
"en" : "Sub category 1" ,
"ar" : "تصنيف فرعي1"
} ,
"url" : "https://osama.zid.store/categories/1473477/تصنيف-فرعي" ,
"image" : null ,
"image_full_size" : null ,
"img_alt_text" : "" ,
"i18n_img_alt_text" : {
"ar" : null
} ,
"cover_image" : null ,
"image_full" : null ,
"products_count" : 0 ,
"sub_categories" : [ ] ,
"parent_id" : null ,
"flat_name" : "تصنيف فرعي" ,
"is_published" : false ,
"metafields" : [ ]
} ,
"message" : {
"type" : "object" ,
"code" : null ,
"name" : null ,
"description" : null
}
} `
```

Modified at 2026-02-15 09:36:24

Previous

Publish Category

Next

Remove Product from Category
