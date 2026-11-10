---
# Synced from https://docs.zid.sa/template-replacements-1938995m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-template-replacements
title: "Template Replacements"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/template-replacements-1938995m0
tags: [from-docs-site, partner-docs]
language: en
---

> Template Replacements - Zid Docs
# Template Replacements

This page documents legacy templates that have been replaced in the Vitrin system

If your theme relies on old template helpers, you must replace them with the corresponding Vitrin templates to ensure compatibility with the latest structure.

### What changed #

The old Twig helper is no longer supported.

To render grouped products, your theme should now include the new Vitrin Jinja template.

## Template Replacement Reference #

Old Template Name New Vitrin Template

`template_for_store_messages` `vitrin:shared/store_messages.jinja`

`template_for_shipping_destination_currency_lang` `vitrin:shared/region_settings_dialog.jinja`

`template_for_products_attributes` `vitrin:products/filters.jinja`

`template_for_category_metafields` `vitrin:shared/metafields.jinja`

`template_for_products_badge` `vitrin:products/badge.jinja`

`template_for_blogs_metafields` `vitrin:shared/metafields.jinja`

`template_for_cart_products_list` `vitrin:cart/products_list.jinja`

`template_for_cart_payments_widget` `vitrin:cart/payment_widgets.jinja`

`template_for_cart_apple_pay_button` `vitrin:checkout/apple-pay-quick-checkout.jinja`

`template_for_cart_gifts_widget` `vitrin:cart/gift-card.jinja`

`template_for_product_badge` `vitrin:products/badge.jinja`

`template_for_product_loyalty_points_widget` `vitrin:products/loyalty_points_widget.jinja`

`template_for_product_payments_widget` `vitrin:products/payment_widgets.jinja`

`template_for_product_variants_list` `vitrin:products/variants_list.jinja`

`template_for_product_custom_input_fields` `vitrin:products/custom_input_fields.jinja`

`template_for_product_apple_pay_button` `vitrin:checkout/apple-pay-quick-checkout.jinja`

`template_for_product_grouped` `vitrin:products/grouped-product.jinja`

`template_for_product_metafields` `vitrin:shared/metafields.jinja`

## Usage Examples #

### 1. Store Messages #

Displays store-wide notification messages.

File: `header.jinja`

`{% include 'vitrin:shared/store_messages.jinja' %}`

### 2. Region Settings Dialog (Shipping Destination / Language) #

Displays a dialog that allows customers to select their region and language.

File: `layout.jinja`

`{% include 'vitrin:shared/region_settings_dialog.jinja' %}`

more details.. (https://docs.zid.sa/region-language-popup-1861342m0)

### 3. Products Filters (Products Attributes) #

Displays product filtering options on category and product listing pages.

Files: `category.jinja` or `products.jinja` Required variable: `async` (set to true for async loading)

```
``
```

### 4. Products Badge #

Displays product badges on product cards.

File: `components/product-card.jinja`

```
``
```

### 5. Product Badge (Product Details Page) #

Displays the product badge on the product details page.

File: `templates/product.jinja`

```
``
```

### 6. Metafields (Shared Template) #

Displays custom metafields for different entities. This shared template is used for products, categories, blogs, and pages.

Required variable: `entity`

#### Product Metafields #

File: `templates/product.jinja`

```
``
```

#### Category Metafields #

File: `templates/category.jinja`

```
``
```

#### Page Metafields #

File: `templates/page.jinja`

```
``
```

### 7. Cart Products List #

Displays the list of products in the shopping cart.

File: `templates/cart.jinja`

```
``
```

### 8. Cart Payment Widgets #

Displays available payment method widgets in the cart, including Tabby, Tamara, and MISPay.

File: `templates/cart.jinja`

```
`{% include 'vitrin:cart/payment_widgets.jinja' %}`
```

**Note:** The MISPay widget is displayed when the merchant enables it for the cart page under **Dashboard → Payments → MISPay**. No additional integration is required for Vitrin themes that already include this shared template. **MISPay widgets are not supported on legacy themes.**

### 9. Apple Pay Quick Checkout Button #

Displays the Apple Pay button for quick checkout. Used on both cart and product pages.

#### Cart & Product Page #

Files: `templates/cart.jinja` & `templates/product.jinja`

`{% include 'vitrin:checkout/apple-pay-quick-checkout.jinja' %}`

more details.. (https://docs.zid.sa/apple-pay-quick-checkout-1859764m0)

### 10. Cart Gift Card Widget #

Displays the gift card or gift wrapping option in the cart.

File: `templates/cart.jinja`

```
``
```

more details.. (https://docs.zid.sa/gift-card-1697835m0)

### 11. Product Loyalty Points Widget #

Displays loyalty points information on the product page.

File: `templates/product.jinja`

`{% include 'vitrin:products/loyalty_points_widget.jinja' %}`

### 12. Product Payment Widgets #

Displays available payment method widgets on the product details page, including Tabby, Tamara, and MISPay.

File: `templates/product.jinja`

```
`{% include 'vitrin:products/payment_widgets.jinja' %}`
```

### 13. Product Variants List #

Displays product variant options such as size or color selectors.

File: `templates/product.jinja`

`{% include 'vitrin:products/variants_list.jinja' %}`

### 14. Product Custom Input Fields #

Displays custom input fields for product personalization.

File: `templates/product.jinja`

```
``
```

### 15. Grouped Product #

Displays grouped or related products on the product page.

File: `templates/product.jinja`

`{% include 'vitrin:products/grouped-product.jinja' %}`

## Future replacements #

When more legacy templates are replaced, they will be added to this page using the same format.

Modified at 2026-10-20 09:51:20

Previous

Legacy Templates

Next

home.jinja
