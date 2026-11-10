---
# Synced from https://docs.zid.sa/list-product-stocks
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-list-product-stocks
title: "List Product Stock Records"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/list-product-stocks
tags: [from-docs-site, partner-docs]
language: en
---

> List Product Stock Records - Zid Docs
# List Product Stock Records

GET

https://api.zid.sa/ v1/products/{product_id}/stocks/

Retrieve a list of all product stocks for a specific product.

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

Request Request Example

Shell

JavaScript

Java

Swift

```
` curl --location 'https://api.zid.sa/v1/products/96d0f5c3-1958-4a31-8b03-7014c2070630/stocks/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Store-Id: {{StoreId}}' \
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
"id" : "e44bbf6b-c62a-4597-b87f-311fba0e0256" ,
"location" : {
"id" : "8ee590fe-d02d-4c50-9184-f628bb8b115a" ,
"name" : "الرياض - فرع عبد العزيز" ,
"type" : "PHYSICAL" ,
"full_address" : "6137 King Abdul Aziz Branch Rd, An Nafal, Riyadh 13312, Saudi Arabia"
} ,
"available_quantity" : null ,
"is_infinite" : true
}
]
} `
```

Modified at 2026-02-16 06:48:13

Previous

Retrieve Product Stock

Next

Create Product Stock
