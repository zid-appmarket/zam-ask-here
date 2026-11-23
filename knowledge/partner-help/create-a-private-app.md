---
# Synced from https://help-partner.zid.sa/en/articles/17348249-create-a-private-app
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: ph-create-a-private-app
title: "Create a Private App"
product: zam
audience: all
status: verified
updated: 2026-11-12
source_url: https://help-partner.zid.sa/en/articles/17348249-create-a-private-app
tags: [from-docs-site, partner-help-center]
language: en
---

> Create and activate a private app for a single Zid store using the Partner Dashboard’s self-service flow, without contract upload, Zid review, or manual installation.
A **private app** is an application created for **one specific Zid store**. It is not listed publicly in Zid App Market and can only be activated by the merchant of the store assigned to the app.

Private apps can now be created and activated through a self-service flow. You do not need to upload a contract, submit the app for Zid review, or wait for Zid to install or activate it.

Before creating a private app, make sure your bank and business details are complete and the current **App Terms & Conditions** have been accepted.

These requirements apply to both new and existing partner accounts. Incomplete account information prevents app creation.

For detailed prerequisites, see Accepting Zid Partner Terms & Conditions (https://help-partner.zid.sa/en/articles/18346966-accepting-zid-partner-terms-conditions).

**Note:** Existing partners who never completed their bank or business details cannot create a private app until they provide the missing information.

**To create a private app:**

(https://downloads.intercomcdn.com/i/o/u7vuis4c/2804824930/c4fbd595efe4b84e100d00885a79/image.png?expires=1795451400&signature=a78055c4446b6b9fcf1049f5dbcedb05ae9fb6ed8b4ed2c2bf1698ea6e0d8517&req=dignEsF8mYhcWfMW1HO4zStSnpMVx1qEsVP%2F%2Fitmywx3LSJnaIVdK1aZxUfe%0ArPDEfAaHxe7KRGF1wug%3D%0A)

- Sign in to your Partner Dashboard (https://partners.zid.sa).

- Navigate to **Apps → All Apps**.

- Click **Create application**.

- If prompted, review the current **App Terms & Conditions**, select the acceptance checkbox, and click **Accept** to proceed.

- Select **Private** as the application type.

(https://downloads.intercomcdn.com/i/o/u7vuis4c/2804825465/cf94085249e2479586b218d1ab54/image.png?expires=1795451400&signature=9e15eb74db54e83e072f60984e07db1c02543a42c5ecfa2391a0c5894189ca87&req=dignEsF8mIVZXPMW1HO4zQJUwErIDKUeRNkOCJkXPYqqZLkeRLZCLpe9zBGJ%0AD7tO%0A)

- Enter the required technical information:

(https://downloads.intercomcdn.com/i/o/u7vuis4c/2804825851/4ac988d74a762501bf9c81818498/image.png?expires=1795451400&signature=b0c38dc5a68d461008d5fda3d987cf37a2e716fc0c9000bfdc460c29d89d1d62&req=dignEsF8mIlaWPMW1HO4zWTIYjrZDfZ1PthAvwo6lZXmEEWGxrUeH9KEQbrH%0AZl1x%0A)

- Application Name (Arabic)

- Application Name (English)

- Application URL

- Maintainer Email

- Application Scopes

- Enter the **Store ID** of the merchant who will use the app.

- Complete the application creation.

**Note:** Only the account owner or a team member with the `manage.partner.partnership.details` permission can accept the Terms & Conditions. Acceptance applies to the entire partner account, so other team members don't need to accept the same version individually.

If Zid publishes a new version, an authorized user must accept it before the account can create another application. No contract upload or manual contract approval is required.

**Important:** A private app can be connected to only one store. The system validates that the Store ID exists and that the store is not already linked to the private app.

## Store eligibility

The target store must have access to the **Private Connection** feature. If the merchant's current plan does not include Private Connection, you can still create the private app. After creation, you will receive an add-on purchase link that you can share with the merchant so they can enable Private Connection for their store.

## Configure OAuth 2.0

Private apps use the same OAuth 2.0 authentication flow as other Zid applications.

Configure your application's redirect URL and OAuth integration to:

- Request permission from the merchant.

- Receive the authorization callback.

- Receive and refresh access tokens.

For more information, see the Zid **Authorization Documentation (https://docs.zid.sa/authorization)**.

## Select application scopes

(https://downloads.intercomcdn.com/i/o/u7vuis4c/2715656345/8222a2e8ae8f215ec6da129fbdee/image.png?expires=1795451400&signature=ab087f791ef0aa3491577b3afc431ad326c05d814a509226d55735768c97a83d&req=dicmE897m4JbXPMW1HO4zaIiWLxsi8fcWkTe0dVe2wwvRQy5eBJ9ySp%2FIuvY%0ARb%2BT%2B%2B80OxaMap3kpZc%3D%0A)

Select the permissions your app requires from the **Application Scopes** section.

The merchant will see the requested scopes before activating the app and must approve them as part of the OAuth consent flow.

Private apps do not require Zid to review or approve the selected scopes before activation.

## Activate the private app

(https://downloads.intercomcdn.com/i/o/u7vuis4c/2715649632/a522e6a7b4cb121337c6fcb3f3d7/image.png?expires=1795451400&signature=96f455617fd3c37dd0b2a019c24e358394d1edc913e9ed6bcbabb6ce416d8c78&req=dicmE896lIdcW%2FMW1HO4zZtnlf3MvjhW2RBeluGSZQDVsbuTovwXn7RjRTny%0Ay24RLPFelX3Mj1pOBfg%3D%0A)

After the app is created, the Partner Dashboard displays a confirmation indicating that the app has been added and that the merchant must activate it.

You will also receive an **activation link**.

Share this activation link with the merchant of the Store ID configured for the app.

The activation link works only for the assigned store. Before activation, you can change the target Store ID if needed. After the merchant activates the app, the Store ID can no longer be changed.

## How the merchant activates the app

When the merchant opens the activation link, they can review:

- Partner name

- Application name

- Requested scopes

- Maintainer email

The merchant then activates the app and completes the standard OAuth consent flow.

Merchant activation acts as the approval for installing and connecting the private app. No additional approval or action from Zid is required.

## How to know when the app is activated

There is no separate activation status in the Partner Dashboard.

After the merchant approves the app, the standard OAuth flow redirects to your configured redirect URL and sends the authorization information required to obtain the app tokens.

Receiving the OAuth callback confirms that the merchant has activated the app.

## Webhooks

(https://downloads.intercomcdn.com/i/o/u7vuis4c/2715653541/cf72361f856e8add5fee236cd8dc/image.png?expires=1795451400&signature=b0dc5b163db29fa124c27ff6780e7d80050b021c08902cc631372c2214435825&req=dicmE897noRbWPMW1HO4zQmOGUHznzQ31pFwlRKFe2vcb8y0dFFN46SgeJvU%0AmSyzPo0pg0Krslw8L70%3D%0A)

You can configure webhooks while creating the application or later from the application's webhook settings.

(https://downloads.intercomcdn.com/i/o/u7vuis4c/2715654553/82c3c95934123664df8ccb30b0de/image.png?expires=1795451400&signature=ab5079168f947f67bac1d60936900c17c6e1152f58b89c403d0d2c753e5880ea&req=dicmE897mYRaWvMW1HO4zcI1ECFGgUcsb9bPHwA%2Fe0H1W5SBiqhZFQlyVYCn%0AvFMas1LLSrT6KDYPBq4%3D%0A)

For more information, see the Zid technical documentation for **Webhooks (https://docs.zid.sa/webhooks)**.

## Uninstalling a private app

The existing uninstall behavior remains unchanged.

When the merchant uninstalls the app:

- The application's tokens are revoked.

- The existing uninstall webhook is triggered.

## Frequently asked questions

## Can I use one private app for multiple stores?

No. Each private app is connected to **one Store ID only**.

If you need a private integration for another store, create a separate private app for that store.

## Can I change the Store ID?

Yes. You can change the target Store ID until the merchant activates the application.

After activation, the Store ID cannot be changed.

## Can another merchant use the activation link?

No. The activation link is bound to the Store ID configured for the private app.

## Does Zid need to review or install my private app?

No. Private app creation and activation are self-service.

You do not need to:

- Upload a contract.

- Submit the private app for Zid review.

- Contact Zid to install the app.

- Wait for Zid to activate it.

The merchant activates the app directly using the activation link you provide.

##

Related Articles

- App type and appearance

(https://help-partner.zid.sa/en/articles/8637255-app-type-and-appearance)

- Create a shipping app or Fulfillment App

(https://help-partner.zid.sa/en/articles/8637270-create-a-shipping-app-or-fulfillment-app)

- Integration and Development Cycle

(https://help-partner.zid.sa/en/articles/8716995-integration-and-development-cycle)

- Create a Private Theme

(https://help-partner.zid.sa/en/articles/11471800-create-a-private-theme)

- New: Explore Your Partner Dashboard

(https://help-partner.zid.sa/en/articles/17731590-new-explore-your-partner-dashboard)
