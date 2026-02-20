---
source_id: "078"
title: "N8N is Failing Us…"
creator: "Simon Scrapes"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=5U3D6o6Gi_g"
date: "2026-02-15"
duration: "11:25"
type: "video"
tags: ["agentic-coding", "claude-code", "mcp", "enterprise-ai"]
curriculum_modules: ["03-claude-code-essentials", "06-strategy-and-economics"]
---

# 078: N8N is Failing Us…

> **Creator**: Simon Scrapes | **Platform**: YouTube | **Date**: 2026-02-15 | **Duration**: 11:25

## Summary

Simon Scrapes — who has taught n8n for over two years — provides an honest comparison of n8n and Claude Code, arguing they are complementary tools rather than competitors. The video identifies three gaps where Claude Code has surpassed n8n (speed of building, product capability, scalability) while defending n8n's irreplaceable strength in visual observability and debugging for non-technical teams.

The core thesis is that the "is n8n dead?" framing is wrong. N8n excels at internal business automation with visual debugging, while Claude Code is built for customer-facing products, multi-tenant systems, and scalable codebases. The real competitive advantage goes to builders who combine both into a unified system.

## Key Concepts

### Speed Parity: Prompting vs. Drag-and-Drop

Claude Code with MCP connections and skills now matches or exceeds n8n's drag-and-drop speed for building workflows. Simon demonstrates building in 10 minutes with Claude Code what took an hour in n8n — eliminating the original speed advantage that made no-code platforms attractive. The manual process of searching nodes, configuring credentials, and mapping fields one by one in n8n is replaced by describing what you want in natural language.

### Product Capability Gap

N8n was never designed for building customer-facing products. Its sustainable use license explicitly restricts usage to internal business purposes — no white-labeling, multi-tenant SaaS, or client-hosted products. Claude Code fills this gap by enabling full-stack development: multi-tenant backends, authenticated client portals, Stripe billing integration, and branded front-ends. This transforms the value proposition from selling $2K n8n workflows to $10K+ complete products.

### N8n's Irreplaceable Advantage: Visual Observability

N8n's execution history log provides visual debugging that Claude Code cannot match. Non-technical team members can click through any workflow run, inspect data inputs/outputs at each node, and diagnose issues without understanding code or logs. This makes n8n the right home for core business logic that needs to be inspected, tested, and debugged by the people who depend on it.

### The Combined System Architecture

The optimal setup uses Claude Code for infrastructure (backends, front-ends, databases, authentication, hosting) and n8n for core business automations (lead enrichment, data processing, client workflows). Claude Code builds the product packaging; n8n handles the value-driving automations that need visual transparency and team accessibility.

## Practical Takeaways

- **Stop comparing n8n and Claude Code as competitors**: They serve fundamentally different purposes — internal automation vs. product development
- **Use n8n for business logic that your team needs to see and debug**: Visual observability matters more than speed when non-technical stakeholders need to diagnose issues
- **Use Claude Code for anything customer-facing or multi-tenant**: N8n's license and architecture aren't designed for products you sell
- **Combine n8n + Claude Code via MCP**: The n8n MCP server and n8n skills let Claude Code build and edit n8n workflows, bridging both tools
- **N8n needs version propagation**: The biggest scaling pain point is updating shared logic across multiple workflow instances — something trivial in code but manual in n8n

## Notable Quotes

> "N8N and Claude Code aren't actually competitors. They do completely different jobs. And once you see them as one system, not two, what you can build actually changes dramatically." — Simon Scrapes ([00:29](https://www.youtube.com/watch?v=5U3D6o6Gi_g&t=29))

> "Don't get me wrong, Claude Code is incredible for building, but try handing a client the terminal or the code that you've created to a non-technical team and saying here check the logs. Good luck with that." — Simon Scrapes ([09:31](https://www.youtube.com/watch?v=5U3D6o6Gi_g&t=571))

> "The builders who figure out how to combine Claude Code and n8n into one system, they are going to leave everyone else behind because they'll no longer be selling automations anymore. They'll be selling complete products and systems." — Simon Scrapes ([11:01](https://www.youtube.com/watch?v=5U3D6o6Gi_g&t=661))

## Related Sources

- [020: How & When to Use Claude Code Agent Teams](020-simon-scrapes-agent-teams.md) — Same creator's earlier work on Claude Code agent teams
- [051: You're Using Claude Code Wrong](051-simon-scrapes-claude-code-tips.md) — Simon's Claude Code tips and workflow patterns
- [062: Every Level of Claude Code Explained](062-simon-scrapes-claude-code-levels.md) — Comprehensive Claude Code breakdown by same creator
- [046: The Rise of WebMCP](046-sam-witteveen-webmcp.md) — MCP as the bridge between AI tools and external services
- [066: How to Use Claude Cowork](066-brooke-wright-cowork-tutorial.md) — Non-developer perspective on Claude Code for business

## Related Curriculum

- [Module 03: Claude Code Essentials](../curriculum/03-claude-code-essentials/README.md) — Claude Code + MCP integration patterns
- [Module 06: Strategy and Economics](../curriculum/06-strategy-and-economics/README.md) — Business model implications of AI-native development vs. no-code platforms
