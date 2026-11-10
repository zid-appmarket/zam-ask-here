---
# Synced from https://help-partner.zid.sa/en/articles/15545669-creating-and-setting-up-a-shipping-fulfillment-app-part-3
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: ph-creating-and-setting-up-a-shipping-fulfillment-app-part-3
title: "Creating and Setting Up a Shipping & Fulfillment App - part 3"
product: zam
audience: all
status: verified
updated: 2026-06-17
source_url: https://help-partner.zid.sa/en/articles/15545669-creating-and-setting-up-a-shipping-fulfillment-app-part-3
tags: [from-docs-site, partner-help-center]
language: en
---
Continuing **Chapter Three** of the "Shipping & Fulfillment" application guide. In this section, we will review the practical experience of activating the app from the merchant's side, testing the integration programmatically, with a special focus on how to analyze the critical Webhooks related to fulfillment and synchronization services.

## **XII. Activating the Shipping & Fulfillment App from the Merchant's Account**

After the merchant searches for the app (as explained at the end of the previous section), they will proceed with the activation steps:

- Upon clicking "Activate", a screen will appear presenting the merchant with important fulfillment-specific options, such as:

- **Auto-Dispatch.**

- **Sync Products/Quantities.**

- The merchant can toggle these features on or off based on their preference.

- Next, the "Permissions" screen appears, detailing the access rights the application needs regarding store data.

- Once the merchant clicks **"Install"**, the Authorization process is complete, and the access keys (Tokens) are sent to your server's Callback URL.

## **XIII. Extracting Store Data and API Testing**

Just as we did with the "Last Mile" app, we as developers must ensure the integration is successful and the received Tokens are valid:

- We use an API testing tool like **Hoppscotch** or **Postman**.

- We send a Request to the Endpoint named Retrieve Store Manager Profile, passing the Tokens in the Headers.

- Upon receiving the Response, we look inside the JSON data structure for the object named "store": { }.

- Inside this object, we will find the store_id and all other details, confirming that the integration is working perfectly, allowing us to proceed to the next step.

## **XIV. Receiving and Analyzing Fulfillment Webhooks (Critical Step)**

Simultaneously with the activation, the Zid system will send Webhook payloads to the URL you configured (e.g., webhook.site during testing). In a "Shipping & Fulfillment" app, these notifications contain highly specific variables that require close attention:

When inspecting the received Payload, we will find the basic data (like app_id, store_id, merchant's email, and phone number). However, the most crucial part is monitoring the following Events:

- **auto_dispatch_active:** Informs you that the merchant has agreed to automatically dispatch orders to you.

- **sync_product_active:** Informs you that the merchant has enabled the inventory synchronization option.

**Dynamic Service Level Updates:** Imagine the merchant later accesses the app settings and disables the "Sync Inventory" option.

- Instantly, you will receive a new Webhook carrying the event: **sync_product_deactivated**.

- If they re-enable it, you will receive: **sync_product_active**. Based on these Conditions (Webhook events), your system must programmatically adjust the "Level of Service" provided to this merchant; halting or resuming synchronization based on their real-time preference.

## **XV. Shipping Pricing and Conclusion of the Activation Phase**

Finally, through their dashboard, the merchant can access the customization section to edit or customize shipping pricing for different regions as they see fit (if you have provided them with this option).

**Summary of Achievements:** We have now fully concluded the explanation of activating the "Shipping & Fulfillment" app. We understand the Authorization mechanism, and how to receive and analyze Webhooks related to fulfillment and sync settings. In the upcoming steps, we will move to the operational side: how a new order is created, how to link inventory, and how to generate the Air Waybill (AWB) with the store to ensure the technical cycle is successfully completed.

Related Articles

- Create a shipping app or Fulfillment App

(https://help-partner.zid.sa/en/articles/8637270-create-a-shipping-app-or-fulfillment-app)

- Creation of the Last Mile Shipping App part 3

(https://help-partner.zid.sa/en/articles/15545496-creation-of-the-last-mile-shipping-app-part-3)

- Creation of the Last Mile Shipping App part 4

(https://help-partner.zid.sa/en/articles/15545553-creation-of-the-last-mile-shipping-app-part-4)

- Creating and Setting Up a Shipping & Fulfillment App - part 1

(https://help-partner.zid.sa/en/articles/15545607-creating-and-setting-up-a-shipping-fulfillment-app-part-1)

- Creating and Setting Up a Shipping & Fulfillment App - part 2

(https://help-partner.zid.sa/en/articles/15545648-creating-and-setting-up-a-shipping-fulfillment-app-part-2)
