---
# Synced from https://docs.zid.sa/create-store-category
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-create-store-category
title: "Create Category"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/create-store-category
tags: [from-docs-site, partner-docs]
language: en
---

> Create Category - Zid Docs
# Create Category

POST

https://api.zid.sa/ v1/managers/store/categories/add

Use this endpoint to add a new store category.

🔑Scopes

`products.read` - Products Read

## Request

Header Params

###

Body Params multipart/form-data

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
` curl --location 'https://api.zid.sa/v1/managers/store/categories/add' \
--header 'Authorization: {{Autherization}}' \
--header 'X-Manager-Token: {{Access-Token}}' \
--header 'Accept-Language: en' \
--form 'name[ar]="hello hello"' \
--form 'name[en]="hello hello"' \
--form 'description[ar]="hello hello"' \
--form 'description[en]="hello hello"' `
```

Response Response Example

200 - Success

```
` {
"status" : "object" ,
"category" : {
"id" : 1482383 ,
"name" : "test121212124" ,
"uuid" : "6d439dd1-6411-444d-babf-5fdb946fd90d" ,
"slug" : "test121212124" ,
"SEO_category_title" : "test121212124" ,
"SEO_category_description" : "test121212124" ,
"i18n_SEO_category_title" : {
"ar" : "test121212124" ,
"en" : "test121212124"
} ,
"i18n_SEO_category_description" : {
"ar" : "test121212124" ,
"en" : "test121212124"
} ,
"names" : {
"en" : "test121212124" ,
"ar" : "test121212124"
} ,
"description" : {
"en" : "test121212124" ,
"ar" : "test121212124"
} ,
"url" : "https://osama.zid.store/categories/1482383/test121212124" ,
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
"flat_name" : "test121212124" ,
"is_published" : true ,
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

Modified at 2026-08-11 09:21:47

Previous

View Category

Next

Create Subcategory
