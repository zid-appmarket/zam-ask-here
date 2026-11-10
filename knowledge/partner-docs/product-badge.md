---
# Synced from https://docs.zid.sa/product-badge
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-product-badge
title: "List Badges"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/product-badge
tags: [from-docs-site, partner-docs]
language: en
---

> List Badges - Zid Docs
# List Badges

GET

https://api.zid.sa/ v1/badges/

This endpoint retrieves a list of all predefined store badges available to the merchant.

🔑Scopes

`products.read` - Products Read

## Request

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
` curl --location 'https://api.zid.sa/v1/badges/' \
--header 'Authorization: {{Autherization}}' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Store-Id: {{StoreId}}' \
--header 'Role: Manager' \
--header 'Accept-Language: en' \
--header 'Content-Type: application/json' \
--data '' `
```

Response Response Example

200 - Success

```
` {
"data" : [
{
"body" : {
"ar" : "خصم {discount_percent}" ,
"en" : "{discount_percent} Discount"
} ,
"is_example" : true ,
"icon" : {
"code" : "discount_percent"
}
} ,
{
"body" : {
"ar" : "خصم 10%" ,
"en" : "10% discount"
} ,
"is_example" : false ,
"icon" : null
} ,
{
"body" : {
"ar" : "خصم 10.00%" ,
"en" : "10.00% Discount"
} ,
"is_example" : false ,
"icon" : null
} ,
{
"body" : {
"ar" : "مخفض" ,
"en" : "Discounted"
} ,
"is_example" : false ,
"icon" : null
} ,
{
"body" : {
"ar" : "خصم {discount_value}" ,
"en" : "{discount_value} Discount"
} ,
"is_example" : false ,
"icon" : null
} ,
{
"body" : {
"ar" : "شحن مجاني" ,
"en" : "Free Shipping"
} ,
"is_example" : false ,
"icon" : null
} ,
{
"body" : {
"ar" : "كمية محدودة" ,
"en" : "Limited Quantity"
} ,
"is_example" : false ,
"icon" : null
} ,
{
"body" : {
"ar" : "منتج مميز" ,
"en" : "Special Product"
} ,
"is_example" : false ,
"icon" : null
} ,
{
"body" : {
"ar" : "يباع سريعًا" ,
"en" : "Selling fast"
} ,
"is_example" : false ,
"icon" : null
}
]
} `
```

Modified at 2026-02-15 11:41:17

Previous

Product Badge

Next

Product Attributes
