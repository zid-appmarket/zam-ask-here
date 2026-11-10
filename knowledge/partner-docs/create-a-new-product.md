---
# Synced from https://docs.zid.sa/create-a-new-product
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-create-a-new-product
title: "Create Product"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/create-a-new-product
tags: [from-docs-site, partner-docs]
language: en
---

> Create Product - Zid Docs
# Create Product

POST

https://api.zid.sa/ v1/products/

Use this endpoint to create a new product in the store.

The Create Product endpoint supports multiple product classes, including `standard products`, `grouped products`, `vouchers`, `downloadable products`, `crowdfunding projects`, `donation items`, `customizable products`, and `dynamic bundle products`.

Some product classes require additional fields in the request body. Dynamic Bundle products require an additional step after product creation to configure selection groups.

## Supported product classes #

Product Class Use Case Additional Step Required

Standard Product Regular physical or digital product. No

`grouped_product` Bundle multiple existing products together as one product. No

`voucher` Digital voucher, gift card, or license key product. May require voucher setup after product creation.

`downloadable` Digital file product. Files are managed separately after product creation.

`crowdfunding_project` Fundraising product with goal tracking. No

`donation_item` Donation product with unit-based progress tracking. No

`dynamic_bundle` Customer-selectable bundle with selection groups. Yes. Selection groups must be created separately.

Customizable Product Product with custom input fields or custom option fields. No

## Features #

**Grouped products:** Create a product that includes multiple existing products as a set.

**Product badges:** Optionally assign a badge to highlight offers, new arrivals, or other product attributes.

**Variants:** Add variants inline during product creation or create them later using the Add Product Variants endpoint.

**Custom fields:** Add customer input fields or predefined customization options during product creation.

**Donation and crowdfunding products:** Create products with progress tracking using product-specific metadata.

**Dynamic bundles:** Create a bundle product first, then configure its selection groups using the Dynamic Bundle selection groups endpoint.

## Important Notes #

1 .

Categories cannot be added during product creation.

To assign a product to one or more categories, use the following endpoints after creation:

**Add a product to a certain category (https://docs.zid.sa/add-a-product-to-a-certain-category)**

**Bulk Add Product to Category (https://docs.zid.sa/bulk-add-product-to-category-24155519e0)**

2 .

Dynamic Bundle products require at least one selection group before they can be published.

3 .

If you create a Dynamic Bundle product as a draft, you can add selection groups later before publishing it.

4 .

Some product classes restrict specific fields such as `sale_price`, `quantity`, `is_infinite`, or `requires_shipping`.

🔑Scopes

`products.read_write` - Products Read & Write

## Dynamic Bundle flow #

Dynamic Bundle products require two API requests:

1 .

Create the Dynamic Bundle product using `POST /v1/products/`

2 .

Add selection groups using `PATCH /v1/products/{product_id}/selection-groups/bulk-patch/`

If the product is created as a draft, use this flow:

1 .

Create the product as draft using `POST /v1/products/`

2 .

Add selection groups using `PATCH /v1/products/{product_id}/selection-groups/bulk-patch/`

3 .

Publish the product using `PATCH /v1/products/{product_id}/`

The Dynamic Bundle selection groups endpoint is currently not published.

## Request

Header Params

###

Body Params application/json

###

Examples

## Responses

🟢 201 OK

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

cURL

```
` curl --location 'https://api.zid.sa/v1/products/' \
--header 'Authorization: {{Autherization}}' \
--header 'X-Manager-Token: {{Access-Token}}' \
--header 'Store-Id: {{StoreId}}' \
--header 'Accept-Language: en' \
--header 'Role: Manager' \
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

201 - Dynamic Bundle

```
` {
"id" : "product-uuid" ,
"name" : {
"ar" : "حزمة البناء المخصصة" ,
"en" : "Custom Build Bundle"
} ,
"product_class" : "dynamic_bundle" ,
"sku" : "BUNDLE-001" ,
"price" : 0 ,
"is_draft" : false ,
"is_published" : false ,
"requires_shipping" : true ,
"meta" : {
"location_id" : "dd125776-70d1-4819-934c-a29b8ebd18ca"
} ,
"selection_groups" : [ ]
} `
```

Modified at 2026-06-10 07:51:16

Previous

Create Product Types

Next

List Products
