---
# Synced from https://help-partner.zid.sa/en/articles/17430435-connect-your-zid-partner-account-to-your-ai-assistant-with-partner-mcp
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: ph-connect-your-zid-partner-account-to-your-ai-assistant-with-partner-mcp
title: "Connect your Zid partner account to your AI assistant with Partner MCP"
product: zam
audience: all
status: verified
updated: 2026-10-07
source_url: https://help-partner.zid.sa/en/articles/17430435-connect-your-zid-partner-account-to-your-ai-assistant-with-partner-mcp
tags: [from-docs-site, partner-help-center]
language: en
---

> Connect your Zid partner account to AI assistants to access documentation, analytics, apps, payouts, and other partner information.
Partner MCP connects your Zid partner account to an MCP-compatible AI assistant such as Claude, Cursor, or VS Code.

Once connected, you can ask questions in natural language about both:

- **How Zid works**, using official Zid documentation and Partner Help Center content.

- **Your own partner account**, including apps, analytics, reviews, payouts, plans, team, webhooks, and partnership information.

This lets you access Zid information and partner account data without switching between the Partner Dashboard, developer documentation, Help Center, and other tools.

## Who can use Partner MCP

Partner MCP is available to **ZAM partner account holders**.

Each connection is linked to the partner account you authorize during sign-in.

Partner MCP can access information related to your partner account only. It does **not** provide access to merchant store data such as:

- Orders

- Customers

- Products

- Other merchant-specific store information

## What you can ask

After connecting your partner account, you can ask questions about your own business and about Zid integrations.

## Your partner account

You can ask about areas such as:

- App performance and install analytics

- Your apps and plans

- Merchant reviews and ratings

- Payouts and earnings

- Partner coupons

- Development stores

- Team information

- Webhooks

- Partnership status

- Your Partner MCP connection and activity

Examples:

- “How many installs did my app get this month?”

- “How many merchants uninstalled my app?”

- “What are my latest merchant reviews?”

- “What is my current app rating?”

- “What are my current payouts?”

- “Is any amount currently withheld?”

- “What plans does my app have?”

- “What webhooks are registered for my app?”

- “Show my development stores.”

- “What is my current partnership status?”

## Zid documentation and Partner Help Center

You can also ask questions about how Zid works.

Examples:

- “How do I authenticate Zid API requests?”

- “What is the difference between `Authorization` and `X-Manager-Token`?”

- “Why is my OAuth callback failing?”

- “What happens after I submit my app for review?”

- “How does the private app activation flow work?”

- “When are partner payouts processed?”

Answers based on Zid documentation include links to the relevant official source.

## Available Partner MCP areas

Partner MCP currently provides access to the following areas:

- Analytics

- Partner apps

- Plans

- Payouts

- Market reviews

- Partner coupons

- Development stores

- Team

- Webhooks

- Partnership information

- Partner Help Center and reference content

- Connection information and activity

Some supported capabilities may also allow you to perform actions through your AI assistant, depending on the available tool and your account permissions.

## Connect Partner MCP to your AI assistant

### 1. Get the Partner MCP address

