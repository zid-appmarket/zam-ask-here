---
# Synced from https://docs.zid.sa/conditional-visibility-1379350m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-conditional-visibility
title: "Conditional Visibility"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/conditional-visibility-1379350m0
tags: [from-docs-site, partner-docs]
language: en
---

> Conditional Visibility - Zid Docs
# Conditional Visibility

You can toggle the visibility of settings by adding the field `visible_if` to any setting. The following example shows a text input that relies on the value of the checkbox to be visible.

```
` {
... ,
"sections" : [
{
...
"settings" : [
{
"type" : "checkbox" ,
"id" : "hide_dots" ,
"label" : {
"ar" : "إخفاء النقاط" ,
"en" : "Hide dots"
} ,
"default" : true
} ,
{
"type" : "text" ,
"id" : "text_input" ,
"label" : { ... } ,
"visible_if" : {
"hide_dots" : false
}
}
]
}
]
}
`
```

Modified at 2026-07-30 11:49:13

Previous

Additional Settings

Next

Migrating twig settings schema
