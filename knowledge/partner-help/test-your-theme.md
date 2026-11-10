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

(https://downloads.intercomcdn.com/i/o/u7vuis4c/1542467158/160a3f6ef1ccffbb8db014ac0118/image+%285%29.png?expires=1794345300&signature=a8cbf3370159eab19a430093fd274669da2badb08191812b108ea4f1b1654024&req=dSUjFM14moBaUfMW1HO4zQRtsRgzdFGCt3xbdjINPX5Qo1%2Fb%2FJdEvRoSLpT%2B%0AsSKMx5hllDmzn6S5lVw%3D%0A)

## 2. Access Your Development Store

- Go to Zid.sa (https://zid.sa/) and log in using your **Development Store credentials** (email and password).

- Alternatively, you can click **Access Dashboard** from the Partner Portal.

## 3. Prepare the Store for Testing

To simulate a fully functional storefront, set up your development store with necessary data:

- **Upload sample product file:**

- Navigate to the **Products** section and import sample products using the provided upload tool.

- This helps you verify how product cards, collections, and filters render.

(https://downloads.intercomcdn.com/i/o/u7vuis4c/1542468666/698d7e8d8cb9c2b6fdc75bd56758/image.png?expires=1794345300&signature=6569e15021944353775b953c129d68c6e75710707138b94bdd49b9b0ff62bbed&req=dSUjFM14lYdZX%2FMW1HO4ze6pZlRTgmCpyCPByyWXaPs3SIZWYuDHwFP4NmOo%0AD%2F0hyBlpZtsBbqrwV38%3D%0A)

- Activate Zid features in the store

- Enable settings such as payment gateways, shipping methods, promotions, and cart rules.

- This allows you to test theme behavior under different store configurations.

## 4. Upload Your Theme to the Store

- Visit the Zid Theme Market (https://web.zid.sa/theme-market)

- Scroll to the **bottom of the page** and click **Upload Theme**

(https://downloads.intercomcdn.com/i/o/u7vuis4c/1542469799/e972ae28669f86d61bb06ef9a08c/image.png?expires=1794345300&signature=d5a9760c82ebf679361d51047bfaba50be73e34384e802b8c98cf47d33d49571&req=dSUjFM14lIZWUPMW1HO4zUE5gtFv0Ag12qWSmCsTJY%2FBoaQ%2FXIA9JW1kB19a%0A5TqtW5Ymnr6ldk9xCEE%3D%0A)

Fill out the theme upload form:

- **Theme Name** – Choose a name that clearly identifies your theme.

- **Theme Code** – Provide a unique identifier (e.g., `custom-furniture-v1`).

- **Theme File** – Upload your `.zip` package created using the Zid Theme Packager.

(https://downloads.intercomcdn.com/i/o/u7vuis4c/1542495449/59d3b0512d8d0de812fdbdb42df9/image+%288%29.png?expires=1794345300&signature=c487a0edb2eb5617069303c1f30fb4e49ce18d608a8e8b3b8b8fdf6c74ba8719&req=dSUjFM13mIVbUPMW1HO4zb4nt20eLXpU3u9VWlpZZJDrYlkye5ZtizH87o%2Ff%0AR%2F3JrGwpQPW%2F8IZQrv8%3D%0A)

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

(https://downloads.intercomcdn.com/i/o/u7vuis4c/1542494558/b043c6761380429d77b0dfc2f572/image+%289%29.png?expires=1794345300&signature=dd086dd119c1b722f6ecf93fc62fd5a5dce8e123d8be623ef7395a81cf63ff82&req=dSUjFM13mYRaUfMW1HO4zfGERz2mhjdltsj4BihDp5w5gWJzTAgLaE2dbMLt%0AXv%2FbzUEKp%2BeMpbJK0X8%3D%0A)

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

- Create & Update Your Public Theme

(https://help-partner.zid.sa/en/articles/11471777-create-update-your-public-theme)

- Create a Private Theme

(https://help-partner.zid.sa/en/articles/11471800-create-a-private-theme)

- Publish Your Theme

(https://help-partner.zid.sa/en/articles/11471817-publish-your-theme)
