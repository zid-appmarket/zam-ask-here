---
# Synced from https://docs.zid.sa/delete-answer
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-delete-answer
title: "Delete Product Answer"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/delete-answer
tags: [from-docs-site, partner-docs]
language: en
---

> Delete Product Answer - Zid Docs
# Delete Product Answer

DELETE

https://api.zid.sa/ v1/products/{product_id}/questions{question_id}/answers/{answer_id}

Delete a specific answer for a question.

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

🟢 200 Answer deleted successfully.

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
` curl --location --request DELETE 'https://api.zid.sa/v1/products/399e381e-7c58-4148-aa26-7f959f4bf22b/questions1ef1cc35-79e7-40b7-a9b2-989fd5895859/answers/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Store-Id: {{StoreId}}' \
--header 'Role: Manager' \
--header 'Accept-Language: en' \
--header 'Content-Type: application/json' \
--data '{
"question": "\"14dbaf07-b257-4ab2-b277-310f14e95672\"",
"answer": "\"Yup, this product has batteries included.\"",
"user": 6
}' `
```

Response Response Example

200 - Example 1

```
` {
"message" : "\"Answer deleted successfully.\""
} `
```

Modified at 2026-02-16 08:11:56

Previous

Delete Product Question

Next

List Store Product Questions
