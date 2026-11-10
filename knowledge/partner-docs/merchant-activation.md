---
# Synced from https://docs.zid.sa/merchant-activation
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-merchant-activation
title: "Merchant Activation"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/merchant-activation
tags: [from-docs-site, partner-docs]
language: en
---

> Merchant Activation - Zid Docs
# Merchant Activation

## Overview #

This is the process of a merchant activating payments, through Zid Payments, with your system. This happens by having a special login page for Zid merchants on the provider / partner side to provide the required information and documents in order to get onboarded.

Upon redirection to the provider's login page, Zid Payments will append the "storeId" query string parameter to the URL, which is the unique identifier for the merchant at Zid. After the onboarding of the merchant happens at the provider side (a new merchant account / record is created), the provider must share the Public/Secret Keys of the merchant with Zid Payments through this webhook Link Merchant webhook (https://docs.zid.sa/api-17956108). This can be done asynchronously; as awaiting for a response is not required here.

Also, the merchant needs to be redirected back to the Zid portal; in order to show him the success or failure result of onboarding. The redirection URLs are specified below:

For testing / staging environment:

https://testing-web.zid.sa/account/settings/payment-options/other?ThirdPartyId={thirdPartyProviderId}&status={status} (https://testing-web.zid.sa/account/settings/payment-options/other?ThirdPartyId={thirdPartyProviderId}&status={status})

For production environment:

https://web.zid.sa/account/settings/payment-options/other?ThirdPartyId={thirdPartyProviderId}&status={status} (https://web.zid.sa/account/settings/payment-options/other?ThirdPartyId={thirdPartyProviderId}&status={status})

Whereas thirdPartyProviderId is the unique ID of the payment service provider (Zid Payments assigns and provides this ID to the partner upfront before starting the integration), and status indicates the status of the onboarding and can be one of two possible values: “**success**” or “**failure**”

Modified at 2026-07-30 11:49:13

Previous

Overview

Next

Overview
