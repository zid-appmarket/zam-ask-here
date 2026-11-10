---
# Synced from https://docs.zid.sa/create-reverse-orders-waybill
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-create-reverse-orders-waybill
title: "Create Reverse Orders Waybill"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/create-reverse-orders-waybill
tags: [from-docs-site, partner-docs]
language: en
---

> Create Reverse Orders Waybill - Zid Docs
# Create Reverse Orders Waybill

POST

https://api.zid.sa/ v1/managers/store/reverse-orders/waybill

Creates a waybill for a reversed order.

🔑Scopes

` orders.read_write` - Orders Read & Write

## Request

Header Params

###

Body Params multipart/form-data

###

## Responses

🟢 200 Reverse order waybill created successfully.

application/json

Body application/json

###

🟠 401 Unauthorized

🔴 500 Internal Server error

🟠 422 Validation errors

Request Request Example

Shell

JavaScript

Java

Swift

```
` curl --location 'https://api.zid.sa/v1/managers/store/reverse-orders/waybill' \
--header 'Authorization: {{Autherization}}' \
--header 'X-MANAGER-TOKEN: {{Access-Token}}' \
--header 'Accept-Language: en' \
--form 'order_id="64086815"' \
--form 'is_standalone_zidship_waybill="0"' `
```

Response Response Example

200 - Example 1

```
` {
"id" : "\"0039bc75-472d-4c48-8c82-5e0a6e8eca14\"" ,
"store_id" : "\"724b67c5-2fca-4813-a4ab-2f77703b2f37\"" ,
"order_id" : 1 ,
"consignee_name" : "\"osama\"" ,
"consignee_mobile" : "\"966500000005\"" ,
"consignee_city" : {
"id" : 1 ,
"country" : {
"id" : 183 ,
"name" : "\"Saudi Arabia\""
} ,
"ar_name" : "string" ,
"en_name" : "string" ,
"name" : "\"Riyadh\"" ,
"priority" : 0
} ,
"consignee_address_1" : "string" ,
"consignee_address_2" : "string" ,
"inventory" : {
"id" : "\"5d1bee6c07e543c99a36849fdd6f5773\"" ,
"country" : {
"id" : 183 ,
"name" : {
"ar" : "string" ,
"en" : "string"
}
} ,
"type" : "\"PHYSICAL\"" ,
"coordinates" : {
"type" : "\"Point\"" ,
"coordinates" : [
0
]
} ,
"city_id" : 1
} ,
"reason" : [
" \"Does not match the description\""
] ,
"waybill" : {
"id" : "\"50e06bb5-2ea7-480d-9e98-961076cf87d7\"" ,
"cost" : 10 ,
"label" : "\"https:\\\\/\\\\/zidship.com\\\\/labels\\\\/50e06bb5-2ea7-480d-9e98-961076cf87d7\"" ,
"status" : "string" ,
"courier" : "\"https:\\\\/\\\\/zidship.com\\\\/labels\\\\/50e06bb5-2ea7-480d-9e98-961076cf87d7\"" ,
"tracking_url" : "\"https:\\\\/\\\\/zidship.com\\\\/track\\\\/24098837-reverse\"" ,
"service_level" : "\"reverse\"" ,
"tracking_number" : "\"290446207592\""
}
} `
```

Modified at 2026-02-09 07:39:08

Previous

Create Reverse Orders

Next

Add Reverse Order Reasons
