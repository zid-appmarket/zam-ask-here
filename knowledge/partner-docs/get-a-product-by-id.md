---
# Synced from https://docs.zid.sa/get-a-product-by-id
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-get-a-product-by-id
title: "View Product"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/get-a-product-by-id
tags: [from-docs-site, partner-docs]
language: en
---

> View Product - Zid Docs
# View Product

GET

https://api.zid.sa/ v1/products/{product_id}/

Get product by ID as Manager or as Customer .

Managers need to provide the `Authorization` and `X-Manager-Token` headers, and the `Role` should be set to `Manager`.

Customers don't need an authorization token, and the `Role` should be set to `Customer`.

Both Customer and Manager get essentially the same object with two key differences for managers:

1 .

In the Manager response, both the `name` field and the `value` field in the `attributes` array are objects containing "ar" (Arabic) and "en" (English) strings, while in the Customer response, they are just single strings.

2 .

The Manager response contains two additional fields: `created_at` and `updated_at`, which provide timestamps for when the product was created and last updated.

These are the main structural differences between the two responses. Other than that, they share the same structure, including the nested arrays and objects.

🔑Scopes

`products.read` - Products Read

## Request

Path Params

###

Header Params

###

Body Params multipart/form-data

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
` curl --location 'https://api.zid.sa/v1/products/2829a483-4336-43ab-a855-84532c9419c2/' \
--header 'Authorization: {{Autherization}}' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Store-Id: {{StoreId}}' \
--header 'Role: Manager' \
--header 'Accept-Language: en' `
```

Response Response Example

200 - Success

```
` {
"id" : "2829a483-4336-43ab-a855-84532c9419c2" ,
"product_class" : null ,
"sku" : "4741-c" ,
"barcode" : "" ,
"parent_id" : null ,
"name" : {
"ar" : "بخاخ منظف كاربوريتر QV5-200 100 Miles"
} ,
"slug" : "بخاخ-منظف-كاربوريتر-qv5-200-100-miles" ,
"price" : 9.0 ,
"short_description" : {
"ar" : "" ,
"en" : ""
} ,
"sale_price" : null ,
"formatted_price" : " SAR 9.00" ,
"formatted_sale_price" : null ,
"currency" : "SAR" ,
"currency_symbol" : " SAR " ,
"attributes" : [
{
"id" : "1ac221ff-f1d4-4abc-9995-45609e0faa7d" ,
"slug" : "ar-بارد-ساخن-و-باردt-en-180" ,
"name" : "بارد / ساخن و بارد\t" ,
"value" : {
"ar" : "بارد"
} ,
"type" : "default" ,
"type_value" : {
"ar" : "" ,
"en" : ""
} ,
"product_id" : "2829a483-4336-43ab-a855-84532c9419c2" ,
"attribute_image_id" : null ,
"display_order" : null ,
"attribute_id" : "eee2e93e-f055-4a28-8f26-e8bac9e9e17f" ,
"attribute_display_order" : null ,
"use_as_filter" : true
}
] ,
"categories" : [
{
"id" : "1346690" ,
"name" : {
"en" : "Test" ,
"ar" : "Test"
} ,
"slug" : "test" ,
"description" : {
"en" : "" ,
"ar" : ""
} ,
"cover_image" : null ,
"image" : "d297fb8b-c322-412e-a2f4-ffa96dc57022/0317d05b-be80-4db4-9fb7-a3616866abcf.jpg" ,
"display_order" : 32767 ,
"meta" : {
"childs" : [ ] ,
"parents" : [ ]
}
} ,
{
"id" : "1400850" ,
"name" : {
"en" : "ANNIVERSARY" ,
"ar" : "ANNIVERSARY"
} ,
"slug" : "anniversary" ,
"description" : {
"en" : "" ,
"ar" : ""
} ,
"cover_image" : null ,
"image" : null ,
"display_order" : 32767 ,
"meta" : {
"childs" : [ ] ,
"parents" : [ ]
}
}
] ,
"display_order" : null ,
"has_options" : true ,
"has_fields" : false ,
"images" : [
{
"id" : "d464301e-d7ce-403d-a2b6-df2d0e4daf88" ,
"image" : {
"large" : "https://media.zid.store/thumbs/d297fb8b-c322-412e-a2f4-ffa96dc57022/d464301e-d7ce-403d-a2b6-df2d0e4daf88-thumbnail-1000x1000-70.jpg" ,
"full_size" : "https://media.zid.store/thumbs/d297fb8b-c322-412e-a2f4-ffa96dc57022/d464301e-d7ce-403d-a2b6-df2d0e4daf88-thumbnail-1000x1000-70.jpg" ,
"medium" : "https://media.zid.store/thumbs/d297fb8b-c322-412e-a2f4-ffa96dc57022/d464301e-d7ce-403d-a2b6-df2d0e4daf88-thumbnail-770x770-70.jpg" ,
"thumbnail" : "https://media.zid.store/thumbs/d297fb8b-c322-412e-a2f4-ffa96dc57022/d464301e-d7ce-403d-a2b6-df2d0e4daf88-thumbnail-370x370-70.jpg" ,
"small" : "https://media.zid.store/thumbs/d297fb8b-c322-412e-a2f4-ffa96dc57022/d464301e-d7ce-403d-a2b6-df2d0e4daf88-thumbnail-500x500-70.jpg"
} ,
"alt_text" : "" ,
"display_order" : 1 ,
"i18n_alt_text" : {
"ar" : "" ,
"en" : ""
}
} ,
{
"id" : "7a2943aa-d1fc-4011-8fda-d42314595092" ,
"image" : {
"large" : "https://media.zid.store/thumbs/d297fb8b-c322-412e-a2f4-ffa96dc57022/7a2943aa-d1fc-4011-8fda-d42314595092-thumbnail-1000x1000-70.jpg" ,
"full_size" : "https://media.zid.store/thumbs/d297fb8b-c322-412e-a2f4-ffa96dc57022/7a2943aa-d1fc-4011-8fda-d42314595092-thumbnail-1000x1000-70.jpg" ,
"medium" : "https://media.zid.store/thumbs/d297fb8b-c322-412e-a2f4-ffa96dc57022/7a2943aa-d1fc-4011-8fda-d42314595092-thumbnail-770x770-70.jpg" ,
"thumbnail" : "https://media.zid.store/thumbs/d297fb8b-c322-412e-a2f4-ffa96dc57022/7a2943aa-d1fc-4011-8fda-d42314595092-thumbnail-370x370-70.jpg" ,
"small" : "https://media.zid.store/thumbs/d297fb8b-c322-412e-a2f4-ffa96dc57022/7a2943aa-d1fc-4011-8fda-d42314595092-thumbnail-500x500-70.jpg"
} ,
"alt_text" : "" ,
"display_order" : 2 ,
"i18n_alt_text" : {
"ar" : "" ,
"en" : ""
}
}
] ,
"videos" : [ ] ,
"is_draft" : false ,
"quantity" : 0 ,
"is_infinite" : false ,
"html_url" : "https://osama.zid.store/products/بخاخ-منظف-كاربوريتر-qv5-200-100-miles" ,
"weight" : {
"value" : 0.5 ,
"unit" : "kg"
} ,
"keywords" : [ ] ,
"requires_shipping" : true ,
"is_taxable" : true ,
"structure" : "parent" ,
"seo" : {
"title" : {
"ar" : "" ,
"en" : ""
} ,
"description" : {
"ar" : "" ,
"en" : ""
}
} ,
"rating" : {
"average" : 0.0 ,
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
"min_quantity_per_cart" : 1 ,
"max_quantity_per_cart" : 1 ,
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
"meta" : { } ,
"related_products_settings" : "AUTO_GENERATED" ,
"related_products_title" : {
"ar" : "" ,
"en" : ""
} ,
"badge" : {
"body" : {
"ar" : "يباع سريعًا" ,
"en" : "Selling fast"
} ,
"icon" : {
"code" : "selling_fast"
}
} ,
"variants" : [
{
"id" : "4b30b53a-72c1-4a6c-b225-de8ce7a70559" ,
"product_class" : null ,
"sku" : "Z.17657946790465753" ,
"barcode" : "" ,
"parent_id" : "2829a483-4336-43ab-a855-84532c9419c2" ,
"name" : {
"ar" : "بخاخ منظف كاربوريتر QV5-200 100 Miles - 12"
} ,
"slug" : "en-بخاخ-منظف-كاربوريتر-qv5-200-100-miles-12" ,
"price" : 9.0 ,
"short_description" : {
"ar" : "" ,
"en" : ""
} ,
"sale_price" : null ,
"formatted_price" : " SAR 9.00" ,
"formatted_sale_price" : null ,
"currency" : "SAR" ,
"currency_symbol" : " SAR " ,
"attributes" : [
{
"id" : "86d2e3da-ad4d-4e42-b40c-5b6c5886a336" ,
"slug" : "ar-درجة-اللون-en" ,
"name" : "درجة اللون" ,
"value" : {
"en" : "12"
} ,
"type" : "default" ,
"type_value" : {
"ar" : "" ,
"en" : ""
} ,
"product_id" : "4b30b53a-72c1-4a6c-b225-de8ce7a70559" ,
"attribute_image_id" : null ,
"display_order" : 1 ,
"attribute_id" : "230192a3-9aef-4dde-aba3-836cc43f9ae6" ,
"attribute_display_order" : 1 ,
"use_as_filter" : false
}
] ,
"categories" : [
{
"id" : "1346690" ,
"name" : {
"en" : "Test" ,
"ar" : "Test"
} ,
"slug" : "test" ,
"description" : {
"en" : "" ,
"ar" : ""
} ,
"cover_image" : null ,
"image" : "d297fb8b-c322-412e-a2f4-ffa96dc57022/0317d05b-be80-4db4-9fb7-a3616866abcf.jpg" ,
"display_order" : 32767 ,
"meta" : {
"childs" : [ ] ,
"parents" : [ ]
}
} ,
{
"id" : "1400850" ,
"name" : {
"en" : "ANNIVERSARY" ,
"ar" : "ANNIVERSARY"
} ,
"slug" : "anniversary" ,
"description" : {
"en" : "" ,
"ar" : ""
} ,
"cover_image" : null ,
"image" : null ,
"display_order" : 32767 ,
"meta" : {
"childs" : [ ] ,
"parents" : [ ]
}
}
] ,
"display_order" : null ,
"has_options" : false ,
"has_fields" : false ,
"images" : [ ] ,
"videos" : [ ] ,
"is_draft" : false ,
"quantity" : 0 ,
"is_infinite" : false ,
"html_url" : "https://osama.zid.store/products/بخاخ-منظف-كاربوريتر-qv5-200-100-miles" ,
"weight" : {
"value" : 0.5 ,
"unit" : "kg"
} ,
"keywords" : [ ] ,
"requires_shipping" : true ,
"is_taxable" : true ,
"structure" : "child" ,
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
"metafields" : [ ] ,
"meta" : null ,
"related_products_settings" : "AUTO_GENERATED" ,
"related_products_title" : {
"ar" : "" ,
"en" : ""
} ,
"badge" : null ,
"cost" : null ,
"is_published" : true ,
"waiting_customers_count" : null ,
"group_products" : null ,
"stocks" : [
{
"id" : "4b1b15f7-e22c-4b24-b5e8-c87bece4b1b1" ,
"location" : {
"id" : "8ee590fe-d02d-4c50-9184-f628bb8b115a" ,
"name" : {
"ar" : "الرياض - فرع عبد العزيز"
} ,
"type" : "PHYSICAL" ,
"full_address" : "6137 King Abdul Aziz Branch Rd, An Nafal, Riyadh 13312, Saudi Arabia"
} ,
"available_quantity" : 0 ,
"is_infinite" : false
}
] ,
"sold_products_count" : null ,
"created_at" : "2025-12-15T10:31:19.067786Z" ,
"updated_at" : "2025-12-15T10:31:19.067804Z"
} ,
{
"id" : "df27027c-c890-4ec5-b07b-2dfd33ddffd2" ,
"product_class" : null ,
"sku" : "Z.17657946790250232" ,
"barcode" : "" ,
"parent_id" : "2829a483-4336-43ab-a855-84532c9419c2" ,
"name" : {
"ar" : "بخاخ منظف كاربوريتر QV5-200 100 Miles - 55"
} ,
"slug" : "en-بخاخ-منظف-كاربوريتر-qv5-200-100-miles-55" ,
"price" : 9.0 ,
"short_description" : {
"ar" : "" ,
"en" : ""
} ,
"sale_price" : null ,
"formatted_price" : " SAR 9.00" ,
"formatted_sale_price" : null ,
"currency" : "SAR" ,
"currency_symbol" : " SAR " ,
"attributes" : [
{
"id" : "eaad7c89-34ad-4c36-98bc-a43b251df3d8" ,
"slug" : "ar-درجة-اللون-en" ,
"name" : "درجة اللون" ,
"value" : {
"ar" : "55" ,
"en" : "55"
} ,
"type" : "default" ,
"type_value" : {
"ar" : "" ,
"en" : ""
} ,
"product_id" : "df27027c-c890-4ec5-b07b-2dfd33ddffd2" ,
"attribute_image_id" : null ,
"display_order" : 2 ,
"attribute_id" : "230192a3-9aef-4dde-aba3-836cc43f9ae6" ,
"attribute_display_order" : 1 ,
"use_as_filter" : false
}
] ,
"categories" : [
{
"id" : "1346690" ,
"name" : {
"en" : "Test" ,
"ar" : "Test"
} ,
"slug" : "test" ,
"description" : {
"en" : "" ,
"ar" : ""
} ,
"cover_image" : null ,
"image" : "d297fb8b-c322-412e-a2f4-ffa96dc57022/0317d05b-be80-4db4-9fb7-a3616866abcf.jpg" ,
"display_order" : 32767 ,
"meta" : {
"childs" : [ ] ,
"parents" : [ ]
}
} ,
{
"id" : "1400850" ,
"name" : {
"en" : "ANNIVERSARY" ,
"ar" : "ANNIVERSARY"
} ,
"slug" : "anniversary" ,
"description" : {
"en" : "" ,
"ar" : ""
} ,
"cover_image" : null ,
"image" : null ,
"display_order" : 32767 ,
"meta" : {
"childs" : [ ] ,
"parents" : [ ]
}
}
] ,
"display_order" : null ,
"has_options" : false ,
"has_fields" : false ,
"images" : [ ] ,
"videos" : [ ] ,
"is_draft" : false ,
"quantity" : 0 ,
"is_infinite" : false ,
"html_url" : "https://osama.zid.store/products/بخاخ-منظف-كاربوريتر-qv5-200-100-miles" ,
"weight" : {
"value" : 0.5 ,
"unit" : "kg"
} ,
"keywords" : [ ] ,
"requires_shipping" : true ,
"is_taxable" : true ,
"structure" : "child" ,
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
"metafields" : [ ] ,
"meta" : null ,
"related_products_settings" : "AUTO_GENERATED" ,
"related_products_title" : {
"ar" : "" ,
"en" : ""
} ,
"badge" : null ,
"cost" : null ,
"is_published" : true ,
"waiting_customers_count" : null ,
"group_products" : null ,
"stocks" : [
{
"id" : "5c968fe2-5257-4b01-8774-d8c1cee70867" ,
"location" : {
"id" : "8ee590fe-d02d-4c50-9184-f628bb8b115a" ,
"name" : {
"ar" : "الرياض - فرع عبد العزيز"
} ,
"type" : "PHYSICAL" ,
"full_address" : "6137 King Abdul Aziz Branch Rd, An Nafal, Riyadh 13312, Saudi Arabia"
} ,
"available_quantity" : 0 ,
"is_infinite" : false
}
] ,
"sold_products_count" : null ,
"created_at" : "2025-12-15T10:31:19.067506Z" ,
"updated_at" : "2025-12-15T10:31:19.067576Z"
} ,
{
"id" : "02095901-ecef-4acc-9e4c-1ac1183da891" ,
"product_class" : null ,
"sku" : "Z.176579467901102951" ,
"barcode" : "" ,
"parent_id" : "2829a483-4336-43ab-a855-84532c9419c2" ,
"name" : {
"ar" : "بخاخ منظف كاربوريتر QV5-200 100 Miles - 15"
} ,
"slug" : "en-بخاخ-منظف-كاربوريتر-qv5-200-100-miles-15" ,
"price" : 9.0 ,
"short_description" : {
"ar" : "" ,
"en" : ""
} ,
"sale_price" : null ,
"formatted_price" : " SAR 9.00" ,
"formatted_sale_price" : null ,
"currency" : "SAR" ,
"currency_symbol" : " SAR " ,
"attributes" : [
{
"id" : "d5d891fa-0655-4468-898d-ae6e447700f7" ,
"slug" : "ar-درجة-اللون-en" ,
"name" : "درجة اللون" ,
"value" : {
"en" : "15"
} ,
"type" : "default" ,
"type_value" : {
"ar" : "" ,
"en" : ""
} ,
"product_id" : "02095901-ecef-4acc-9e4c-1ac1183da891" ,
"attribute_image_id" : null ,
"display_order" : 3 ,
"attribute_id" : "230192a3-9aef-4dde-aba3-836cc43f9ae6" ,
"attribute_display_order" : 1 ,
"use_as_filter" : false
}
] ,
"categories" : [
{
"id" : "1346690" ,
"name" : {
"en" : "Test" ,
"ar" : "Test"
} ,
"slug" : "test" ,
"description" : {
"en" : "" ,
"ar" : ""
} ,
"cover_image" : null ,
"image" : "d297fb8b-c322-412e-a2f4-ffa96dc57022/0317d05b-be80-4db4-9fb7-a3616866abcf.jpg" ,
"display_order" : 32767 ,
"meta" : {
"childs" : [ ] ,
"parents" : [ ]
}
} ,
{
"id" : "1400850" ,
"name" : {
"en" : "ANNIVERSARY" ,
"ar" : "ANNIVERSARY"
} ,
"slug" : "anniversary" ,
"description" : {
"en" : "" ,
"ar" : ""
} ,
"cover_image" : null ,
"image" : null ,
"display_order" : 32767 ,
"meta" : {
"childs" : [ ] ,
"parents" : [ ]
}
}
] ,
"display_order" : null ,
"has_options" : false ,
"has_fields" : false ,
"images" : [ ] ,
"videos" : [ ] ,
"is_draft" : false ,
"quantity" : 0 ,
"is_infinite" : false ,
"html_url" : "https://osama.zid.store/products/بخاخ-منظف-كاربوريتر-qv5-200-100-miles" ,
"weight" : {
"value" : 0.5 ,
"unit" : "kg"
} ,
"keywords" : [ ] ,
"requires_shipping" : true ,
"is_taxable" : true ,
"structure" : "child" ,
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
"metafields" : [ ] ,
"meta" : null ,
"related_products_settings" : "AUTO_GENERATED" ,
"related_products_title" : {
"ar" : "" ,
"en" : ""
} ,
"badge" : null ,
"cost" : null ,
"is_published" : true ,
"waiting_customers_count" : null ,
"group_products" : null ,
"stocks" : [
{
"id" : "8e9f5411-3aa5-4c8c-b2d6-d04539b6ba0a" ,
"location" : {
"id" : "8ee590fe-d02d-4c50-9184-f628bb8b115a" ,
"name" : {
"ar" : "الرياض - فرع عبد العزيز"
} ,
"type" : "PHYSICAL" ,
"full_address" : "6137 King Abdul Aziz Branch Rd, An Nafal, Riyadh 13312, Saudi Arabia"
} ,
"available_quantity" : 0 ,
"is_infinite" : false
}
] ,
"sold_products_count" : null ,
"created_at" : "2025-12-15T10:31:19.067198Z" ,
"updated_at" : "2025-12-15T10:31:19.067236Z"
}
] ,
"cost" : null ,
"is_published" : true ,
"waiting_customers_count" : null ,
"description" : {
"ar" : "<p><img src=\"https://ibb.co/zhsQ7qwy\" alt=\"\" width=\"1279\" height=\"721\"></p>"
} ,
"custom_user_input_fields" : [ ] ,
"custom_option_fields" : [ ] ,
"options" : [
{
"id" : "230192a3-9aef-4dde-aba3-836cc43f9ae6" ,
"name" : "درجة اللون" ,
"slug" : "ar-درجة-اللون-en" ,
"choices" : [
"12" ,
"55" ,
"15"
]
}
] ,
"related_products" : [ ] ,
"next_product" : null ,
"previous_product" : null ,
"group_products" : null ,
"stocks" : [ ] ,
"sold_products_count" : null ,
"created_at" : "2025-12-15T08:42:07.070592Z" ,
"updated_at" : "2025-12-15T11:22:40.786573Z"
} `
```

Modified at 2026-02-05 12:29:15

Previous

List Products

Next

List Product Settings
