---
# Synced from https://docs.zid.sa/get-vat-settings
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-get-vat-settings
title: "Retrieve VAT Settings"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/get-vat-settings
tags: [from-docs-site, partner-docs]
language: en
---

> Retrieve VAT Settings - Zid Docs
# Retrieve VAT Settings

GET

https://api.zid.sa/ v1/managers/store/third-party/vat

Return a list of the VAT settings configured on this store. For example, to indicate whether the store VAT is applied on shipping fees or not.

🔑Scopes

`third_vat_read` - Third Vat Read

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
` curl --location 'https://api.zid.sa/v1/managers/store/third-party/vat' \
--header 'Accept-Language: en' \
--header 'Authorization: {{Autherization}}' \
--header 'X-Manager-Token: {{Access-Token}}' `
```

Response Response Example

200 - Example 1

```
` {
"status" : "object" ,
"tax_settings" : {
"can_use_vat" : true ,
"vat_activate" : true ,
"is_vat_self_paid" : false ,
"is_vat_included_in_product_price" : true ,
"is_shipping_fee_included_in_vat" : false ,
"other_countries_tax_percentage" : 0 ,
"countries" : [
{
"id" : "9345a371-1b26-449b-812f-ef5b8ecd0e81" ,
"country" : {
"id" : 184 ,
"name" : {
"ar" : "السعودية" ,
"en" : "Saudi Arabia"
} ,
"iso_code_2" : "SA" ,
"iso_code_3" : "SAU"
} ,
"tax_percentage" : 0 ,
"vat_number" : "310329522200003" ,
"tax_registration_certificate" : null ,
"settings" : [ ] ,
"is_certificate_visible" : false ,
"is_vat_number_visible" : true
}
]
} ,
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

Retrieve Store Manager Profile

Next

List Payment Methods
