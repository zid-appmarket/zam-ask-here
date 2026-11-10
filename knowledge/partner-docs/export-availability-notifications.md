---
# Synced from https://docs.zid.sa/export-availability-notifications
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-export-availability-notifications
title: "Export Notifications"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/export-availability-notifications
tags: [from-docs-site, partner-docs]
language: en
---

> Export Notifications - Zid Docs
# Export Notifications

POST

https://api.zid.sa/ v1/products/notifications/export/

Export availability notifications data.

🔑Scopes

`products.read_write` - Products Read & Write

## Request

Header Params

###

Body Params multipart/form-data

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
` curl --location 'https://api.zid.sa/v1/products/notifications/export/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Store-Id: {{StoreId}}' \
--header 'Accept-Language: en' \
--form 'email="merchant@store.come"' \
--form 'is_notified="true"' `
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

Modified at 2026-02-16 06:39:29

Previous

Send Notification Email

Next

Product Export
