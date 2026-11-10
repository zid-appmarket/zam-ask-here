---
# Synced from https://docs.zid.sa/rate-limiting-644369m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-rate-limiting
title: "Rate Limiting"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/rate-limiting-644369m0
tags: [from-docs-site, partner-docs]
language: en
---

> Rate Limiting - Zid Docs
# Rate Limiting

The **Rate Limiting** policy controls the number of requests an API will accept within a defined timeframe. Requests exceeding the set limit are rejected to maintain optimal performance.

### What's New #

**New Rate Limiting Rule**: When any third-party system calls our API, we have introduced a restriction of `60 requests / Minute` per application per store.

## Quota and Throttling Policy #

The **Throttling** policy temporarily holds requests that exceed the rate limit, retrying them within a set timeframe. After multiple retry attempts without success, the request is finally rejected. You can adjust:

**Retry Delay**: The time between retries

**Retry Limit**: The maximum number of retries

This feature protects our backend, ensuring smooth performance for other users.

### 💡 Exceptions #

We understand there may be cases that require exceptions. If you believe you have a valid case, please email us with details, and we will evaluate accordingly.

## Zid's Rate Limiting Algorithm #

At **Zid**, we implement the **Leaky Bucket Algorithm** for rate limiting. Wikipedia describes this algorithm as follows:

**From Wikipedia**: The Leaky Bucket algorithm is analogous to a bucket with a small leak. It overflows if the inflow rate exceeds the leak rate or if an excess amount is added all at once. This algorithm is useful for ensuring that event sequences adhere to specified average and peak rates, thus managing any variations.

```
` Leaky Bucket Flow:
- Incoming requests are queued as if being added to a bucket.
- The bucket "leaks" requests at a consistent rate.
- When the bucket is full, additional requests are rejected.`
```

## Polling vs. Webhooks #

### 📊 Polling #

Polling periodically makes requests to check for updates or new data. If new data exists, the system returns it in the response payload. Otherwise, no response is given.

### 📬 Webhooks #

Webhooks simplify tracking data changes by notifying your app directly when status updates occur, reducing the need for repeated calls to our API.

### ⚠️ Important #

**Avoid Frequent Requests**: To prevent system overload, please refrain from repeatedly checking for status updates. For tracking order or payment statuses, consider using our robust Webhook APIs (https://docs.zid.sa/list-of-webhooks) instead.

Modified at 2026-07-30 11:49:13

Previous

Responses

Next

Embedded Apps
