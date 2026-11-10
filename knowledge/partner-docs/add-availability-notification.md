---
# Synced from https://docs.zid.sa/add-availability-notification
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-add-availability-notification
title: "Create Notification"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/add-availability-notification
tags: [from-docs-site, partner-docs]
language: en
---

> Create Notification - Zid Docs
# Create Notification

POST

https://api.zid.sa/ v1/products/{product_id}/notifications/

Sign up to receive a notification by email when the specified product becomes available again in the store.

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

🟢 201 Created

This response does not have a body.

🟠 404 Not Found

🟠 401 Unauthorized

🔴 500 Internal Server error

Request Request Example

Shell

JavaScript

Java

Swift

```
` curl --location 'https://api.zid.sa/v1/products/a7ad89d0-03e2-430f-b6e4-0624ef05e571/notifications/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Store-Id: {{StoreId}}' \
--header 'Accept-Language: en' \
--form 'email="example@test.com"' \
--form 'language="ar"' \
--form 'name="Test Customer"' \
--form 'phone="+966500000005"' \
--form 'customer_id="15141670"' \
--form 'customer_phone_number="+966500000005"' \
--form 'customer_name="Test Customer"' `
```

Response Response Example

404 - Exception

```
` {
"email" : [
"This field is required."
]
} `
```

Modified at 2026-02-16 06:40:20

Previous

List Notifications

Next

Update Settings
