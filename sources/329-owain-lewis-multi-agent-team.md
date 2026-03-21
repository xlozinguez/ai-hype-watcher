---
source_id: "329"
title: "My Multi-Agent Team (NOT OpenClaw)"
creator: "Owain Lewis"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=Zhbx-dj0qHE"
date: "2026-03-19"
duration: "16:18"
type: "video"
tags: ["agent-teams", "multi-agent", "agentic-coding", "task-system", "claude-code"]
curriculum_modules: ["04-agentic-patterns", "05-team-orchestration"]
---

# 329: My Multi-Agent Team (NOT OpenClaw)

> **Creator**: Owain Lewis | **Platform**: YouTube | **Date**: 2026-03-19 | **Duration**: 16:18

## Summary

Owain Lewis demonstrates a polling-based multi-agent worker architecture as an alternative to OpenClaw for delegating coding tasks to AI agents without staying in the loop. The system uses a task management tool (Linear, though any task manager works) as the coordination layer, with background worker agents that poll for new tickets, delegate implementation to Claude Code, run automated checks, and open pull requests for human review.

The core architectural insight is the contrast between push-based systems (like OpenClaw, which expose HTTP endpoints and webhooks) and pull-based polling architectures that make only outbound requests and expose no attack surface. Lewis argues this approach is simpler, more secure, and scales from a single laptop worker to hundreds of agents running on remote servers.

The video also introduces deterministic hooks (pre-hooks and post-hooks) as guardrails wrapping the nondeterministic agent execution, ensuring consistent quality even when humans are fully out of the loop.

## Key Concepts

### Pull-Based vs. Push-Based Agent Architecture

OpenClaw and similar tools use a push-based architecture with HTTP endpoints and webhooks, requiring exposed ports on the host machine. Lewis proposes a pull-based alternative where agents poll a task queue at regular intervals (e.g., every 60 seconds). This eliminates exposed attack surfaces since only outbound requests are made. The latency trade-off (up to 60 seconds to pick up a ticket) is irrelevant for coding tasks that take minutes to complete.

### Deterministic Hooks Around Nondeterministic Agents

The system wraps the nondeterministic agent execution with deterministic pre-hooks and post-hooks. Pre-hooks handle tasks like checking out a git branch and pulling latest changes. Post-hooks run tests, push commits, and open pull requests using the GitHub CLI. This pattern ensures consistent behavior regardless of agent output quality and provides guardrails for fully delegated work.

### Full Delegation vs. Iterative Collaboration

Lewis distinguishes between two modes of working with coding agents: iterative collaboration (sitting in the terminal, going back and forth) which is best for complex, exploratory tasks; and full delegation (assigning tickets and reviewing PRs) which is best for smaller, well-defined tasks like bug fixes and documentation updates. The CLAUDE.md inside the agent worker instructs the agent to write code, run tests, perform a code review with CodeRabbit, fix any issues found, and re-run tests, simulating an iterative process in a single shot.

### Task Manager as Agent Coordination Layer

Using existing task management tools (Linear, Jira, Monday.com) as the coordination layer for agent teams means you get built-in tracking, lifecycle management, and visibility without building custom infrastructure. Agents claim tickets, move them through status columns (in progress, review, done/failed), and comment results back on the ticket.

## Practical Takeaways

- **Start simple, scale later**: Begin with one worker on your laptop polling a task queue; scale to multiple workers on VPS instances as confidence grows
- **Use deterministic hooks for quality**: Wrap nondeterministic agent execution with pre-hooks (branch checkout, git pull) and post-hooks (tests, linting, PR creation) to maintain code quality
- **Agent-harness agnostic**: The pattern works with Claude Code, Codex, or any coding agent, making the architecture more important than the specific tool
- **CodeRabbit as automated reviewer**: When humans are out of the loop, automated code review tools provide the validation layer that interactive sessions would normally include
- **Git worktrees for parallel work**: Each agent worker creates a new git worktree to avoid conflicts when multiple agents work on the same repo simultaneously

## Notable Quotes

> "We're no longer in the loop where we're sitting in the terminal waiting for changes. We're just delegating to our system." — Owain Lewis

> "These are deterministic guardrails around nondeterministic agents." — Owain Lewis

> "What's interesting here is the architecture, not necessarily the code." — Owain Lewis

## Related Sources

- [280: Leon van Zyl - Claude Code Loop](280-leon-van-zyl-claude-code-loop.md) — Agent loop patterns
- [269: Peter Yang - Six Agents App Design](269-peter-yang-six-agents-app-design.md) — Multi-agent design patterns

## Related Curriculum

- [Module 04: Agentic Patterns](../curriculum/04-agentic-patterns/README.md) — Polling-based agent loops, hooks as guardrails, builder-validator in single-shot mode
- [Module 05: Team Orchestration](../curriculum/05-team-orchestration/README.md) — Multi-worker coordination via task management systems
