---
# Synced from https://docs.zid.sa/bulk-update-product-stocks
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-bulk-update-product-stocks
title: "Bulk Update Product Stock Records"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/bulk-update-product-stocks
tags: [from-docs-site, partner-docs]
language: en
---

> Bulk Update Product Stock Records - Zid Docs
# Bulk Update Product Stock Records

PATCH

https://api.zid.sa/ v1/products/{product_id}/stocks/

Bulk update product stocks through locations. It is recommended when updating multiple stocks.

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
` curl --location --request PATCH 'https://api.zid.sa/v1/products/96d0f5c3-1958-4a31-8b03-7014c2070630/stocks/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Store-Id: {{StoreId}}' \
--header 'Accept-Language: en' \
--header 'Content-Type: application/json' \
--data '[
{
"location": "8ee590fe-d02d-4c50-9184-f628bb8b115a",
"available_quantity": 10,
"is_infinite": false
},
{
"location": "982a2aac-b9af-44e3-a3e0-51d2faa6b7c2",
"available_quantity": 20,
"is_infinite": false
}
]' `
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

Modified at 2026-02-16 07:07:13

Previous

Update Product Stock

Next

Product Questions & Answers
