---
# Synced from https://docs.zid.sa/delete-points-redemption-method
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-delete-points-redemption-method
title: "Delete Points Redemption Method"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/delete-points-redemption-method
tags: [from-docs-site, partner-docs]
language: en
---

> Delete Points Redemption Method - Zid Docs
# Delete Points Redemption Method

POST

https://api.zid.sa/ v1/managers/loyalty-program/points-redemption/delete

Deletes a specific redemption method from a store's loyalty program.

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

The redemption method is deleted successfully.

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
` curl --location 'https://api.zid.sa/v1/managers/loyalty-program/points-redemption/delete' \
--header 'Authorization: {{Autherization}}' \
--header 'X-Manager-Token: {{Access-Token}}' \
--header 'Accept: application/json' \
--header 'Accept-Language: en' \
--form 'ruleId="4890974d-d474-4d08-99a4-a42b856ea71a"' `
```

Response Response Example

200 - Success

```
` {
"status" : "object" ,
"points_redemption" : {
"status" : true ,
"message" : "Point redemption method deleted successfully"
} ,
"message" : {
"type" : "object" ,
"code" : "MSG_POPUP_OK" ,
"name" : "Points redemption" ,
"description" : "Point redemption method deleted successfully"
}
} `
```

Modified at 2026-08-11 09:17:26

Previous

Update Points Redemption Method

Next

Adjust Customer Points
