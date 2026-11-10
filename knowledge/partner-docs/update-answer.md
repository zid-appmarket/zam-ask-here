---
# Synced from https://docs.zid.sa/update-answer
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-update-answer
title: "Update Product Answer"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/update-answer
tags: [from-docs-site, partner-docs]
language: en
---

> Update Product Answer - Zid Docs
# Update Product Answer

PATCH

https://api.zid.sa/ v1/products/{product_id}/questions/{question_id}/answers/{answer_id}

Update details of a specific answer to a question.

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

🟢 200 Answer updated successfully.

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
` curl --location --request PATCH 'https://api.zid.sa/v1/products/399e381e-7c58-4148-aa26-7f959f4bf22b/questions/1ef1cc35-79e7-40b7-a9b2-989fd5895859/answers/a4f54aa9-7d50-4c49-a114-709643d1d175' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Store-Id: {{StoreId}}' \
--header 'Role: Manager' \
--header 'Accept-Language: en' \
--header 'Content-Type: application/json' \
--data '{
"answer": "\"New answer\""
}' `
```

Response Response Example

200 - Example 1

```
` {
"id" : "\"b5e1cdea-1e9f-4bcd-ae33-21c70b5d715e\"" ,
"question_id" : "\"cf2fc926-d179-4330-8fff-330853416aea\"" ,
"answer" : "\"Updated answer content.\"" ,
"created_at" : "\"2024-07-12T07:00:00.000000Z\""
} `
```

Modified at 2026-02-16 08:10:54

Previous

Update Product Question

Next

Delete Product Question
