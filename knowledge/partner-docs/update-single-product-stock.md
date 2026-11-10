---
# Synced from https://docs.zid.sa/update-single-product-stock
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-update-single-product-stock
title: "Update Product Stock"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/update-single-product-stock
tags: [from-docs-site, partner-docs]
language: en
---

> Update Product Stock - Zid Docs
# Update Product Stock

PATCH

https://api.zid.sa/ v1/products/{product_id}/stocks/{stock_id}/

Update a single product stock by its unique ID. It is not recommended when handling lots of stocks.

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

🟢 200 Successful operation. Returns the updated product stock.

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
` curl --location --request PATCH 'https://api.zid.sa/v1/products/96d0f5c3-1958-4a31-8b03-7014c2070630/stocks/0abacb3a-6a43-474d-b1c9-097e95824117/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Store-Id: {{StoreId}}' \
--header 'Accept-Language: en' \
--header 'Content-Type: application/json' \
--data '{
"available_quantity": 5,
"is_infinite": false
}' `
```

Response Response Example

200 - Example 1

```
` {
"product_id" : "string" ,
"location" : "string" ,
"quantity" : 0 ,
"is_infinite" : true
} `
```

Modified at 2026-02-16 06:57:50

Previous

Create Product Stock

Next

Bulk Update Product Stock Records
