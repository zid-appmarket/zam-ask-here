---
# Synced from https://docs.zid.sa/new-reviews-total
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-new-reviews-total
title: "Count Reviews"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/new-reviews-total
tags: [from-docs-site, partner-docs]
language: en
---

> Count Reviews - Zid Docs
# Count Reviews

GET

https://api.zid.sa/ v1/managers/store/reviews/count/{status}

This API endpoint retrieves the total number of new reviews. It allows you to filter the results based on specific query parameters like search terms, date ranges, or customer IDs.

🔑Scopes

`products.read` - Products Read

## Request

Path Params

###

Header Params

###

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
` curl --location 'https://api.zid.sa/v1/managers/store/reviews/count/approved' \
--header 'Authorization: {{Autherization}}' \
--header 'X-Manager-Token: {{Access-Token}}' \
--header 'Accept: application/json' \
--header 'Accept-Language: ar' `
```

Response Response Example

200 - Success

```
` {
"status" : "object" ,
"count" : 45 ,
"message" : {
"type" : "object" ,
"code" : null ,
"name" : null ,
"description" : null
}
} `
```

Modified at 2026-02-08 14:46:59

Previous

List Reviews

Next

Digital Products
