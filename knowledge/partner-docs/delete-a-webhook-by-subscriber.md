---
# Synced from https://docs.zid.sa/delete-a-webhook-by-subscriber
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-delete-a-webhook-by-subscriber
title: "Delete Webhook By subscriber"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/delete-a-webhook-by-subscriber
tags: [from-docs-site, partner-docs]
language: en
---

> Delete Webhook By subscriber - Zid Docs
# Delete Webhook By subscriber

Deprecated

DELETE

https://api.zid.sa/ v1/managers/webhooks/subscribers/{subscriber}

This endpoint allows you to delete all the webhooks associated with a subscriberID. The subscriberID refers to the unique identifier assigned to the user upon creation.

🔑Scopes

`webhooks.read_write` - Webhooks Read & Write

## Request

Path Params

###

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
` curl --location --request DELETE 'https://api.zid.sa/v1/managers/webhooks/subscribers/8208974663db80265e9bfe7b222dcb18' \
--header 'Authorization: {{Autherization}}' \
--header 'X-Manager-Token: {{Access-Token}}' \
--header 'Accept-Language: en' `
```

Response Response Example

200 - Example 1

```
` {
"status" : "string" ,
"message" : {
"type" : "string" ,
"code" : "string" ,
"name" : "string" ,
"description" : "string"
}
} `
```

Modified at 2026-01-30 20:55:20

Previous

Delete Webhook

Next

App Management
