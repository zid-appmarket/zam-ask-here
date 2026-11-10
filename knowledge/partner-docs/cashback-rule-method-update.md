---
# Synced from https://docs.zid.sa/cashback-rule-method-update
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-cashback-rule-method-update
title: "Update Cashback Rule"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/cashback-rule-method-update
tags: [from-docs-site, partner-docs]
language: en
---

> Update Cashback Rule - Zid Docs
# Update Cashback Rule

POST

https://api.zid.sa/ v1/managers/loyalty-program/points-collection/update

Updates the configuration of a cashback rule within a store's loyalty program.

🔑Scopes

`loyalty_program.read_write` - Loyalty Program Read & Write

## Request

Header Params

###

Body Params multipart/form-data

###

## Responses

🟢 200 OK

application/json

The cashback rule method status is updated successfully.

Body application/json

###

🟠 400 Bad Request

🟠 401 Unauthorized

🟠 422 Unprocessable Entity

🔴 500 Internal Server error

Request Request Example

Shell

JavaScript

Java

Swift

```
` curl --location 'https://api.zid.sa/v1/managers/loyalty-program/points-collection/update' \
--header 'Authorization: {{Autherization}}' \
--header 'X-Manager-Token: {{Access-Token}}' \
--header 'Accept: application/json' \
--header 'Accept-Language: en' \
--form 'ruleId=""' \
--form 'config[money]=""' \
--form 'config[points]=""' `
```

Response Response Example

200 - Example 1

```
` {
"status" : { } ,
"data" : {
"status" : true ,
"message" : "Points collection updated successfully" ,
"is_cashback_enabled" : false ,
"points_collection_methods_list" : [
{
"id" : "b1e3ca5d-2a89-4993-89bf-0f31a4b70b00" ,
"external_id" : "pos" ,
"store_id" : "3dfc16e6-ad19-4126-9c2a-5e4a7fb73051" ,
"points_rewarded" : 1 ,
"amount_to_spend" : 100 ,
"available_to" : null ,
"is_active" : false ,
"created_at" : "2023-12-28T10:32:13.000000Z" ,
"updated_at" : "2023-08-28T10:32:13.000000Z" ,
"deleted_at" : null
}
]
} ,
"message" : {
"type" : "string" ,
"code" : "MSG_POPUP_OK" ,
"name" : "Points collection" ,
"description" : "Points collection updated successfully"
}
} `
```

Modified at 2026-08-11 09:14:16

Previous

Set Points Expiration Rules

Next

Create Points Redemption Method
