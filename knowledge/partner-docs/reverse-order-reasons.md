---
# Synced from https://docs.zid.sa/reverse-order-reasons
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-reverse-order-reasons
title: "List Reverse Reasons"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/reverse-order-reasons
tags: [from-docs-site, partner-docs]
language: en
---

> List Reverse Reasons - Zid Docs
# List Reverse Reasons

GET

https://api.zid.sa/ v1/managers/store/reverse-orders/reasons

Retrieves a list of order reverse reasons for the store.

🔑Scopes

`orders.read` - Orders Read

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
` curl --location 'https://api.zid.sa/v1/managers/store/reverse-orders/reasons' \
--header 'Authorization: {{Autherization}}' \
--header 'X-MANAGER-TOKEN: {{Access-Token}}' \
--header 'Accept-Language: en' `
```

Response Response Example

200 - Success

```
` {
"status" : "object" ,
"order_reverse_reasons" : [
{
"id" : "1e99df02-fe5f-4bff-b305-2b32731f50bc" ,
"name" : "new reason"
} ,
{
"id" : "3a7112b2-6bda-431a-bfdf-62942610f308" ,
"name" : "hhfjhdfh"
} ,
{
"id" : "3f4d9d0f-a502-4d8a-bee4-fef91be8b185" ,
"name" : "test"
} ,
{
"id" : "460d7f3b-35e6-4c82-b8eb-2ec3627e4708" ,
"name" : "dndgn"
} ,
{
"id" : "658d82bd-f828-49f1-8a39-a77e207a0fa6" ,
"name" : "hello"
} ,
{
"id" : "8b46f9b5-d88f-4687-8df5-f91c7d0373ad" ,
"name" : "Does not match the description"
} ,
{
"id" : "ebcfd40a-7c2f-4ed4-b30f-3fd142388ad7" ,
"name" : "Customer canceled"
} ,
{
"id" : "f569c42a-c134-492b-a2f0-c0a561b02cf5" ,
"name" : "Product was broken"
}
] ,
"message" : {
"type" : "object" ,
"code" : null ,
"name" : null ,
"description" : null
}
} `
```

Modified at 2026-02-09 07:40:05

Previous

Add Reverse Order Reasons

Next

Calculate Reverse Totals
