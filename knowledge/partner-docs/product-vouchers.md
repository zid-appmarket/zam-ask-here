---
# Synced from https://docs.zid.sa/product-vouchers
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-product-vouchers
title: "List Vouchers"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/product-vouchers
tags: [from-docs-site, partner-docs]
language: en
---

> List Vouchers - Zid Docs
# List Vouchers

GET

https://api.zid.sa/ v1/products/{product_id}/vouchers/

Retrieves all vouchers for a specified product.

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

🟠 400 Bad Request

Request Request Example

Shell

JavaScript

Java

Swift

```
` curl --location 'https://api.zid.sa/v1/products/a1477bb2-72ea-4be9-b2cf-093cefc721bb/vouchers/' \
--header 'Authorization: {{Autherization}}' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Store-Id: {{StoreId}}' \
--header 'Role: Manager' \
--header 'Accept-Language: en' `
```

Response Response Example

200 - Success

```
` {
"count" : 1 ,
"next" : null ,
"previous" : null ,
"results" : [
{
"id" : "0b470326-d2b1-4d96-8ee1-ea03a50dfd83" ,
"product_id" : "a1477bb2-72ea-4be9-b2cf-093cefc721bb" ,
"status" : "AVAILABLE" ,
"order" : null ,
"serial_number" : "Z.12345" ,
"key" : "FX00001" ,
"pin_code" : "12345" ,
"expires_at" : "2026-10-10T03:00:00Z" ,
"updated_at" : "2026-02-11T10:25:33.999016Z" ,
"created_at" : "2026-02-11T10:25:33.998979Z"
}
]
} `
```

Modified at 2026-02-11 12:07:59

Previous

Digital Vouchers

Next

Order Vouchers
