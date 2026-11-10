---
# Synced from https://help-partner.zid.sa/en/articles/15545303-creation-of-the-last-mile-shipping-app-part-2
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: ph-creation-of-the-last-mile-shipping-app-part-2
title: "Creation of the Last Mile Shipping App part 2"
product: zam
audience: all
status: verified
updated: 2026-06-17
source_url: https://help-partner.zid.sa/en/articles/15545303-creation-of-the-last-mile-shipping-app-part-2
tags: [from-docs-site, partner-help-center]
language: en
---

> Technical Creation of the Last Mile Shipping App and Authorization Settings part 2
Continuing **Chapter Two** of the detailed guide for setting up the Last Mile Shipping Application. After configuring the basic settings and authorization URLs, we now move to setting up coverage details, delivery times, and pricing.

## **VII. Defining Geographical Coverage (Shipping Coverage)**

In this step, you will precisely define the geographical scope covered by your shipping application:

- **Ship From:** Select the country (e.g., Saudi Arabia) and the cities from which you will collect the shipments. You can select specific cities or choose "All Cities".

- **Ship To:** Define the destinations you deliver to. Similarly, you can choose the country and all cities, or exclude specific areas that your service does not cover.

(https://downloads.intercomcdn.com/i/o/u7vuis4c/2484259785/065db23c8ddb2412e526dcc41ea2/image.png?expires=1794346200&signature=bc5d5768b1ca72d86413af78e1d03b3cee55db27146b30d99cf9124752b30d95&req=diQvEst7lIZXXPMW1HO4zdjI3vbEYl5A0OXug60dV7yeRZluK2LcH5ARqv8G%0AP%2BUR%0A)

## **VIII. Delivery & Collection Durations**

Here we define the timeframes for the provided services. Data must be entered in both Arabic and English:

- **Collection Time:** The time taken to transfer "Cash on Delivery" (COD) amounts to the merchant after collecting them from customers. This duration depends on your policy and mutual agreement.

- **Time to Receive:** The time it takes for your courier to pick up the orders from the merchant's warehouse or store (e.g., within 1 day).

- **Order Delivery Time:** The time it takes to deliver the order to the final customer (e.g., within 3 days).

## **IX. Developer Info & App Description**

Next, fill in the application interface details that will be visible to the merchant:

- **Developer Name:** The name of the service provider or company.

- **Short Description:** A brief overview of the app.

​**Very Important Warning:** The short description has a strict limit of (100 characters). If you exceed this limit, the Proceed button will disappear, and you won't be able to save. This is a common issue developers face during setup.

- **App Description:** A space to write a comprehensive and detailed description of your shipping services, supported weights, and features.

## **X. Setting Up the Pricing Mechanism**

This is one of the most crucial settings, as Zid provides two main options for determining how shipping costs are calculated:

- **Based on Contract:** In this option, you leave the freedom of setting the shipping price to the merchant within their store, based on your mutual contract. In this case, you only need to provide your company's **Onboarding Link**, where the merchant can log in and complete their account activation procedures with you.

- **Direct Pricing (From the App):** Here, you define the prices directly within the app settings to be applied automatically to orders. You will create "Customizations" as follows:

- **Zone Selection:** (e.g., Eastern Province).

- **City Selection:** Selecting the cities that fall under this zone.

- **Pricing Type:** Is it a Flat Rate or By Weight?

- **COD Fees:** Specifying additional fees if the order includes Cash on Delivery.

## **XI. Important Validation Note on Custom Pricing**

When adding multiple pricing zones (Customizations) under the "Direct Pricing" option, pay attention to an important rule: **You cannot add the same city to more than one pricing customization.** For example, if you add the city of "Al-Ahsa" to the first customization, and then try to add it again to another customization (e.g., Al-Ahsa 2), the system will throw an Error and will not allow you to save. Each city must belong to only one pricing zone.

After saving successfully, we move on to the "Webhooks" phase, which will be explained in detail in the next part.

Related Articles

- Create a shipping app or Fulfillment App

(https://help-partner.zid.sa/en/articles/8637270-create-a-shipping-app-or-fulfillment-app)

- Creation of the Last Mile Shipping App part 1

(https://help-partner.zid.sa/en/articles/15545034-creation-of-the-last-mile-shipping-app-part-1)

- Creation of the Last Mile Shipping App part 3

(https://help-partner.zid.sa/en/articles/15545496-creation-of-the-last-mile-shipping-app-part-3)

- Creation of the Last Mile Shipping App part 4

(https://help-partner.zid.sa/en/articles/15545553-creation-of-the-last-mile-shipping-app-part-4)

- Creating and Setting Up a Shipping & Fulfillment App - part 1

(https://help-partner.zid.sa/en/articles/15545607-creating-and-setting-up-a-shipping-fulfillment-app-part-1)
