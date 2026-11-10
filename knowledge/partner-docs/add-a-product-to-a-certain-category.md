---
# Synced from https://docs.zid.sa/add-a-product-to-a-certain-category
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-add-a-product-to-a-certain-category
title: "Assign Product to Category"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/add-a-product-to-a-certain-category
tags: [from-docs-site, partner-docs]
language: en
---

> Assign Product to Category - Zid Docs
# Assign Product to Category

POST

https://api.zid.sa/ v1/products/{product_id}/categories/

Use this endpoint to add a new product to a certain category by specifying the product id and providing the category id in the request body.

🔑Scopes

`products.read_write` - Products Read & Write

## Request

Path Params

###

Header Params

###

Body Params application/json

###

Examples

## Responses

🟢 201 OK

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
` curl --location 'https://api.zid.sa/v1/products/a7ad89d0-03e2-430f-b6e4-0624ef05e571/categories/' \
--header 'Authorization: {{Autherization}}' \
--header 'X-Manager-Token: {{Access-Token}}' \
--header 'Store-Id: {{StoreId}}' \
--header 'Content-Type: application/json' \
--data '{
"id": 1473477
}' `
```

Response Response Example

201 - Success

```
` {
"id" : "1473477" ,
"name" : "test sub" ,
"slug" : "تصنيف-فرعي" ,
"description" : "Sub category 1" ,
"cover_image" : null ,
"image" : null ,
"display_order" : 0 ,
"meta" : {
"childs" : [ ] ,
"parents" : [ ]
}
} `
```

Modified at 2026-02-15 09:28:18

Previous

Update Category

Next

Bulk Assign Products to Category
