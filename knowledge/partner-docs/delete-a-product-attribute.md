---
# Synced from https://docs.zid.sa/delete-a-product-attribute
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-delete-a-product-attribute
title: "Delete Attribute"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/delete-a-product-attribute
tags: [from-docs-site, partner-docs]
language: en
---

> Delete Attribute - Zid Docs
# Delete Attribute

DELETE

https://api.zid.sa/ v1/attributes/{Attribute-Id}/

Delete a certain ID using its id.

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

🔴 500 Internal Server error

Request Request Example

Shell

JavaScript

Java

Swift

```
` curl --location --request DELETE 'https://api.zid.sa/v1/attributes/1f258e6a-4433-46f0-aa8a-3bc987839b69/' \
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

Modified at 2026-02-15 15:53:06

Previous

Update Attribute

Next

Product Attribute Presets
