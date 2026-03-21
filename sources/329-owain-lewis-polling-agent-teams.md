---
source_id: "329"
title: "My Multi-Agent Team (NOT OpenClaw)"
creator: "Owain Lewis"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=Zhbx-dj0qHE"
date: "2026-03-19"
duration: "16:18"
type: "video"
tags: ["agent-teams", "multi-agent", "agentic-coding", "claude-code", "security", "ai-sdlc"]
curriculum_modules: ["04-agentic-patterns", "05-team-orchestration", "06-strategy-and-economics"]
---

# 329: My Multi-Agent Team (NOT OpenClaw)

> **Creator**: Owain Lewis | **Platform**: YouTube | **Date**: 2026-03-19 | **Duration**: 16:18

## Summary

Owain Lewis demonstrates a minimal, polling-based multi-agent architecture that lets developers delegate coding tasks to autonomous AI workers via a task management system (demonstrated with Linear). Workers continuously poll for new tickets, claim them, execute changes via Claude Code or Codex, and open pull requests for human review — all without requiring the developer to be in the coding loop. The system handles full ticket lifecycle management: moving issues through states (queued → in-progress → review/done/failed) and posting agent output summaries as ticket comments.

The core architectural insight is the contrast between **pull-based** (this system) and **push-based** (OpenClaw-style) architectures. Push-based systems expose HTTP webhook endpoints publicly, increasing attack surface. This pull-based approach makes only outbound requests, requires no exposed ports, and is dramatically simpler while still scaling from one worker on a laptop to hundreds of workers across machines. The tradeoff — slightly higher latency to pick up tasks — is irrelevant for async coding work.

The system uses **deterministic hooks** to wrap the non-deterministic agent execution: pre-hooks handle setup (git checkout, branch creation, git pull) and post-hooks handle validation and delivery (running tests, linting, opening PRs via GitHub CLI). This pattern provides guardrails around agent behavior without requiring complex orchestration infrastructure, and the whole architecture is both task-manager-agnostic and agent-harness-agnostic.

---

## Key Concepts

### Pull-Based vs. Push-Based Agent Architecture
Push-based systems (like OpenClaw) receive work via publicly-exposed HTTP webhook endpoints, creating an attack surface and infrastructure complexity. Pull-based systems poll the task queue on a schedule (e.g., every 60 seconds), making only outbound requests. No ports are exposed, the infrastructure is simpler, and the security posture is significantly better for local and VPS-hosted deployments. The latency tradeoff is negligible for background coding work.

### Task Manager as Delegation Interface
Using a project management tool (Linear, Jira, Monday.com, etc.) as the agent's work queue decouples delegation from execution. Developers act as managers — creating tickets with specifications from any device — while agents handle implementation. This provides visibility into parallel work at scale without the chaos of chat-based delegation, and mirrors how human engineering teams already coordinate work.

### Deterministic Pre/Post Hooks as Agent Guardrails
Non-deterministic agent execution is sandwiched between deterministic steps. Pre-hooks perform predictable setup (branch creation, git pull, workspace preparation). Post-hooks enforce quality gates (test runs, linting, `git push`, PR creation). This pattern adds reliability without complex orchestration: the agent does the creative/reasoning work, but its output is always validated and delivered by predictable code.

### Git Worktrees for Parallel Agent Isolation
Each worker agent creates a new git worktree for its assigned ticket, isolating concurrent work across multiple agents operating on the same repository. This prevents agents from interfering with each other's changes when multiple workers process tickets simultaneously.

### Horizontal Scaling via Independent Workers
The architecture scales by simply running more worker processes — locally or on remote VPS instances. Workers are stateless with respect to each other; coordination happens through the task manager's ticket-claiming mechanism (a worker marks a ticket "in progress" to claim it, preventing double-pickup). This scales from one worker to potentially hundreds with no architectural changes.

---

## Practical Takeaways

- **Start with a simple polling worker before adopting complex agent platforms.** A script that polls Linear/Jira every 60 seconds and delegates to Claude Code is more secure, easier to debug, and easier to customize than webhook-based frameworks like OpenClaw.
- **Use ticket descriptions as your agent's CLAUDE.md-level instructions.** The demo shows tickets with "quite a lot of instruction" — treating ticket bodies as rich specifications is the primary mechanism for guiding agent behavior without real-time interaction.
- **Wrap agent calls in pre/post hooks from day one.** Even simple hooks (run tests after completion, open a PR) dramatically improve reliability and create the review checkpoints needed when you're out of the coding loop.
- **Reserve synchronous/interactive agent use for iterative, exploratory work.** The polling-agent model is best suited for well-defined, smaller tasks (bug fixes, docs updates, adding variables). When requirements are ambiguous or highly iterative, staying in the terminal loop remains preferable.
- **Use automated code review tools (e.g., CodeRabbit) as an additional quality gate on PRs.** When human review latency is high due to async delegation, bot-based code review provides a near-real-time quality check before merges.

---

## Notable Quotes

> "We're kind of working as managers here. We're just delegating work to agents who are going to do the work for us."

> "These are deterministic guardrails around non-deterministic agents."

> "This is a really, really simple bit of software. It's not doing very much. It's really easy to adapt. It's really easy to understand. We're not adding layers and layers of complexity. This is really, really simple, but it scales really well."

---
