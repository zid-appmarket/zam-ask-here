---
# Synced from https://docs.zid.sa/retrieve-store-operating-countries
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-retrieve-store-operating-countries
title: "List Store Operating Countries"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/retrieve-store-operating-countries
tags: [from-docs-site, partner-docs]
language: en
---

> List Store Operating Countries - Zid Docs
# List Store Operating Countries

GET

https://api.zid.sa/ v1/managers/countries

Retrieve a list of countries where the store operates. This list includes the country's unique ID, name, ISO codes, and flag image URL.

🔑Scopes

`countries_cities.read` - Countries & Cities Read

## Request

Header Params

###

## Responses

🟢 200 OK

application/json

A list of countries is returned

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
` curl --location 'https://api.zid.sa/v1/managers/countries' \
--header 'Authorization: {{Autherization}}' \
--header 'X-Manager-Token: {{Access-Token}}' \
--header 'Accept-Language: en' `
```

Response Response Example

200 - Example 1

```
` {
"status" : "object" ,
"countries" : [
{
"id" : 184 ,
"name" : "السعودية" ,
"code" : "SA" ,
"country_code" : "SAU" ,
"flag" : "https://media.zid.store/static/sa.svg"
}
] ,
"message" : {
"type" : "success" ,
"code" : "MSG_POPUP_OK" ,
"name" : "Coupons" ,
"description" : "Coupons created successfully"
}
} `
```

Modified at 2026-01-30 20:55:20

Previous

List Payment Methods

Next

OneSignal Store Settings
