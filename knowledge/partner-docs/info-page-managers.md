---
# Synced from https://docs.zid.sa/info-page-managers
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-info-page-managers
title: "Loyalty Program Info"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/info-page-managers
tags: [from-docs-site, partner-docs]
language: en
---

> Loyalty Program Info - Zid Docs
# Loyalty Program Info

GET

https://api.zid.sa/ v1/managers/store/loyalty-program-info

Retrieves information about the store's loyalty program info page content.

🔑Scopes

`loyalty_program.read` - Loyalty Program Read

## Request

Header Params

###

## Responses

🟢 200 OK

application/json

Store loyalty program info page content is retrieved successfully.

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
` curl --location 'https://api.zid.sa/v1/managers/store/loyalty-program-info' \
--header 'Authorization: {{Autherization}}' \
--header 'X-Manager-Token: {{Access-Token}}' \
--header 'Accept: application/json' \
--header 'Accept-Language: en' `
```

Response Response Example

200 - Success

```
` {
"status" : "object" ,
"payload" : {
"title_ar" : "نقاط الولاء" ,
"title_en" : null ,
"content_ar" : "<p>10 نقاط يتم الحصول عليها مقابل كل 50 ريال تم الشراء بها.<br />صالحة لمدة سنة كاملة.<br />والنقاط المكتسبة قابلة للأستبدال بمقابل مبلغ مالي عند اتمام عملية الشراء القادمة.</p>" ,
"content_en" : null
} ,
"message" : {
"type" : "object" ,
"code" : null ,
"name" : null ,
"description" : null
}
} `
```

Modified at 2026-08-11 09:22:34

Previous

Loyalty Program Details

Next

Customer Loyalty Summary
