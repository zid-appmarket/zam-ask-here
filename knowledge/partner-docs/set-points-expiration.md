---
# Synced from https://docs.zid.sa/set-points-expiration
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-set-points-expiration
title: "Set Points Expiration Rules"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/set-points-expiration
tags: [from-docs-site, partner-docs]
language: en
---

> Set Points Expiration Rules - Zid Docs
# Set Points Expiration Rules

POST

https://api.zid.sa/ v1/managers/loyalty-program/points-expiration

Sets the expiration period for loyalty points within a store's program.

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

The cashback rule method is updated successfully.

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
` curl --location 'https://api.zid.sa/v1/managers/loyalty-program/points-expiration' \
--header 'Authorization: {{Autherization}}' \
--header 'X-Manager-Token: {{Access-Token}}' \
--header 'Accept: application/json' \
--header 'Accept-Language: en' \
--form 'days="5"' `
```

Response Response Example

200 - Success

```
` {
"status" : "object" ,
"points_expiry_period" : 5 ,
"message" : {
"type" : "object" ,
"code" : "MSG_POPUP_OK" ,
"name" : "Points expiration" ,
"description" : "Points expiration updated successfully"
}
} `
```

Modified at 2026-08-11 09:16:13

Previous

Activate Loyalty Program

Next

Update Cashback Rule
