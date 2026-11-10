---
# Synced from https://docs.zid.sa/delete-a-product-image
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-delete-a-product-image
title: "Delete Image"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/delete-a-product-image
tags: [from-docs-site, partner-docs]
language: en
---

> Delete Image - Zid Docs
# Delete Image

DELETE

https://api.zid.sa/ v1/products/{product_id}/images/{Image-Id}/

Delete a specific product image by using the image id and product id.

🔑Scopes

`products.read_write` - Products Read & Write

## Request

Path Params

###

Header Params

###

## Responses

🟢 204 No Content

This response does not have a body.

🟠 401 Unauthorized

🟠 404 Not Found

🔴 500 Internal Server error

Request Request Example

Shell

JavaScript

Java

Swift

```
` curl --location --request DELETE 'https://api.zid.sa/v1/products/96d0f5c3-1958-4a31-8b03-7014c2070630/images/0bcc247a-61fa-4a95-bab1-21827a824749/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Store-Id: {{StoreId}}' \
--header 'Accept-Language: en' `
```

Response Response Example

401 - Example 1

```
` {
"status" : "error" ,
"message" : {
"type" : "error" ,
"code" : "ERROR_SESSION_MISSING" ,
"name" : "Sorry" ,
"description" : "Please login first."
}
} `
```

Modified at 2026-02-16 06:28:41

Previous

Update Image Order

Next

Product Availability Notifications
