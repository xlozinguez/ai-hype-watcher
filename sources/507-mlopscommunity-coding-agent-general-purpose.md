---
source_id: "507"
title: "How to Make a Coding Agent a General Purpose Agent - Harrison Chase"
creator: "MLOps.community"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=OYK1-vCbSMU"
date: "2026-03-31"
duration: "36:54"
type: "video"
tags: ["agentic-coding", "multi-agent", "context-engineering", "enterprise-ai", "mcp", "security", "claude-code"]
curriculum_modules: ["04-agentic-patterns", "05-team-orchestration", "06-strategy-and-economics"]
---

# 507: How to Make a Coding Agent a General Purpose Agent - Harrison Chase

> **Creator**: MLOps.community | **Platform**: YouTube | **Date**: 2026-03-31 | **Duration**: 36:54

# How to Make a Coding Agent a General Purpose Agent

## Summary

Harrison Chase (LangChain CEO) and Sam Parr T (Arcade.dev CTO) argue that coding agents are the foundational paradigm for building general-purpose agents. The core insight is that coding agents already solve the hardest problems in agentic systems: persistent workspace management via file systems, context window discipline, planning, and sub-agent orchestration. These patterns generalize far beyond writing code—they represent a blueprint for any agent that needs to act reliably on behalf of users.

The talk is structured around two complementary components: the **agent harness** (Harrison's focus) and the **tool runtime** (Sam's focus). The harness provides the scaffolding around the model—file system tools, planning, sub-agents, context compaction, and human-in-the-loop controls. The tool runtime handles everything outside the local environment: multi-user authentication, OAuth delegation, and third-party service integrations. Together, these two layers constitute what the speakers call a general-purpose agent capable of serving an entire organization, not just a single user on a laptop.

The presentation grounds these concepts in LangChain's own tooling: LangGraph (agent runtime with durable execution and persistence) and Deep Agents (their agent harness built on LangGraph, modeled heavily on Claude Code). The tool runtime layer is represented by Arcade.dev, which handles the "dirty work" of delegated authorization across enterprise systems—solving the hard problem of giving agents scoped, user-specific access to services like Google Calendar, Slack, and payment systems without resorting to dangerously over-privileged service tokens.

## Key Concepts

### Agent Harness vs. Agent Runtime
An **agent harness** is distinguished from a bare LLM-in-a-loop by its "batteries included" design. Where a runtime (like LangGraph) provides infrastructural primitives—durable execution, streaming, persistence, human-in-the-loop—the harness layers on opinionated, ready-to-use components: file system tools, a planning tool, sub-agent support, skills, and context management strategies. Deep Agents is LangChain's harness built on LangGraph, modeled closely on Claude Code's architecture. The distinction matters because harnesses encode best practices that would otherwise require significant custom engineering.

### Pluggable File System Backends
One of Deep Agents' notable innovations is treating the file system as an abstraction rather than a concrete local path. The agent always interacts with the same file system interface (list, read, write, edit, glob, grep), but the backend can be the real local file system, a database-backed virtual file system, or a remote sandbox. This makes it straightforward to run agents remotely or multi-tenant without changing the agent's behavior, since the file system is how agents naturally persist state, plans, and intermediate work.

### Sub-Agents and Context Isolation
Sub-agents are a core primitive in the coding agent paradigm. The key property is **context isolation**: a sub-agent receives only its specific task and returns only its result—it sees nothing of the parent agent's history, and the parent sees none of the sub-agent's intermediate work. This enables safe parallelism and focused execution. The failure modes are communication-related: the parent must give precise task descriptions, and the sub-agent must return the right information. When this breaks down, the orchestration fails silently.

### Context Engineering Built Into the Harness
Deep Agents embeds several context management strategies at the harness level: large tool results are offloaded to files (with only the first 100 lines shown inline), compaction triggers automatically at a configurable context threshold (saving full message history to disk for optional retrieval), and the planning tool injects plans into the context window without persisting them—keeping the LLM oriented without permanently occupying tokens. The philosophical direction is giving the LLM more agency over managing its own context.

### Delegated Agent Authorization
The tool runtime's central challenge is that agents are now **intermediaries** in authentication flows, which breaks traditional patterns. A service token either has too many privileges (CISO blocker) or too few (useless for real tasks). The solution is **delegated agent authorization**: the agent receives a scoped token representing a subset of the user's permissions for a specific set of services, for a specific session. This allows enterprise SSO to flow through to the agent, which can then call Google Calendar, Slack, payment systems, etc., as that specific user—enabling personalized, authorized actions at scale across an entire organization.

## Practical Takeaways

- **Model your agent's persistent state as a file system**, even if the underlying storage is a database. Agents already know how to navigate file systems, and this abstraction makes remote/multi-tenant deployment much simpler.
- **Sub-agents are your primary parallelism and focus primitive**—design them with explicit, complete task descriptions and require structured, complete responses. Communication failures between parent and sub-agent are the main failure mode, not capability failures.
- **Don't ship service tokens to production multi-user agents.** The either/or of over-privileged vs. under-privileged service tokens is a dead end. Plan for delegated authorization (OAuth scoping per user, per agent, per session) from the start if enterprise deployment is a goal.
- **Treat context management as infrastructure, not an afterthought.** Offloading large tool results, triggering compaction, and logging full history to disk for optional retrieval should be harness-level defaults, not per-agent custom logic.
- **The coding agent paradigm generalizes.** Skills, agent.md definitions, sub-agents, and file-system-as-workspace are patterns that apply to any domain. If you're building a general-purpose agent, start by adopting the coding agent harness architecture and extend from there.

## Notable Quotes

> "What we have in Deep Agents is that file system—it can be your real file system or it can be a virtual file system. So we can use a database to store quote-unquote files. So you store it in database, but you represent it as a file system to the agent because that's what it knows and that's what it interacts with."

> "A service token is either got incredibly elevated privileges to the point where no CISO is going to let your product be bought at enterprise. Or it's got so low privileges your agent's not useful."

> "A lot of this is in spirit of giving the LLM more control over managing its own context window."
