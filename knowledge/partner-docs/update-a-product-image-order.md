---
# Synced from https://docs.zid.sa/update-a-product-image-order
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-update-a-product-image-order
title: "Update Image Order"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/update-a-product-image-order
tags: [from-docs-site, partner-docs]
language: en
---

> Update Image Order - Zid Docs
# Update Image Order

PATCH

https://api.zid.sa/ v1/products/{product_id}/images/{Image-Id}/

use this endpoint to reorder an image's appearance for a product.

🔑Scopes

`products.read_write` - Products Read & Write

## Request

Path Params

###

Header Params

###

Body Params application/json

###

Examples

## Responses

🟢 200 OK

application/json

Body application/json

###

🟠 401 Unauthorized

🔴 500 Internal Server error

Request Request Example

Shell

JavaScript

Java

Swift

```
` curl --location --request PATCH 'https://api.zid.sa/v1/products/96d0f5c3-1958-4a31-8b03-7014c2070630/images/0bcc247a-61fa-4a95-bab1-21827a824749/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Store-Id: {{StoreId}}' \
--header 'Accept-Language: en' \
--header 'Content-Type: application/json' \
--data '{
"display_order": 3
}' `
```

Response Response Example

200 - Success

```
` {
"id" : "0bcc247a-61fa-4a95-bab1-21827a824749" ,
"image" : {
"large" : "https://media.zid.store/thumbs/d297fb8b-c322-412e-a2f4-ffa96dc57022/0bcc247a-61fa-4a95-bab1-21827a824749-thumbnail-1000x1000-70.jpg" ,
"small" : "https://media.zid.store/thumbs/d297fb8b-c322-412e-a2f4-ffa96dc57022/0bcc247a-61fa-4a95-bab1-21827a824749-thumbnail-500x500-70.jpg" ,
"full_size" : "https://media.zid.store/d297fb8b-c322-412e-a2f4-ffa96dc57022/0bcc247a-61fa-4a95-bab1-21827a824749.jpg" ,
"medium" : "https://media.zid.store/thumbs/d297fb8b-c322-412e-a2f4-ffa96dc57022/0bcc247a-61fa-4a95-bab1-21827a824749-thumbnail-770x770-70.jpg" ,
"thumbnail" : "https://media.zid.store/thumbs/d297fb8b-c322-412e-a2f4-ffa96dc57022/0bcc247a-61fa-4a95-bab1-21827a824749-thumbnail-370x370-70.jpg"
} ,
"alt_text" : null ,
"display_order" : 3
} `
```

Modified at 2026-02-16 06:27:38

Previous

Upload Image

Next

Delete Image
