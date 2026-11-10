---
# Synced from https://docs.zid.sa/availability-notifications-settings
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-availability-notifications-settings
title: "Noticiation Settings"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/availability-notifications-settings
tags: [from-docs-site, partner-docs]
language: en
---

> Noticiation Settings - Zid Docs
# Noticiation Settings

GET

https://api.zid.sa/ v1/products/notifications/settings/

Retrieve current settings for availability notifications.

🔑Scopes

`products.read` - Products Read

## Request

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
` curl --location --request GET 'https://api.zid.sa/v1/products/notifications/settings/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Store-Id: {{StoreId}}' \
--header 'Accept-Language: en' \
--header 'Content-Type: application/json' \
--data-raw '{
"email": "test@test.com",
"language": "ar"
}' `
```

Response Response Example

200 - Success

```
` {
"settings" : {
"delay_unit" : "hour" ,
"delay_value" : 15 ,
"email_text" : {
"ar" : "سيتم إرسال إشعار عند توفر المنتج" ,
"en" : "You will be notified when the product is available"
} ,
"email_title" : {
"ar" : "المنتج متوفر الآن" ,
"en" : "Product is now available"
} ,
"coupon_code" : null
}
} `
```

Modified at 2026-02-16 06:41:07

Previous

Notification Stats

Next

List Notifications
