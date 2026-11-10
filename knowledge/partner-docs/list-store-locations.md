---
# Synced from https://docs.zid.sa/list-store-locations
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-list-store-locations
title: "List Locations"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/list-store-locations
tags: [from-docs-site, partner-docs]
language: en
---

> List Locations - Zid Docs
# List Locations

GET

https://api.zid.sa/ v1/locations/

Returns a list of all store locations.

**Note:**

This endpoint returns summary data only (`id` and `short_address`).

To view full location details including `name`, `address`, `coordinates`, etc., please use the Get Store Location by ID (https://docs.zid.sa/get-store-location-by-id)

endpoint.

🔑Scopes

`inventories.read` - Inventories Read

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
` curl --location 'https://api.zid.sa/v1/locations/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Authorization: {{Autherization}}' \
--header 'Store-Id: {{StoreId}}' \
--header 'Role: Manager' \
--header 'Accept-Language: en' `
```

Response Response Example

200 - Success

```
` {
"next" : null ,
"previous" : null ,
"count" : 14 ,
"active_locations_limit" : 1036 ,
"active_locations_count" : 11 ,
"results" : [
{
"id" : "8ee590fe-d02d-4c50-9184-f628bb8b115a" ,
"name" : {
"ar" : "الرياض - فرع عبد العزيز"
} ,
"city" : {
"id" : 1 ,
"name" : "Riyadh" ,
"ar_name" : "الرياض" ,
"country" : {
"id" : 184 ,
"name" : "Saudi Arabia" ,
"ar_name" : "السعودية" ,
"iso_code_2" : "SA" ,
"iso_code_3" : "SAU" ,
"code" : "SA"
} ,
"country_code" : "SA"
} ,
"type" : "PHYSICAL" ,
"coordinates" : {
"latitude" : 24.77208405941104 ,
"longitude" : 46.66803359985352
} ,
"full_address" : "6137 King Abdul Aziz Branch Rd, An Nafal, Riyadh 13312, Saudi Arabia" ,
"short_address" : null ,
"district" : "King Abdul Aziz" ,
"street" : "نفال" ,
"fulfillment_priority" : 9 ,
"is_default" : false ,
"is_private" : false ,
"is_enabled" : true ,
"has_stocks" : true ,
"channels" : [
"pos" ,
"catalog"
] ,
"linked_users" : [
{
"user_uuid" : "6675a8a4-ad6e-4663-b53e-6852e63f48c7" ,
"full_name" : "Osama"
}
]
} ,
{
"id" : "cbcd24ce-5600-4b51-bf75-4d2020e2b9e9" ,
"name" : {
"ar" : "مخزن الرياض - فرع السلي"
} ,
"city" : {
"id" : 1 ,
"name" : "Riyadh" ,
"ar_name" : "الرياض" ,
"country" : {
"id" : 184 ,
"name" : "Saudi Arabia" ,
"ar_name" : "السعودية" ,
"iso_code_2" : "SA" ,
"iso_code_3" : "SAU" ,
"code" : "SA"
} ,
"country_code" : "SA"
} ,
"type" : "PHYSICAL" ,
"coordinates" : {
"latitude" : 24.66667439068546 ,
"longitude" : 46.80931091308594
} ,
"full_address" : "RQYA7651, 7651 Wadi Bish, 2339، حي السلي، Riyadh 14263, Saudi Arabia" ,
"short_address" : "ABCD1234" ,
"district" : "السلي" ,
"street" : "وليد" ,
"fulfillment_priority" : 4 ,
"is_default" : false ,
"is_private" : false ,
"is_enabled" : true ,
"has_stocks" : true ,
"channels" : [
"pos"
] ,
"linked_users" : [ ]
} ,
{
"id" : "982a2aac-b9af-44e3-a3e0-51d2faa6b7c2" ,
"name" : {
"en" : "مخزن الكويت"
} ,
"city" : {
"id" : 1107 ,
"name" : "Abu Hasaniya" ,
"ar_name" : "أبو الحصانية" ,
"country" : {
"id" : 114 ,
"name" : "Kuwait" ,
"ar_name" : "الكويت" ,
"iso_code_2" : "KW" ,
"iso_code_3" : "KWT" ,
"code" : "KW"
} ,
"country_code" : "KW"
} ,
"type" : "PHYSICAL" ,
"coordinates" : {
"latitude" : 30.0546476642069 ,
"longitude" : 31.23390532891117
} ,
"full_address" : "32 Ibn Al Yazri, Boulaq Num.4, Bulaq, Cairo Governorate 4310066, Egypt" ,
"short_address" : null ,
"district" : "" ,
"street" : "" ,
"fulfillment_priority" : null ,
"is_default" : false ,
"is_private" : false ,
"is_enabled" : true ,
"has_stocks" : true ,
"channels" : [
"catalog"
] ,
"linked_users" : [ ]
} ,
{
"id" : "0bf616e8-a3f5-491c-97b3-746ab100eb8c" ,
"name" : {
"en" : "مخزون جدة"
} ,
"city" : {
"id" : 71 ,
"name" : "Jeddah" ,
"ar_name" : "جدة" ,
"country" : {
"id" : 184 ,
"name" : "Saudi Arabia" ,
"ar_name" : "السعودية" ,
"iso_code_2" : "SA" ,
"iso_code_3" : "SAU" ,
"code" : "SA"
} ,
"country_code" : "SA"
} ,
"type" : "PHYSICAL" ,
"coordinates" : {
"latitude" : 21.53040203157045 ,
"longitude" : 39.17084954081419
} ,
"full_address" : "JCHA3867, 3867 Al Hilam, 6825, Al Hamra District, Jeddah 23324, Saudi Arabia" ,
"short_address" : null ,
"district" : "" ,
"street" : "" ,
"fulfillment_priority" : 2 ,
"is_default" : false ,
"is_private" : false ,
"is_enabled" : true ,
"has_stocks" : true ,
"channels" : [
"catalog"
] ,
"linked_users" : [ ]
} ,
{
"id" : "fbc5c958-4f51-49de-bb69-18d587e27166" ,
"name" : {
"ar" : "زد كاشير"
} ,
"city" : {
"id" : 1 ,
"name" : "Riyadh" ,
"ar_name" : "الرياض" ,
"country" : {
"id" : 184 ,
"name" : "Saudi Arabia" ,
"ar_name" : "السعودية" ,
"iso_code_2" : "SA" ,
"iso_code_3" : "SAU" ,
"code" : "SA"
} ,
"country_code" : "SA"
} ,
"type" : "PHYSICAL" ,
"coordinates" : {
"latitude" : 24.75274712075788 ,
"longitude" : 46.65049508956145
} ,
"full_address" : "RGNA7959، 7959 وادي المقراة، 5375، حي النخيل، الرياض 12381, Saudi Arabia" ,
"short_address" : "jmba2121" ,
"district" : "kjjlk" ,
"street" : "lklk" ,
"fulfillment_priority" : 1 ,
"is_default" : false ,
"is_private" : false ,
"is_enabled" : true ,
"has_stocks" : true ,
"channels" : [
"pos" ,
"external.3"
] ,
"linked_users" : [ ]
} ,
{
"id" : "e5e1ea5f-4e3d-48c3-ad96-6622fc598736" ,
"name" : {
"ar" : "مخزن الطايف"
} ,
"city" : {
"id" : 92 ,
"name" : "Tabuk" ,
"ar_name" : "تبوك" ,
"country" : {
"id" : 184 ,
"name" : "Saudi Arabia" ,
"ar_name" : "السعودية" ,
"iso_code_2" : "SA" ,
"iso_code_3" : "SAU" ,
"code" : "SA"
} ,
"country_code" : "SA"
} ,
"type" : "PHYSICAL" ,
"coordinates" : {
"latitude" : 21.27117116694547 ,
"longitude" : 40.42276206147611
} ,
"full_address" : "حي, TAAE9183, 9183 Oman, 3457, Ashuhada Ashamaliyyah, At Taif 26513, Saudi Arabia" ,
"short_address" : null ,
"district" : "" ,
"street" : "" ,
"fulfillment_priority" : 6 ,
"is_default" : false ,
"is_private" : false ,
"is_enabled" : true ,
"has_stocks" : true ,
"channels" : [
"catalog"
] ,
"linked_users" : [ ]
} ,
{
"id" : "e53d5450-c4b0-45e0-ad7b-3c61eb667897" ,
"name" : {
"en" : "China Inv"
} ,
"city" : {
"id" : 5332 ,
"name" : "Beijing" ,
"ar_name" : "بكين" ,
"country" : {
"id" : 44 ,
"name" : "China" ,
"ar_name" : "الصين" ,
"iso_code_2" : "CN" ,
"iso_code_3" : "CHN" ,
"code" : "CN"
} ,
"country_code" : "CN"
} ,
"type" : "PHYSICAL" ,
"coordinates" : {
"latitude" : 24.71867979090541 ,
"longitude" : 46.67605867583006
} ,
"full_address" : "6576 Prince Faisal Ibn Saad Ibn Abd Al Rahman, 2884, Al Wurud, Riyadh 12251, Saudi Arabia" ,
"short_address" : null ,
"district" : null ,
"street" : null ,
"fulfillment_priority" : null ,
"is_default" : false ,
"is_private" : false ,
"is_enabled" : true ,
"has_stocks" : false ,
"channels" : [
"catalog"
] ,
"linked_users" : [ ]
} ,
{
"id" : "34bb2514-5359-4b52-ac8e-a045d0ec7956" ,
"name" : {
"ar" : "WeboTestInventory"
} ,
"city" : {
"id" : 5298 ,
"name" : "As-Salt" ,
"ar_name" : "السلط" ,
"country" : {
"id" : 108 ,
"name" : "Jordan" ,
"ar_name" : "الأردن" ,
"iso_code_2" : "JO" ,
"iso_code_3" : "JOR" ,
"code" : "JO"
} ,
"country_code" : "JO"
} ,
"type" : "PHYSICAL" ,
"coordinates" : {
"latitude" : 0.0 ,
"longitude" : 0.0
} ,
"full_address" : "69.35.32.36" ,
"short_address" : null ,
"district" : "Test" ,
"street" : "Test" ,
"fulfillment_priority" : 3 ,
"is_default" : false ,
"is_private" : false ,
"is_enabled" : true ,
"has_stocks" : true ,
"channels" : [
"pos"
] ,
"linked_users" : [ ]
} ,
{
"id" : "2fdcc886-74d2-4f76-a5f3-ed06797a6d82" ,
"name" : {
"en" : "nbb"
} ,
"city" : {
"id" : 1 ,
"name" : "Riyadh" ,
"ar_name" : "الرياض" ,
"country" : {
"id" : 184 ,
"name" : "Saudi Arabia" ,
"ar_name" : "السعودية" ,
"iso_code_2" : "SA" ,
"iso_code_3" : "SAU" ,
"code" : "SA"
} ,
"country_code" : "SA"
} ,
"type" : "PHYSICAL" ,
"coordinates" : {
"latitude" : 24.76965922592517 ,
"longitude" : 46.73923006254881
} ,
"full_address" : "RFHA2884، 2884 شارع الأمير مقرن بن عبدالعزيز، 7046, Al Hamra, Riyadh 13216, Saudi Arabia" ,
"short_address" : null ,
"district" : null ,
"street" : null ,
"fulfillment_priority" : null ,
"is_default" : false ,
"is_private" : false ,
"is_enabled" : true ,
"has_stocks" : false ,
"channels" : [
"catalog"
] ,
"linked_users" : [ ]
} ,
{
"id" : "bd3a596c-2e5c-42af-a5f2-b7a341cff1cb" ,
"name" : {
"ar" : "الطائف واحد"
} ,
"city" : {
"id" : 55 ,
"name" : "Taif" ,
"ar_name" : "الطائف" ,
"country" : {
"id" : 184 ,
"name" : "Saudi Arabia" ,
"ar_name" : "السعودية" ,
"iso_code_2" : "SA" ,
"iso_code_3" : "SAU" ,
"code" : "SA"
} ,
"country_code" : "SA"
} ,
"type" : "PHYSICAL" ,
"coordinates" : {
"latitude" : 21.29444499014764 ,
"longitude" : 40.42501380639715
} ,
"full_address" : "TADA6658, 6658 Airport Rd, 4403, Al Faisaliyyah, At Taif 26526, Saudi Arabia" ,
"short_address" : "ABCD1234" ,
"district" : "TEST" ,
"street" : "TEST" ,
"fulfillment_priority" : null ,
"is_default" : false ,
"is_private" : false ,
"is_enabled" : false ,
"has_stocks" : false ,
"channels" : [
"catalog"
] ,
"linked_users" : [ ]
} ,
{
"id" : "337419fb-fa90-4308-b1e3-6a2b272dd0d9" ,
"name" : {
"en" : "الطائف اثنين"
} ,
"city" : {
"id" : 55 ,
"name" : "Taif" ,
"ar_name" : "الطائف" ,
"country" : {
"id" : 184 ,
"name" : "Saudi Arabia" ,
"ar_name" : "السعودية" ,
"iso_code_2" : "SA" ,
"iso_code_3" : "SAU" ,
"code" : "SA"
} ,
"country_code" : "SA"
} ,
"type" : "PHYSICAL" ,
"coordinates" : {
"latitude" : 21.22340841508445 ,
"longitude" : 40.4116280737773
} ,
"full_address" : "TAAB7494، 7494 طريق الشفاء، 5802، حي أم العراد، At Taif 26512, Saudi Arabia" ,
"short_address" : null ,
"district" : null ,
"street" : null ,
"fulfillment_priority" : null ,
"is_default" : false ,
"is_private" : false ,
"is_enabled" : false ,
"has_stocks" : false ,
"channels" : [
"catalog"
] ,
"linked_users" : [ ]
} ,
{
"id" : "c4350760-cc30-464a-a471-48806670f607" ,
"name" : {
"en" : "الطائف ثلاثة"
} ,
"city" : {
"id" : 55 ,
"name" : "Taif" ,
"ar_name" : "الطائف" ,
"country" : {
"id" : 184 ,
"name" : "Saudi Arabia" ,
"ar_name" : "السعودية" ,
"iso_code_2" : "SA" ,
"iso_code_3" : "SAU" ,
"code" : "SA"
} ,
"country_code" : "SA"
} ,
"type" : "PHYSICAL" ,
"coordinates" : {
"latitude" : 21.28418578478053 ,
"longitude" : 40.38288212103146
} ,
"full_address" : "8075, 3729, Al Khalidiyyah, At Taif 26521, Saudi Arabia" ,
"short_address" : null ,
"district" : null ,
"street" : null ,
"fulfillment_priority" : null ,
"is_default" : false ,
"is_private" : false ,
"is_enabled" : false ,
"has_stocks" : false ,
"channels" : [
"catalog"
] ,
"linked_users" : [ ]
} ,
{
"id" : "2ada7f56-c207-470d-a1d6-ee539defb6a3" ,
"name" : {
"en" : "الرياض تجربة جديدة"
} ,
"city" : {
"id" : 1 ,
"name" : "Riyadh" ,
"ar_name" : "الرياض" ,
"country" : {
"id" : 184 ,
"name" : "Saudi Arabia" ,
"ar_name" : "السعودية" ,
"iso_code_2" : "SA" ,
"iso_code_3" : "SAU" ,
"code" : "SA"
} ,
"country_code" : "SA"
} ,
"type" : "PHYSICAL" ,
"coordinates" : {
"latitude" : 24.75593717435618 ,
"longitude" : 46.77733888823241
} ,
"full_address" : "3833 Riyad Al Raoudah, 6970, King Faisal Dt., Riyadh 13215, Saudi Arabia" ,
"short_address" : null ,
"district" : "" ,
"street" : "" ,
"fulfillment_priority" : null ,
"is_default" : false ,
"is_private" : false ,
"is_enabled" : true ,
"has_stocks" : false ,
"channels" : [
"pos" ,
"catalog"
] ,
"linked_users" : [ ]
} ,
{
"id" : "59be4f1d-3b59-4b34-ba47-9f7293894b47" ,
"name" : {
"ar" : "الدمام" ,
"en" : "Dammam"
} ,
"city" : {
"id" : 24 ,
"name" : "Dammam" ,
"ar_name" : "الدمام" ,
"country" : {
"id" : 184 ,
"name" : "Saudi Arabia" ,
"ar_name" : "السعودية" ,
"iso_code_2" : "SA" ,
"iso_code_3" : "SAU" ,
"code" : "SA"
} ,
"country_code" : "SA"
} ,
"type" : "PHYSICAL" ,
"coordinates" : {
"latitude" : 26.34179794003899 ,
"longitude" : 49.83497092822263
} ,
"full_address" : "8RRM+PX Dammam Saudi Arabia" ,
"short_address" : "EDJB3266" ,
"district" : "البديعة" ,
"street" : "الأمير نايف بن عبدالعزيز" ,
"fulfillment_priority" : null ,
"is_default" : true ,
"is_private" : false ,
"is_enabled" : true ,
"has_stocks" : true ,
"channels" : [
"catalog"
] ,
"linked_users" : [ ]
}
]
} `
```

Modified at 2026-02-01 19:49:33

Previous

Update Product Stock for Location

Next

View Location
