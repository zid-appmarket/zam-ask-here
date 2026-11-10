---
# Synced from https://docs.zid.sa/localization-jinja-v-twig-1379352m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-localization-jinja-v-twig
title: "localization (jinja v. twig)"
product: theme_market
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/localization-jinja-v-twig-1379352m0
tags: [from-docs-site, partner-docs]
language: en
---

> localization (jinja v. twig) - Zid Docs
# localization (jinja v. twig)

# Gettext Localization (.po) with Jinja2 (`jinja2.ext.i18n`) #

Localization isn’t just about “show a different string.” It’s about giving translators a first-class workflow, handling plural rules correctly (especially in languages like Arabic), and keeping your templates readable. Gettext does all of this with a simple idea: your templates contain **literal source strings**, and `.po` files map those source strings to translated text. Jinja’s `jinja2.ext.i18n` (https://jinja.palletsprojects.com/en/stable/extensions/#i18n-extension) extension makes this flow natural and ergonomic.

## What a `.po` file really is #

A `.po` file is a human-editable catalog that pairs each source string (`msgid`) with its translation (`msgstr`). Translators also see comments, fuzzy flags, and plural rules, and they use established tools to manage quality. For runtime speed, `.po` files are compiled into binary `.mo` files—no app logic required.

For example, an Arabic catalog might contain both a simple string and a pluralized string:

```
`msgid "Add to cart"
msgstr "أضف إلى السلة"

# Plural example with a numeric placeholder
msgid "%(n)s item"
msgid_plural "%(n)s items"
msgstr[0] "لا عناصر"
msgstr[1] "عنصر واحد"
msgstr[2] "عنصران"
msgstr[3] "%(n)s عناصر"
msgstr[4] "%(n)s عنصرًا"
msgstr[5] "%(n)s عنصر"`
```

You don’t hard-code grammar in your app; the locale’s plural rules guide which `msgstr[index]` is chosen.

## Wiring Gettext into Jinja #

Inside templates, write **natural, literal strings**:

```
`{{ _("Add to cart") }}

{% trans count=n %}{{ count }} item{% pluralize %}{{ count }} items{% endtrans %}

{% trans store=store_name %}Welcome to {{ store }}!{% endtrans %}

{# Contextual disambiguation: same English, different meaning #}
{{ pgettext("button", "Open") }}
{{ pgettext("verb", "Open") }}`
```

The key to effective extraction is keeping messages **literal** (no string concatenation that hides the text from extractors) and passing variables in via `{% trans %}` bindings.

## Extraction → Translation → Compilation (Babel flow) #

Gettext shines because translators don’t need source code—they work from a POT template that your build generates. A typical workflow with Babel looks like this:

```
``
```

A minimal `babel.cfg` to make Jinja extraction work:

```
``
```

This means you write strings once, run extraction, and translators get a clean list of what needs attention—no spelunking through your codebase.

## How this differs from the old `locals.*` approach #

Previously, with Twig, you passed a context mapping like `locals.*` to templates and accessed keys such as `{{ locals.add_to_cart }}`. That “dictionary of messages” works in a pinch, but it shifts localization responsibilities onto application code and template authors:

**No native plural rules:** You had to hand-roll logic for “1 item” vs “5 items”—a non-starter for languages with complex plural categories like Arabic.

**No disambiguation:** When the same English string has multiple meanings, you ended up inventing key suffixes (`open_button`, `open_action`) and policing consistency manually.

**No automatic extraction:** The app never had a guaranteed, up-to-date catalog of translatable strings. It was easy to ship with missing or stale keys.

**Weak translator tooling:** Translators couldn’t rely on standard PO editors, translation memory, or automatic QA. Everything looked like arbitrary keys.

**Brittle fallbacks:** You had to implement your own fallback chains (e.g., `ar-SA → ar → en`), and missing keys could silently break or degrade UX.

Gettext flips that model. Templates contain canonical, **human-readable source text**; extraction discovers those strings automatically; translators enjoy first-class tools and plural logic; and your runtime simply looks up the right translation. It’s both cleaner for developers and kinder to translators.

## Migrating from `locals.*` to Gettext #

Think in terms of **source text**, not keys. For each key that used to be looked up, write the intended English phrase directly in the template. Then rely on `{% trans %}` and `ngettext` to handle variables and plurals.

**Simple key → literal string**

Old:

```
`{{ locals.add_to_cart }}`
```

New:

```
`{{ _("Add to cart") }}`
```

**Manual plural logic → built-in pluralization**

Old (app logic or ternaries in template):

```
`{{ n == 1 ? locals.one_item : locals.many_items }}`
```

New (locale-aware):

```
`{% trans count=n %}{{ count }} item{% pluralize %}{{ count }} items{% endtrans %}`
```

**Variables inside messages**

Old:

```
`{{ locals.welcome }} {{ store_name }}`
```

New:

```
`{% trans store=store.name %}Welcome to {{ store }}!{% endtrans %}`
```

**Disambiguation by key suffix → semantic context**

Old:

```
`{{ locals.open_button }}
{{ locals.open_action }}`
```

New:

```
`{{ pgettext("button", "Open") }}
{{ pgettext("action", "Open") }}`
```

After updating templates, run extraction and compilation. Your translators will see exactly the strings you added, and the app will pick up translations once `.mo` files are compiled.

## Practical tips that save time #

Keep HTML **outside** the translatable text when possible (translate text, not tags), avoid building messages dynamically (concatenation hides strings from extractors), and remember to recompile after any change to `.po` files. With those habits, Gettext + Jinja gives you a clean, scalable, and translator-friendly localization system—far more robust than passing a bespoke `locals.*` mapping into your views.

Modified at 2026-07-30 11:49:13

Previous

Migrating twig settings schema

Next

Overview
