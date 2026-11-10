---
# Synced from https://docs.zid.sa/delete-a-webhook-by-original-id
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-delete-a-webhook-by-original-id
title: "Delete Webhook"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/delete-a-webhook-by-original-id
tags: [from-docs-site, partner-docs]
language: en
---

> Delete Webhook - Zid Docs
# Delete Webhook

DELETE

https://api.zid.sa/ v1/managers/webhooks

This endpoint allows you to delete a specific webhook using originalID . The original ID refers to the unique identifier assigned by the user upon creation.

🔑Scopes

`third_webhook_write` - Webhooks Read & Write

## Request

Query Params

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
` curl --location --request DELETE 'https://api.zid.sa/v1/managers/webhooks?original_id=2404' \
--header 'Authorization: {{Autherization}}' \
--header 'X-Manager-Token: {{Access-Token}}' \
--header 'Accept-Language: en' \
--header 'Content-Type: text/plain' \
--data '' `
```

Response Response Example

200 - Example 1

```
` { } `
```

Modified at 2026-06-04 11:09:30

Previous

Create Webhook

Next

Delete Webhook By subscriber
