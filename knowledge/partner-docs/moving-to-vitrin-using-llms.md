---
# Synced from https://docs.zid.sa/moving-to-vitrin-using-llms-1379318m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-moving-to-vitrin-using-llms
title: "Moving to Vitrin Using LLMs"
product: theme_market
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/moving-to-vitrin-using-llms-1379318m0
tags: [from-docs-site, partner-docs]
language: en
---

> Moving to Vitrin Using LLMs - Zid Docs
# Moving to Vitrin Using LLMs

This guide walks you through migrating an existing theme to the Vitrin system using our pre-prepared LLM prompt.

## Prerequisites #

**Before starting the migration:**

Ensure you have the full source code of your theme.

Back up the original theme files.

Have a working LLM interface (e.g., OpenAI API, internal LLM tooling).

Access to Vitrin theme documentation for reference.

**Familiarity with:**

HTML, CSS, JavaScript

Template engine syntax used in both old and Vitrin systems

Any API changes in Vitrin

## Migration Steps #

The migration process will automate most of the conversion work, but **manual validation** and testing remain essential.

Note that your mileage may vary with the following instructions due to the behaviors of different LLMs and context size limitations.

### Step 1 – **Prepare Your Theme Code** #

Gather all relevant files: templates, assets, configuration files.

Find your agentic coding tool of choice (we recommend using Claude Code given that most of our testin was done on it).

### Step 2 – **Load the Migration Prompt** #

We have provided a pre-written LLM prompt to guide the transformation of your theme code.

Prompt 1:

```
`Convert the following twig theme to Jinja based on the following docs:

Introduction: https://docs.zid.sa/theme-development
Architecture: https://docs.zid.sa/architecture-1379322m0
Mappings: https://docs.zid.sa/store-settings-mapping-1379317m0
Twig to Jinja: https://docs.zid.sa/twig-to-jinja-1379319m0
Breaking changes: https://docs.zid.sa/breaking-changes-1379320m0
API integrations:
https://docs.zid.sa/cart-1475306m0
https://docs.zid.sa/products-1475307m0
https://docs.zid.sa/schema-files-1702180m0
New schema format:
https://docs.zid.sa/schema-files-1702180m0`
```

Prompt 2:

```
`Find all occurrences of the settings described here and update them to the new paths:
https://docs.zid.sa/store-settings-mapping-1379317m0

Make sure that the settings are store.settings.*
`
```

**Using the Vitrin Theme Migration Prompt:**

Convert the theme to match Vitrin's template structure.

Adjust settings schema to match Vitrin configuration format.

Ensure file naming conventions follow Vitrin standards.

Includes the new required tags that will add the appropriate headers and scripts.

We recommend that you read the migration documents and re-prompt the agent if it missed any of the of the instructions due to context window.

### Step 3 – **Apply Manual Fixes** #

Even after running the LLM migration, you will likely need to:

Adjust logic where the LLM’s output may not fully reflect intended functionality.

Correct dynamic content rendering.

Verify responsive design and mobile compatibility.

Replace or adjust any deprecated code.

### Step 4 – **Test Thoroughly** #

**Visual Testing**

Check layout, typography, colors, and images.

Compare with the original theme design.

**Functional Testing**

Verify navigation menus, search, product listings, and checkout flow.

Test all interactive components (sliders, forms, modals, etc.).

**Performance Testing**

Refer to https://docs.zid.sa/performance-1379358m0 (https://docs.zid.sa/performance-1379358m0)

Modified at 2026-07-30 11:49:13

Previous

Legacy Theme Migration

Next

Twig to Jinja
