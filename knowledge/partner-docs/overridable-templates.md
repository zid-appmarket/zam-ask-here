---
# Synced from https://docs.zid.sa/overridable-templates-1650867m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-overridable-templates
title: "Overridable Templates"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/overridable-templates-1650867m0
tags: [from-docs-site, partner-docs]
language: en
---

> Overridable Templates - Zid Docs
# Overridable Templates

Some templates are provided **out of the box** and are fully functional with best-practice UX. We **recommend using the defaults** in most cases, because these templates evolve frequently and automatically receive improvements.

If your theme has a use case that **requires** custom behavior or UI, you can override any of the templates below by adding a file with the **same path and filename** in your theme.

## Available overrides #

Template path (add this to your theme to override)

`templates/account_profile.jinja`

`templates/account_orders.jinja`

`templates/account_wishlist.jinja`

`templates/loyalty_program.jinja`

### Information #

Template Purpose Route

**account_profile.jinja** The customer profile page. `/account`

**account_orders.jinja** Displays customer's orders. `/account/orders`

**loyalty_program.jinja** Display customer loyalty wallet and points history. `/account/loyalty-program`

**account_wishlist.jinja** Customer's wishlist page. `/account/wishlist` or `/wishlist`

These ship enabled by default. If you **don’t** add a file, the system version is used automatically.

## How overriding works #

1 .

**Create the file** in your theme at the exact path shown above.

2 .

Your file takes precedence over the built-in version.

3 .

Remove or rename your file any time to revert to the system default.

All overridable templates should **extend** your base layout and can use the same sections/components you use elsewhere:

```
`{% extends "layout.jinja" %}

{% block page_title %}My Account{% endblock %}

{% block content %}
<section class="account">
<h1>{{ _("Profile") }}</h1>
{# Your custom UI here. Built-in data objects remain available. #}
</section>
{% endblock %}`
```

Modified at 2026-07-30 11:49:13

Previous

Overview

Next

Legacy Templates
