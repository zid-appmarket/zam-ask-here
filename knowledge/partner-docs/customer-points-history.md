---
# Synced from https://docs.zid.sa/customer-points-history
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-customer-points-history
title: "Customer Points History"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/customer-points-history
tags: [from-docs-site, partner-docs]
language: en
---

> Customer Points History - Zid Docs
# Customer Points History

GET

https://api.zid.sa/ v1/managers/loyalty-program/points-history/{customer-id}

Retrieves the transaction history of a specific customer's loyalty points activity.

🔑Scopes

`loyalty_program.read` - Loyalty Program Read

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

🟠 400 Bad Request

🟠 401 Unauthorized

🔴 500 Internal Server error

Request Request Example

Shell

JavaScript

Java

Swift

```
` curl --location 'https://api.zid.sa/v1/managers/loyalty-program/points-history/37' \
--header 'Authorization: {{Autherization}}' \
--header 'X-Manager-Token: {{Access-Token}}' \
--header 'Accept: application/json' \
--header 'Accept-Language: en' `
```

Response Response Example

200 - Success

```
{
"status": "object",
"history": [
{
"date": "2026-02-16T19:41:52.000000Z",
"reason": "Expired pending transaction",
"points": 135,
"direction": "-",
"type": "expiry",
"order_number": null,
"order_code": null,
"expiry_date": null,
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Points expired"
},
{
"date": "2026-02-11T11:59:28.000000Z",
"reason": null,
"points": 10,
"direction": "+",
"type": "reward",
"order_number": 64855100,
"order_code": "x8uwLv8aa5",
"expiry_date": "2026-03-13T11:59:28.000000Z",
"point_status": "Pending",
"point_status_code": "pending",
"collection_method": "Reward for a placed order"
},
{
"date": "2025-12-22T18:12:38.000000Z",
"reason": "deduct expired points of pending transaction",
"points": 135,
"direction": "-",
"type": "expiry",
"order_number": null,
"order_code": null,
"expiry_date": null,
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Points expired"
},
{
"date": "2025-12-22T13:12:28.000000Z",
"reason": "deduct expired points of pending transaction",
"points": 135,
"direction": "-",
"type": "expiry",
"order_number": null,
"order_code": null,
"expiry_date": null,
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Points expired"
},
{
"date": "2025-12-19T12:12:42.000000Z",
"reason": "deduct expired points of pending transaction",
"points": 135,
"direction": "-",
"type": "expiry",
"order_number": null,
"order_code": null,
"expiry_date": null,
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Points expired"
},
{
"date": "2025-12-16T10:15:39.000000Z",
"reason": "deduct expired points of pending transaction",
"points": 28,
"direction": "-",
"type": "expiry",
"order_number": null,
"order_code": null,
"expiry_date": null,
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Points expired"
},
{
"date": "2025-12-16T10:15:37.000000Z",
"reason": "deduct expired points of pending transaction",
"points": 27,
"direction": "-",
"type": "expiry",
"order_number": null,
"order_code": null,
"expiry_date": null,
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Points expired"
},
{
"date": "2025-12-16T10:15:36.000000Z",
"reason": "deduct expired points of pending transaction",
"points": 27,
"direction": "-",
"type": "expiry",
"order_number": null,
"order_code": null,
"expiry_date": null,
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Points expired"
},
{
"date": "2025-12-16T10:15:36.000000Z",
"reason": "deduct expired points of pending transaction",
"points": 27,
"direction": "-",
"type": "expiry",
"order_number": null,
"order_code": null,
"expiry_date": null,
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Points expired"
},
{
"date": "2025-12-16T10:15:35.000000Z",
"reason": "deduct expired points of pending transaction",
"points": 27,
"direction": "-",
"type": "expiry",
"order_number": null,
"order_code": null,
"expiry_date": null,
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Points expired"
},
{
"date": "2025-11-23T09:15:48.000000Z",
"reason": "deduct expired points of pending transaction",
"points": 13,
"direction": "-",
"type": "expiry",
"order_number": null,
"order_code": null,
"expiry_date": null,
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Points expired"
},
{
"date": "2025-11-12T09:15:47.000000Z",
"reason": "deduct expired remaining points of active transaction",
"points": 13,
"direction": "-",
"type": "expiry",
"order_number": null,
"order_code": null,
"expiry_date": null,
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Points expired"
},
{
"date": "2025-11-12T09:15:47.000000Z",
"reason": "deduct expired points of pending transaction",
"points": 13,
"direction": "-",
"type": "expiry",
"order_number": null,
"order_code": null,
"expiry_date": null,
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Points expired"
},
{
"date": "2025-11-12T09:15:47.000000Z",
"reason": "deduct expired points of pending transaction",
"points": 13,
"direction": "-",
"type": "expiry",
"order_number": null,
"order_code": null,
"expiry_date": null,
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Points expired"
},
{
"date": "2025-11-12T09:15:47.000000Z",
"reason": "deduct expired points of pending transaction",
"points": 13,
"direction": "-",
"type": "expiry",
"order_number": null,
"order_code": null,
"expiry_date": null,
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Points expired"
},
{
"date": "2025-11-12T09:15:46.000000Z",
"reason": "deduct expired points of pending transaction",
"points": 13,
"direction": "-",
"type": "expiry",
"order_number": null,
"order_code": null,
"expiry_date": null,
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Points expired"
},
{
"date": "2025-11-12T08:12:12.000000Z",
"reason": "deduct expired points of pending transaction",
"points": 13,
"direction": "-",
"type": "expiry",
"order_number": null,
"order_code": null,
"expiry_date": null,
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Points expired"
},
{
"date": "2025-11-12T08:12:12.000000Z",
"reason": "deduct expired points of pending transaction",
"points": 27,
"direction": "-",
"type": "expiry",
"order_number": null,
"order_code": null,
"expiry_date": null,
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Points expired"
},
{
"date": "2025-10-24T08:27:14.000000Z",
"reason": null,
"points": 13,
"direction": "+",
"type": "reward",
"order_number": 59561231,
"order_code": "26hYMc9eN0",
"expiry_date": "2025-11-23T08:27:14.000000Z",
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Reward for a placed order"
},
{
"date": "2025-10-13T09:04:56.000000Z",
"reason": null,
"points": 13,
"direction": "+",
"type": "reward",
"order_number": 59216351,
"order_code": "Fcf1q7MnKc",
"expiry_date": "2025-11-12T09:04:56.000000Z",
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Reward for a placed order"
},
{
"date": "2025-10-13T09:04:30.000000Z",
"reason": null,
"points": 13,
"direction": "+",
"type": "reward",
"order_number": 59216333,
"order_code": "TbOze5upkw",
"expiry_date": "2025-11-12T09:04:30.000000Z",
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Reward for a placed order"
},
{
"date": "2025-10-13T09:03:46.000000Z",
"reason": null,
"points": 13,
"direction": "+",
"type": "reward",
"order_number": 59216317,
"order_code": "Y63vkFU8PR",
"expiry_date": "2025-11-12T09:03:46.000000Z",
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Reward for a placed order"
},
{
"date": "2025-10-13T08:45:27.000000Z",
"reason": null,
"points": 13,
"direction": "+",
"type": "reward",
"order_number": 59215877,
"order_code": "RAJnIAXl2a",
"expiry_date": "2025-11-12T08:45:27.000000Z",
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Reward for a placed order"
},
{
"date": "2025-10-13T08:44:29.000000Z",
"reason": null,
"points": 13,
"direction": "+",
"type": "reward",
"order_number": 59215854,
"order_code": "78icLnIFcE",
"expiry_date": "2025-11-12T08:44:29.000000Z",
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Reward for a placed order"
},
{
"date": "2025-10-13T08:11:17.000000Z",
"reason": null,
"points": 13,
"direction": "+",
"type": "reward",
"order_number": 59215141,
"order_code": "MvdfNjX2RU",
"expiry_date": "2025-11-12T08:11:17.000000Z",
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Reward for a placed order"
},
{
"date": "2025-10-13T07:53:14.000000Z",
"reason": null,
"points": 27,
"direction": "+",
"type": "reward",
"order_number": 59214748,
"order_code": "AIajhbzS7h",
"expiry_date": "2025-11-12T07:53:14.000000Z",
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Reward for a placed order"
},
{
"date": "2025-09-30T10:26:33.000000Z",
"reason": "deduct expired points of pending transaction",
"points": 10,
"direction": "-",
"type": "expiry",
"order_number": null,
"order_code": null,
"expiry_date": null,
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Points expired"
},
{
"date": "2025-09-27T10:25:57.000000Z",
"reason": "deduct expired points of pending transaction",
"points": 13,
"direction": "-",
"type": "expiry",
"order_number": null,
"order_code": null,
"expiry_date": null,
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Points expired"
},
{
"date": "2025-09-26T13:14:45.000000Z",
"reason": "deduct expired points of pending transaction",
"points": 13,
"direction": "-",
"type": "expiry",
"order_number": null,
"order_code": null,
"expiry_date": null,
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Points expired"
},
{
"date": "2025-09-25T06:16:51.000000Z",
"reason": "deduct expired points of pending transaction",
"points": 13,
"direction": "-",
"type": "expiry",
"order_number": null,
"order_code": null,
"expiry_date": null,
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Points expired"
},
{
"date": "2025-09-13T01:18:06.000000Z",
"reason": "deduct expired points of pending transaction",
"points": 13,
"direction": "-",
"type": "expiry",
"order_number": null,
"order_code": null,
"expiry_date": null,
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Points expired"
},
{
"date": "2025-09-13T01:18:05.000000Z",
"reason": "deduct expired points of pending transaction",
"points": 13,
"direction": "-",
"type": "expiry",
"order_number": null,
"order_code": null,
"expiry_date": null,
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Points expired"
},
{
"date": "2025-09-13T01:18:05.000000Z",
"reason": "deduct expired remaining points of active transaction",
"points": 13,
"direction": "-",
"type": "expiry",
"order_number": null,
"order_code": null,
"expiry_date": null,
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Points expired"
},
{
"date": "2025-09-06T11:25:15.000000Z",
"reason": "deduct expired remaining points of active transaction",
"points": 9,
"direction": "-",
"type": "expiry",
"order_number": null,
"order_code": null,
"expiry_date": null,
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Points expired"
},
{
"date": "2025-08-28T09:45:46.000000Z",
"reason": null,
"points": 13,
"direction": "+",
"type": "reward",
"order_number": 56522219,
"order_code": "dZhTbZE9Yn",
"expiry_date": "2025-09-27T09:45:46.000000Z",
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Reward for a placed order"
},
{
"date": "2025-08-27T12:27:53.000000Z",
"reason": null,
"points": 13,
"direction": "+",
"type": "reward",
"order_number": 56464544,
"order_code": "2f8YxtXwz5",
"expiry_date": "2025-09-26T12:27:53.000000Z",
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Reward for a placed order"
},
{
"date": "2025-08-26T05:14:44.000000Z",
"reason": null,
"points": 13,
"direction": "+",
"type": "reward",
"order_number": 56397696,
"order_code": "z0862DOjzu",
"expiry_date": "2025-09-25T05:14:44.000000Z",
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Reward for a placed order"
},
{
"date": "2025-08-14T00:56:15.000000Z",
"reason": null,
"points": 13,
"direction": "+",
"type": "reward",
"order_number": 56002619,
"order_code": "8mM4sFUtd2",
"expiry_date": "2025-09-13T00:56:15.000000Z",
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Reward for a placed order"
},
{
"date": "2025-08-14T00:35:13.000000Z",
"reason": null,
"points": 13,
"direction": "+",
"type": "reward",
"order_number": 56002317,
"order_code": "mWEC4Q4vf8",
"expiry_date": "2025-09-13T00:35:13.000000Z",
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Reward for a placed order"
},
{
"date": "2025-08-14T00:17:53.000000Z",
"reason": null,
"points": 13,
"direction": "+",
"type": "reward",
"order_number": 56002018,
"order_code": "X1cMwY29s3",
"expiry_date": "2025-09-13T00:17:53.000000Z",
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Reward for a placed order"
},
{
"date": "2025-08-07T10:26:24.000000Z",
"reason": null,
"points": 9,
"direction": "+",
"type": "reward",
"order_number": 55761045,
"order_code": "eUB2XxLFmW",
"expiry_date": "2025-09-06T10:26:24.000000Z",
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Reward for a placed order"
},
{
"date": "2025-07-30T10:52:54.000000Z",
"reason": null,
"points": 60,
"direction": "-",
"type": "expiry",
"order_number": null,
"order_code": null,
"expiry_date": null,
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Points expired"
},
{
"date": "2025-07-29T08:21:58.000000Z",
"reason": null,
"points": 83,
"direction": "-",
"type": "expiry",
"order_number": null,
"order_code": null,
"expiry_date": null,
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Points expired"
},
{
"date": "2025-07-26T13:26:56.000000Z",
"reason": null,
"points": 216,
"direction": "-",
"type": "expiry",
"order_number": null,
"order_code": null,
"expiry_date": null,
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Points expired"
},
{
"date": "2025-06-30T10:52:51.000000Z",
"reason": null,
"points": 60,
"direction": "+",
"type": "reward",
"order_number": 54330029,
"order_code": "VHXYxLARDo",
"expiry_date": "2025-07-30T10:52:54.000000Z",
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Reward for a placed order"
},
{
"date": "2025-06-29T08:21:57.000000Z",
"reason": null,
"points": 83,
"direction": "+",
"type": "reward",
"order_number": 54284651,
"order_code": "y0AZCj6BQH",
"expiry_date": "2025-07-29T08:21:58.000000Z",
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Reward for a placed order"
},
{
"date": "2025-06-26T13:26:53.000000Z",
"reason": null,
"points": 216,
"direction": "+",
"type": "reward",
"order_number": 54154307,
"order_code": "IAjjm8cnkY",
"expiry_date": "2025-07-26T13:26:56.000000Z",
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Reward for a placed order"
},
{
"date": "2025-06-11T14:14:01.000000Z",
"reason": null,
"points": 104,
"direction": "-",
"type": "expiry",
"order_number": null,
"order_code": null,
"expiry_date": null,
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Points expired"
},
{
"date": "2025-05-30T07:58:06.000000Z",
"reason": null,
"points": 103,
"direction": "-",
"type": "expiry",
"order_number": null,
"order_code": null,
"expiry_date": null,
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Points expired"
},
{
"date": "2025-05-18T11:42:12.000000Z",
"reason": null,
"points": 83,
"direction": "-",
"type": "expiry",
"order_number": null,
"order_code": null,
"expiry_date": null,
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Points expired"
},
{
"date": "2025-05-17T10:35:13.000000Z",
"reason": null,
"points": 83,
"direction": "-",
"type": "expiry",
"order_number": null,
"order_code": null,
"expiry_date": null,
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Points expired"
},
{
"date": "2025-05-17T03:49:46.000000Z",
"reason": null,
"points": 103,
"direction": "-",
"type": "expiry",
"order_number": null,
"order_code": null,
"expiry_date": null,
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Points expired"
},
{
"date": "2025-05-13T17:33:43.000000Z",
"reason": null,
"points": 83,
"direction": "-",
"type": "expiry",
"order_number": null,
"order_code": null,
"expiry_date": null,
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Points expired"
},
{
"date": "2025-05-12T14:13:59.000000Z",
"reason": null,
"points": 104,
"direction": "+",
"type": "reward",
"order_number": 52116969,
"order_code": "HtPK0eM1AC",
"expiry_date": "2025-06-11T14:14:01.000000Z",
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Reward for a placed order"
},
{
"date": "2025-04-30T07:58:04.000000Z",
"reason": null,
"points": 103,
"direction": "+",
"type": "reward",
"order_number": 51626527,
"order_code": "AEZBQN0bJK",
"expiry_date": "2025-05-30T07:58:06.000000Z",
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Reward for a placed order"
},
{
"date": "2025-04-18T11:42:10.000000Z",
"reason": null,
"points": 83,
"direction": "+",
"type": "reward",
"order_number": 51256383,
"order_code": "dweyAV6q7k",
"expiry_date": "2025-05-18T11:42:12.000000Z",
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Reward for a placed order"
},
{
"date": "2025-04-17T10:35:11.000000Z",
"reason": null,
"points": 83,
"direction": "+",
"type": "reward",
"order_number": 51231984,
"order_code": "DwFYIpHlpo",
"expiry_date": "2025-05-17T10:35:13.000000Z",
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Reward for a placed order"
},
{
"date": "2025-04-17T03:49:38.000000Z",
"reason": null,
"points": 103,
"direction": "+",
"type": "reward",
"order_number": 51226265,
"order_code": "HvPcEEOSqd",
"expiry_date": "2025-05-17T03:49:46.000000Z",
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Reward for a placed order"
},
{
"date": "2025-04-13T17:33:42.000000Z",
"reason": null,
"points": 83,
"direction": "+",
"type": "reward",
"order_number": 51137943,
"order_code": "K1EGLWqIxg",
"expiry_date": "2025-05-13T17:33:43.000000Z",
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Reward for a placed order"
},
{
"date": "2025-03-26T08:20:54.000000Z",
"reason": null,
"points": 181,
"direction": "-",
"type": "expiry",
"order_number": null,
"order_code": null,
"expiry_date": null,
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Points expired"
},
{
"date": "2025-03-04T12:01:22.000000Z",
"reason": null,
"points": 4774,
"direction": "-",
"type": "expiry",
"order_number": null,
"order_code": null,
"expiry_date": null,
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Points expired"
},
{
"date": "2025-02-24T08:20:51.000000Z",
"reason": null,
"points": 181,
"direction": "+",
"type": "reward",
"order_number": 47993579,
"order_code": "i1yPVUNBos",
"expiry_date": "2025-03-26T08:20:54.000000Z",
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Reward for a placed order"
},
{
"date": "2025-02-02T11:25:59.000000Z",
"reason": null,
"points": 4774,
"direction": "+",
"type": "reward",
"order_number": 47009589,
"order_code": "GmU8WqDHZ8",
"expiry_date": "2025-03-04T11:26:01.000000Z",
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Reward for a placed order"
},
{
"date": "2025-01-01T13:22:53.000000Z",
"reason": null,
"points": 135,
"direction": "+",
"type": "reward",
"order_number": 45881366,
"order_code": "syuQXMfCvo",
"expiry_date": "2026-02-05T13:22:54.000000Z",
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Reward for a placed order"
},
{
"date": "2024-11-17T18:05:45.000000Z",
"reason": null,
"points": 135,
"direction": "+",
"type": "reward",
"order_number": 44162569,
"order_code": "UUXEjMypB8",
"expiry_date": "2025-12-22T18:05:47.000000Z",
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Reward for a placed order"
},
{
"date": "2024-11-17T12:32:04.000000Z",
"reason": null,
"points": 135,
"direction": "+",
"type": "reward",
"order_number": 44153085,
"order_code": "2ABjLoknGB",
"expiry_date": "2025-12-22T12:32:06.000000Z",
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Reward for a placed order"
},
{
"date": "2024-11-14T11:35:59.000000Z",
"reason": null,
"points": 135,
"direction": "+",
"type": "reward",
"order_number": 44071225,
"order_code": "dMYcHkuLxt",
"expiry_date": "2025-12-19T11:36:01.000000Z",
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Reward for a placed order"
},
{
"date": "2024-11-11T10:14:24.000000Z",
"reason": null,
"points": 27,
"direction": "+",
"type": "reward",
"order_number": 43988433,
"order_code": "OtXxlx7o0d",
"expiry_date": "2025-12-16T10:14:27.000000Z",
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Reward for a placed order"
},
{
"date": "2024-11-11T09:28:01.000000Z",
"reason": null,
"points": 27,
"direction": "+",
"type": "reward",
"order_number": 43987395,
"order_code": "1jETm7eVEe",
"expiry_date": "2025-12-16T09:28:04.000000Z",
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Reward for a placed order"
},
{
"date": "2024-11-11T09:25:52.000000Z",
"reason": null,
"points": 27,
"direction": "+",
"type": "reward",
"order_number": 43987353,
"order_code": "QItKi3ynIO",
"expiry_date": "2025-12-16T09:25:55.000000Z",
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Reward for a placed order"
},
{
"date": "2024-11-11T09:12:38.000000Z",
"reason": null,
"points": 28,
"direction": "+",
"type": "reward",
"order_number": 43987077,
"order_code": "MQ7UJyZn69",
"expiry_date": "2025-12-16T09:12:44.000000Z",
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Reward for a placed order"
},
{
"date": "2024-11-11T09:00:28.000000Z",
"reason": null,
"points": 27,
"direction": "+",
"type": "reward",
"order_number": 43986837,
"order_code": "jl4BzNdbrP",
"expiry_date": "2025-12-16T09:00:31.000000Z",
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Reward for a placed order"
},
{
"date": "2024-10-17T10:11:49.000000Z",
"reason": null,
"points": 3,
"direction": "-",
"type": "expiry",
"order_number": null,
"order_code": null,
"expiry_date": null,
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Points expired"
},
{
"date": "2024-10-17T10:10:17.000000Z",
"reason": null,
"points": 1,
"direction": "-",
"type": "expiry",
"order_number": null,
"order_code": null,
"expiry_date": null,
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Points expired"
},
{
"date": "2024-08-26T10:20:44.000000Z",
"reason": null,
"points": 10,
"direction": "+",
"type": "reward",
"order_number": 40361929,
"order_code": "lY78BfzfyS",
"expiry_date": "2025-09-30T10:21:02.000000Z",
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Reward for a placed order"
},
{
"date": "2024-05-07T08:20:06.000000Z",
"reason": null,
"points": 23,
"direction": "-",
"type": "expiry",
"order_number": null,
"order_code": null,
"expiry_date": null,
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Points expired"
},
{
"date": "2024-05-02T08:20:02.000000Z",
"reason": null,
"points": 23,
"direction": "+",
"type": "reward",
"order_number": 36331464,
"order_code": "lZ9LEGDplR",
"expiry_date": "2024-05-07T08:20:06.000000Z",
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Reward for a placed order"
},
{
"date": "2024-03-26T09:42:13.000000Z",
"reason": null,
"points": 5,
"direction": "-",
"type": "expiry",
"order_number": null,
"order_code": null,
"expiry_date": null,
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Points expired"
},
{
"date": "2024-03-24T13:01:13.000000Z",
"reason": null,
"points": 28,
"direction": "-",
"type": "expiry",
"order_number": null,
"order_code": null,
"expiry_date": null,
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Points expired"
},
{
"date": "2024-03-24T12:53:39.000000Z",
"reason": null,
"points": 2,
"direction": "-",
"type": "expiry",
"order_number": null,
"order_code": null,
"expiry_date": null,
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Points expired"
},
{
"date": "2024-03-21T09:42:07.000000Z",
"reason": null,
"points": 5,
"direction": "+",
"type": "reward",
"order_number": 34328031,
"order_code": "URZy6Ct9SM",
"expiry_date": "2024-03-26T09:42:13.000000Z",
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Reward for a placed order"
},
{
"date": "2024-03-19T13:00:00.000000Z",
"reason": null,
"points": 28,
"direction": "+",
"type": "reward",
"order_number": 34205559,
"order_code": "tBYMtHW14L",
"expiry_date": "2024-03-24T13:01:13.000000Z",
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Reward for a placed order"
},
{
"date": "2024-03-19T12:17:55.000000Z",
"reason": null,
"points": 2,
"direction": "+",
"type": "reward",
"order_number": 34204234,
"order_code": "x56qXDQodU",
"expiry_date": "2024-03-24T12:53:39.000000Z",
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Reward for a placed order"
},
{
"date": "2023-10-23T10:11:39.000000Z",
"reason": null,
"points": 3,
"direction": "+",
"type": "reward",
"order_number": 28788638,
"order_code": "Ua04ci4n0p",
"expiry_date": "2024-10-17T10:11:49.000000Z",
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Reward for a placed order"
},
{
"date": "2023-10-23T10:10:02.000000Z",
"reason": null,
"points": 1,
"direction": "+",
"type": "reward",
"order_number": 28788603,
"order_code": "9puS0B9dU0",
"expiry_date": "2024-10-17T10:10:17.000000Z",
"point_status": "Expired",
"point_status_code": "expired",
"collection_method": "Reward for a placed order"
}
],
"message": {
"type": "object",
"code": null,
"name": null,
"description": null
}
}
```

Modified at 2026-08-11 09:16:33

Previous

Customer Loyalty Summary

Next

Activate Loyalty Program
