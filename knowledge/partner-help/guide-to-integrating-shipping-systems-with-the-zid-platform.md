---
# Synced from https://help-partner.zid.sa/en/articles/15544622-guide-to-integrating-shipping-systems-with-the-zid-platform
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: ph-guide-to-integrating-shipping-systems-with-the-zid-platform
title: "Guide to Integrating Shipping Systems with the Zid Platform"
product: zam
audience: all
status: verified
updated: 2026-06-17
source_url: https://help-partner.zid.sa/en/articles/15544622-guide-to-integrating-shipping-systems-with-the-zid-platform
tags: [from-docs-site, partner-help-center]
language: en
---

> The Comprehensive Guide to Integrating Shipping Systems with the Zid Platform
**Introduction:** This guide serves as the primary reference for developers and new shipping companies looking to build an effective technical integration with the Zid e-commerce platform. This integration aims to automate and manage shipping and fulfillment operations seamlessly between the shipping company's system and the merchants' stores on Zid, utilizing the "Partners System".

## **I. Commercial Prerequisites**

Before writing any code, there is a fundamental administrative step that must be completed to ensure the workflow is official and legally bound:

- **Commercial Agreement:** An official agreement must be signed between the shipping company (service provider) and the logistics department at Zid.

- **Contacting Zid's Team:** This process begins by sending an email to the Partners Team via the following address: [email protected] .

- **Scoring & Evaluation:** The team will review your request and evaluate the integration idea and the services provided to initiate formal procedures.

**Note for Developers:** The application cannot be fully activated technically for stores without completing the commercial approvals from Zid's management.

## **II. Technical Integration & App Creation Steps**

Once the commercial procedures are underway, the development team can simultaneously start preparing the technical integration. The integration relies on two-way data passing between the Zid store and the shipping company's system using APIs and Webhooks.

Here are the steps to create the application in the Partner Dashboard:

