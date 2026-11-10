---
# Synced from https://docs.zid.sa/update-a-store-category
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-update-a-store-category
title: "Update Category"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/update-a-store-category
tags: [from-docs-site, partner-docs]
language: en
---

> Update Category - Zid Docs
# Update Category

POST

https://api.zid.sa/ v1/managers/store/categories/{category_id}/update

Use this endpoint to update only one store category

🔑Scopes

`products.read_write` - Products Read & Write

## Request

Path Params

###

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
` curl --location 'https://api.zid.sa/v1/managers/store/categories/1486524/update' \
--header 'Authorization: {{Autherization}}' \
--header 'X-Manager-Token: {{Access-Token}}' \
--header 'Accept-Language: en' \
--form 'name[ar]="Hello World"' \
--form 'name[en]="Hello World"' \
--form 'description[ar]="Hello World"' \
--form 'description[en]="Hello World"' \
--form '_method="put"' `
```

Response Response Example

200 - Success

```
` {
"status" : "object" ,
"category" : {
"id" : 1486524 ,
"name" : "Hello World" ,
"uuid" : "d20ff9ed-90c0-4733-9657-6b4e671d7809" ,
"slug" : "hello-world" ,
"SEO_category_title" : "Hello World" ,
"SEO_category_description" : "Hello World" ,
"i18n_SEO_category_title" : {
"ar" : "Hello World" ,
"en" : "Hello World"
} ,
"i18n_SEO_category_description" : {
"ar" : "Hello World" ,
"en" : "Hello World"
} ,
"names" : {
"en" : "Hello World" ,
"ar" : "Hello World"
} ,
"description" : {
"en" : "Hello World" ,
"ar" : "Hello World"
} ,
"url" : "https://osama.zid.store/categories/1486524/hello-world" ,
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
"flat_name" : "Hello World" ,
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

Modified at 2026-02-15 09:23:33

Previous

Create Subcategory

Next

Assign Product to Category
