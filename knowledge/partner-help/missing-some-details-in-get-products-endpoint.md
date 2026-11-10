---
# Synced from https://help-partner.zid.sa/en/articles/8693827-missing-some-details-in-get-products-endpoint
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: ph-missing-some-details-in-get-products-endpoint
title: "Missing Some Details in Get Products Endpoint"
product: zam
audience: all
status: verified
updated: 2025-08-04
source_url: https://help-partner.zid.sa/en/articles/8693827-missing-some-details-in-get-products-endpoint
tags: [from-docs-site, partner-help-center]
language: en
---
Encountering missing details or the full list in API response can be a perplexing challenge, but fret not, here's a comprehensive guide to help you troubleshoot and resolve the issue efficiently.

## **Prerequisite**

### 1. **API Documentation Review:**

Start by revisiting the **API documentation (https://docs.zid.sa/)**. Ensure that you are well-acquainted with the expected response format, including the structure and presence of key objects. This step provides a baseline for identifying discrepancies.

### 2. **Verify API Call Parameters:**

Check your API call parameters against the documentation. Confirm that you are sending the correct data and that all required parameters are included. Misconfigurations here can lead to unexpected results.

## **How to solve it: **

### #1 Hint

- **Issue description**:

Missing Product Name in English & Arabic and total product count in Retrieve a list of products endpoint

​

- **Reason:**

not passing the appropriate value on the header

​

- **How to solve it**:

Please send **`role: manager`** on the header of the endpoint

#### Need a further help?

connect with us via chat support and share the cURL command. This will enable us to conduct a more in-depth analysis and provide thorough support.

(https://downloads.intercomcdn.com/i/o/908115027/26b16809a6cf4ee47c4012ee/IMG_20231112_195857.png?expires=1794346200&signature=5925068e3691e7a610cfc522ff2b5662c2835d889f702abc34eff04536ac4937&req=fSAvF8h7nYNYFb4f3HP0gK1Y6PYWYNFDnc2W4OjU4QmPbkdkWnXcAwS0GWL%2F%0ApKqahwdfvK5o65WiKw%3D%3D%0A)

Related Articles

- Troubleshooting the request is missing a required parameter, including an invalid parameter value,. 'Includes a parameter more than once, or is otherwise malformed.

(https://help-partner.zid.sa/en/articles/8717683-troubleshooting-the-request-is-missing-a-required-parameter-including-an-invalid-parameter-value-includes-a-parameter-more-than-once-or-is-otherwise-malformed)

- The authorization server encountered an unexpected condition that prevented it from fulfilling

(https://help-partner.zid.sa/en/articles/8717971-the-authorization-server-encountered-an-unexpected-condition-that-prevented-it-from-fulfilling)

- The refresh token is invalid

(https://help-partner.zid.sa/en/articles/8717984-the-refresh-token-is-invalid)

- If you got a bad request in Create a new product endpoint

(https://help-partner.zid.sa/en/articles/8718008-if-you-got-a-bad-request-in-create-a-new-product-endpoint)

- Error message Changing order status disallowed / لا يمكن تغيير حالة الطلب

(https://help-partner.zid.sa/en/articles/8718012-error-message-changing-order-status-disallowed-لا-يمكن-تغيير-حالة-الطلب)
