---
source_id: "393"
title: "Agent Skills or MCP in the era of Claude Code?"
creator: "Confluent Developer"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=pvxNcQTcIy4"
date: "2026-03-10"
duration: "9:56"
type: "video"
tags: ["mcp", "skills", "claude-code", "agentic-coding", "multi-agent"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns", "06-strategy-and-economics"]
---

# 393: Agent Skills or MCP in the era of Claude Code?

> **Creator**: Confluent Developer | **Platform**: YouTube | **Date**: 2026-03-10 | **Duration**: 9:56

# Agent Skills vs. MCP in the Claude Code Era

## Summary

This video from Confluent Developer provides a concise comparison of Claude Skills and the Model Context Protocol (MCP), arguing that despite surface-level overlap, they serve fundamentally different use cases and neither replaces the other. The presenter first reviews recent MCP evolution—including the near-abandonment of the resources API in favor of tools, adoption of streamable HTTP, and OAuth 2.1 support—before introducing Skills as a complementary but distinct mechanism for extending agent capabilities.

Skills are described as markdown-based instruction files (plus optional scripts and static reference data) that live on the local filesystem where an agent can see them. They emerged primarily as plugins for Claude Desktop and Claude Code, making them inherently local and developer-laptop-oriented. MCP, by contrast, provides a standardized, network-accessible interface to real-time data and cloud-authenticated actions—making it essential for headlessly running agentic microservices that can't rely on local file trees or CLI tokens.

The key insight is that the apparent tension between Skills and MCP largely dissolves when you distinguish the *local coding agent* use case (where Skills + CLI scripts can substitute for many MCP patterns) from the *agentic microservice* use case (where MCP remains the right standard interface). The presenter notes a nascent Python API for executing Skills in custom agents as a development worth watching, but concludes that practitioners need fluency in both tools given the current landscape.

## Key Concepts

### MCP Recent Evolution (2025–2026)
The MCP ecosystem has matured across three dimensions since its initial release: (1) the **resources API** has been largely bypassed by the community, which found that tool calls handle resource queries adequately; (2) **streamable HTTP** replaced server-sent events as the transport layer, simplifying cloud deployment; and (3) **OAuth 2.1** was added to support user-facing authentication flows (e.g., GitHub popups) for locally running agents, with headless/microservice OAuth solutions still forthcoming.

### Skills as Filesystem-Native Agent Extensions
A Skill is a directory tree anchored by a `root-skill.md` markdown file containing specialized instructions, procedures, and conditions for a specific task domain. Supporting directories can hold static reference data and executable scripts (bash, Python, etc.). Because Skills are files distributed via repositories like GitHub and consumed from the local filesystem, they are inherently incompatible with cloud-hosted headless agents—they are a local-first primitive.

### MCP vs. Skills: Orientation Differences
The core distinction is **local vs. networked** and **static vs. live**. Skills excel at encoding curated static knowledge and invoking local scripts or CLIs with pre-authenticated sessions. MCP excels at providing a standardized, discoverable interface to real-time data sources (Kafka topics, ticket systems, customer records) and cloud resources requiring network authentication. Both can invoke scripts and represent resources, but their deployment context and data freshness assumptions differ substantially.

### CLI Scripts as MCP Substitutes (Local Case Only)
In the local coding agent scenario, a Skill's script invoking an authenticated CLI (e.g., a cloud provider CLI with a cached token) can replicate much of what an MCP server would do. This is why developers conflate the two: for laptop-based Claude Code workflows, Skills + CLIs cover a large portion of the MCP value proposition. This substitution breaks down entirely for agentic microservices running headlessly without a local filesystem or user-facing auth flow.

### Emerging Skills API for Custom Agents
At time of recording, Anthropic provides a Python library that allows developers to import and execute Skills within their own custom-built agents—not just within Claude Code or Claude Desktop. This represents a potential bridge between the two worlds, but adoption is nascent and the trajectory is uncertain.

## Practical Takeaways

- **Use MCP for agentic microservices**: Any headlessly deployed agent that needs standardized, discoverable access to real-time data or cloud resources should use MCP. Skills are not a substitute in this context.
- **Use Skills for local coding agent enhancement**: For Claude Code or Claude Desktop workflows, Skills are the right tool for encoding domain-specific procedures, static reference data, and local script execution—they're faster to author and distribute than MCP servers.
- **Don't wait on the MCP resources API**: The community has effectively deprecated it in practice. Model resource access as tool calls to stay aligned with real-world usage patterns.
- **Treat OAuth 2.1 MCP as local-agent-only for now**: The current OAuth 2.1 implementation works well for developer laptops but isn't production-ready for headless microservice deployments; plan for that gap in architecture decisions.
- **Watch the Skills Python API**: If Anthropic's library for executing Skills in custom agents matures, it could meaningfully shift how Skills are used beyond the Claude Code/Desktop context—worth tracking before committing to MCP-only architectures for custom agents.

## Notable Quotes

> "You definitely do need to know and use MCP. You definitely do need to know and use skills. This is without a doubt the most rapidly evolving landscape I have seen in more than 30 years of software engineering."

> "For changing states of affairs out there in the world, deploying a resource into the cloud, opening a GitHub issue—those are things more out there that require authentication to some network resource in the cloud, less local stuff on my machine."

> "When we take our attention over here, not to a coding agent that I got from a foundation lab, but an agentic microservice that I wrote that needs to access tools, that needs to access resources—suddenly, that script, that CLI, those skills, none of that stuff makes sense over here."
