---
# Synced from https://docs.zid.sa/retrieve-a-product-attribute
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-retrieve-a-product-attribute
title: "View Attribute"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/retrieve-a-product-attribute
tags: [from-docs-site, partner-docs]
language: en
---

> View Attribute - Zid Docs
# View Attribute

GET

https://api.zid.sa/ v1/attributes/{Attribute-Id}/

Use this endpoint to retrieve a specific product attribute using its id.

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
` curl --location 'https://api.zid.sa/v1/attributes/cfb5bd3f-bbc5-4439-a171-b2d70e1c0293/' \
--header 'Authorization: {{Autherization}}' \
--header 'X-Manager-Token: {{Access-Token}}' \
--header 'Store-Id: {{StoreId}}' \
--header 'Accept-Language: en' `
```

Response Response Example

200 - Success

```
` {
"id" : "cfb5bd3f-bbc5-4439-a171-b2d70e1c0293" ,
"name" : "" ,
"slug" : "color-6" ,
"presets" : [
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
] ,
"is_extra" : false ,
"is_enabled" : true ,
"display_order" : null ,
"preset_count" : 3
} `
```

Modified at 2026-02-15 15:52:46

Previous

List Attributes

Next

Create Attribute
