---
# Synced from https://docs.zid.sa/export-vouchers
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-export-vouchers
title: "Export Vouchers"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/export-vouchers
tags: [from-docs-site, partner-docs]
language: en
---

> Export Vouchers - Zid Docs
# Export Vouchers

POST

https://api.zid.sa/ v1/products/{product_id}/vouchers/export/

Exports vouchers for a specified product to an Excel file.

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

🟢 200 The response will be an Excel file download.

application/json

Body application/json

###

🟠 415 Unsupported Media Type

🟠 401 Unauthorized

🔴 500 Internal Server error

Request Request Example

Shell

JavaScript

Java

Swift

```
` curl --location 'https://api.zid.sa/v1/products/a1477bb2-72ea-4be9-b2cf-093cefc721bb/vouchers/export/' \
--header 'Authorization: {{Autherization}}' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Store-Id: {{StoreId}}' \
--header 'Role: Manager' \
--header 'Accept-Language: en' \
--header 'Content-Type: application/json' \
--data-raw '{
"email": "test@example.com"
}' `
```

Response Response Example

200 - Example 1

```
` { } `
```

Modified at 2026-02-11 13:12:56

Previous

Import Vouchers

Next

Update Voucher
