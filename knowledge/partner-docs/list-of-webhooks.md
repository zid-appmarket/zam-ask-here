---
# Synced from https://docs.zid.sa/list-of-webhooks
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-list-of-webhooks
title: "List Webhooks"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/list-of-webhooks
tags: [from-docs-site, partner-docs]
language: en
---

> List Webhooks - Zid Docs
# List Webhooks

GET

https://api.zid.sa/ v1/managers/webhooks

Webhooks enable your application to receive real-time notifications when specific events occur. This endpoint retrieves the list of webhook events that your application is currently subscribed to.

## Supported Webhook Events #

For more details on available events and their conditions,

please refer to the Supported Webhook Events (https://docs.zid.sa/webhooks) page.

🔑Scopes

`third_webhook_read` - Webhooks Read

## Request

Header Params

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
` curl --location 'https://api.zid.sa/v1/managers/webhooks' \
--header 'Authorization: {{Autherization}}' \
--header 'X-Manager-Token: {{Access-Token}}' \
--header 'Accept-Language: en' `
```

Response Response Example

200 - Success

```
` {
"status" : "object" ,
"data" : [
{
"id" : "b1a7ec47-c896-46ea-b5de-727c5bca40d0" ,
"event" : "category.create" ,
"target_url" : "https://webhook.site/b1590566-c28c-4c82-b948-8f8027e84335" ,
"store_id" : "d297fb8b-c322-412e-a2f4-ffa96dc57022" ,
"conditions" : [ ] ,
"original_id" : "2404" ,
"subscriber" : "8208974663db80265e9bfe7b222dcb18" ,
"active" : true ,
"doc" : null
}
] ,
"message" : {
"type" : "object" ,
"code" : null ,
"name" : null ,
"description" : null
}
} `
```

Modified at 2026-06-06 22:03:56

Previous

Recover Broken Webhooks

Next

Create Webhook
