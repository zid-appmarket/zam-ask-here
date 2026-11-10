---
# Synced from https://docs.zid.sa/get-product-attributes
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-get-product-attributes
title: "List Attributes"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/get-product-attributes
tags: [from-docs-site, partner-docs]
language: en
---

> List Attributes - Zid Docs
# List Attributes

GET

https://api.zid.sa/ v1/attributes/

Use this endpoint to retrieve the Product Attributes of a certain store.

🔑Scopes

`products.read` - Products Read

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
` curl --location 'https://api.zid.sa/v1/attributes/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Store-Id: {{StoreId}}' `
```

Response Response Example

200 - Success

```
{
"count": 103,
"next": "http://api.zid.sa/v1/attributes/?page=2",
"previous": null,
"results": [
{
"id": "06c7eaed-54e3-4fe3-8c3d-23f0d24d3b9e",
"name": "Color",
"slug": "color-7",
"presets": [],
"is_extra": false,
"is_enabled": true,
"display_order": null,
"preset_count": 0
},
{
"id": "cfb5bd3f-bbc5-4439-a171-b2d70e1c0293",
"name": "",
"slug": "color-6",
"presets": [
{
"id": "1f4956ea-e19c-4de9-8c75-7e12b5e4aee8",
"slug": "color-6",
"name": "",
"value": "color",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "cfb5bd3f-bbc5-4439-a171-b2d70e1c0293"
},
{
"id": "4620a7e7-c4e3-4402-9c07-f08aab29a4dd",
"slug": "color-6",
"name": "",
"value": "color",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "cfb5bd3f-bbc5-4439-a171-b2d70e1c0293"
},
{
"id": "f56e7d74-290e-45a5-8057-f0c8b868aaee",
"slug": "color-6",
"name": "",
"value": "color",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "cfb5bd3f-bbc5-4439-a171-b2d70e1c0293"
}
],
"is_extra": false,
"is_enabled": true,
"display_order": null,
"preset_count": 3
},
{
"id": "a1d2136e-0231-4ef0-825d-30b80caf8a99",
"name": "Color",
"slug": "color-5",
"presets": [],
"is_extra": false,
"is_enabled": true,
"display_order": null,
"preset_count": 0
},
{
"id": "2ffbf61f-0f7e-44b8-954c-da223019356e",
"name": "Color",
"slug": "color-4",
"presets": [],
"is_extra": false,
"is_enabled": true,
"display_order": null,
"preset_count": 0
},
{
"id": "f1a69ab0-f3cc-459c-aeff-94046595496f",
"name": "Color",
"slug": "color-2",
"presets": [
{
"id": "25b1ff9c-a1d7-4fb6-b4e1-eb5295e9d046",
"slug": "color-2",
"name": "Color",
"value": "Color",
"type": "default",
"type_value": null,
"display_order": 1,
"attribute_image_id": null,
"attribute_id": "f1a69ab0-f3cc-459c-aeff-94046595496f"
},
{
"id": "05fea683-499b-431b-86e3-88ea50ff8bb7",
"slug": "color-2",
"name": "Color",
"value": "Red",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "f1a69ab0-f3cc-459c-aeff-94046595496f"
}
],
"is_extra": false,
"is_enabled": true,
"display_order": null,
"preset_count": 2
},
{
"id": "230192a3-9aef-4dde-aba3-836cc43f9ae6",
"name": "درجة اللون",
"slug": "ar-درجة-اللون-en",
"presets": [
{
"id": "83d7856d-a7d9-490f-9a78-406e29468246",
"slug": "ar-درجة-اللون-en",
"name": "درجة اللون",
"value": "6646444",
"type": "default",
"type_value": null,
"display_order": 15,
"attribute_image_id": null,
"attribute_id": "230192a3-9aef-4dde-aba3-836cc43f9ae6"
},
{
"id": "fbcf4607-f5cd-4ba6-8ad5-cd33c83a93ed",
"slug": "ar-درجة-اللون-en",
"name": "درجة اللون",
"value": "وعتشاه",
"type": "default",
"type_value": null,
"display_order": 16,
"attribute_image_id": null,
"attribute_id": "230192a3-9aef-4dde-aba3-836cc43f9ae6"
},
{
"id": "901fac34-3fc7-48bb-b416-883a7b1eb838",
"slug": "ar-درجة-اللون-en",
"name": "درجة اللون",
"value": "15",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "230192a3-9aef-4dde-aba3-836cc43f9ae6"
},
{
"id": "847e6202-d777-424d-a344-6f7cb07fe792",
"slug": "ar-درجة-اللون-en",
"name": "درجة اللون",
"value": "55",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "230192a3-9aef-4dde-aba3-836cc43f9ae6"
},
{
"id": "79c031d5-739b-489f-a036-cf324761646f",
"slug": "ar-درجة-اللون-en",
"name": "درجة اللون",
"value": "777",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "230192a3-9aef-4dde-aba3-836cc43f9ae6"
},
{
"id": "589cc2c5-930b-4eaa-883d-5e75bc9f2b55",
"slug": "ar-درجة-اللون-en",
"name": "درجة اللون",
"value": "12",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "230192a3-9aef-4dde-aba3-836cc43f9ae6"
},
{
"id": "f28dcd67-b37c-46a9-a96a-22de8dd150b3",
"slug": "ar-درجة-اللون-en",
"name": "درجة اللون",
"value": "11",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "230192a3-9aef-4dde-aba3-836cc43f9ae6"
},
{
"id": "6d374e3c-aceb-4b54-937d-79a2c5dcb0cf",
"slug": "ar-درجة-اللون-en",
"name": "درجة اللون",
"value": "10",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "230192a3-9aef-4dde-aba3-836cc43f9ae6"
},
{
"id": "d7d71220-f22e-436f-9a62-43139637e454",
"slug": "ar-درجة-اللون-en",
"name": "درجة اللون",
"value": "09",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "230192a3-9aef-4dde-aba3-836cc43f9ae6"
},
{
"id": "576a7d4d-cefd-4e6f-9503-5920e451876a",
"slug": "ar-درجة-اللون-en",
"name": "درجة اللون",
"value": "08",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "230192a3-9aef-4dde-aba3-836cc43f9ae6"
},
{
"id": "cdd84ea8-09dd-4e3e-aac8-1deb3782a1c2",
"slug": "ar-درجة-اللون-en",
"name": "درجة اللون",
"value": "07",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "230192a3-9aef-4dde-aba3-836cc43f9ae6"
},
{
"id": "a75d8570-0c80-423f-b59c-675df859bca9",
"slug": "ar-درجة-اللون-en",
"name": "درجة اللون",
"value": "0666",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "230192a3-9aef-4dde-aba3-836cc43f9ae6"
},
{
"id": "cfe35c9b-0a6e-4712-9099-3d841969bf77",
"slug": "ar-درجة-اللون-en",
"name": "درجة اللون",
"value": "05",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "230192a3-9aef-4dde-aba3-836cc43f9ae6"
},
{
"id": "c4b17330-3eac-4da9-ad7e-186d239776af",
"slug": "ar-درجة-اللون-en",
"name": "درجة اللون",
"value": "04",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "230192a3-9aef-4dde-aba3-836cc43f9ae6"
},
{
"id": "df74ec92-dbf9-4705-80f2-7edc39f011ec",
"slug": "ar-درجة-اللون-en",
"name": "درجة اللون",
"value": "03",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "230192a3-9aef-4dde-aba3-836cc43f9ae6"
},
{
"id": "59dd1880-59a5-495d-8ece-5111648b1878",
"slug": "ar-درجة-اللون-en",
"name": "درجة اللون",
"value": "02",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "230192a3-9aef-4dde-aba3-836cc43f9ae6"
},
{
"id": "95d20f5d-a196-4ae5-ad29-4161de849a2e",
"slug": "ar-درجة-اللون-en",
"name": "درجة اللون",
"value": "01",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "230192a3-9aef-4dde-aba3-836cc43f9ae6"
}
],
"is_extra": false,
"is_enabled": true,
"display_order": null,
"preset_count": 17
},
{
"id": "c9e0605b-9d8e-46c5-9292-e841c9b7c51a",
"name": "خيارات",
"slug": "ar-خيارات-en",
"presets": [
{
"id": "5d0d974e-0769-4717-a758-afffe24e16d6",
"slug": "ar-خيارات-en",
"name": "خيارات",
"value": "احمر",
"type": "default",
"type_value": null,
"display_order": 4,
"attribute_image_id": null,
"attribute_id": "c9e0605b-9d8e-46c5-9292-e841c9b7c51a"
},
{
"id": "67b9eb05-95e3-4e95-8db2-c1a802fc88e7",
"slug": "ar-خيارات-en",
"name": "خيارات",
"value": "ازرق",
"type": "default",
"type_value": null,
"display_order": 5,
"attribute_image_id": null,
"attribute_id": "c9e0605b-9d8e-46c5-9292-e841c9b7c51a"
},
{
"id": "cd882970-c925-47cd-b9f1-2e105deecc74",
"slug": "ar-خيارات-en",
"name": "خيارات",
"value": "لون رمادي",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "c9e0605b-9d8e-46c5-9292-e841c9b7c51a"
},
{
"id": "7829942a-5b87-462b-8c47-f98cdaebca01",
"slug": "ar-خيارات-en",
"name": "خيارات",
"value": "لون اسود",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "c9e0605b-9d8e-46c5-9292-e841c9b7c51a"
},
{
"id": "daca6cab-884d-48bf-b71f-64718a92ce23",
"slug": "ar-خيارات-en",
"name": "خيارات",
"value": "لون زهري",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "c9e0605b-9d8e-46c5-9292-e841c9b7c51a"
}
],
"is_extra": false,
"is_enabled": true,
"display_order": null,
"preset_count": 5
},
{
"id": "4336d230-7695-4fe3-aa42-de378f376698",
"name": "الباليت",
"slug": "ar-الباليت-en",
"presets": [
{
"id": "c53a7f2b-3234-4fd3-aa5a-480431e61598",
"slug": "ar-الباليت-en",
"name": "الباليت",
"value": "B",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "4336d230-7695-4fe3-aa42-de378f376698"
},
{
"id": "376988fa-f94c-42c8-b951-ace6efcbfbd4",
"slug": "ar-الباليت-en",
"name": "الباليت",
"value": "C",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "4336d230-7695-4fe3-aa42-de378f376698"
}
],
"is_extra": false,
"is_enabled": true,
"display_order": null,
"preset_count": 2
},
{
"id": "7ca27aaf-3d32-4999-855b-d70fd77ac0b1",
"name": "W:",
"slug": "ar-w-en",
"presets": [
{
"id": "b1b01946-e125-42c3-9dc8-639461130dcd",
"slug": "ar-w-en",
"name": "W:",
"value": "37",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "7ca27aaf-3d32-4999-855b-d70fd77ac0b1"
},
{
"id": "50edfd46-ba36-4cb8-8011-8466bba3a249",
"slug": "ar-w-en",
"name": "W:",
"value": "36",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "7ca27aaf-3d32-4999-855b-d70fd77ac0b1"
},
{
"id": "97890e2e-3f00-49fe-b772-1c0c47358cb5",
"slug": "ar-w-en",
"name": "W:",
"value": "35",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "7ca27aaf-3d32-4999-855b-d70fd77ac0b1"
},
{
"id": "a23c8cbd-6f33-4d95-ba86-ab8a998620ef",
"slug": "ar-w-en",
"name": "W:",
"value": "34",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "7ca27aaf-3d32-4999-855b-d70fd77ac0b1"
},
{
"id": "c6f05dba-cfb4-4887-abe7-5d92ddf2f263",
"slug": "ar-w-en",
"name": "W:",
"value": "33",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "7ca27aaf-3d32-4999-855b-d70fd77ac0b1"
},
{
"id": "72f0d65f-7cb2-4d9b-86cb-3e4f4c6db98b",
"slug": "ar-w-en",
"name": "W:",
"value": "32",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "7ca27aaf-3d32-4999-855b-d70fd77ac0b1"
},
{
"id": "28552318-df7b-47ed-9331-5e92ab500314",
"slug": "ar-w-en",
"name": "W:",
"value": "31",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "7ca27aaf-3d32-4999-855b-d70fd77ac0b1"
},
{
"id": "c9a582a8-72b0-4df3-b307-2509ab6c0dac",
"slug": "ar-w-en",
"name": "W:",
"value": "30",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "7ca27aaf-3d32-4999-855b-d70fd77ac0b1"
},
{
"id": "8edd83ba-e6c7-4860-99c0-f8f8498e5d10",
"slug": "ar-w-en",
"name": "W:",
"value": "29",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "7ca27aaf-3d32-4999-855b-d70fd77ac0b1"
},
{
"id": "b0f5b693-a62d-46da-9c9d-2189732a8df3",
"slug": "ar-w-en",
"name": "W:",
"value": "28",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "7ca27aaf-3d32-4999-855b-d70fd77ac0b1"
},
{
"id": "cac5e035-9db8-4159-8d81-c3f173550f1d",
"slug": "ar-w-en",
"name": "W:",
"value": "27",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "7ca27aaf-3d32-4999-855b-d70fd77ac0b1"
},
{
"id": "a06623d8-94fc-4a87-a438-2d0227642475",
"slug": "ar-w-en",
"name": "W:",
"value": "26",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "7ca27aaf-3d32-4999-855b-d70fd77ac0b1"
},
{
"id": "5aebf6f4-5ab0-436d-b661-f67c1724a8e0",
"slug": "ar-w-en",
"name": "W:",
"value": "25",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "7ca27aaf-3d32-4999-855b-d70fd77ac0b1"
},
{
"id": "f920e7c3-3c1e-4734-8c4a-a81d0c6ed83e",
"slug": "ar-w-en",
"name": "W:",
"value": "24",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "7ca27aaf-3d32-4999-855b-d70fd77ac0b1"
},
{
"id": "476b449d-f3e6-4e10-9dc8-fe1cfe8273ea",
"slug": "ar-w-en",
"name": "W:",
"value": "23",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "7ca27aaf-3d32-4999-855b-d70fd77ac0b1"
},
{
"id": "d24f8df5-0929-4ad5-8d1e-ca7733f3494b",
"slug": "ar-w-en",
"name": "W:",
"value": "22",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "7ca27aaf-3d32-4999-855b-d70fd77ac0b1"
},
{
"id": "f5fe0003-265a-4f29-826c-636962206353",
"slug": "ar-w-en",
"name": "W:",
"value": "21",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "7ca27aaf-3d32-4999-855b-d70fd77ac0b1"
},
{
"id": "eeea8ed2-2f73-4685-9394-971646b1963f",
"slug": "ar-w-en",
"name": "W:",
"value": "20",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "7ca27aaf-3d32-4999-855b-d70fd77ac0b1"
},
{
"id": "3f6efceb-0dd5-4817-93bb-ff4a34605ea2",
"slug": "ar-w-en",
"name": "W:",
"value": "19",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "7ca27aaf-3d32-4999-855b-d70fd77ac0b1"
},
{
"id": "bbbd00d9-2384-42a5-98a3-ffd00f6db05d",
"slug": "ar-w-en",
"name": "W:",
"value": "18",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "7ca27aaf-3d32-4999-855b-d70fd77ac0b1"
},
{
"id": "eb3c5f8d-0896-48bf-adb7-7bfe07ace017",
"slug": "ar-w-en",
"name": "W:",
"value": "17",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "7ca27aaf-3d32-4999-855b-d70fd77ac0b1"
},
{
"id": "c93ca261-52ee-4d9f-b575-dee673def8b9",
"slug": "ar-w-en",
"name": "W:",
"value": "16",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "7ca27aaf-3d32-4999-855b-d70fd77ac0b1"
},
{
"id": "c113d5e4-c840-47f5-ba46-2086f74a58b9",
"slug": "ar-w-en",
"name": "W:",
"value": "15",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "7ca27aaf-3d32-4999-855b-d70fd77ac0b1"
},
{
"id": "527db38c-4ef1-421f-b24a-6d8c27038387",
"slug": "ar-w-en",
"name": "W:",
"value": "14",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "7ca27aaf-3d32-4999-855b-d70fd77ac0b1"
},
{
"id": "ea0c3a63-b18d-4d48-9754-f915b32f3b1b",
"slug": "ar-w-en",
"name": "W:",
"value": "13",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "7ca27aaf-3d32-4999-855b-d70fd77ac0b1"
},
{
"id": "5b5adc99-62c7-4749-82a1-766a2c5f682e",
"slug": "ar-w-en",
"name": "W:",
"value": "12",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "7ca27aaf-3d32-4999-855b-d70fd77ac0b1"
},
{
"id": "13fa48d6-795a-4f48-ac48-4e8e010b41d1",
"slug": "ar-w-en",
"name": "W:",
"value": "11",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "7ca27aaf-3d32-4999-855b-d70fd77ac0b1"
},
{
"id": "9319da24-ad26-4670-8dd4-68df86a9aaf9",
"slug": "ar-w-en",
"name": "W:",
"value": "10",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "7ca27aaf-3d32-4999-855b-d70fd77ac0b1"
},
{
"id": "a99fc364-81ca-4d6f-9adc-2bc6fa2a33b0",
"slug": "ar-w-en",
"name": "W:",
"value": "09",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "7ca27aaf-3d32-4999-855b-d70fd77ac0b1"
},
{
"id": "32e3af8b-d06c-4eaa-9d50-4d2e1f198312",
"slug": "ar-w-en",
"name": "W:",
"value": "08",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "7ca27aaf-3d32-4999-855b-d70fd77ac0b1"
},
{
"id": "f4202816-9f98-4399-880b-881b6c7bfb7b",
"slug": "ar-w-en",
"name": "W:",
"value": "07",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "7ca27aaf-3d32-4999-855b-d70fd77ac0b1"
},
{
"id": "928e6c26-f6f3-40c3-9dec-e70e5844b2a1",
"slug": "ar-w-en",
"name": "W:",
"value": "06",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "7ca27aaf-3d32-4999-855b-d70fd77ac0b1"
},
{
"id": "8c5d9e15-9407-4d1c-bd28-deed910ebe0b",
"slug": "ar-w-en",
"name": "W:",
"value": "05",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "7ca27aaf-3d32-4999-855b-d70fd77ac0b1"
},
{
"id": "36023866-b26f-49ea-a705-82b82457dbb4",
"slug": "ar-w-en",
"name": "W:",
"value": "04",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "7ca27aaf-3d32-4999-855b-d70fd77ac0b1"
},
{
"id": "7e65ce05-8e50-488c-b98c-fc5fae1b1ff1",
"slug": "ar-w-en",
"name": "W:",
"value": "03",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "7ca27aaf-3d32-4999-855b-d70fd77ac0b1"
},
{
"id": "d796e23e-4212-4c3e-aeeb-7a160377e36a",
"slug": "ar-w-en",
"name": "W:",
"value": "02",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "7ca27aaf-3d32-4999-855b-d70fd77ac0b1"
},
{
"id": "94de498c-8369-4b92-9e10-3a4a44243c3d",
"slug": "ar-w-en",
"name": "W:",
"value": "01",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "7ca27aaf-3d32-4999-855b-d70fd77ac0b1"
}
],
"is_extra": false,
"is_enabled": true,
"display_order": null,
"preset_count": 37
},
{
"id": "ab13238e-edff-4dc2-9596-57ff524a1315",
"name": "النوع:",
"slug": "ar-النوع-en-1",
"presets": [
{
"id": "c0a701bb-ecf4-420e-9958-0320a0c1d15f",
"slug": "ar-النوع-en-1",
"name": "النوع:",
"value": "E",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "ab13238e-edff-4dc2-9596-57ff524a1315"
},
{
"id": "74de71f0-26f6-4761-bf34-06cd9ef13b05",
"slug": "ar-النوع-en-1",
"name": "النوع:",
"value": "F",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "ab13238e-edff-4dc2-9596-57ff524a1315"
},
{
"id": "871ea896-baeb-4379-b3ed-f8496239eef6",
"slug": "ar-النوع-en-1",
"name": "النوع:",
"value": "G",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "ab13238e-edff-4dc2-9596-57ff524a1315"
},
{
"id": "9f31d46d-7c53-4789-b319-3e5a1ac7ceb0",
"slug": "ar-النوع-en-1",
"name": "النوع:",
"value": "B",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "ab13238e-edff-4dc2-9596-57ff524a1315"
},
{
"id": "25095b67-bd56-4d33-818f-26598f20c521",
"slug": "ar-النوع-en-1",
"name": "النوع:",
"value": "C",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "ab13238e-edff-4dc2-9596-57ff524a1315"
},
{
"id": "94ef6dde-0b82-434e-8bee-4f840e71816c",
"slug": "ar-النوع-en-1",
"name": "النوع:",
"value": "D",
"type": "default",
"type_value": null,
"display_order": null,
"attribute_image_id": null,
"attribute_id": "ab13238e-edff-4dc2-9596-57ff524a1315"
}
],
"is_extra": false,
"is_enabled": true,
"display_order": null,
"preset_count": 6
}
]
}
```

Modified at 2026-02-15 15:52:35

Previous

Product Attributes

Next

View Attribute
