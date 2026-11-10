---
# Synced from https://help-partner.zid.sa/en/articles/17129233-managing-your-app-s-support-channels-on-zid-app-market
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: ph-managing-your-app-s-support-channels-on-zid-app-market
title: "Managing your app's support channels on Zid App Market"
product: zam
audience: all
status: verified
updated: 2026-09-24
source_url: https://help-partner.zid.sa/en/articles/17129233-managing-your-app-s-support-channels-on-zid-app-market
tags: [from-docs-site, partner-help-center]
language: en
---

> How to fill in your app's support-contact fields from the Partner Dashboard and where merchants see them.
Every app listing on Zid App Market includes a set of support-contact fields that you manage from the app submission form in the Partner Dashboard. What you enter is displayed to merchants in the **Contact details** tab of your app's detail page, and merchants use these channels to reach your support team directly.

These are listing fields only — they do not affect your app's API integration, webhooks, OAuth scopes, or embedded-app behavior.

## The contact fields

Alongside your app's email and website, the submission form includes the following fields:

Field

Requirement

Purpose

Privacy Policy URL

**Always required**

Merchant-facing privacy terms for your app

Phone number

Conditional

Direct voice/SMS contact

Support channel URL

Conditional

WhatsApp, Telegram, or any support portal

FAQ URL

Optional

Self-service answers before contacting you

## The conditional requirement rule

Phone number and Support channel URL are linked: **at least one of the two must be filled in.**

Each becomes mandatory when the other is empty. In practice:

- Phone filled, Support channel empty → valid

- Support channel filled, Phone empty → valid

- Both filled → valid, and recommended

- Both empty → the form blocks submission

Privacy Policy URL is required independently of this rule.

## How to fill them in

- Open **Partner Dashboard → Apps** and select the app.

- Open the app submission/edit form and go to the contact details section.

- Enter the **Privacy Policy URL** — a live, publicly reachable page, not a login-gated or draft document.

- Enter a **Phone number**, a **Support channel URL**, or both.

- Optionally add an **FAQ URL**.

- Save and submit. Changes appear on the app page after review.

## Choosing a good support channel URL

The field accepts any URL, so choose a destination that actually helps the merchant:

- **Point it at a real support destination** — a WhatsApp Business link, a Telegram support account, or a ticketing portal. Not your homepage, not a pricing page.

- **Verify the link opens a conversation.** A WhatsApp link tied to a deactivated number is worse than an empty field, because the merchant assumes support exists.

- **Match the channel to your capacity.** A phone number no one answers converts a support problem into a bad review.

- **Use the FAQ URL for deflection.** Point it at real documentation for common setup and billing questions to reduce inbound volume.

## FAQ

**Do these fields require any change to my app's code or version?**

No. These are listing fields only.

**Which fields are mandatory?**

The Privacy Policy URL is always mandatory, and at least one of Phone number or Support channel URL must be filled in. The FAQ URL is optional.

**Can I use the same phone number across multiple apps?**

Yes, if the team behind that number actually supports all of them.

**Where do merchants see this information?**

In the **Contact details** tab on your app's detail page in Zid App Market.

**Where do I get help?**

Contact the App Market team at [email protected] .

Related Articles

- Zid App Market: App Review Requirements Checklist

(https://help-partner.zid.sa/en/articles/10658329-zid-app-market-app-review-requirements-checklist)

- Support your customers

(https://help-partner.zid.sa/en/articles/10938425-support-your-customers)

- Maintain Your Theme Support

(https://help-partner.zid.sa/en/articles/11471850-maintain-your-theme-support)

- Oddo Integration - Arabic session on how to connect Odoo with Zid App Market APIs

(https://help-partner.zid.sa/en/articles/12867648-oddo-integration-arabic-session-on-how-to-connect-odoo-with-zid-app-market-apis)

- Connect your Zid partner account to your AI assistant with Partner MCP

(https://help-partner.zid.sa/en/articles/17430435-connect-your-zid-partner-account-to-your-ai-assistant-with-partner-mcp)
