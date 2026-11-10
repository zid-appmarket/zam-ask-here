---
# Synced from https://docs.zid.sa/loyalty-status
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-loyalty-status
title: "Loyalty Program Status"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/loyalty-status
tags: [from-docs-site, partner-docs]
language: en
---

> Loyalty Program Status - Zid Docs
# Loyalty Program Status

GET

https://api.zid.sa/ v1/managers/loyalty-program/loyalty-status

Retrieves information about the overall status (active/inactive) of a store's loyalty program.

🔑Scopes

`loyalty_program.read` - Loyalty Program Read

## Request

Header Params

###

## Responses

🟢 200 OK

application/json

Store loyalty program status retrieved successfully.

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
` curl --location 'https://api.zid.sa/v1/managers/loyalty-program/loyalty-status' \
--header 'Authorization: {{Autherization}}' \
--header 'X-MANAGER-TOKEN: {{Access-Token}}' \
--header 'Accept: application/json' \
--header 'Accept-Language: en' \
--header 'Content-Type: text/plain' \
--data '' `
```

Response Response Example

200 - Example 1

```
` {
"status" : "string" ,
"loyalty_status" : true ,
"message" : {
"type" : "success" ,
"code" : "MSG_POPUP_OK" ,
"name" : "Coupons" ,
"description" : "Coupons created successfully"
}
} `
```

Modified at 2026-03-02 12:31:49

Previous

Loyalty Program

Next

Loyalty Program Details
