---
source_id: "010"
title: "Claude Code Multi-Agent Orchestration with Opus 4.6, Tmux and Agent Sandboxes"
creator: "IndyDevDan (Dan Disler)"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=RpUTF_U4kiw"
date: "2026-02-09"
duration: "24:02"
type: "video"
tags: ["multi-agent", "agent-teams", "agentic-coding", "claude-code"]
curriculum_modules: ["05-team-orchestration"]
---

# 010: Claude Code Multi-Agent Orchestration with Opus 4.6, Tmux and Agent Sandboxes

> **Creator**: IndyDevDan (Dan Disler) | **Platform**: YouTube | **Date**: 2026-02-09 | **Duration**: 24:02

## Summary

IndyDevDan demonstrates the new Claude Code multi-agent orchestration capabilities powered by Opus 4.6. The video goes beyond benchmarks to show practical usage: spinning up teams of specialized agents that work in parallel, each with their own context window, model, and tasks. He orchestrates two full teams of four Opus agents running simultaneously across eight full-stack applications using Tmux, E2B agent sandboxes, and the new Claude Code experimental agent teams feature, paired with his open-source multi-agent observability system for full visibility into agent activity.

The central thesis is that the engineering game has changed. As of Sonnet 4.5 and now Opus 4.6, the models can do far more than most engineers know how to unlock. The true constraint is now twofold: the tools available to engineers, and engineers' own ability to prompt engineer and context engineer outcomes into reusable agentic systems. The video serves as both a practical tutorial and a demonstration of the "scale compute to scale impact" philosophy.

## Key Concepts

### Models Are No Longer the Constraint

IndyDevDan's core argument: as of Sonnet 4.5 (and now Opus 4.6), the models can do far more than most engineers know how to unlock. The true constraint is now the tools available and your ability to prompt engineer and context engineer outcomes, then build them into reusable agentic systems. Every engineer is limited by their tools and their knowledge of their tools.

### Demo Setup: Eight Full-Stack Applications

The demo starts with eight unique full-stack applications (not just frontends -- complete applications with backends), all one-shotted by Claude Opus 4.6 in E2B agent sandboxes. Applications include an agentic support dashboard, photo gallery, mission briefings dashboard, portfolio tracker, recipe app, ad performance dashboard, developer tools (pull requests), and data visualization app.

### Enabling Multi-Agent Orchestration

The setup requires:
1. Open a Tmux session (required for multi-pane visualization)
2. Export the experimental flag: `export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`
3. Launch Claude Code within the Tmux session

### First Agent Team: Summarize Eight Codebases

The prompt "Build a new agent team for each codebase in this directory. Have an agent summarize and how to set it up" triggers the following sequence:
1. Primary agent creates a task list (centralized hub for orchestration)
2. Primary agent opens new Tmux panes for each sub-agent
3. Eight Haiku agents spin up, each exploring a different codebase
4. Each agent has its own context window, model, session ID, and unique name
5. Agents complete work and send results back
6. Primary agent compiles summaries -- only used 31% of its context window despite orchestrating eight agents

The observability system captured 160+ tool calls in under a minute, with full visibility into each agent's activity.

### Second Demo: Reboot Applications in Agent Sandboxes

A more complex workflow using four Opus 4.6 agents in parallel:
1. Primary agent runs the agent sandbox skill and /command skill to understand available tools
2. Creates task list, then kicks off a team of four Opus 4.6 agents
3. Each agent runs the sandbox skill independently, sets up E2B environments, uploads code, installs dependencies
4. All four agents run in parallel, visible in Tmux panes
5. A second team of four agents handles the remaining four applications in a separate Tmux window

Result: Two teams of four agents running simultaneously. Six out of eight sandbox environments successfully rebooted (two had data issues that were then addressed by spinning up another ad hoc agent team).

### The Multi-Agent Orchestration Lifecycle

The full workflow:
1. **Create the team** (TeamCreate)
2. **Create tasks** (TaskCreate)
3. **Spawn agents** (one per task)
4. **Work in parallel** (agents communicate via SendMessage)
5. **Shut down agents** when work completes
6. **Delete the team** (TeamDelete) -- forces good context engineering by resetting context

