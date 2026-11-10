---
# Synced from https://help-partner.zid.sa/en/articles/8637270-create-a-shipping-app-or-fulfillment-app
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: ph-create-a-shipping-app-or-fulfillment-app
title: "Create a shipping app or Fulfillment App"
product: zam
audience: all
status: verified
updated: 2025-06-26
source_url: https://help-partner.zid.sa/en/articles/8637270-create-a-shipping-app-or-fulfillment-app
tags: [from-docs-site, partner-help-center]
language: en
---

> This article summarizes the required steps to create your a shipping or fulfillment App on the Zid App Market.
### What is the function of Zid Shipping APIs?

Zid Shipping APIs enable the integration between Zid and the logistic systems of shipping companies. As a shipping company, you can manage and automate all your operations seamlessly with Zid Merchants through the Shipping APIs.

### How does it work?

Merchants who have activated your shipping application on their store could place new orders, choose a payment method, track shipments, check supported countries and cities, and generate AWB.

To create a new application, follow these steps:

- Open your partner dashboard

- Navigate to **My Apps**

- Click the **Create Application** button.

- Choose the **Shipping Application**

- Fill in the general data:

​

(https://downloads.intercomcdn.com/i/o/893756245/47843cc57ca0dd2267a3524d/SHipping+1.png?expires=1794346200&signature=0dbf9e0a349c968abc71ccee65ef741fbb2f6971fd2d560070ffe983fb855052&req=fCkkEcx4n4VaFb4f3HP0gEPlU%2Fd0kjln%2FG3xllGBKoxNo6rpkg6jXVOayjTj%0A9sw%3D%0A)

- **company name:** The name of your App that will appear to the merchant. "make sure to write the App name in Arabic and English Language"

- **company URL:** Your main company website. started with "http://"

- **Technical support email:** The responsible email to receive and reply to merchant issues.

- **Mobile number:** The responsible phone number to receive and reply to merchant issues. "don't write a random number as it'll appear on your page and be seen by the merchants"

- **Type of shipping and storage company:** you can choose your service type category, either:

- Shipping and fulfillment company

- Shipping company only

- **About your company:** Write a brief introduction about your company and the nature of the service provided to merchants.

"make sure to write it in Arabic and English Language"

- **Company logo**

- Use this template to fit the requirements. Here (https://docs.google.com/presentation/d/1KNH2Ag5gv2yScjFYheFIBkT3nEIJFQ0w/edit?usp=sharing&ouid=110224827639058744727&rtpof=true&sd=true)

- **Services provided by the company**: if you're providing refrigerated Shipping or Heavy Shipping, this would help in identifying your services.

- Click the Create App button to move to the next step.

## 2. Implement OAuth

(https://downloads.intercomcdn.com/i/o/893758024/ddc2b353e0425c69dc646b13/Shipping+2.png?expires=1794346200&signature=44557fcdb3b0fa585288b33e41c89d85031ea435d6a5e48d87fe76cb1d2f2a03&req=fCkkEcx2nYNbFb4f3HP0gBf7kS0SxRS2BIw%2BxE%2FfskTov9icHxjcXy2g5Nel%0A%2BI2%2FM1Df%2FLZXqR6YwA%3D%3D%0A)

In this section, you can set up your OAuth. You'll be provided with your OAUTH 2.0 ENDPOINT, CLIENT ID, and CLIENT SECRET, to set up three requirements:

- Redirect URL (Ask for merchant permission)

- Callback URL (Get the tokens)

- Refresh tokens

### OAUTH 2.0

If you are not familiar with OAuth 2.0 or you need more information about OAuth 2.0, redirection, or Callback, please check our Authorization Documentation (https://docs.zid.sa/authorization)

After this, you can start integrating your system using our APIs. Check the below links.

## 3. Explore our APIs

Our Standard APIs (https://docs.zid.sa/start-here)

## 4. Shipping option details

In this section, you can set up your shipping option details to appear in your App page and be seen by the merchants.

(https://downloads.intercomcdn.com/i/o/893760116/8fa391e439fadcf481a9e9a8/Shipping+3.png?expires=1794346200&signature=c6d7baa03990da61ea9d2ec51d6c7f34e7dcc6a9db2b4f568d8ab191a865e7bd&req=fCkkEc9%2BnIBZFb4f3HP0gMFwITBRn3fg7bpq4LdIBJyTTh0RXQ2srKGlD6%2Fv%0A5GzPiA81bKa6N9zJfA%3D%3D%0A)

- **Delivery/Pickup coverage:** Select the countries and cities covered by your company

- **Collection of money:** Expected time to collect shipment amounts "In Arabic and English languages"

- **Dates for receiving and delivering orders:** "In Arabic and English languages"

- **Developed by**: write the name of the developer that will appear in the application card when it is published on the Zid app market. "In Arabic and English languages"

- **Short description:** Briefly explain to merchants how your app and the features of the app will help them. "In Arabic and English languages"

- **Shipping Weight:** Indicate the maximum weight for each shipment and the price increases for each weight gain. "In Arabic and English languages"

- **App photos &screenshots** "In Arabic and English languages" Add photos and screenshots from the application.

- Screen User interface template in PSD (https://drive.google.com/file/d/17cE-ijX7U7aJTX2xp3P_TU9ql69vlPTc/view?usp=sharing)

- Mobile User Interface template in PSD (https://drive.google.com/file/d/1Obo9dX4JRyXTdAt2HpvwVMksVqLq5HEH/view?usp=sharing)

Click on **Save & Continue**

This is how your information will be presented

## **5. Set your Activation and pricing mechanism:**

### Based on the contract

The merchant needs to request an activation and prices are according to the contract.

**Note that the merchant** will need to set up the shipping option manually from his dashboard.

(https://downloads.intercomcdn.com/i/o/893786951/2c8724dd8fb28fa5ef5aceac/Screenshot+2023-11-27+at+12.33.59%E2%80%AFPM.png?expires=1794346200&signature=f26982d18c955a01a5a114a47b9a2c96f71d7cae68fee195774175a0afd0711f&req=fCkkEcF4lIReFb4f3HP0gNFDb4ixWRnw9V2q0tIvGKx5XgGixo4r93i%2FiYDA%0AK1Tw8haJrQJnIf3b7Q%3D%3D%0A)

### Fixed price

By using this model, the merchant account will activate immediately and the prices are fixed

(https://downloads.intercomcdn.com/i/o/893785556/dd23fa10d40fdb55d0bc73f9/Shipping+4.png?expires=1794346200&signature=9642e56bb3529563889b3d2b740fa890ebf95938d0ef36916ad5489bf75c2ef3&req=fCkkEcF7mIRZFb4f3HP0gKO0v17wTXcV1245s7%2BHpfo5cNn8HLJEEiBUA4TE%0ANg2FOkttENbbEBaDqg%3D%3D%0A)

- Add customization

- Customization name

- Added countries and cities

- Activate cash on delivery

- shipping price

- Fixed price

- By weight

###

## 6. Webhook Management

The next step is to add a webhook. Through this, you can add new webhooks, and delete or edit your added ones. You can perform this action while creating your application.

**For each webhook, there are 3 fields:**

- **1. Actions list:**

- **2. Target URL**: "mandatory" is a URL used to receive the actions when occurred.

- You can have a single URL for both actions, or you can have a different URLs for each one

- **Same URL for both**: Choose both of them from the action list field, then add your URL

- **Different URLs**: Choose the needed one and add its URL then click on the Save button . Then Choose the other one and add its URL then click on the Save button .

- **3. Header**: any information you need to pass or identify.

### Webhooks

For more information about webhooks, check our technical references (https://docs.zid.sa/webhooks) Section.

### Shipping system webhooks

These webhooks are for companies that provide **only** Shipping services. As a shipping system, you're required to subscribe in **4 webhooks**. 2 for order updates, and 2 for App updates

(https://downloads.intercomcdn.com/i/o/893798406/dd3d88449bf96ca9c49b5765/webhooks+sh.png?expires=1794346200&signature=a99736ea4e000b4a9ffb5d651546878f5400e5a505b27889398859ea731a756c&req=fCkkEcB2mYFZFb4f3HP0gIte%2BK%2Bkv0LbUgKKzEvLo4Dq%2FMCHIZ7tjmSpFVJ%2B%0AcoYibgGl0UgJ1MaIMQ%3D%3D%0A)

- **Create webhooks for Order updates:**

- **order.ready** "mandatory"

- **order.canceled** "mandatory"

**2. Create Webhooks For Activation Updates**

- **app.market.application.install**: To be notified when your App is installed in the store

- **app.market.application.uninstall**: To be notified when your App is un-installed in the store

##

### Shipping and fulfillment webhooks

These webhooks are for companies that provide Shipping and Fulfillment services, such as Storage, Order processing, packaging, etc..

As a Shipping and Fulfillment company, you're required to subscribe to **13 webhooks**. 3 for order updates, 2 for App updates, 4 for products updates, and 4 for Fulfillment options

(https://downloads.intercomcdn.com/i/o/893800704/b5bfb4a7cedf39227bc01a09/ff+1.png?expires=1794346200&signature=56f588a330ace24bba9ebb9e58e02caede5ceefaec380b230c32eb02ab248e03&req=fCkkHsl%2BmoFbFb4f3HP0gC2wt6%2F9SD1vUBhAVJxziA9bH1i5rfaEAEhIrKSQ%0AOgCvQNEfG6%2FicpkZZg%3D%3D%0A)

(https://downloads.intercomcdn.com/i/o/893800796/2cbfed3ad3fede426ff85fbd/ff2+.png?expires=1794346200&signature=ea7f687baed0c979e4fdfa5b2ce6b23979c9c3e846bf6fee107b281a12b80549&req=fCkkHsl%2BmohZFb4f3HP0gCaMQW7XUiGW4U0tkAtzhVxQ3QSsIxsllRvqZ5D%2B%0AjQjRREuxexQXHR9stA%3D%3D%0A)

**1. Create webhooks for Orders updates:**

- **order.create** "New" "mandatory"

- **order.ready** "mandatory"

- **order.canceled** "mandatory"

**2. Create Webhooks For Activation Updates**

- **app.market.application.install** "mandatory" : To be notified when your App is installed in the store

- **app.market.application.uninstall***"mandatory"*: To be notified when your App is un-installed in the store

**3. Create webhooks for Products updates**

- **product.create** "mandatory" : when a new product is created in the store

- **product.delete** "mandatory" : when a product is deleted from the store

- **product.update** "mandatory" : when a product is updated in the store

- **product.publish** "mandatory" : when a product is published in the store

**4. Create Webhook For Fulfilment Options**

Merchant has the ability to enable or disable "auto-dispatching of orders and auto-syncing of products", so you'll be notified in each event if occurs. You need to subscribe in these Webhooks:

- **app.market.dispatch_orders.activate** "mandatory"

- **app.market.dispatch_orders.deactivate** "mandatory"

- **app.market.sync_product.activate** "mandatory"

- **app.market.sync_product.deactivate** "mandatory"

Here is a clear explanation about order statuses in Zid

**ORDER STATUS**

**DESCRIPTION**

**RESPONSIBILITY**

New

Order has just been placed by merchant

Merchant

Preparing

This status is between the merchant and the customer

Merchant

Ready

Once the merchant changes the status to ready, a request should be sent to the shipping company. You should subscribe to **Order List** webhook to receive the order in a specific status and send the shipping information (waybill and tracking information)

Merchant

Indelivery

Once your driver arrives at the merchant and picks up the shipment the order status should be updated to **Indelivery**.

Delivered

Once the order arrives at the customer, the order status changes to **Delivered**

Partner

Canceled

In case the customer didn't receive the shipment or returned the order status should be **Canceled**

Merchant, Partner

## All Done? Let's move to the testing phase (https://help-partner.zid.sa/en/articles/8645309-test-your-application)

Related Articles

- Create a Public App

(https://help-partner.zid.sa/en/articles/8637655-create-a-public-app)

- Guide to Integrating Shipping Systems with the Zid Platform

(https://help-partner.zid.sa/en/articles/15544622-guide-to-integrating-shipping-systems-with-the-zid-platform)

- Creation of the Last Mile Shipping App part 4

(https://help-partner.zid.sa/en/articles/15545553-creation-of-the-last-mile-shipping-app-part-4)

- Creating and Setting Up a Shipping & Fulfillment App - part 2

(https://help-partner.zid.sa/en/articles/15545648-creating-and-setting-up-a-shipping-fulfillment-app-part-2)

- Create a Private App

(https://help-partner.zid.sa/en/articles/17348249-create-a-private-app)
