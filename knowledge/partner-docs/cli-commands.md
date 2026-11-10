---
# Synced from https://docs.zid.sa/cli-commands-1390556m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-cli-commands
title: "CLI Commands"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/cli-commands-1390556m0
tags: [from-docs-site, partner-docs]
language: en
---

> CLI Commands - Zid Docs
# CLI Commands

The **Vitrin CLI (https://www.npmjs.com/package/@zidsa/vitrin-cli)** helps you authenticate, create, build, preview, and manage themes for Zid stores. Each command is straightforward, with copy-ready examples below.

## 🔑 Authentication #

Authenticate your CLI with Zid Partner Dashboard.

```
``
```

Opens your browser for the OAuth flow and saves credentials locally.

**Example:**

```
``
```

## 🎨 Theme Creation #

Create a new theme from a template.

```
``
```

**Options:**

`-t`, `--template <template>` → Template to use (basic, minimal, advanced)

`--no-git` → Skip Git initialization

**Example:**

```
``
```

## Theme Push #

Builds and pushes your theme to Zid servers, creating or updating the theme.

```
``
```

**Options:**

`-s`, `--store` `<email>` → Dev store email to install on

`-a`, `--activate` → Activate theme after installation

`-v`, `--version` `<version>` → Version number (default: from theme.json)

`-c`, `--changelog` `<text>` → Version changelog

**Example:**

```
``
```

## 🛠️ Building Themes #

Build your theme into a distributable `.zip` package.

```
``
```

**Example:**

```
``
```

## 👀 Preview on Dev Store #

Preview your theme on a development store for testing.

```
``
```

**Options:**

`-s`, `--store` `<store-id>` → Dev store email

`--build` → Build theme before previewing

**Example:**

```
``
```

## 📋 List Resources #

List available themes or dev stores.

```
``
```

**Example:**

```
``
```

## 📦 Theme Installation #

Install a specific theme version on a store.

```
``
```

**Example:**

```
``
```

## 🚀 Theme Activation #

Activate an installed theme on a store.

```
``
```

**Example:**

```
``
```

## Temporary themes settings editing #

Since we got a little too excited to share the new themes with you when the new theme editor is still cooking, here's a quick way to upload drafted settings while building the theme through the cli:

with your theme files, add the following:

```
``
```

in a .json file with the template name, you can add settings for the template that will be uploaded to the store during `preview`.

in `home.json` you can add the sections settings that you want reflected in the home page like so:

```
` {
"components" : {
"ar" : [
{
"template" : "sections/....jinja" ,
"settings" : ... ,
}
] ,
"en" : [
...
]
}
} `
```

checkout https://github.com/zidsa/soft-theme-vitrin/ (https://github.com/zidsa/soft-theme-vitrin/) for reference...

p.s. you can give you schema an LLM and ask it to give placeholder values

Sorry for the inconvenince, we promise to make it worthwhile ;)

Modified at 2026-07-30 11:49:13

Previous

Introduction

Next

Performance
