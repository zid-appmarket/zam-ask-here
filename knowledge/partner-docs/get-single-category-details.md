---
# Synced from https://docs.zid.sa/get-single-category-details
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-get-single-category-details
title: "View Category"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/get-single-category-details
tags: [from-docs-site, partner-docs]
language: en
---

> View Category - Zid Docs
# View Category

GET

https://api.zid.sa/ v1/managers/store/categories/{category_id}/view

Retrieves detailed information about a specific category, including its attributes, status, and associated products or subcategories, based on the provided category ID.

🔑Scopes

`products.read` - Products Read

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
` curl --location 'https://api.zid.sa/v1/managers/store/categories/1473477/view' \
--header 'Authorization: {{Autherization}}' \
--header 'X-Manager-Token: {{Access-Token}}' \
--header 'Accept-Language: en' `
```

Response Response Example

200 - Success

```
` {
"status" : "object" ,
"categories" : {
"id" : 1473477 ,
"name" : "test sub" ,
"uuid" : "8cc71774-bf3e-4383-9778-64d50d965dc7" ,
"slug" : "تصنيف-فرعي" ,
"SEO_category_title" : "test sub" ,
"SEO_category_description" : "Sub category 1" ,
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
"products_count" : 1 ,
"sub_categories" : [ ] ,
"parent_id" : null ,
"flat_name" : "test sub" ,
"is_published" : false ,
"metafields" : [
{
"id" : "2cf0cf26-d468-452a-9492-2fe5970c3cd8" ,
"name" : {
"ar" : "لون" ,
"en" : "Color"
} ,
"slug" : "Color-1" ,
"data_type" : "text" ,
"display_order" : 3 ,
"structure_definition" : null ,
"value" : null
} ,
{
"id" : "6579510a-0ce0-4f83-b53f-e3abe9c0f0d5" ,
"name" : {
"ar" : null ,
"en" : "g gg"
} ,
"slug" : "g-gg" ,
"data_type" : "text" ,
"display_order" : 2 ,
"structure_definition" : null ,
"value" : null
} ,
{
"id" : "ff173ea4-429c-40f0-a6a0-8e29e655ea83" ,
"name" : {
"ar" : null ,
"en" : "date"
} ,
"slug" : "date" ,
"data_type" : "date" ,
"display_order" : 1 ,
"structure_definition" : null ,
"value" : null
}
]
} ,
"message" : {
"type" : "object" ,
"code" : null ,
"name" : null ,
"description" : null
}
} `
```

Modified at 2026-08-11 09:21:09

Previous

List Categories

Next

Create Category
