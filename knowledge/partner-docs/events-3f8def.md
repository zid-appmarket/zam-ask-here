---
# Synced from https://docs.zid.sa/events-878234m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-events-3f8def
title: "Events"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/events-878234m0
tags: [from-docs-site, partner-docs]
language: en
---

> Events - Zid Docs
# Events

Subscription app events notify applications about important subscription activities, such as installation, authorization, renewals, and expiration. These webhooks allow developers to stay updated on merchant interactions with their applications.

## **App Subscription Events** #

The table below lists the subscription events along with their descriptions. Each event sends a notification based on specific subscription activities.

**Event Name** **Description**

`app.market.application.authorized` Triggered when a merchant authorizes an app prior to installation.

`app.market.subscription.active` Send notification on successful activation of subscription.

`app.market.application.install` Send notification on the installation of the application.

`app.market.subscription.warning` Send notification 3 days before the last subscription date (T is the duration of the plan in days).

`app.market.subscription.suspended` Send notification on completion of subscription.

`app.market.subscription.expired` Send notification on T+5 days of subscription where 5 days are GRACE Period and T is in the duration of the plan in days.

`app.market.subscription.renew` Send notification on successful renewal of the same plan subscription 5 days before the last date.

`app.market.subscription.upgrade` Send notification on upgrade of subscription.

`app.market.subscription.refunded` Send notification on refund of subscription.

`app.market.application.uninstall` Send notification on uninstallation of the application.

`app.market.application.rated` Triggered when a merchant submits a rating or review for the app.

`app.market.private.plan.request` Triggered when a merchant submits a request for a private plan.

## Subscribing to App Subscription Events #

To receive real-time notifications about specific events, partners must subscribe to webhooks using the **Partner Dashboard**.

### Creating a Webhook Subscription #

1 .

