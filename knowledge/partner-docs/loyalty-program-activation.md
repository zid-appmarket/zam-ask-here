---
# Synced from https://docs.zid.sa/loyalty-program-activation
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-loyalty-program-activation
title: "Activate Loyalty Program"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/loyalty-program-activation
tags: [from-docs-site, partner-docs]
language: en
---

> Activate Loyalty Program - Zid Docs
# Activate Loyalty Program

POST

https://api.zid.sa/ v1/managers/loyalty-program/activation

Activates a loyalty program for a store.

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

The Loyalty program is activated successfully.

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
` curl --location 'https://api.zid.sa/v1/managers/loyalty-program/activation' \
--header 'Authorization: {{Autherization}}' \
--header 'X-Manager-Token: {{Access-Token}}' \
--header 'Accept: application/json' \
--header 'Accept-Language: en' \
--form 'activate="1"' `
```

Response Response Example

200 - Example 1

```
` {
"status" : "string" ,
"loyalty_program" : {
"status" : true ,
"activated" : true ,
"message" : "Loyalty Program activation successfully"
} ,
"message" : {
"type" : "success" ,
"code" : "MSG_POPUP_OK" ,
"name" : "Coupons" ,
"description" : "Coupons created successfully"
}
} `
```

Modified at 2026-08-11 08:54:01

Previous

Customer Points History

Next

Set Points Expiration Rules
