---
# Synced from https://docs.zid.sa/bulk-update-product
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-bulk-update-product
title: "Bulk Update Products"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/bulk-update-product
tags: [from-docs-site, partner-docs]
language: en
---

> Bulk Update Products - Zid Docs
# Bulk Update Products

PATCH

https://api.zid.sa/ v1/products/

This endpoint allows you to update multiple products at once by specifying their IDs or SKUs along with the new data. This makes managing large inventory updates more efficient.

🔑Scopes

`products.read_write` - Products Read & Write

Please note that submitting more than **50 IDs/SKUs** for product updates may lead to processing issues. We recommend adhering to this constraint to ensure smooth operations.

## Request

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

🟠 400 Bad Request

🔴 500 Internal Server error

Request Request Example

Shell

JavaScript

Java

Swift

```
` curl --location --request PATCH 'https://api.zid.sa/v1/products/' \
--header 'Authorization: {{Autherization}}' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Store-Id: {{StoreId}}' \
--header 'Role: Manager' \
--header 'Accept-Language: en' \
--header 'Content-Type: application/json' \
--data '[
{
"id": "a497974d-1755-423a-b06c-e0578ba8c318",
"sku": "WH-1000XX3",
"name": {
"ar": "تويتر",
"en": "twitter"
},
"description": {
"ar": "منتج اختبار",
"en": "This is a test product"
},
"price": 257,
"sale_price": 199,
"cost": 10,
"is_draft": false,
"quantity": 1,
"is_infinite": false,
"weight": {
"unit": "kg",
"value": 100
},
"keywords": [
"apps",
"social"
],
"requires_shipping": true,
"is_published": true
}
]' `
```

Response Response Example

200 - Success

```
` [
{
"id" : "a497974d-1755-423a-b06c-e0578ba8c318" ,
"product_class" : null ,
"sku" : "WH-1000XX3" ,
"barcode" : "" ,
"parent_id" : null ,
"name" : {
"ar" : "تويتر" ,
"en" : "twitter"
} ,
"slug" : "wireless-headphones-7" ,
"price" : 257.0 ,
"short_description" : {
"ar" : "" ,
"en" : ""
} ,
"sale_price" : 199.0 ,
"formatted_price" : " SAR 257.00" ,
"formatted_sale_price" : " SAR 199.00" ,
"currency" : "SAR" ,
"currency_symbol" : " SAR " ,
"attributes" : [ ] ,
"categories" : [ ] ,
"display_order" : 32766 ,
"has_options" : false ,
"has_fields" : false ,
"images" : [ ] ,
"videos" : [ ] ,
"is_draft" : false ,
"quantity" : 1 ,
"is_infinite" : false ,
"html_url" : "https://osama.zid.store/products/wireless-headphones-7" ,
"weight" : {
"value" : 100.0 ,
"unit" : "kg"
} ,
"keywords" : [
"social" ,
"apps"
] ,
"requires_shipping" : true ,
"is_taxable" : true ,
"structure" : "standalone" ,
"seo" : null ,
"rating" : {
"average" : 0 ,
"total_count" : 0 ,
"1_ratings" : {
"percentage" : 0 ,
"count" : 0
} ,
"2_ratings" : {
"percentage" : 0 ,
"count" : 0
} ,
"3_ratings" : {
"percentage" : 0 ,
"count" : 0
} ,
"4_ratings" : {
"percentage" : 0 ,
"count" : 0
} ,
"5_ratings" : {
"percentage" : 0 ,
"count" : 0
}
} ,
"store_id" : 3 ,
"purchase_restrictions" : {
"min_quantity_per_cart" : null ,
"max_quantity_per_cart" : null ,
"availability_period_start" : null ,
"availability_period_end" : null ,
"sale_price_period_start" : null ,
"sale_price_period_end" : null
} ,
"metafields" : [
{
"id" : "d2eebc1f-4c4b-4268-bbf2-c463aa3c7a71" ,
"name" : {
"en" : "" ,
"ar" : "تيست"
} ,
"slug" : "تيست-1" ,
"data_type" : "table" ,
"display_order" : 11 ,
"value" : null
} ,
{
"id" : "0fdb9855-ba77-4736-beba-e2c1f3b98550" ,
"name" : {
"en" : "Calories" ,
"ar" : "السعرات الحرارية"
} ,
"slug" : "السعرات الحرارية" ,
"data_type" : "number" ,
"display_order" : 10 ,
"value" : null
} ,
{
"id" : "f620c7fe-240a-4ba4-a206-5db470d3f115" ,
"name" : {
"en" : "" ,
"ar" : "لوحة"
} ,
"slug" : "لوحة" ,
"data_type" : "json" ,
"display_order" : 9 ,
"value" : null
} ,
{
"id" : "1681dc82-ca68-4147-ad56-b80039ef85de" ,
"name" : {
"en" : "expiry date" ,
"ar" : "تاريخ الإنتهاء"
} ,
"slug" : "تاريخ الإنتهاء" ,
"data_type" : "date" ,
"display_order" : 8 ,
"value" : null
} ,
{
"id" : "a3f4fd3f-6f47-4f78-b82a-cfc89a57b0d0" ,
"name" : {
"en" : "tt" ,
"ar" : "ttt"
} ,
"slug" : "tttt" ,
"data_type" : "file" ,
"display_order" : 7 ,
"value" : null
} ,
{
"id" : "8fe0a25f-dd49-44fa-a035-573ab64707fb" ,
"name" : {
"en" : "eeeuuuu" ,
"ar" : "yyyy"
} ,
"slug" : "eee" ,
"data_type" : "text" ,
"display_order" : 6 ,
"value" : null
} ,
{
"id" : "5a051783-ccdd-4185-ac60-563a93eae477" ,
"name" : {
"en" : "" ,
"ar" : "qeqe"
} ,
"slug" : "qeqe" ,
"data_type" : "text" ,
"display_order" : 5 ,
"value" : null
} ,
{
"id" : "4a476402-1b24-4c27-9c9f-3abfacde292f" ,
"name" : {
"en" : "Width" ,
"ar" : ""
} ,
"slug" : "width of the couch" ,
"data_type" : "text" ,
"display_order" : 4 ,
"value" : null
} ,
{
"id" : "b0ee31c9-b5de-441a-8616-3155b94cff2b" ,
"name" : {
"en" : "aaaa" ,
"ar" : "aaaaa"
} ,
"slug" : "aaa" ,
"data_type" : "text" ,
"display_order" : 3 ,
"value" : null
} ,
{
"id" : "93c92f9d-b2a3-4ccd-8222-594869ae1e8b" ,
"name" : {
"en" : "Wight" ,
"ar" : "الوزن"
} ,
"slug" : "الوزن" ,
"data_type" : "number" ,
"display_order" : 2 ,
"value" : null
} ,
{
"id" : "e6c621fb-14f0-4974-9ad2-973856699cf4" ,
"name" : {
"en" : "Test" ,
"ar" : "للاختبار"
} ,
"slug" : "For test" ,
"data_type" : "rich_text" ,
"display_order" : 1 ,
"value" : null
}
] ,
"meta" : null ,
"related_products_settings" : "AUTO_GENERATED" ,
"related_products_title" : {
"ar" : "" ,
"en" : ""
} ,
"badge" : null ,
"variants" : [ ] ,
"cost" : 10.0 ,
"is_published" : true ,
"description" : {
"ar" : "منتج اختبار" ,
"en" : "This is a test product"
} ,
"custom_user_input_fields" : [ ] ,
"custom_option_fields" : [ ] ,
"options" : [ ] ,
"related_products" : [ ] ,
"next_product" : null ,
"previous_product" : null ,
"group_products" : null ,
"stocks" : [
{
"id" : "750fef17-de8e-4599-af2c-6e82dc2f09a0" ,
"location" : {
"id" : "59be4f1d-3b59-4b34-ba47-9f7293894b47" ,
"name" : {
"ar" : "الدمام" ,
"en" : "Dammam"
} ,
"type" : "PHYSICAL" ,
"full_address" : "8RRM+PX Dammam Saudi Arabia"
} ,
"available_quantity" : 1 ,
"is_infinite" : false
}
] ,
"sold_products_count" : null ,
"created_at" : "2026-02-10T18:33:37.084198Z" ,
"updated_at" : "2026-02-10T18:42:44.196126Z"
}
] `
```

Modified at 2026-02-10 18:47:34

Previous

Update Product

Next

Delete Product