### New Claude Code Orchestration Tools

Three categories of tools enable this workflow:

**Team Management:**
- `TeamCreate` -- create a new agent team
- `TeamDelete` -- delete a team when work is done

**Task Management:**
- `TaskCreate` -- create tasks for agents
- `TaskList` -- list all tasks
- `TaskGet` -- get details of a specific task
- `TaskUpdate` -- update task status

**Communications:**
- `SendMessage` -- how agents communicate with each other and the primary orchestrator

### Multi-Agent Observability

IndyDevDan's open-source observability system (github.com/disler/claude-code-hooks-multi-agent-observability) provides:
- Session start/end hooks captured automatically
- Every tool call, agent session, and task update traced
- "Swim lanes" for individual agents to see their specific activity
- Searchable tool types across the fleet
- 160+ tool calls tracked in under a minute

### Agent Sandboxes at Scale

- Uses E2B (e2b.dev) for cloud-based agent sandboxes
- Had 24 sandboxes running simultaneously during the demo
- Each sandbox runs for 12 hours
- Mac Mini noted as a local sandbox alternative for privacy-sensitive workflows
- Custom skill/agent can list and manage all running sandboxes

### The Core Four Framework

Everything in agentic engineering comes back to four fundamentals:
1. **Context** -- what information the agent has
2. **Model** -- the AI model being used
3. **Prompt** -- how you instruct the agent
4. **Tools** -- what capabilities the agent has access to

### Engineers vs. Vibe Coders

A recurring theme: engineers who understand what is happening under the hood will vastly outperform "vibe coders" who do not. Understanding the underlying mechanics -- context windows, tool calls, task management, agent lifecycle -- is what separates effective multi-agent orchestration from trial and error. Engineers are the best positioned to use agentic technology because they understand the systems they are building on top of.

## Practical Takeaways

- **Multi-agent orchestration is now native in Claude Code**: Enable with `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` in a Tmux session. No custom frameworks required.
- **Use Tmux for visualization**: The multi-pane view lets you see all agents working simultaneously, providing the visual feedback loop needed for effective oversight.
- **Delegate to preserve context**: The primary agent used only 31% of its context window while orchestrating eight sub-agents, demonstrating that delegation is also a context engineering strategy.
- **Delete teams when done**: Forcing a clean context reset between teams is a best practice for maintaining quality across multi-step workflows.
- **Invest in observability**: Without visibility into what agents are doing, you cannot improve your systems. Track tool calls, session events, and task updates.
- **Agent sandboxes are essential for scale**: Use E2B or similar for cloud-based sandboxes, or a dedicated local device (Mac Mini) for privacy-sensitive workflows. Agents need their own environments to avoid jeopardizing your local machine.
- **Scale compute to scale impact**: Each additional agent multiplies your engineering throughput. 160+ tool calls in under a minute across a fleet is the new baseline.
- **Understanding beats vibing**: Engineers who understand context windows, tool calls, and agent lifecycles will outperform those who do not, regardless of how powerful the model becomes.

## Notable Quotes

> "The true limitation is you and I." -- IndyDevDan

> "This is where vibe coders fall apart. They don't actually know what's going on. And so the engineers, the builders, and even the vibe coders that know what's going on underneath the hood can do so much more." -- IndyDevDan

> "This whole idea that engineers are going to be replaced by this technology to me is absurd. Engineers are the best positioned to use agentic technology." -- IndyDevDan

## Related Sources

- [008: The Capability Overhang](008-nate-b-jones-phase-transition.md) -- Discusses the same Task System and multi-agent patterns from a strategic perspective
- [006: 4 AI Skills That Set You Apart](006-ali-salem-4-ai-skills.md) -- Foundational skills framework; the "Core Four" parallels Ali Salem's prompting framework

## Related Curriculum

- [Module 05: Team Orchestration](../curriculum/05-team-orchestration/README.md) -- Multi-agent team patterns, observability, and scaling compute for engineering impact
