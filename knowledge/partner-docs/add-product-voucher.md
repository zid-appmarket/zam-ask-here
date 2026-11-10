---
# Synced from https://docs.zid.sa/add-product-voucher
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-add-product-voucher
title: "Create Voucher"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/add-product-voucher
tags: [from-docs-site, partner-docs]
language: en
---

> Create Voucher - Zid Docs
# Create Voucher

POST

https://api.zid.sa/ v1/products/{product_id}/vouchers/

Adds a new voucher for a specified product.

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

🟠 415 Unsupported Media Type

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
--header 'Accept-Language: en' \
--header 'Content-Type: application/json' \
--data '{
"key": "key-2",
"serial_number": "serial-number-2",
"pin_code": "pin-code-example-2",
"expires_at": "2026-10-10 00:00:00",
"status": "SOLD"
}' `
```

Response Response Example

201 - Success

```
` {
"id" : "3663992f-989e-4056-9a71-02a9109ec7fa" ,
"product_id" : "a1477bb2-72ea-4be9-b2cf-093cefc721bb" ,
"status" : "AVAILABLE" ,
"order" : null ,
"serial_number" : "serial-number-1" ,
"key" : "key-1" ,
"pin_code" : "pin-code-example" ,
"expires_at" : "2026-10-10T00:00:00Z" ,
"updated_at" : "2026-02-11T12:39:55.597191Z" ,
"created_at" : "2026-02-11T12:39:55.597152Z"
} `
```

Modified at 2026-02-11 12:43:33

Previous

Order Vouchers

Next

Import Vouchers
