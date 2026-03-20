---
source_id: "328"
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

# 328: My Multi-Agent Team (NOT OpenClaw)

> **Creator**: Owain Lewis | **Platform**: YouTube | **Date**: 2026-03-19 | **Duration**: 16:18

## Summary

Owain Lewis demonstrates a minimal, polling-based multi-agent architecture that allows developers to delegate coding tasks to autonomous AI workers via a task management system (Linear in the demo). Workers watch a ticket queue, claim tasks, delegate implementation to Claude Code or Codex, and then open pull requests for human review—all without requiring the developer to be in the loop during execution. The system scales from a single worker on a laptop to many workers running in parallel across different machines.

The core architectural argument is that this polling-based approach is meaningfully more secure and simpler than push-based alternatives like OpenClaw, which expose HTTP endpoints publicly. By only making outbound requests, the system eliminates inbound attack surface entirely. The tradeoff is slightly higher latency in picking up tasks (up to 60 seconds), which is irrelevant for typical development workflows where ticket turnaround is measured in minutes or hours.

The workflow is built around deterministic "hooks" wrapping a nondeterministic agent core. Pre-hooks handle setup (git checkout, pull), the agent does the creative coding work, and post-hooks enforce quality (running tests, linting, opening a PR via GitHub CLI, code review via CodeRabbit). This guardrail pattern compensates for agent unpredictability with reliable, auditable steps before and after each agent invocation.

---

## Key Concepts

### Poll-Based vs. Push-Based Agent Architecture

Push-based systems (like OpenClaw) expose public HTTP/webhook endpoints that external services ping when work is available. This increases attack surface since any internet actor can potentially reach those endpoints. A poll-based system instead has the worker make outbound requests to check for new tasks on a cadence (e.g., every 60 seconds). No ports are exposed, infrastructure is simpler, and the system is inherently more secure for local or VPS deployments. The latency tradeoff is negligible for development tasks.

### Task Manager as Delegation Interface

Rather than chatting with agents interactively, work is delegated through a structured task management system (Linear, Jira, Todoist, etc.). Tickets move through lifecycle states: unassigned → in progress → review → done (or failed). This provides visibility into what agents are doing at any point, enables parallel work across many agents without confusion, and mirrors how human teams coordinate—via tracked work items rather than ad-hoc conversation. The system is task-manager-agnostic; the concept transfers to any PM tool.

### Deterministic Hooks Around a Nondeterministic Core

The agent worker wraps Claude Code (or Codex) with pre- and post-execution hooks that run deterministic code. Pre-hooks might check out a branch or run `git pull`. Post-hooks might execute the test suite, run linters, push to a remote, and open a pull request. These guardrails make the overall pipeline reliable even though the agent's internal behavior is probabilistic. Failed tests in post-hooks cause the ticket to be marked as failed rather than silently passing bad code to review.

### Git Worktrees for Parallel Agent Isolation

Each worker creates a separate git worktree when claiming a ticket, allowing multiple agents to work on different tasks in the same repository simultaneously without interfering with each other's file changes. This is the mechanism that enables true parallelism at the filesystem level.

### CLAUDE.md Workflow Specification

Inside the agent worker, a `CLAUDE.md` file encodes a specific, constrained workflow for the agent to follow. Because iterative back-and-forth is not possible in a background worker context, the instructions must be self-contained and complete enough for the agent to execute without human clarification. This makes prompt/workflow design in `CLAUDE.md` critical to the reliability of the entire system.

---

## Practical Takeaways

- **Use a task manager, not a chat interface, to delegate agent work at scale.** Tickets provide state tracking, parallelism without confusion, and a natural review checkpoint (PR + ticket comment with Claude's output summary).
- **Prefer poll-based architectures for local or VPS agent deployments.** Avoid exposing public webhook endpoints unless you have a specific reason; polling is simpler, more secure, and sufficient for dev workflows where sub-minute latency doesn't matter.
- **Wrap every agent invocation with deterministic pre- and post-hooks.** Tests, linting, and PR creation should happen automatically after the agent finishes—don't rely on the agent to do these reliably on its own.
- **Scope background agent tasks carefully.** This pattern works best for well-defined, smaller tasks (bug fixes, documentation, isolated features). Iterative, exploratory work still benefits from direct human-in-the-loop coding sessions.
- **The architecture scales horizontally with minimal overhead.** Running N workers is just launching N processes; they all poll the same queue and claim tickets independently. You can distribute these across your laptop, a VPS, or multiple servers without any coordination infrastructure.

---

## Notable Quotes

> "We're kind of working as managers here. We're just delegating work to agents who are going to do the work for us."

> "These are deterministic guardrails around nondeterministic agents."

> "If you have many, many things going on at once, you don't want to be chatting with agents. You want a way to actually track what they're doing."

---
