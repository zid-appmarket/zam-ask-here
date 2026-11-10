---
# Synced from https://docs.zid.sa/publish/unpublish-a-category
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-publish-unpublish-a-category
title: "Publish Category"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/publish/unpublish-a-category
tags: [from-docs-site, partner-docs]
language: en
---

> Publish Category - Zid Docs
# Publish Category

PUT

https://api.zid.sa/ v1/managers/store/categories/{category_id}/publishing

Use this endpoint to either publish or unpublish a certain category.

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
` curl --location --request PUT 'https://api.zid.sa/v1/managers/store/categories/1486524/publishing' \
--header 'Authorization: {{Autherization}}' \
--header 'X-Manager-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
"is_published": "string"
}' `
```

Response Response Example

200 - Success

```
` {
"status" : "success" ,
"message" : {
"type" : "success" ,
"code" : "" ,
"name" : "" ,
"description" : "ok"
}
} `
```

Modified at 2026-08-11 09:20:52

Previous

Bulk Assign Products to Category

Next

Detach Category from All Products
