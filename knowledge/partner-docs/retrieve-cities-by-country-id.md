---
# Synced from https://docs.zid.sa/retrieve-cities-by-country-id
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-retrieve-cities-by-country-id
title: "List Cities for Country"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/retrieve-cities-by-country-id
tags: [from-docs-site, partner-docs]
language: en
---

> List Cities for Country - Zid Docs
# List Cities for Country

GET

https://api.zid.sa/ v1/managers/cities/by-country-id/{country_id}

Retrieve a list of cities for a specific country where the store operates or delivers. The list includes each city's unique ID, name, and country details. Note that a city can be labeled as 'Other', represented by an 'أخرى' or 'Other' in the 'name' field, which typically signifies a location outside of the predefined list of cities.

🔑Scopes

`countries_cities.read` - Countries & Cities Read

## Request

Path Params

###

Header Params

###

## Responses

🟢 200 OK

application/json

A list of cities is returned

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
` curl --location 'https://api.zid.sa/v1/managers/cities/by-country-id/184' \
--header 'Authorization: {{Autherization}}' \
--header 'X-Manager-Token: {{Access-Token}}' \
--header 'Accept-Language: en' `
```

Response Response Example

200 - Example 1

```
` {
"status" : "object" ,
"cities" : [
{
"id" : 1 ,
"national_id" : 3 ,
"name" : "Other" ,
"priority" : 10 ,
"country_id" : 184 ,
"country_name" : "السعودية" ,
"country_code" : "SA" ,
"ar_name" : "الرياض" ,
"en_name" : "Riyadh"
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

List Countries

Next

Blogs
