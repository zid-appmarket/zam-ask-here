---
# Synced from https://docs.zid.sa/set-custom-product-order
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-set-custom-product-order
title: "Set Manual Product Order"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/set-custom-product-order
tags: [from-docs-site, partner-docs]
language: en
---

> Set Manual Product Order - Zid Docs
# Set Manual Product Order

POST

https://api.zid.sa/ v1/products/ordering/

Sets a custom ordering of products by accepting an ordered list of product IDs. This manual sorting can also be applied to a specific category when the category ID is passed in the body.

🔑Scopes

`products.read_write` - Products Read & Write

## Request

Header Params

###

Body Params application/json

###

Examples

## Responses

🟢 200 Products Sorted Successfully in te given category

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
` curl --location 'https://api.zid.sa/v1/products/ordering/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Store-Id: {{StoreId}}' \
--header 'Content-Type: application/json' \
--data '{
"products": [
"d22fb4a6-cbcf-464c-8877-6cbf3df52056",
"d22fb4a6-cbcf-46g5-8877-6c367f52053"
],
"category": 0
}' `
```

Response Response Example

200 - Example 1

```
` { } `
```

Modified at 2026-02-15 16:16:23

Previous

Product Sorting

Next

Reset Manual Product Order