- **Log in to the Partner Dashboard:** Create an account or log in to the Zid Partners Dashboard via the link: partner.zid.sa (https://partner.zid.sa/).

- **Create the Application:** From the sidebar menu, go to the "My Apps" section, then click on the "Create Application" button.

- **Select Application Type:** Choose "Shipping Application" from the available options and fill in the required basic information.

- **Define the Exact App Category (Critical Step):** You will be asked to precisely define the type of shipping service. Options include: **Fulfillment & Shipping**, or **Shipping Only / Last Mile**.

(https://downloads.intercomcdn.com/i/o/u7vuis4c/2484011263/d5009c9585501a3ead3aa217c924/image.png?expires=1794346200&signature=fa9894ad32df976f12754e304d77afcd000324a97f31f514fbfbfd8511e68893&req=diQvEsl%2FnINZWvMW1HO4zZVfc3%2BivAVvaEMVyL1YvbDWFJtkQamrfWqTqOMB%0A2bdx%0A)

**Very Important Warning:** Selecting the application type in step (4) is an **irreversible action**. Please ensure you select the exact category that matches your company's business model before saving.

## **III. Synchronization & Application Workflow**

After successfully creating the application, here is how the technical workflow operates:

- **Merchant Activation:** Your application will appear in the "Zid App Market". The merchant installs the application through their Merchant Dashboard.

- **Authorization:** Upon installation, the merchant grants your application the necessary permissions to access order data.

- **Receiving New Orders (Webhooks):** The Zid system will send real-time notifications (Webhooks) to your servers whenever there are new orders requiring shipping.

- **Order Processing (API Post):** Your system processes the order, then uses APIs to update the shipment status, upload the Air Waybill (AWB), and provide the merchant and the customer with the tracking number.

## **IV. Technical References**

To ensure a correct and error-free integration, developers must rely on the following documentation provided by Zid:

- **API Documentation:** Contains all details regarding Endpoints and Authentication methods.

- **Merchant Dashboard Guide:** To understand how the merchant views and interacts with the application.

## **V. Merchant Dashboard & Help Center**

After creating the application through the Partner Dashboard, we now move to understanding the environment in which the merchant operates. The "Merchant Dashboard" is the primary interface through which the merchant manages their orders, products, and overall store.

- **Help Center:** Zid provides a "Help Center," which is a highly important reference for developers and shipping companies before starting. This center helps you understand how the merchant manages their store and how orders are created and processed within the dashboard, giving you an accurate picture of the Order Journey and how your service will intervene.

(https://downloads.intercomcdn.com/i/o/u7vuis4c/2484007687/aa86a1a11e9b0b336480db26aef6/image.png?expires=1794346200&signature=584c87768752fdde4248340432fb004a39c035a71a1d4a3d4afb3be3aaf40f49&req=diQvEsl%2BmodXXvMW1HO4zRaSOE5UZ%2BacqRxtoMfsINoltSdgjNJBULq6z58s%0ASMRF%0A)

## **VI. Technical Documentation & APIs**

Zid provides comprehensive Technical Documentation that contains all the details of the Application Programming Interfaces (APIs). Through these interfaces, you as a developer can query specific data; for example, using a specific endpoint and passing an "Order ID" through it to retrieve all the details of that order.

## **VII. Authorization & Tokens**

This step is the technical backbone of the integration process. For your application to execute any action via the API (such as listing orders, updating order status, or sending an Air Waybill - AWB), you **must** possess valid Tokens.

**How to obtain Tokens?** These tokens are generated during the "App Activation" (Authorization Phase) by the merchant, which happens as follows:

- The merchant logs into their dashboard.

- Navigates to the "Logistics" section, then "Other Shipping Companies".

- Searches for your application (which has been reviewed and published on the App Market after signing the commercial agreement).

- Upon clicking "Activate," the merchant views the service details and grants your application the authorization to manage their orders. At this precise moment, the Tokens are sent to your system.

(https://downloads.intercomcdn.com/i/o/u7vuis4c/2484032985/d9aee5bbace16a37ad7d90b4d1fe/image.png?expires=1794346200&signature=b31a863a7e78d4586a484c0f49a55e371142f1be918eabdf1f4e4fc015b66763&req=diQvEsl9n4hXXPMW1HO4zUUpgKGn44Cr9DW4wCJU9pVdc8bfOJ3NVON7cay%2B%0As3Qp%0A)

**Note on Development Store:** During the development phase, you will be able to see and activate your test application through your own dedicated development store (linked to your account). This application will not be visible to other Zid merchants until it is fully approved and published.

## **VIII. Ready-Made Auth Code (Sample Auth Clients on GitHub)**

To facilitate and accelerate the integration process and reduce development time for the Authorization Phase, Zid provides ready-to-download code repositories via "GitHub" under the section "Sample Auth Clients". These repositories contain ready-made methods to handle the authentication protocol, saving developers significant time and effort.

Click on the image below to go to that page:

(https://docs.zid.sa/authorization#sample-oauth-clients)

## **IX. Business Documentation**

In addition to the Technical Documentation, Zid offers "Business Documentation" directed at Business Managers. This guide explains how to manage the application from an operational and financial perspective, such as:

- How to manage shipments generally.

- Details on financial settlements and Payouts. This documentation is also supplemented with light technical details to connect the operational side with the technical side.

Explore the guides (https://help-partner.zid.sa/en/collections/18315261-shipping-fulfillment)

**Summary of the Partner's Journey Overview:** With this, we have covered the comprehensive overview of the "Zid Shipping Partner" journey, starting from signing commercial agreements, to creating the application, to understanding how the merchant interacts with the app, and acquiring tokens for technical integration. In the upcoming parts, we will explain and apply each of these steps practically and in deep detail.

Related Articles

- App type and appearance

(https://help-partner.zid.sa/en/articles/8637255-app-type-and-appearance)

- Create a shipping app or Fulfillment App

(https://help-partner.zid.sa/en/articles/8637270-create-a-shipping-app-or-fulfillment-app)

- Integration and Development Cycle

(https://help-partner.zid.sa/en/articles/8716995-integration-and-development-cycle)

- Oddo Integration - Arabic session on how to connect Odoo with Zid App Market APIs

(https://help-partner.zid.sa/en/articles/12867648-oddo-integration-arabic-session-on-how-to-connect-odoo-with-zid-app-market-apis)

- New: Explore Your Partner Dashboard

(https://help-partner.zid.sa/en/articles/17731590-new-explore-your-partner-dashboard)
