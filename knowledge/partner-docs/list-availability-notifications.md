---
# Synced from https://docs.zid.sa/list-availability-notifications
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-list-availability-notifications
title: "List Notifications"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/list-availability-notifications
tags: [from-docs-site, partner-docs]
language: en
---

> List Notifications - Zid Docs
# List Notifications

GET

https://api.zid.sa/ v1/products/notifications/

Retrieve a list of availability notifications.

🔑Scopes

`products.read` - Products Read

## Request

Query Params

###

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
` curl --location --request GET 'https://api.zid.sa/v1/products/notifications/?q=undefined&product_id=undefined&created_at__gte=undefined&created_at__lte=undefined&page=1&page_size=15' \
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
"count" : 1 ,
"next" : null ,
"previous" : null ,
"results" : [
{
"id" : "0d8f7dc9-423d-4e54-ab47-6c170f4c0d84" ,
"product_id" : "a7ad89d0-03e2-430f-b6e4-0624ef05e571" ,
"product_name" : {
"ar" : "لوحة" ,
"en" : "voucher-no1 & small size "
} ,
"customer" : {
"id" : 1 ,
"name" : "مازن الضراب" ,
"email" : "test@test.com" ,
"phone_number" : "+966501234567"
} ,
"language" : "ar" ,
"is_notified" : false ,
"image" : {
"full_size" : "https://media.zid.store/d297fb8b-c322-412e-a2f4-ffa96dc57022/52e4613d-6576-484d-b6f1-f43f8bc20b88.png" ,
"thumbnail" : "https://media.zid.store/thumbs/d297fb8b-c322-412e-a2f4-ffa96dc57022/52e4613d-6576-484d-b6f1-f43f8bc20b88-thumbnail-370x370.png" ,
"large" : "https://media.zid.store/thumbs/d297fb8b-c322-412e-a2f4-ffa96dc57022/52e4613d-6576-484d-b6f1-f43f8bc20b88-thumbnail-1000x1000.png" ,
"medium" : "https://media.zid.store/thumbs/d297fb8b-c322-412e-a2f4-ffa96dc57022/52e4613d-6576-484d-b6f1-f43f8bc20b88-thumbnail-770x770.png" ,
"small" : "https://media.zid.store/thumbs/d297fb8b-c322-412e-a2f4-ffa96dc57022/52e4613d-6576-484d-b6f1-f43f8bc20b88-thumbnail-500x500.png"
} ,
"created_at" : "2026-02-04T11:10:41.514985Z" ,
"updated_at" : "2026-02-04T11:11:13.666533Z" ,
"code" : "5XRDXCSL" ,
"is_purchased" : false ,
"purchased_total" : 0.0
}
]
} `
```

Modified at 2026-02-16 06:40:51

Previous

Noticiation Settings

Next

Create Notification
