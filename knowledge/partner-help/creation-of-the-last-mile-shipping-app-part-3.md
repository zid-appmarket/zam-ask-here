---
# Synced from https://help-partner.zid.sa/en/articles/15545496-creation-of-the-last-mile-shipping-app-part-3
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: ph-creation-of-the-last-mile-shipping-app-part-3
title: "Creation of the Last Mile Shipping App part 3"
product: zam
audience: all
status: verified
updated: 2026-06-17
source_url: https://help-partner.zid.sa/en/articles/15545496-creation-of-the-last-mile-shipping-app-part-3
tags: [from-docs-site, partner-help-center]
language: en
---
we reach the final stages of setting up the "Last Mile" shipping application by configuring Webhooks and setting up the Testing Environment.

## **XII. Webhooks Setup & Activation**

This phase is absolutely crucial for ensuring real-time data synchronization between the Zid platform and your system. It is imperative to note that **you must subscribe to all required Webhook events** on this screen.

**Webhook Events for (Last Mile) Apps:** Since you have created a "Shipping Only/Delivery" app, you will see two main order-related events, in addition to the activation events:

- **Order Ready:** This notification is sent when the merchant changes the order status to "Ready" (meaning the shipment is ready to be picked up by your courier).

- **Order Canceled:** This notification is sent if the merchant cancels the order.

**How to link Webhooks:**

- Select the event (e.g., Order Ready).

- Paste your server's Webhook URL that will receive the payloads. (For temporary testing purposes, you can use open public sites like webhook.site to catch and inspect the payloads, then change the URL later to your actual production server URL).

**Activation & Deactivation Events:** These are extremely important. You must subscribe to the following events to ensure your system updates the app's status:

- **App Activated:** Sends a notification when a merchant activates your app.

- **App Deactivated:** Sends a notification if the merchant deactivates/uninstalls your app.

**Note:** To confirm you have subscribed to all required Webhooks, click the events dropdown menu; if it says (List is Empty), it means you have successfully added them all. (Note: For "Fulfillment & Shipping" apps, the number of required events is much higher, around 13 events, and skipping any of them will prevent you from testing the app).

## **XIII. Moving Forward: Commercial Partnership Agreement**

At this stage of the setup, you might wonder how to get the official app approval. For shipping applications, we don't just rely on the (Send for Review) button inside the dashboard. Instead, at this stage (or parallel to it), you must contact the logistics team via email at: [email protected] .

**Email Content:** Request a commercial agreement, clearly stating:

- The name of the app you created (e.g., Test App).

- The type of application and the services provided. The Zid Business Team will reach out to complete the scoring procedures and the commercial agreement.

## **XIV. Setting Up Development Stores for Testing**

**Good news for developers:** You don't have to wait for the commercial agreements to conclude to start testing your code! You can begin immediate testing via "Development Stores."

**Development Stores Features:**

- You can create up to **15 Concurrent Development Stores**.

- These stores are Fully Functional and come with the features of Zid's full package, allowing you to simulate all potential scenarios.

**To create a store:** Navigate to the (Development Stores) section from the left sidebar in the Partner Dashboard and create a new store (or use an existing one).

## **XV. Installing & Testing the App on the Development Store**

Now, we will link our programmed app to the test store to see how it works in action:

- From the (My Apps) section, find your app (e.g., Test App).

- Click on the installation or linking option, choose your Development Store (e.g., Ahmed Maher Store), and click (Install).

- To access the Merchant Dashboard, return to the (Development Stores) menu. Next to your store's name, you will find a **(Dash Access)** button. This button logs you directly into the Merchant Dashboard. (You can also change the store's password from this same screen).

- Inside the Merchant Dashboard (preferably switching to the new dashboard interface), go to the **"Logistics"** section, then **"Other Shipping Companies"**.

- You will find your app listed there; activate it to start receiving Authorization Tokens and Webhook payloads to your system, successfully simulating the full workflow!

Related Articles

- Guide to Integrating Shipping Systems with the Zid Platform

(https://help-partner.zid.sa/en/articles/15544622-guide-to-integrating-shipping-systems-with-the-zid-platform)

- Creation of the Last Mile Shipping App part 1

(https://help-partner.zid.sa/en/articles/15545034-creation-of-the-last-mile-shipping-app-part-1)

- Creation of the Last Mile Shipping App part 4

(https://help-partner.zid.sa/en/articles/15545553-creation-of-the-last-mile-shipping-app-part-4)

- Creating and Setting Up a Shipping & Fulfillment App - part 2

(https://help-partner.zid.sa/en/articles/15545648-creating-and-setting-up-a-shipping-fulfillment-app-part-2)

- Creating and Setting Up a Shipping & Fulfillment App - part 3

(https://help-partner.zid.sa/en/articles/15545669-creating-and-setting-up-a-shipping-fulfillment-app-part-3)
