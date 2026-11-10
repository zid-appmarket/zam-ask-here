---
# Synced from https://help-partner.zid.sa/en/articles/8718064-timeout-response-in-get-product-customer-endpoint
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: ph-timeout-response-in-get-product-customer-endpoint
title: "Timeout response in Get Product / Customer endpoint"
product: zam
audience: all
status: verified
updated: 2025-08-04
source_url: https://help-partner.zid.sa/en/articles/8718064-timeout-response-in-get-product-customer-endpoint
tags: [from-docs-site, partner-help-center]
language: en
---
## **Prerequisite**

## 1. **API Documentation Review:**

Start by revisiting the **API documentation (https://docs.zid.sa/)**. Ensure that you are well-acquainted with the expected response format, including the structure and presence of key objects. This step provides a baseline for identifying discrepancies.

## 2. **Verify API Call Parameters:**

Check your API call parameters against the documentation. Confirm that you are sending the correct data and that all required parameters are included. Misconfigurations here can lead to unexpected results.

## **How to solve it: **

## #1 Hint

- **Issue description**:

504 gateway timeout

​

- **Reason:**

Make sure you don't send long capacity requests and only use the pagination

​

- **How to solve it**:

- Make a request with the limit for example 50 per page.

- Use the pagination for example make a request with limit for example 50 per page

## Need a further help?

connect with us via chat support and share the cURL command. This will enable us to conduct a more in-depth analysis and provide thorough support.

(https://downloads.intercomcdn.com/i/o/908115027/26b16809a6cf4ee47c4012ee/IMG_20231112_195857.png?expires=1794345300&signature=0824dbef724e31ac3442c0acd22d5c2f04f5c031e959dcb6746f6c6da49c0ab4&req=fSAvF8h7nYNYFb4f3HP0gK1Y6PYWY9BDnc2W4OjU4QmxP7fEQRhFKXLrUSTZ%0AYdQ%2BC9g6NhjD9oODWA%3D%3D%0A)

Related Articles

- Missing Some Details in Get Products Endpoint

(https://help-partner.zid.sa/en/articles/8693827-missing-some-details-in-get-products-endpoint)

- If you got a bad request in Create a new product endpoint

(https://help-partner.zid.sa/en/articles/8718008-if-you-got-a-bad-request-in-create-a-new-product-endpoint)

- Inventory address not found in calling List Store Locations endpoint

(https://help-partner.zid.sa/en/articles/8718029-inventory-address-not-found-in-calling-list-store-locations-endpoint)

- No such user - Unauthorized request

(https://help-partner.zid.sa/en/articles/8718037-no-such-user-unauthorized-request)

- Too Many Attempts, Please slow down for few seconds !

(https://help-partner.zid.sa/en/articles/8718081-too-many-attempts-please-slow-down-for-few-seconds)
