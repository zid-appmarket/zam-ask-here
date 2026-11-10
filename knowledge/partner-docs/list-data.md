---
# Synced from https://docs.zid.sa/list-data
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-list-data
title: "Loyalty Program Details"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/list-data
tags: [from-docs-site, partner-docs]
language: en
---

> Loyalty Program Details - Zid Docs
# Loyalty Program Details

GET

https://api.zid.sa/ v1/managers/loyalty-program/list-data

Retrieves list data relevant to the loyalty program configuration.

🔑Scopes

`loyalty_program.read` - Loyalty Program Read

## Request

Header Params

###

## Responses

🟢 200 OK

application/json

Loyalty program list data is retrieved successfully.

Body application/json

###

🟠 401 Unauthorized

🟠 401 Unauthorized

🔴 500 Internal Server error

Request Request Example

Shell

JavaScript

Java

Swift

```
` curl --location 'https://api.zid.sa/v1/managers/loyalty-program/list-data' \
--header 'Authorization: {{Autherization}}' \
--header 'X-Manager-Token: {{Access-Token}}' \
--header 'Accept: application/json' \
--header 'Accept-Language: en' `
```

Response Response Example

200 - Example 1

```
` {
"status" : "string" ,
"cashback_rules" : [
{
"id" : "b1e3ca5d-2a89-4993-89bf-0f31a4b70b00" ,
"external_id" : "pos" ,
"store_id" : "3dfc16e6-ad19-4126-9c2a-5e4a7fb73051" ,
"points_rewarded" : 1 ,
"amount_to_spend" : 1 ,
"available_to" : {
"tags" : [
"string"
] ,
"level" : {
"levelId" : "string" ,
"levelName" : "string"
}
} ,
"is_active" : false ,
"created_at" : "2023-12-28T10:32:13.000000Z" ,
"updated_at" : "2023-12-28T10:32:13.000000Z" ,
"deleted_at" : null
}
] ,
"redemption_rules" : [
{
"id" : "efc450a4-3f09-4544-bcdd-80ddcbde23c8" ,
"external_id" : "string" ,
"store_id" : "3dfc16e6-ad19-4126-9c2a-5e4a7fb73051" ,
"name" : "3" ,
"points_to_redeem" : 3 ,
"rule_type" : "fixed_rate_settings" ,
"reward" : {
"discount_value" : 1
} ,
"conditions" : null ,
"is_active" : false ,
"created_at" : "2023-10-26T10:59:16.000000Z" ,
"updated_at" : "2023-04-26T10:59:16.000000Z" ,
"deleted_at" : null
}
] ,
"total_earned_points" : 1271060 ,
"total_redemed_points" : 2004 ,
"total_pending_points" : 51419 ,
"total_customers_with_points" : 48 ,
"expiration_peroid" : 5 ,
"is_active" : true ,
"message" : {
"type" : "string" ,
"code" : null ,
"name" : null ,
"description" : null
}
} `
```

Modified at 2026-03-02 12:50:52

Previous

Loyalty Program Status

Next

Loyalty Program Info
