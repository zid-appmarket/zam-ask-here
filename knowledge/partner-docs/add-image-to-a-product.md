---
# Synced from https://docs.zid.sa/add-image-to-a-product
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-add-image-to-a-product
title: "Upload Image"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/add-image-to-a-product
tags: [from-docs-site, partner-docs]
language: en
---

> Upload Image - Zid Docs
# Upload Image

POST

https://api.zid.sa/ v1/products/{product_id}/images/

Use this endpoint to add a single image to a product.

🔑Scopes

`products.read_write` - Products Read & Write

## Request

Path Params

###

Header Params

###

Body Params multipart/form-data

###

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
` curl --location 'https://api.zid.sa/v1/products/96d0f5c3-1958-4a31-8b03-7014c2070630/images/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Store-Id: {{StoreId}}' \
--header 'Accept-Language: en' \
--form 'image=@"cmMtdXBsb2FkLTE3NzExNjEzNzY5MTQtMg==/test1.jpg"' \
--form 'alt_text="test alt text"' `
```

Response Response Example

200 - Success

```
` {
"id" : "59b5fff2-2281-44a4-8bf1-56d9fd1165bb" ,
"image" : {
"full_size" : "https://media.zid.store/d297fb8b-c322-412e-a2f4-ffa96dc57022/59b5fff2-2281-44a4-8bf1-56d9fd1165bb.jpg" ,
"medium" : "https://media.zid.store/thumbs/d297fb8b-c322-412e-a2f4-ffa96dc57022/59b5fff2-2281-44a4-8bf1-56d9fd1165bb-thumbnail-770x770-70.jpg" ,
"large" : "https://media.zid.store/thumbs/d297fb8b-c322-412e-a2f4-ffa96dc57022/59b5fff2-2281-44a4-8bf1-56d9fd1165bb-thumbnail-1000x1000-70.jpg" ,
"small" : "https://media.zid.store/thumbs/d297fb8b-c322-412e-a2f4-ffa96dc57022/59b5fff2-2281-44a4-8bf1-56d9fd1165bb-thumbnail-500x500-70.jpg" ,
"thumbnail" : "https://media.zid.store/thumbs/d297fb8b-c322-412e-a2f4-ffa96dc57022/59b5fff2-2281-44a4-8bf1-56d9fd1165bb-thumbnail-370x370-70.jpg"
} ,
"alt_text" : "test alt text" ,
"display_order" : 2
} `
```

Modified at 2026-02-16 06:18:27

Previous

List Images

Next

Update Image Order
