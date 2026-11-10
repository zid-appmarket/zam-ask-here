---
# Synced from https://docs.zid.sa/add-product-variants
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-add-product-variants
title: "Create Variants"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/add-product-variants
tags: [from-docs-site, partner-docs]
language: en
---

> Create Variants - Zid Docs
# Create Variants

POST

https://api.zid.sa/ v1/products/{product_id}/variants/

This endpoint allows adding or creating variants for a given product. If the specified product is a standalone product (does not have any variants), this operation will convert it into a parent product.

**Steps to Create Variants:**

**1. Create Product Attributes**: Create product attributes for the store using the **add a new product attribute (https://docs.zid.sa/add-a-new-product-attribute)** endpoint.

**2. Define Attribute Choices**: Define choices (presets) for these attributes using the **Create attribute preset (https://docs.zid.sa/create-attribute-preset)** Endpoint.

For example, for a size attribute, choices might include 'small', 'medium', 'large', etc. Each choice is an object that accepts values in multiple languages. Currently, English and Arabic are supported. (If a choice is already created, no need to create it again).

**3. Variant Generation**: Send the details of variants you want to create using this endpoint. Refer to the example request payload below for the required structure.

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

🟢 200 Product Variants Added Successfully

application/json

Body application/json

###

🟠 400 Failed Response

🟠 401 Unauthorized

🔴 500 Internal Server error

🟠 400 Bad Request

Request Request Example

Shell

JavaScript

Java

Swift

```
` curl --location 'https://api.zid.sa/v1/products/e0ad7a76-ba42-4c59-94c9-0da600117fbf/variants/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Store-Id: {{StoreId}}' \
--header 'Content-Type: application/json' \
--data '{
"variants": [
{
"id": "ebd067c3-6c51-4692-9cac-e43118930ec2",
"is_deleted": false,
"sku": "Z.1.111111",
"price": 144,
"sale_price": null,
"cost": null,
"barcode": "Z.1.111111",
"attributes": [
{
"slug": "اللون",
"value": {
"ar": "ابيض",
"en": "White"
}
}
],
"stocks": [
{
"available_quantity": 44,
"is_infinite": false,
"location": "e2629f14-12ad-4ee4-8103-9db7290c4ccc"
}
],
"weight": {
"unit": "kg",
"value": null
}
},
{
"is_deleted": false,
"sku": "Z.2.1111",
"price": 144,
"sale_price": 122,
"cost": null,
"barcode": "Z.2.1111",
"attributes": [
{
"slug": "اللون",
"value": {
"ar": "اسود",
"en": "Black"
}
}
],
"stocks": [
{
"available_quantity": 77,
"is_infinite": false,
"location": "e2629f14-12ad-4ee4-8103-9db7290c4ccc"
}
],
"weight": {
"unit": "kg",
"value": null
}
}
]
}' `
```

Response Response Example

200 - Example 1

```
` {
"id" : "3c58afbb-7b07-4859-b653-b52242a33bb7" ,
"name" : {
"ar" : "" ,
"en" : ""
} ,
"sku" : "Z.1762848292350157" ,
"slug" : "3c58afbb-7b07-4859-b653-b52242a33bb7" ,
"currency" : "SAR" ,
"currency_symbol" : " SAR " ,
"price" : 0 ,
"sale_price" : null ,
"formatted_price" : " SAR 0.00" ,
"formatted_sale_price" : null ,
"description" : { } ,
"short_description" : { } ,
"categories" : [ ] ,
"images" : [ ] ,
"videos" : [ ] ,
"is_draft" : true ,
"is_infinite" : false ,
"is_taxable" : true ,
"requires_shipping" : true ,
"group_products" : null ,
"custom_option_fields" : [ ] ,
"custom_user_input_fields" : [ ] ,
"options" : [
{
"id" : "518fe604-8642-4032-b967-0be821ae235d" ,
"name" : "Color" ,
"slug" : "اللون" ,
"choices" : [
"Black" ,
"White"
]
}
] ,
"related_products" : [ ] ,
"related_products_settings" : "AUTO_GENERATED" ,
"related_products_title" : { } ,
"badge" : null ,
"html_url" : "https://mustafastore.localhost:8084/products/3c58afbb-7b07-4859-b653-b52242a33bb7" ,
"created_at" : "2025-11-11T08:04:52.363138Z" ,
"updated_at" : "2025-11-11T08:05:16.595741Z" ,
"store_id" : 6 ,
"structure" : "parent" ,
"stocks" : [ ] ,
"variants" : [
{
"id" : "22a32ae6-6c6c-4904-9e2f-9c3a9373f8f1" ,
"parent_id" : "3c58afbb-7b07-4859-b653-b52242a33bb7" ,
"name" : {
"en" : " - Black"
} ,
"slug" : "en-black" ,
"sku" : "Z.6.7228299999713898900" ,
"price" : 0 ,
"sale_price" : null ,
"is_published" : false ,
"is_draft" : true ,
"is_infinite" : false ,
"is_taxable" : true ,
"has_fields" : false ,
"has_options" : false ,
"created_at" : "2025-11-11T08:05:16.588385Z" ,
"updated_at" : "2025-11-11T08:05:16.588397Z" ,
"currency" : "SAR" ,
"currency_symbol" : " SAR " ,
"html_url" : "https://mustafastore.localhost:8084/products/en-black" ,
"structure" : "child" ,
"weight" : { } ,
"stocks" : [ ]
}
] ,
"weight" : { }
} `
```

Modified at 2026-02-15 16:06:34

Previous

Product Variants

Next

Create Custom Option
