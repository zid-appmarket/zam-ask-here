---
# Synced from https://docs.zid.sa/availability-notification-stats
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-availability-notification-stats
title: "Notification Stats"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/availability-notification-stats
tags: [from-docs-site, partner-docs]
language: en
---

> Notification Stats - Zid Docs
# Notification Stats

GET

https://api.zid.sa/ v1/products/notifications/stats/

Retrieve statistics on availability notifications.

🔑Scopes

`products.read` - Products Read

## Request

Header Params

###

Body Params multipart/form-data

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
` curl --location --request GET 'https://api.zid.sa/v1/products/notifications/stats/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Store-Id: {{StoreId}}' \
--header 'Accept-Language: en' \
--form 'email="test@test.com"' \
--form 'language="ar"' `
```

Response Response Example

200 - Success

```
` {
"total_count" : 1 ,
"notified_count" : 0 ,
"purchased_count" : 0 ,
"purchased_total" : 0
} `
```

Modified at 2026-02-16 06:41:22

Previous

Product Availability Notifications

Next

Noticiation Settings
