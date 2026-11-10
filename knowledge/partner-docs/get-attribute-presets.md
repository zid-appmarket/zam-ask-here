---
# Synced from https://docs.zid.sa/get-attribute-presets
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-get-attribute-presets
title: "List Presets"
product: theme_market
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/get-attribute-presets
tags: [from-docs-site, partner-docs]
language: en
---

> List Presets - Zid Docs
# List Presets

GET

https://api.zid.sa/ v1/attributes/{Attribute-Id}/presets/

This endpoint retrieves all attribute presets, allowing users to quickly and easily add attributes in a specified language. It provides a list of available presets, each containing attribute values in both Arabic and English.

🔑Scopes

`products.read` - Products Read

## Request

Path Params

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
` curl --location 'https://api.zid.sa/v1/attributes/cfb5bd3f-bbc5-4439-a171-b2d70e1c0293/presets/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Store-Id: {{StoreId}}' \
--header 'Accept-Language: en' `
```

Response Response Example

200 - Success

```
` {
"count" : 3 ,
"next" : null ,
"previous" : null ,
"results" : [
{
"id" : "1f4956ea-e19c-4de9-8c75-7e12b5e4aee8" ,
"slug" : "color-6" ,
"name" : "" ,
"value" : "color" ,
"type" : "default" ,
"type_value" : null ,
"display_order" : null ,
"attribute_image_id" : null ,
"attribute_id" : "cfb5bd3f-bbc5-4439-a171-b2d70e1c0293"
} ,
{
"id" : "4620a7e7-c4e3-4402-9c07-f08aab29a4dd" ,
"slug" : "color-6" ,
"name" : "" ,
"value" : "color" ,
"type" : "default" ,
"type_value" : null ,
"display_order" : null ,
"attribute_image_id" : null ,
"attribute_id" : "cfb5bd3f-bbc5-4439-a171-b2d70e1c0293"
} ,
{
"id" : "f56e7d74-290e-45a5-8057-f0c8b868aaee" ,
"slug" : "color-6" ,
"name" : "" ,
"value" : "color" ,
"type" : "default" ,
"type_value" : null ,
"display_order" : null ,
"attribute_image_id" : null ,
"attribute_id" : "cfb5bd3f-bbc5-4439-a171-b2d70e1c0293"
}
]
} `
```

Modified at 2026-02-15 15:53:19

Previous

Product Attribute Presets

Next

Create Preset
