---
# Synced from https://help-partner.zid.sa/en/articles/15545034-creation-of-the-last-mile-shipping-app-part-1
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: ph-creation-of-the-last-mile-shipping-app-part-1
title: "Creation of the Last Mile Shipping App part 1"
product: zam
audience: all
status: verified
updated: 2026-06-17
source_url: https://help-partner.zid.sa/en/articles/15545034-creation-of-the-last-mile-shipping-app-part-1
tags: [from-docs-site, partner-help-center]
language: en
---

> Technical Creation of the Last Mile Shipping App and Authorization Settings
In this new chapter, we will begin the practical execution of creating a "Last Mile" or "Shipping Only" application via the Partner Dashboard.

## **I. Initiating App Creation and Entering Basic Data**

To start creating your application, follow these steps within the Partner Dashboard:

- Navigate to the "My Apps" section from the sidebar menu.

- Click on the "Create Application" button.

- Enter the application name (for example: "Test App" or "New Shipping App").

- Enter the basic company data, which includes:

- The company's official Website Link.

- The official contact Email.

- The company's Phone Number.

- The Application Website link. (It is always highly recommended to use the real and official links and data of your company, especially when the application is ready to go Live).

## **II. Accurately Defining the App Type (A Pivotal Step)**

This is the most critical point in this phase, as the selection here will dictate all the upcoming stages in the application setup. You will have two main options:

- **Shipping & Fulfillment:** This is the more comprehensive type, covering the entire order cycle starting from Order Processing, Packaging, down to final delivery.

- **Shipping Company Only / Last Mile:** This is dedicated to shipping companies whose role is strictly limited to delivery; meaning the shipping company's representative goes to pick up the ready and packaged shipment from the merchant to deliver it directly to the customer or buyer.

**Very Critical Warning:** We reiterate that this step is **Irreversible**. If you choose the wrong type that does not align with your company's Business Model, you will be forced to recreate a new application from scratch. You must accurately define the service type based on what your company provides.

(https://downloads.intercomcdn.com/i/o/u7vuis4c/2484177342/2b582432b5a534129598e08a276f/Screenshot+2026-06-17+213213.png?expires=1794346200&signature=08586affc5c14d671ae8e78209ed6857b50d521e9771fca2823d4d960d2b3ed5&req=diQvEsh5moJbW%2FMW1HO4zdrBgQGRAAuztOx9KEUXGUQ9%2Bd9%2F%2BNL%2FIDzWtLrA%0AiLDwx1dOTiQaWqrdr7g%3D%0A)

## **III. Additional Details (Description, Logo, and Shipping Type)**

After determining the application type, we move on to completing the application's profile:

- **About the Company:** Write an accurate description reflecting the company's services in both Arabic and English.

- **Logo:** Upload the official image or logo of the shipping company.

- **Special Shipping Options:** You will find important options to specify the nature of shipping your company supports:

- **Refrigerated Shipping**.

- **Heavy Shipping**. If your company supports these types, activate them (check the box) next to them. If they are not available, leave them unchecked.

(https://downloads.intercomcdn.com/i/o/u7vuis4c/2484181269/53b1447af8909090a78e1e747f62/image.png?expires=1794346200&signature=bb902b2ecf35b15d89a2e726c6ff7ab6fe2f042e780fff7d4190189784661ea6&req=diQvEsh2nINZUPMW1HO4zbatP%2BrRnCHEkhgsVkuhVlhiaJsJd0T0W3ABVojQ%0AjwOg%0A)

## **IV. Setting Up Authorization URLs**

After completing the basic setup for the Last Mile shipping app, we move to the technical steps common to most applications, which is setting up the redirection and callback URLs for the Authorization process. This requires using your application's Client ID and Client Secret.

In this step, you must enter two highly important URLs to execute and receive the Authorization process:

- **Redirection URL**.

- **Callback URL**.

(You can refer to the Zid API Documentation under the Authorization section to learn how to build these links and how they work, or use the ready-made "Sample Auth Clients" explained in the previous chapter).

(https://downloads.intercomcdn.com/i/o/u7vuis4c/2484182395/f5ed353d2193cdb69ee88b41ee23/image.png?expires=1794346200&signature=3b16987cdab270a31e82bee054c650e8c5b3dd8db6b8cfc564dd318984d4ada4&req=diQvEsh2n4JWXPMW1HO4zT2AVmcZorIT5i2Sa4HjZVdpnRIfnRHIWaqiUxjI%0AnKyfCxBGuMe5nEAXOFs%3D%0A)

## **V. Using Tunneling Services for Local Development**

Since the URLs required in the previous step (Redirection & Callback) must be public, internet-accessible links to receive responses from Zid's servers, you might face an issue if you are programming and developing the application locally on your machine (Localhost).

To solve this issue and complete the authorization process during development, it is **highly recommended** to use Cloud Tunneling Services such as:

- **ngrok** tool

- **Cloudflare Tunnels** tool These tools provide you with a temporary public URL that routes requests directly to your local server (Localhost) for processing.

## **VI. Linking the App to a Development Store**

The final step on this screen is choosing the Development Store you previously created from the Partner Dashboard to test the application on. You can do this step now, or postpone it since the application settings (like Webhooks) are not yet fully completed, which will be explained in detail in the next part.

(https://downloads.intercomcdn.com/i/o/u7vuis4c/2484194053/0f4418cf834ac99453167b383936/image.png?expires=1794346200&signature=a1a5e09945fbda0cf0b8a29bb3caa5050a047208310f419220bd9e2ef93687e0&req=diQvEsh3mYFaWvMW1HO4zcw5pjkfl3gYPVqb6Qa9xAmnqZ3mD9cFG5OPergO%0A3DUPRfG2dfc9w%2B3Eizw%3D%0A)

Related Articles

- Create a shipping app or Fulfillment App

(https://help-partner.zid.sa/en/articles/8637270-create-a-shipping-app-or-fulfillment-app)

- Creation of the Last Mile Shipping App part 2

(https://help-partner.zid.sa/en/articles/15545303-creation-of-the-last-mile-shipping-app-part-2)

- Creation of the Last Mile Shipping App part 3

(https://help-partner.zid.sa/en/articles/15545496-creation-of-the-last-mile-shipping-app-part-3)

- Creation of the Last Mile Shipping App part 4

(https://help-partner.zid.sa/en/articles/15545553-creation-of-the-last-mile-shipping-app-part-4)

- Creating and Setting Up a Shipping & Fulfillment App - part 1

(https://help-partner.zid.sa/en/articles/15545607-creating-and-setting-up-a-shipping-fulfillment-app-part-1)
