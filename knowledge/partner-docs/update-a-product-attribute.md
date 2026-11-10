---
# Synced from https://docs.zid.sa/update-a-product-attribute
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-update-a-product-attribute
title: "Update Attribute"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/update-a-product-attribute
tags: [from-docs-site, partner-docs]
language: en
---

> Update Attribute - Zid Docs
# Update Attribute

PATCH

https://api.zid.sa/ v1/attributes/{Attribute-Id}/

Use to update the value of a single attribute for a certain Role.

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
` curl --location --request PATCH 'https://api.zid.sa/v1/attributes/6f637324-a016-4389-a397-44233a13692c/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Store-Id: {{StoreId}}' \
--header 'Accept-Language: en' \
--header 'Content-Type: application/json' \
--data '{
"name": "Weight 2",
"slug": "weight_2",
"is_extra": true,
"is_enabled": false,
"display_order": 1
}' `
```

Response Response Example

200 - Success

```
` {
"id" : "6f637324-a016-4389-a397-44233a13692c" ,
"name" : "Weight 2" ,
"slug" : "weight" ,
"presets" : [ ] ,
"is_extra" : true ,
"is_enabled" : false ,
"display_order" : 1 ,
"preset_count" : null
} `
```

Modified at 2026-02-15 15:53:00

Previous

Create Attribute

Next

Delete Attribute
