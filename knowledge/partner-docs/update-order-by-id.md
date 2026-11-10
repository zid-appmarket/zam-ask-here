---
# Synced from https://docs.zid.sa/update-order-by-id
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-update-order-by-id
title: "Change Order Status"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/update-order-by-id
tags: [from-docs-site, partner-docs]
language: en
---

> Change Order Status - Zid Docs
# Change Order Status

POST

https://api.zid.sa/ v1/managers/store/orders/{order-id}/change-order-status

Please note that if the order is shipped through an integrated shipping company, then we cannot update the order status from "Ready" to "New".

To deliver the order through a shipping company, you need to change the order status to ready, and send the `inventory_address_id` value with your request, hence shipping companies need to know which pickup point to get the package from. To get a list of your current inventory addresses along with their ids, please check the inventory addresses API (https://docs.zid.sa/docs/zid-merchant-api/59b14f9f24f3a-get-inventory-addresses) endpoint.

Available order statuses are as follows: (`new`, `preparing`, `ready`, `indelivery`, `delivered`, `cancelled`, `reversed`, `reverse_in_progress`, `partially_reversed`)

The endpoint now **`accepts a custom status code`** in addition to predefined codes.

🔑 Scopes

`orders.read_write` - Orders Read & Write

🔑 Permission

`can:orders.status.change`

## Note #

When the order status is changed to `delivered` and product reviews are enabled for the store, `products[].review_url `is populated in the same response. No additional order retrieval request is required.

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

🟠 403 Permission Denied

🟠 400 Bad Request

🔴 500 Internal Server error

Request Request Example

Shell

JavaScript

Java

Swift

```
` curl --location 'https://api.zid.sa/v1/managers/store/orders/64086815/change-order-status' \
--header 'Authorization: {{Autherization}}' \
--header 'Accept: application/json' \
--header 'Accept-Language: en' \
--header 'X-MANAGER-TOKEN: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
"order_status": "cancelled",
"comment": "Cancelled by merchant",
"inventory_address_id": "dffdaac2-441e-42cb-8bb7-2ac733f63c43",
"inventory_location_id": "dffdaac2-441e-42cb-8bb7-2ac733f63c43",
"marketplace_cancellation_reason": "NoInventory",
"tracking_number": "123456",
"tracking_url": "",
"waybill_url": "",
"params": {
"packages_count": 3
}
}' `
```

Response Response Example

200 - Example 1

```
` {
"status" : "string" ,
"order" : {
"id" : 63945643 ,
"invoice_number" : 63945643 ,
"code" : "4lF4p7HluM" ,
"store_id" : 3 ,
"order_url" : "https://osama.zid.store/o/4lF4p7HluM/inv" ,
"store_name" : "متجر أسامة." ,
"shipping_method_code" : "custom" ,
"store_url" : "https://osama.zid.store/" ,
"currency_code" : "SAR" ,
"order_status" : {
"name" : "جديد" ,
"code" : "new"
} ,
"display_status" : {
"id" : 1 ,
"code" : "new" ,
"color" : "#3498db" ,
"name" : "جديد"
} ,
"customer" : {
"id" : 1441 ,
"name" : "John Doe" ,
"email" : "test@mail.com" ,
"mobile" : "966123456789" ,
"note" : "" ,
"verified" : 1 ,
"type" : "individual" ,
"business_name" : "string" ,
"tax_number" : "string" ,
"commercial_registration" : "string"
} ,
"has_different_consignee" : 0 ,
"is_guest_customer" : 0 ,
"is_gift_order" : 0 ,
"gift_card_details" : { } ,
"consignee" : {
"name" : "string" ,
"email" : "string" ,
"mobile" : "string"
} ,
"is_quick_checkout_order" : true ,
"order_total" : "string" ,
"order_total_string" : "201.86 SAR" ,
"has_different_transaction_currency" : true ,
"transaction_reference" : "string" ,
"transaction_amount" : 201.85999896568 ,
"transaction_amount_string" : "201.86 SAR" ,
"issue_date" : "string" ,
"payment_status" : "pending" ,
"is_potential_fraud" : true ,
"source" : "string" ,
"source_code" : "string" ,
"is_reseller_transaction" : true ,
"created_at" : "2026-01-26 10:21:08" ,
"updated_at" : "2026-01-26 10:21:08" ,
"is_on_demand" : true ,
"import_id" : "string" ,
"store_logo" : "string" ,
"store_uuid" : "string" ,
"tags" : [
{
"id" : "string" ,
"name" : "string" ,
"store_id" : "string" ,
"user_id" : "string" ,
"orders" : [
"string"
]
}
] ,
"marketing_source" : {
"utm_id" : "" ,
"utm_source" : "" ,
"utm_medium" : "" ,
"utm_campaign" : "" ,
"utm_term" : "" ,
"utm_content" : "" ,
"referer" : "organic" ,
"platform" : "unknown" ,
"device_type" : "unknown" ,
"browser" : null ,
"os" : null ,
"ip" : "192.168.162.93" ,
"ip_country" : null ,
"ip_content" : null ,
"ip_city" : null ,
"ip_region" : null ,
"ip_timezone" : null
} ,
"requires_shipping" : true ,
"should_merchant_set_shipping_method" : true ,
"shipping" : {
"method" : {
"id" : 0 ,
"name" : "string" ,
"code" : "string" ,
"estimated_delivery_time" : "string" ,
"icon" : "string" ,
"is_system_option" : true ,
"waybill" : "string" ,
"had_errors_while_fetching_waybill" : true ,
"waybill_tracking_id" : "string" ,
"has_waybill_and_packing_list" : true ,
"tracking" : {
"number" : "string" ,
"status" : "string" ,
"url" : "string"
} ,
"order_shipping_status" : "string" ,
"inventory_address" : [
"string"
] ,
"courier" : {
"name" : {
"ar" : "string" ,
"en" : "string"
} ,
"code" : "string" ,
"logo" : "string" ,
"identifier" : "string"
} ,
"return_shipment" : [
"string"
] ,
"packages_count" : 0
} ,
"address" : {
"formatted_address" : "string" ,
"street" : "string" ,
"district" : "string" ,
"lat" : 0 ,
"lng" : 0 ,
"short_address" : "string" ,
"meta" : {
"building_number" : "string" ,
"postcode" : "string" ,
"additional_number" : "string" ,
"city_name" : "string"
} ,
"city" : {
"id" : 0 ,
"name" : "string"
} ,
"country" : {
"id" : 0 ,
"name" : "string"
}
}
} ,
"payment" : {
"method" : {
"name" : "string" ,
"code" : "hyperpay" ,
"type" : "string" ,
"cart_payment_request_token" : "string" ,
"transaction_status" : "string" ,
"transaction_status_name" : "string" ,
"transaction_bank" : "string" ,
"transaction_slip" : "string" ,
"transaction_sender_name" : "string" ,
"updated_at" : "string"
} ,
"invoice" : [
{
"code" : "string" ,
"value" : "string" ,
"value_string" : "string" ,
"title" : "string"
}
] ,
"split_payments" : [
{
"name" : "string" ,
"code" : "string" ,
"amount" : 0 ,
"amount_string" : "string" ,
"near_pay_transaction_uuid" : "string" ,
"near_pay_transaction_details" : "string"
}
]
} ,
"cod_confirmed" : true ,
"reverse_order_label_request" : {
"id" : "string" ,
"store_id" : "string" ,
"order_id" : 0 ,
"is_partial" : 0 ,
"consignee_name" : "string" ,
"consignee_mobile" : "string" ,
"consignee_city" : { } ,
"consignee_address_1" : "string" ,
"consignee_address_2" : "string" ,
"inventory_address_id" : 0 ,
"inventory_location_id" : "string" ,
"inventory" : { } ,
"reason" : [
"string"
] ,
"shipping_method" : "string" ,
"waybill" : { } ,
"products" : [
{ }
]
} ,
"reverse_order_label_requests" : [
{
"id" : "string" ,
"store_id" : "string" ,
"order_id" : 0 ,
"is_partial" : 0 ,
"consignee_name" : "string" ,
"consignee_mobile" : "string" ,
"consignee_city" : { } ,
"consignee_address_1" : "string" ,
"consignee_address_2" : "string" ,
"inventory_address_id" : 0 ,
"inventory_location_id" : "string" ,
"inventory" : { } ,
"reason" : [
"string"
] ,
"shipping_method" : "string" ,
"waybill" : { } ,
"products" : [
{ }
]
}
] ,
"customer_note" : "string" ,
"gift_message" : "string" ,
"payment_link" : "string" ,
"service_fee_invoice_link" : "string" ,
"weight" : 0 ,
"weight_cost_details" : [
"string"
] ,
"currency" : {
"order_currency" : {
"id" : 0 ,
"code" : "string" ,
"exchange_rate" : 0
} ,
"order_store_currency" : {
"id" : 0 ,
"code" : "string" ,
"exchange_rate" : 0
}
} ,
"coupon" : {
"id" : 0 ,
"code" : "string" ,
"name" : "string" ,
"discount" : "string" ,
"discount_string" : "string"
} ,
"products" : [
{
"id" : "003140e2-9d8e-462d-b823-373407746871" ,
"order_product_id" : 0 ,
"parent_id" : "string" ,
"parent_name" : "string" ,
"parent_sku" : "null" ,
"review_url" : "null" ,
"product_class" : "string" ,
"name" : "طقم سفر للحواجب سوبرستار من بنفت" ,
"short_description" : {
"ar" : "string" ,
"en" : "string"
} ,
"sku" : "Z.217795.169603646831188" ,
"barcode" : "string" ,
"custom_fields" : [
{
"type" : "string" ,
"value" : "string" ,
"formatted_value" : "string" ,
"name" : "string" ,
"label" : "string"
}
] ,
"quantity" : 1 ,
"weight" : {
"value" : 1.2 ,
"unit" : "kg"
} ,
"is_taxable" : true ,
"is_discounted" : true ,
"vouchers" : [
{
"id" : "string" ,
"product_id" : "string" ,
"status" : "string" ,
"order" : 0 ,
"serial_number" : "string" ,
"key" : "string" ,
"pin_code" : "string" ,
"expires_at" : "string" ,
"updated_at" : "string" ,
"created_at" : "string" ,
"expires_at_formatted" : "string"
}
] ,
"downloadables" : [
{
"download_url" : "string" ,
"download_limit" : 0 ,
"download_requests_count" : 0 ,
"expiration_period" : 0 ,
"is_external" : true ,
"display_name" : "string"
}
] ,
"downloadables_zipped" : [
{
"download_url" : "string" ,
"download_limit" : 0 ,
"download_requests_count" : 0 ,
"expiration_period" : 0 ,
"is_external" : true ,
"display_name" : "string"
}
] ,
"meta" : { } ,
"is_external_product" : true ,
"discounts" : [
"string"
] ,
"net_price_with_additions" : 0 ,
"net_price_with_additions_string" : "string" ,
"price_with_additions" : 0 ,
"price_with_additions_string" : "string" ,
"net_price" : "string" ,
"net_price_string" : "string" ,
"net_sale_price" : "string" ,
"net_sale_price_string" : "string" ,
"net_additions_price" : 0 ,
"net_additions_price_string" : "string" ,
"gross_price" : 0 ,
"gross_price_string" : "string" ,
"gross_sale_price" : "string" ,
"gross_sale_price_string" : "string" ,
"price_before" : 0 ,
"price_before_string" : "string" ,
"total_before" : 0 ,
"total_before_string" : "string" ,
"gross_additions_price" : 0 ,
"gross_additions_price_string" : "string" ,
"discount_percentage" : 0 ,
"tax_percentage" : 0.15 ,
"tax_amount" : "string" ,
"tax_amount_string" : "26.03 SAR" ,
"tax_amount_string_per_item" : "string" ,
"discounted_tax_amount" : 0 ,
"discounted_tax_amount_string" : "string" ,
"discounted_tax_amount_string_per_item" : "string" ,
"price" : 199.55999896568 ,
"price_string" : "199.56 SAR" ,
"additions_price" : 0 ,
"additions_price_string" : "string" ,
"total" : 0 ,
"total_string" : "string" ,
"discounted_total" : 0 ,
"discounted_total_string" : "string" ,
"images" : [
{
"id" : "string" ,
"origin" : "string" ,
"thumbs" : {
"fullSize" : "string" ,
"thumbnail" : "string" ,
"small" : "string" ,
"medium" : "string" ,
"large" : "string"
}
}
] ,
"options" : [
"string"
]
}
] ,
"products_count" : 1 ,
"products_sum_total_string" : "string" ,
"language" : "string" ,
"histories" : [
{
"order_status_id" : 0 ,
"order_status_name" : "New" ,
"changed_by_id" : 0 ,
"changed_by_type" : "Admin" ,
"changed_by_details" : {
"action" : "string" ,
"by" : "string" ,
"comment" : "string"
} ,
"comment" : "Order has been created." ,
"created_at" : "2026-01-26 10:21:10" ,
"humanized_created_at" : "1 second ago"
}
] ,
"product_ids" : [
"string"
] ,
"is_reactivated" : true ,
"return_policy" : "string" ,
"packages_count" : 0 ,
"inventory_address" : {
"id" : "string" ,
"name" : "string" ,
"city" : {
"name" : "Other" ,
"id" : 1 ,
"national_id" : 3 ,
"priority" : 10 ,
"country_id" : 184 ,
"country_name" : "السعودية" ,
"country_code" : "SA" ,
"ar_name" : "الرياض" ,
"en_name" : "Riyadh"
} ,
"street" : "string" ,
"district" : "string" ,
"postal_code" : "string" ,
"coordinates" : {
"lat" : 0 ,
"lon" : 0
} ,
"cop_enabled" : true ,
"is_pickup_option" : true ,
"is_zidship_default" : true ,
"working_hours" : [
{
"day_name" : "string" ,
"time_from" : "string" ,
"time_to" : "string"
}
] ,
"full_address" : "string" ,
"short_address" : "string"
} ,
"expected_shipping_method_type" : "string" ,
"reseller_meta" : [
"string"
] ,
"zidship_ticket_number" : "string" ,
"edits_count" : 0 ,
"delivered_at" : "string" ,
"is_marketplace_order" : true ,
"marketplace_commission" : {
"commission_percentage" : 0 ,
"commision_amount" : "string" ,
"tax_percentage" : 0 ,
"tax_amount" : "string" ,
"total" : "string"
} ,
"pos_invoice_number" : "string" ,
"return_invoice_number" : "string" ,
"invoice_link" : "string" ,
"payment_network" : "string" ,
"digital_products_access_token" : "string"
} ,
"message" : {
"type" : "string" ,
"code" : "string" ,
"name" : "string" ,
"description" : "string"
}
} `
```

Modified at 2026-09-21 10:33:53

Previous

Create Order

Next

Add Order Comment
