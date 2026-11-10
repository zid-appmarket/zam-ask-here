---
# Synced from https://docs.zid.sa/get-answer
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-get-answer
title: "Retrieve Product Answer"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/get-answer
tags: [from-docs-site, partner-docs]
language: en
---

> Retrieve Product Answer - Zid Docs
# Retrieve Product Answer

GET

https://api.zid.sa/ v1/products/{product_id}/questions/{question_id}/answers

Retrieve details of a specific answer to a question.

🔑Scopes

`products.read` - Products Read

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
` curl --location --request GET 'https://api.zid.sa/v1/products/399e381e-7c58-4148-aa26-7f959f4bf22b/questions/1ef1cc35-79e7-40b7-a9b2-989fd5895859/answers' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Store-Id: {{StoreId}}' \
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
"count" : 0 ,
"next" : "string" ,
"previous" : "string" ,
"results" : [
{
"id" : "string" ,
"question" : "string" ,
"product" : "string" ,
"deleted" : "string" ,
"created_at" : "string" ,
"updated_at" : "string" ,
"answer" : "string" ,
"user" : "string"
}
]
} `
```

Modified at 2026-02-16 07:23:47

Previous

Retrieve Product Question

Next

List Product Questions
