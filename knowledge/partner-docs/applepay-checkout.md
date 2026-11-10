---
# Synced from https://docs.zid.sa/applepay-checkout-1032876m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-applepay-checkout
title: "ApplePay Checkout"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/applepay-checkout-1032876m0
tags: [from-docs-site, partner-docs]
language: en
---

> ApplePay Checkout - Zid Docs
# ApplePay Checkout

## Overview #

We will integrate directly with Apple Pay on the web JS API: https://developer.apple.com/documentation/applepayontheweb (https://developer.apple.com/documentation/applepayontheweb)

Apple Pay JS API Version 6 will be used for Apple Pay in the checkout page (as the minimal supported version).

## Creating an Apple Pay Session #

An ApplePaySession will be initiated by Zid on the client side using the following params / ApplePayPaymentRequest object;

```
` {
currencyCode : { Merchant Currency based on country } ,
countryCode : { Merchant Country } ,
total : {
label : { Store Name } ,
amount : **
} ,
supportedNetworks : [ 'masterCard' , 'visa' , 'mada' ] , // Merchant Networks
merchantCapabilities : [ 'supports3DS' , 'supportsCredit' , 'supportsDebit' ]
} ;`
```

## Validating the merchant and obtaining merchant session #

The next step is handling the onvalidatemerchant event in the payment sheet. Here we call an API provided by the partner / provider to validate the merchant with Apple, and obtain a merchant session to be passed to completeMerchantValidation callback function defined by Apple.

Here's a detailed description of this step: Providing Merchant Validation (https://docs.zid.sa/api-17111709)

**Note:** The domain where the Apple Pay button is displayed must be registered with Apple as a prerequisite. We will do this through an API endpoint exposed by the provider.

See Register Domain (https://docs.zid.sa/api-17111260) for more details

## On Payment Authorized #

During the onpaymentauthorized event after the customer authenticates the transaction through FaceID or TouchID or whatever, an Apple payemnt token will be obtained on the client side. After obtaining the token, the payment sheet will be closed using the completePayment (https://developer.apple.com/documentation/apple_pay_on_the_web/applepaysession/1778012-completepayment) function. Then, a request will be sent to Zid Payments backend with the encrypted payment payload / token. From there, an execute payment API request will be sent to the payment provider passing the token.

`Once the payment is authorized and an execute payment request is sent to the provider, the customer should be charged immediately.`

Modified at 2026-07-30 11:49:13

Previous

ApplePay

Next

Register ApplePay Domain
