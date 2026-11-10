---
# Synced from https://docs.zid.sa/product-setting
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-product-setting
title: "List Product Settings"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/product-setting
tags: [from-docs-site, partner-docs]
language: en
---

> List Product Settings - Zid Docs
# List Product Settings

GET

https://api.zid.sa/ v1/products/settings

The product setting endpoint allows merchants to retrieve the current product settings status from their dashboard. These settings control various aspects of how products are displayed, including search features, related products, and sold product counts. The endpoint helps merchants manage and fine-tune the visibility and order of products in their stores.

🔑Scopes

`products.read` - Products Read

## Request

Header Params

###

## Responses

🟢 200 Success

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
` curl --location 'https://api.zid.sa/v1/products/settings' \
--header 'x-manager-token: {{Access-Token}}' \
--header 'Authorization: {{Autherization}}' \
--header 'store-id: {{StoreId}}' \
--header 'Role: Manager' \
--header 'Accept-Language: en' `
```

Response Response Example

200 - Success

```
` {
"settings" : {
"extended_search_support" : false ,
"related_products_status" : false ,
"related_products_count" : 8 ,
"sold_products_count_status" : false ,
"min_sold_products_count" : 1 ,
"default_products_ordering" : "-is_infinite,-quantity" ,
"has_products_filtration" : false ,
"is_wishlist_enabled" : true ,
"is_quick_donation_enabled" : false
}
} `
```

Modified at 2026-02-08 14:01:54

Previous

View Product

Next

Update Product
