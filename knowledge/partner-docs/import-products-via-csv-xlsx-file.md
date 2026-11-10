---
# Synced from https://docs.zid.sa/import-products-via-csv/xlsx-file
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-import-products-via-csv-xlsx-file
title: "Import Products via CSV or xlsx File"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/import-products-via-csv/xlsx-file
tags: [from-docs-site, partner-docs]
language: en
---

> Import Products via CSV or xlsx File - Zid Docs
# Import Products via CSV or xlsx File

POST

https://api.zid.sa/ v1/products/import/

Imports products to the store using a CSV or xlsx file. The endpoint accepts a file, a Dropbox folder link for images, and an optional `delete_old_products` parameter to delete all previous store products upon successful import.

🔑Scopes

`products.read_write` - Products Read & Write

## Request

Header Params

###

Body Params application/x-www-form-urlencoded

###

## Responses

🟢 200 All Products Sent to the Owner Email

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
` curl --location 'https://api.zid.sa/v1/products/import/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Store-Id: {{StoreId}}' \
--header 'Accept-Language: en' \
--data-urlencode 'file=' \
--data-urlencode 'delete_old_products=' \
--data-urlencode 'response_type=json' `
```

Response Response Example

200 - Example 1

```
` { } `
```

Modified at 2026-02-16 06:35:20

Previous

Email All Products to Store Owner

Next

Product Stock
