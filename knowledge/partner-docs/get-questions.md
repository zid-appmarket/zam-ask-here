---
# Synced from https://docs.zid.sa/get-questions
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-get-questions
title: "Retrieve Product Question"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/get-questions
tags: [from-docs-site, partner-docs]
language: en
---

> Retrieve Product Question - Zid Docs
# Retrieve Product Question

GET

https://api.zid.sa/ v1/products/{product_id}/questions

Retrieve details of a specific question for a product.

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
` curl --location --request GET 'https://api.zid.sa/v1/products/399e381e-7c58-4148-aa26-7f959f4bf22b/questions' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Store-Id: {{StoreId}}' \
--header 'Accept-Language: en' \
--header 'Content-Type: application/json' \
--data-raw '{
"name": "\"Maira Anwar\"",
"email": "\"manager@zid.sa\"",
"question": "\"What do you think of me?\"",
"store": "\"aba1846c-c536-4c8a-9e1d-6b27ef1d240a\"",
"product": "\"e5715f91a23a4eeabcead3f75b2d939c\""
}' `
```

Response Response Example

200 - Success

```
` {
"count" : 1 ,
"next" : null ,
"previous" : null ,
"results" : [
{
"id" : "1ef1cc35-79e7-40b7-a9b2-989fd5895859" ,
"store" : "d297fb8b-c322-412e-a2f4-ffa96dc57022" ,
"product" : "399e381e-7c58-4148-aa26-7f959f4bf22b" ,
"product_name" : "apple" ,
"customer" : 143299 ,
"name" : "sara" ,
"email" : "sara.aljerasy@gmail.com" ,
"is_anonymous" : false ,
"is_owner" : false ,
"is_published" : true ,
"is_sent" : false ,
"is_new" : false ,
"question" : "التفاحه حمرا؟" ,
"created_at" : "2024-01-23T11:10:07.717021Z" ,
"answers" : [
{
"id" : "a4f54aa9-7d50-4c49-a114-709643d1d175" ,
"question" : "1ef1cc35-79e7-40b7-a9b2-989fd5895859" ,
"product" : "399e381e-7c58-4148-aa26-7f959f4bf22b" ,
"deleted" : null ,
"created_at" : "2024-01-23T11:11:35.288765Z" ,
"updated_at" : "2024-11-02T09:52:21.418915Z" ,
"answer" : "نعم، التفاحه حمراء" ,
"user" : "3"
}
]
}
]
} `
```

Modified at 2026-02-16 07:19:54

Previous

Product Questions & Answers

Next

Retrieve Product Answer
