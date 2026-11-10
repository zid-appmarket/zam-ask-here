---
# Synced from https://docs.zid.sa/adjust-customer-points
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-adjust-customer-points
title: "Adjust Customer Points"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/adjust-customer-points
tags: [from-docs-site, partner-docs]
language: en
---

> Adjust Customer Points - Zid Docs
# Adjust Customer Points

POST

https://api.zid.sa/ v1/managers/loyalty-program/customers/adjust-customer-points

Allows manual adjustments to a customer's loyalty points balance.

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

The customer points balance is adjusted successfully.

Body application/json

###

🟠 401 Unauthorized

🟠 422 Unprocessable Entity

🔴 500 Internal Server error

Request Request Example

Shell

JavaScript

Java

Swift

```
` curl --location 'https://api.zid.sa/v1/managers/loyalty-program/customers/adjust-customer-points' \
--header 'Authorization: {{Autherization}}' \
--header 'X-Manager-Token: {{Access-Token}}' \
--header 'Accept: application/json' \
--header 'Accept-Language: en' \
--form 'customerId="37"' \
--form 'direction="+"' \
--form 'points="5"' \
--form 'reason="gift"' `
```

Response Response Example

200 - Success

```
` {
"status" : "object" ,
"data" : {
"date" : "2026-03-02T13:26:14.000000Z" ,
"reason" : "gift" ,
"points" : 5 ,
"direction" : "+" ,
"type" : "ManualAccumulation" ,
"order_number" : null ,
"expiry_date" : null ,
"point_status" : "Active" ,
"collection_method" : "Manually added points"
} ,
"message" : {
"type" : "object" ,
"code" : "MSG_POPUP_OK" ,
"name" : "Adjust customer points" ,
"description" : "Points updated successfully"
}
} `
```

Modified at 2026-08-11 08:54:45

Previous

Delete Points Redemption Method

Next

Update Redemption Method Status
