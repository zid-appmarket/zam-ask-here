---
# Synced from https://docs.zid.sa/twig-to-jinja-1379319m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-twig-to-jinja
title: "Twig to Jinja"
product: theme_market
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/twig-to-jinja-1379319m0
tags: [from-docs-site, partner-docs]
language: en
---

> Twig to Jinja - Zid Docs
# Twig to Jinja

# Twig ➜ Jinja Migration Guide #

## 1) Overview #

A practical cheat sheet to move templates from **Twig** to **Jinja**, with filename rules, filter/tag equivalents, globals, syntax tips, translation changes, and common include mappings.

## 2) File and variable names #

Rename all `.twig` and `.html` files to `.jinja`.

following the standard python snake_case naming for variables, files, marcors, etc.. is preffered for better code readablity. However this isn't a strict rule.

## 3) Filters — Direct Equivalents #

Twig Jinja Notes

`raw` `safe` Marks string as safe HTML so jinja doesn't double-escape.

`json_encode()` `tojson` Useful for embedding data in `<script>`.

`filter` `select` / `reject` Jinja uses tests/expressions: `items | selectattr('x', 'equalto', 1)` etc.

`url_encode` `urlencode` Percent-encodes strings.

## 4) Helper Functions → Jinja Filters #

In many cases, function-style helpers in Twig become filters in Jinja.

Twig (function/helper) Jinja (filter) Notes

`asset_url` `asset_url` Same name (environment-provided).

`assetUrl` `asset_url` Switch to snake_case.

`strReplace(haystack, search, replace)` `haystack | replace(search, replace)` Jinja `replace` takes `(old, new)`.

`imageUrl(store_partner.image,{ w: 250, q: 100, f:'auto' })` `image_url(store_partner.image, w=250, q=100, f='auto')` Jinja references the params directly and switch to `snake_case`.

**Prebound context helpers**

Name What it does Typical usage

`today()` Current date in the request’s timezone, preformatted `{{ today() }}`

`now()` Current time in the request’s timezone `{{ now() }}`

`format_datetime` DateTime formatter with `tz`/`locale` already set `{{ format_datetime(order.created_at) }}`

`format_time` Time formatter with `tz`/`locale` already set `{{ format_time(order.created_at) }}`

`url_for` Application route builder `{{ url_for('list_products') }}`

### Usage examples #

