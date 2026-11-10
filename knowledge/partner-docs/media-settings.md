---
# Synced from https://docs.zid.sa/media-settings-1379346m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-media-settings
title: "Media Settings"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/media-settings-1379346m0
tags: [from-docs-site, partner-docs]
language: en
---

> Media Settings - Zid Docs
# Media Settings

**Common fields**

Field Type Description

id string Unique identifier of the setting (e.g., "images", "title").

label object {ar,en} Input label shown to the merchant.

type string Input type (e.g., "text", "textarea", "image", "number", "color", "list").

default any Default value when none is provided.

icon text Optional reference to an icon (e.g. `fal fa-box`).

### Image #

**Extra fields**

Field Type Description

info text Optional informational below upload box.

Allows upload of an image.

```
` {
"type" : "image" ,
"id" : "image" ,
"label" : {
"ar" : "صورة" ,
"en" : "Image"
} ,
"info" : {
"ar" : "ارفع صورة بحجم ٢٠٠ *٢٠٠" ,
"en" : "Upload an image of size 200x200"
}
} `
```

Output

### Video #

**Extra fields**

Field Type Description

info text Optional informational below upload box.

Allows upload of a video.

```
` {
"type" : "video" ,
"id" : "video" ,
"label" : {
"ar" : "فيديو" ,
"en" : "Video"
}
"info" : {
"ar" : "mp4 اقصى حجم 10MB" ,
"en" : "max upload size 10MB"
}
} `
```

Modified at 2026-07-30 11:49:13

Previous

Input Settings

Next

Form Controls Settings
