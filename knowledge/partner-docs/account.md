---
# Synced from https://docs.zid.sa/account-1579470m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-account
title: "Account"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/account-1579470m0
tags: [from-docs-site, partner-docs]
language: en
---

> Account - Zid Docs
# Account

This page documents the **new** Vitrin account functions and shows the old Zid equivalents.

All functions are available via **`window.zid.account`**.

## Get Account #

**New:** `zid.account.get()`

**Description:** Retrieve the current customer's account information (profile details).

**Usage**

```
``
```

## Update Account #

**New:** `zid.account.update(payload)`

**Description:** Update the current customer's profile information.

### Arguments #

**`payload`** (object, required) — The customer data to update:

**`name`** (string, required) — Customer's full name.

**`email`** (string, required) — Customer's email address.

**`is_newsletter_subscriber`** (boolean, required) — Newsletter subscription preference.

**`gender`** (string | null, optional) — Customer's gender.

**`birth_date`** (string | null, optional) — Customer's birth date.

**Usage**

```
``
```

## List Addresses #

**New:** `zid.account.addresses()`

**Old:** `zid.store.customer.fetchAddresses()`

**Description:** Retrieve all addresses associated with the current customer.

### Usage #

```
``
```

## Add Address #

**New:** `zid.account.addAddress(payload)`

**Description:** Create a new address in the customer's address book.

### Parameters #

**`payload`** (object, required) — Address creation details.

### Payload Structure #

#### Required Fields: #

**`address_district`** (string, required) — District/neighborhood name.

**`address_city_id`** (number, required) — City ID.

**`address_country_id`** (number, required) — Country ID.

#### Optional Fields: #

**`address_type`** (string, optional) — Address type (defaults to "GENERAL").

**`name`** (string, optional) — Address nickname/label.

**`mobile`** (string, optional) — Mobile phone number.

**`address_street`** (string, optional) — Street address.

**`address_formatted`** (string, optional) — Formatted full address.

**`short_address`** (string, optional) — Short address label.

**`address_lat`** (string, optional) — Latitude coordinate.

**`address_lng`** (string, optional) — Longitude coordinate.

**`is_default`** (boolean, optional) — Whether this is the default address.

**`meta`** (object, optional) — Additional metadata containing:

**`city_name`** (string, optional) — City name.

**`postcode`** (string, optional) — Postal code.

**`building_number`** (string, optional) — Building number.

**`additional_number`** (string, optional) — Additional/unit number.

### Example Payload #

```
` {
"address_district" : "Downtown" ,
"address_city_id" : 123 ,
"address_country_id" : 456 ,
"address_type" : "HOME" ,
"name" : "My Home Address" ,
"mobile" : "+1234567890" ,
"address_street" : "123 Main Street" ,
"address_formatted" : "123 Main Street, Downtown, City" ,
"short_address" : "123 Main St" ,
"address_lat" : "40.7128" ,
"address_lng" : "-74.0060" ,
"is_default" : true ,
"meta" : {
"city_name" : "New York" ,
"postcode" : "10001" ,
"building_number" : "123" ,
"additional_number" : "Apt 4B"
}
} `
```

### Minimal Required Payload #

```
` {
"address_district" : "Downtown" ,
"address_city_id" : 123 ,
"address_country_id" : 456
} `
```

### Usage #

```
``
```

**Key Points:**

`address_district`, `address_city_id`, and `address_country_id` are **required**

`address_lat` and `address_lng` are **strings**, not numbers

Fields like `postcode`, `building_number`, `additional_number`, and `city_name` go inside the `meta` object

## Edit Address #

**New:** `zid.account.editAddress(address_id, payload)`

**Old:** (Likely `zid.store.customer.updateAddress()` or similar)

**Description:** Update an existing address in the customer's address book.

### Parameters #

**`address_id`** (number, required) — The ID of the address to update.

**`payload`** (object, required) — Address update details.

