---
# Synced from https://docs.zid.sa/add-reverse-order-reasons
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-add-reverse-order-reasons
title: "Add Reverse Order Reasons"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/add-reverse-order-reasons
tags: [from-docs-site, partner-docs]
language: en
---

> Add Reverse Order Reasons - Zid Docs
# Add Reverse Order Reasons

POST

https://api.zid.sa/ v1/managers/store/reverse-orders/reasons

Adds a new reverse order reason.

🔑Scopes

` orders.read_write` - Orders Read & Write

## Request

Header Params

###

Body Params multipart/form-data

###

## Responses

🟢 200 OK

application/json

Body application/json

###

🟠 401 Unauthorized

🔴 500 Internal Server error

🟠 422 Validation errors

Request Request Example

Shell

JavaScript

Java

Swift

```
` curl --location 'https://api.zid.sa/v1/managers/store/reverse-orders/reasons' \
--header 'Authorization: {{Autherization}}' \
--header 'X-MANAGER-TOKEN: {{Access-Token}}' \
--header 'Accept-Language: en' \
--form 'name="Customer not responding"' `
```

Response Response Example

200 - Success

```
` {
"status" : "object" ,
"order_reverse_reason" : {
"id" : "f991919f-a230-407b-83d6-930b46c8303c" ,
"name" : "Customer not responding"
} ,
"message" : {
"type" : "object" ,
"code" : null ,
"name" : null ,
"description" : null
}
} `
```

Modified at 2026-02-09 07:39:39

Previous

Create Reverse Orders Waybill

Next

List Reverse Reasons
