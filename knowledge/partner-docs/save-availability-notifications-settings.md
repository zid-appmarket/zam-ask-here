---
# Synced from https://docs.zid.sa/save-availability-notifications-settings
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-save-availability-notifications-settings
title: "Update Settings"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/save-availability-notifications-settings
tags: [from-docs-site, partner-docs]
language: en
---

> Update Settings - Zid Docs
# Update Settings

POST

https://api.zid.sa/ v1/products/notifications/settings/

Save settings for availability notifications.

🔑Scopes

`products.read_write` - Products Read & Write

## Request

Header Params

###

Body Params application/json

###

Examples

## Responses

🟢 201 Created

This response does not have a body.

🟠 401 Unauthorized

🔴 500 Internal Server error

Request Request Example

Shell

JavaScript

Java

Swift

```
` curl --location 'https://api.zid.sa/v1/products/notifications/settings/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Store-Id: {{StoreId}}' \
--header 'Accept-Language: en' \
--header 'Content-Type: application/json' \
--data '{
"delay_unit": "hour",
"delay_value": 15,
"email_text": {
"ar": "سيتم إرسال إشعار عند توفر المنتج",
"en": "You will be notified when the product is available"
},
"email_title": {
"ar": "المنتج متوفر الآن",
"en": "Product is now available"
},
"coupon_code": null
}' `
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

Modified at 2026-02-16 06:40:04

Previous

Create Notification

Next

Send Notification Email
