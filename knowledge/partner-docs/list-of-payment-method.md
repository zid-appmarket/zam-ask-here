---
# Synced from https://docs.zid.sa/list-of-payment-method
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-list-of-payment-method
title: "List Payment Methods"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/list-of-payment-method
tags: [from-docs-site, partner-docs]
language: en
---

> List Payment Methods - Zid Docs
# List Payment Methods

GET

https://api.zid.sa/ v1/managers/store/payment-methods

**Note:** This API does not return the active payment methods configured in POS.

🔑Scopes

`account.read` - Account Read

## Request

Header Params

###

## Responses

🟢 200 OK

application/json

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
` curl --location 'https://api.zid.sa/v1/managers/store/payment-methods' \
--header 'Authorization: {{Autherization}}' \
--header 'X-Manager-Token: {{Access-Token}}' \
--header 'Accept-Language: en' `
```

Response Response Example

200 - Example 1

```
` {
"code" : "string" ,
"payload" : [
{
"enabled" : true ,
"code" : "string" ,
"fees" : 0 ,
"fees_string" : "string" ,
"type" : "string" ,
"name" : "string" ,
"icons" : [
"https://zid-testing.s3.eu-west-1.amazonaws.com/static/cod.png"
] ,
"id" : 0
}
]
} `
```

Modified at 2026-01-30 20:55:20

Previous

Retrieve VAT Settings

Next

List Store Operating Countries
