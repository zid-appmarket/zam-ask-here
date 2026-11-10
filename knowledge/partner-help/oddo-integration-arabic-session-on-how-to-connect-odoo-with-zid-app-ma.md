---
# Synced from https://help-partner.zid.sa/en/articles/12867648-oddo-integration-arabic-session-on-how-to-connect-odoo-with-zid-app-market-apis
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: ph-oddo-integration-arabic-session-on-how-to-connect-odoo-with-zid-app-ma
title: "Oddo Integration - Arabic session on how to connect Odoo with Zid App Market APIs"
product: zam
audience: all
status: verified
updated: 2025-11-24
source_url: https://help-partner.zid.sa/en/articles/12867648-oddo-integration-arabic-session-on-how-to-connect-odoo-with-zid-app-market-apis
tags: [from-docs-site, partner-help-center]
language: en
---

> This guide explains how to integrate Odoo with Zid App Market APIs.
# **1. Overview**

This guide explains how to integrate **Odoo** with **Zid App Market APIs** so that developers can sync:

- Products

- Categories

- Inventory

- Orders

- Customers

The video teaches how to authenticate, call the APIs, build the connector inside Odoo, and sync/store data using Odoo models.

# **2. Prerequisites**

Before starting, you need:

## **Zid Requirements**

✔ Zid merchant account

✔ An approved app in **Zid App Market**

✔ API credentials:

- **client_id**

- **client_secret**

- **redirect_url**

- **scopes**

✔ Knowledge of Zid API endpoints (REST)

## **Odoo Requirements**

✔ Odoo custom module or development access

✔ Knowledge of Odoo:

- Models

- Controllers

- Scheduled Jobs

- External API calls

✔ Ability to install 3rd-party Python libraries (requests)

# **3. Integration Architecture (High-Level)**

```
Merchant clicks "Connect to Zid" in Odoo

↓

Zid OAuth page opens

↓

Merchant approves access

↓

Zid redirects back with a temporary "code"

↓

Odoo exchanges code → access_token + refresh_token

↓

Odoo uses access_token to call Zid APIs:

- Get Products

- Get Categories

- Get Orders

- Get Customers

↓

Odoo stores the data in corresponding Odoo models

↓

Optional: Webhooks from Zid notify Odoo automatically

```

# **4. Step-by-Step Integration**

## **STEP 1 — Create a Zid App**

From Zid App Market Developer Dashboard:

- Go to: **Apps → Create New App**

- Fill app info (name, description, logo)

- Add **redirect URL** (where Odoo will receive the code)

- Select the required **permissions (scopes)**:

- products.read/write

- categories.read

- orders.read

- customers.read

- inventory.write

- Save and get:

- `client_id`

- `client_secret`

## **STEP 2 — Build the Authorization URL**

Odoo should generate this URL for the merchant:

```
<https://api.zid.sa/oauth/authorize>? client_id=YOUR_CLIENT_ID& response_type=code& redirect_uri=YOUR_REDIRECT_URL& scope=products.read categories.read orders.read customers.read
```

Merchant clicks **Connect**, is redirected to Zid, and approves.

## **STEP 3 — Zid Redirects Back With `code`**

Example:

```
<https://your-odoo.com/zid/callback?code=BDJHSDJH87sd98SD7>
```

Odoo receives the **code** and immediately exchanges it for tokens.

## **STEP 4 — Exchange Code for Tokens**

Odoo sends:

## **POST /oauth/token**

```
POST <https://api.zid.sa/oauth/token>
```

**Body:**

```
{ "grant_type": "authorization_code", "client_id": "xxxxx", "client_secret": "yyyyy", "redirect_uri": "<https://your-odoo.com/zid/callback>", "code": "BDJHSDJH87sd98SD7" }
```

**Response:**

```
{ "access_token": "ACCESS_TOKEN", "refresh_token": "REFRESH_TOKEN", "expires_in": 3600, "token_type": "Bearer" }
```

Store both tokens in Odoo.

## **STEP 5 — Refresh Token Automatically**

Odoo must schedule a cron job to refresh the token:

```
POST /oauth/token { "grant_type": "refresh_token", "client_id": "xxxxx", "client_secret": "yyyyy", "refresh_token": "REFRESH_TOKEN" }
```

## **STEP 6 — Start Syncing Data**

## **Products**

```
GET <https://api.zid.sa/v1/products> Authorization: Bearer ACCESS_TOKEN
```

Sync fields:

- id

- name (ar/en)

- price

- sku

- barcode

- inventory

- images

- categories

- variants (if any)

## **Categories**

```
GET <https://api.zid.sa/v1/categories>
```

Sync:

- id

- parent_id

- name

- visibility

## **Orders**

```
GET <https://api.zid.sa/v1/orders>
```

Sync:

- order id

- customer

- order items

- totals

- shipping address

- payment status

- order status

## **Customers**

```
GET <https://api.zid.sa/v1/customers>
```

Sync:

- id

- name

- phone

- email

- addresses

## **Inventory (Stock Updates)**

```
PUT <https://api.zid.sa/v1/products/{id}/inventory>
```

Odoo should update quantities whenever stock changes.

# **7. Implementing Webhooks (Optional)**

Zid can notify Odoo directly when:

- New order created

- Product updated

- Inventory changed

- Customer created

Odoo should expose an endpoint:

```
POST <https://your-odoo.com/zid/webhook>
```

Zid sends JSON updates → Odoo updates models.

# **8. Common Mistakes Mentioned in the Video**

**Issue**

**Explanation**

Missing scopes

API calls fail because the app wasn’t granted the needed permissions

Incorrect redirect URL

Zid will not return the `code` if redirect is wrong

Not refreshing tokens

Access token expires (3600 seconds = 1 hour)

Odoo SSL issues

Odoo must run with HTTPS for OAuth

Wrong headers

Must always include: `Authorization: Bearer ACCESS_TOKEN`

Pagination ignored

Products / Orders need pagination handling

# **9. Quick Start Version (Short Guide)**

**1. Create a Zid App** → copy client_id + client_secret

**2. Generate OAuth URL** → merchant approves

**3. Zid sends `code` to Odoo**

**4. Exchange code for access_token**

**5. Store access & refresh tokens**

**6. Sync data using Zid APIs**

**7. Optional:** Set up webhooks for real-time updates

## **Connect Odoo With Zid App Market (Step-by-Step)**

- Go to **Odoo → Settings → Integrations**.

- Click **Connect with Zid**.

- You will be redirected to Zid’s permission page.

- Approve the required permissions.

- After approval, Odoo receives a temporary `code`.

- Odoo exchanges it for an `access_token` and `refresh_token`.

- Odoo can now sync products, categories, orders, and customers.

- Stock levels are synced automatically using the inventory API.

- (Optional) Enable webhooks for real-time order and product updates.

Related Articles

- Create a shipping app or Fulfillment App

(https://help-partner.zid.sa/en/articles/8637270-create-a-shipping-app-or-fulfillment-app)

- Guide to Integrating Shipping Systems with the Zid Platform

(https://help-partner.zid.sa/en/articles/15544622-guide-to-integrating-shipping-systems-with-the-zid-platform)

- Managing your app's support channels on Zid App Market

(https://help-partner.zid.sa/en/articles/17129233-managing-your-app-s-support-channels-on-zid-app-market)

- Connect your Zid partner account to your AI assistant with Partner MCP

(https://help-partner.zid.sa/en/articles/17430435-connect-your-zid-partner-account-to-your-ai-assistant-with-partner-mcp)
