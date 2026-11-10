---
# Synced from https://docs.zid.sa/insert-custom-user-input-fields-to-a-product
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-insert-custom-user-input-fields-to-a-product
title: "Create Custom Input Field"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/insert-custom-user-input-fields-to-a-product
tags: [from-docs-site, partner-docs]
language: en
---

> Create Custom Input Field - Zid Docs
# Create Custom Input Field

POST

https://api.zid.sa/ v1/products/{product_id}/custom_user_input_fields/

Adds custom user-input fields to a product, allowing customers to provide additional information while making a purchase. Custom user input fields can be used to collect data such as personalization details, gift messages, or special instructions.

🔑Scopes

`products.read_write` - Products Read & Write

## Request

Path Params

###

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

🔴 500 Internal Server error

Request Request Example

Shell

JavaScript

Java

Swift

```
` curl --location 'https://api.zid.sa/v1/products/e0ad7a76-ba42-4c59-94c9-0da600117fbf/custom_user_input_fields/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Store-Id: {{StoreId}}' \
--header 'Role: Manager' \
--header 'Content-Type: application/json' \
--data '{
"type": "TEXT",
"label": {
"en": "Engraving Text",
"ar": "نص النقش"
},
"hint": {
"en": "Please enter the engraving you want on the product",
"ar": "الرجاء إدخال النص المراد نقشه على المنتج"
},
"price": 44.5,
"is_required": false,
"is_published": true,
"display_order": 1,
"configs": {
"is_multiline": true
}
}' `
```

Response Response Example

201 - Created

```
` {
"id" : "b5364fa7-dda9-4005-aabf-fd20abb82517" ,
"type" : "TEXT" ,
"hint" : {
"en" : "Please enter the engraving you want on the product" ,
"ar" : "الرجاء إدخال النص المراد نقشه على المنتج"
} ,
"label" : {
"en" : "Engraving Text" ,
"ar" : "نص النقش"
} ,
"display_order" : 1 ,
"is_required" : false ,
"price" : 44.5 ,
"formatted_price" : " SAR 44.50" ,
"configs" : {
"is_multiline" : true
} ,
"visibility_condition" : null ,
"is_published" : true
} `
```

Modified at 2026-03-19 11:23:44

Previous

Delete Custom Option Field

Next

Update Custom Input Field
