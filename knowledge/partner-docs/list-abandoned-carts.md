---
# Synced from https://docs.zid.sa/list-abandoned-carts
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-list-abandoned-carts
title: "List Carts"
product: zam
audience: all
status: verified
updated: 2026-11-23
source_url: https://docs.zid.sa/list-abandoned-carts
tags: [from-docs-site, partner-docs]
language: en
---

> List Carts - Zid Docs
# List Carts

GET

https://api.zid.sa/ v1/managers/store/abandoned-carts

Retrieves a list of abandoned carts for a given store.

Each entry in the list provides a brief overview of the abandoned cart,

including essential details such as the cart ID, customer information, total value, and a unique URL for retargeting.

Abandoned carts are identified when a user adds products to their online shopping cart but

does not proceed to checkout and complete the purchase within **10 minutes** of inactivity.

For **retargeting** purposes, each abandoned cart object includes a `url` field, which is the direct link

to the specific abandoned cart. This URL, along with customer name and contact details provided in the response,

facilitates effective retargeting strategies by merchants.

You can filter the list by date, phase, and the total number of carts.

For a detailed view of a specific cart, including product details

and additional customer information, refer to the

Get Abandoned Cart Details

endpoint using the cart's unique ID.

🔑Scopes

`abandoned_carts.read` - Abandoned Carts Read

### Including Cart Products #

Use the optional `with_products` query parameter to control whether product details are included.

`with_products=1`: Returns the full `products` list for each abandoned cart.

`with_products=0` (default): Excludes the `products` field.

`products_count` is always returned, regardless of the `with_products` parameter.

**Note:** The `products` field returns `null` if the cart's products cannot be retrieved or the cart has no saved currency. In either case, the remaining carts in the list are returned normally.

**Important:** When both `with_products` and `with_product_ids` are provided, failure to retrieve a cart's products causes the entire request to fail instead of returning `products: null` for that cart.

**Product Images:** Product images are not included in this response. To retrieve them, use the Get Abandoned Cart (https://docs.zid.sa/get-abandoned-cart-details) endpoint (`GET /v1/managers/store/abandoned-carts/{id}`).

## Request

Query Params

###

Header Params

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
` curl --location 'https://api.zid.sa/v1/managers/store/abandoned-carts?page=1&page_size=15&phase=payment_method&search_term=mahmoud&customer_id=15141670&products_count=3&has_reminders=true&country_id=1&city_id=5354&currency_code=EGP&date_from=2025-12-01&date_to=2025-12-31&cart_total=509.8254&filter_order_by=created_at&filter_sort_by=DESC&customer_type=individual&with_products=1&with_product_ids=1' \
--header 'Authorization: {{Autherization}}' \
--header 'X-Manager-Token: {{Access-Token}}' \
--header 'Accept-Language: en' `
```

Response Response Example

200 - Success

```
` {
"status" : "object" ,
"abandoned-carts" : [
{
"id" : "b978fcc2-ccd0-45f6-81a7-7ab1f3b8f85d" ,
"store_id" : "d297fb8b-c322-412e-a2f4-ffa96dc57022" ,
"session_id" : "3:694ff0d8df6032a7697a3849" ,
"url" : "https://osama.zid.store/checkout/fromBasket/3:694ff0d8df6032a7697a3849" ,
"cart_id" : "3:694ff0d8df6032a7697a3849" ,
"order_id" : null ,
"phase" : "payment_method" ,
"customer_id" : 15141670 ,
"customer_name" : "mahmoud aaaa" ,
"customer_email" : "a.alkallas@zid.sa" ,
"customer_mobile" : "966500000005" ,
"city_id" : 5354 ,
"products_count" : 1 ,
"reminders_count" : 2 ,
"cart_total" : 509.8254 ,
"cart_total_string" : "509.83 ج.م" ,
"whatsapp_message" : "Hello What'sapp" ,
"currency_code" : "EGP" ,
"created_at" : "2025-12-27T14:45:44.000000Z" ,
"updated_at" : "2025-12-28T14:53:39.000000Z" ,
"source" : "catalog"
} ,
{
"id" : "88537913-f12a-468b-8b03-5a10ada7eb3d" ,
"store_id" : "d297fb8b-c322-412e-a2f4-ffa96dc57022" ,
"session_id" : "3:69473e9254de8076e8311e0c" ,
"url" : "https://osama.zid.store/checkout/fromBasket/3:69473e9254de8076e8311e0c" ,
"cart_id" : "3:69473e9254de8076e8311e0c" ,
"order_id" : null ,
"phase" : "payment_method" ,
"customer_id" : 15141670 ,
"customer_name" : "mahmoud aaaa" ,
"customer_email" : "test@zid.sa" ,
"customer_mobile" : "966500000005" ,
"city_id" : 1 ,
"products_count" : 1 ,
"reminders_count" : 4 ,
"cart_total" : 13.35 ,
"cart_total_string" : "13.35 SAR" ,
"whatsapp_message" : "Hello What'sapp" ,
"currency_code" : "SAR" ,
"created_at" : "2025-12-21T00:26:39.000000Z" ,
"updated_at" : "2025-12-22T00:37:53.000000Z" ,
"source" : "catalog"
}
] ,
"pagination" : {
"page" : 1 ,
"page_size" : 2 ,
"next_page" : 2 ,
"last_page" : 243 ,
"result_count" : 485
} ,
"message" : {
"type" : "object" ,
"code" : null ,
"name" : null ,
"description" : null
}
} `
```

Modified at 2026-11-16 08:41:15

Previous

Abandoned Carts

Next

View Cart
