---
# Synced from https://docs.zid.sa/countries-list
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-countries-list
title: "List Countries"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/countries-list
tags: [from-docs-site, partner-docs]
language: en
---

> List Countries - Zid Docs
# List Countries

GET

https://api.zid.sa/ v1/settings/countries

The endpoint returns all countries' names, codes, and IDs, and is not specific to any particular store's operations or merchant's activated countries.

🔑Scopes

`countries_cities.read` - Countries & Cities Read

## Request

Header Params

###

## Responses

🟢 200 OK

application/json

OK

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
` curl --location 'https://api.zid.sa/v1/settings/countries' \
--header 'Accept: application/json' \
--header 'Authorization: {{Autherization}}' \
--header 'Accept-Language: en' `
```

Response Response Example

200 - Example 1

```
` {
"status" : "string" ,
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

Countries and Cities

Next

List Cities for Country
