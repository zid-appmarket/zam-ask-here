---
# Synced from https://docs.zid.sa/update-an-existing-product
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-update-an-existing-product
title: "Update Product"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/update-an-existing-product
tags: [from-docs-site, partner-docs]
language: en
---

> Update Product - Zid Docs
# Update Product

PATCH

https://api.zid.sa/ v1/products/{product_id}/

This endpoint lets you modify an existing product. You can update various aspects of the product, including:

**General Details:** Edit core information like title, description, price, and inventory.

**Grouped Products:** Manage the structure of grouped products (add, remove, or change linked products).

**Product Badges:** Assign, remove, or update the badge associated with the product.

### Creating or modifying variants of a product #

To modify or add options (variants) to the product, populate the `variants`

array in the request body. Each object in the `variants` array can either

update an existing variant (by specifying its `id`) or add a new variant (if `id` is omitted).

Alternatively, you can use the

Add Product Variants

endpoint to add new variants to the product.

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
` curl --location --request PATCH 'https://api.zid.sa/v1/products/a497974d-1755-423a-b06c-e0578ba8c318/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Authorization: {{Autherization}}' \
--header 'Store-Id: {{StoreId}}' \
--header 'Role: Manager' \
--header 'Accept-Language: en' \
--header 'Content-Type: application/json' \
--data '{
"name": {
"ar": "منتج شامل",
"en": "Comprehensive Product"
},
"description": {
"ar": "منتج يوضح جميع الميزات المتاحة",
"en": "Product showcasing all available features"
},
"short_description": {
"ar": "منتج شامل مع جميع الميزات",
"en": "Comprehensive product with all features"
},
"sku": "FULL-001",
"barcode": "1234567890128",
"price": 199.99,
"sale_price": 149.99,
"cost": 80.00,
"quantity": 100,
"is_infinite": false,
"is_draft": false,
"is_published": true,
"is_taxable": true,
"requires_shipping": true,
"weight": {
"value": 1.5,
"unit": "kg"
},
"categories": [
1,
2,
3
],
"keywords": [
"product",
"complete",
"featured"
],
"display_order": 1,
"seo": {
"title": {
"ar": "منتج شامل - متجر متقدم",
"en": "Comprehensive Product - Advanced Store"
},
"description": {
"ar": "اكتشف منتجنا الشامل بميزات متقدمة",
"en": "Discover our comprehensive product with advanced features"
}
},
"purchase_restrictions": {
"min_quantity_per_cart": 1,
"max_quantity_per_cart": 5,
"availability_period_start": "2024-01-01T00:00:00Z",
"availability_period_end": "2024-12-31T23:59:59Z",
"sale_price_period_start": "2024-01-01T00:00:00Z",
"sale_price_period_end": "2024-03-31T23:59:59Z"
},
"badge": {
"body": {
"ar": "خصم {discount_percent}",
"en": "Discount {discount_percent}"
}
}
}' `
```

Response Response Example

200 - Success

```
` {
"id" : "a497974d-1755-423a-b06c-e0578ba8c318" ,
"product_class" : null ,
"sku" : "WH-1000XX3" ,
"barcode" : "" ,
"parent_id" : null ,
"name" : {
"ar" : "منتج" ,
"en" : "Product"
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
"is_draft" : true ,
"quantity" : 50 ,
"is_infinite" : false ,
"html_url" : "https://osama.zid.store/products/wireless-headphones-7" ,
"weight" : {
"value" : null ,
"unit" : "kg"
} ,
"keywords" : [ ] ,
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
"cost" : null ,
"is_published" : false ,
"description" : {
"ar" : "" ,
"en" : ""
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
"available_quantity" : 50 ,
"is_infinite" : false
}
] ,
"sold_products_count" : null ,
"created_at" : "2026-02-10T18:33:37.084198Z" ,
"updated_at" : "2026-02-10T18:37:07.756518Z"
} `
```

Modified at 2026-06-17 12:18:53

Previous

List Product Settings

Next

Bulk Update Products
