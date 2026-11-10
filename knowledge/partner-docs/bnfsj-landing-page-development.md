---
# Synced from https://docs.zid.sa/bnfsj-landing-page-development-2488608m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-bnfsj-landing-page-development
title: "Bnfsj Landing Page Development"
product: theme_market
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/bnfsj-landing-page-development-2488608m0
tags: [from-docs-site, partner-docs]
language: en
---

> Bnfsj Landing Page Development - Zid Docs
# Bnfsj Landing Page Development

Learn how the **Bnfsj theme** is structured and how to build custom product landing pages on Zid's Vitrin platform.

This guide covers the theme architecture, project structure, development setup, customization options, testing, and release process.

## **About Bnfsj** #

Bnfsj is a **product landing-page theme** for Zid's Vitrin platform. A single theme serves every landing page: each page selects a catalog product and defines its own collection of sections through the merchant editor.

You don't need to fork the theme for individual stores or products. Instead, create reusable sections and styles that merchants can arrange and customize.

## 1. How a Page Is Rendered #

Bnfsj uses a layered structure to render landing pages, combining a shared layout, page-specific sections, and product components.

### Rendering structure #

```
`layout.jinja <html>, <head>, fonts, CSS variables, shared scripts
└── templates/landing.jinja {% template_components %} renders the page's sections in order
├── sections/header.jinja
├── sections/product-section.jinja ← uses components/*.jinja + bnfsj-product.js
├── sections/<any other section>.jinja
└── components/product-purchase-bar.jinja (sticky Buy now bar, always rendered)`
```

### Rendering components #

**1. Base layout — `layout.jinja`**

Reads the global design settings, including font, colors, radius, width, and spacing, and defines them as CSS variables on `:root` (`--bnfsj-primary`, `--bnfsj-surface`, and so on).

It also loads:

Bootstrap (RTL or LTR, depending on language)

Slick

`bnfsj.css`

`bnfsj-sections.js`

**2. Landing-page template — `templates/landing.jinja`**

Renders the merchant-configured sections using `{% template_components %}`.

If the page has no configured sections, it falls back to the product section.

Exposes `window.productObj` for the SDK.

Always includes the purchase bar.

**3. Individual sections**

Each section renders a specific block of the page using its own `settings`.

**4. Product runtime**

The product runtime (`assets/bnfsj-product.js`, built from `src/product/`) manages:

Variant selection

Quantity

Gallery

Add to cart

Buy now

Dynamic bundles

## 2. Project Structure #

The following files and directories make up the Bnfsj theme project.

### Theme files and directories #

Path Purpose Shipped in ZIP

`layout.jinja` Page shell; converts layout settings into `--bnfsj-*` CSS variables Yes

`layout.schema.json` Editor controls for global design (font, colors, radius, width, spacing, custom CSS) Yes

`layout.json` Default layout settings for Arabic and English Yes

`templates/landing.jinja` Landing-page template with sections, purchase bar, and bundle handling Yes

`templates/landing.schema.json` Template-level settings (currently none) Yes

`sections/*.jinja` Individual merchant-editable sections Yes

`sections/*.schema.json` Editor controls for each section (required) Yes

`components/*.jinja` Product partials for gallery, options, actions, quantity, stock alerts, and purchase bar Yes

`assets/*` (others) Vendor libraries, icons, images, and legacy CSS Yes

`locale/ar/LC_MESSAGES/messages.po` Arabic translations of `_('...')` strings Yes

`src/product/*.js` Product runtime ES modules bundled using esbuild No

`preset.json` Default starter page (6 sections) and layout settings No

`tests/` Python template/build tests and JavaScript runtime tests; `fixtures/madar.json` contains the sample product No

## **Note — Theme packaging** #

Only `layout.*` and the `assets`, `components`, `layouts`, `locale`, `sections`, and `templates` directories are included in the theme ZIP. Other project files and folders, including `docs/`, are ignored during the build.

### Available Sections #

Bnfsj provides the following reusable sections, which merchants can configure in the editor.

Section file Editor name Main settings

`header` Header Logo, mobile logo

`product-section` Product Title, description (falls back to product data)

`main-slider` Slider Slides list, hide dots, colors

`banner` Banner Image, title, description, URL

`text-section` Text Text

`ad-section` Text (announcement) Text, colors

`features-section` Features Up to 4 icon and text items, colors

`features-section-2` Features 2 Title, items, background color/image

`features-section-3` Features 3 Items (image and text rows)

`ggallery` Gallery Title, image fit, images

`video` Video Title, video, controls, autoplay

`count-down-timer` Countdown timer Title, date, text after end, colors

`testimonials` Testimonials Title, list, hide dots

`partners` Partners Title, logos

`payments` Payments options Hide

`social-media` Social media Hide

`store-logo` Store logo Hide, image

`copywrites` Copyrights Text, links, colors

## 3. Setup and Daily Commands #

### Prerequisites #

Before working with the Bnfsj theme, make sure your environment meets these requirements:

Requirement Version

Python 3.11 or later

Node.js 20 or later

### Set Up Your Development Environment #

Run the following commands:

```
`python3 -m venv .venv && source .venv/bin/activate
python -m pip install 'Jinja2>=3.1,<4' 'pytest>=8,<10'
npm ci --ignore-scripts`
```

### Common Development Commands #

Use these commands to test, validate, preview, and package the theme.

Task Command

Run all tests `python -m pytest tests -q && npm test`

Validate and render (Arabic) `python scripts/validate.py --language ar`

Validate and render (English) `python scripts/validate.py --language en`

Rebuild product runtime only `npm run build:runtime`

Build the theme ZIP `python scripts/build.py --output dist/bnfsj.zip --manifest dist/assets-manifest.json`

Validate the built ZIP `python scripts/validate.py dist/bnfsj.zip`

### Preview the Theme Locally #

**Step 1: Generate the HTML preview.**

```
`python scripts/validate.py --language en --html-output dist/preview.html`
```

**Step 2: Start the local server.**

```
`python -m http.server 8000 --bind 127.0.0.1`
```

**Step 3: Open the preview in your browser.**

`http://127.0.0.1:8000/dist/preview.html`

## **Important — Local preview limitations** #

The local preview uses sample product data and stubbed `vitrin:` partials. Checkout, SDK calls, bundles, and editor saving must be tested directly on Vitrin.

## 4. Build a Landing Page with Your Own Design #

Choose the simplest customization approach that meets your design requirements.

Most landing-page designs can be implemented using **Path A**, with one or two additional sections from **Path B**.

### Choose Your Development Path #

Path Approach When to use

**Path A** Configure only (no code) Existing sections already support your layout, and you only need to customize the appearance

**Path B** Add a new section Your design requires a block that the existing sections don't provide

**Path C** Change the product area You need to customize the shared product section or its runtime behavior

### Path A: Configure Only (No Code) #

Use this approach when the existing sections support your desired layout and you only need to change the visual design.

**Step 1: Create a landing page**

In the merchant editor, create a landing page and select the catalog product.

**Step 2: Arrange your sections**

Add, remove, reorder, or repeat sections as needed.

## **Important** #

Keep **exactly one Product section** on each landing page.

**Step 3: Configure Layout settings**

Open **Layout settings** and customize the following:

Setting group Options

Typography Font family

Colors and shape Primary, text on primary, page background, text, card background, borders, secondary text, corner radius

Spacing and width Content width, spacing between sections

Custom styles Additional CSS for the current page only

**Step 4: Add your images**

Upload images through the store's media library.

Do not hotlink local files or example image paths.

**Example — Madar landing page**

The `examples/madar/` directory provides a complete reference for this approach, featuring ten sections and the Zid color palette without any theme code changes.

Refer to its README for preview instructions.

### Path B: Add a New Section #

Use this approach when the design requires a block that isn't available in the existing sections, such as:

A comparison table

An FAQ section

A hero section with a custom layout

Follow these steps to create and integrate a new section.

#### Step 1: Create the Section Template #

Create the file:

`sections/my-section.jinja`

```
`<section section-id="{{ sectionId }}"
class="bnfsj-section bnfsj-my-section"
style="{% if settings.background_color %}--section-background: {{ settings.background_color }};{% endif %}">
<div class="bnfsj-container">
{% if settings.title %}<h2 class="bnfsj-heading">{{ settings.title }}</h2>{% endif %}
{% for item in settings.items or [] %}
<div class="bnfsj-my-section__item">
{% if item.image %}<img loading="lazy" src="{{ image_url(item.image) }}" alt="{{ item.text }}">{% endif %}
{% if item.text %}<p>{{ item.text }}</p>{% endif %}
</div>
{% endfor %}
</div>
</section>`
```

**Section template requirements**

Requirement Implementation

Root element Use `<section section-id="{{ sectionId }}" ...>` so the editor can identify and update the block

Standard spacing Add the `bnfsj-section` class

Content width Wrap content in `bnfsj-container`

CSS isolation Use a section-specific prefix such as `bnfsj-my-section`

Optional settings Use `{% if %}` and `or []` for optional values and lists

Merchant colors Pass values through CSS custom properties such as `--section-background` and `--section-color`

Images Use `image_url(value)`; supports `w=`, `q=`, and `f='auto'` for responsive `srcset` (see `main-slider.jinja`)

Theme assets Use `{{ 'file.svg' | asset_url }}`

Fixed UI text Use `{{ _('Read more') }}` with Arabic translations in `messages.po`

Product data Access `product` (for example `product.name`, `product.selected_product.formatted_price`)

Template syntax Use Jinja syntax only

## **Important — Section rendering rules** #

Never style sections using `section-id`, because sections can be repeated and reordered.

Treat every setting as optional. Newly added sections must render even when their settings are empty.

Do not hardcode product details.

Twig-only syntax, such as `is empty`, fails validation.

English is the source language for fixed UI strings. Add Arabic translations to `locale/ar/LC_MESSAGES/messages.po`.

#### Step 2: Create the Section Schema #

Every new section requires a corresponding schema file.

Create:

`sections/my-section.schema.json`

```
` {
"section_id" : "uuid" ,
"template" : "sections/my-section.jinja" ,
"name" : { "ar" : "قسمي" , "en" : "My section" } ,
"icon" : "fal fa-sparkles" ,
"display" : true ,
"settings" : [
{ "id" : "title" , "type" : "text" , "label" : { "ar" : "العنوان" , "en" : "Title" } } ,
{
"id" : "items" ,
"type" : "list" ,
"max_items" : 6 ,
"label" : { "ar" : "العناصر" , "en" : "Items" } ,
"settings" : [
{ "id" : "text" , "type" : "text" , "label" : { "ar" : "النص" , "en" : "Text" } } ,
{ "id" : "image" , "type" : "image" , "label" : { "ar" : "الصورة" , "en" : "Image" } }
]
} ,
{ "id" : "background_color" , "type" : "color" , "label" : { "ar" : "لون الخلفية" , "en" : "Background color" } }
]
} `
```

**Schema validation requirements**

The validator enforces the following rules:

Element Requirement

File naming `sections/X.schema.json` must reference `"template": "sections/X.jinja"`

Localized values `name` and every `label` must contain both `ar` and `en` strings

Settings Must be a non-empty list with unique `id` values

Nested settings `list` and `fieldset` require non-empty nested `settings`

Range settings `range` requires numeric `min` and `max` values, where `min` ≤ `max`

Choice settings `select` and `radio` require `options`

**Supported setting types**

**Text and values:** `text`, `textarea`, `richtext`, `number`

**Media and appearance:** `color`, `url`, `image`, `video`

**Selections and controls:** `checkbox`, `checkboxes`, `radio`, `range`, `select`

**Catalog data:** `product`, `products`, `category`, `category_products`

**Structured settings:** `snippet`, `list`, `fieldset`

#### Step 3: Style Your Section #

Add the section's styles to:

`assets/bnfsj.css`

```
``
```

**Available design tokens**

The following CSS variables are configured through Layout settings and should be reused throughout your custom sections.

Variable Purpose

`--bnfsj-primary` / `--bnfsj-on-primary` Brand color and text on it

`--bnfsj-background` / `--bnfsj-foreground` Page background and main text

`--bnfsj-surface` Card or section background

`--bnfsj-border` Borders and dividers

`--bnfsj-muted` Secondary text

`--bnfsj-radius` Corner radius

`--bnfsj-width` Maximum content width

`--bnfsj-space`, `--bnfsj-space-sm`, `--bnfsj-space-lg` Section spacing scale

`--bnfsj-font` Selected font family

`--bnfsj-danger`, `--bnfsj-success` Status colors

**Styling guidelines**

Use design tokens rather than fixed colors so pages can be rebranded from Layout settings without code changes.

Write RTL-safe CSS using logical properties such as `margin-inline-start`, `padding-inline`, `inset-inline-end`, and `text-align: start`.

Scope CSS under your section class or `.bnfsj`.

Avoid global element selectors that could affect other sections or platform widgets.

Check layouts at mobile widths.

**Mobile layout note**

Arabic is the primary language, so RTL-safe styling is important.

Also consider the sticky purchase bar when testing mobile layouts. The `.bnfsj-main` class already reserves space at the bottom of the screen for the bar.

#### Step 4: Add Interactive Behavior (Optional) #

For carousels and countdowns, reuse the built-in JavaScript hooks rather than introducing new implementations.

**Existing interaction hooks**

Feature Hook Details

Carousels `data-bnfsj-carousel="main"` Main slider

Carousels `data-bnfsj-carousel="testimonials"` Testimonials slider

Carousels `data-bnfsj-carousel="partners"` Partners slider

Countdown `data-bnfsj-countdown` Countdown container

Countdown date `data-date="YYYY-MM-DD HH:mm"` Target date and time

Countdown values `data-countdown-part="days|hours|minutes|seconds"` Countdown display elements

Carousels use Slick with RTL support.

**Adding custom behavior**

If your section requires new JavaScript behavior, add it to:

`assets/bnfsj-sections.js`

Follow the existing implementation pattern:

1 .

Initialize behavior separately for each element within a given root.

2 .

Maintain a registry to prevent elements from being initialized more than once.

3 .

Clean up initialized elements in `destroy()`.

**Note — Live editor updates**

The merchant editor dynamically inserts and removes sections.

A `MutationObserver` handles calls to `initialize()` and `destroy()`, so custom behavior must follow the same lifecycle pattern.

#### Step 5: Add Tests and Examples #

After implementing the section, validate that it renders correctly.

**Run validation in both languages:**

```
`python scripts/validate.py --language ar
python scripts/validate.py --language en`
```

These commands render every section using values generated from its schema. Both validations must pass.

**Verify section rendering through the landing template:**

`tests/test_tools.py::test_all_sections_render_through_landing_entrypoint_in_both_languages`

This test renders all sections through the landing template.

**Optional:** Add the section to one of the following:

`preset.json` — the default starter page

`examples/` — an example landing page

### Path C: Change the Product Area #

The product section and the files in `components/` are shared across all landing pages.

They interact with the product runtime using `data-bnfsj-*` attributes.

You can freely restyle these components using CSS, but their markup must retain the required runtime contract.

## **Product markup requirements** #

**Important — Preserve runtime attributes**

Do not remove or rename any `data-bnfsj-*` attributes or required IDs, including:

`#product-form`

`#product-id`

`#product-view-add-to-cart`

**Modify runtime behavior**

Make runtime logic changes in:

`src/product/*.js`

Do not modify the generated `assets/bnfsj-product.js` directly.

After making changes:

1 .

Run `npm test` to rebuild the bundle.

2 .

Commit the rebuilt asset.

**Maintain dynamic bundle handling**

Keep `dynamic_bundle` behavior intact.

Purchase buttons must remain locked until the bundle kit reports that the selection is complete.

## 5. Releasing a New Theme Version #

Before releasing a new version of Bnfsj, complete the validation, versioning, and packaging steps below.

### Step 1: Run the Full Validation Suite #

Run all tests, validate both languages, build the ZIP, and validate the resulting package.

```
`python -m pytest tests -q && npm test
python scripts/validate.py --language ar && python scripts/validate.py --language en
python scripts/build.py --output dist/bnfsj.zip && python scripts/validate.py dist/bnfsj.zip`
```

### Step 2: Update the Theme Version #

Update `"version"` in `package.json` using the `X.Y.Z` format.

The deployment workflow sends this version when changes are pushed to `master` or `develop`.

### Step 3: Update Asset Cache Versions #

If any of the following files have changed, update their `?v=` query parameters:

`bnfsj.css`

`bnfsj-sections.js`

`bnfsj-product.js`

Update the relevant asset tags in:

`layout.jinja`

`templates/landing.jinja`

Also update `data-bnfsj-version` on `<body>`.

This prevents browsers from continuing to use outdated cached files.

### Step 4: Release Runtime Changes as a New Version #

## **Warning — Runtime compatibility** #

Always ship runtime changes as a **new theme version**, rather than an in-place push.

An in-place update can cause new templates to load alongside an outdated cached `bnfsj-product.js`, resulting in incompatible behavior.

### Step 5: Open a Pull Request #

Open a pull request into `master`.

Do not commit the following files or directories:

`dist/`

`.vitrin/`

`.venv/`

ZIP files

### Package Validation Limits #

The build and validation tools enforce the following limits:

Validation Requirement

Individual asset size Maximum 2 MB

Total package size Maximum 50 MB

Root structure Only the allowed folders and files

Asset references Every `asset_url` reference must point to an existing file in `assets/`

## 6. Checklist for a New Design #

Use this checklist before releasing a new landing-page design.

### Design and Configuration #

Checked whether existing sections and Layout settings cover the design (Path A).

Created matching `.jinja` and `.schema.json` files for every new section.

Used `<section section-id="{{ sectionId }}">` as the root, with `bnfsj-section` and `bnfsj-container`.

Made all settings optional so empty sections render without errors.

### Localization and Styling #

Added Arabic and English section names and labels.

Wrapped fixed strings in `_()` and added Arabic translations to `messages.po`.

Added scoped styles to `assets/bnfsj.css` using `--bnfsj-*` design tokens and RTL-safe logical properties.

Used `image_url()` for images and `asset_url` for theme files, with each asset under 2 MB.

### Product Integration #

Avoided hardcoding product data, store data, or section IDs.

Preserved the product markup contract, including `data-bnfsj-*` attributes and form IDs.

### Testing and Release #

Passed all tests, both language validations, and the ZIP build.

Tested on Vitrin in Arabic and English.

Tested on desktop and mobile, including add to cart and buy now.

Updated the `package.json` version and asset `?v=` values.

**Related documentation**

Theme Development (https://docs.zid.sa/theme-development)

Theme Architecture (https://docs.zid.sa/architecture-1379322m0)

Schema Files (https://docs.zid.sa/schema-files-1702180m0)

Vitrin's Jinja Extensions (https://docs.zid.sa/vitrins-jinja-extensions-1379354m0)

Modified at 2026-10-20 09:27:15

Previous

Theme Development

Next

Vitrin Changelog
