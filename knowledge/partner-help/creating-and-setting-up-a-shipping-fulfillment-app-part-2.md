---
# Synced from https://help-partner.zid.sa/en/articles/15545648-creating-and-setting-up-a-shipping-fulfillment-app-part-2
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: ph-creating-and-setting-up-a-shipping-fulfillment-app-part-2
title: "Creating and Setting Up a Shipping & Fulfillment App - part 2"
product: zam
audience: all
status: verified
updated: 2026-06-17
source_url: https://help-partner.zid.sa/en/articles/15545648-creating-and-setting-up-a-shipping-fulfillment-app-part-2
tags: [from-docs-site, partner-help-center]
language: en
---
Continuing **Chapter Three** of our technical guide, we reach the most critical phase in setting up a "Shipping & Fulfillment" app: configuring Webhooks and initiating the beta testing phase for the application.

## **VIII. Webhooks Setup for Shipping & Fulfillment**

This stage is the programmatic nerve center for the "Fulfillment" process. Unlike the "Last Mile" app, this application requires listening to a significantly larger number of events to ensure absolute data synchronization.

When you open this screen, you will find a list divided into four main sections. You must subscribe to all of these events (around 12 events in total):

- **Order Updates:**

- As a shipping and fulfillment company, you must listen to various order statuses such as: Created, Ready, and Canceled.

- **Activation Updates:**

- Track when a merchant activates your app (App Activated) or deactivates it (App Deactivated). This is vital to know if the deactivation was forced or due to a technical issue that needs tracking.

- **Product Updates:**

- **(Mandatory and Highly Critical Section):** Includes events for when a product is Created, Updated, Deleted, or Published.

- The importance of this section lies in knowing when a merchant adds new products to sync inventory and stock quantities between your warehouse management system and the merchant's Zid store.

- **Fulfillment Options:**

- **Fulfillment Options:** A merchant may decide to use your service as "Shipping Only" and temporarily disable fulfillment; you must receive a notification for this.

- **Auto-Dispatch:** If the merchant disables this option, it means they wish to manually review and confirm orders before you dispatch them.

- **Product Sync Active/Inactive:** Notifications regarding the status of product synchronization enabled/disabled by the merchant.

**Technical Note:** You can assign a different URL for each event or use a single URL to receive all payloads. For initial testing purposes, you can use tools like webhook.site.

## **IX. Moving Forward: Commercial Agreement**

To launch your application officially (Live), you must finalize the commercial agreement:

- This is done by sending an email to the Zid Logistics team at: [email protected] .

- The Business and Partnerships team will contact you to conduct the Scoring and finalize the agreement.

- Once the agreement is complete, the Zid team will unlock the **"Send for Review"** option in your dashboard, allowing you to launch the app after testing is finished.

## **X. Linking the App to a Development Store for Testing**

As developers, you do not need to wait for the commercial agreement to conclude to test the app.

- Through the Partner Dashboard, navigate to "Development Stores". You can create up to 15 concurrent test stores.

- To access the Merchant Dashboard, use the **(Dash Access)** button.

- **Indispensable Step Before Testing:** Go to the app's (General) settings, select your Development Store, and click the **"Install"** button. (Without this step, the app will not appear in the merchant's store when searched).

## **XI. Searching for the App in the Merchant Dashboard**

After successfully linking the app:

- Log into the Merchant Dashboard (via Dash Access).

- Go to the "Logistics" section, then choose "Other Shipping Companies".

- Search for the app name you created (e.g., Test Fulfillment).

​**Warning:** The search language must match the merchant dashboard's language (search using the Arabic name if the dashboard is in Arabic, and vice versa).

Related Articles

- Create a shipping app or Fulfillment App

(https://help-partner.zid.sa/en/articles/8637270-create-a-shipping-app-or-fulfillment-app)

- Guide to Integrating Shipping Systems with the Zid Platform

(https://help-partner.zid.sa/en/articles/15544622-guide-to-integrating-shipping-systems-with-the-zid-platform)

- Creation of the Last Mile Shipping App part 3

(https://help-partner.zid.sa/en/articles/15545496-creation-of-the-last-mile-shipping-app-part-3)

- Creating and Setting Up a Shipping & Fulfillment App - part 1

(https://help-partner.zid.sa/en/articles/15545607-creating-and-setting-up-a-shipping-fulfillment-app-part-1)

- Creating and Setting Up a Shipping & Fulfillment App - part 3

(https://help-partner.zid.sa/en/articles/15545669-creating-and-setting-up-a-shipping-fulfillment-app-part-3)
