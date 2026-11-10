---
# Synced from https://docs.zid.sa/email-all-products-to-store-owner
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-email-all-products-to-store-owner
title: "Email All Products to Store Owner"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/email-all-products-to-store-owner
tags: [from-docs-site, partner-docs]
language: en
---

> Email All Products to Store Owner - Zid Docs
# Email All Products to Store Owner

POST

https://api.zid.sa/ v1/products/export/

Sends an email to the store owner containing all the store's products in CSV format.

🔑Scopes

`products.read_write` - Products Read & Write

### **Note** #

The export flow is being updated for the New Dashboard.

For merchants using the **Current Dashboard**, exported files are still sent via email.

For merchants using the **New Dashboard**, you will instead receive a confirmation when the export is ready, and the file can be downloaded from: `Settings → Export Requests`.

Example URL: `/en-sa/stores/{store_id}/settings/export-requests`

## Request

Header Params

###

## Responses

🟢 204 Products list is sent to the owner's Email

This response does not have a body.

🟠 401 Unauthorized

🔴 500 Internal Server error

Request Request Example

Shell

JavaScript

Java

Swift

```
` curl --location --request POST 'https://api.zid.sa/v1/products/export/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Store-Id: {{StoreId}}' \
--header 'Accept-Language: en' `
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

Modified at 2026-02-16 06:34:43

Previous

Product Export

Next

Import Products via CSV or xlsx File