### Payload Structure #

#### Required Fields: #

**`address_district`** (string, required) — District/neighborhood name.

**`address_city_id`** (number, required) — City ID.

**`address_country_id`** (number, required) — Country ID.

#### Optional Fields: #

**`address_type`** (string, optional) — Address type (defaults to "GENERAL").

**`name`** (string, optional) — Address nickname/label.

**`mobile`** (string, optional) — Mobile phone number.

**`address_street`** (string, optional) — Street address.

**`address_formatted`** (string, optional) — Formatted full address.

**`short_address`** (string, optional) — Short address label.

**`address_lat`** (string, optional) — Latitude coordinate.

**`address_lng`** (string, optional) — Longitude coordinate.

**`is_default`** (boolean, optional) — Whether this is the default address.

**`meta`** (object, optional) — Additional metadata containing:

**`city_name`** (string, optional) — City name.

**`postcode`** (string, optional) — Postal code.

**`building_number`** (string, optional) — Building number.

**`additional_number`** (string, optional) — Additional/unit number.

### Example Payload #

```
` {
"address_district" : "Downtown" ,
"address_city_id" : 123 ,
"address_country_id" : 456 ,
"address_type" : "HOME" ,
"name" : "My Home Address" ,
"mobile" : "+1234567890" ,
"address_street" : "123 Main Street" ,
"address_formatted" : "123 Main Street, Downtown, City" ,
"short_address" : "123 Main St" ,
"address_lat" : "40.7128" ,
"address_lng" : "-74.0060" ,
"is_default" : true ,
"meta" : {
"city_name" : "New York" ,
"postcode" : "10001" ,
"building_number" : "123" ,
"additional_number" : "Apt 4B"
}
} `
```

### Minimal Required Payload #

```
` {
"address_district" : "Downtown" ,
"address_city_id" : 123 ,
"address_country_id" : 456
} `
```

**Key Points:**

`address_district`, `address_city_id`, and `address_country_id` are **required**

`address_lat` and `address_lng` are **strings**, not numbers

Fields like `postcode`, `building_number`, `additional_number`, and `city_name` go inside the `meta` object

## Delete Address #

**New:** `zid.account.deleteAddress(address_id)`

**Description:** Delete a specific address from the customer's address book.

### Arguments #

**`address_id`** (number, required) — The ID of the address to delete.

**Usage**

```
``
```

## Get Wishlists #

**New:** `zid.account.wishlists(params?)`

**Description:** Retrieve the customer's wishlist items with optional pagination and share token support.

### Arguments #

**`params`** (object, optional) — Optional parameters:

**`share_token`** (string) — Token to view a shared wishlist.

**`page`** (number) — Page number for pagination.

**`page_size`** (number) — Number of items per page.

**Usage**

```
``
```

## Add to Wishlist #

**New:** `zid.account.addToWishlists(payload)`

**Description:** Add one or more products to the customer wishlist.

### Arguments #

**`payload`** (object, required) — `{ product_ids: string[] }`

### Usage #

```
``
```

## Share Wishlist #

**New:** `zid.account.shareWishlist()`

**Description:** Generate a shareable link for the current wishlist.

### Usage #

```
``
```

## Remove from Wishlist #

**New:** `zid.account.removeFromWishlist(product_id)`

**Old:** `zid.store.customer.removeFromWishlist(product_id)`

**Description:** Remove a product from the customer wishlist.

### Arguments #

**`product_id`** (string, required) — The product ID

### Usage #

```
``
```

## Get Orders #

**New:** `zid.account.orders(params?)`

**Description:** Retrieve the customer's order history with optional pagination.

### Arguments #

**`params`** (object, optional) — Optional pagination parameters:

**`page`** (number) — Page number for pagination.

**`page_size`** (number) — Number of orders per page.

**Usage**

```
``
```

Modified at 2026-07-30 11:49:13

Previous

Store

Next

Blogs
