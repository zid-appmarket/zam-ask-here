---
# Synced from https://docs.zid.sa/import-vouchers
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-import-vouchers
title: "Import Vouchers"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/import-vouchers
tags: [from-docs-site, partner-docs]
language: en
---

> Import Vouchers - Zid Docs
# Import Vouchers

POST

https://api.zid.sa/ v1/products/{product_id}/vouchers/import/

Imports multiple vouchers for a specified product from an Excel file.

🔑Scopes

`products.read_write` - Products Read & Write

## Request

Path Params

###

Header Params

###

Body Params multipart/form-data

###

## Responses

🟢 201 Created

This response does not have a body.

🟠 401 Unauthorized

🟠 400 Bad Request

🔴 500 Internal Server error

Request Request Example

Shell

JavaScript

Java

Swift

```
` curl --location 'https://api.zid.sa/v1/products/a1477bb2-72ea-4be9-b2cf-093cefc721bb/vouchers/import/' \
--header 'Authorization: {{Autherization}}' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Store-Id: {{StoreId}}' \
--header 'Role: Manager' \
--header 'Accept-Language: en' \
--form 'file=@"cmMtdXBsb2FkLTE3NzA2MjQ2NjAxNjQtMzA=/product_voucher_template.csv"' `
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

Modified at 2026-02-11 13:11:06

Previous

Create Voucher

Next

Export Vouchers
