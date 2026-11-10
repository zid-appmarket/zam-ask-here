---
# Synced from https://docs.zid.sa/create-a-webhook
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-create-a-webhook
title: "Create Webhook"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/create-a-webhook
tags: [from-docs-site, partner-docs]
language: en
---

> Create Webhook - Zid Docs
# Create Webhook

POST

https://api.zid.sa/ v1/managers/webhooks

Webhooks enable your application to receive real-time notifications when specific events occur. For supported events, you can define trigger conditions to control when webhook notifications are sent, allowing you to receive only the data that matches your business requirements.

## Supported Webhook Events #

For more details on available events and their conditions,

please refer to the Supported Webhook Events (https://docs.zid.sa/webhooks) page.

🔑Scopes

`third_webhook_write` - Webhooks Read & Write

## **Authentication** #

If `username` and `password` are provided when creating a webhook, Zid will include a `Basic Authentication` header when sending webhook requests.

The values are combined in the format:

```
``
```

This string is then `Base64` encoded and sent in the Authorization header.

Example

If the webhook was created with:

```
`username = user
password = secret`
```

The encoded value will be:

```
``
```

Zid will send webhook requests with the following header:

```
``
```

This allows partners to verify that the webhook request is coming from Zid.

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

🟢 200 OK

Request Request Example

Shell

JavaScript

Java

Swift

```
` curl --location 'https://api.zid.sa/v1/managers/webhooks' \
--header 'Authorization: {{Autherization}}' \
--header 'X-Manager-Token: {{Access-Token}}' \
--header 'Accept-Language: en' \
--header 'Content-Type: application/json' \
--data '{
"event": "order.status.update",
"target_url": "https://webhook.site/b1590566-c28c-4c82-b948-8f8027e84335",
"original_id": 2404,
"conditions": {},
"username": "user",
"password": "secret"
}' `
```

Response Response Example

200 - Success

```
` {
"status" : "object" ,
"data" : {
"id" : "e307483e-795b-4e9c-8f36-a06cb1cf54bf" ,
"event" : "order.status.update" ,
"target_url" : "https://webhook.site/b1590566-c28c-4c82-b948-8f8027e84335" ,
"store_id" : "d297fb8b-c322-412e-a2f4-ffa96dc57022" ,
"store_name" : "متجر أسامة." ,
"store_url" : "https://osama.zid.store/" ,
"conditions" : [ ] ,
"original_id" : "2404" ,
"subscriber" : "8208974663db80265e9bfe7b222dcb18" ,
"active" : true ,
"health_status" : null ,
"consecutive_failures" : null ,
"last_failed_at" : null ,
"last_success_at" : null ,
"broken_at" : null ,
"doc" : null
} ,
"message" : {
"type" : "object" ,
"code" : null ,
"name" : null ,
"description" : null
}
} `
```

Modified at 2026-06-11 09:41:19

Previous

List Webhooks

Next

Delete Webhook
