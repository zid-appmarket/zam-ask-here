---
# Synced from https://docs.zid.sa/get-all-questions
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-get-all-questions
title: "List Product Questions"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/get-all-questions
tags: [from-docs-site, partner-docs]
language: en
---

> List Product Questions - Zid Docs
# List Product Questions

GET

https://api.zid.sa/ v1/products/{product_id}/questions

Retrieve a list of all questions for a product.

🔑Scopes

`products.read` - Products Read

## Request

Path Params

###

Header Params

###

Body Params application/json

###

Examples

## Responses

🟢 200 All questions retrieved successfully.

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
` curl --location --request GET 'https://api.zid.sa/v1/products//questions' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxMTciLCJqdGkiOiJhMTg5ZTg3MmYxMzhkMWVhYjU5MjVkMDkyMGE5NmI0YjliNjg0Y2E2ZTdmM2M2MjljZWYxNmQ4NDJjMmJlYmVhMjI4YTdmMTA0ZWQ4NWE5NCIsImlhdCI6MTY3OTU3Njk5OS41NjY4NzcsIm5iZiI6MTY3OTU3Njk5OS41NjY4OCwiZXhwIjoxNzExMTk5Mzk5LjQ4NjE1Mywic3ViIjoiMTgyNDc1Iiwic2NvcGVzIjpbInRoaXJkLXBhcnRpZXMtYXBpcyJdfQ.i07ef09nVNXGZF-g-QXpNoS2vlFQK_zntAqAMS4Az2XD2EyMLhxLZZRL-QlR11zUPqMmXjMAl_4ooKa3M3zkfZQ6Ga6qStvamk8RnC_39VUx0lfN2A4k65ERZpqwrMy6-t3dE99zay3aicIdNvbgi0zeuMSE5Tn99u-2AtSRa8ffbfAcYPPXacHrhdmlYzdiZS_x_skovFEow1E-nDjdL1WHqO92XdZ7RfNLkiYFTjZlZmM_UruvioaR3q6TXJbqRK_ZrziivezL8ohIQ2SBosUp58I29rlKzvlw_R2j0rKKYZbdxYDaxAHOISmOFKAlO66k7dNevAHI3s4uGIjoGA6ZXHknccWPLLLiaAQ0r64HV8GowW5dg2rhZNurJGDTnLlBQ6F-ql42ptHzSAfzzi576CEoN3gMVpgXcbntUY3reETkFsTBPUjeSuMpANMioXAA0GRp3Ut-84fTnrWxqsCW1WVUIx33HvmfCGPXIdkaCCWoA6G6KXo04MtFbKXQmXkK9esQWI-rqdVnMD3zSR3g3yFHZSL1U-mZeNja03706Rav1ordsRNOtRwtLuoRRbk9KasbUpEwqq4Ao9lqZZwRIjdEw-pQtnUT8V53fhmuuRIefCLFO7eGEtGUnh9o6Uh_pgi6AB6uSlnN9GEMGgI1alqvMmTjxvC-HHt0V-Y' \
--header 'Store-Id;' \
--header 'Role;' \
--header 'Access-Token: eyJpdiI6Imh3L2dGbmJmRnVCOUY4WW5WQ2s3RFE9PSIsInZhbHVlIjoiZklpRnJyVGV1OWcrZUJBNk44bVp5SjZzSS92V3czcTJjbnJ2dFYvenZ3SFBtWHNSMFU3ZEMzZ0ZJNnpucVE4Ui9rNFdicUduOGpKUlg1VXdGOFFIaVUzZjZyUUZybWx3R0tNY3orUmxoUUUxQ29wSkEyVDZTVnVYb2dlUXJSVzBYVkdESjBpS0xiN05Hbndzc2wzV2N0YitGM1NEdkk4ckZZOTZsTFdEL1ZQRlJJTE5FQmttZng2elpwL1RCeXFRdUd1U3JTc0FHV1kySS80RFJaWlIyZ3gwM2FsQVRFbkt3VWtFOUQyKzdGOD0iLCJtYWMiOiJmZDQ0YzM4ODE0OWQxOWRhYWU0NDhhYmIzYzQ1MDAxMDAzODZjZGM3ZGM4NGJhMGNkMDEyYWZlM2UzYjAxMTI4IiwidGFnIjoiIn0=' \
--header 'User-Agent;' \
--header 'Content-Type: application/json' \
--data-raw '{
"name": "\"Authed Manager\"",
"email": "\"manager@zid.sa\"",
"question": "\"What do you think of me?\"",
"store": "\"aba1846c-c536-4c8a-9e1d-6b27ef1d240a\"",
"product": "\"e5715f91a23a4eeabcead3f75b2d939c\"",
"is_anonymous": true,
"is_published": false
}' `
```

Response Response Example

200 - Example 1

```
` {
"id" : "\"cf2fc926-d179-4330-8fff-330853416aea\"," ,
"store" : "\"3dfc16e6-ad19-4126-9c2a-5e4a7fb73051\"" ,
"product" : "\"678c40b4-3989-4623-b4c2-61d29066e6ab\"" ,
"product_name" : "\"i phone\"" ,
"customer" : null ,
"name" : "\"anonymous customer\"" ,
"email" : "\"anon_customer@email.com\"" ,
"is_anonymous" : true ,
"is_owner" : false ,
"is_published" : false ,
"is_sent" : false ,
"is_new" : true ,
"question" : "\"What is ZID?\"" ,
"created_at" : "\"2024-07-12T06:28:34.765167Z\"" ,
"answers" : [
{ }
]
} `
```

Modified at 2026-01-30 20:55:20

Previous

Retrieve Product Answer

Next

List Answers for Question
