---
# Synced from https://docs.zid.sa/zid-agent-skill
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-zid-agent-skill
title: "Zid AI Agent Skill"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/zid-agent-skill
tags: [from-docs-site, partner-docs]
language: en
---

> Zid AI Agent Skill - Zid Docs
# Zid AI Agent Skill

The **Zid AI Agent Skill** is an open-source, Markdown-based skill that helps compatible AI coding agents build and troubleshoot Zid integrations using Zid’s official documentation.

It provides Zid-specific guidance for OAuth 2.0, multi-tenant token storage, Merchant API requests, error handling, rate limits, and integration troubleshooting. You can use it with Claude, Claude Code, opencode, and other coding agents that support custom skills.

The skill reduces the risk of generated code using incorrect authentication patterns or nonexistent endpoints by directing the agent to verify implementation details against the latest Zid documentation.

## Who should use the Zid AI Agent Skill? #

The skill is designed for developers who use AI coding agents to:

Build public or private Zid apps.

Implement the Zid OAuth installation flow.

Store credentials securely for multiple merchant stores.

Integrate with Zid Merchant APIs.

Diagnose authentication and API errors.

Prepare technical issue reports for the Zid team.

Find the correct Zid API documentation before implementing a feature.

## Why use the Zid AI Agent Skill? #

### Follow Zid’s actual OAuth flow #

The skill explains Zid’s OAuth 2.0 Authorization Code flow, including authorization redirects, callback handling, token exchange, token refresh, and secure credential storage.

It also highlights an important Zid authentication requirement: Merchant API requests generally require two separate headers:

`Authorization`

`X-Manager-Token`

These headers represent different values and must not be treated as interchangeable.

For complete authentication requirements, see **Authorization** in the Zid developer documentation.

### Reduce incorrect or invented API usage #

The skill instructs the coding agent to check the live Zid documentation before implementing an endpoint.

This reduces the chance of the agent:

Inventing an endpoint that does not exist.

Using an outdated request structure.

Sending the wrong authentication headers.

Assuming unsupported API behavior.

Using Storefront API conventions for Merchant API requests.

The live Zid documentation remains the source of truth whenever it differs from information included in the skill.

### Support multi-tenant Zid apps #

A Zid app may be installed by many independent merchants. Each merchant has a separate store and separate credentials.

The skill provides patterns for:

Storing tokens by `store_id`.

Keeping merchant credentials isolated.

Avoiding cross-store token leakage.

Encrypting sensitive credentials at rest.

Refreshing tokens before they expire.

Removing or invalidating credentials after an app is uninstalled.

These patterns help developers design integrations that can scale safely from one merchant installation to many.

### Handle errors and rate limits correctly #

The skill includes guidance for:

Zid API response formats.

Common HTTP status codes.

Validation errors.

Authentication and authorization failures.

`429 Too Many Requests` responses.

Retry and backoff behavior.

Escalating unresolved issues to Zid’s technical team.

Zid currently applies API rate limits per application and store. Always check the **Rate Limiting** documentation for the latest policy before implementing request queues, retries, or polling.

## Which AI coding agents are supported? #

The skill can be used with agents that support custom skills or instruction directories.

Agent Installation method

Claude Upload or save the packaged skill through the custom-skills workflow available in your Claude workspace.

Claude Code Clone or copy the skill into the project or global Claude skills directory.

opencode Copy the skill folder into the directory scanned by opencode for custom skills.

Other compatible agents Copy the skill into the agent’s supported skills or instructions directory.

The exact installation workflow may vary depending on the agent and its version.

## How do I install the Zid AI Agent Skill? #

### Install it in Claude Code #

From the root directory of your project, run:

```
``
```

This installs the skill for the current project.

To make it available globally, clone or copy it into your global Claude skills directory:

```
``
```

After installation, restart or reload Claude Code so it can detect the new skill.

### Install it in Claude #

Download the packaged `.skill` file from the Zid Agent Skill GitHub repository.

