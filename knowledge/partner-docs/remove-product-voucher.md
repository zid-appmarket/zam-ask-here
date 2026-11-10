---
# Synced from https://docs.zid.sa/remove-product-voucher
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-remove-product-voucher
title: "Remove Voucher"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/remove-product-voucher
tags: [from-docs-site, partner-docs]
language: en
---

> Remove Voucher - Zid Docs
# Remove Voucher

DELETE

https://api.zid.sa/ v1/products/{product_id}/vouchers/{voucher_id}/

Deletes a specified voucher for a product.

🔑Scopes

`products.read_write` - Products Read & Write

## Request

Path Params

###

Header Params

###

## Responses

🟢 204 No Content

application/json

Body application/json

###

🟠 404 Not Found

🟠 401 Unauthorized

🔴 500 Internal Server error

🟢 204 No Content

Request Request Example

Shell

JavaScript

Java

Swift

```
` curl --location --request DELETE 'https://api.zid.sa/v1/products/a1477bb2-72ea-4be9-b2cf-093cefc721bb/vouchers/b9a21ac0-0c04-4706-bef9-a05270613092/' \
--header 'Authorization: {{Autherization}}' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Store-Id: {{StoreId}}' \
--header 'Role: Manager' \
--header 'Accept-Language: en' \
--header 'Content-Type: application/json' `
```

Response Response Example

204 - Example 1

```
` { } `
```

Modified at 2026-02-11 13:43:48

Previous

Update Voucher

Next

Product Categories
