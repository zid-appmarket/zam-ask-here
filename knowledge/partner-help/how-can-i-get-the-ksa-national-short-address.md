---
# Synced from https://help-partner.zid.sa/en/articles/12981222-how-can-i-get-the-ksa-national-short-address
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: ph-how-can-i-get-the-ksa-national-short-address
title: "How can I get the KSA national short address?"
product: zam
audience: all
status: verified
updated: 2025-12-21
source_url: https://help-partner.zid.sa/en/articles/12981222-how-can-i-get-the-ksa-national-short-address
tags: [from-docs-site, partner-help-center]
language: en
---
(https://downloads.intercomcdn.com/i/o/u7vuis4c/1896193327/f68dd7484d1b7c858f5940427755/Partner+Update.png?expires=1794345300&signature=d297cee56899734de874f029268ae24375e3fcb522c63a4c7b8bcd337c7c312c&req=dSguEMh3noJdXvMW1HO4zeSOXOOobiGR6oL33WNP442sGiH%2ByZ1r%2FfMu5ayF%0AB7NwCteQyi%2FAkpduia0%3D%0A)

In compliance with the Kingdom of Saudi Arabia’s Logistics Mandate, all shipments within KSA must utilize the **National Short Address** (e.g., `RCTA4483`). To ensure successful Waybill (AWB) generation and delivery rates, Zid ensured exposing these fields clearly for both the **Origin** (Merchant Inventory) and **Destination** (Customer Location).

## **Data Mapping**

You will receive the Short Address dat via our standard webhooks (https://docs.zid.sa/webhook-events-order) (`order.create`, `order.status.update`) or via Polling (List (https://docs.zid.sa/list-of-orders)/Retrieve (https://docs.zid.sa/retrieve-order-12479054e0) Orders).

Please map the following fields from the Zid payload to your AWB generation logic:

**Address Type**

**Purpose**

**Payload Path**

**JSON Key**

Destination

Customer Delivery

shipping.address

short_address

Origin

Merchant Pickup

inventory_address

short_address

## **Payload Snippet**

Below is a focused view of the JSON structure highlighting where to find the required data.

The `short_address` is an alphanumeric string (e.g., RCTA4483).

```
{

"shipping": {

"method": { ... },

"address": {

"formatted_address": "4483 الشيخ سلمان بن حمد ال خليفة - حي الضباط",

"street": "الخامس و سادس",

"district": "الجزيره",

"lat": 24.6770905,

"lng": 46.724061,

// 📍 DESTINATION SHORT ADDRESS (Customer)

"short_address": "RCTA4483",

"meta": null,

"city": {

"id": 1,

"name": "الرياض"

},

"country": {

"id": 184,

"name": "السعودية"

}

}

},

"inventory_address": {

"id": "731f3180e9254c6b827f425f58f29c31",

"name": "Default - الافتراضي",

"city": { ... },

"full_address": "RMFB4155، 4155 ابي الحسن بن المبارك، 7831، حي المصفاة، الرياض 14528، السعودية",

"street": "RMFB4155، 4155 ابي الحسن بن المبارك، 7831، حي المصفاة، الرياض 14528، السعودية",

// 📍 ORIGIN SHORT ADDRESS (Merchant Inventory)

"short_address": "RMFB4155",

"district": "",

"postal_code": null,

"coordinates": {

"lat": 24.51753521164098,

"lon": 46.89878643217163

},

"cop_enabled": false,

"is_pickup_option": false,

"is_zidship_default": true,

"working_hours": []

}

}
```

## **Rollout Strategy & Flow**

We are managing the transition on the Merchant/Customer side to ensure data availability for you.

### **Phase 1: Merchant Inventory (Origin)**

- We enabled the Short Address field for merchant inventory settings in early October.

- **Current State:** +20% of active merchants have already updated their warehouse locations.

### **Phase 2: Customer Checkout (Destination)**

- We are continuously encouraging merchants to enable "Pin on Map" or "National Address Input" at the checkout for KSA customers.

- This automatically resolves the `short_address` based on the coordinates or user input.

### **Phase 3: Validation & Error Handling**

- **Your System:** If your system requires the Short Address and it is missing, the AWB generation request should fail.

- **Our System:** We will display an error to the merchant if order lacks short address and before generating a shipping label, prompting them to manually fix the address.

## **FAQ: Operational & Edge Cases**

### **Will every single order contain a Short Address?**

Ideally yes, but practically no. While we enforce it at checkout, merchants have the ability to:

- Disable the Short Address requirement in their store settings (we warn them of the risk, but they have the toggle).

- Manually create orders with incomplete data.

- Have legacy data from before the mandate.

### **How should we handle orders missing the Short Address?**

If the shipment is Domestic KSA and the Short Address is null/empty:

- You can generate a dummy address and request manual update from customer/merchant.

- You can reject the shipment creation with a specific validation error (e.g., "Missing National Short Address" ) so that the merchant can update and retry.

### **Can we rely solely on Lat/Long coordinates?**

The mandate explicitly requires the **Short Address code** for compliance and sorting efficiency. However, you can utilize the provided **Latitude/Longitude** coordinates as a fallback mechanism to look up the Short Address if the direct value is missing.

## **Next Steps for Partners**

- **Update your mapping:** Point your integration to ingest `shipping.address.short_address` and `inventory_address.short_address`.

- **Update your validation:** Ensure your system checks for these fields for KSA shipments and returns clear errors if missing.

- **Drive Merchant Awareness:** Please proactively communicate with your merchant base. Encourage them to update their **Inventory Locations** and warn them against disabling the **Short Address** field in their checkout settings. This is critical to prevent shipment rejections and operational delays.

Related Articles

- How can i get the tokens ?

(https://help-partner.zid.sa/en/articles/8513579-how-can-i-get-the-tokens)

- Shipping Technical Troubleshooting Guide and Best Practices

(https://help-partner.zid.sa/en/articles/17603812-shipping-technical-troubleshooting-guide-and-best-practices)
