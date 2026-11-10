---
# Synced from https://docs.zid.sa/update-points-redemption-method
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-update-points-redemption-method
title: "Update Points Redemption Method"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/update-points-redemption-method
tags: [from-docs-site, partner-docs]
language: en
---

> Update Points Redemption Method - Zid Docs
# Update Points Redemption Method

POST

https://api.zid.sa/ v1/managers/loyalty-program/points-redemption/update

Updates the details of an existing redemption method within a store's loyalty program.

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

The redemption method is updated successfully.

Body application/json

###

🟠 404 Record Not Found

🟠 401 Unauthorized

🔴 500 Internal Server error

Request Request Example

Shell

JavaScript

Java

Swift

```
` curl --location 'https://api.zid.sa/v1/managers/loyalty-program/points-redemption/update' \
--header 'Authorization: {{Autherization}}' \
--header 'X-Manager-Token: {{Access-Token}}' \
--header 'Accept: application/json' \
--header 'Accept-Language: en' \
--form 'ruleId="4890974d-d474-4d08-99a4-a42b856ea71a"' \
--form 'config[type]="percentage_discount_settings"' \
--form 'config[discount]="5"' \
--form 'config[points]="5"' `
```

Response Response Example

200 - Success

```
` {
"status" : "object" ,
"points_redemption" : {
"status" : true ,
"message" : "Point redemption method updated successfully"
} ,
"message" : {
"type" : "object" ,
"code" : "MSG_POPUP_OK" ,
"name" : "Points redemption" ,
"description" : "Point redemption method updated successfully"
}
} `
```

Modified at 2026-08-11 09:18:14

Previous

Create Points Redemption Method

Next

Delete Points Redemption Method
