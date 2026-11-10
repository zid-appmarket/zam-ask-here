---
# Synced from https://docs.zid.sa/list-store-delivery-options
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-list-store-delivery-options
title: "List Store Shipping Methods"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/list-store-delivery-options
tags: [from-docs-site, partner-docs]
language: en
---

> List Store Shipping Methods - Zid Docs
# List Store Shipping Methods

GET

https://api.zid.sa/ v1/managers/store/delivery-options

This endpoint provides the list of all delivery options configured for the store, including custom shipping names, associated cities, and status of each shipping method. It's useful for managing delivery settings and understanding available shipping methods.

🔑Scopes

` shipping.read` - Shipping Read

## Request

Query Params

###

Header Params

###

## Responses

🟢 200 OK

application/json

Body application/json

###

🟠 401 Unauthorized

🔴 500 Internal Server error

Request Request Example

Shell

JavaScript

Java

Swift

```
` curl --location 'https://api.zid.sa/v1/managers/store/delivery-options?payload_type=simple' \
--header 'Authorization: {{Autherization}}' \
--header 'X-Manager-Token: {{Access-Token}}' \
--header 'Accept-Language: en' `
```

Response Response Example

200 - Success

```
{
"status": "object",
"delivery_options": [
{
"id": 432501,
"name": "شركة اســناد للخدمات اللوجستية",
"system_option_code": "zid_isnaad",
"select_cities": [
{
"id": 1,
"national_id": 3,
"name": "Riyadh",
"priority": 10,
"country_id": 184,
"country_name": "Saudi Arabia",
"country_code": "SA",
"ar_name": "الرياض",
"en_name": "Riyadh"
},
{
"id": 2,
"national_id": 3158,
"name": "Al Hariq",
"priority": 0,
"country_id": 184,
"country_name": "Saudi Arabia",
"country_code": "SA",
"ar_name": "الحريق",
"en_name": "Al Hariq"
},
{
"id": 3,
"national_id": 1061,
"name": "Kharj",
"priority": 0,
"country_id": 184,
"country_name": "Saudi Arabia",
"country_code": "SA",
"ar_name": "الخرج",
"en_name": "Kharj"
},
{
"id": 4,
"national_id": 828,
"name": "Diriyah",
"priority": 0,
"country_id": 184,
"country_name": "Saudi Arabia",
"country_code": "SA",
"ar_name": "الدرعية",
"en_name": "Diriyah"
},
{
"id": 5,
"national_id": 1073,
"name": "Dilam",
"priority": 0,
"country_id": 184,
"country_name": "Saudi Arabia",
"country_code": "SA",
"ar_name": "الدلم",
"en_name": "Dilam"
},
{
"id": 6,
"national_id": 669,
"name": "Duwadimi",
"priority": 0,
"country_id": 184,
"country_name": "Saudi Arabia",
"country_code": "SA",
"ar_name": "الدوادمي",
"en_name": "Duwadimi"
},
{
"id": 7,
"national_id": 270,
"name": "Zulfi",
"priority": 0,
"country_id": 184,
"country_name": "Saudi Arabia",
"country_code": "SA",
"ar_name": "الزلفي",
"en_name": "Zulfi"
},
{
"id": 8,
"national_id": 1361,
"name": "Sulayyil",
"priority": 0,
"country_id": 184,
"country_name": "Saudi Arabia",
"country_code": "SA",
"ar_name": "السليل",
"en_name": "Sulayyil"
},
{
"id": 9,
"national_id": 306,
"name": "Ghat",
"priority": 0,
"country_id": 184,
"country_name": "Saudi Arabia",
"country_code": "SA",
"ar_name": "الغاط",
"en_name": "Ghat"
},
{
"id": 10,
"national_id": 880,
"name": "Quwayiyah",
"priority": 0,
"country_id": 184,
"country_name": "Saudi Arabia",
"country_code": "SA",
"ar_name": "القويعية",
"en_name": "Quwayiyah"
},
{
"id": 11,
"national_id": 24,
"name": "Majmaah",
"priority": 0,
"country_id": 184,
"country_name": "Saudi Arabia",
"country_code": "SA",
"ar_name": "المجمعة",
"en_name": "Majmaah"
},
{
"id": 12,
"national_id": 990,
"name": "Muzahmiyah",
"priority": 0,
"country_id": 184,
"country_name": "Saudi Arabia",
"country_code": "SA",
"ar_name": "المزاحمية",
"en_name": "Muzahmiyah"
},
{

```

Modified at 2026-02-11 13:54:38

Previous

Shipping

Next

Coupons
