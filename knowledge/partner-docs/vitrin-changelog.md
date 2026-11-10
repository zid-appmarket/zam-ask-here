---
# Synced from https://docs.zid.sa/vitrin-changelog-1769483m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-vitrin-changelog
title: "Vitrin Changelog"
product: theme_market
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/vitrin-changelog-1769483m0
tags: [from-docs-site, partner-docs]
language: en
---

> Vitrin Changelog - Zid Docs
# Vitrin Changelog

September 15, 2026

Feature Update Products

### Product Brands Theme Support #

Vitrin now supports Product Brands across the storefront. Theme developers can use `brands.jinja` to display all store brands at `/brands` and `brand.jinja` to display a specific brand and its products at `/brands/{slug_brand}`.

The `product.jinja` template also now exposes `product.brand.name` and `product.brand.logo`, allowing themes to display the assigned brand on product pages.

Brand routes are not currently supported by `url_for()`.

Read full post → (https://docs.zid.sa/brands-jinja-2427114m0)

August 20, 2026

Action Required Payment

### Bank Discounts Theme Support #

Vitrin now supports Bank Discounts, allowing merchants using ZidPay to offer discounts for eligible banks and card types, including Mada, Visa, and Mastercard. Theme developers are required to add the Bank Discounts shared template to both the product details and cart pages:

`{% include 'vitrin:shared/bank_discounts.jinja' %}`

Without this template, Bank Discounts configured by merchants will not appear on these pages. No theme changes are required for checkout.

Read full post → (https://docs.zid.sa/bank-discounts-2332488m0)

December 23, 2025

Action Required Feature Update

### Multi-Inventory & Region–Language Modal #

We’ve introduced support for the **multi-inventory** feature along with a new

**region & language selection modal**.

Theme developers are required to implement this update to ensure compatibility and enable

full migration of remaining stores. This change should also be applied to previously released themes.

QA test cases will be updated to cover this functionality moving forward.

Read full post → (https://docs.zid.sa/region-language-popup-1861342m0)

December 16, 2025

Performance

### Grouped Products Template Update #

We’ve introduced a new template for grouped products as part of last week’s updates.

Theme developers are required to apply this change to ensure compatibility with the latest Vitrin structure. What changed?

A simple substitution of the old Twig template with the new Jinja template:

Old (Twig):

{{ template_for_product_grouped }}

New (Jinja):

{% include 'vitrin:products/grouped-product.jinja' %}

Example implementation → (https://github.com/zidsa/soft-theme-vitrin/commit/574ea3d5b6a8a6ded6b1a6607d7590cd974c4222)

December 11, 2025

Action Required Payment

### Apple Pay Quick Checkout Template Support #

Vitrin now fully supports the new Apple Pay Quick Checkout template, enabling faster and more seamless checkout experiences for customers.

All theme developers are required to update their themes to use this new template as soon as possible to prevent any checkout issues.

Read full post → (https://docs.zid.sa/apple-pay-quick-checkout-1859764m0)

December 7, 2025

Checkout

### Checkout as a Pop-up #

The checkout popup feature allows customers to display the checkout page inside a modal dialog instead of redirecting customers away from the current page. When enabled, this creates a smoother, faster checkout experience and allows customers to complete their purchase without losing context.

Read full post → (https://docs.zid.sa/checkout-as-a-popup-1806668m0)

December 4, 2025

Performance

### UndefinedErrors Now Visible in Dev Preview #

Undefined-variable errors are now displayed in the development preview environment.

Themes that previously looked fine may now show errors—this is expected.

Use this update to fix missing fallbacks, handle optional values, and rely on safeget where needed.

December 4, 2025

Performance

### Updated Settings Mapping #

The Store Settings Mapping page has been updated with corrected and complete mappings.

Developers should review the page to ensure their themes reflect the correct configuration behavior.

Read full post → (https://docs.zid.sa/store-settings-mapping-1379317m0)

December 3, 2025

Performance

### Validate Endpoint Now Available #

We’ve added a new /validate endpoint is now available for all partners.

Use it to instantly validate theme files, catch issues early, and shorten the testing cycle.

Read full post → (https://docs.zid.sa/theme-development#theme-testing)

November 18, 2025

Performance

### Image Handling & Performance Update #

We’ve added a detailed guide in the Performance page for the new `image_url` helper, the equivalent of the old `imageUrl` function.

We strongly recommend all developers use `image_url` to generate responsive, optimized images, which greatly enhances performance and reduces page load time.

Read full post → (https://docs.zid.sa/performance-1379358m0)

November 18, 2025

Products Categoris

### Route Updates for Products & Categories #

**Products Route:**

Previously, both `/p` and `/products` were supported. Now, only `/products` is valid.

`/p` will permanently redirect to `/products`.

**Categories Route:**

`/c` now permanently redirects to `/categories`. **🚨 IMPORTANT:** Always use the `url_for` filter when generating links. Hard-coding URLs may break your theme if routes change again in the future.

Example `url_for` for a product details link

(https://github.com/zidsa/soft-theme-vitrin/blob/36c31cb1aaa2116c7be9527d12b707ce63bdc213/templates/reviews.jinja#L15)

Read full post → (https://docs.zid.sa/overview-1379323m0)

October 27, 2025

Action Required Login

### Customer Login as a Pop-up #

The login popup feature allows users to authenticate without leaving the current page. When enabled, it provides a modal dialog for user login, creating a smoother and more seamless user experience.

Read full post → (https://docs.zid.sa/login-popup-1702155m0)

October 20, 2025

Action Required Login

### Customer Address as a Pop-up #

The address dialog feature allows users to add or edit their shipping addresses without leaving the current page.

When enabled, it provides a modal dialog for address management, creating a smoother and more seamless user

experience.

Read full post → (https://docs.zid.sa/addresses-popup-1706785m0)

Modified at 2026-09-15 09:59:47

Previous

Bnfsj Landing Page Development

Next

Creating and Managing Theme Presets
