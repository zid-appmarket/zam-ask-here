---
# Synced from https://docs.zid.sa/create-first-app
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-create-first-app
title: "Create your First App"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/create-first-app
tags: [from-docs-site, partner-docs]
language: en
---

> Create your First App - Zid Docs
# Create your First App

To begin creating and developing subscription apps for the Zid App Market, ensure you have a registered **partner account (https://partner.zid.sa)**. Simply log in and follow the steps outlined below. Through the Partner Dashboard, you can build apps, test them on demo stores, launch them in the Zid App Market, and unlock new revenue opportunities!

Subscription Apps

Shipping Apps

## Create Your Draft App #

Navigate to **My Apps** (https://partner.zid.sa/applications) from your Partner Dashboard. Click on **Create Application** button, and select **Private/Public Application**.

Begin by entering the basic details for your app, which will be displayed in Zid App Market to attract merchants!

Item Description

Application Name The name of your app in Arabic and English as it will appear to merchants

App Categories Choose relevant categories (max 3) to help merchants find your app

Application Language Specify the language(s) your app supports

Maintainer E-mail Provide an email address for merchant support and inquiries

Once you click on Create Application, your app will be saved as a draft. You can return and continue editing it at any time.

## Configure App General Settings #

After creating your draft app, you'll be redirected to the App Details page, where you can complete the required app configuration.

1

View Your API Keys

To authorize your app for use by merchants, you'll need to access and use the following credentials from the App Keys section: Item Description

OAuth 2.0 End-Point The authorization URL for handling OAuth requests

Client ID The unique identifier for your app

Client Secret The secret key used to authenticate your app

2

Select App Scopes

App scopes define what features and services your app can access. In this section, choose the scopes required for your app's functionality. Be sure to provide clear justifications for each scope to help the review team approve your selections.

3

Embed Your App

Embedding your app allows merchants to seamlessly interact with it directly within merchant dashboard, enhancing the user experience by minimizing the need to navigate to external pages.

Before enabling the embed feature, ensure that you have selected the **embedded apps** in the App Scopes section.

## Fill App Details #

1

Add App Links

Provide the necessary URLs to enable Zid merchants to access your application seamlessly. The following URLs are essential: Item Description

Application URL The main URL where your app is hosted and accessed by merchants

Redirection URL The URL merchants are redirected to after successfully installing your app. For embedded apps, this URL should handle the OAuth flow before redirecting the merchant to the embedded app inside Zid Merchant Dashboard.

Callback URL The URL used for communication between your app and Zid for OAuth integrations

Note for Embedded Apps

If your app is embedded, use the Redirection URL to complete the OAuth flow after installation. Once the installation and authorization flow is complete, redirect the merchant to the embedded app inside Zid Merchant Dashboard. For the embedded app redirect URL format and Hermes behavior, see Embedded Apps (https://docs.zid.sa/embedded-apps-2168216m0)

2

Fill in App Description

Add a clear and concise description of your app that highlights its key features, functionalities, and benefits to merchants. This will help merchants understand the value your app brings to their store.

3

Define App Developer

Provide information about the app developer or the development company. This allows merchants to know who is behind the app and how they can reach out for support.

4

Add Media for Your app

**Application Video:** Showcase your app through a video that demonstrates how it works and the value it provides. Supported format

Embedded YouTube video URL (e.g. https://www.youtube.com/embed/###### (https://www.youtube.com/embed/######))

**Application Pictures:** Add images that visually represent your app, its features, or interface.

You can add different images for both Arabic and English language settings. If no English-specific images are provided, the Arabic images will be used by default.

**Application Icon:** Upload a distinctive icon that will represent your app in Zid App Market and Merchant Dashboard.

5

Install on Development Stores

Set up your app on development stores after creating them, to test its functionality and ensure everything works as intended before making it publicly available.

## Manage App Webhooks #

Subscribe to the available webhooks designed to provide your with real-time update about app subscriptions. Add your target Webhook URL in where you will be receiving the events you choose to listen to.

🔗

Learn more about webhook events and their conditions here (https://apidog.com/apidoc/project-613905/doc-604945)

## Add Plans and Prices #

The final step before submitting your app for review is to define pricing plans that merchants can choose and subscribe to.

1

Select Subscription Model

Choose the appropriate subscription model for your app based on how you want to charge merchants.

**Recurring:** Merchants are charged a fixed amount at regular intervals (e.g., monthly or yearly) for continuous access to the app’s features.

**Usage-Based:** Merchants are billed based on their actual consumption of a specific resource (e.g., per order, message, or API request), with costs varying according to usage.

2

Add App Plans

To publish your app, you must create at least one pricing plan, with a maximum of four.

🔁 Recurring Plans

Adding Recurring Plan

Field Description

**Name** A clear and relevant name that highlights the plan’s features or pricing. This name will be visible to merchants.

**Duration** The length of the plan’s subscription period, defining when the merchant's access starts and ends.

**Trial Period** Optionally, offer number of days merchants can use the app for free before committing to a subscription.

**Description** A summary of what the plan offers, including any specific conditions or limitations.

**Features** List up to five key features that highlight the value of the plan.

**Price** The fixed base price for the plan.

**One-time Fee** Optionally, apply an additional fee merchants pay only once, such as an installation or setup fee.

**Offer** Optionally, apply a discount to attract new merchants by selecting an offer type and specifying the discount rate.

📶 Usage-Based Plans

Adding Usage-Based Plan

Field Description

**Name** A clear and relevant name that highlights the plan’s features or pricing. This name will be visible to merchants.

**Description** A brief overview of the plan, including what it offers, the billing cycle, and any constraints.

**Features** List up to five key features that highlight the value of the plan.

**Usage Type** The unit of measurement for usage-based billing. Merchants will be charged based on their consumption.

**Initial Cost** A one-time fee merchants must pay to activate their subscription before incurring usage-based charges.

### Manage Private Plans #

In this section, you can offer merchants the option to request custom plans if the available public plans don’t meet their needs.

**Enable Private Plans**

Activate this option to allow merchants to request tailored pricing plans directly from your app’s page in the merchant dashboard.

Partner Settings

Merchant View

**View Merchant Requests**

Receive notifications for new requests, review merchant requirements, send customized pricing offers, and track their subscription status.

Private Plans Management

**Create Plan for a Specific Store**

Click on "Add Private Plan" to send a pricing offer to a specific store. Define usage limits, pricing details, and any special terms before activating the plan.

Adding Private Plan for Store

## Request App Publish #

Once all required details are filled in, you can submit your app for Zid's review and testing. Our team will assess your app’s functionality, usability, and overall readiness before approval.

**To ensure a smooth review process, make sure your app is fully prepared:**

✅ Signed a partnership agreement.

✅ Tested on a development store to confirm all features work as expected.

✅ App platform test accounts and login credentials are ready.

✅ QA test cases prepared to assist with validation.

✅ Merchant activation steps, setup requirements, and FAQs outlined.

Once submitted, you’ll receive a notification regarding your app’s review status and estimated publish date. Ensuring your app is well-prepared will speed up approval and minimize iterations. 🚀

Modified at 2026-10-21 16:16:56

Previous

Build an app

Next

Justifying your scopes
