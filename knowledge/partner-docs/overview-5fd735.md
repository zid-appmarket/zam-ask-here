---
# Synced from https://docs.zid.sa/overview-1379323m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-overview-5fd735
title: "Overview"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/overview-1379323m0
tags: [from-docs-site, partner-docs]
language: en
---

> Overview - Zid Docs
# Overview

# Templates #

Templates define how each **storefront route** is rendered in Zid using **Jinja2**.

Each template file maps to a specific page type (e.g., product, cart, homepage) and determines the **layout, sections, and components** shown to customers.

## Templates #

Each template in this list links to the **Template Library**, where you'll find code examples and UI previews.

You can name components as sections as you please, however templates and layout files names and directories need to be standardized to something our system recognize.

### Core Templates #

Template Purpose Route Path Operation

**home.jinja** (https://docs.zid.sa/home-jinja-1914518m0) Homepage layout with banners, featured collections, or products. `/` `home`

**product.jinja** (https://docs.zid.sa/product-jinja-1914519m0) Individual product details page. `/products/{product}` `product_details`

**cart.jinja** (https://docs.zid.sa/cart-jinja-1914520m0) Shopping cart with items and totals. `/cart` `cart_page`

**category.jinja** (https://docs.zid.sa/category-jinja-1914521m0) Single category page with product listings. `/categories/{category}` `category_details`

### Product Discovery Templates #

Template Purpose Route Path Operation

**products.jinja** (https://docs.zid.sa/products-jinja-1914522m0) General product listing (all products). `/products` `list_products`

**categories.jinja** (https://docs.zid.sa/categories-jinja-1914523m0) Overview of categories with links. `/categories` `list_categories`

**brands.jinja (https://docs.zid.sa/brands-jinja-2427114m0)** Displays all store brands. `/brands` Not supported

**brand.jinja (https://docs.zid.sa/brand-jinja-2427123m0)** Displays a specific brand and its products. `/brands/{slug_brand}` Not supported

### Content Templates #

Template Purpose Route Path Operation

**blog.jinja** (https://docs.zid.sa/blog-jinja-1914525m0) Displays a single blog post. `/blogs/{slug}` `blogs`

**page.jinja** (https://docs.zid.sa/page-jinja-1914524m0) Generic CMS/content page. `/pages/{slug}` `pages`

### Support Templates #

Template Purpose Route Path Operation

**faqs.jinja** (https://docs.zid.sa/faqs-jinja-1914526m0) Frequently Asked Questions. `/faqs` `faqs`

**questions.jinja** (https://docs.zid.sa/questions-jinja-1914528m0) Product-specific Q&A. `/products/{slug}/questions` `product_questions`

**reviews.jinja** (https://docs.zid.sa/reviews-jinja-1914527m0) Customer reviews section. `/products/{slug}/reviews` `product_reviews`

**shipping_payment.jinja** (https://docs.zid.sa/shipping-payment-jinja-1914529m0) Shipping & payment info page. `/shipping-and-payment` `shipping_payment`

### Utility Templates #

Template Purpose Route Path Operation

**404_not_found.jinja** (https://docs.zid.sa/404-not-found-jinja-1914530m0) Error page for missing content. Error handler `not_found`

### Key Features (All Templates) #

All templates **extend** the base template `layout.jinja`:

```
``
```

Common components like header and footer are included automatically.

Support for multilingual content with _( ) translations.

Assets are referenced with the asset_url filter:

```
``
```

Use url_for() filter to generate URLs instead of hardcoding:

```
``
```

Brand routes are not currently supported by url_for(). Use /brands for the brands listing page and /brands/{slug_brand} for individual brand pages.

Modified at 2026-09-15 09:55:18

Previous

Architecture

Next

Overridable Templates
