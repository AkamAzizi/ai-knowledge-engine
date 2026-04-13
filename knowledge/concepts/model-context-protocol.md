---
title: "Model Context Protocol (MCP)"
type: concept
tags: [mcp, ai-agents, protocol, tool-use, anthropic, llm-engineering]
created: 2026-04-13
updated: 2026-04-13
sources: [writing-effective-tools-for-ai-agents]
---

# Model Context Protocol (MCP)

## Definition

An open protocol developed by [[entities/anthropic|Anthropic]] that standardizes how LLM agents connect to and use external tools and services. MCP defines how tools are exposed to agents, how agents invoke them, and how results are returned — providing a consistent interface across any tool and any MCP-compatible agent.

## How It Works

### Core Architecture
- **MCP server** — exposes tools (functions) that an agent can call. Can be local (running on your machine) or remote.
- **MCP client** — the agent or agent runtime that connects to MCP servers and calls their tools.
- Tools are defined with names, descriptions, and input schemas — loaded into the agent's context.

### Connecting Tools to Agents

**Claude Code:**
```
claude mcp add <name> <command> [args...]
```

**Claude Desktop app:**
- MCP servers: `Settings > Developer`
- Desktop Extensions (DXT): `Settings > Extensions`

**Programmatic testing:**
- Tools can also be passed directly into Anthropic API calls without an MCP server.

### Key Features
- **Tool annotations** — metadata that discloses whether a tool requires open-world access or makes destructive/irreversible changes. Helps agents and users understand tool risk.
- **Namespacing** — MCP clients sometimes namespace tools automatically (e.g. prefixing by server name). Tool designers should design names that work well with this.
- **Scale** — agents can potentially have access to hundreds of tools across many MCP servers simultaneously — making [[concepts/agent-tool-design|good tool design]] (naming, selection, descriptions) critical.

### Local MCP Server Development
Wrap tools in a local MCP server to test interactively in Claude Code or Claude Desktop before deploying. Use the MCP SDK; provide the SDK documentation (via llms.txt or direct paste) to Claude Code when generating server code.

## Key Sources

- [[sources/writing-effective-tools-for-ai-agents|Writing Effective Tools for AI Agents — Using AI Agents]] — describes MCP as the deployment target for agent tools; covers server setup and tool annotations

## Related Concepts

- [[concepts/agent-tool-design|Agent Tool Design]] — MCP is the protocol through which well-designed tools are exposed to agents
- [[concepts/tool-evaluation|Tool Evaluation]] — evals test tools deployed via MCP servers

## Open Questions

- How does the MCP protocol handle tool versioning and backwards compatibility?
- What are the security implications of granting an agent access to many MCP servers simultaneously?
- How does MCP compare to OpenAI's function calling or tool use specifications?
