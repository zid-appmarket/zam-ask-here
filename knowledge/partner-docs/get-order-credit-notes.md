---
# Synced from https://docs.zid.sa/get-order-credit-notes
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-get-order-credit-notes
title: "List Order Credit Notes"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/get-order-credit-notes
tags: [from-docs-site, partner-docs]
language: en
---

> List Order Credit Notes - Zid Docs
# List Order Credit Notes

GET

https://api.zid.sa/ v1/managers/store/orders/{order-id}/credit-notes

The GET Credit Notes endpoint allows you to retrieve a list of credit notes associated with an order from the system. Credit notes are issued for orders that have been cancelled or modified, and this endpoint provides detailed information about each credit note, including customer details, product information, and payment details.

🔑Scopes

`orders.read` - Orders Read

## Request

Path Params

###

Header Params

###

## Responses

🟢 200 OK

application/json

Body application/json

###

🟠 401 Unauthorized

🟠 403 Permission Denied

🟠 404 Not Found

🔴 500 Internal Server error

Request Request Example

Shell

JavaScript

Java

Swift

```
` curl --location 'https://api.zid.sa/v1/managers/store/orders/59214748/credit-notes' \
--header 'Accept: application/json' \
--header 'Authorization: {{Autherization}}' \
--header 'X-manager-Token: {{Access-Token}}' \
--header 'Accept-Language: en' \
--header 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36' `
```

Response Response Example

200 - Success

```
` {
"code" : "SUCCESS_WITH_SINGLE_PAYLOAD_OBJECT" ,
"message" : null ,
"payload" : {
"credit_notes" : [
{
"id" : "a46ebd12-1392-488c-88f3-66d1835e1e32" ,
"order_id" : 59214748 ,
"store_id" : 3 ,
"invoice_type" : "credit_note" ,
"translated_invoice_type" : "Credit note" ,
"original_invoice_number" : 59214748 ,
"invoice_number" : 1133976 ,
"issue_reason" : "issue_reason_update" ,
"invoice_title" : "Updated order" ,
"translated_issue_reason" : "Order update" ,
"store_name" : "Mohammed Zayan" ,
"shipping_method_code" : "zid_shipping.option_574614" ,
"store_url" : "https://osama.zid.store/" ,
"order_status" : {
"name" : "جديد" ,
"code" : "new"
} ,
"payment_status" : "paid" ,
"currency_code" : "SAR" ,
"customer" : {
"id" : 37 ,
"name" : "Osama Khaled" ,
"email" : "osamakhaled2010@gmail.com" ,
"mobile" : "966503187421" ,
"note" : "" ,
"type" : "individual"
} ,
"has_different_consignee" : 0 ,
"order_total" : "143.4500" ,
"order_total_string" : "143.45 SAR" ,
"products_sum_total_string" : "68.00 SAR" ,
"has_different_transaction_currency" : false ,
"transaction_reference" : null ,
"transaction_amount" : "143.4500" ,
"transaction_amount_string" : "143.45 SAR" ,
"return_policy" : "ojghwriojgbwriojgwergiou" ,
"items" : [
{
"id" : "dfd6d0fa-dc45-49f7-b8dc-05d209d9bf8c" ,
"product_id" : "2a39d7b88d9d4040b636ab9a085b540d" ,
"code" : null ,
"name" : "ماء تونر جينسينغ من بيوتي اوف جوسون" ,
"custom_fields" : [ ] ,
"sku" : "glow1114" ,
"quantity" : 1 ,
"is_taxable" : true ,
"is_discounted" : false ,
"meta" : null ,
"weight" : null ,
"net_price_with_additions" : 59.1304 ,
"net_price_with_additions_string" : "59.13 SAR" ,
"price_with_additions" : 68 ,
"price_with_additions_string" : "68.00 SAR" ,
"net_price" : "59.1304" ,
"net_price_string" : "59.13 SAR" ,
"net_sale_price" : null ,
"net_sale_price_string" : null ,
"net_additions_price" : 0 ,
"net_additions_price_string" : null ,
"original_price" : null ,
"original_price_string" : null ,
"gross_price" : 68 ,
"gross_price_string" : "68.00 SAR" ,
"gross_sale_price" : null ,
"gross_sale_price_string" : null ,
"price_before" : null ,
"price_before_string" : null ,
"total_before" : null ,
"total_before_string" : null ,
"gross_additions_price" : 0 ,
"gross_additions_price_string" : null ,
"tax_percentage" : 0.15 ,
"tax_amount" : 8.8696 ,
"tax_amount_string" : "8.87 SAR" ,
"tax_amount_string_per_item" : "8.86 SAR" ,
"sale_price" : null ,
"sale_price_string" : null ,
"price" : 68 ,
"price_string" : "68.00 SAR" ,
"additions_price" : 0 ,
"additions_price_string" : "0.00 SAR" ,
"total" : 68 ,
"total_string" : "68.00 SAR" ,
"images" : [
{
"id" : "ffe37efb-2e27-4002-9175-9f764687f9a7" ,
"origin" : "https://media.zid.store/thumbs/d297fb8b-c322-412e-a2f4-ffa96dc57022/ffe37efb-2e27-4002-9175-9f764687f9a7-thumbnail-500x500-70.jpg" ,
"thumbs" : {
"fullSize" : "https://media.zid.store/d297fb8b-c322-412e-a2f4-ffa96dc57022/ffe37efb-2e27-4002-9175-9f764687f9a7.jpg" ,
"thumbnail" : "https://media.zid.store/thumbs/d297fb8b-c322-412e-a2f4-ffa96dc57022/ffe37efb-2e27-4002-9175-9f764687f9a7-thumbnail-370x370-70.jpg" ,
"small" : "https://media.zid.store/thumbs/d297fb8b-c322-412e-a2f4-ffa96dc57022/ffe37efb-2e27-4002-9175-9f764687f9a7-thumbnail-500x500-70.jpg" ,
"medium" : "https://media.zid.store/thumbs/d297fb8b-c322-412e-a2f4-ffa96dc57022/ffe37efb-2e27-4002-9175-9f764687f9a7-thumbnail-770x770-70.jpg" ,
"large" : "https://media.zid.store/thumbs/d297fb8b-c322-412e-a2f4-ffa96dc57022/ffe37efb-2e27-4002-9175-9f764687f9a7-thumbnail-1000x1000-70.jpg"
}
}
] ,
"shipping" : false ,
"options" : [ ] ,
"barcode" : null
}
] ,
"shipping" : {
"address" : {
"district" : "حي قرطبة" ,
"street" : "معسكر" ,
"city" : {
"id" : 1 ,
"name" : "Riyadh"
} ,
"country" : {
"id" : 184 ,
"name" : "Saudi Arabia"
} ,
"meta" : {
"editable_order_cart_id" : "3:69712c34860aa59fbc2a180b" ,
"shipping_address_meta" : {
"building_number" : "73829" ,
"postcode" : "" ,
"additional_number" : "" ,
"city_name" : ""
}
}
} ,
"method" : {
"id" : 574614 ,
"type" : "delivery" ,
"is_system_option" : true ,
"name" : "الشريك الثالث" ,
"estimated_delivery_time" : null ,
"code" : "zid_shipping.option_574614" ,
"icon" : "https://media.zid.store/apps/91f12581-2275-481e-9437-da14f6633f4d.png" ,
"tracking_number" : null
}
} ,
"payment" : {
"invoice" : [
{
"code" : "sub_totals_before_vat" ,
"value" : "59.1304" ,
"value_string" : "59.13 SAR" ,
"title" : "Total without VAT"
} ,
{
"code" : "taxable_amount" ,
"value" : "59.1304" ,
"value_string" : "59.13 SAR" ,
"title" : "Taxable amount"
} ,
{
"code" : "vat" ,
"value" : "8.8696" ,
"value_string" : "8.87 SAR" ,
"title" : "VAT (%15)"
} ,
{
"code" : "total" ,
"value" : "68.0000" ,
"value_string" : "68.00 SAR" ,
"title" : "Total"
}
] ,
"method" : {
"id" : 813413 ,
"name" : "Bank Transfer" ,
"code" : "zid_bank_transfer" ,
"type" : "zid_bank_transfer"
}
} ,
"payment_method" : {
"name" : "تحويل بنكي"
} ,
"customer_note" : "" ,
"currency" : {
"order_currency" : {
"id" : 4 ,
"code" : "SAR" ,
"exchange_rate" : 1
} ,
"order_store_currency" : {
"id" : 4 ,
"code" : "SAR" ,
"exchange_rate" : null
}
} ,
"coupon" : null ,
"items_count" : 1 ,
"original_order_date" : "13-10-2025 | 10:53 ص" ,
"issue_date" : "31-01-2026 | 01:32 ص" ,
"created_at" : "2026-01-30 22:32:24" ,
"updated_at" : "2026-01-30 22:32:24" ,
"zatca" : {
"qr_code_data" : "AQACDzMxMTExMTExMTExMTExMwMUMjAyNi0wMS0zMFQyMjozMjoyNFoEAjY4BQQ4Ljg3"
}
} ,
{
"id" : "ca2dc662-9ee4-4fb5-a543-74693946ef4c" ,
"order_id" : 59214748 ,
"store_id" : 3 ,
"invoice_type" : "debit_note" ,
"translated_invoice_type" : "Debit note" ,
"original_invoice_number" : 59214748 ,
"invoice_number" : 1122155 ,
"issue_reason" : "issue_reason_update" ,
"invoice_title" : "Updated order" ,
"translated_issue_reason" : "Order update" ,
"store_name" : "Mohammed Zayan" ,
"shipping_method_code" : "zid_shipping.option_574614" ,
"store_url" : "https://osama.zid.store/" ,
"order_status" : {
"name" : "جديد" ,
"code" : "new"
} ,
"payment_status" : "paid" ,
"currency_code" : "SAR" ,
"customer" : {
"id" : 37 ,
"name" : "Osama Khaled" ,
"email" : "osamakhaled2010@gmail.com" ,
"mobile" : "966503187421" ,
"note" : "" ,
"type" : "individual"
} ,
"has_different_consignee" : 0 ,
"order_total" : "211.4500" ,
"order_total_string" : "211.45 SAR" ,
"products_sum_total_string" : "68.00 SAR" ,
"has_different_transaction_currency" : false ,
"transaction_reference" : null ,
"transaction_amount" : "211.4500" ,
"transaction_amount_string" : "211.45 SAR" ,
"return_policy" : "ojghwriojgbwriojgwergiou" ,
"items" : [
{
"id" : "bb15784e-e525-4438-bb3b-27871d3baae6" ,
"product_id" : "2a39d7b88d9d4040b636ab9a085b540d" ,
"code" : null ,
"name" : "ماء تونر جينسينغ من بيوتي اوف جوسون" ,
"custom_fields" : [ ] ,
"sku" : "glow1114" ,
"quantity" : 1 ,
"is_taxable" : true ,
"is_discounted" : false ,
"meta" : null ,
"weight" : null ,
"net_price_with_additions" : 59.1304 ,
"net_price_with_additions_string" : "59.13 SAR" ,
"price_with_additions" : 68 ,
"price_with_additions_string" : "68.00 SAR" ,
"net_price" : "59.1304" ,
"net_price_string" : "59.13 SAR" ,
"net_sale_price" : null ,
"net_sale_price_string" : null ,
"net_additions_price" : 0 ,
"net_additions_price_string" : null ,
"original_price" : null ,
"original_price_string" : null ,
"gross_price" : 68 ,
"gross_price_string" : "68.00 SAR" ,
"gross_sale_price" : null ,
"gross_sale_price_string" : null ,
"price_before" : null ,
"price_before_string" : null ,
"total_before" : null ,
"total_before_string" : null ,
"gross_additions_price" : 0 ,
"gross_additions_price_string" : null ,
"tax_percentage" : 0.15 ,
"tax_amount" : 8.8696 ,
"tax_amount_string" : "8.87 SAR" ,
"tax_amount_string_per_item" : "8.86 SAR" ,
"sale_price" : null ,
"sale_price_string" : null ,
"price" : 68 ,
"price_string" : "68.00 SAR" ,
"additions_price" : 0 ,
"additions_price_string" : "0.00 SAR" ,
"total" : 68 ,
"total_string" : "68.00 SAR" ,
"images" : [
{
"id" : "ffe37efb-2e27-4002-9175-9f764687f9a7" ,
"origin" : "https://media.zid.store/thumbs/d297fb8b-c322-412e-a2f4-ffa96dc57022/ffe37efb-2e27-4002-9175-9f764687f9a7-thumbnail-500x500-70.jpg" ,
"thumbs" : {
"fullSize" : "https://media.zid.store/d297fb8b-c322-412e-a2f4-ffa96dc57022/ffe37efb-2e27-4002-9175-9f764687f9a7.jpg" ,
"thumbnail" : "https://media.zid.store/thumbs/d297fb8b-c322-412e-a2f4-ffa96dc57022/ffe37efb-2e27-4002-9175-9f764687f9a7-thumbnail-370x370-70.jpg" ,
"small" : "https://media.zid.store/thumbs/d297fb8b-c322-412e-a2f4-ffa96dc57022/ffe37efb-2e27-4002-9175-9f764687f9a7-thumbnail-500x500-70.jpg" ,
"medium" : "https://media.zid.store/thumbs/d297fb8b-c322-412e-a2f4-ffa96dc57022/ffe37efb-2e27-4002-9175-9f764687f9a7-thumbnail-770x770-70.jpg" ,
"large" : "https://media.zid.store/thumbs/d297fb8b-c322-412e-a2f4-ffa96dc57022/ffe37efb-2e27-4002-9175-9f764687f9a7-thumbnail-1000x1000-70.jpg"
}
}
] ,
"shipping" : false ,
"options" : [ ] ,
"barcode" : null
}
] ,
"shipping" : {
"address" : {
"district" : "حي قرطبة" ,
"street" : "معسكر" ,
"city" : {
"id" : 1 ,
"name" : "Riyadh"
} ,
"country" : {
"id" : 184 ,
"name" : "Saudi Arabia"
} ,
"meta" : {
"editable_order_cart_id" : "3:6970e9f1481430d3d8d90101" ,
"shipping_address_meta" : {
"building_number" : "11" ,
"short_address" : "RUQB4314"
}
}
} ,
"method" : {
"id" : 574614 ,
"type" : "delivery" ,
"is_system_option" : true ,
"name" : "الشريك الثالث" ,
"estimated_delivery_time" : null ,
"code" : "zid_shipping.option_574614" ,
"icon" : "https://media.zid.store/apps/91f12581-2275-481e-9437-da14f6633f4d.png" ,
"tracking_number" : null
}
} ,
"payment" : {
"invoice" : [
{
"code" : "sub_totals_before_vat" ,
"value" : "59.1304" ,
"value_string" : "59.13 SAR" ,
"title" : "Total without VAT"
} ,
{
"code" : "taxable_amount" ,
"value" : "59.1304" ,
"value_string" : "59.13 SAR" ,
"title" : "Taxable amount"
} ,
{
"code" : "vat" ,
"value" : "8.8696" ,
"value_string" : "8.87 SAR" ,
"title" : "VAT (%15)"
} ,
{
"code" : "total" ,
"value" : "68.0000" ,
"value_string" : "68.00 SAR" ,
"title" : "Total"
}
] ,
"method" : {
"id" : 813413 ,
"name" : "Bank Transfer" ,
"code" : "zid_bank_transfer" ,
"type" : "zid_bank_transfer"
}
} ,
"payment_method" : {
"name" : "تحويل بنكي"
} ,
"customer_note" : "" ,
"currency" : {
"order_currency" : {
"id" : 4 ,
"code" : "SAR" ,
"exchange_rate" : 1
} ,
"order_store_currency" : {
"id" : 4 ,
"code" : "SAR" ,
"exchange_rate" : null
}
} ,
"coupon" : null ,
"items_count" : 1 ,
"original_order_date" : "13-10-2025 | 10:53 ص" ,
"issue_date" : "21-01-2026 | 06:00 م" ,
"created_at" : "2026-01-21 15:00:22" ,
"updated_at" : "2026-01-21 15:00:22" ,
"zatca" : {
"qr_code_data" : "AQACDzMxMTExMTExMTExMTExMwMUMjAyNi0wMS0yMVQxNTowMDoyMloEAjY4BQQ4Ljg3"
}
}
] ,
"returned_items" : [
{
"id" : "dfd6d0fa-dc45-49f7-b8dc-05d209d9bf8c" ,
"product_id" : "2a39d7b88d9d4040b636ab9a085b540d" ,
"code" : null ,
"name" : "ماء تونر جينسينغ من بيوتي اوف جوسون" ,
"custom_fields" : [ ] ,
"sku" : "glow1114" ,
"quantity" : 1 ,
"is_taxable" : true ,
"is_discounted" : false ,
"meta" : null ,
"weight" : null ,
"net_price_with_additions" : 59.1304 ,
"net_price_with_additions_string" : "59.13 SAR" ,
"price_with_additions" : 68 ,
"price_with_additions_string" : "68.00 SAR" ,
"net_price" : "59.1304" ,
"net_price_string" : "59.13 SAR" ,
"net_sale_price" : null ,
"net_sale_price_string" : null ,
"net_additions_price" : 0 ,
"net_additions_price_string" : null ,
"original_price" : null ,
"original_price_string" : null ,
"gross_price" : 68 ,
"gross_price_string" : "68.00 SAR" ,
"gross_sale_price" : null ,
"gross_sale_price_string" : null ,
"price_before" : null ,
"price_before_string" : null ,
"total_before" : null ,
"total_before_string" : null ,
"gross_additions_price" : 0 ,
"gross_additions_price_string" : null ,
"tax_percentage" : 0.15 ,
"tax_amount" : 8.8696 ,
"tax_amount_string" : "8.87 SAR" ,
"tax_amount_string_per_item" : "8.86 SAR" ,
"sale_price" : null ,
"sale_price_string" : null ,
"price" : 68 ,
"price_string" : "68.00 SAR" ,
"additions_price" : 0 ,
"additions_price_string" : "0.00 SAR" ,
"total" : 68 ,
"total_string" : "68.00 SAR" ,
"images" : [
{
"id" : "ffe37efb-2e27-4002-9175-9f764687f9a7" ,
"origin" : "https://media.zid.store/thumbs/d297fb8b-c322-412e-a2f4-ffa96dc57022/ffe37efb-2e27-4002-9175-9f764687f9a7-thumbnail-500x500-70.jpg" ,
"thumbs" : {
"fullSize" : "https://media.zid.store/d297fb8b-c322-412e-a2f4-ffa96dc57022/ffe37efb-2e27-4002-9175-9f764687f9a7.jpg" ,
"thumbnail" : "https://media.zid.store/thumbs/d297fb8b-c322-412e-a2f4-ffa96dc57022/ffe37efb-2e27-4002-9175-9f764687f9a7-thumbnail-370x370-70.jpg" ,
"small" : "https://media.zid.store/thumbs/d297fb8b-c322-412e-a2f4-ffa96dc57022/ffe37efb-2e27-4002-9175-9f764687f9a7-thumbnail-500x500-70.jpg" ,
"medium" : "https://media.zid.store/thumbs/d297fb8b-c322-412e-a2f4-ffa96dc57022/ffe37efb-2e27-4002-9175-9f764687f9a7-thumbnail-770x770-70.jpg" ,
"large" : "https://media.zid.store/thumbs/d297fb8b-c322-412e-a2f4-ffa96dc57022/ffe37efb-2e27-4002-9175-9f764687f9a7-thumbnail-1000x1000-70.jpg"
}
}
] ,
"shipping" : false ,
"options" : [ ] ,
"barcode" : null
} ,
{
"id" : "bb15784e-e525-4438-bb3b-27871d3baae6" ,
"product_id" : "2a39d7b88d9d4040b636ab9a085b540d" ,
"code" : null ,
"name" : "ماء تونر جينسينغ من بيوتي اوف جوسون" ,
"custom_fields" : [ ] ,
"sku" : "glow1114" ,
"quantity" : 1 ,
"is_taxable" : true ,
"is_discounted" : false ,
"meta" : null ,
"weight" : null ,
"net_price_with_additions" : 59.1304 ,
"net_price_with_additions_string" : "59.13 SAR" ,
"price_with_additions" : 68 ,
"price_with_additions_string" : "68.00 SAR" ,
"net_price" : "59.1304" ,
"net_price_string" : "59.13 SAR" ,
"net_sale_price" : null ,
"net_sale_price_string" : null ,
"net_additions_price" : 0 ,
"net_additions_price_string" : null ,
"original_price" : null ,
"original_price_string" : null ,
"gross_price" : 68 ,
"gross_price_string" : "68.00 SAR" ,
"gross_sale_price" : null ,
"gross_sale_price_string" : null ,
"price_before" : null ,
"price_before_string" : null ,
"total_before" : null ,
"total_before_string" : null ,
"gross_additions_price" : 0 ,
"gross_additions_price_string" : null ,
"tax_percentage" : 0.15 ,
"tax_amount" : 8.8696 ,
"tax_amount_string" : "8.87 SAR" ,
"tax_amount_string_per_item" : "8.86 SAR" ,
"sale_price" : null ,
"sale_price_string" : null ,
"price" : 68 ,
"price_string" : "68.00 SAR" ,
"additions_price" : 0 ,
"additions_price_string" : "0.00 SAR" ,
"total" : 68 ,
"total_string" : "68.00 SAR" ,
"images" : [
{
"id" : "ffe37efb-2e27-4002-9175-9f764687f9a7" ,
"origin" : "https://media.zid.store/thumbs/d297fb8b-c322-412e-a2f4-ffa96dc57022/ffe37efb-2e27-4002-9175-9f764687f9a7-thumbnail-500x500-70.jpg" ,
"thumbs" : {
"fullSize" : "https://media.zid.store/d297fb8b-c322-412e-a2f4-ffa96dc57022/ffe37efb-2e27-4002-9175-9f764687f9a7.jpg" ,
"thumbnail" : "https://media.zid.store/thumbs/d297fb8b-c322-412e-a2f4-ffa96dc57022/ffe37efb-2e27-4002-9175-9f764687f9a7-thumbnail-370x370-70.jpg" ,
"small" : "https://media.zid.store/thumbs/d297fb8b-c322-412e-a2f4-ffa96dc57022/ffe37efb-2e27-4002-9175-9f764687f9a7-thumbnail-500x500-70.jpg" ,
"medium" : "https://media.zid.store/thumbs/d297fb8b-c322-412e-a2f4-ffa96dc57022/ffe37efb-2e27-4002-9175-9f764687f9a7-thumbnail-770x770-70.jpg" ,
"large" : "https://media.zid.store/thumbs/d297fb8b-c322-412e-a2f4-ffa96dc57022/ffe37efb-2e27-4002-9175-9f764687f9a7-thumbnail-1000x1000-70.jpg"
}
}
] ,
"shipping" : false ,
"options" : [ ] ,
"barcode" : null
}
]
}
} `
```

Modified at 2026-01-30 22:31:15

Previous

List Custom Order Statuses

Next

Get Orders Highlights
