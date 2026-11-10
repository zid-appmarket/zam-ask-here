---
# Synced from https://help-partner.zid.sa/en/articles/15545607-creating-and-setting-up-a-shipping-fulfillment-app-part-1
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: ph-creating-and-setting-up-a-shipping-fulfillment-app-part-1
title: "Creating and Setting Up a Shipping & Fulfillment App - part 1"
product: zam
audience: all
status: verified
updated: 2026-06-17
source_url: https://help-partner.zid.sa/en/articles/15545607-creating-and-setting-up-a-shipping-fulfillment-app-part-1
tags: [from-docs-site, partner-help-center]
language: en
---
**Creating and Setting Up a Shipping & Fulfillment App**

In this chapter, we will move on to explaining the second and more comprehensive type of shipping applications on the Zid platform: the **"Shipping & Fulfillment Application"**. This type differs from "Last Mile" as it covers the entire order lifecycle, starting from processing, warehousing, packaging, and down to the final shipment.

## **I. App Creation & Basic Data**

To begin, follow these steps from the Partner Dashboard:

- Go to the "My Apps" menu and select "Create Application".

- Choose "Shipping Application".

- Name the application (e.g., Test Fulfillment).

- Enter the basic company URLs and the Support Email.

​**Note:** It is highly important to provide an active email address, as merchants will use it to contact you if they encounter any technical or operational issues.

## **II. Choosing the App Type (Shipping & Fulfillment)**

Here we reach the pivotal step; you must select: **Shipping & Fulfillment Company**

- This option is dedicated to companies that update the order status from its inception (when created), update inventory/stock quantities, process orders, package them, and then ship them.

- This option is fundamentally different from the "Last Mile" app explained in the previous chapter.

## **III. Completing the Profile & Auth URLs**

- **Company Description & Logo:** Enter the company description in both languages and upload the Logo.

- **Special Shipping Options:** Specify whether you support refrigerated or heavy shipping.

- **Auth URLs:** Enter the Redirection URL and the Callback URL as detailed in the previous chapter (you can refer to the Zid Documentation to understand the Auth Clients mechanism). Once done, click "Save & Continue".

## **IV. Geographical Coverage Settings**

Just like in the Last Mile app, you must define your geographical coverage areas:

- **Ship From:** Select the country (e.g., Saudi Arabia) and then the cities. You can use the "Select All" option or uncheck specific cities your coverage doesn't include.

- **Ship To:** In the same manner, define the country and cities you deliver to.

## **V. Collection & Delivery Durations**

Enter the timeframes for your services (in Arabic and English):

- **Money Collection Duration:** The time taken to transfer COD amounts to the merchant.

- **Order Receiving Time:** The time taken to start processing and receiving the order.

- **Delivery Time:** The time taken to deliver the order to the customer (e.g., 1 day).

## **VI. Developer Info & Description (Important Note on Character Limits)**

- Enter the Developer Name.

- **Short Description:** Must not exceed 100 characters.

​**Technical Warning:** If you notice a red character counter (e.g., 101 or 23 extra characters), it means you have exceeded the limit. You will not be able to proceed unless you rephrase the sentence and remove excess words to keep the description under 100 characters.

- Add the detailed App Description.

## **VII. Pricing Mechanism**

We reach the pricing settings, where you have the two standard options:

- **Based on Contract:** You leave the pricing to the merchant and provide them with a direct Onboarding Link.

- **Direct Pricing:** You set fixed prices from within the app.

- You can create pricing areas; for example, Area 1 and Area 2.

- Select the cities belonging to each area and set the shipping and COD fees.

- **Remember the Golden Rule:** You cannot add the same city in two different pricing areas.

Related Articles

- Create a shipping app or Fulfillment App

(https://help-partner.zid.sa/en/articles/8637270-create-a-shipping-app-or-fulfillment-app)

- Creation of the Last Mile Shipping App part 1

(https://help-partner.zid.sa/en/articles/15545034-creation-of-the-last-mile-shipping-app-part-1)

- Creation of the Last Mile Shipping App part 2

(https://help-partner.zid.sa/en/articles/15545303-creation-of-the-last-mile-shipping-app-part-2)

- Creating and Setting Up a Shipping & Fulfillment App - part 2

(https://help-partner.zid.sa/en/articles/15545648-creating-and-setting-up-a-shipping-fulfillment-app-part-2)

- Creating and Setting Up a Shipping & Fulfillment App - part 3

(https://help-partner.zid.sa/en/articles/15545669-creating-and-setting-up-a-shipping-fulfillment-app-part-3)
