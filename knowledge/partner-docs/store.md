---
# Synced from https://docs.zid.sa/store-1578829m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-store
title: "Store"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/store-1578829m0
tags: [from-docs-site, partner-docs]
language: en
---

> Store - Zid Docs
# Store

This page documents the **new** Vitrin store functions and shows the old Zid equivalents.

All functions are available via **`window.zid.store`**.

## List Countries #

**New:** `zid.store.countries()`

**Old:** `zid.store.settings.fetchCountries()`

**Description:** Retrieve a list of countries available in the store.

### Usage #

```
``
```

## Get Cities of a Country #

**New:** `zid.store.getCities(country_id)`

**Old:** `zid.store.settings.fetchCitiesOfCountry(countryId)`

**Description:** Retrieve a list of cities for a given country.

### Arguments #

**`country_id`** (number, required) — The ID of the country.

### Usage #

```
``
```

## Get Terms and Conditions #

**New:** `zid.store.getTermsAndCondition()`

**Old:** `zid.store.settings.fetchTermsAndCondition()`

**Description:** Retrieve the Terms and Conditions page of the store.

### Usage #

```
``
```

## Get Privacy Policy #

**New:** `zid.store.getPrivacyPolicy()`

**Old:** `zid.store.settings.fetchPrivacyPolicy()`

**Description:** Retrieve the Privacy Policy page of the store.

### Usage #

```
``
```

## Get FAQs #

**New:** `zid.store.getFaqs()`

**Old:** `zid.store.page.fetchFaqs()`

**Description:** Retrieve all Frequently Asked Questions (FAQs).

### Usage #

```
``
```

## Get Shipping and Payment #

**New:** `zid.store.getShippingAndPayment()`

**Old:** `zid.store.page.fetchShippingAndPayment()`

**Description:** Retrieve information about shipping and payment options in the store.

### Usage #

```
``
```

Modified at 2026-07-30 11:49:13

Previous

Categories

Next

Account
