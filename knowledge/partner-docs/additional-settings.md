---
# Synced from https://docs.zid.sa/additional-settings-1379349m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-additional-settings
title: "Additional Settings"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/additional-settings-1379349m0
tags: [from-docs-site, partner-docs]
language: en
---

> Additional Settings - Zid Docs
# Additional Settings

**Common fields**

Field Type Description

id string Unique identifier of the setting (e.g., "images", "title").

label object {ar,en} Input label shown to the merchant.

type string Input type (e.g., "text", "textarea", "image", "number", "color", "list").

default any Default value when none is provided.

icon text Optional reference to an icon (e.g. `fal fa-box`).

### List #

**Extra fields**

Field Type Description

settings list[Any] List of settings.

max_items int Maximum number of items allowed. Useful to not clutter the UI in some cases.

List of settings. For example a list of images.

```
` {
"type" : "list" ,
"id" : "list_of_settings" ,
"label" : {
"ar" : "" ,
"en" : "List of Settings"
} ,
"max_items" : 4 ,
"settings" : [
{
"type" : <Any Setting Type>
...
} ,
...
]
} `
```

### Fieldset #

**Extra fields**

Field Type Description

settings list[Any] List of settings.

expandable bool Flag to make the grouping expandable.

A grouping of settings. Similar to List, but is different in that the user is not allowed to add settings, its just an organizational grouping of the settings.

```
` {
"type" : "fieldset" ,
"id" : "links" ,
"label" : {
"ar" : "روابط مهمة" ,
"en" : "Links"
} ,
"expandable" : true ,
"settings" : [
{ ... } ,
...
]
} `
```

### Snippet #

Accepts arbitrary HTML values.

```
` {
"type" : "snippet" ,
"id" : "some_snippet" ,
"label" : {
"ar" : "" ,
"en" : "Some HTML"
}
} `
```

Modified at 2026-07-30 11:49:13

Previous

Products Settings

Next

Conditional Visibility
