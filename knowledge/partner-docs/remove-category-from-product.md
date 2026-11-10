---
# Synced from https://docs.zid.sa/remove-category-from-product
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-remove-category-from-product
title: "Remove Product from Category"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/remove-category-from-product
tags: [from-docs-site, partner-docs]
language: en
---

> Remove Product from Category - Zid Docs
# Remove Product from Category

DELETE

https://api.zid.sa/ v1/products/{product_id}/categories/{category_id}/

This endpoint removes a specified category from a particular product. This action

does not delete the category itself, but disassociates it from the product.

🔑Scopes

`products.read_write` - Products Read & Write

## Request

Path Params

###

Header Params

###

## Responses

🟢 204 No Content

This response does not have a body.

🟠 401 Unauthorized

🔴 500 Internal Server error

Request Request Example

Shell

JavaScript

Java

Swift

```
` curl --location --request DELETE 'https://api.zid.sa/v1/products/a7ad89d0-03e2-430f-b6e4-0624ef05e571/categories/1473477/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Authorization: {{Autherization}}' \
--header 'Store-Id: 3' \
--header 'Role: Manager' `
```

Response Response Example

401 - Example 1

```
` {
"status" : "error" ,
"message" : {
"type" : "error" ,
"code" : "ERROR_SESSION_MISSING" ,
"name" : "Sorry" ,
"description" : "Please login first."
}
} `
```

Modified at 2026-02-15 09:39:20

Previous

Detach Category from All Products

Next

Set Categories Nesting
