---
# Synced from https://docs.zid.sa/our-custom-mcp-server-1363315m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-our-custom-mcp-server
title: "Our custom MCP server"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/our-custom-mcp-server-1363315m0
tags: [from-docs-site, partner-docs]
language: en
---

> Our custom MCP server - Zid Docs
# Our custom MCP server

Partners can connect to our MCP server to fetch this API documentation and get answers for their inquiries about the integration.

### Configuring the MCP Client #

**Prerequisites**

Node.js environment installed (version 18 or higher, latest LTS recommended)

Any IDE that supports MCP:

Cursor

VSCode + Cline extension

Others

In your AI-powered IDE, Add the config of the MCP server to the json config file of the MCP servers. This is a sample code snippet of the json file:

```
` {
"mcpServers" : {
"zid-open-apis-mcp" : {
"command" : "npx" ,
"args" : [
"-y" ,
"zid-open-apis-mcp"
]
}
}
} `
```

### Verify Configuration #

Test the connection by asking the AI (in Agent mode):

```
`Based on the open apis doc, explain how merchant onboarding works`
```

Successful connection is confirmed when AI returns to you information based on the API documentation context.

Modified at 2026-07-30 11:49:13

Previous

Zid SDKs

Next

Zid AI Agent Skill
