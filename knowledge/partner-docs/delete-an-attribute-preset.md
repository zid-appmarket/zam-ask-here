---
# Synced from https://docs.zid.sa/delete-an-attribute-preset
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-delete-an-attribute-preset
title: "Delete Preset"
product: theme_market
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/delete-an-attribute-preset
tags: [from-docs-site, partner-docs]
language: en
---

> Delete Preset - Zid Docs
# Delete Preset

DELETE

https://api.zid.sa/ v1/attributes/{Attribute-Id}/presets/{Preset-Id}/

Delete a defined attribute preset.

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

🟠 404 Not Found

Request Request Example

Shell

JavaScript

Java

Swift

```
` curl --location --request DELETE 'https://api.zid.sa/v1/attributes/cfb5bd3f-bbc5-4439-a171-b2d70e1c0293/presets/4469e2f3-20b5-438b-893d-a22e61d55b7b/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Store-Id: {{StoreId}}' `
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

Modified at 2026-02-15 15:53:37

Previous

Update Preset

Next

Product Variants
