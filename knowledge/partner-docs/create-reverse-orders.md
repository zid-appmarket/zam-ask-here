---
# Synced from https://docs.zid.sa/create-reverse-orders
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-create-reverse-orders
title: "Create Reverse Orders"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/create-reverse-orders
tags: [from-docs-site, partner-docs]
language: en
---

> Create Reverse Orders - Zid Docs
# Create Reverse Orders

POST

https://api.zid.sa/ v1/managers/store/reverse-orders

Creates an order reverse request.

🔑Scopes

`orders.read_write `- Orders Read & Write

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
` curl --location 'https://api.zid.sa/v1/managers/store/reverse-orders' \
--header 'Authorization: {{Autherization}}' \
--header 'X-MANAGER-TOKEN: {{Access-Token}}' \
--header 'Accept-Language: en' \
--header 'Content-Type: application/json' \
--data '{
"order_id": 64086815,
"is_partial": false,
"inventory_location_id": "8ee590fe-d02d-4c50-9184-f628bb8b115a",
"refund_payment_method": "bank_transfer",
"consignee_name": "Jane Smith",
"consignee_mobile": "+966500000005",
"consignee_city_id": 1,
"consignee_address_1": "456 Commerce Avenue",
"consignee_address_2": "Suite 301",
"reason": [
{
"name": "Customer canceled",
"id": "ebcfd40a-7c2f-4ed4-b30f-3fd142388ad7"
}
],
"products": [],
"packages_count": null,
"shipping_method": null
}' `
```

Response Response Example

200 - Success

```
` {
"status" : "object" ,
"order_reverse" : {
"id" : "cb86fa22-29a3-4169-8106-149591f5f512" ,
"store_id" : "d297fb8b-c322-412e-a2f4-ffa96dc57022" ,
"order_id" : 64086815 ,
"is_partial" : false ,
"consignee_name" : "Jane Smith" ,
"consignee_mobile" : "+966500000005" ,
"consignee_city" : {
"id" : 1 ,
"country_id" : 184 ,
"zone_id" : 2879 ,
"name" : "Riyadh" ,
"ar_name" : "الرياض" ,
"code" : null ,
"status" : 1 ,
"priority" : 10 ,
"created_at" : null ,
"updated_at" : "2021-05-26T13:04:05.000000Z" ,
"deleted_at" : null ,
"national_address_city_id" : 3 ,
"governorate_ar_name" : "امارة منطقة الرياض" ,
"governorate_en_name" : "Riyadh Principality" ,
"region_id" : 1 ,
"region_ar_name" : "الرياض" ,
"region_en_name" : "Riyadh" ,
"country" : {
"id" : 184 ,
"name" : "Saudi Arabia" ,
"ar_name" : "السعودية" ,
"country_code" : "+966" ,
"iso_code_2" : "SA" ,
"iso_code_3" : "SAU" ,
"address_format" : "" ,
"postcode_required" : 0 ,
"status" : 1 ,
"currency_code" : "SAR" ,
"tax_percentage" : null ,
"is_supported_by_zid" : 1 ,
"priority" : 1 ,
"created_at" : "2019-09-25T18:43:01.000000Z" ,
"updated_at" : "2019-09-25T18:43:01.000000Z"
}
} ,
"consignee_address_1" : "456 Commerce Avenue" ,
"consignee_address_2" : "Suite 301" ,
"inventory_address_id" : null ,
"inventory_location_id" : "8ee590fed02d4c509184f628bb8b115a" ,
"inventory" : {
"deleted" : null ,
"id" : "8ee590fed02d4c509184f628bb8b115a" ,
"created_at" : "2023-09-21T10:11:10.135964Z" ,
"updated_at" : "2025-10-13T14:55:15.609712Z" ,
"name" : {
"ar" : "الرياض - فرع عبد العزيز"
} ,
"type" : "PHYSICAL" ,
"coordinates" : {
"type" : "Point" ,
"coordinates" : [
46.66803359985352 ,
24.77208405941104
]
} ,
"is_default" : 0 ,
"is_private" : 0 ,
"is_enabled" : 1 ,
"fulfillment_priority" : 9 ,
"meta" : null ,
"city_id" : 1 ,
"store_id" : "d297fb8b-c322-412e-a2f4-ffa96dc57022" ,
"full_address" : "6137 King Abdul Aziz Branch Rd, An Nafal, Riyadh 13312, Saudi Arabia" ,
"channels" : [
"pos" ,
"catalog"
] ,
"district" : "King Abdul Aziz" ,
"street" : "نفال" ,
"short_address" : null
} ,
"reason" : [
{
"name" : "Customer canceled" ,
"id" : "ebcfd40a-7c2f-4ed4-b30f-3fd142388ad7"
}
] ,
"shipping_method" : null ,
"waybill" : null ,
"products" : [
{
"id" : "2ddecb80-348d-4880-be98-fdc756e47912" ,
"order_reverse_id" : "cb86fa22-29a3-4169-8106-149591f5f512" ,
"order_product_id" : 110168319 ,
"product_uuid" : "003140e29d8e462db823373407746871" ,
"quantity" : 1 ,
"reversed_quantity" : 1 ,
"received_quantity" : 0 ,
"not_received_quantity" : 0 ,
"damaged_quantity" : 0 ,
"product" : {
"id" : "003140e29d8e462db823373407746871" ,
"structure" : "standalone" ,
"store_id" : 3 ,
"name" : "طقم سفر للحواجب سوبرستار من بنفت" ,
"quantity" : null ,
"is_infinite" : true ,
"slug" : "طقم-سفر-للحواجب-سوبرستار-من-بنفت" ,
"sku" : "Z.217795.169603646831188" ,
"price" : "199.5600" ,
"sale_price" : null ,
"parent_id" : null ,
"is_published" : 1 ,
"is_draft" : 0 ,
"old_id" : null ,
"upc" : null ,
"rating" : null ,
"revision" : 1 ,
"product_class_id" : null ,
"display_order" : 32766 ,
"has_been_modified" : 1 ,
"created_at" : "2025-04-03T00:11:39.826154Z" ,
"updated_at" : "2025-04-03T00:11:39.826193Z" ,
"deleted" : null ,
"popularity_order" : null ,
"cost" : "0.0000" ,
"weight" : null ,
"popularity_points" : 26 ,
"requires_shipping" : 1 ,
"weight_display_unit" : "kg" ,
"is_taxable" : true ,
"purchase_restrictions" : {
"max_quantity_per_cart" : null ,
"min_quantity_per_cart" : null ,
"sale_price_period_end" : null ,
"availability_period_end" : null ,
"sale_price_period_start" : null ,
"availability_period_start" : null
} ,
"meta" : null ,
"short_description" : "{\"ar\": \"<p><br></p>\", \"en\": \"<p><br></p>\"}" ,
"badge" : null ,
"related_products_settings" : "AUTO_GENERATED" ,
"related_products_title" : null ,
"barcode" : null ,
"product_class" : null
} ,
"product_class" : null ,
"order_product" : {
"id" : 110168319 ,
"order_id" : 64086815 ,
"reseller_meta" : null ,
"product_id" : 0 ,
"product_uuid" : "003140e29d8e462db823373407746871" ,
"sku" : "Z.217795.169603646831188" ,
"name" : "طقم سفر للحواجب سوبرستار من بنفت" ,
"custom_fields" : null ,
"model" : "" ,
"quantity" : 1 ,
"requires_shipping" : 1 ,
"weight" : null ,
"cost" : 0 ,
"price" : "199.55999896568000" ,
"additions_price" : "0.00000000000000" ,
"total" : "199.55999896568000" ,
"net_price" : "173.53043388320000" ,
"net_sale_price" : null ,
"net_additions_price" : "0.00000000000000" ,
"gross_sale_price" : null ,
"gross_additions_price" : "0.00000000000000" ,
"gross_price" : "199.55999896568000" ,
"tax_percentage" : "0.15000000000000" ,
"tax_amount" : "26.02956508248000" ,
"is_taxable" : true ,
"is_discounted" : false ,
"meta" : null ,
"reward" : 0 ,
"created_at" : "2026-01-28T16:52:59.000000Z" ,
"updated_at" : "2026-01-28T16:52:59.000000Z" ,
"deleted_at" : null ,
"external_product_id" : null ,
"is_external_product" : false ,
"net_unit_price" : "173.53043388320000" ,
"gross_unit_price" : "199.55999896568000" ,
"undiscounted_net_unit_price" : "173.53" ,
"undiscounted_gross_unit_price" : "199.56" ,
"undiscounted_net_total" : "173.53" ,
"undiscounted_gross_total" : "199.56" ,
"unit_discount_amount" : "0.00000000000000" ,
"unit_discount_percentage" : "0.00000000000000" ,
"subtotal_discounts" : [ ]
} ,
"created_at" : "2026-01-31T12:15:40.000000Z" ,
"updated_at" : "2026-01-31T12:15:40.000000Z"
}
] ,
"reverse_total" : 199.56 ,
"refund_total" : 199.56 ,
"refund" : null ,
"available_refund_payment_methods" : [
{
"name" : "Bank Transfer" ,
"code" : "zid_bank_transfer"
}
] ,
"shipment_status" : null
} ,
"message" : {
"type" : "object" ,
"code" : null ,
"name" : null ,
"description" : null
}
} `
```

Modified at 2026-02-09 07:38:20

Previous

Reverse Orders

Next

Create Reverse Orders Waybill
