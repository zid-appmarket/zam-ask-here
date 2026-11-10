---
# Synced from https://docs.zid.sa/delete-question
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-delete-question
title: "Delete Product Question"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/delete-question
tags: [from-docs-site, partner-docs]
language: en
---

> Delete Product Question - Zid Docs
# Delete Product Question

DELETE

https://api.zid.sa/ v1/products/{question_id}/questions/{question_id}

Delete a specific question for a product.

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

🟢 200 Question deleted successfully.

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
` curl --location --request DELETE 'https://api.zid.sa/v1/products//questions/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Store-Id: {{StoreId}}' \
--header 'Role: Manager' \
--header 'Accept-Language: en' \
--header 'Content-Type: application/json' \
--data-raw '{
"name": "\"Authed Manager\"",
"email": "\"manager@zid.sa",
"question": "\"What do you think of me?\"",
"store": "\"aba1846c-c536-4c8a-9e1d-6b27ef1d240a\"",
"product": "\"e5715f91a23a4eeabcead3f75b2d939c\""
}' `
```

Response Response Example

200 - Example 1

```
` {
"message" : "\"Question deleted successfully.\""
} `
```

Modified at 2026-02-16 08:08:49

Previous

Update Product Answer

Next

Delete Product Answer
