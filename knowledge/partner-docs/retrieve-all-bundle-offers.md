---
# Synced from https://docs.zid.sa/retrieve-all-bundle-offers
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-retrieve-all-bundle-offers
title: "List Bundle Offers"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/retrieve-all-bundle-offers
tags: [from-docs-site, partner-docs]
language: en
---

> List Bundle Offers - Zid Docs
# List Bundle Offers

GET

https://api.zid.sa/ v1/managers/store/discounts/bundle-offers

This endpoint retrieves all available bundle offers for the store. Bundle offers are special promotions where customers can get a discount if they buy a specific bundle of products.

Bundle offers can now apply to specific products, categories, or all products using the new `applies_to` field. Additionally, you can now `exclude on-sale` products using the exclude_on_sale_products flag in both conditions and actions.

🔑Scopes

`third_bundle_offers_read` - Bundle Offers Read

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
` curl --location 'https://api.zid.sa/v1/managers/store/discounts/bundle-offers?page=1&per_page=15&code=&status=undefined&type=&start_date=undefined&end_date=undefined&order_by=undefined&sort_by=undefined&search_term=undefined' \
--header 'Authorization: {{Autherization}}' \
--header 'X-Manager-Token: {{Access-Token}}' \
--header 'Accept-Language: en' \
--header 'Currency: SAR' `
```

Response Response Example

200 - Success

```
` {
"status" : "object" ,
"discount_rules" : [
{
"id" : "02ed8742-354d-4b44-8f3f-39766081c12e" ,
"name" : {
"en" : null ,
"ar" : "BuyOne_GetSameFree"
} ,
"description" : {
"ar" : null ,
"en" : null
} ,
"code" : "bundle_offer" ,
"conditions" : [
{
"field" : "products_quantity" ,
"value" : 1 ,
"operator" : ">=" ,
"product_ids" : [
"e76df08490ff4f9da738557bad069c64"
]
}
] ,
"actions" : [
{
"type" : "percentage" ,
"field" : "products" ,
"value" : 100 ,
"product_ids" : [
"e76df08490ff4f9da738557bad069c64"
] ,
"products_quantity" : 1
}
] ,
"conditions_criteria" : "all" ,
"uses_total" : null ,
"uses_customer" : null ,
"enabled" : false ,
"auto_adding" : true ,
"status_code" : "disabled" ,
"start_date" : "2023-11-07" ,
"end_date" : null ,
"meta" : {
"auto_add_products" : true
} ,
"channel" : "catalog" ,
"channel_name" : {
"ar" : "المتجر الإلكتروني" ,
"en" : "Store"
}
} ,
{
"id" : "0500ec17-54b6-47b5-910c-b73e319f7381" ,
"name" : {
"en" : null ,
"ar" : "احصل عليه مجانًا"
} ,
"description" : {
"en" : null ,
"ar" : "في حال اشتر عطر اخضر واحصل على الازرق"
} ,
"code" : "bundle_offer" ,
"conditions" : [
{
"field" : "products_quantity" ,
"value" : 1 ,
"operator" : ">=" ,
"product_ids" : [
"6f1cae36a39b4378ab175f60626e9d4c"
]
}
] ,
"actions" : [
{
"type" : "percentage" ,
"field" : "products" ,
"value" : 100 ,
"product_ids" : [
"fe90852cf53442edbdcac868039f0366"
] ,
"products_quantity" : 1
}
] ,
"conditions_criteria" : "all" ,
"uses_total" : 4 ,
"uses_customer" : 1 ,
"enabled" : false ,
"auto_adding" : true ,
"status_code" : "disabled" ,
"start_date" : "2023-12-24" ,
"end_date" : null ,
"meta" : {
"auto_add_products" : true
} ,
"channel" : "catalog" ,
"channel_name" : {
"ar" : "المتجر الإلكتروني" ,
"en" : "Store"
}
} ,
{
"id" : "089f6543-46cf-445b-b745-7f6fa02edb05" ,
"name" : {
"en" : null ,
"ar" : "رمضان"
} ,
"description" : {
"ar" : null ,
"en" : null
} ,
"code" : "bundle_offer" ,
"conditions" : [
{
"field" : "products_quantity" ,
"value" : 1 ,
"operator" : ">=" ,
"product_ids" : [
"3d17bbb6a49945fbbb2a009b8332b53b"
]
}
] ,
"actions" : [
{
"type" : "percentage" ,
"field" : "products" ,
"value" : 100 ,
"product_ids" : [
"170fcdc010914568a79c6cc634bb94bf"
] ,
"products_quantity" : 1
}
] ,
"conditions_criteria" : "all" ,
"uses_total" : null ,
"uses_customer" : null ,
"enabled" : false ,
"auto_adding" : true ,
"status_code" : "disabled" ,
"start_date" : "2022-03-10" ,
"end_date" : null ,
"meta" : {
"auto_add_products" : true
} ,
"channel" : "catalog" ,
"channel_name" : {
"ar" : "المتجر الإلكتروني" ,
"en" : "Store"
}
} ,
{
"id" : "0e038a43-fd58-40ac-ab1c-f03efa601207" ,
"name" : {
"en" : null ,
"ar" : "حزمة للسلة الجديدة مجانى"
} ,
"description" : {
"ar" : null ,
"en" : null
} ,
"code" : "bundle_offer" ,
"conditions" : [
{
"field" : "products_quantity" ,
"value" : 1 ,
"operator" : ">=" ,
"product_ids" : [
"1aeae4bb3bf44821b9d6182afeeb085b"
]
}
] ,
"actions" : [
{
"type" : "percentage" ,
"field" : "products" ,
"value" : 50 ,
"product_ids" : [
"56a538f1b4e24a1ab01d7472f89df37d"
] ,
"products_quantity" : 1
}
] ,
"conditions_criteria" : "all" ,
"uses_total" : null ,
"uses_customer" : null ,
"enabled" : false ,
"auto_adding" : false ,
"status_code" : "disabled" ,
"start_date" : "2023-12-24" ,
"end_date" : null ,
"meta" : {
"auto_add_products" : false
} ,
"channel" : "catalog" ,
"channel_name" : {
"ar" : "المتجر الإلكتروني" ,
"en" : "Store"
}
} ,
{
"id" : "138f9af1-fc13-4f75-aa27-7ca08c00ec69" ,
"name" : {
"en" : null ,
"ar" : "BuyOne_GetDiscountedOne"
} ,
"description" : {
"ar" : null ,
"en" : null
} ,
"code" : "bundle_offer" ,
"conditions" : [
{
"field" : "products_quantity" ,
"value" : 1 ,
"operator" : ">=" ,
"product_ids" : [
"b859bb3e306749a9acc76bbfd7bbb211" ,
"ccc39cdfeef149b0bc188189c983de90"
]
}
] ,
"actions" : [
{
"type" : "percentage" ,
"field" : "products" ,
"value" : 50 ,
"product_ids" : [
"f0d8bfe64b1c431bba0639bfdb88fca0"
] ,
"products_quantity" : 1
}
] ,
"conditions_criteria" : "all" ,
"uses_total" : null ,
"uses_customer" : null ,
"enabled" : false ,
"auto_adding" : true ,
"status_code" : "disabled" ,
"start_date" : "2023-11-07" ,
"end_date" : null ,
"meta" : {
"auto_add_products" : true
} ,
"channel" : "catalog" ,
"channel_name" : {
"ar" : "المتجر الإلكتروني" ,
"en" : "Store"
}
} ,
{
"id" : "1d1542bf-3dcd-4328-bdb9-48d30936747a" ,
"name" : {
"ar" : "tets" ,
"en" : "test"
} ,
"description" : {
"ar" : "tes" ,
"en" : "tes"
} ,
"code" : "bundle_offer" ,
"conditions" : [
{
"field" : "products_quantity" ,
"value" : 1 ,
"operator" : ">=" ,
"product_ids" : [
"f655e3492cc141d2aecdb81cd6a12985"
]
}
] ,
"actions" : [
{
"type" : "percentage" ,
"field" : "products" ,
"value" : 10.7 ,
"product_ids" : [
"f655e3492cc141d2aecdb81cd6a12985"
] ,
"products_quantity" : 1
}
] ,
"conditions_criteria" : "all" ,
"uses_total" : null ,
"uses_customer" : null ,
"enabled" : true ,
"auto_adding" : true ,
"status_code" : "expired" ,
"start_date" : "2025-06-24" ,
"end_date" : "2025-06-30" ,
"meta" : {
"auto_add_products" : true
} ,
"channel" : "catalog" ,
"channel_name" : {
"ar" : "المتجر الإلكتروني" ,
"en" : "Store"
}
} ,
{
"id" : "224c8be1-9922-4939-ba74-dbd91881361f" ,
"name" : {
"en" : null ,
"ar" : "حزمه تيست"
} ,
"description" : {
"en" : null ,
"ar" : "قم بأضافه منتج لتحصل علي منتج مجاني"
} ,
"code" : "bundle_offer" ,
"conditions" : [
{
"field" : "products_quantity" ,
"value" : 1 ,
"operator" : ">=" ,
"product_ids" : [
"c70f8371187f4285959e9ac2223185e3"
]
}
] ,
"actions" : [
{
"type" : "percentage" ,
"field" : "products" ,
"value" : 100 ,
"product_ids" : [
"c51a3e1ce15c4f089e4f10226816662f"
] ,
"products_quantity" : 1
}
] ,
"conditions_criteria" : "all" ,
"uses_total" : null ,
"uses_customer" : null ,
"enabled" : true ,
"auto_adding" : true ,
"status_code" : "expired" ,
"start_date" : "2022-10-09" ,
"end_date" : "2023-07-20" ,
"meta" : {
"auto_add_products" : true
} ,
"channel" : "catalog" ,
"channel_name" : {
"ar" : "المتجر الإلكتروني" ,
"en" : "Store"
}
} ,
{
"id" : "249571bb-6ad1-4fc3-8f76-3b435e78f6de" ,
"name" : {
"en" : null ,
"ar" : "Test 1 + 1"
} ,
"description" : {
"ar" : null ,
"en" : null
} ,
"code" : "bundle_offer" ,
"conditions" : [
{
"field" : "products_quantity" ,
"value" : 1 ,
"operator" : ">=" ,
"product_ids" : [
"75bd90f0353c41329e9e13a3a24be684"
]
}
] ,
"actions" : [
{
"type" : "percentage" ,
"field" : "products" ,
"value" : 100 ,
"product_ids" : [
"75bd90f0353c41329e9e13a3a24be684"
] ,
"products_quantity" : 1
}
] ,
"conditions_criteria" : "all" ,
"uses_total" : null ,
"uses_customer" : null ,
"enabled" : false ,
"auto_adding" : true ,
"status_code" : "disabled" ,
"start_date" : "2024-02-11" ,
"end_date" : null ,
"meta" : {
"auto_add_products" : true
} ,
"channel" : "catalog" ,
"channel_name" : {
"ar" : "المتجر الإلكتروني" ,
"en" : "Store"
}
} ,
{
"id" : "2aec3a84-d253-45f4-ac05-d97cea113477" ,
"name" : {
"en" : null ,
"ar" : "٣حهت"
} ,
"description" : {
"en" : null ,
"ar" : "٣حختب"
} ,
"code" : "bundle_offer" ,
"conditions" : [
{
"field" : "products_quantity" ,
"value" : 1 ,
"operator" : ">=" ,
"product_ids" : [
"ae1b4ddd86c64acb96b79dc22fa7cf8f"
]
}
] ,
"actions" : [
{
"type" : "percentage" ,
"field" : "products" ,
"value" : 100 ,
"product_ids" : [
"525fd66eb9fb4d27a56abcae3854a61f"
] ,
"products_quantity" : 1
}
] ,
"conditions_criteria" : "all" ,
"uses_total" : null ,
"uses_customer" : null ,
"enabled" : false ,
"auto_adding" : true ,
"status_code" : "disabled" ,
"start_date" : "2024-09-11" ,
"end_date" : null ,
"meta" : {
"auto_add_products" : true
} ,
"channel" : "catalog" ,
"channel_name" : {
"ar" : "المتجر الإلكتروني" ,
"en" : "Store"
}
} ,
{
"id" : "2ded51ec-adb5-4c7b-a0b9-1c8ef90d764c" ,
"name" : {
"ar" : "bundle" ,
"en" : "bundle"
} ,
"description" : {
"ar" : null ,
"en" : null
} ,
"code" : "bundle_offer" ,
"conditions" : [
{
"field" : "products_quantity" ,
"value" : 1 ,
"operator" : ">=" ,
"product_ids" : [
"deb71db2ef90464a9de7fe3e2ab12297" ,
"d42f305a2f7d4abaa7a380a5ba9caa3f" ,
"b43abb22179b4f0baf0e7c55eb04135f" ,
"15aa95a82f35400e956016805cfe0553" ,
"b00dca745a0a437fbca95791385519e6" ,
"afa334778e1d4bb5a50af69a28ec4e9e" ,
"1e8621b55ed147138f3545da2c9383d1" ,
"5cb4238444e94e139105f7ba07b095be" ,
"bc06c5e3e8a442b091c7a2eb6ff9b04c" ,
"83fb0df2e3f44e6da16c27e6afe5b3f4"
]
}
] ,
"actions" : [
{
"type" : "percentage" ,
"field" : "products" ,
"value" : 100 ,
"product_ids" : [
"deb71db2ef90464a9de7fe3e2ab12297" ,
"d42f305a2f7d4abaa7a380a5ba9caa3f" ,
"b43abb22179b4f0baf0e7c55eb04135f" ,
"15aa95a82f35400e956016805cfe0553" ,
"b00dca745a0a437fbca95791385519e6" ,
"afa334778e1d4bb5a50af69a28ec4e9e" ,
"1e8621b55ed147138f3545da2c9383d1" ,
"5cb4238444e94e139105f7ba07b095be" ,
"bc06c5e3e8a442b091c7a2eb6ff9b04c" ,
"83fb0df2e3f44e6da16c27e6afe5b3f4"
] ,
"products_quantity" : 1
}
] ,
"conditions_criteria" : "all" ,
"uses_total" : 0 ,
"uses_customer" : null ,
"enabled" : false ,
"auto_adding" : true ,
"status_code" : "disabled" ,
"start_date" : "2025-10-11" ,
"end_date" : null ,
"meta" : {
"auto_add_products" : true
} ,
"channel" : "catalog" ,
"channel_name" : {
"ar" : "المتجر الإلكتروني" ,
"en" : "Store"
}
} ,
{
"id" : "32043a1e-ee05-4224-838e-c2496d3a82a6" ,
"name" : {
"ar" : "test bundle" ,
"en" : null
} ,
"description" : [ ] ,
"code" : "bundle_offer" ,
"conditions" : [
{
"field" : "products_quantity" ,
"value" : 1 ,
"operator" : ">=" ,
"applies_to" : "product" ,
"product_ids" : [
"031c1dcd72ec493f927531c559b3f493"
]
}
] ,
"actions" : [
{
"type" : "free" ,
"field" : "products" ,
"value" : 100 ,
"applies_to" : "product" ,
"product_ids" : [
"4fea1312a57b419b8258a12aa2c95754"
] ,
"products_quantity" : 1
}
] ,
"conditions_criteria" : "all" ,
"uses_total" : null ,
"uses_customer" : null ,
"enabled" : true ,
"auto_adding" : true ,
"status_code" : "expired" ,
"start_date" : "2024-07-06" ,
"end_date" : "2024-07-31" ,
"meta" : {
"auto_add_products" : true
} ,
"channel" : "catalog" ,
"channel_name" : {
"ar" : "المتجر الإلكتروني" ,
"en" : "Store"
}
} ,
{
"id" : "38405394-8654-419b-8736-574b5461a543" ,
"name" : {
"ar" : "test xy" ,
"en" : null
} ,
"description" : {
"ar" : "hello" ,
"en" : null
} ,
"code" : "bundle_offer" ,
"conditions" : [
{
"field" : "products_quantity" ,
"value" : 1 ,
"operator" : ">=" ,
"product_ids" : [
"775cdfe0510e4228ae32956011ff24aa"
]
}
] ,
"actions" : [
{
"type" : "percentage" ,
"field" : "products" ,
"value" : 100 ,
"product_ids" : [
"775cdfe0510e4228ae32956011ff24aa" ,
"b4b6fe6c9aa24a978dacec2df53fe9ba"
] ,
"products_quantity" : 1
}
] ,
"conditions_criteria" : "all" ,
"uses_total" : 555 ,
"uses_customer" : 1 ,
"enabled" : false ,
"auto_adding" : true ,
"status_code" : "disabled" ,
"start_date" : "2024-12-11" ,
"end_date" : null ,
"meta" : {
"auto_add_products" : true
} ,
"channel" : "catalog" ,
"channel_name" : {
"ar" : "المتجر الإلكتروني" ,
"en" : "Store"
}
} ,
{
"id" : "3bf8ddc9-6ee9-4121-9c15-d4566d41add0" ,
"name" : {
"en" : null ,
"ar" : "Bundle"
} ,
"description" : {
"en" : null ,
"ar" : "احصل علي خصم 50 %"
} ,
"code" : "bundle_offer" ,
"conditions" : [
{
"field" : "products_quantity" ,
"value" : 2 ,
"operator" : ">=" ,
"product_ids" : [
"271a034c4d7c40fcb54fdc5df113812c"
]
}
] ,
"actions" : [
{
"type" : "percentage" ,
"field" : "products" ,
"value" : 100 ,
"product_ids" : [
"02f2ed69f8654edfba91c217bd493b48" ,
"aaf2492b8fd14ce1abdf41a63c4721db" ,
"98f8ca54642e4a639fee8f38800e25a7"
] ,
"products_quantity" : 1
}
] ,
"conditions_criteria" : "all" ,
"uses_total" : null ,
"uses_customer" : null ,
"enabled" : false ,
"auto_adding" : true ,
"status_code" : "disabled" ,
"start_date" : "2022-08-16" ,
"end_date" : null ,
"meta" : {
"auto_add_products" : true
} ,
"channel" : "catalog" ,
"channel_name" : {
"ar" : "المتجر الإلكتروني" ,
"en" : "Store"
}
} ,
{
"id" : "3cb40974-56de-4bfa-ba60-6d8c9e5f4688" ,
"name" : {
"en" : null ,
"ar" : "Main Grouped Bundle Test"
} ,
"description" : {
"en" : null ,
"ar" : "Main Grouped Bundle Test"
} ,
"code" : "bundle_offer" ,
"conditions" : [
{
"field" : "products_quantity" ,
"value" : 1 ,
"operator" : ">=" ,
"product_ids" : [
"7d2e793a2a314a5bb40d6f1db26aa07d"
]
}
] ,
"actions" : [
{
"type" : "percentage" ,
"field" : "products" ,
"value" : 100 ,
"product_ids" : [
"99810cc078a34e339cf4f3016136990a"
] ,
"products_quantity" : 1
}
] ,
"conditions_criteria" : "all" ,
"uses_total" : null ,
"uses_customer" : null ,
"enabled" : false ,
"auto_adding" : true ,
"status_code" : "disabled" ,
"start_date" : "2024-07-09" ,
"end_date" : null ,
"meta" : {
"auto_add_products" : true
} ,
"channel" : "catalog" ,
"channel_name" : {
"ar" : "المتجر الإلكتروني" ,
"en" : "Store"
}
} ,
{
"id" : "3ed7ec23-902d-4593-971c-7aa2b989154c" ,
"name" : {
"ar" : "qwe"
} ,
"description" : [ ] ,
"code" : "bundle_offer" ,
"conditions" : [
{
"field" : "products_quantity" ,
"value" : 1 ,
"operator" : ">=" ,
"product_ids" : [
"c7d0807875044b78a101415a7e1a17f7" ,
"71078fb3ad46482c87927861504a5867" ,
"b5c89eed0de841359bd3987331849b29" ,
"dcb012d027b94e89bb907490d89ff972" ,
"3b8297d589354ef2a2215ae07b41c94f"
]
}
] ,
"actions" : [
{
"type" : "percentage" ,
"field" : "products" ,
"value" : 1 ,
"product_ids" : [
"dcb012d027b94e89bb907490d89ff972" ,
"16eb746e0e974f369cd591e4f21d5124" ,
"2f45e833f698483786291e7b9d4b75f5" ,
"3b8297d589354ef2a2215ae07b41c94f"
] ,
"products_quantity" : 1
}
] ,
"conditions_criteria" : "all" ,
"uses_total" : null ,
"uses_customer" : null ,
"enabled" : false ,
"auto_adding" : true ,
"status_code" : "disabled" ,
"start_date" : "2025-01-22" ,
"end_date" : null ,
"meta" : {
"auto_add_products" : true
} ,
"channel" : null ,
"channel_name" : null
}
] ,
"page" : 1 ,
"next_page" : 2 ,
"last_page" : 4 ,
"total" : 51 ,
"message" : {
"type" : "object" ,
"code" : null ,
"name" : null ,
"description" : null
}
} `
```

Modified at 2026-10-13 10:09:46

Previous

Bundle Offers

Next

View Bundle Offer
