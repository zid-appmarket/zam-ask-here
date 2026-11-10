---
# Synced from https://docs.zid.sa/create-question
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-create-question
title: "Create Product Question"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/create-question
tags: [from-docs-site, partner-docs]
language: en
---

> Create Product Question - Zid Docs
# Create Product Question

POST

https://api.zid.sa/ v1/products/{product_id}/questions

Create a new question for a specified product.

🔑Scopes

`products.read_write` - Products Read & Write

## Request

Path Params

###

Header Params

###

Body Params multipart/form-data

###

## Responses

🟢 200 Question created successfully.

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
` curl --location 'https://api.zid.sa/v1/products/399e381e-7c58-4148-aa26-7f959f4bf22b/questions' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Store-Id: {{StoreId}}' \
--header 'Accept-Language: en' \
--header 'Role: manager' \
--form 'question="What' \ '' s the best option for this product? "' `
```

Response Response Example

200 - Example 1

```
` {
"id" : "\"cf2fc926-d179-4330-8fff-330853416aea\"," ,
"store" : "\"3dfc16e6-ad19-4126-9c2a-5e4a7fb73051\"" ,
"product" : "\"678c40b4-3989-4623-b4c2-61d29066e6ab\"" ,
"product_name" : "\"i phone\"" ,
"customer" : null ,
"name" : "\"anonymous customer\"" ,
"email" : "\"anon_customer@email.com\"" ,
"is_anonymous" : true ,
"is_owner" : false ,
"is_published" : false ,
"is_sent" : false ,
"is_new" : true ,
"question" : "\"What is ZID?\"" ,
"created_at" : "\"2024-07-12T06:28:34.765167Z\"" ,
"answers" : [
{ }
]
} `
```

Modified at 2026-02-16 07:31:02

Previous

List Answers for Question

Next

Create Product Answer
