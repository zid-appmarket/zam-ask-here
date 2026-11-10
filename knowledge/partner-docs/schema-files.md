---
# Synced from https://docs.zid.sa/schema-files-1702180m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-schema-files
title: "Schema files"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/schema-files-1702180m0
tags: [from-docs-site, partner-docs]
language: en
---

> Schema files - Zid Docs
# Schema files

The theme editor reads a JSON schema that defines **display settings** for merchants in the theme editor.

## Introduction #

Schema files are represenations of your theme's settings. They are required to:

1 .

Build the **settings form** in the Theme Editor (https://docs.zid.sa/theme-editor-1702203m0).

2 .

Define the keys (ids) that will allow you to reference the theme settings in your templates.

The schema files are split into two types, section schema files, and layout schema files.

**Note:** in the old theme system, the schema used to be part of the template.twig file, now it is a separate json file.

## Sections #

Each `section.jinja` is required to have a corresponding `section.schema.json` file in the same directory.

**Structure**

Field Type Description Required

name object {ar,en} Section title shown to the merchant (Arabic/English).

template string Path to the section’s Jinja template (e.g., "sections/image_slider.jinja").

settings array List of inputs the merchant can change (see Input Settings).

icon text Optional reference to an icon at the section parent level only. Use Remixicon class names without the `ri-` prefix (e.g., `box-3-line`, `image-add-line`). See Remixicon (https://remixicon.com/icon/) for available icons. **Note:** `icon` should only be defined at the parent section level, not within individual settings objects.

**Example**

This is an example of what a section schema `/sections/image_slider.schema.json` file would look like:

```
` {
"name" : {
"ar" : "شرائح الصور" ,
"en" : "Image Slider"
} ,
"settings" : [
{
"default" : true ,
"id" : "hide_dots" ,
"label" : {
"ar" : "إخفاء النقاط" ,
"en" : "Hide dots"
} ,
"type" : "checkbox"
}
] ,
"template" : "sections/image_slider.jinja"
} `
```

## Layout, Header, Footer #

These core jinja templates require a schema file each to represent the settings form in the theme editor. Therefore it is required you the following in your theme root directory:

`layout.schema.json`

`header.schema.json`

`footer.schema.json`

**Structure**

Field Type Description Required

name object {ar,en} Section title shown to the merchant (Arabic/English).

groups array List of objects that represent each group of settings. The structure of a group is almost identical to the schema of an individual section, but each group requires an id.

icon text Optional reference to an icon at the group parent level only. Use Remixicon class names without the `ri-` prefix (e.g., `box-3-line`, `image-add-line`). See Remixicon (https://remixicon.com/icon/) for available icons. **Note:** `icon` should only be defined at the parent group level, not within individual settings objects.

Example:

```
` {
"groups" : [
{
"icon" : "box-3-line" ,
"id" : "header" ,
"name" : {
"ar" : "رأس الصفحة" ,
"en" : "Header"
} ,
"settings" : [
{
"id" : "logo" ,
"info" : {
"ar" : "ارفع صورة بحجم 750 * 750 " ,
"en" : "This is an info text sample here"
} ,
"label" : {
"ar" : "الشعار" ,
"en" : "Logo"
} ,
"type" : "image"
}
]
}
] ,
"icon" : "layout-grid-line" ,
"name" : {
"ar" : "اعلى الصفحة" ,
"en" : "Header"
}
} `
```

**Note:** Each group will appear as a fieldset in the theme editor. You do not need to explicitly specify fieldset for these groups.

You can also view a live example in the Soft Theme Vitrin Repository (https://github.com/zidsa/soft-theme-vitrin/blob/master/layout.schema.json).

## Mapping schema to keys #

The settings object inside every template is a flattend version of your schema file. For example the following shorthand schema:

```
` {
"icon" : "fa fa-square" ,
"name" : {
"ar" : "اعلى الصفحة" ,
"en" : "Header"
} ,
"groups" : [
{
"id" : "header" ,
...
"settings" : [
{
"id" : "logo" ,
...
}
}
]
}
]
} `
```

Where the value of "logo" can be accessed as `settings.header_logo` in your jinja file templates.

The exception to this rule is any list settings. If a setting is inside a list, it will be treated as a list of objects that can be accessed like this in jinja:

```
` { % for image in safeget(settings , "images" , [ ] ) % } `
```

It is good to use `safeget` to handle cases where a variable could be null. You can add a default value as the third paremeter of the `safeget` global function.

## Icon Usage #

The `icon` field in schema files accepts Remixicon class names **without the `ri-` prefix**. Icons should only be defined at the **parent level** of section.

**How it looks:**

**Where to use:**

**Sections**: Add `icon` at the root level of the section schema (alongside `name`, `template`, `settings`)

**How to use:**

1 .

Visit Remixicon (https://remixicon.com/icon/) to browse available icons

2 .

Copy the icon name (e.g., `box-3-line`, `image-add-line`, `layout-grid-line`)

3 .

Use the name directly in your schema's parent `icon` field — do NOT include the `ri-` prefix

**Examples:**

Section with icon:

```
` {
"icon" : "image-add-line" ,
"name" : {
"ar" : "شرائح الصور" ,
"en" : "Image Slider"
} ,
"settings" : [
{
"id" : "hide_dots" ,
"label" : { "ar" : "إخفاء النقاط" , "en" : "Hide dots" } ,
"type" : "checkbox"
}
] ,
"template" : "sections/image_slider.jinja"
} `
```

The system automatically prepends `ri-` when rendering the icon in the theme editor.

## Section Preview Images #

Theme developers can upload desktop and mobile preview images for each section. These images are displayed in the Theme Editor when merchants browse sections to add, and beside each existing section in the sidebar.

**How it looks:**

### Naming Convention #

Based on the section file name (e.g., `slider.jinja`):

View File Name

Desktop `slider`

Mobile `slider_mobile`

**Supported formats:** `png`, `jpg`, `jpeg`

### File Location #

Place preview images in the same directory as your section template:

```
`sections/
├── slider.jinja
├── slider.png # Desktop preview
├── slider_mobile.png # Mobile preview
├── testimonials.jinja
├── testimonials.jpg # Desktop preview
├── testimonials_mobile.jpg # Mobile preview
└── ...`
```

### Behavior #

**Preview images are optional**: Sections work without them, but providing images improves the merchant experience.

**Responsive display**: The displayed preview image switches based on the frame selected in the top bar (desktop or mobile).

**Fallback**: If a mobile preview image is not provided, the desktop image is shown in mobile mode.

### Example #

For a section template `featured-products.jinja`:

```
`sections/
├── featured-products.jinja
├── featured-products.png # Shown when desktop frame is selected
└── featured-products_mobile.png # Shown when mobile frame is selected`
```

Modified at 2026-05-20 13:44:43

Previous

brand.jinja

Next

Input Settings
