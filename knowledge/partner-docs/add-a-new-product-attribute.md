---
# Synced from https://docs.zid.sa/add-a-new-product-attribute
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-add-a-new-product-attribute
title: "Create Attribute"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/add-a-new-product-attribute
tags: [from-docs-site, partner-docs]
language: en
---

> Create Attribute - Zid Docs
# Create Attribute

POST

https://api.zid.sa/ v1/attributes/

Add new product attributes for a certain Role.

🔑Scopes

`products.read_write` - Products Read & Write

## Request

Header Params

###

Body Params application/json

###

Examples

## Responses

🟢 201 Created

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
` curl --location 'https://api.zid.sa/v1/attributes/' \
--header 'Authorization: {{Autherization}}' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Store-Id: {{StoreId}}' \
--header 'Accept-Language: en' \
--header 'Content-Type: application/json' \
--data '{
"name": "Weight",
"slug": "weight",
"is_extra": false,
"is_enabled": true,
"display_order": null
}' `
```

Response Response Example

201 - Success

```
` {
"id" : "6f637324-a016-4389-a397-44233a13692c" ,
"name" : "Weight" ,
"slug" : "weight" ,
"presets" : [ ] ,
"is_extra" : false ,
"is_enabled" : true ,
"display_order" : null ,
"preset_count" : null
} `
```

Modified at 2026-02-15 15:52:52

Previous

View Attribute

Next

Update Attribute
