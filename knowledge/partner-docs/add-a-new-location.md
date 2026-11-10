---
# Synced from https://docs.zid.sa/add-a-new-location
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-add-a-new-location
title: "Create Location"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/add-a-new-location
tags: [from-docs-site, partner-docs]
language: en
---

> Create Location - Zid Docs
# Create Location

POST

https://api.zid.sa/ v1/locations/

Adds a new location to the store.

🔑Scopes

`inventories.read_write `- Inventories Read & Write

## Request

Header Params

###

Body Params application/json

###

Examples

## Responses

🟢 201 Created

application/json

Body application/json

###

🟠 401 Unauthorized

🟠 400 Bad Request

🔴 500 Internal Server error

Request Request Example

Shell

JavaScript

Java

Swift

```
` curl --location 'https://api.zid.sa/v1/locations/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Authorization: {{Autherization}}' \
--header 'Store-Id: {{StoreId}}' \
--header 'Role: Manager' \
--header 'Accept-Language: en' \
--header 'Content-Type: application/json' \
--data '{
"store_id": 3,
"name": "test 3",
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

201 - Success

```
` {
"id" : "0b602ebc-1bbe-4905-b010-51599615ce82" ,
"name" : {
"en" : "test 2"
} ,
"city" : {
"id" : 1 ,
"name" : "Riyadh" ,
"ar_name" : "الرياض" ,
"country" : {
"id" : 184 ,
"name" : "Saudi Arabia" ,
"ar_name" : "السعودية" ,
"iso_code_2" : "SA" ,
"iso_code_3" : "SAU" ,
"code" : "SA"
} ,
"country_code" : "SA"
} ,
"type" : "PHYSICAL" ,
"coordinates" : {
"latitude" : 23.2532 ,
"longitude" : 23.3232
} ,
"full_address" : "RHHB4094, 4094 Al Aflaj, 7377، حي الواحة، Riyadh 12442, Saudi Arabia" ,
"short_address" : "RHHB4094" ,
"district" : null ,
"street" : null ,
"fulfillment_priority" : null ,
"is_default" : false ,
"is_private" : true ,
"is_enabled" : false ,
"has_stocks" : false ,
"channels" : [
"catalog"
] ,
"linked_users" : [ ]
} `
```

Modified at 2026-02-01 20:10:02

Previous

Inventories

Next

Update Location
