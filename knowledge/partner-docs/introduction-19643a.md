---
# Synced from https://docs.zid.sa/introduction-1379356m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-introduction-19643a
title: "Introduction"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/introduction-1379356m0
tags: [from-docs-site, partner-docs]
language: en
---

> Introduction - Zid Docs
# Introduction

The **Vitrin CLI (https://www.npmjs.com/package/@zidsa/vitrin-cli)** is a command-line tool for Zid theme developers. It helps you **develop, validate, and publish** themes to the Zid platform directly from your local environment.

### With the CLI, you can: #

**✨ Visual Dashboard**

Quick access to all commands

Real-time build status tracking

Theme and authentication information at a glance

**🔨 Build & Development**

Visual build progress with step-by-step feedback

Instant theme preview on dev stores

**🎨 Theme Management**

Create, browse and select existing themes

One-click theme preview deployment

Automatic theme detection in current directory

**🔐 Authentication & Settings**

Easy login/logout flow

Configure API endpoints

Persistent settings management

## Installing the CLI #

📌

https://www.npmjs.com/package/@zidsa/vitrin-cli (https://www.npmjs.com/package/@zidsa/vitrin-cli)

```
``
```

## Quick Start #

### Launch the interactive TUI (recommended) #

```
``
```

### Use CLI Commands Directly: #

```
``
```

## Configuration #

### Environment Variables #

`VITRIN_API_URL` - API endpoint (default: https://api.zid.sa (https://api.zid.sa))

`VITRIN_PARTNER_URL` - Partner dashboard URL (default: https://partner.zid.sa (https://partner.zid.sa))

`LOG_LEVEL` - Logging level (debug, info, error)

### Debug Mode #

Run with detailed logging for troubleshooting:

```
``
```

### File Structure #

Expected theme structure:

```
``
```

## Authentication #

Authentication tokens are stored in `~/.vitrin/config.json`.

**To logout:**

```
``
```

## Troubleshooting #

**Found a bug or unexpected behavior?** Please report issues on our GitHub tracker: zidsa/vitrin-cli/issues (https://github.com/zidsa/vitrin-cli/issues)

### Authentication Issues #

```
``
```

### Build Failures #

```
``
```

**Common causes:**

Missing required directories (`assets/`, `templates/`)

Invalid or missing `package.json`

`.DS_Store` files (these are auto-cleaned during build)

### Preview Errors #

```
``
```

**Common causes:**

Expired authentication token → run `vitrin login`

Invalid store ID → check using `vitrin list stores`

Theme name conflict → CLI auto-generates a unique name

Explore Vitrin CLI Commands (https://docs.zid.sa/cli-commands-1390556m0) page for detailed syntax and options for each command.

Modified at 2026-07-30 11:49:13

Previous

Vitrin's Jinja Extensions

Next

CLI Commands
