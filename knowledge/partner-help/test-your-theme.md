---
# Synced from https://help-partner.zid.sa/en/articles/11461482-test-your-theme
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: ph-test-your-theme
title: "Test Your Theme"
product: theme_market
audience: all
status: verified
updated: 2025-05-28
source_url: https://help-partner.zid.sa/en/articles/11461482-test-your-theme
tags: [from-docs-site, partner-help-center]
language: en
---

> This article explains how to test your Zid theme before launch for both public and private themes.
# Step-by-Step: How to Test Your Theme

## 1. Create a Development Store

- Navigate to your **Partner Dashboard** → **Development Stores**.

- Click **Create Store** to generate your dedicated testing environment.

- Once created, your development store will automatically link to your partner account.

💡 Your development store behaves exactly like a merchant store but is intended solely for theme and app testing.

### Benefits of Using the Development Store

By leveraging the development store, you can:

- Identify and fix layout inconsistencies early

- Ensure your theme adheres to merchant expectations

- Catch schema/data errors before submission

- Experience your theme just like an actual merchant would

(https://downloads.intercomcdn.com/i/o/u7vuis4c/1542467158/160a3f6ef1ccffbb8db014ac0118/image+%285%29.png?expires=1795451400&signature=cf51a52cbbb5c3b6c7acf9d5ac3985a3cc3f58ba74fbd934a3a4269afd8f892f&req=dSUjFM14moBaUfMW1HO4zQRtsRk0dVWFt3xbdjINPX6j1F3E9%2FxjI1DufIMF%0AgRCh1RbWldvoU3rXVJI%3D%0A)

## 2. Access Your Development Store

- Go to Zid.sa (https://zid.sa/) and log in using your **Development Store credentials** (email and password).

- Alternatively, you can click **Access Dashboard** from the Partner Portal.

## 3. Prepare the Store for Testing

To simulate a fully functional storefront, set up your development store with necessary data:

- **Upload sample product file:**

- Navigate to the **Products** section and import sample products using the provided upload tool.

- This helps you verify how product cards, collections, and filters render.

(https://downloads.intercomcdn.com/i/o/u7vuis4c/1542468666/698d7e8d8cb9c2b6fdc75bd56758/image.png?expires=1795451400&signature=adb1ef5bb45c90491fe7e754b6396d298a310027fc6ed76327d6f5af06e4b3f8&req=dSUjFM14lYdZX%2FMW1HO4ze6pZlVUg2SuyCPByyWXaPt%2BEmCfpCHnYSFPqD4Q%0AKfkkxLVjYqTIsmozDGY%3D%0A)

- Activate Zid features in the store

- Enable settings such as payment gateways, shipping methods, promotions, and cart rules.

- This allows you to test theme behavior under different store configurations.

## 4. Upload Your Theme to the Store

- Visit the Zid Theme Market (https://web.zid.sa/theme-market)

- Scroll to the **bottom of the page** and click **Upload Theme**

(https://downloads.intercomcdn.com/i/o/u7vuis4c/1542469799/e972ae28669f86d61bb06ef9a08c/image.png?expires=1795451400&signature=b6e7e866b775f1b48e82993a616b32e0bf4a4973790d3e1cd177855678569f8e&req=dSUjFM14lIZWUPMW1HO4zUE5gtBo0Qwy2qWSmCsTJY8s2751peCyrhE7Ky1%2F%0Adg%2Fkt4ccwHapVtz6P0I%3D%0A)

Fill out the theme upload form:

- **Theme Name** – Choose a name that clearly identifies your theme.

- **Theme Code** – Provide a unique identifier (e.g., `custom-furniture-v1`).

- **Theme File** – Upload your `.zip` package created using the Zid Theme Packager.

(https://downloads.intercomcdn.com/i/o/u7vuis4c/1542495449/59d3b0512d8d0de812fdbdb42df9/image+%288%29.png?expires=1795451400&signature=4a779113093b7d1b8e5dca7e2e0e1951bb1f07600b158be78b9475ee61281f94&req=dSUjFM13mIVbUPMW1HO4zb4nt2wZLH5T3u9VWlpZZJAQdg1WILFvRpJ%2Bhifn%0AijEfUm23TaMhTgjIl0U%3D%0A)

## 5. Validate Theme Behavior

Once your theme is uploaded, begin a full-cycle test to validate using the testing cases guide (https://www.notion.so/145e2450d22280be9718ce6a426d6f12?pvs=21):

- **Visual Layout**:

- Test responsiveness across devices (mobile, tablet, desktop).

- Check alignment, spacing, fonts, and imagery.

- **Core Components**:

- Product grid, product details page, collections, search results.

- Header and footer configurations.

- Navigation menus and category filters.

- **Custom Blocks**:

- Ensure any custom HTML/Twig blocks render correctly.

- **Interactive Elements**:

- Validate button actions, sliders, tabs, collapsible sections, etc.

- **Checkout Flow**:

- Simulate a full order from cart to checkout using test data.

- **Merchant Settings Compatibility**:

- Adjust store settings and observe how your theme adapts (e.g., store logos, banners, custom CSS, RTL support).

(https://downloads.intercomcdn.com/i/o/u7vuis4c/1542494558/b043c6761380429d77b0dfc2f572/image+%289%29.png?expires=1795451400&signature=f8e1f2761940af665511d06d3e0eff3365bc5a12fd27518a5332295a95e37d67&req=dSUjFM13mYRaUfMW1HO4zfGERzyhhzNitsj4BihDp5yriWPGUooJ97qFoJtj%0ACYcPj1yneJvqhH1O3uM%3D%0A)

# **Private Themes Flow**

Private themes are not listed publicly and are used by specific stores only. There is **no need to use the Partner Dashboard** for submission or management.

## As a private theme developer, you should:

- Use the Zid theme documentation to **develop your theme**

- Test the theme as public

- Once ready, ask the **target merchant** to:

- Log in to their own store dashboard

- Go to Theme Market (https://web.zid.sa/theme-market)

- Upload the theme from the **Upload Theme** section

- The merchant can now preview and test the theme directly in their store

💡 Note: The testing flow for private themes is the same as public themes—just conducted directly inside a real store, not a dev store.

Related Articles

- Integration and Development Cycle

(https://help-partner.zid.sa/en/articles/8716995-integration-and-development-cycle)

- Theme Type and Appearance

(https://help-partner.zid.sa/en/articles/11471758-theme-type-and-appearance)

- Create a Private Theme

(https://help-partner.zid.sa/en/articles/11471800-create-a-private-theme)

- Publish Your Theme

(https://help-partner.zid.sa/en/articles/11471817-publish-your-theme)

- New: Explore Your Partner Dashboard

(https://help-partner.zid.sa/en/articles/17731590-new-explore-your-partner-dashboard)
