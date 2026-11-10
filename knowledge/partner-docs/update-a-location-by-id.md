---
# Synced from https://docs.zid.sa/update-a-location-by-id
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-update-a-location-by-id
title: "Update Location"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/update-a-location-by-id
tags: [from-docs-site, partner-docs]
language: en
---

> Update Location - Zid Docs
# Update Location

PATCH

https://api.zid.sa/ v1/locations/{location_id}/

Updates the details of a specified location.

🔑Scopes

`inventories.read_write `- Inventories Read & Write

## Request

Path Params

###

Header Params

###

Body Params application/json

###

Examples

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
` curl --location --request PATCH 'https://api.zid.sa/v1/locations/056e7f7f-85e2-42fc-a630-3a7ba839231e/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Authorization: {{Autherization}}' \
--header 'Store-Id: {{StoreId}}' \
--header 'Role: Manager' \
--header 'Accept-Language: en' \
--header 'Content-Type: application/json' \
--data '{
"name": "test 3333",
"city": 1,
"coordinates": {
"latitude": "23.2532",
"longitude": "23.3232"
},
"full_address": "RHHB4094, 4094 Al Aflaj, 7377، حي الواحة، Riyadh 12442, Saudi Arabia",
"is_default": false,
"is_private": true,
"is_enabled": false,
"channels": [
"catalog"
],
"short_address": "RHHB4094"
}' `
```

Response Response Example

200 - Example 1

```
` {
"id" : "string" ,
"name" : {
"ar" : "string" ,
"en" : "string"
} ,
"city" : {
"id" : 0 ,
"name" : "string" ,
"ar_name" : "string" ,
"country" : {
"id" : 0 ,
"name" : "string" ,
"ar_name" : "string" ,
"iso_code_2" : "string" ,
"iso_code_3" : "string" ,
"code" : "string"
} ,
"country_code" : "string"
} ,
"type" : "string" ,
"coordinates" : {
"latitude" : 0 ,
"longitude" : 0
} ,
"full_address" : "string" ,
"short_address" : "string" ,
"district" : "string" ,
"street" : "string" ,
"fulfillment_priority" : 0 ,
"is_default" : true ,
"is_private" : true ,
"is_enabled" : true ,
"has_stocks" : true ,
"channels" : [
"string"
] ,
"linked_users" : [
{
"user_uuid" : "string" ,
"full_name" : "string"
}
]
} `
```

Modified at 2026-02-01 20:17:48

Previous

Create Location

Next

Update Product Stock for Location
