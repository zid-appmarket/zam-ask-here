---
# Synced from https://docs.zid.sa/add-points-redemption-method
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-add-points-redemption-method
title: "Create Points Redemption Method"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/add-points-redemption-method
tags: [from-docs-site, partner-docs]
language: en
---

> Create Points Redemption Method - Zid Docs
# Create Points Redemption Method

POST

https://api.zid.sa/ v1/managers/loyalty-program/points-redemption

Creates a new redemption method (e.g., gift certificate) for a store's loyalty program.

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

The redemption method is created successfully.

Body application/json

###

🟠 401 Unauthorized

🔴 500 Internal Server error

🟢 200 OK

Request Request Example

Shell

JavaScript

Java

Swift

```
` curl --location 'https://api.zid.sa/v1/managers/loyalty-program/points-redemption' \
--header 'Authorization: {{Autherization}}' \
--header 'X-Manager-Token: {{Access-Token}}' \
--header 'Accept: application/json' \
--header 'Accept-Language: en' \
--form 'config[type]="fixed_rate_settings"' \
--form 'config[discount]="1"' \
--form 'config[points]="1"' `
```

Response Response Example

200 - Success

```
` {
"status" : "object" ,
"points_redemption" : {
"status" : true ,
"message" : "Point redemption method added successfully" ,
"redemptionRule" : {
"store_id" : "d297fb8b-c322-412e-a2f4-ffa96dc57022" ,
"external_id" : "202603021311282861" ,
"name" : "1" ,
"points_to_redeem" : 1 ,
"rule_type" : "fixed_rate_settings" ,
"reward" : {
"discount_value" : 1
} ,
"is_active" : true ,
"id" : "4890974d-d474-4d08-99a4-a42b856ea71a" ,
"updated_at" : "2026-03-02T13:11:28.000000Z" ,
"created_at" : "2026-03-02T13:11:28.000000Z"
}
} ,
"message" : {
"type" : "object" ,
"code" : "MSG_POPUP_OK" ,
"name" : "Points redemption" ,
"description" : "Point redemption method added successfully"
}
} `
```

Modified at 2026-08-11 09:16:59

Previous

Update Cashback Rule

Next

Update Points Redemption Method
