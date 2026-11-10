---
# Synced from https://help-partner.zid.sa/en/articles/8716995-integration-and-development-cycle
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: ph-integration-and-development-cycle
title: "Integration and Development Cycle"
product: zam
audience: all
status: verified
updated: 2026-10-27
source_url: https://help-partner.zid.sa/en/articles/8716995-integration-and-development-cycle
tags: [from-docs-site, partner-help-center]
language: en
---

> This article will take you thorough a tour in how to integrate your App or develop your theme in Zid.
# 1. Create a Partner Account

Before developing an app or a theme, you must create a Zid Partner account. This account gives you access to the Partner Dashboard, where you’ll manage submissions, development stores, analytics, and more.

## How to Register

- Visit Zid Developer Portal (https://partners.zid.sa)

- Click on **Sign Up**

- Fill in the required details:

- **Full Name**: Use your company name – this will be publicly visible

- **Email**: Use a fresh email not associated with any Zid store

- **Mobile**: Must be a GCC number

- **Password**: At least 8 characters, including letters and numbers

- **Country**

- **Role**: Choose whether you're a company employee or freelancer

- **App Type**: Select Public App or Private App depending on your target

- **Looking for Ideas?**: Opt-in to receive guidance

(https://downloads.intercomcdn.com/i/o/u7vuis4c/1574612163/d15f3ce7fb46a19a019875aea5b5/image+%2835%29.png?expires=1794346200&signature=6f14fa74da71ed9f99a872de36c91a52f608b5ed7c2c109d5ec036d611d626cb&req=dSUgEs9%2Fn4BZWvMW1HO4zUx1vBsqbOTnIQVPccoNlbQZOGb2iSLr4YL5TSdU%0AHFb%2Bx%2BgAr4pKFzWtfJk%3D%0A)

**Through the Partner Dashboard, you can:**

- Submit partnership details to receive your agreement to publish your App in our marketplace.

⚠️ **Note:** This process applies to **public** integrations only. For private apps or themes, please refer to the respective private integration guides.

- Build and create your applications and themes, update, monitor installations, and subscriptions.

- Create a development store, so you can test your App until you are ready to publish it apps on the market.

- Submit your App to be reviewed and listed on the market.

You can register your account in a few easy guided steps, and you can track the progress of your account completion from the dashboard.

# 2. Apps

Once registered, your journey will branch into either **Apps** or **Themes**. Each path has its own development, testing, and publishing flow depending on whether you're building a **Public** or **Private** version.

# App Types

- **Public Apps**: Available to all merchants on the Zid App Market

- **Private Apps**: Available only to specific stores with explicit access

- **Shipping Apps**: A special category of Public Apps for logistics and fulfillment services

Note: Shipping apps must be public. Private shipping apps are not supported.

## Public App Flow

- Complete Partnership Details (https://partners.zid.sa/en-sa/partner/17/partnership) to receive your agreement

- Create your application (https://help-partner.zid.sa/en/articles/8637655-create-a-public-app)

- Start development using the Zid Merchant API (https://docs.zid.sa/start-here)

- Test your app (https://help-partner.zid.sa/en/articles/8645309-test-your-application) in a development store

- Publish your app (https://help-partner.zid.sa/en/articles/8683729-publish-your-app) for Zid’s review

- Once approved, your app is listed in the Zid App Market

## Private App Flow

A private app is created for **one specific Zid store** and is not listed publicly in Zid App Market.

## Prerequisites

- The target store must have access to **Private Connection**.

- If the store’s plan does not include it, the app can still be created and an add-on purchase link can be shared with the merchant.

- Shipping apps cannot be private and must remain public.

## How it works

- Create a new application in the **Partner Dashboard (https://partners.zid.sa/)** and select **Private**.

- Enter the required technical details and the target **Store ID**.

- Develop and test your integration using the **Merchant API**.

- Share the generated activation link with the merchant.

- The merchant reviews the requested permissions and activates the app through the standard OAuth consent flow.

**No contract upload, Zid review, or manual installation by Zid is required.**

For complete setup instructions, Store ID rules, activation behavior, and detailed eligibility information, see **Create a private app (https://help-partner.zid.sa/en/articles/17348249-create-a-private-app#h_af1e3994cf)**.

# 3. Themes

# Theme Types:

- **Public Themes**: Available for all merchants in the Zid Theme Market

- **Private Themes**: Built for specific merchants and uploaded manually

## Public Theme Flow

- Complete Partnership Details (https://partners.zid.sa/en-sa/partner/17/partnership)

- Start development following the Theme Development Roadmap (https://help-partner.zid.sa/en/articles/8683883-theme-development-roadmap)

- Create and upload (https://help-partner.zid.sa/en/articles/8684798-create-a-new-theme) your theme in the dashboard

- Test your theme (https://help-partner.zid.sa/en/articles/11461482-test-your-theme) using a development store

- Submit your theme for review

- Once approved, your theme is published in the Zid Theme Market

## Private Theme Flow

Private themes are not listed publicly. They are uploaded directly to a specific store.

If you’re willing to develop a theme for one or more specific stores, so these stores are the only stores that will be able to install your theme, you’ll be involved in the following cycle:

**Prerequisites:** To install a private theme for a specific store, the store must have either a Pro or an Enterprise plan subscription in Zid. Or the user has activated Theme SDK access (https://web.zid.sa/subscriptions). To check the store's current subscription, click here (https://web.zid.sa/subscriptions).

- Build your theme using the Theme Development Roadmap (https://help-partner.zid.sa/en/articles/8683883-theme-development-roadmap)

- Test it using a development store (https://help-partner.zid.sa/en/articles/11461482-test-your-theme)

- Provide the merchant with the SDK file to upload it to the store

- To find the theme in the store

- Go to web.zi.sa (https://web.zid.sa/theme-market)

- Click on Zid Theme Market

- Scroll to the end of the page

- Upload the theme into the Custom Themes section

The testing flow is similar to public themes, but occurs inside the live merchant store.

(https://downloads.intercomcdn.com/i/o/u7vuis4c/1574616214/9ca87b57ed961930052c6dbec5d3/image+%2838%29.png?expires=1794346200&signature=1f24aae83fc4717e6fe2bda350eb66e6d42404402855fa50eb32e3651216e408&req=dSUgEs9%2Fm4NeXfMW1HO4zWTQUc%2BxW2rti8CaszMSC%2FFZfO7rmuJzZEm7%2FWmn%0AMHtarY1hKUxxgQzLQMM%3D%0A)

## Next Steps

- API Documentation (https://docs.zid.sa/start-here)

- Partner Help Center (https://help-partner.zid.sa/en)

- Join our Telegram Community (https://t.me/zidpartnersthemes)

Need help? Reach out via the support widget in your Partner Dashboard.

Related Articles

- Theme Development Cycle

(https://help-partner.zid.sa/en/articles/8683883-theme-development-cycle)

- Test Your Theme

(https://help-partner.zid.sa/en/articles/11461482-test-your-theme)

- Theme Type and Appearance

(https://help-partner.zid.sa/en/articles/11471758-theme-type-and-appearance)

- Create a Private Theme

(https://help-partner.zid.sa/en/articles/11471800-create-a-private-theme)

- Guide to Integrating Shipping Systems with the Zid Platform

(https://help-partner.zid.sa/en/articles/15544622-guide-to-integrating-shipping-systems-with-the-zid-platform)
