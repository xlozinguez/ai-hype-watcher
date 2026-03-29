---
source_id: "410"
title: "Claude Code + Paperclip Just Destroyed OpenClaw"
creator: "Nate Herk | AI Automation"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=HJ-dwefABss"
date: "2026-03-28"
duration: "20:33"
type: "video"
tags: ["claude-code", "agent-teams", "multi-agent", "task-system", "agentic-coding"]
curriculum_modules: ["04-agentic-patterns", "05-team-orchestration"]
---

# 410: Claude Code + Paperclip Just Destroyed OpenClaw

> **Creator**: Nate Herk | AI Automation | **Platform**: YouTube | **Date**: 2026-03-28 | **Duration**: 20:33

## Summary

Nate Herk demonstrates Paperclip, an open-source orchestration platform for running multi-agent AI companies without human employees. The tool launched in early March 2025, rapidly accumulating 36,000+ GitHub stars, and addresses a core pain point in agentic workflows: managing many simultaneous Claude Code sessions without losing context, visibility, or coordination. Paperclip provides a unified dashboard where users can spin up agent teams (CEO, marketer, designer, researcher, etc.), assign goals, monitor activity, and approve actions from a single "board member" interface rather than juggling dozens of terminals.

The video walks through a full setup flow — creating a new company, configuring an initial CEO agent, and watching it execute its first task (hiring plan). Key infrastructure features include native heartbeat scheduling (agents wake on a timer, re-orient from memory, and continue work autonomously), per-agent budget controls, a ticketing/inbox system for human-in-the-loop approval, and composable instruction files (soul, heartbeat, agents, tools) that define each agent's persona and operating procedures. The platform runs locally by default but can be deployed to a VPS for remote access.

Herk also describes a meta-practice: setting up a dedicated Claude Code project pre-loaded with Paperclip's GitHub repo, API docs, and usage patterns so that Claude itself acts as a configuration assistant. This layered approach — using Claude Code to help configure and expand a Paperclip deployment — illustrates a broader pattern of agents managing agents and AI tooling assisting AI tooling setup.

---

## Key Concepts

### Paperclip as Multi-Agent Orchestration Layer
Paperclip sits above individual Claude Code sessions and provides a shared coordination plane. Rather than running isolated terminals, each agent lives inside Paperclip with persistent context, a ticketing system, defined roles, and cross-agent visibility. The orchestrator tracks tasks in progress, recent activity, and pending approvals in a single dashboard — solving the observability gap that made managing many concurrent agentic sessions impractical.

### Heartbeat Protocol for Autonomous Continuity
Agents in Paperclip operate on scheduled "heartbeats" (every 4, 8, or 12 hours). On each heartbeat, an agent wakes with fresh context, reads its instruction files, reviews its task queue, and resumes work. This mirrors the pattern that made OpenClaw popular — proactive, always-on agents — but with the scaffolding to keep them oriented without human re-prompting. The heartbeat file functions as an execution checklist run on every wake cycle.

### Composable Agent Instruction Files
Each agent's behavior is defined by four modular files: **soul** (persona, values, tone), **heartbeat** (execution checklist for every wake cycle), **agents** (directory of other agents and how to collaborate), and **tools** (available capabilities). This separation of concerns allows fine-grained customization of agent identity and operating procedure independently of the underlying model, and enables the files to evolve as the deployment matures.

### Board Member vs. Operator Mental Model
Herk frames the human role as a "board member" rather than an operator: setting high-level goals and metrics, reviewing inbox items, approving key decisions, and occasionally injecting new issues — but not managing day-to-day execution. This is a practical framing for how to delegate effectively to an agent team without micromanaging individual tasks, and maps directly to how Paperclip's inbox and issue systems are designed.

### Claude Code as Configuration Assistant (Meta-Agent Pattern)
To ease Paperclip onboarding, Herk created a Claude Code project loaded with Paperclip's full repo, API documentation, and community usage patterns. This Claude instance acts as a persistent configuration partner — helping set up new agents, plan VPS migrations, add secrets, and debug gotchas. The pattern generalizes: use a well-context-loaded Claude Code session to help configure and manage the broader agent infrastructure, not just to write application code.

---

## Practical Takeaways

- **Start with one agent (CEO) and let it hire** — Paperclip's default onboarding task (CEO creates a hiring plan) bootstraps the org structure organically; resist the urge to manually define all agents upfront.
- **Use per-agent budget caps from day one** — Each agent's token spend is trackable; set limits immediately to prevent runaway costs before you understand each agent's consumption patterns.
- **Pre-load a Claude Code project with the Paperclip repo** — Treating Claude itself as your Paperclip config assistant dramatically accelerates setup and reduces gotchas, especially for heartbeat tuning and VPS migration.
- **Treat the inbox as your primary interface** — Rather than monitoring individual agent terminals, configure agents to surface decisions and approvals to the inbox; this keeps the human role lightweight and scalable across multiple companies/departments.
- **Deploy to a VPS early if you want always-on agents** — Local deployment ties heartbeats to your machine's uptime; a VPS unlocks true autonomous operation and remote dashboard access.

---

## Notable Quotes

> "I'm acting as a board — which means I'm giving them high-level goals, metrics, things that I want to achieve — but I'm not actually sitting in the business being an operator."

> "Every day he would have 20 different terminals running, 20 different Claude Code sessions running. And then when you come back, you're like, okay, I forgot which one's doing what."

> "If you can set up a project where you give it the GitHub repo, you let it look at X to see how people are using it, you let it do its own research — it's going to help you use tools so much better."

---
