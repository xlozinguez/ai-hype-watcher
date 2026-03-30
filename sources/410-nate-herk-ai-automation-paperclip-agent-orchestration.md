---
source_id: "410"
title: "Claude Code + Paperclip Just Destroyed OpenClaw"
creator: "Nate Herk | AI Automation"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=HJ-dwefABss"
date: "2026-03-28"
duration: "20:33"
type: "video"
tags: ["claude-code", "multi-agent", "agent-teams", "task-system", "agentic-coding"]
curriculum_modules: ["04-agentic-patterns", "05-team-orchestration"]
---

# 410: Claude Code + Paperclip Just Destroyed OpenClaw

> **Creator**: Nate Herk | AI Automation | **Platform**: YouTube | **Date**: 2026-03-28 | **Duration**: 20:33

# Claude Code + Paperclip: Multi-Agent Company Orchestration

## Summary

Nate Herk demonstrates Paperclip, an open-source orchestration tool that enables running autonomous AI agent teams as simulated companies or departments. The tool gained 36,000+ GitHub stars within weeks of its early-March 2026 launch by solving a real pain point: when running many parallel Claude Code sessions, visibility and coordination collapse. Paperclip addresses this by providing a unified dashboard where each agent has persistent instructions, scheduled heartbeats, a budget cap, and a ticketing/inbox system for human-in-the-loop approvals.

The core workflow combines Claude Code as the AI execution engine with Paperclip as the orchestration layer. Users define a company with a mission, spin up role-based agents (CEO, marketer, designer, researcher, etc.), assign initial tasks, and then step back into a "board member" role—setting high-level goals rather than micromanaging execution. Agents wake on a schedule (every 4–12 hours), review their context, check existing tasks, and continue working, routing anything needing human judgment to an inbox for approval.

Herk also demonstrates a meta-pattern: creating a dedicated Claude Code project that has ingested the entire Paperclip GitHub repo and community usage patterns, effectively building a personal "Paperclip expert" assistant to help configure, debug, and expand the system. This illustrates a broader principle—using one Claude Code instance to help operate and configure another AI system—that compounds the value of both tools.

## Key Concepts

### Agent Heartbeat Protocol
Agents are not persistent processes; they wake up on a schedule (configurable: every 4, 8, or 12 hours), initialize with fresh context, and orient themselves via their instruction files before resuming work. This means memory discipline is critical—agents must check their task queue, prior outputs, and goals on each wake cycle. The heartbeat pattern was cited as a key reason OpenClaw gained traction, as it makes agents feel proactive rather than purely reactive.

### Structured Agent Identity Files
Each agent in Paperclip carries four configuration files that persist across heartbeat cycles: **agents** (team structure and directory), **heartbeat** (execution checklist run on every wake), **soul** (persona, values, voice/tone), and **tools** (available capabilities). This separation of concerns allows fine-grained control—you can edit the soul to change communication style without touching execution logic, or update the tools file as new capabilities become available.

### Human-in-the-Loop via Inbox/Ticketing
Paperclip implements a lightweight approval workflow: agents route decisions requiring human judgment to an inbox, and a ticketing system logs every conversation and action. This creates an audit trail and enables the "board member" operating model—the human sets direction, checks in periodically (~30 minutes of oversight described), approves or comments on flagged items, and issues new high-level goals rather than writing individual prompts.

### Multi-Company / Multi-Department Architecture
A single Paperclip instance can host multiple distinct "companies," each with its own agent roster, goals, and budget. This maps naturally to real business use cases: separate companies for separate product lines, or separate departments within a single business (e.g., automating a content team while leaving other functions human-run). Agents within a company can hire other agents, enabling organic org-chart growth from a single initial seed.

### Meta-Agent Configuration Pattern
Herk sets up a Claude Code project whose context includes the full Paperclip GitHub repo, observed usage patterns from X/Twitter, and his own system's agent definitions and secrets. This project acts as a knowledgeable co-pilot for configuring, monitoring, and expanding Paperclip itself—not for executing business tasks, but for helping the human operator work more effectively with the orchestration layer. This is a transferable pattern: use Claude Code to build expertise about any open-source tool you're deploying.

## Practical Takeaways

- **Start with one agent and a real task**: Paperclip's onboarding defaults to a CEO agent with a "hire your first engineer" task, which is a useful scaffold—but replace the initial task with something relevant to your actual goal before launching.
- **Set per-agent budgets immediately**: The spend-analytics feature (meaningful when using API/pay-per-token access rather than a subscription) allows cost control at the individual agent level; configure this before agents run unattended.
- **Use the heartbeat files as persistent memory**: Because agents reinitialize on each wake cycle, the heartbeat checklist file is the primary mechanism for maintaining continuity—treat it as executable documentation of what the agent should verify and resume each session.
- **Build a "tool expert" Claude Code project for any new open-source platform you adopt**: Feeding a tool's GitHub repo into a dedicated Claude Code project creates a reusable expert assistant for configuration and debugging—this pattern generalizes well beyond Paperclip.
- **Adopt a "board member" mental model**: The intended operating posture is high-level goal-setting and inbox triage (~30 min/day), not prompt-by-prompt management. Designing your agent instructions around this assumption (autonomous defaults, flag edge cases) is key to making the system actually save time.

## Notable Quotes

> "I'm coming in here acting as a board, which means I'm giving them high-level goals, metrics, things that I want to achieve, but I'm not actually sitting in the business being an operator."

> "Every day he would have 20 different terminals running, 20 different Claude Code sessions running... and then when you come back, you're like, 'I forgot which one's doing what and I forgot what I asked.'"

> "If you can set up a project where you give it the GitHub repo—it's open source, so it can know everything about it—you let it look at X to see how people are using it, you let it do its own research and find its own things, and it's going to help you use tools so, so much better."
