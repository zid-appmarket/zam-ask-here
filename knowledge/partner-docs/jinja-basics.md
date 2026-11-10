---
# Synced from https://docs.zid.sa/jinja-basics-1379353m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-jinja-basics
title: "Jinja Basics"
product: theme_market
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/jinja-basics-1379353m0
tags: [from-docs-site, partner-docs]
language: en
---

> Jinja Basics - Zid Docs
# Jinja Basics

Zid themes are powered by the **Jinja** templating engine. Making it easy to embed dynamic data and logic into your theme design while keeping layouts flexible and reusable.

Check out the full Jinja Documentation (https://jinja.palletsprojects.com/en/stable/) to discover all available syntax, tags, filters, and features you can apply to build fully customizable and flexible layouts.

## Understanding the Basics #

Jinja uses two main syntax forms:

1 .

**Output variables** — `{{ ... }}` Used to display the value of a variable in the template.

```
``
```

2 .

**Control statements** — `{{ ... }}`

Used for logic, loops, and template structure.

```
``
```

📚 Reference: Jinja Template Basics (https://jinja.palletsprojects.com/en/stable/templates/)

## Common Jinja Tags #

Tag Purpose

`extends` Inherit from a base template

`include` Insert another template inside this one

`for` Loop over sequences

`if`/ `elif` / `else` Conditional logic

`set` Assign variables

## Template Inheritance (extends and block) #

Use extends to base your template on another (usually a layout), and block to fill in or override sections.

```
``
```

**In this example:**

The template inherits the overall HTML structure from main.jinja.

The title and content blocks are overridden to provide page-specific content.

📚 Reference: Jinja Template Inheritance (https://jinja.palletsprojects.com/en/stable/templates/#template-inheritance)

## Base Layout Example #

```
``
```

Child templates extend this file and override blocks as needed.

## Including Templates (include) #

Use include to insert another template’s contents, similar to a “copy-paste” at render time.

```
``
```

📚 Reference: Jinja Include Statement (https://jinja.palletsprojects.com/en/stable/templates/#include)

## Conditional Logic (if, elif, else) #

```
``
```

📚 Reference: Jinja If Statement (https://jinja.palletsprojects.com/en/stable/templates/#if)

## Loops (for) #

```
``
```

📚 Reference: Jinja For Statement (https://jinja.palletsprojects.com/en/stable/templates/#for)

## Variable Assignment (set) #

```
``
```

## Filters #

Filters modify values before rendering. Zid supports Jinja’s core filters, plus some platform-specific ones.

Examples:

```
``
```

📚 Reference: List of Built-in Jinja Filters (https://jinja.palletsprojects.com/en/stable/templates/#list-of-builtin-filters)

## Functions #

Functions perform logic or transformations in templates. Jinja provides built-in functions, and Zid adds platform-specific ones (e.g., url_for, asset_url).

```
``
```

📚 Reference: Built-in Jinja Functions (https://jinja.palletsprojects.com/en/stable/templates/#list-of-global-functions)

## Null safety #

Jinja templating engine can handle accessing chained null elements safely, however it has limitations

for example trying to iterate on a null element or trying to devide by zero will break the rendering

Jinja provides builtin tests to protect against these mistakes

so you can check if a variable is iterable by testing

```
``
```

📚 Refernce: Jinja's builtin tests (https://jinja.palletsprojects.com/en/stable/templates/#list-of-builtin-tests)

Modified at 2026-07-30 11:49:13

Previous

Overview

Next

Vitrin's Jinja Extensions
