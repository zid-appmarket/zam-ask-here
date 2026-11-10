---
# Synced from https://help-partner.zid.sa/en/articles/15341721-invalid-tls-url-error-in-the-partner-dashboard
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: ph-invalid-tls-url-error-in-the-partner-dashboard
title: "Invalid 'TLS URL Error' in the Partner Dashboard"
product: zam
audience: all
status: verified
updated: 2026-06-02
source_url: https://help-partner.zid.sa/en/articles/15341721-invalid-tls-url-error-in-the-partner-dashboard
tags: [from-docs-site, partner-help-center]
language: en
---

> Learn how to troubleshoot and fix the “Invalid TLS URL” error when configuring webhook or endpoint URLs in the Partner Dashboard.
If you see an **“Invalid TLS URL”** error while configuring your webhook or endpoint URL in the Partner Dashboard, it means the system could not establish a secure and timely connection with your server.

To protect data integrity, the platform strictly validates all destination URLs before accepting them. This error usually happens because of an SSL/TLS issue, an unreachable server, or a slow connection response.

## Common Causes and How to Fix Them

**Cause**

**What It Means**

**How to Fix It**

Unsupported TLS version

Your server is using an older TLS version such as TLS 1.0 or TLS 1.1.

Update your server or reverse proxy configuration to support and prioritize TLS 1.2 or TLS 1.3.

Invalid SSL certificate

Your SSL certificate may be expired, self-signed, missing intermediate certificates, or not matching the domain.

Use a valid SSL certificate issued by a recognized Certificate Authority, such as Let’s Encrypt or DigiCert.

Connection timeout

Your server takes more than 5 seconds to acknowledge the connection and complete the TLS handshake.

Check your server resources and network performance. Make sure the server responds quickly.

Server is unreachable

The system cannot connect to your server because of DNS, firewall, ACL, or server availability issues.

Verify that your URL is publicly accessible and that your firewall or DDoS protection allows incoming traffic.

URL is not using HTTPS

The endpoint URL starts with `http://` instead of `https://`.

Update the URL in the dashboard and make sure it starts with `https://`.

## 1. Unsupported TLS Version

The platform only supports modern and secure encryption standards: **TLS 1.2** and **TLS 1.3**.

### Problem

If your server still uses older protocols such as **TLS 1.0** or **TLS 1.1**, the connection will be rejected automatically.

### Fix

Upgrade your web server or reverse proxy configuration to support and prioritize **TLS 1.2** or **TLS 1.3**.

This may apply to services such as:

- Nginx

- Apache

- Cloudflare

- Other reverse proxy or server configurations

## 2. Invalid, Expired, or Self-Signed SSL Certificate

The platform performs strict SSL certificate verification for security reasons.

### Problem

The TLS handshake may fail if your SSL certificate is:

- Expired

- Self-signed

- Missing intermediate certificate chains

- Not matching your domain name

### Fix

Make sure your server uses a valid SSL certificate issued by a recognized Certificate Authority, such as:

- Let’s Encrypt

- DigiCert

- Another trusted Certificate Authority

You can also use free online tools such as **SSL Labs** to verify your certificate chain.

## 3. Connection Timeout

The platform expects your server to respond quickly when establishing a secure connection.

### Problem

If your server takes longer than **5 seconds** to acknowledge the connection and complete the TLS handshake, the request will time out.

### Fix

- Check your server’s resource usage and network performance.

- Make sure your server is not performing heavy or synchronous processing before responding to the TLS handshake.

## 4. Target Server is Unreachable

The platform must be able to reach your server publicly.

### Problem

The connection may fail if:

- The domain name cannot be resolved to an IP address.

- Firewall rules or Access Control Lists are blocking incoming requests.

- The server or application is offline.

- DDoS protection or security rules are blocking the request.

### Fix

- Verify that your URL is publicly accessible.

- Also, make sure your firewall, DDoS protection, Cloudflare, AWS WAF, or similar service allows incoming traffic to your endpoint.

## 5. URL is Not Using HTTPS

The endpoint URL must use a secure protocol.

### Problem

The URL entered in the Partner Dashboard does not start with `https://`.

### Fix

Check the URL and make sure it begins with:

```
https://
```

Instead of:

```
http://
```

## How to Test Your Endpoint

Before updating your dashboard configuration, you can test your endpoint from your terminal using `curl`.

Replace the sample URL with your actual endpoint:

```
curl -Iv https://your-server.com/endpoint
```

## What to Check in the Output

After running the command, review the output and check the following:

**What to Check**

**Expected Result**

TLS version

The output should show `TLSv1.2` or `TLSv1.3`.

SSL certificate

There should be no certificate verification errors.

Connection time

The connection should complete well under the 5-second limit.

For example, look for lines similar to:

```
SSL connection using TLSv1.2
```

or:

```
SSL connection using TLSv1.3
```

Also make sure the output does not include errors such as:

```
SSL certificate problem
```

## Summary:

To resolve the **“Invalid TLS URL”** error, make sure your endpoint:

- Uses `https://`

- Supports TLS 1.2 or TLS 1.3

- Has a valid SSL certificate

- Is publicly accessible

- Responds within 5 seconds

Once these checks are complete, update the URL again in the Partner Dashboard.

##

Related Articles

- Old: Explore the Previous Partner Dashboard

(https://help-partner.zid.sa/en/articles/8635324-old-explore-the-previous-partner-dashboard)

- New: Explore Your Partner Dashboard

(https://help-partner.zid.sa/en/articles/17731590-new-explore-your-partner-dashboard)
