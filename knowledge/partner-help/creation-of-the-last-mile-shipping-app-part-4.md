---
# Synced from https://help-partner.zid.sa/en/articles/15545553-creation-of-the-last-mile-shipping-app-part-4
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: ph-creation-of-the-last-mile-shipping-app-part-4
title: "Creation of the Last Mile Shipping App part 4"
product: zam
audience: all
status: verified
updated: 2026-06-17
source_url: https://help-partner.zid.sa/en/articles/15545553-creation-of-the-last-mile-shipping-app-part-4
tags: [from-docs-site, partner-help-center]
language: en
---
We conclude **Chapter Two** of our technical guide with this final part, where we review the practical experience of what the merchant sees during app activation, how to capture and test Authorization Tokens via API, and how to analyze the activation Webhook payload.

## **XVI. Searching for and Activating the App in the Merchant Dashboard**

After installing the app on the Development Store as explained in the previous step, the merchant logs into their dashboard and navigates to the "Logistics" section, then "Other Shipping Companies".

Here, all available shipping apps are displayed (both the officially Live apps and the test apps linked to your store).

**Important Technical Note on Searching:** The search functionality depends on the dashboard's language. If the merchant's dashboard is in Arabic, you must search using the **Arabic Name** you entered during creation. If the dashboard is switched to English, you must search using the **English Name**.

Once the app is found, the merchant clicks on "View Details", then clicks the **"Activate Now"** button, and confirms the action when prompted. [Suggested image location: Merchant interface showing the search for the app and clicking the Activate Now button]

## **XVII. The Authorization Flow**

The moment the merchant clicks "Confirm", the authorization flow begins programmatically:

- **Redirection:** The merchant is redirected to the permissions screen.

- **Granting Permissions:** A screen displays the exact permissions the shipping app is requesting (e.g., reading orders, updating shipment status, etc.). The merchant agrees to grant these permissions.

- **Callback URL:** After approval, the system redirects back to the Callback URL that you, as the developer, configured earlier in the app settings.

- **Receiving Tokens:** At this exact moment, your system receives the authentication keys (Tokens) required to control the store programmatically. [Suggested image location: The authorization screen where the merchant grants permissions]

## **XVIII. API Testing Using Authorization Tokens**

To verify that the authorization process was successful, we will conduct a practical test using an API testing tool like **Hoppscotch** (which is similar to Postman).

To communicate with the Zid API, you need to pass two primary "keys" (the pillars of authorization) in the request Headers:

- Authorization: This is the (Access Token).

- X-Manager-Token: This is the (Manager Token).

**Practical Testing Steps:**

- We will test the endpoint responsible for retrieving the store and merchant data: Store Manager Profile. (Details and the link for this endpoint can be found in the Zid API Documentation).

- We insert the Tokens into the Headers and click (Send).

- The system will return a (JSON Response) containing all the store's details.

- To find the Store ID (store_id), you must look inside the displayed data structure, specifically inside an Object named "store": { }. (Ensure you read the structure correctly to grab the exact ID).

- Your company can use this retrieved data to automatically create a Profile for the merchant in your system. [Suggested image location: Hoppscotch/Postman interface showing the insertion of Tokens in Headers and retrieving the Store ID data]

## **XIX. Receiving and Analyzing the Webhook Payload**

In parallel with the authorization process, and since we previously subscribed to the (App Activated) event, our server (or the temporary test URL we provided) will receive a (POST Request).

When inspecting this Webhook, we will find that it contains a highly important data Payload, which includes:

- **App ID (app_id)**.

- **Store ID (store_id)** of the store that performed the activation.

- **Store URL**.

- **Event:** Which will correspond to app installation (Install/Activated).

- **Contact Data:** Such as the merchant's email and phone number.

**Utility of this Data:** When the shipping company's system receives this Webhook, it can programmatically recognize the new merchant, create an account for them, and immediately start the Onboarding process, enabling the merchant to sync their orders seamlessly with your company. [Suggested image location: Screen showing the JSON Payload of the Webhook received upon app activation]

**Conclusion of Chapter Two:** With this, we have completed the entire setup cycle for the shipping app and verified the successful activation and initial integration. In the upcoming phase (Chapter Three), we will dive deeply into order creation, receiving order-related webhooks (Order Events), and programmatically completing the shipment lifecycle.

Related Articles

- Guide to Integrating Shipping Systems with the Zid Platform

(https://help-partner.zid.sa/en/articles/15544622-guide-to-integrating-shipping-systems-with-the-zid-platform)

- Creation of the Last Mile Shipping App part 1

(https://help-partner.zid.sa/en/articles/15545034-creation-of-the-last-mile-shipping-app-part-1)

- Creation of the Last Mile Shipping App part 2

(https://help-partner.zid.sa/en/articles/15545303-creation-of-the-last-mile-shipping-app-part-2)

- Creation of the Last Mile Shipping App part 3

(https://help-partner.zid.sa/en/articles/15545496-creation-of-the-last-mile-shipping-app-part-3)

- Creating and Setting Up a Shipping & Fulfillment App - part 3

(https://help-partner.zid.sa/en/articles/15545669-creating-and-setting-up-a-shipping-fulfillment-app-part-3)
