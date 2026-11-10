---
# Synced from https://docs.zid.sa/sdk-popups-integration-guidelines-1946485m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-sdk-popups-integration-guidelines
title: "SDK Popups – Integration Guidelines"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/sdk-popups-integration-guidelines-1946485m0
tags: [from-docs-site, partner-docs]
language: en
---

> SDK Popups – Integration Guidelines - Zid Docs
# SDK Popups – Integration Guidelines

### Description #

This document provides general guidelines, known issues, and recommended fixes for integrating **SDK popups** within themes and custom UI components.

It is a **living reference** and will be continuously updated as new common issues are discovered and solutions are introduced, ensuring consistent and reliable integrations over time.

### Popup & Modal Coordination #

SDK popups may be triggered from various UI contexts such as sidebars, drawers, or other overlay components. Improper coordination between these layers can lead to unstable behavior.

### Common Issue: Focus & Overlay Conflicts #

Opening an SDK popup while another modal-type component is still active may cause:

Focus conflicts

Unresponsive inputs

JavaScript errors

Unexpected or broken UI behavior

### Recommended Fix #

Before opening any SDK popup, ensure that no other modal-type component is currently active.

Close any of the following if present:

Sidebars / Drawers

Modals / Popups

Any overlay component that manages focus or keyboard interaction

### Example #

```
``
```

Modified at 2026-07-30 11:49:13

Previous

Events

Next

Custom Styles Guide
