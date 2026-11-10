---
# Synced from https://docs.zid.sa/embedded-payment-1030692m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-embedded-payment
title: "Embedded Payment"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/embedded-payment-1030692m0
tags: [from-docs-site, partner-docs]
language: en
---

> Embedded Payment - Zid Docs
# Embedded Payment

## Load JS library script #

### Description #

A JavaScript library will be needed for embedding the provider payment form in the checkout page.

**Expected Library path**

`{ProviderUrl}/payment/embedded/credit-card.js `

### **Initializing the form** #

`this.embeddedPaymentForm.init(embeddedFormConfig);`

## Config params: #

Property Type Description

publishableApiKey Merchant public key

cardViewId string Element which the provider form will be appended to

supportedNetworks string Networks to be displayed Example: "visa,mada,amex"

style Object Styling object for the form Sample Code

## Style Sample Code #

```
` {
hideCardIcons : true ,
direction : "ltr" ,
cardHeight : 225 ,
input : {
color : "rgb(66, 67, 71)" ,
fontSize : "13px" ,
fontFamily : "inherit" ,
inputHeight : "32px" ,
inputMargin : "10px" ,
borderColor : "c7c7c7" ,
borderWidth : "1px" ,
borderRadius : "0px" ,
boxShadow : "" ,
placeHolder : {
holderName : " " ,
cardNumber : " " ,
expiryDate : "شهر / سنة" ,
securityCode : " " ,
}
} ,
label : {
display : true ,
color : formStyle && formStyle.fontColor ? formStyle.fontColor : "rgb(66, 67, 71)" ,
fontSize : formStyle && formStyle.fontSize ? formStyle.fontSize : "14px" ,
fontFamily : formStyle && formStyle.fontFamily ? formStyle.fontFamily : "inherit" ,
fontWeight : formStyle && formStyle.fontWeight ? formStyle.fontWeight : "500" ,
text : {
holderName : "الاسم على البطاقة:" ,
cardNumber : "رقم البطاقة:" ,
expiryDate : "تاريخ انتهاء البطاقة:" ,
securityCode : "الرمز الأمني (CVV):" ,
} ,
} ,
error : {
borderColor : "red" ,
borderRadius : "8px" ,
boxShadow : "0px" ,
} ,
}

`
```

## Submitting the form #

We will call a submit function in the JS library to get the payment form fields submitted.

`this.embeddedPaymentForm.submit();`

### Expected function return #

Property Type Description

token string

brand string Card type, types: • visa • master • mada • amex

funding string Types: • Credit • debit

network string Network that the payment is going to be processed on Types: • visa • master • mada • amex

country string Card country

cardBin function Bank Identification Number

lastFour string Last four digits

Modified at 2026-07-30 11:49:13

Previous

Overview

Next

Gateway Error Codes
