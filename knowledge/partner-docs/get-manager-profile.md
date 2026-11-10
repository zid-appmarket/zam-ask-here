---
# Synced from https://docs.zid.sa/get-manager-profile
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-get-manager-profile
title: "Retrieve Store Manager Profile"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/get-manager-profile
tags: [from-docs-site, partner-docs]
language: en
---

> Retrieve Store Manager Profile - Zid Docs
# Retrieve Store Manager Profile

GET

https://api.zid.sa/ v1/managers/account/profile

Retrieves the profile data of the authenticated Manager. This includes detailed information about the Manager, their role, associated store, and the set of permissions they hold.

This operation is exclusively for users with the Manager role (Store Owner, Store Moderator). Customer roles are not allowed to access this endpoint.

The system identifies the Manager and the related store via the `X-Manager-Token`. The `Authorization` token validates the user's access to the API.

For a detailed explanation of user roles and permissions, refer to our User Roles and Permissions guide.

🔑Scopes

`account.read` - Account Read

## Request

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
` curl --location 'https://api.zid.sa/v1/managers/account/profile' \
--header 'Accept: application/json' \
--header 'Authorization: {{Autherization}}' \
--header 'X-Manager-Token: {{Access-Token}}' \
--header 'Accept-Language: en' `
```

Response Response Example

200 - Success

```
{
"status": "object",
"user": {
"id": 3,
"old_id": 3,
"uuid": "6675a8a4-ad6e-4663-b53e-6852e63f48c7",
"name": "John",
"username": "os1987@yahoo.com",
"email": "os1987@yahoo.com",
"email_pending_confirmation": null,
"is_email_verified": true,
"mobile": "966500000005",
"mobile_pending_confirmation": null,
"mobile_object": {
"country_code": "966",
"mobile": "500000005"
},
"gender": "m",
"language_code": "ar",
"intercom_user_hash": "a117640eacd50906970d5371a56c450dfe72ddf39f36d14bb2fab2c28df45fc1",
"vloops_ref_code": "Wq2Gcr2",
"user_profile_data": {
"birth_date": "1987-05-05",
"country_id": 184,
"city_id": 1,
"city": {
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
"country": {
"id": 184,
"name": "Saudi Arabia",
"priority": 1,
"code": "SA",
"country_code": "SAU",
"flag": "https://media.zid.store/static/sa.svg"
},
"is_organization_employee": true,
"working_organization_name": null,
"job_title": null
},
"md_session_lifetime": 30,
"business_location": {
"country": {
"id": 184,
"name": "Saudi Arabia",
"priority": 1,
"code": "SA",
"country_code": "SAU",
"flag": "https://media.zid.store/static/sa.svg"
},
"city": {
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
"district": "1",
"street": "1",
"building_no": "1",
"postal_code": "1",
"additional_postal_code": "1",
"lat": "24.736143",
"lng": "46.717257",
"short_address": null,
"show_location": false,
"national_address_certificate": "https://s3-eu-west-1.amazonaws.com/private.zid.store/d297fb8b-c322-412e-a2f4-ffa96dc57022/14243022-9a65-4896-958b-e414224401ae.jpg?X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAXOL3MW23XIWBH54F%2F20260406%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260406T085453Z&X-Amz-SignedHeaders=host&X-Amz-Expires=86400&X-Amz-Signature=14459e9ebdf2e8836466e4e0d0ef01e840e67bad6a1895b6607c0c33ee741a29",
"is_address_confirmed": true
},
"roles": [
{
"id": "9b91f2fe-a7c6-4791-8e3d-b6f860f452eb",
"slug": "store.owner",
"name": "Store Owner"
}
],
"permissions": [
{
"id": "00a11d98-c5aa-49ae-8ffe-67739484119f",
"slug": "products.trash.bin",
"name": "Browse Trash Bin",
"description": "",
"order": 12,
"relies_on": [
"products.view"
],
"package_restrictions": []
},
{
"id": "00b8e1b6-3a44-4225-863e-144b9c870e53",
"slug": "automatic.messages.manage",
"name": "Manage Automatic messages",
"description": "",
"order": 24,
"relies_on": [
"automatic.messages.view"
],
"package_restrictions": []
},
{
"id": "013c118e-05a5-4af2-914f-d1a1bb9d128f",
"slug": "abandoned.carts.export",
"name": "Export",
"description": "Export Abandoned Carts",
"order": 19,
"relies_on": [
"abandoned.carts.view"
],
"package_restrictions": [
{
"package_key": "new_professional",
"names": "Professional"
},
{
"package_key": "business",
"names": "Essential"
},
{
"package_key": "growth",
"names": "Growth"
},
{
"package_key": "professional",

```

Modified at 2026-08-11 08:52:33

Previous

📄 User Roles and Permissions

Next

Retrieve VAT Settings
