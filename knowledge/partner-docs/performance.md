---
# Synced from https://docs.zid.sa/performance-1379358m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-performance
title: "Performance"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/performance-1379358m0
tags: [from-docs-site, partner-docs]
language: en
---

> Performance - Zid Docs
# Performance

Follow these tips to improve loading times and Core Web Vitals scores.

### `image_url` filter #

Use `image_url` to generate fast, responsive, modern images without changing your original assets.

📌

Use `image_url` to serve AVIF/WebP images, control quality, and generate multiple sizes on the fly.

### What it does #

The `image_url` filter is a macro built into the Vitrin theme SDK. It lets you:

1 .

Convert images to modern formats (AVIF / WebP) dynamically

2 .

Adjust image quality for faster downloads, especially on mobile

3 .

Generate different sizes for responsive layouts (`srcset`, etc.)

### Signature #

```
`image_url(path, w=None, h=None, q=None, f=None)`
```

**Parameters:**

**`path`** (required) – URL or path to the original image

**`w`** – Output width in pixels

**`h`** – Output height in pixels

**`q`** – Output quality from `0` to `100`

**`f`** – Output format. Use `'auto'` to let the client’s browser choose the best supported format (recommended)

### Basic usage #

```
`{{ image_url(ny_image, w=400, q=85, f='auto') }}`
```

This returns a URL to a 400px-wide, high-quality, auto-formatted image.

### Responsive `srcset` example #

```
``
```

The browser will automatically pick the most appropriate size for the user’s device and viewport.

1

Step 1 – Start simple

Replace hard-coded image URLs with `{{ image_url(...) }}` in your templates.

2

Step 2 – Tune quality

Use `q` (e.g. `q=70`) to balance visual quality and performance, especially for mobile.

3

Step 3 – Add responsiveness

Generate several widths and build a `srcset` so images stay sharp on all screen sizes.

### Preload Critical Assets #

Preloading key images can significantly improve your **Core Web Vitals**:

**First Contentful Paint (FCP)** — Preload the store logo so it appears as soon as possible.

**Largest Contentful Paint (LCP)** — Preload large banners or hero images to speed up main visual rendering.

Add the preload tags in your `<head>` section:

```
`<link rel="preload" as="image"
href="{{ image_url(logoUrl, h=175, q=100) }}"
media="(min-width: 992px)">

{% if logoUrlMobile %}
<link rel="preload" as="image"
href="{{ image_url(logoUrlMobile, h=175, q=100) }}"
media="(max-width: 991px)">
{% else %}
<link rel="preload" as="image"
href="{{ image_url(logoUrl, h=175, q=100) }}"
media="(max-width: 991px)">
{% endif %}`
```

The `media` attribute specifies the viewport size that triggers the preloading.

In the example above, we preload a different logo for desktop and mobile, with a fallback to the desktop logo if `logoUrlMobile` is not defined.

### Optimize Script Loading #

Use `async` for scripts that don’t require order.

```
``
```

Use `defer` for scripts that require order but should not block rendering:

```
``
```

### Image Optimization #

Use responsive images with `srcset` to serve the right size based on device:

```
``
```

Modified at 2026-07-30 11:49:13

Previous

CLI Commands

Next

Supporting both Vitrin and Legacy themes
