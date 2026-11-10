---
# Synced from https://docs.zid.sa/blogs-jinja-2125764m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-blogs-jinja
title: "blogs.jinja"
product: theme_market
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/blogs-jinja-2125764m0
tags: [from-docs-site, partner-docs]
language: en
---

> blogs.jinja - Zid Docs
# blogs.jinja

**Route:** `/blogs`

**Path Operation:** `list_blogs`

Listing page for blog posts. Supports filtering by category via the

`?category={slug}` query parameter and pagination via `?page={n}` and

`?page_size={n}`.

## Variables #

Variable Type

`blogs` PaginatedBlogPosts

`categories` PaginatedBlogCategories

`store` Store

`session` Session

## PaginatedBlogPosts #

Property Description

`results` List of `BlogPost` for the current page

`count` Total number of matching posts

`page` Current page number

`page_size` Blogs per page (default `24`)

`pages_count` Total page count

## PaginatedBlogCategories #

Property Description

`results` List of `BlogCategory`

`count` / `page` / `page_size` / `pages_count` Same shape as above

## BlogCategory #

Property Description

`id` Category ID

`name` Localized category name

`slug` URL slug — use as `?category={slug}`

`description` Optional description

`icon` Optional icon URL

## BlogPost (fields used in listing) #

Property Description

`id` Post ID

`title` Post title

`slug` URL slug — link as `/blogs/{slug}`

`snippet` Short summary (HTML)

`published_at` ISO date string

`cover` `BlogPostMedia` (use `cover.image.medium`)

`category` `BlogCategoryShort` (`name`, `slug`) — optional

`tags` List of `BlogTag` (`tag.name`, `tag.slug`)

`recommended_product_ids` List of product IDs (resolved into `related_products` on the detail page only)

## Filtering by category #

Listings can be filtered with the `?category={slug}` query parameter. When no

`category` is set, the backend defaults to the first category in

`categories.results` — the listing is never empty as long as at least one

category exists.

Read the active filter from the request:

```
``
```

Render category pills, marking the active one:

```
``
```

Always reset to `?page=1` when the user changes category — pagination of the

old category is meaningless under the new one.

## Example #

```
``
```

Modified at 2026-05-03 17:15:15

Previous

page.jinja

Next

blog.jinja
