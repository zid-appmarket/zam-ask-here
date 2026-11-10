---
# Synced from https://help-partner.zid.sa/en/articles/8718012-error-message-changing-order-status-disallowed-لا-يمكن-تغيير-حالة-الطلب
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: ph-error-message-changing-order-status-disallowed
title: "Error message Changing order status disallowed / لا يمكن تغيير حالة الطلب"
product: zam
audience: all
status: verified
updated: 2025-08-04
source_url: https://help-partner.zid.sa/en/articles/8718012-error-message-changing-order-status-disallowed-لا-يمكن-تغيير-حالة-الطلب
tags: [from-docs-site, partner-help-center]
language: en
---
Encountering an Error message that prevents you to change order status can be a perplexing challenge, but fret not, here's a comprehensive guide to help you troubleshoot and resolve the issue efficiently.

## **Prerequisite**

## 1. **API Documentation Review:**

Start by revisiting the **API documentation (https://docs.zid.sa/)**. Ensure that you are well-acquainted with the expected response format, including the structure and presence of key objects. This step provides a baseline for identifying discrepancies.

## 2. **Verify API Call Parameters:**

Check your API call parameters against the documentation. Confirm that you are sending the correct data and that all required parameters are included. Misconfigurations here can lead to unexpected results.

## **How to solve it: **

## #1 Hint

- **Issue description**:

Changing order status disallowed / لا يمكن تغيير حالة الطلب

​

- **Reason:**

make sure the order status is not ready because you can’t reverse it at this stage and also if completed unless the merchant has made the status process reverse you can make the reverse update via the API.

​

- **How to solve it**:

- Make sure the order status is not ready because you can’t reverse it at this stage and also if completed unless the merchant has made the status processing reverse you can make the reverse update via the API.

​

- Simply use the '/managers/store/orders/{order-id}/change-order-status' endpoint to change the order_status to reversed.

​

​

## Need a further help?

connect with us via chat support and share the cURL command. This will enable us to conduct a more in-depth analysis and provide thorough support.

(https://downloads.intercomcdn.com/i/o/908115027/26b16809a6cf4ee47c4012ee/IMG_20231112_195857.png?expires=1794345300&signature=0824dbef724e31ac3442c0acd22d5c2f04f5c031e959dcb6746f6c6da49c0ab4&req=fSAvF8h7nYNYFb4f3HP0gK1Y6PYWY9BDnc2W4OjU4QmxP7fEQRhFKXLrUSTZ%0AYdQ%2BC9g6NhjD9oODWA%3D%3D%0A)

Related Articles

- Create a shipping app or Fulfillment App

(https://help-partner.zid.sa/en/articles/8637270-create-a-shipping-app-or-fulfillment-app)

- Inventory ID isn't appearing on order details payload or API request

(https://help-partner.zid.sa/en/articles/8718056-inventory-id-isn-t-appearing-on-order-details-payload-or-api-request)

- Invalid order status

(https://help-partner.zid.sa/en/articles/8718076-invalid-order-status)

- Guide to Integrating Shipping Systems with the Zid Platform

(https://help-partner.zid.sa/en/articles/15544622-guide-to-integrating-shipping-systems-with-the-zid-platform)

- Shipping Technical Troubleshooting Guide and Best Practices

(https://help-partner.zid.sa/en/articles/17603812-shipping-technical-troubleshooting-guide-and-best-practices)
