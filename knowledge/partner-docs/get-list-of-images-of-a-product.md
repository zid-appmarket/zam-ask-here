---
# Synced from https://docs.zid.sa/get-list-of-images-of-a-product
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-get-list-of-images-of-a-product
title: "List Images"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/get-list-of-images-of-a-product
tags: [from-docs-site, partner-docs]
language: en
---

> List Images - Zid Docs
# List Images

GET

https://api.zid.sa/ v1/products/{product_id}/images/

Retrieve a list with all images available for a certain product using product id.

🔑Scopes

`products.read` - Products Read

## Request

Path Params

###

Query Params

###

Header Params

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
` curl --location 'https://api.zid.sa/v1/products/96d0f5c3-1958-4a31-8b03-7014c2070630/images/?page_size=15&Page=1' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Store-Id: {{StoreId}}' \
--header 'Accept-Language: en' `
```

Response Response Example

200 - Success

```
` {
"next" : null ,
"previous" : null ,
"count" : 1 ,
"results" : [
{
"id" : "0bcc247a-61fa-4a95-bab1-21827a824749" ,
"image" : {
"large" : "https://media.zid.store/thumbs/d297fb8b-c322-412e-a2f4-ffa96dc57022/0bcc247a-61fa-4a95-bab1-21827a824749-thumbnail-1000x1000-70.jpg" ,
"medium" : "https://media.zid.store/thumbs/d297fb8b-c322-412e-a2f4-ffa96dc57022/0bcc247a-61fa-4a95-bab1-21827a824749-thumbnail-770x770-70.jpg" ,
"small" : "https://media.zid.store/thumbs/d297fb8b-c322-412e-a2f4-ffa96dc57022/0bcc247a-61fa-4a95-bab1-21827a824749-thumbnail-500x500-70.jpg" ,
"full_size" : "https://media.zid.store/d297fb8b-c322-412e-a2f4-ffa96dc57022/0bcc247a-61fa-4a95-bab1-21827a824749.jpg" ,
"thumbnail" : "https://media.zid.store/thumbs/d297fb8b-c322-412e-a2f4-ffa96dc57022/0bcc247a-61fa-4a95-bab1-21827a824749-thumbnail-370x370-70.jpg"
} ,
"alt_text" : null ,
"display_order" : 1
}
] ,
"filters" : { }
} `
```

Modified at 2026-02-15 16:20:32

Previous

Product Images

Next

Upload Image
