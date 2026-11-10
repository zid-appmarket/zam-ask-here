---
# Synced from https://help-partner.zid.sa/en/articles/17348249-create-a-private-app
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: ph-create-a-private-app
title: "Create a Private App"
product: zam
audience: all
status: verified
updated: 2026-10-06
source_url: https://help-partner.zid.sa/en/articles/17348249-create-a-private-app
tags: [from-docs-site, partner-help-center]
language: en
---

> Create and activate a private app for a single Zid store using the Partner Dashboard’s self-service flow, without contract upload, Zid review, or manual installation.
A **private app** is an application created for **one specific Zid store**. It is not listed publicly in Zid App Market and can only be activated by the merchant of the store assigned to the app.

Private apps can now be created and activated through a self-service flow. You do not need to upload a contract, submit the app for Zid review, or wait for Zid to install or activate it.

## Create a private app

(https://downloads.intercomcdn.com/i/o/u7vuis4c/2715611813/612e73b6b905b0857f14c260a54b/image.png?expires=1794346200&signature=fd195ce2d9c1ae6f85cb2971a2dbf34e502f5d6348e5c83c305c2b18af65af75&req=dicmE89%2FnIleWvMW1HO4zcxqixH%2BnuxJvwOVKZQtgEAMBNIG8nlcQzvyuauF%0AfqwfrMsiLOO5P2sy6ws%3D%0A)

To create a private app:

- Open the **Partner Dashboard (https://partners.zid.sa/)**.

- Go to **All Apps (https://partners.zid.sa/en-sa/partner/186/apps?page=1)**.

- Click **Create Application**.

- Select **Private** as the application type.

(https://downloads.intercomcdn.com/i/o/u7vuis4c/2715614087/74c5b9a64e5cefcd9f1946c47269/image.png?expires=1794346200&signature=bee0d44bc183cf7f141a7f7abf72d0e2dffadf6020f53c1798f8f7f776fce30a&req=dicmE89%2FmYFXXvMW1HO4zWDvsvBL3qLGZdMvvtVAEdf2G7UZYUpRMXP82P%2B8%0ANdjD%0A)

- Enter the required technical information:

(https://downloads.intercomcdn.com/i/o/u7vuis4c/2715615095/91b44a22dd4afec60a39fabb064f/image.png?expires=1794346200&signature=c6103b03ebc69304e174526d19a7432314d489ff6b0b20ed6d18a529b33f43e7&req=dicmE89%2FmIFWXPMW1HO4zRXfQjtnqZVmgcJwbjSDDW07IEFyodK0PLh0XNIs%0Arp%2FW%0A)

- **Application Name (Arabic)**

- **Application Name (English)**

- **Application URL**

- **Maintainer Email**

- **Application Scopes**

- Enter the **Store ID** of the merchant who will use the app.

- Complete the application creation.

**Note:** A private app can be connected to only **one store**. The system validates that the Store ID exists and that the store is not already linked to the private app.

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

(https://downloads.intercomcdn.com/i/o/u7vuis4c/2715656345/8222a2e8ae8f215ec6da129fbdee/image.png?expires=1794346200&signature=8b9cef8cb773ecb912758717817742230c9dfe23ae22f8ae97f0d3945e78648b&req=dicmE897m4JbXPMW1HO4zaIiWL1risDaWkTe0dVe2wzAhMXJIlosyekN2BhL%0AB19ntD14DE%2BbVafUHi4%3D%0A)

Select the permissions your app requires from the **Application Scopes** section.

The merchant will see the requested scopes before activating the app and must approve them as part of the OAuth consent flow.

Private apps do not require Zid to review or approve the selected scopes before activation.

## Activate the private app

(https://downloads.intercomcdn.com/i/o/u7vuis4c/2715649632/a522e6a7b4cb121337c6fcb3f3d7/image.png?expires=1794346200&signature=21dd7dd532232a19106d0f58de1159d1eadc08559a68a8675cc509baa7d2068f&req=dicmE896lIdcW%2FMW1HO4zZtnlfzLvz9Q2RBeluGSZQAiR1IwNH2hADa5xsfv%0AYyZJW%2Fmm0zHzHmpa%2B8Q%3D%0A)

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

(https://downloads.intercomcdn.com/i/o/u7vuis4c/2715653541/cf72361f856e8add5fee236cd8dc/image.png?expires=1794346200&signature=31c7b3e493d486f562f13363547a0168de1f3f98c13d3d9c2cdd1c13a2a7bafe&req=dicmE897noRbWPMW1HO4zQmOGUD0njMx1pFwlRKFe2uzPDhg%2Bm316mElgCM1%0AFhPLgFbzoydaqMSmTcc%3D%0A)

You can configure webhooks while creating the application or later from the application's webhook settings.

(https://downloads.intercomcdn.com/i/o/u7vuis4c/2715654553/82c3c95934123664df8ccb30b0de/image.png?expires=1794346200&signature=23c0956db29390766a1d9bbc5b42b1b32e20a53c721bd4289d3c77fc15a10632&req=dicmE897mYRaWvMW1HO4zcI1ECBBgEAqb9bPHwA%2Fe0En21UQaginRDJF2S9I%0Ahd1BM2MA0WeTgccQgqQ%3D%0A)

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

- Create a Private Theme

(https://help-partner.zid.sa/en/articles/11471800-create-a-private-theme)

- Oddo Integration - Arabic session on how to connect Odoo with Zid App Market APIs

(https://help-partner.zid.sa/en/articles/12867648-oddo-integration-arabic-session-on-how-to-connect-odoo-with-zid-app-market-apis)

- New: Explore Your Partner Dashboard

(https://help-partner.zid.sa/en/articles/17731590-new-explore-your-partner-dashboard)
