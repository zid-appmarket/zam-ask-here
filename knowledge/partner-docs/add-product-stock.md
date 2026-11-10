---
# Synced from https://docs.zid.sa/add-product-stock
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-add-product-stock
title: "Create Product Stock"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/add-product-stock
tags: [from-docs-site, partner-docs]
language: en
---

> Create Product Stock - Zid Docs
# Create Product Stock

POST

https://api.zid.sa/ v1/products/{product_id}/stocks/

Add a new product stock for a specific product.

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

🟢 201 Created

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
` curl --location 'https://api.zid.sa/v1/products/96d0f5c3-1958-4a31-8b03-7014c2070630/stocks/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Store-Id: {{StoreId}}' \
--header 'Accept-Language: en' \
--header 'Content-Type: application/json' \
--data '{
"location": "982a2aac-b9af-44e3-a3e0-51d2faa6b7c2",
"available_quantity": 3,
"is_infinite": false
}' `
```

Response Response Example

201 - Success

```
` {
"id" : "0abacb3a-6a43-474d-b1c9-097e95824117" ,
"location" : "982a2aac-b9af-44e3-a3e0-51d2faa6b7c2" ,
"available_quantity" : 3 ,
"is_infinite" : false
} `
```

Modified at 2026-02-16 06:56:08

Previous

List Product Stock Records

Next

Update Product Stock
