---
# Synced from https://docs.zid.sa/update-product-voucher
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-update-product-voucher
title: "Update Voucher"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/update-product-voucher
tags: [from-docs-site, partner-docs]
language: en
---

> Update Voucher - Zid Docs
# Update Voucher

PATCH

https://api.zid.sa/ v1/products/{product_id}/vouchers/{voucher_id}

Updates an existing voucher for a specified product.

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
` curl --location --request PATCH 'https://api.zid.sa/v1/products/a1477bb2-72ea-4be9-b2cf-093cefc721bb/vouchers/b9a21ac0-0c04-4706-bef9-a05270613092' \
--header 'Authorization: {{Autherization}}' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Store-Id: {{StoreId}}' \
--header 'Role: Manager' \
--header 'Accept-Language: en' \
--header 'Content-Type: application/json' \
--data '{
"key": "key-2",
"serial_number": "serial--2",
"pin_code": "pin-code--2",
"expires_at": "2026-10-10 00:00:00",
"status": "AVAAILABLE"
}' `
```

Response Response Example

200 - Example 1

```
` {
"vouchers" : [
{
"id" : "\"0d6dc296-f757-4f11-83b2-6d5fddb6ad85\"" ,
"key" : "\"ABC123XYZ\"" ,
"pin_code" : "string" ,
"status" : "\"AVAILABLE\"" ,
"serial_number" : "\"SN123456\"" ,
"expires_at" : "\"2024-12-31\"" ,
"created_at" : "\"2024-01-01T12:00:00Z\"" ,
"updated_at" : "\"2024-01-01T12:00:00Z\""
}
]
} `
```

Modified at 2026-02-11 13:42:26

Previous

Export Vouchers

Next

Remove Voucher
