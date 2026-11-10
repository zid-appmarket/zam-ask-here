---
# Synced from https://docs.zid.sa/retrieve-a-list-of-products
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-retrieve-a-list-of-products
title: "List Products"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/retrieve-a-list-of-products
tags: [from-docs-site, partner-docs]
language: en
---

> List Products - Zid Docs
# List Products

GET

https://api.zid.sa/ v1/products/

**Retrieve a list of all products with extensive filtering options.**

💡 Use Cases

Full Product Synchronization

🔑 Scopes

`products.read` - Products Read

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
` curl --location 'https://api.zid.sa/v1/products/?page=1&page_size=15&quantity__gte=10&quantity__lte=5&price=undefined&price__gt=50&price__lt=200&brand=4f8e78b8-64be-4f58-a79a-31e4e7ba3e80' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Store-Id: {{StoreId}}' \
--header 'Accept-Language: en' \
--header 'Role: Manager' `
```

Response Response Example

200 - Success

```
{
"total_products_count": 2282,
"normal_products_count": 2273,
"voucher_products_count": 3,
"grouped_products_count": 0,
"downloadable_products_count": 2,
"dynamic_bundle_products_count": 4,
"donation_item_count": 0,
"crowd_funding_count": 0,
"next": "http://api.zid.sa/v1/products/?is_infinite=false&page=2&page_size=15",
"previous": null,
"count": 175,
"results": [
{
"id": "a1477bb2-72ea-4be9-b2cf-093cefc721bb",
"product_class": "voucher",
"sku": "Z.1770805225810645",
"barcode": "",
"parent_id": null,
"name": {
"ar": "قسيمة",
"en": "voucher"
},
"slug": "قسيمة",
"price": 100.0,
"short_description": {
"ar": "",
"en": ""
},
"sale_price": null,
"formatted_price": " SAR 100.00",
"formatted_sale_price": null,
"currency": "SAR",
"currency_symbol": " SAR ",
"attributes": [],
"categories": [
{
"id": "1473476",
"name": {
"en": "Electronics",
"ar": "إلكترونيات"
},
"slug": "إلكترونيات",
"description": {
"en": "Devices and gadgets including mobiles, accessories, and smart technology.",
"ar": "أجهزة ومستلزمات إلكترونية تشمل الهواتف الذكية والإكسسوارات والتقنيات الذكية"
},
"cover_image": null,
"image": null,
"display_order": null,
"meta": {
"childs": [],
"parents": []
}
}
],
"display_order": 32766,
"has_options": false,
"has_fields": false,
"images": [],
"videos": [],
"is_draft": false,
"quantity": 4,
"is_infinite": false,
"html_url": "https://osama.zid.store/products/قسيمة",
"weight": {
"value": null,
"unit": "kg"
},
"keywords": [
"voucher"
],
"requires_shipping": false,
"is_taxable": true,
"structure": "standalone",
"seo": {
"title": {
"ar": "",
"en": ""
},
"description": {
"ar": "",
"en": ""
}
},
"rating": {
"average": 0,
"total_count": 0,
"1_ratings": {
"percentage": 0,
"count": 0
},
"2_ratings": {
"percentage": 0,
"count": 0
},
"3_ratings": {
"percentage": 0,
"count": 0
},
"4_ratings": {
"percentage": 0,
"count": 0
},
"5_ratings": {
"percentage": 0,
"count": 0
}
},
"store_id": 3,
"purchase_restrictions": {
"min_quantity_per_cart": null,
"max_quantity_per_cart": null,
"availability_period_start": null,
"availability_period_end": null,
"sale_price_period_start": null,
"sale_price_period_end": null
},
"metafields": [],
"meta": {},
"related_products_settings": "AUTO_GENERATED",
"related_products_title": {
"ar": "",
"en": ""
},
"badge": null,
"cost": 0.0,
"is_published": true,
"waiting_customers_count": null,
"group_products": null,
"stocks": [
{
"id": "e6c039b3-875f-431e-ae3d-85d37a10bb77",
"location": {
"id": "59be4f1d-3b59-4b34-ba47-9f7293894b47",
"name": {
"ar": "الدمام",
"en": "Dammam"
},
"type": "PHYSICAL",
"full_address": "8RRM+PX Dammam Saudi Arabia"
},
"available_quantity": 4,
"is_infinite": false
}
],
"vouchers_count": 5,
"sold_products_count": null,
"created_at": "2026-02-11T10:20:25.813306Z",
"updated_at": "2026-02-11T10:
```

Modified at 2026-09-16 09:48:16

Previous

Create Product

Next

View Product
