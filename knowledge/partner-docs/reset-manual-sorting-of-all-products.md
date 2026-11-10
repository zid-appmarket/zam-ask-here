---
# Synced from https://docs.zid.sa/reset-manual-sorting-of-all-products
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-reset-manual-sorting-of-all-products
title: "Reset Manual Product Order"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/reset-manual-sorting-of-all-products
tags: [from-docs-site, partner-docs]
language: en
---

> Reset Manual Product Order - Zid Docs
# Reset Manual Product Order

DELETE

https://api.zid.sa/ v1/products/ordering/

Delete any manual sorting that was done on any of the store products.

🔑Scopes

`products.read_write` - Products Read & Write

## Request

Header Params

###

## Responses

🟢 204 No Content

This response does not have a body.

🟠 401 Unauthorized

🔴 500 Internal Server error

Request Request Example

Shell

JavaScript

Java

Swift

```
` curl --location --request DELETE 'https://api.zid.sa/v1/products/ordering/' \
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

Modified at 2026-02-15 16:15:24

Previous

Set Manual Product Order

Next

Product Images
