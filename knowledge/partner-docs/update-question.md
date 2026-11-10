---
# Synced from https://docs.zid.sa/update-question
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-update-question
title: "Update Product Question"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/update-question
tags: [from-docs-site, partner-docs]
language: en
---

> Update Product Question - Zid Docs
# Update Product Question

PATCH

https://api.zid.sa/ v1/products/{product_id}/questions/{question_id}

Update details of a specific question for a product.

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

🟢 200 Question updated successfully.

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
` curl --location --request PATCH 'https://api.zid.sa/v1/products/399e381e-7c58-4148-aa26-7f959f4bf22b/questions/1ef1cc35-79e7-40b7-a9b2-989fd5895859' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Store-Id: {{StoreId}}' \
--header 'Role: Manager' \
--header 'Accept-Language: en' \
--header 'Content-Type: application/json' \
--data '{
"question": "test",
"is_published": false
}' `
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

Modified at 2026-02-16 07:41:08

Previous

Create Product Answer

Next

Update Product Answer