Navigate to the Webhooks (https://partner.zid.sa/create-application-steps/webhook-management) section when creating or editing your app in the Partner Dashboard.

2 .

Provide the endpoint where webhook notifications should be sent.

3 .

Choose one or more events from the available list.

4 .

If needed, specify additional headers for authentication or other requirements.

5 .

Save and submit the changes. You can return later to edit or add more events as needed.

### Testing Webhooks Using a Development Store #

1 .

Utilize your created development stores to simulate real-world webhook events.

2 .

Perform actions in the store that triggers to the subscribed events.

3 .

Check the webhook logs for successful deliveries or errors. If a webhook fails, review the response details and retry as needed.

## **Webhook Event List and Payloads** #

### **1. App Authorized** #

**Description:** Triggered when a merchant **authorizes an app** before installing it. This event ensures that the merchant has granted permissions required by the application.

**Payload Example:**

```
` {
"app_id" : 1292 ,
"store_id" : 507530 ,
"store_uuid" : "d78468cd-4b44-4fee-a00d-76561f35787c" ,
"store_url" : "https:\/\/wyatt.com.sa\/" ,
"plan_name" : "\u0627\u0644\u0646\u0645\u0648" ,
"status" : "authorized" ,
"start_date" : "2025-02-21T08:05:29.000000Z" ,
"end_date" : "2025-03-22T08:05:29.000000Z" ,
"amount_paid" : 79.01 ,
"old_plan_name" : null ,
"merchant_email" : "info@ehmp.com.sa" ,
"merchant_phone_no" : "966554349999" ,
"event_name" : "app.market.application.authorized" ,
"plan_type" : "Paid" ,
"plan_id" : 904 ,
"payment_date" : "2025-02-21T08:05:29.000000Z"
} `
```

### **2. Subscription Activated** #

**Description:** Sent when a subscription is successfully **activated** after payment.

**Payload Example:**

```
` {
"app_id" : 1292 ,
"store_id" : 507530 ,
"store_uuid" : "d78468cd-4b44-4fee-a00d-76561f35787c" ,
"store_url" : "https:\/\/wyatt.com.sa\/" ,
"plan_name" : "\u0627\u0644\u0646\u0645\u0648" ,
"status" : "active" ,
"start_date" : "2025-02-21T08:05:29.000000Z" ,
"end_date" : "2025-03-22T08:05:29.000000Z" ,
"amount_paid" : 79.01 ,
"old_plan_name" : null ,
"merchant_email" : "info@ehmp.com.sa" ,
"merchant_phone_no" : "966554349999" ,
"event_name" : "app.market.subscription.active" ,
"plan_type" : "Paid" ,
"plan_id" : 904 ,
"payment_date" : "2025-02-21T08:05:29.000000Z"
} `
```

### **3. App Installed** #

**Description:** Sent when an application is **installed** by a merchant.

**Payload Example:**

```
` {
"app_id" : 1292 ,
"store_id" : 507530 ,
"store_uuid" : "d78468cd-4b44-4fee-a00d-76561f35787c" ,
"store_url" : "https:\/\/wyatt.com.sa\/" ,
"plan_name" : "\u0627\u0644\u0646\u0645\u0648" ,
"status" : "install" ,
"start_date" : "2025-02-21T08:05:29.000000Z" ,
"end_date" : "2025-03-22T08:05:29.000000Z" ,
"amount_paid" : 79.01 ,
"old_plan_name" : null ,
"merchant_email" : "info@ehmp.com.sa" ,
"merchant_phone_no" : "966554349999" ,
"event_name" : "app.market.application.install" ,
"plan_type" : "Paid" ,
"plan_id" : 904 ,
"payment_date" : "2025-02-21T08:05:29.000000Z"
} `
```

### **4. Subscription Warning** #

**Description:** Sent **3 days before** the last subscription date as a reminder to renew.

**Payload Example:**

```
` {
"app_id" : 1292 ,
"store_id" : 507530 ,
"store_uuid" : "d78468cd-4b44-4fee-a00d-76561f35787c" ,
"store_url" : "https:\/\/wyatt.com.sa\/" ,
"plan_name" : "\u0627\u0644\u0646\u0645\u0648" ,
"status" : "warning" ,
"start_date" : "2025-02-21T08:05:29.000000Z" ,
"end_date" : "2025-03-22T08:05:29.000000Z" ,
"amount_paid" : 79.01 ,
"old_plan_name" : null ,
"merchant_email" : "info@ehmp.com.sa" ,
"merchant_phone_no" : "966554349999" ,
"event_name" : "app.market.subscription.warning" ,
"plan_type" : "Paid" ,
"plan_id" : 904 ,
"payment_date" : "2025-02-21T08:05:29.000000Z"
} `
```

### **5. Subscription Suspended** #

**Description:** Sent when a subscription is **suspended** after expiration.

**Payload Example:**

```
` {
"app_id" : 1292 ,
"store_id" : 507530 ,
"store_uuid" : "d78468cd-4b44-4fee-a00d-76561f35787c" ,
"store_url" : "https:\/\/wyatt.com.sa\/" ,
"plan_name" : "\u0627\u0644\u0646\u0645\u0648" ,
"status" : "suspended" ,
"start_date" : "2025-02-21T08:05:29.000000Z" ,
"end_date" : "2025-03-22T08:05:29.000000Z" ,
"amount_paid" : 79.01 ,
"old_plan_name" : null ,
"merchant_email" : "info@ehmp.com.sa" ,
"merchant_phone_no" : "966554349999" ,
"event_name" : "app.market.subscription.suspended" ,
"plan_type" : "Paid" ,
"plan_id" : 904 ,
"payment_date" : "2025-02-21T08:05:29.000000Z"
} `
```

### **6. Subscription Expired** #

**Description:** Sent **T+5 days** after the subscription expires, where **T is the plan duration** and **5 days** is the grace period.

**Payload Example:**

```
` {
"app_id" : 1292 ,
"store_id" : 507530 ,
"store_uuid" : "d78468cd-4b44-4fee-a00d-76561f35787c" ,
"store_url" : "https:\/\/wyatt.com.sa\/" ,
"plan_name" : "\u0627\u0644\u0646\u0645\u0648" ,
"status" : "expired" ,
"start_date" : "2025-02-21T08:05:29.000000Z" ,
"end_date" : "2025-03-22T08:05:29.000000Z" ,
"amount_paid" : 79.01 ,
"old_plan_name" : null ,
"merchant_email" : "info@ehmp.com.sa" ,
"merchant_phone_no" : "966554349999" ,
"event_name" : "app.market.subscription.expired" ,
"plan_type" : "Paid" ,
"plan_id" : 904 ,
"payment_date" : "2025-02-21T08:05:29.000000Z"
} `
```

### **7. Subscription Renewed** #

**Description:** Sent **5 days before** the last subscription date when the same plan is successfully renewed.

**Payload Example:**

```
` {
"app_id" : 1292 ,
"store_id" : 507530 ,
"store_uuid" : "d78468cd-4b44-4fee-a00d-76561f35787c" ,
"store_url" : "https:\/\/wyatt.com.sa\/" ,
"plan_name" : "\u0627\u0644\u0646\u0645\u0648" ,
"status" : "renew" ,
"start_date" : "2025-02-21T08:05:29.000000Z" ,
"end_date" : "2025-03-22T08:05:29.000000Z" ,
"amount_paid" : 79.01 ,
"old_plan_name" : null ,
"merchant_email" : "info@ehmp.com.sa" ,
"merchant_phone_no" : "966554349999" ,
"event_name" : "app.market.subscription.renew" ,
"plan_type" : "Paid" ,
"plan_id" : 904 ,
"payment_date" : "2025-02-21T08:05:29.000000Z"
} `
```

### **8. Subscription Upgraded** #

**Description:** Sent when a merchant upgrades their subscription to a higher-tier plan.

**Payload Example:**

```
` {
"app_id" : 1292 ,
"store_id" : 507530 ,
"store_uuid" : "d78468cd-4b44-4fee-a00d-76561f35787c" ,
"store_url" : "https:\/\/wyatt.com.sa\/" ,
"plan_name" : "\u0627\u0644\u0646\u0645\u0648" ,
"status" : "upgrade" ,
"start_date" : "2025-02-21T08:05:29.000000Z" ,
"end_date" : "2025-03-22T08:05:29.000000Z" ,
"amount_paid" : 79.01 ,
"old_plan_name" : null ,
"merchant_email" : "info@ehmp.com.sa" ,
"merchant_phone_no" : "966554349999" ,
"event_name" : "app.market.subscription.upgrade" ,
"plan_type" : "Paid" ,
"plan_id" : 904 ,
"payment_date" : "2025-02-21T08:05:29.000000Z"
} `
```

### **9. Subscription Refunded** #

**Description:** Sent when a subscription payment is **refunded** to the merchant.

**Payload Example:**

```
` {
"app_id" : 1292 ,
"store_id" : 507530 ,
"store_uuid" : "d78468cd-4b44-4fee-a00d-76561f35787c" ,
"store_url" : "https:\/\/wyatt.com.sa\/" ,
"plan_name" : "\u0627\u0644\u0646\u0645\u0648" ,
"status" : "refunded" ,
"start_date" : "2025-02-21T08:05:29.000000Z" ,
"end_date" : "2025-03-22T08:05:29.000000Z" ,
"amount_paid" : 79.01 ,
"old_plan_name" : null ,
"merchant_email" : "info@ehmp.com.sa" ,
"merchant_phone_no" : "966554349999" ,
"event_name" : "app.market.subscription.refunded" ,
"plan_type" : "Paid" ,
"plan_id" : 904 ,
"payment_date" : "2025-02-21T08:05:29.000000Z"
} `
```

### **10. App Uninstalled** #

**Description:** Sent when a merchant **uninstalls** the application.

**Payload Example:**

```
` {
"app_id" : 1292 ,
"store_id" : 507530 ,
"store_uuid" : "d78468cd-4b44-4fee-a00d-76561f35787c" ,
"store_url" : "https:\/\/wyatt.com.sa\/" ,
"plan_name" : "\u0627\u0644\u0646\u0645\u0648" ,
"status" : "uninstall" ,
"start_date" : "2025-02-21T08:05:29.000000Z" ,
"end_date" : "2025-03-22T08:05:29.000000Z" ,
"amount_paid" : 79.01 ,
"old_plan_name" : null ,
"merchant_email" : "info@ehmp.com.sa" ,
"merchant_phone_no" : "966554349999" ,
"event_name" : "app.market.application.uninstall" ,
"plan_type" : "Paid" ,
"plan_id" : 904 ,
"payment_date" : "2025-02-21T08:05:29.000000Z"
} `
```

### **11. App Rated** #

**Description:** Triggered when a merchant **submits a rating or review** for the application.

**Payload Example:**

```
` {
"app_id" : 1292 ,
"store_id" : 507530 ,
"store_uuid" : "d78468cd-4b44-4fee-a00d-76561f35787c" ,
"store_url" : "https:\/\/wyatt.com.sa\/" ,
"plan_name" : "\u0627\u0644\u0646\u0645\u0648" ,
"status" : "rated" ,
"start_date" : "2025-02-21T08:05:29.000000Z" ,
"end_date" : "2025-03-22T08:05:29.000000Z" ,
"amount_paid" : 79.01 ,
"old_plan_name" : null ,
"merchant_email" : "info@ehmp.com.sa" ,
"merchant_phone_no" : "966554349999" ,
"event_name" : "app.market.application.rated" ,
"plan_type" : "Paid" ,
"plan_id" : 904 ,
"payment_date" : "2025-02-21T08:05:29.000000Z"
} `
```

### **12. Private Plan Requested** #

**Description:** Triggered when a merchant submits a **request for a private plan**.

**Payload Example:**

```
` {
"app_id" : 1292 ,
"store_id" : 507530 ,
"store_uuid" : "d78468cd-4b44-4fee-a00d-76561f35787c" ,
"store_url" : "https:\/\/wyatt.com.sa\/" ,
"plan_name" : "\u0627\u0644\u0646\u0645\u0648" ,
"status" : "request" ,
"start_date" : "2025-02-21T08:05:29.000000Z" ,
"end_date" : "2025-03-22T08:05:29.000000Z" ,
"amount_paid" : 79.01 ,
"old_plan_name" : null ,
"merchant_email" : "info@ehmp.com.sa" ,
"merchant_phone_no" : "966554349999" ,
"event_name" : "app.market.private.plan.request" ,
"plan_type" : "Paid" ,
"plan_id" : 904 ,
"payment_date" : "2025-02-21T08:05:29.000000Z"
} `
```

### Identifying Free Trial Subscriptions #

Applications can determine whether a merchant is currently on a free trial by monitoring subscription-related webhook events.

#### Relevant Webhook Events #

The following events include subscription details:

`app.market.subscription.active`

`app.market.application.authorized`

`app.market.application.install`

#### Free Trial Detection #

A subscription should be considered a free trial only when the following condition is met:

`plan_type` is equal to `"Free Trial"`

#### Example #

```
` {
"app_id" : 6528 ,
"store_id" : 3104452 ,
"store_uuid" : "b2052c72-ddaa-411f-a428-748dcd885a6e" ,
"store_url" : "https://xle6e8.zid.store/" ,
"plan_name" : "Test Plan With Trial" ,
"status" : "active" ,
"start_date" : "2026-06-14T08:05:40.000000Z" ,
"end_date" : "2026-07-04T08:05:40.000000Z" ,
"amount_paid" : 0 ,
"old_plan_name" : null ,
"merchant_email" : "bv3e7xxnx5@zam-partner.email" ,
"merchant_phone_no" : "+201101050117" ,
"event_name" : "app.market.subscription.active" ,
"plan_type" : "Free Trial" ,
"plan_id" : 3329 ,
"payment_date" : "2026-06-14T08:05:40.000000Z"
} `
```

In the example above, the subscription is identified as a free trial because `plan_type` is `"Free Trial"`. Applications should validate this field when determining whether a subscription is in a trial period and applying any trial-specific business logic.

## New Webhooks: Usage-Based Subscription Payments #

Two new webhook events have been added to the **Subscription Webhooks** category. Partners with OAuth apps can subscribe to these events to track usage-based subscription charge outcomes.

### 1. Usage-Based Subscription Payment Success #

**Topic:** `app.market.subscription.usage_based.payment_success`

Fired when a usage-based subscription charge is successfully paid by a merchant.

#### Payload #

```
` {
"action" : "usage_based_subscription_payment_success" ,
"envelope" : {
"store_id" : 12345 ,
"app" : {
"app_id" : 67 ,
"app_name" : "My App"
} ,
"subscription" : {
"plan" : "Professional" ,
"plan_price" : 99.00
}
}
} `
```

### 2. Usage-Based Subscription Payment Failure #

**Topic:** `app.market.subscription.usage_based.payment_failure`

Fired when a usage-based subscription charge payment attempt fails for a merchant.

#### Payload #

```
` {
"action" : "usage_based_subscription_payment_failure" ,
"envelope" : {
"store_id" : 12345 ,
"app" : {
"app_id" : 67 ,
"app_name" : "My App"
} ,
"subscription" : {
"plan" : "Professional" ,
"plan_price" : 99.00
}
}
} `
```

### Payload Fields #

Field Type Description

`action` `string` The webhook event type. Either `usage_based_subscription_payment_success` or `usage_based_subscription_payment_failure`.

`envelope.store_id` `integer` The ID of the merchant store where the charge was attempted.

`envelope.app.app_id` `integer` The ID of the app the subscription charge belongs to.

`envelope.app.app_name` `string` The display name of the app.

`envelope.subscription.plan` `string` The name of the subscription plan.

`envelope.subscription.plan_price` `number` The price of the subscription plan.

### Subscribing #

These events are part of the **Subscription Webhooks** group, available to **OAuth apps**. Subscribe via the App Market partner dashboard under webhook settings,

### When Are These Fired? #

Usage-based plans allow apps to charge merchants for actual usage rather than a fixed recurring fee. When a charge is initiated:

If the payment succeeds → `app.market.subscription.usage_based.payment_success` is sent.

If the payment fails → `app.market.subscription.usage_based.payment_failure` is sent.

Both events are delivered asynchronously after the payment attempt resolves.

Modified at 2026-06-30 11:22:55

Previous

App Management

Next

APIs
