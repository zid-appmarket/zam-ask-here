---
# Synced from https://docs.zid.sa/create-attribute-preset
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-create-attribute-preset
title: "Create Preset"
product: theme_market
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/create-attribute-preset
tags: [from-docs-site, partner-docs]
language: en
---

> Create Preset - Zid Docs
# Create Preset

POST

https://api.zid.sa/ v1/attributes/{Attribute-Id}/presets/

Use this endpoint to add a new attribute preset, allowing for quick and easy creation of attributes with localized values in both Arabic and English.

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
` curl --location 'https://api.zid.sa/v1/attributes/cfb5bd3f-bbc5-4439-a171-b2d70e1c0293/presets/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Store-Id: {{StoreId}}' \
--header 'Content-Type: application/json' \
--data '{
"value": {
"ar": "اللون",
"en": "color"
}
}' `
```

Response Response Example

201 - Success

```
` {
"id" : "4469e2f3-20b5-438b-893d-a22e61d55b7b" ,
"slug" : "color-6" ,
"name" : "" ,
"value" : "color" ,
"type" : "default" ,
"type_value" : null ,
"display_order" : null ,
"attribute_image_id" : null ,
"attribute_id" : "cfb5bd3f-bbc5-4439-a171-b2d70e1c0293"
} `
```

Modified at 2026-02-15 15:53:25

Previous

List Presets

Next

Update Preset
