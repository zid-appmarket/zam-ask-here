---
# Synced from https://docs.zid.sa/toggle-redemption-method-status
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-toggle-redemption-method-status
title: "Update Redemption Method Status"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/toggle-redemption-method-status
tags: [from-docs-site, partner-docs]
language: en
---

> Update Redemption Method Status - Zid Docs
# Update Redemption Method Status

PUT

https://api.zid.sa/ v1/managers/loyalty-program/points-redemption/update-status

Enables or disables a specific redemption method within a store's loyalty program.

🔑Scopes

`loyalty_program.read_write` - Loyalty Program Read & Write

## Request

Header Params

###

Body Params application/json

###

Examples

## Responses

🟢 200 OK

application/json

Redemption method status toggled successfully.

Body application/json

###

🟠 404 Record Not Found

🟠 401 Unauthorized

🔴 500 Internal Server error

🟠 403 Forbidden

🟠 400 Bad Request

Request Request Example

Shell

JavaScript

Java

Swift

```
` curl --location --request PUT 'https://api.zid.sa/v1/managers/loyalty-program/points-redemption/update-status' \
--header 'Authorization: {{Autherization}}' \
--header 'Store-ID: {{StoreId}}' \
--header 'Content-Type: application/json' \
--data '{
"redemptionRuleUuid": "c5ed20de-fe99-40b8-9fee-36b05b1a8436",
"status": true
}' `
```

Response Response Example

200 - Example 1

```
` {
"status" : "string" ,
"redemption_rule" : {
"id" : "7ba3e0ac-0ca9-4eeb-9026-01ec09ea3f6a" ,
"external_id" : "15505" ,
"store_id" : "8b1cf62d-d05c-4405-949d-5c1cdcc64987" ,
"name" : "35" ,
"points_to_redeem" : 35 ,
"rule_type" : "percentage_discount_settings" ,
"reward" : {
"discount_value" : 3
} ,
"conditions" : null ,
"is_active" : true ,
"created_at" : "2023-04-03T09:17:47.000000Z" ,
"updated_at" : "2023-08-03T09:17:47.000000Z" ,
"deleted_at" : null
} ,
"message" : {
"type" : "string" ,
"code" : "MSG_POPUP_OK" ,
"name" : "Points redemption" ,
"description" : "Update point redemption method status"
}
} `
```

Modified at 2026-09-10 08:58:25

Previous

Adjust Customer Points

Next

Loyalty Program Analytics
