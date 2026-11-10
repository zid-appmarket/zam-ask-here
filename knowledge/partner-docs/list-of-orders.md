---
# Synced from https://docs.zid.sa/list-of-orders
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-list-of-orders
title: "List Orders"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/list-of-orders
tags: [from-docs-site, partner-docs]
language: en
---

> List Orders - Zid Docs
# List Orders

GET

https://api.zid.sa/ v1/managers/store/orders

Orders can be created either by the customers from the storefronts or by the merchants from their dashboard.

Use this endpoint to retrieve a list of orders filtered by specific parameters.

**Important Note**

To retrieve products inside each order in the List Orders API, you must use the query parameter:

```
``
```

Without this parameter, the API defaults to "`simple`", which does not include products.

**Data Masking for Marketplace Orders**

When `is_marketplace_order` is true, the order is from an external provider, and certain customer information, such as `customer.name`, `customer.email`, and `customer.phone`, will be masked for privacy. For example, names like "John Doe" become "J*** D***", emails are masked as "t***@.", and phone numbers as "***00". Masked data may not follow proper syntax. Additionally, for marketplace orders, `customer.phone` may be `null` if not provided.

🔑Scopes

`orders.read` - Orders Read

## Request

Query Params

###

Header Params

###

## Responses

🟢 200 Simple

application/json

Body application/json

###

🟢 200 Default

🟢 200 Tiny

🟢 200 POS

🟢 200 Print

🟢 200 Print Summary

🟠 401 Unauthorized

🔴 500 Internal Server error

Request Request Example

Shell

JavaScript

Java

Swift

```
` curl --location 'https://api.zid.sa/v1/managers/store/orders?payload_type=simple&page=1&per_page=15' \
--header 'Authorization: {{Autherization}}' \
--header 'X-Manager-Token: {{Access-Token}}' \
--header 'Accept-Language: en' `
```

Response Response Example

200 - Example 1

```
` {
"status" : "object" ,
"orders" : [
{
"id" : 60407024 ,
"invoice_number" : 60407024 ,
"code" : "YMK3VPgkhy" ,
"store_id" : 3 ,
"order_url" : "https://osama.zid.store/o/YMK3VPgkhy/inv" ,
"store_name" : "متجر أسامة" ,
"shipping_method_code" : "zid_zidship.level_2" ,
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
"is_quick_checkout_order" : true ,
"order_total" : "string" ,
"order_total_string" : "124.15 SAR" ,
"has_different_transaction_currency" : true ,
"transaction_reference" : "string" ,
"transaction_amount" : 124.1499994817 ,
"transaction_amount_string" : "124.15 SAR" ,
"issue_date" : "string" ,
"payment_status" : "pending" ,
"is_potential_fraud" : true ,
"source" : "string" ,
"source_code" : "string" ,
"is_reseller_transaction" : true ,
"created_at" : "2025-11-12 08:57:35" ,
"updated_at" : "2026-01-26 07:18:19" ,
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
]
}
] ,
"grand_total" : 517 ,
"total_order_count" : 517 ,
"total_order_count_per_status" : {
"ready" : 517 ,
"initial" : 0 ,
"new" : 0 ,
"preparing" : 0 ,
"indelivery" : 0 ,
"delivered" : 0 ,
"reversed" : 0 ,
"partially_reversed" : 0 ,
"reverse_in_progress" : 0 ,
"canceled" : 0 ,
"cancelled" : 0
} ,
"tax_settings" : [ ] ,
"storeColors" : {
"btn_default_background_color" : "#982abc" ,
"btn_default_text_color" : "#ffffff" ,
"btn_default_border_color" : "#982abc" ,
"btn_hover_background_color" : "#7d229b" ,
"btn_pressed_background_color" : "#641b7c" ,
"btn_pressed_text_color" : "#ffffff" ,
"btn_pressed_border_color" : "#641b7c"
} ,
"printed_invoice_settings" : {
"is_zid_invoice_generation_enabled" : true ,
"is_tax_number_active" : true ,
"is_return_policy_active" : true ,
"is_products_weight_active" : true ,
"is_products_image_active" : true ,
"is_barcode_active" : true ,
"is_qr_code_active" : true ,
"is_expected_time_active" : true ,
"is_store_address_active" : true ,
"is_vat_settings_active" : true ,
"is_sku_active" : true ,
"is_thanks_msg_active" : true ,
"is_order_status_active" : true ,
"is_discount_coupon_active" : true ,
"config_logo" : "https://media.zid.store/.../logo.jpg" ,
"store_business_address" : false ,
"store_business_name" : false ,
"store_business_type" : false ,
"commercial_number" : true ,
"is_payment_stamp_active" : true ,
"is_order_notifications_enabled" : true ,
"is_owner_email_notifications_enabled" : true ,
"is_product_description_active" : true
} ,
"orders_list_view_settings" : {
"order_number_column" : 1 ,
"customer_column" : 1 ,
"created_at_column" : 1 ,
"updated_at_column" : 1 ,
"source_column" : 1 ,
"shipping_method_column" : 1 ,
"payment_method_column" : 1 ,
"customer_note_column" : 1 ,
"tags_column" : 1 ,
"order_status_column" : 1 ,
"payment_status_column" : 1 ,
"totals_column" : 1 ,
"action_buttons" : true ,
"all_columns" : 1 ,
"order_number" : 1
} ,
"message" : {
"type" : "success" ,
"code" : "MSG_POPUP_OK" ,
"name" : "Coupons" ,
"description" : "Coupons created successfully"
}
} `
```

Modified at 2026-08-11 09:24:50

Previous

View Order

Next

List Custom Order Statuses
