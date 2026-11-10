---
# Synced from https://docs.zid.sa/get-store-location-by-id
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-get-store-location-by-id
title: "View Location"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/get-store-location-by-id
tags: [from-docs-site, partner-docs]
language: en
---

> View Location - Zid Docs
# View Location

GET

https://api.zid.sa/ v1/locations/{location_id}/

Retrieves details about a specified location.

🔑Scopes

`inventories.read` - Inventories Read

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

🟠 404 Not found

🔴 500 Internal Server error

Request Request Example

Shell

JavaScript

Java

Swift

```
` curl --location --request GET 'https://api.zid.sa/v1/locations/056e7f7f-85e2-42fc-a630-3a7ba839231e/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Authorization: {{Autherization}}' \
--header 'Store-Id: {{StoreId}}' \
--header 'Role: Manager' \
--header 'Accept-Language: en' \
--header 'Content-Type: application/json' \
--data '{
"short_address": "RHHB4094"
}' `
```

Response Response Example

200 - Success

```
` {
"id" : "8ee590fe-d02d-4c50-9184-f628bb8b115a" ,
"name" : {
"ar" : "الرياض - فرع عبد العزيز"
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
"latitude" : 24.77208405941104 ,
"longitude" : 46.66803359985352
} ,
"full_address" : "6137 King Abdul Aziz Branch Rd, An Nafal, Riyadh 13312, Saudi Arabia" ,
"short_address" : null ,
"district" : "King Abdul Aziz" ,
"street" : "نفال" ,
"fulfillment_priority" : 9 ,
"is_default" : false ,
"is_private" : false ,
"is_enabled" : true ,
"has_stocks" : true ,
"channels" : [
"pos" ,
"catalog"
] ,
"linked_users" : [
{
"user_uuid" : "6675a8a4-ad6e-4663-b53e-6852e63f48c7" ,
"full_name" : "Osama"
}
]
} `
```

Modified at 2026-02-01 20:47:34

Previous

List Locations

Next

Shipping
