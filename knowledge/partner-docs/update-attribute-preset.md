---
# Synced from https://docs.zid.sa/update-attribute-preset
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-update-attribute-preset
title: "Update Preset"
product: theme_market
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/update-attribute-preset
tags: [from-docs-site, partner-docs]
language: en
---

> Update Preset - Zid Docs
# Update Preset

PATCH

https://api.zid.sa/ v1/attributes/{Attribute-Id}/presets/{Preset-Id}/

Use this endpoint to update an existing attribute preset by specifying both the preset ID and the attribute ID. The request allows you to update the preset values in different languages.

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
` curl --location --request PATCH 'https://api.zid.sa/v1/attributes/cfb5bd3f-bbc5-4439-a171-b2d70e1c0293/presets/4469e2f3-20b5-438b-893d-a22e61d55b7b/' \
--header 'X-Manager-Token: {{Access-Token}}' \
--header 'Store-Id: {{StoreId}}' \
--header 'Content-Type: application/json' \
--data '{
"value": {
"ar": "Size Size",
"en": "Size Size"
}
}' `
```

Response Response Example

200 - Success

```
` {
"id" : "4469e2f3-20b5-438b-893d-a22e61d55b7b" ,
"slug" : "color-6" ,
"name" : "" ,
"value" : "Size Size" ,
"type" : "default" ,
"type_value" : null ,
"display_order" : null ,
"attribute_image_id" : null ,
"attribute_id" : "cfb5bd3f-bbc5-4439-a171-b2d70e1c0293"
} `
```

Modified at 2026-02-15 15:53:31

Previous

Create Preset

Next

Delete Preset