- Sign in to the **Partner Dashboard (https://partners.zid.sa/)**.

- From the sidebar, select **AI Connections (https://partners.zid.sa/en-sa/partner/186/ai-connections)**.

- Under **Connect an assistant**, click **Copy address**.

The Partner MCP server address is:

`https://partners-mcp-server.zid.sa/mcp`

You do not need to create, copy, or store an API key. Authentication happens when you sign in to your Zid partner account.

(https://downloads.intercomcdn.com/i/o/u7vuis4c/2718267267/2137410b45f2df5e6179124d7de0/Screenshot+2026-10-07+at+2_50_16%E2%80%AFAM.png?expires=1794346200&signature=ccb7d9f5a61555d776e4fdd4eec23538d9dfdfa1745250009575c607a0a57a64&req=dicmHst4moNZXvMW1HO4zVmN0Ev6beN3nUvcLXsHZ%2FELQKM0EhY4eotLHiHk%0AD%2B9ab1949bH4h%2BpXeF0%3D%0A)

### 2. Add Partner MCP to your AI assistant

In Claude, Cursor, VS Code, or another MCP-compatible client:

- Add a **custom connector** or MCP server.

- Paste the Partner MCP address.

- Continue with the connection.

A browser window opens automatically.

### 3. Sign in and approve access

- Sign in to **Zid Partners**.

- Review the partner account and requested access shown on the consent screen.

- Approve the connection.

- Return to your AI assistant.

Your assistant can now work with the Zid partner account you authorized.

### 4. Confirm the connection

Try asking a simple question such as:

- “Who am I?”

- “How many apps do I have?”

- “Show my partner account information.”

You can also return to **Partner Dashboard → AI Connections** to confirm that the connection appears in your connection list.

## Session duration

A Partner MCP session remains active for **30 days**.

After the session expires, you will need to sign in and approve the connection again.

## Manage your AI connections

Go to **Partner Dashboard (https://partners.zid.sa/) → AI Connections (https://partners.zid.sa/en-sa/partner/186/ai-connections)** to manage your connected AI assistants.

For each connection, you can view information such as:

- Access

- When the connection was created

- When it was last used

- Current status

You can also review the connection activity and revoke access when the connection is no longer needed.

## Revoke access

To revoke a connection:

- Open **Partner Dashboard (https://partners.zid.sa/)→ AI Connections (https://partners.zid.sa/en-sa/partner/186/ai-connections)**.

- Find the connection you want to remove.

- Revoke its access.

Once revoked, the AI assistant can no longer access your Zid partner account through that connection.

You can reconnect later by adding Partner MCP again and completing the sign-in and consent flow.

## Example prompts

Here are some examples you can try after connecting Partner MCP.

### App performance

- “How many installs did my app get this month?”

- “Show my install and uninstall trend.”

- “Which of my apps has the highest number of installs?”

### Reviews

- “Show my latest merchant reviews.”

- “What complaints appear most often in my recent reviews?”

- “What is my current app rating?”

### Payouts

- “What are my current payouts?”

- “Is any amount withheld?”

- “Show my latest payout transactions.”

### Apps and plans

- “List my apps.”

- “What plans does my app have?”

- “What are the prices of my app plans?”

### Development and integration

- “What webhooks are registered for my app?”

- “Show my development stores.”

- “How do I authenticate against Zid APIs?”

- “Why is my OAuth callback failing?”

### Partnership

- “What is my current partnership status?”

- “Show information about my partner account.”

- “What does the Partner Help Center say about app review requirements?”

## FAQ

### Is Partner MCP the same as `zid-open-apis-mcp`?

**No.** `zid-open-apis-mcp` is a local, documentation-focused MCP server that helps you search and understand Zid developer documentation.

Partner MCP is authenticated with your Zid partner account and can answer questions about your own partner account data in addition to Zid documentation.

### Can Partner MCP access merchant store data?

**No.** Partner MCP is scoped to your partner account and does not provide access to merchant store information such as orders, customers, or products.

### Can I connect more than one AI assistant?

You can create and manage Partner MCP connections through the **AI Connections** section in the Partner Dashboard.

Each connection must be authorized using your Zid partner account.

### How long does the connection stay active?

The authenticated session lasts **30 days**.

After that, you need to sign in and approve the connection again.

### Can I revoke access?

**Yes.** Go to **Partner Dashboard → AI Connections**, find the relevant connection, and revoke its access.

### Does Partner MCP support shipping apps?

Yes. Partner MCP includes capabilities related to shipping apps.

### Does Partner MCP support themes?

Theme-related capabilities are currently available for supported areas, including:

- Reading theme reviews

- Publishing a theme review

- Creating coupons that apply to paid themes

- Viewing theme purchase transactions in payouts

- Handling supported theme agreement operations

Available functionality may vary depending on your partner account and permissions.

## Troubleshooting

### The sign-in window does not open

Make sure:

- You copied the correct Partner MCP address from **Partner Dashboard → AI Connections**.

- Your AI client supports remote MCP connections.

- Your browser is not blocking the sign-in window or redirect.

If needed, remove the connector and add it again.

### I signed in, but Partner MCP cannot access my account

Make sure you approved the correct Zid partner account during the consent flow.

You can also check the connection under **Partner Dashboard → AI Connections**.

### My connection stopped working

Partner MCP sessions expire after **30 days**.

Reconnect and sign in again to create a new authenticated session.

### The answer does not include my account data

Some questions may only use public Zid documentation.

Try asking explicitly about your own account, for example:

- “Show my apps.”

- “What are my current payouts?”

- “Show my latest merchant reviews.”

### I no longer want the AI assistant connected

Go to **Partner Dashboard → AI Connections** and revoke the relevant connection.

Related Articles

- Get Started with Partner Payouts

(https://help-partner.zid.sa/en/articles/8750045-get-started-with-partner-payouts)

- App Payouts

(https://help-partner.zid.sa/en/articles/11501759-app-payouts)

- Guide to Integrating Shipping Systems with the Zid Platform

(https://help-partner.zid.sa/en/articles/15544622-guide-to-integrating-shipping-systems-with-the-zid-platform)

- Create a Private App

(https://help-partner.zid.sa/en/articles/17348249-create-a-private-app)

- New: Explore Your Partner Dashboard

(https://help-partner.zid.sa/en/articles/17731590-new-explore-your-partner-dashboard)
