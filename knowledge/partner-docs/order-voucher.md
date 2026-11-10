---
# Synced from https://docs.zid.sa/order-voucher
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-order-voucher
title: "Order Vouchers"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/order-voucher
tags: [from-docs-site, partner-docs]
language: en
---

> Order Vouchers - Zid Docs
# Order Vouchers

GET

https://api.zid.sa/ v1/order-vouchers/{order_id}/

Retrieves the voucher details for a specified order.

🔑Scopes

`products.read` - Products Read

## Request

Path Params

###

Query Params

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

Request Request Example

Shell

JavaScript

Java

Swift

```
` curl --location 'https://api.zid.sa/v1/order-vouchers/64855100/?page=1&page_size=15' \
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
"status" : "RESERVED" ,
"order" : 64855100 ,
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

Modified at 2026-02-11 12:41:41

Previous

List Vouchers

Next

Create Voucher
