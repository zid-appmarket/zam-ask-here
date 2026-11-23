---
# Synced from https://help-partner.zid.sa/en/articles/8716995-integration-and-development-cycle
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: ph-integration-and-development-cycle
title: "Integration and Development Cycle"
product: zam
audience: all
status: verified
updated: 2026-11-12
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

(https://downloads.intercomcdn.com/i/o/u7vuis4c/1574612163/d15f3ce7fb46a19a019875aea5b5/image+%2835%29.png?expires=1795451400&signature=e02d54fcf10adacb86b3752f40c5ff41755b0d20bf3e4318cdc5d88a9a30c83b&req=dSUgEs9%2Fn4BZWvMW1HO4zUx1vBotbePhIQVPccoNlbSavBG8riqLqZDaYHjI%0AJn%2FfD18L279ogefl4pE%3D%0A)

**Through the Partner Dashboard, you can:**

Complete your required bank and business details and accept the current Terms & Conditions before creating apps, themes, or landing pages. These requirements apply to both new and existing partners. For detailed prerequisites and acceptance instructions, see Accepting Zid Partner Terms & Conditions (https://help-partner.zid.sa/en/articles/18346966-accepting-zid-partner-terms-conditions).

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

- Complete your required bank and business details in the Partner Dashboard (https://partners.zid.sa).

- Navigate to **Apps → All Apps → Create application**. If prompted, review the current App Terms & Conditions, select the acceptance checkbox, and click **Accept** to proceed with creating your application (https://help-partner.zid.sa/en/articles/8637655-create-a-public-app).

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

- Complete your required bank and business details, then navigate to **Apps → All Apps → Create application** in the Partner Dashboard (https://partners.zid.sa).

- If prompted, review and accept the current App Terms & Conditions, then select **Private** as the application type.

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

- Complete your bank and business details in the Partner Dashboard (https://partners.zid.sa).

- Start development following the Theme Development Roadmap (https://help-partner.zid.sa/en/articles/8683883-theme-development-roadmap)

- Click **Add theme** in the Partner Dashboard. If prompted, review the current Theme Terms & Conditions, select the acceptance checkbox, and click **Accept** to proceed with creating and uploading your theme (https://help-partner.zid.sa/en/articles/11471777-create-update-your-public-theme).

- Test your theme (https://help-partner.zid.sa/en/articles/11461482-test-your-theme) using a development store

- Submit your theme for review

- Once approved, your theme is published in the Zid Theme Market

**Note:** Terms & Conditions acceptance applies to the entire partner account. Once an authorized user accepts the current version, other team members can proceed according to their permissions. If Zid publishes a new version, it must be accepted before creating another item under the affected document type. See Accepting Zid Partner Terms & Conditions (https://help-partner.zid.sa/en/articles/18346966-accepting-zid-partner-terms-conditions) for details.

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

(https://downloads.intercomcdn.com/i/o/u7vuis4c/1574616214/9ca87b57ed961930052c6dbec5d3/image+%2838%29.png?expires=1795451400&signature=2bbb9735d13fab9f67d0e39846ba30964cc253bce97d1ad4000dca22f1c39eff&req=dSUgEs9%2Fm4NeXfMW1HO4zWTQUc62Wm3ri8CaszMSC%2FFACvNvY7amzYGk2Q15%0ADLeWX7iaWrO3KY%2Fbdeg%3D%0A)

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

- New: Explore Your Partner Dashboard

(https://help-partner.zid.sa/en/articles/17731590-new-explore-your-partner-dashboard)
