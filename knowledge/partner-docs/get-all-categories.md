---
# Synced from https://docs.zid.sa/get-all-categories
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-get-all-categories
title: "List Categories"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/get-all-categories
tags: [from-docs-site, partner-docs]
language: en
---

> List Categories - Zid Docs
# List Categories

GET

https://api.zid.sa/ v1/managers/store/categories

Fetches all the available categories for a certain store, including details such as their names, status, SEO information, and the number of products they contain. It supports returning both detailed and minimal category information depending on the request parameters.

🔑Scopes

`products.read` - Products Read

## Request

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
` curl --location 'https://api.zid.sa/v1/managers/store/categories' \
--header 'Authorization: {{Autherization}}' \
--header 'X-Manager-Token: {{Access-Token}}' \
--header 'Accept-Language: en' `
```

Response Response Example

200 - Success

```
{
"status": "object",
"categories": [
{
"id": 1473477,
"uuid": "8cc71774-bf3e-4383-9778-64d50d965dc7",
"name": "test sub",
"slug": "تصنيف-فرعي",
"SEO_category_title": "test sub",
"SEO_category_description": "Sub category 1",
"names": {
"en": "test sub",
"ar": "تصنيف فرعي"
},
"description": null,
"url": "https://osama.zid.store/categories/1473477/تصنيف-فرعي",
"image": null,
"image_full_size": null,
"img_alt_text": "",
"products_count": 1,
"sub_categories": [],
"parent_id": null,
"flat_name": "test sub",
"is_published": false,
"metafields": [
{
"id": "2cf0cf26-d468-452a-9492-2fe5970c3cd8",
"name": {
"ar": "لون",
"en": "Color"
},
"slug": "Color-1",
"data_type": "text",
"display_order": 3,
"structure_definition": null,
"value": null
},
{
"id": "6579510a-0ce0-4f83-b53f-e3abe9c0f0d5",
"name": {
"ar": null,
"en": "g gg"
},
"slug": "g-gg",
"data_type": "text",
"display_order": 2,
"structure_definition": null,
"value": null
},
{
"id": "ff173ea4-429c-40f0-a6a0-8e29e655ea83",
"name": {
"ar": null,
"en": "date"
},
"slug": "date",
"data_type": "date",
"display_order": 1,
"structure_definition": null,
"value": null
}
]
},
{
"id": 1473476,
"uuid": "a0fb3f4a-3e16-40ec-ba50-e6fccd2ff6f6",
"name": "Electronics",
"slug": "إلكترونيات",
"SEO_category_title": "Electronics",
"SEO_category_description": "Devices and gadgets including mobiles, accessories, and smart technology.",
"names": {
"en": "Electronics",
"ar": "إلكترونيات"
},
"description": null,
"url": "https://osama.zid.store/categories/1473476/إلكترونيات",
"image": null,
"image_full_size": null,
"img_alt_text": "",
"products_count": 1,
"sub_categories": [],
"parent_id": null,
"flat_name": "Electronics",
"is_published": true,
"metafields": [
{
"id": "2cf0cf26-d468-452a-9492-2fe5970c3cd8",
"name": {
"ar": "لون",
"en": "Color"
},
"slug": "Color-1",
"data_type": "text",
"display_order": 3,
"structure_definition": null,
"value": null
},
{
"id": "6579510a-0ce0-4f83-b53f-e3abe9c0f0d5",
"name": {
"ar": null,
"en": "g gg"
},
"slug": "g-gg",
"data_type": "text",
"display_order": 2,
"structure_definition": null,
"value": null
},
{
"id": "ff173ea4-429c-40f0-a6a0-8e29e655ea83",
"name": {
"ar": null,
"en": "date"
},
"slug": "date",
"data_type": "date",
"display_order": 1,
"structure_definition": null,
"value": null
}
]
},
{
"id": 1400850,
"uuid": "f298454b-d271-4971-9500-fe58494034c8",
"name": "ANNIVERSARY",
"slug": "anniversary",
"SEO_category_title": "ANNIVERSARY",
"SEO_category_description": "",
"names": {
"en": "ANNIVERSARY",
"ar": "ANNIVERSARY"
},
"description": null,
"url": "https://osama.zid.store/categories/1400850/anniversary",
"image": null,
"image_full_size": null,
"img_alt_text": "",
"products_count": 17,
"sub_categories": [],
"parent_id": null,
"fla
```

Modified at 2026-08-11 09:20:32

Previous

Product Categories

Next

View Category
