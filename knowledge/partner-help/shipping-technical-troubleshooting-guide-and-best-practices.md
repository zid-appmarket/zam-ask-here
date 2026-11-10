---
# Synced from https://help-partner.zid.sa/en/articles/17603812-shipping-technical-troubleshooting-guide-and-best-practices
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: ph-shipping-technical-troubleshooting-guide-and-best-practices
title: "Shipping Technical Troubleshooting Guide and Best Practices"
product: zam
audience: all
status: verified
updated: 2026-10-14
source_url: https://help-partner.zid.sa/en/articles/17603812-shipping-technical-troubleshooting-guide-and-best-practices
tags: [from-docs-site, partner-help-center]
language: en
---
(https://downloads.intercomcdn.com/i/o/u7vuis4c/2741330904/85587ff7453a601ce84fbe50e0c2/Gemini_Generated_Image_uspveruspveruspv.jpg?expires=1794346200&signature=fac0c08946b3deae7d24430ba94fa1b1df173d9b855a30b2cca9b88868b5da1d&req=dicjF8p9nYhfXfMW1HO4zXNQTQVQXz9jQ00QBjCSVR%2F5q%2FJc3VR%2FovyyT4ja%0A%2BH0Q60MmmPTh4McIyuk%3D%0A)

##

## I. Merchant Troubleshooting

**1. Shipping Option Not Showing at Checkout**

- **Common Cause:** This is the most frequent error. It usually happens due to:

- The app is not activated within the specific "Inventory/Warehouse" settings where the products reside.

- Geographical coverage mismatch (the city entered by the customer is not supported).

- Missing "Product Weights/Dimensions". If the shipping partner calculates rates based on weight, the option will not appear if the cart weight is zero.

- **Solution:** Review coverage settings, inventory linking, and ensure correct product weights are entered.

**2. Inventory Sync Conflicts**

- **Common Cause:** Occurs in fulfillment apps when a merchant manually adjusts stock levels in the Zid dashboard while the fulfillment app is simultaneously pushing API updates (Race Condition).

- **Solution:** Advise merchants to rely entirely on the fulfillment company's system as the (Source of Truth) for inventory, avoiding manual adjustments in Zid if Auto-Sync is enabled.

**3. Order is "Ready" but Courier Doesn't Arrive**

- **Common Cause:** The merchant disabled the "Auto-dispatch" setting, manually changed the order status to "Ready", but the shipping company received no webhook.

- **Solution:** The merchant must verify dispatch settings, or the shipping company should provide a "Manual Push Order" button within the app's UI as a fallback.

## II. Developer / Shipping Partner Troubleshooting

**1. Missed Webhooks & Timeouts**

- **The Problem:** The shipping company's server might be momentarily down or take too long to respond to Zid, resulting in a timeout and lost new order data.

- **Standard Solution:** Do not process the order immediately upon receiving the webhook. Instead, receive the payload, instantly return a `200 OK` success response to Zid (under 2 seconds), and place the payload in a Message Queue (like RabbitMQ or AWS SQS) for background processing.

**2. API Rate Limits (Error 429)**

- **The Problem:** When a developer attempts to update 500 order statuses in the same second (e.g., when a delivery truck returns to the depot), the Zid server temporarily blocks requests to protect the system.

- **Solution:** Implement an "Exponential Backoff" algorithm. If you receive a 429 error, have your system wait 1 second, retry, then wait 2 seconds, and so on.

**3. Double Order Processing (Lack of Idempotency)**

- **The Problem:** Due to a network glitch, the "Order Created" webhook might be sent twice. Without protection, your system will create two AWBs for the same order, causing financial discrepancies.

- **Solution:** Build an Idempotency mechanism using the `order_id`. Before creating a new AWB, always check your database: "Have we processed this order ID before?".

**4. Authentication Errors and Token Expiry (Error 401 Unauthorized)**

- **The Problem:** API requests fail suddenly because the Access Token has expired.

- **Solution:** Program a Cron Job that proactively refreshes the Token (using the Refresh Token) well before its expiration time and stores it securely.

## III. Proactive Best Practices for a Seamless Experience

- **Reconciliation (Fallback Polling):** Never rely 100% on webhooks. Program your system to execute an API pull every 12 hours to fetch "New Orders" from the merchant's store and compare them against your database to catch any missed orders. This is a gold standard in the popular integrations.

- **Status Mapping Table:** Order status names in your system might differ from Zid's (e.g., your system uses `In Transit` while Zid expects `inDelivery`). Create a strict Status Mapping Table to avoid sending undefined statuses that cause API errors.

- **App Dashboard & Error Logging:** Build a simple User Interface (UI) for the merchant within your app that displays Error Logs. (e.g., "We couldn't process Order #105 because the address is missing"). Empowering merchants with visibility reduces customer support tickets by over 60%.

## IV. **Integration Hurdles for Last Mile Companies**

During the integration phase, Last Mile companies primarily face challenges related to order ingestion and courier routing.

- **Incomplete or Unstructured Address Data:**

- **The Problem:** The merchant's store may rely on free-text address inputs, resulting in a Webhook payload containing street or neighborhood names unrecognized by the shipping company's routing database.

- **The Solution:** Do not rely solely on free text. Utilize map coordinates (Lat/Lng) if available in the payload, and build a validation system that gracefully rejects the order and displays a clear error message in the merchant's dashboard if the address is unidentifiable.

- **COD vs. Prepaid Logic Confusion:**

- **The Problem:** A logic bug in reading the payment type from the Webhook leads to generating an AWB with a Cash on Delivery (COD) amount for a prepaid order, creating an awkward situation for both the courier and the customer.

- **The Solution:** Rely strictly on the `payment_method` field and the `is_paid` status. The system must be programmed to automatically override the COD collection amount to (0.00) if the order status is paid, regardless of the original payment method.

- **Post-AWB Cancellations:**

- **The Problem:** The merchant cancels the order from the Zid dashboard after the shipping company has generated the AWB and dispatched a courier.

- **The Solution:** Continuously listen to the order status update Webhook (`order.status.updated`). Once a "Canceled" status is received from Zid, your system must automatically void the AWB and halt the courier to save operational costs.

**Integration Hurdles for Shipping & Fulfillment Companies**

Fulfillment applications face higher programmatic complexity because they handle Warehouse Management System (WMS) mapping and inventory control, not just parcel transit.

- **SKU & Variant Mismatch:**

- **The Problem:** The fulfillment system receives a shipping order via Webhook, but the product's SKU coming from the Zid store does not exist in the company's WMS, or child products (variants like color/size) are not mapped correctly.

- **The Solution:** Enforce a "Strict SKU Mapping" policy. Upon app installation, your system should perform an Initial Sync to map SKUs. If an order arrives with an unrecognized SKU, automatically place the order "On Hold" and alert the merchant to map it manually.

- **The `inventory_address_id` Hurdle:**

- **The Problem:** When a developer attempts to update the order status to "Ready" for a fulfillment app, the API rejects the request because the developer failed to pass Zid's inventory ID.

- **The Solution:** Upon app activation by the merchant, the developer must call the `GET /inventories` endpoint, store the merchant's `inventory_address_id` in the database, and map it to the actual physical facility ID in your system. This ID must then be passed dynamically with every status update request.

- **Reverse Inventory Sync & Rate Limiting:**

- **The Problem:** When the fulfillment center receives a massive restocking shipment from the merchant, the developer fires thousands of API calls simultaneously to update product quantities in the Zid store, leading to IP blocking due to exceeding API Rate Limits.

- **The Solution:** Use Batch Processing if the API supports it, or queue the updates using a throttling mechanism to send a safe, specific number of requests per minute.

- **Handling Bundled Products (Kits):**

- **The Problem:** The merchant sells a "Bundle" consisting of 3 different products as a single item on Zid. The fulfillment system reads it as one item and doesn't know the internal components to pick and pack.

- **The Solution:** Build a "Bundle Decomposition" feature within your system. The app must allow the merchant to map the Bundle's SKU in Zid to the multiple individual SKUs in your warehouse.

Related Articles

- Create a shipping app or Fulfillment App

(https://help-partner.zid.sa/en/articles/8637270-create-a-shipping-app-or-fulfillment-app)

- Test your app

(https://help-partner.zid.sa/en/articles/8645309-test-your-app)

- Guide to Integrating Shipping Systems with the Zid Platform

(https://help-partner.zid.sa/en/articles/15544622-guide-to-integrating-shipping-systems-with-the-zid-platform)

- Creation of the Last Mile Shipping App part 3

(https://help-partner.zid.sa/en/articles/15545496-creation-of-the-last-mile-shipping-app-part-3)

- Creating and Setting Up a Shipping & Fulfillment App - part 3

(https://help-partner.zid.sa/en/articles/15545669-creating-and-setting-up-a-shipping-fulfillment-app-part-3)
