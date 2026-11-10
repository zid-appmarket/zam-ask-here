---
# Synced from https://docs.zid.sa/insert-custom-options-to-a-product
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-insert-custom-options-to-a-product
title: "Create Custom Option"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/insert-custom-options-to-a-product
tags: [from-docs-site, partner-docs]
language: en
---

> Create Custom Option - Zid Docs
# Create Custom Option

POST

https://api.zid.sa/ v1/products/{product_id}/custom_options_fields/

Adds custom options to a product, allowing customers to choose from a predefined set of options while making a purchase. Custom options can be used to offer choices such as gift wrapping, warranty options, or other additional services.

🔑Scopes

`products.read_write` - Products Read & Write

## Request

Path Params

###

Header Params

###

Body Params application/json Required

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
` curl --location 'https://api.zid.sa/v1/products/e0ad7a76-ba42-4c59-94c9-0da600117fbf/custom_options_fields/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Store-Id: {{StoreId}}' \
--header 'Role: Manager' \
--header 'Accept-Language: en' \
--header 'Content-Type: application/json' \
--data '{
"type": "CHECKBOX",
"label": {
"ar": "خيار مخصص",
"en": "custom option"
},
"hint": {
"ar": "يرجى اختيار الخيار المناسب",
"en": "Please select a suitable option"
},
"min_choices": 1,
"max_choices": 100,
"can_choose_multiple_options": true,
"is_published": true,
"is_required": true,
"display_order": 2,
"choices": [
{
"price": 66.5,
"id": "",
"ar": "قيمة 1",
"en": "value 1"
}
]
}' `
```

Response Response Example

201 - Example 1

```
` {
"id" : "string" ,
"type" : "string" ,
"label" : {
"ar" : "string" ,
"en" : "string"
} ,
"hint" : {
"ar" : "string" ,
"en" : "string"
} ,
"min_choices" : 0 ,
"max_choices" : 0 ,
"can_choose_multiple_options" : true ,
"is_published" : true ,
"is_required" : true ,
"display_order" : 0 ,
"choices" : [
{
"ar" : "string" ,
"en" : "string" ,
"price" : 0 ,
"id" : "string"
}
] ,
"visibility_condition" : { }
} `
```

Modified at 2026-03-19 11:12:03

Previous

Create Variants

Next

Update Custom Option
