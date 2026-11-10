---
# Synced from https://docs.zid.sa/get-abandoned-cart-details
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-get-abandoned-cart-details
title: "View Cart"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/get-abandoned-cart-details
tags: [from-docs-site, partner-docs]
language: en
---

> View Cart - Zid Docs
# View Cart

GET

https://api.zid.sa/ v1/managers/store/abandoned-carts/{cart-id}

This endpoint fetches comprehensive details about an abandoned cart, identified

by its unique ID. An abandoned cart is a shopping cart to which items have been added

but is left incomplete by the customer. A cart is marked as abandoned after

**10 minutes** of inactivity.

Along with detailed information about the cart and its contents, this endpoint provides

the `url` field, which is the direct link to the abandoned cart. This enables merchants

to easily **retarget** customers with a direct link to their uncompleted purchase,

enhancing the chances of converting these abandoned carts into completed transactions.

The response also includes the customer's name and contact details, providing additional context

for retargeting efforts and potential follow-up communications.

The response conforms to the Abandoned Cart schema, providing comprehensive details

of the cart, its associated customer, and the products within it.

🔑Scopes

`abandoned_carts.read` - Abandoned Carts Read

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

🟠 422 Validation errors

🔴 500 Internal Server error

Request Request Example

Shell

JavaScript

Java

Swift

```
` curl --location 'https://api.zid.sa/v1/managers/store/abandoned-carts/b978fcc2-ccd0-45f6-81a7-7ab1f3b8f85d' \
--header 'Authorization: {{Autherization}}' \
--header 'X-Manager-Token: {{Access-Token}}' \
--header 'Accept-Language: en' `
```

Response Response Example

200 - Success

```
` {
"status" : "object" ,
"abandoned_cart" : {
"id" : "b978fcc2-ccd0-45f6-81a7-7ab1f3b8f85d" ,
"url" : "https://osama.zid.store/checkout/fromBasket/3:694ff0d8df6032a7697a3849" ,
"store_id" : "d297fb8b-c322-412e-a2f4-ffa96dc57022" ,
"store_name" : "متجر أسامة." ,
"store_logo" : "https://media.zid.store/d297fb8b-c322-412e-a2f4-ffa96dc57022/0e959ed7-ced5-47df-b839-16969940db08-200x.jpg" ,
"store_url" : "https://osama.zid.store/" ,
"products_count" : 1 ,
"products" : [
{
"id" : 1048562914 ,
"product_id" : "b2dd7116dd724f7fb10cac7e85b34655" ,
"product_url" : "https://osama.zid.store/products/b2dd7116dd724f7fb10cac7e85b34655" ,
"sku" : "Z.17639724523193033" ,
"name" : "Test recurring" ,
"custom_field" : [ ] ,
"price" : 38.0182984840272 ,
"price_string" : "38.02 ج.م" ,
"additions_price" : 0 ,
"additions_price_string" : "0.00 ج.م" ,
"quantity" : 1 ,
"total" : 38.0182984840272 ,
"total_string" : "38.02 ج.م" ,
"images" : [
{
"id" : "9fa5ece1-5c33-486f-97b1-bdd1f1b7770d" ,
"origin" : "https://media.zid.store/thumbs/d297fb8b-c322-412e-a2f4-ffa96dc57022/9fa5ece1-5c33-486f-97b1-bdd1f1b7770d-thumbnail-500x500.png" ,
"thumbs" : {
"fullSize" : "https://media.zid.store/d297fb8b-c322-412e-a2f4-ffa96dc57022/9fa5ece1-5c33-486f-97b1-bdd1f1b7770d.png" ,
"thumbnail" : "https://media.zid.store/thumbs/d297fb8b-c322-412e-a2f4-ffa96dc57022/9fa5ece1-5c33-486f-97b1-bdd1f1b7770d-thumbnail-370x370.png" ,
"small" : "https://media.zid.store/thumbs/d297fb8b-c322-412e-a2f4-ffa96dc57022/9fa5ece1-5c33-486f-97b1-bdd1f1b7770d-thumbnail-500x500.png" ,
"medium" : "https://media.zid.store/thumbs/d297fb8b-c322-412e-a2f4-ffa96dc57022/9fa5ece1-5c33-486f-97b1-bdd1f1b7770d-thumbnail-770x770.png" ,
"large" : "https://media.zid.store/thumbs/d297fb8b-c322-412e-a2f4-ffa96dc57022/9fa5ece1-5c33-486f-97b1-bdd1f1b7770d-thumbnail-1000x1000.png"
}
}
]
}
] ,
"city" : {
"id" : 5354 ,
"national_id" : null ,
"name" : "Assuit" ,
"priority" : 0 ,
"country_id" : 63 ,
"country_name" : "Egypt" ,
"country_code" : "EG" ,
"ar_name" : "أسيوط" ,
"en_name" : "Assuit"
} ,
"order_id" : null ,
"history" : [
{
"uuid" : "23e4394c-2048-4a68-b95c-8310058c7d0f" ,
"abandoned_cart_id" : "b978fcc2-ccd0-45f6-81a7-7ab1f3b8f85d" ,
"type" : "Created Successfully" ,
"created_at" : "2025-12-27T14:53:32.000000Z" ,
"updated_at" : "2025-12-27T14:53:32.000000Z"
} ,
{
"uuid" : "6ffa538f-5be0-49f7-8e90-06c4b405b522" ,
"abandoned_cart_id" : "b978fcc2-ccd0-45f6-81a7-7ab1f3b8f85d" ,
"type" : "Reminder Sent" ,
"created_at" : "2025-12-28T14:53:39.000000Z" ,
"updated_at" : "2025-12-28T14:53:39.000000Z"
} ,
{
"uuid" : "ec62449e-fac5-4837-b640-32e94435f9d8" ,
"abandoned_cart_id" : "b978fcc2-ccd0-45f6-81a7-7ab1f3b8f85d" ,
"type" : "Reminder Sent" ,
"created_at" : "2025-12-27T15:53:27.000000Z" ,
"updated_at" : "2025-12-27T15:53:27.000000Z"
}
] ,
"phase" : "payment_method" ,
"customer_id" : 15141670 ,
"customer_name" : "mahmoud aaaa" ,
"customer_email" : "a.alkallas@zid.sa" ,
"customer_mobile" : "966500000005" ,
"reminders_count" : 2 ,
"cart_total" : 509.8254 ,
"cart_total_string" : "509.83 ج.م" ,
"whatsapp_message" : "Hello What'sapp" ,
"created_at" : "2025-12-27 14:45:44" ,
"updated_at" : "2025-12-28 14:53:39" ,
"source" : "catalog"
} ,
"message" : {
"type" : "object" ,
"code" : null ,
"name" : null ,
"description" : null
}
} `
```

Modified at 2026-08-11 09:19:39

Previous

List Carts

Next

Validate Abandoned Cart Messages
