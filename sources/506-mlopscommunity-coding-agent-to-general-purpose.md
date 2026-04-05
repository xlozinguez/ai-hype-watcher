---
source_id: "506"
title: "How to Make a Coding Agent a General Purpose Agent - Harrison Chase"
creator: "MLOps.community"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=OYK1-vCbSMU"
date: "2026-03-31"
duration: "36:54"
type: "video"
tags: ["agentic-coding", "multi-agent", "context-engineering", "enterprise-ai", "mcp", "agent-teams"]
curriculum_modules: ["04-agentic-patterns", "05-team-orchestration", "06-strategy-and-economics"]
---

# 506: How to Make a Coding Agent a General Purpose Agent - Harrison Chase

> **Creator**: MLOps.community | **Platform**: YouTube | **Date**: 2026-03-31 | **Duration**: 36:54

# How to Make a Coding Agent a General Purpose Agent

## Summary

Harrison Chase (LangChain CEO) and Sam Parry (Arcade.dev CTO) argue that the coding agent paradigm — exemplified by tools like Claude Code — provides the foundational architecture for building general-purpose agents that can serve entire organizations rather than just individual developers. Their core thesis is that the local file-system-centric design of coding agents (reading, writing, managing context in a workspace) is a pattern that naturally extends into broader agentic workflows when combined with a proper tool runtime layer.

The talk is structured around two complementary components: the **agent harness** (Harrison's domain) and the **tool runtime** (Sam's domain). The agent harness is the scaffolding around the model — planning tools, file system tools, sub-agents, context engineering, and human-in-the-loop controls — that gives you the "batteries included" experience of a coding agent. LangChain's implementation is called Deep Agents, built on top of LangGraph, and is explicitly modeled after Claude Code's architecture.

The tool runtime addresses what the harness alone cannot: multi-user authentication, authorization, and third-party service integrations. The speakers argue that deploying agents at enterprise scale requires a new pattern they call "delegated agent authorization" — where the agent receives a scoped portion of a user's credentials rather than relying on either a blunt service token or a full user token. Without this layer, agents either have dangerously over-privileged access or are too restricted to be genuinely useful across an organization.

## Key Concepts

### Agent Harness vs. Agent Framework vs. Agent Runtime

The speakers distinguish three layers: a **framework** (LangChain) handles abstractions and integrations; a **runtime** (LangGraph) provides infrastructure like durable execution, streaming, persistence, and human-in-the-loop; and a **harness** (Deep Agents) adds higher-level batteries — planning tools, file system tools, sub-agents, and context engineering. Most developers conflate these, but the harness is the layer that makes a raw LLM-in-a-loop feel like Claude Code.

### Pluggable File System Backend

Deep Agents introduces the concept of a virtual file system backed by a database rather than the local disk. The agent interacts with the same file-system interface it always uses (list, read, write, edit, glob, grep), but the underlying storage can be a database or sandbox. This enables remote deployment and multi-user scenarios without changing the agent's behavior or prompts — a key architectural move for scaling beyond the single-developer laptop use case.

### Context Engineering in the Harness

Several deliberate context management techniques are baked into the harness rather than left to the LLM: (1) large tool results are offloaded to files rather than injected directly into the context window; (2) a compaction step triggers at a configurable threshold, saving original messages to disk for potential retrieval; (3) the planning tool writes a plan into the context window without persisting it, nudging the model to reason about steps before acting. These are framed as giving the LLM more agency over its own context management.

### Sub-Agents and Context Isolation

Sub-agents in the harness provide **context isolation**: a sub-agent receives only the specific task delegated to it, does its work, and returns only the final result to the orchestrating agent. Neither the sub-agent's working memory nor the orchestrator's prior history bleeds across the boundary. This enables parallel execution and focused task completion but requires the orchestrator to be precise in task delegation — vague instructions cause coordination failures.

### Delegated Agent Authorization

The critical unsolved problem for enterprise agents is authentication and authorization across third-party services. Two naive patterns both fail: **service tokens** are either over-privileged (a CISO blocker) or too restricted to be useful; **user tokens** don't compose well when an agent is an intermediary serving many users across an organization. The proposed solution is delegated agent authorization — the agent holds a scoped, time-bound token representing a subset of a specific user's permissions for a specific set of services at a specific time. This is the responsibility of the tool runtime layer, not the harness.

## Practical Takeaways

- **Model your agent architecture on coding agents.** The file-system-centric workspace pattern (agent reads/writes state to disk rather than keeping everything in context) is directly applicable to general-purpose agents — it externalizes memory, enables long-running tasks, and limits context blowup.
- **Separate your harness from your tool runtime early.** Authentication/authorization concerns for third-party services should live in a dedicated runtime layer (e.g., Arcade), not baked into the agent harness. Mixing these creates the service-token antipattern.
- **Build context engineering into infrastructure, not prompts.** Offloading large tool results to files, triggering compaction, and using planning tools should be harness-level defaults — not things each team re-implements in system prompts.
- **Design sub-agent interfaces like API contracts.** The main agent must specify tasks precisely and sub-agents must return structured, complete results. Treat the orchestrator↔sub-agent boundary as a formal interface to avoid silent coordination failures.
- **Delegated authorization is the enterprise deployment bottleneck.** If you're building agents for company-wide use, solve the "how does this agent authenticate as *this specific user* to *this specific service*" problem before you hit scale — it cannot be retrofitted easily.

## Notable Quotes

> "An agent harness adds more things in. You can think of it as having more batteries included."
> — Harrison Chase

> "Why don't agents do that yet? Book the flight. Actually pay for it. Payment mechanisms. Notifying your team on Slack. OAuth integration. OAuth integration. OAuth integration. OAuth integration. This is the necessary evil that the tool runtime is responsible for."
> — Sam Parry

> "It's no longer just a web app with social sign-in you can use a user token for... You're giving it a portion of your user token for as many services as there are."
> — Sam Parry