Upload or save the skill using the custom-skills workflow available in your Claude workspace or organization.

### Install it in opencode or another compatible agent #

Clone or download the repository, then copy the `zid-api-integration` folder into the directory your agent scans for skills.

The skill is Markdown-based and does not require a runtime dependency, SDK, or package installation.

## How does the Zid AI Agent Skill work? #

The repository contains a primary `SKILL.md` file and a set of supporting references.

```
`zid-api-integration/
├── SKILL.md
└── references/
├── oauth-flow.md
├── multi-tenant-architecture.md
├── error-handling.md
├── endpoint-index.md
└── troubleshooting-tools.md`
```

`SKILL.md` is the entry point. It defines the core integration principles, workflow, and situations where the coding agent should ask the developer for more information.

The supporting reference files provide additional details for specific tasks. A compatible agent can load only the references relevant to the current request rather than placing all Zid integration information into every conversation.

For example, when you ask the agent to implement an OAuth callback, it can use the OAuth and multi-tenant references. When you ask about a failed API request, it can use the error-handling and troubleshooting references.

## What does the skill cover? #

Area Guidance included

OAuth 2.0 Authorization Code flow, authorization redirects, callback handling, token exchange, refresh, and expiry handling.

Authentication headers Correct use of `Authorization` and `X-Manager-Token` for Merchant API requests.

Multi-tenancy Per-merchant credential storage, store-level isolation, and secure token handling.

Token refresh Proactive token-refresh patterns intended to prevent avoidable authentication failures.

Error handling Response formats, HTTP status codes, validation errors, authentication errors, retries, and escalation guidance.

Rate limits Guidance for handling request limits, `429` responses, retry delays, and backoff.

API discovery A categorized map of Merchant APIs, Storefront APIs, Webhooks, and Payments documentation.

Troubleshooting Guidance for diagnosing OAuth and Partner Dashboard integration problems.

Escalation A minimal structure for reporting reproducible integration issues to Zid’s technical team.

## How do I use the skill? #

After installation, describe the Zid integration task normally in your coding agent.

Example prompts include:

```
`Build an Express backend that handles the Zid OAuth installation flow and stores tokens separately for each merchant.`
```

```
`Why am I receiving a 401 response from the Zid orders endpoint even though my token appears valid?`
```

```
`Create a scheduled job that refreshes Zid tokens before they expire.`
```

```
`Show me the correct authentication headers for a Zid Merchant API request.`
```

```
`Find the official Zid endpoint for retrieving products and generate a Python example.`
```

```
`Help me prepare a reproducible report for an API issue that I need to send to Zid’s technical team.`
```

A compatible agent should recognize that the task involves Zid and apply the skill. Agent behavior may vary, so you can also explicitly ask it to use the Zid API integration skill.

## What is the source of truth? #

The Zid developer documentation is the source of truth for all API behavior.

The skill provides integration principles, reference maps, and common implementation patterns. However, API documentation may change more frequently than the repository.

Before generating or deploying an API integration, the agent should verify the following against the live endpoint documentation:

HTTP method and URL.

Required OAuth scopes.

Authentication headers.

Path and query parameters.

Request body schema.

Response schema.

Supported values.

Rate-limit behavior.

Error responses.

When the live documentation and the skill disagree, use the live documentation and report the outdated skill content through the GitHub repository.

## Does the skill replace the Zid MCP server? #

No. The Zid AI Agent Skill and the Zid MCP server serve related but different purposes.

The **Zid AI Agent Skill** provides reusable instructions, architectural guidance, troubleshooting patterns, and Zid-specific integration rules inside the coding agent’s context.

The **Zid MCP server** allows supported AI tools to retrieve Zid API documentation and answer questions using documentation provided through an MCP connection.

They can be used together:

Use the skill to guide how the agent designs and implements Zid integrations.

Use the MCP server to help the agent retrieve relevant documentation during the task.