```
`{# Current date (uses prebound fmt) #}
{{ today() }} {# e.g., 2025/08/20 #}

{# Current time #}
{{ now() }} {# e.g., 17:05 #}

{# Format a specific datetime with defaults (tz/locale are prebound) #}
{{ format_datetime(order.created_at) }}

{# Choose a predefined width: "full" | "long" | "medium" | "short" #}
{{ format_datetime(order.created_at, fmt="long") }}

{# Override the format string if needed #}
{{ format_datetime(order.created_at, fmt="%Y-%m-%d %H:%M") }}

{# Format only the time portion #}
{{ format_time(order.created_at) }}`
```

### Notes #

If `datetime_`/`time_` is omitted (`None`), the helpers use “now” in the request’s timezone.

`fmt` accepts `"full" | "long" | "medium" | "short"` or a custom format string.

`tz` and `locale` are already supplied via partial application; override only when you truly need to.

## 5) Globals & URL Utilities #

Twig Global / Helper Jinja / App Equivalent Example

`requestAdd(query: dict)` `session.url.include_query_params(**params)` `session.url.include_query_params(page=2)`

`requestGet` `session.query_params.get()` `session.query_params.get('q')`

`requestUri` `session.url.path` `/products/123`

`requestInputs` `session.url.params` Dict-like of current query.

`urlWithQuery` `session.url.include_query_params(**params)` —

`rangeN` Python `range(n)` `range(5)` → 0..4

`rangeNWithStep` Python `range(start, stop, step)` `range(0, 10, 2)`

`tDate` — (no direct equivalent) Use Babel date/time formatters.

— `url_for(name, *, localize=True, query_params=None, **path_params)` Returns app route: `url_for('list_products')`

`url_for` is provided by your app. Use `query_params` to append query strings.

## 6) Data: Pagination Key Mapping #

Concept Twig (old) Jinja (new)

Items `response.data` `response.results`

Total count `response.total` `response.count`

Current page `response.current_page` `response.page`

Page size / per page `response.per_page` `response.page_size`

Total pages `response.last_page` `response.pages_count`

## 7) Syntax Differences & Tips #

### 7.1 Null safety / defaults #

Task Twig Jinja Notes

Default value `var ?? 'x'` `var or 'x'` **or** `var | default('x')` Short alias: `| d('x')`

Force default on falsy — `default('x', true)` Treats `None,'' ,0,[],False` as “missing”.

Null literal `null` `None` —

**Examples**

```
`{{ title or 'Untitled' }}
{{ title | default('Untitled') }}
{{ count | default(0, true) }}`
```

### 7.2 Include with a small local context #

Twig Jinja

`{% include 'x' with {a: 1} %}` `{% with a=1 %}{% include 'x' %}{% endwith %}`

### 7.3 Translations #

Old: `locals.hello_world`

New: `_("Hello world")`

**Variable placeholders (gettext style):**

```
`{{ _("Hello %(name)s", name=user.name) }}
{{ ngettext("%(n)s item", "%(n)s items", n, n=n) }}`
```

## 8) Settings Schema Extraction #

Move the JSON inside `{% schema %}...{% endschema %}` to a **separate** `{}.schema.json` file with the same base filename.

Remove the schema block from the `.jinja` template.

## 9) Translations Migration (JSON ➜ PO) #

1 .

Replace all `locals.*` usages with `_('English text')` using strings from `en.json`.

2 .

Generate a `.po` file and migrate Arabic strings from `ar.json` into that PO.

3 .

Replace runtime formatting args with gettext placeholders:

Before: `_("Welcome, {}").format(name)`

After: `_("Welcome, %(name)s", name=name)`

## 10) Template Conversion (Vitrin-managed Includes) #

When including or extending **vitrin-managed** templates, prefix with `vitrin:{template}`.

Old (Twig-like) New (Jinja)

`{{ template_for_product_badge }}` `{% include 'vitrin:products/badge.jinja' %}`

`{{ template_for_product_variants_list }}` `{% include 'vitrin:products/variants_list.jinja' %}`

`{{ template_for_product_variants_dropdown }}` `{% include 'vitrin:products/variants_dropdown.jinja' %}`

`{{ template_for_product_payments_widget }}` `{% include 'vitrin:products/payment_widgets.jinja' %}`

`{{ template_for_product_custom_input_fields }}` `{% include 'vitrin:products/custom_input_fields' %}`

`{{ template_for_product_loyalty_points_widget }}` `{% include 'vitrin:products/loyalty_points_widget.jinja' %}`

`{{ template_for_product_apple_pay_button }}` `{% include 'vitrin:checkout/apple-pay-quick-checkout.jinja' %}`

`{{ template_for_product_metafields }}` `{% include 'vitrin:shared/metafields.jinja' %}`

`{{ template_for_product_grouped }}` `{% include 'vitrin:products/bundle-products.jinja' %}`

`{{ template_for_products_badge }}` `{% include 'vitrin:products/badge.jinja' %}`

`{{ template_for_products_attributes }}` `{% include 'vitrin:products/filters.jinja' %}`

`{{ account_profile_template_content|safe }}` `{% include 'vitrin:account/profile.jinja' %}`

`{{ template_for_mazeed_badge }}` `{% include 'vitrin:shared/mazeed_badge.jinja' %}`

`{{ template_for_cart_products_list }}` `{% include 'vitrin:cart/products_list.jinja' %}`

`{{ template_for_cart_payments_widget }}` `{% include 'vitrin:cart/payment_widgets.jinja' %}`

`{{ template_for_cart_gifts_widget }}` `{% include 'vitrin:cart/gift-card.jinja' %}`

`{{ template_for_category_metafields }}` `{% include 'vitrin:shared/metafields.jinja' %}`

`{{ template_for_blogs_metafields }}` `{% include 'vitrin:shared/metafields.jinja' %}`

`{{ template_for_shipping_destination_currency_lang }}` `{% include 'vitrin:shared/locale_modal.jinja' %}`

## 11) Quick Examples #

### Replace `strReplace`: #

```
`{# Twig-ish #}
{{ strReplace(title, 'old', 'new') }}

{# Jinja #}
{{ title | replace('old', 'new') }}`
```

### Build a URL with extra query params: #

```
`{{ session.url.include_query_params(page=page+1) }}`
```

### Route generation: #

```
`{{ url_for('list_products') }}
{{ url_for('product_details', path_params={'id': product.id}) }}`
```

### Date/time formatting (Babel): #

```
`{{ format_datetime(order.created_at, format='medium', locale=session.lang) }}
{{ format_time(order.created_at, format='short') }}`
```

## 12) Gotchas #

`select`/`reject` rely on tests/expressions (e.g., `selectattr`, `rejectattr`, `equalto`).

Prefer gettext placeholders (`%(name)s`) over string concatenation for translatable messages.

Modified at 2026-07-30 11:49:13

Previous

Moving to Vitrin Using LLMs

Next

Breaking Changes
