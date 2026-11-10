---
# Synced from https://docs.zid.sa/manually-send-availability-notification-email
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-manually-send-availability-notification-email
title: "Send Notification Email"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/manually-send-availability-notification-email
tags: [from-docs-site, partner-docs]
language: en
---

> Send Notification Email - Zid Docs
# Send Notification Email

POST

https://api.zid.sa/ v1/products/notifications/send/

Manually send an availability notification email.

🔑Scopes

`products.read_write` - Products Read & Write

## Request

Header Params

###

Body Params multipart/form-data

###

## Responses

🟢 201 Notification email sent successfully.

This response does not have a body.

🟠 401 Unauthorized

🔴 500 Internal Server error

🟠 400 Bad Request

Request Request Example

Shell

JavaScript

Java

Swift

```
` curl --location 'https://api.zid.sa/v1/products/notifications/send/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Store-Id: {{StoreId}}' \
--header 'Accept-Language: en' \
--form 'email="test@example.com"' \
--form 'customer_name="Test Customer"' \
--form 'product_id="f9d2bfea-acf4-4251-b4ca-88edcd56d464"' \
--form 'method="email"' \
--form 'language="ar"' \
--form 'content="Hurry up and complete your order with Product \"X\""' \
--form 'title="Product is now available"' `
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

Modified at 2026-02-16 06:39:47

Previous

Update Settings

Next

Export Notifications