See **Our custom MCP server** for setup instructions.

## Scope and limitations #

The skill primarily covers OAuth-based Merchant API integrations and apps managed through the Zid Partner Dashboard.

It can direct developers to Storefront, Webhook, Payments, and other Zid documentation, but those systems may have separate authentication models and implementation conventions.

The skill intentionally does not include complete, production-ready templates for every programming language. It provides reusable patterns that an AI agent can adapt to Node.js, Python, PHP, or another supported stack.

The skill also does not:

Execute API requests by itself.

Store or manage production credentials.

Replace validation against the live documentation.

Guarantee that every AI-generated response is correct.

Replace application security reviews or integration testing.

Automatically determine whether an app is public, private, or intended for a single merchant.

Provide the coding agent with relevant application details whenever they affect the implementation.

## Troubleshooting #

### The agent does not detect the skill #

Confirm that:

1 .

The skill is stored in a directory supported by the agent.

2 .

The folder contains `SKILL.md`.

3 .

The original directory structure has not been flattened or renamed incorrectly.

4 .

The agent was restarted or reloaded after installation.

5 .

Custom skills are enabled in the current workspace.

You can also explicitly tell the agent:

```
`Use the Zid API integration skill for this task.`
```

### Merchant API requests return `401 Unauthorized` #

Check that:

Both `Authorization` and `X-Manager-Token` are included when required.

The correct value is assigned to each header.

The tokens belong to the same merchant installation.

The tokens have not expired.

The merchant has not uninstalled the application.

The request uses HTTPS.

The app has the required scopes.

### The generated endpoint does not exist #

Ask the agent to locate the endpoint in the live Zid documentation before continuing.

Do not rely on an endpoint generated only from the model’s general knowledge. Confirm the method, URL, parameters, request body, and required scopes against the current endpoint page.

### The documentation and skill disagree #

Follow the live Zid documentation.

Then open an issue or pull request in the Zid Agent Skill GitHub repository and include the documentation page that supports the correction.

## Frequently asked questions #

### What is the Zid AI Agent Skill? #

The Zid AI Agent Skill is an open-source set of instructions and references that helps compatible AI coding agents build Zid integrations using Zid-specific OAuth, multi-tenant, API, and error-handling guidance.

### Is the Zid AI Agent Skill open source? #

Yes. The skill is available publicly through the Zid GitHub organization and is licensed under the MIT License.

### Does the skill make API calls? #

No. The skill guides the AI coding agent while it generates, reviews, or troubleshoots integration code. It is not an API client and does not make requests independently.

### Does the skill store merchant tokens? #

No. It provides architectural guidance for how your application should store and isolate merchant credentials. Your application remains responsible for implementing secure storage.

### Does the skill prevent all hallucinated endpoints? #

No AI skill can guarantee that every generated response will be correct. The Zid Agent Skill reduces the risk by instructing the agent to locate and verify endpoints in the official Zid documentation before implementation.

### Which Zid APIs does the skill support? #

The skill primarily focuses on Merchant API integrations. It also includes a documentation map covering Storefront APIs, Webhooks, Payments, and other Zid integration areas.

### Can I use it with Python, PHP, or Node.js? #

Yes. The skill is programming-language independent. A compatible coding agent can apply its patterns to Python, PHP, Node.js, or another stack.

### How is the skill updated? #

The skill is maintained in its public GitHub repository. Developers can open an issue or pull request when content is outdated, incomplete, or inconsistent with the live Zid documentation.

## Source and contributions #

The Zid AI Agent Skill is open source and maintained alongside the Zid developer documentation.

Use the **Zid Agent Skill GitHub repository** to:

Download or clone the skill.

Review its source files.

Report outdated guidance.

Suggest additional integration patterns.

Submit improvements through pull requests.

Contributions should be supported by an existing Zid documentation page rather than assumed API behavior.

Modified at 2026-07-21 11:53:58

Previous

Our custom MCP server

Next

Build an app
