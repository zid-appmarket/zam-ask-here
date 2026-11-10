---
# Synced from https://docs.zid.sa/list-of-customers
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-list-of-customers
title: "List Customers"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/list-of-customers
tags: [from-docs-site, partner-docs]
language: en
---

> List Customers - Zid Docs
# List Customers

GET

https://api.zid.sa/ v1/managers/store/customers

Retrieves a paginated list of store customers, including customer details, order counts, and summary metadata, with support for advanced filtering, sorting, and array based queries.

🔑Scopes

`third_customers_read` - Customers Read

## Request

Query Params

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
` curl --location 'https://api.zid.sa/v1/managers/store/customers?after=0&per_page=15' \
--header 'Authorization: {{Autherization}}' \
--header 'X-Manager-Token: {{Access-Token}}' \
--header 'Accept-Language: en' `
```

Response Response Example

200 - Example 1

```
` {
"status" : "string" ,
"customers" : [
{
"id" : 0 ,
"name" : "string" ,
"email" : "string" ,
"mobile" : "string" ,
"gender" : "string" ,
"birth_date" : "string" ,
"verified" : true ,
"is_active" : true ,
"is_cod_enabled" : true ,
"type" : "string" ,
"business_name" : "string" ,
"tax_number" : "string" ,
"commercial_registration" : "string" ,
"source" : "string" ,
"points" : 0 ,
"order_total_payments" : "string" ,
"last_order_date" : "string" ,
"created_at" : "string" ,
"updated_at" : "string" ,
"city" : {
"name" : "Other" ,
"id" : 1 ,
"national_id" : 3 ,
"priority" : 10 ,
"country_id" : 184 ,
"country_name" : "السعودية" ,
"country_code" : "SA" ,
"ar_name" : "الرياض" ,
"en_name" : "Riyadh"
} ,
"nickname" : "string" ,
"pivotEmail" : "string" ,
"pivotMobile" : "string" ,
"order_counts" : 0
}
] ,
"grand_total" : 0 ,
"total_customers_count" : 0 ,
"active_customers_count" : 0 ,
"inactive_customers_count" : 0 ,
"next_cursor" : 0 ,
"message" : {
"type" : "success" ,
"code" : "MSG_POPUP_OK" ,
"name" : "Coupons" ,
"description" : "Coupons created successfully"
}
} `
```

Modified at 2026-05-18 16:34:34

Previous

Customer Portal Ticket Detail

Next

View Customer
