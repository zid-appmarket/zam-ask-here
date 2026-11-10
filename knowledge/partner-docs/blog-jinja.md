---
# Synced from https://docs.zid.sa/blog-jinja-1914525m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-blog-jinja
title: "blog.jinja"
product: theme_market
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/blog-jinja-1914525m0
tags: [from-docs-site, partner-docs]
language: en
---

> blog.jinja - Zid Docs
# blog.jinja

**Route:** `/blogs/{slug}`

**Path Operation:** `blogs`

Detail page for a single blog post.

## Variables #

Variable Type

`blog` BlogPost

`store` Store

`session` Session

## BlogPost Properties #

Property Description

`blog.id` Blog ID

`blog.title` Blog title

`blog.slug` URL slug

`blog.snippet` Short summary (HTML)

`blog.content` Full post body (HTML — use `| safe`)

`blog.published_at` ISO date string

`blog.cover` `BlogPostMedia` — see below

`blog.seo` `SEO` metadata

`blog.category` `BlogCategoryShort` (`id`, `name`, `slug`) — optional

`blog.tags` List of `BlogTag` (`id`, `name`, `slug`)

`blog.related_posts` List of `BlogPost`

`blog.recommended_product_ids` List of product IDs

`blog.related_products` List of `Product` (only present on the detail page when the post has recommended products)

## BlogPostMedia / ImageURLs #

Property Description

`cover.image.full_size` Full-size image

`cover.image.large` Large variant

`cover.image.medium` Medium variant

`cover.image.small` Small variant

`cover.image.thumbnail` Thumbnail

`cover.alt_text` Alt text

## Example #

```
``
```

Modified at 2026-05-03 17:10:29

Previous

blogs.jinja

Next

faqs.jinja
