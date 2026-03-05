---
source_id: "196"
title: "Claude Opus 4.6 Agent Teams: Setup, Demo, and Cost Analysis"
creator: "Turing College"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=oC3F2SFaF9w"
date: "2026-02-26"
duration: "18:13"
type: "video"
tags: ["agent-teams", "multi-agent", "claude-code"]
curriculum_modules: ["05-team-orchestration", "04-agentic-patterns"]
---

# 196: Claude Opus 4.6 Agent Teams: Setup, Demo, and Cost Analysis

> **Creator**: Turing College | **Platform**: YouTube | **Date**: 2026-02-26 | **Duration**: 18:13

## Summary

A practical walkthrough of Claude Opus 4.6's agent teams feature, demonstrated through a social media content creation project. The video covers setup (enabling the experimental feature in settings.json, installing tmux for multi-pane agent visibility), a full end-to-end demo with specialized agents (strategist, copywriter, visual concept agent, reviewer), and an honest cost analysis. The key differentiator from sub-agents is that individual team members can be observed, interacted with directly, and can request information from each other rather than routing everything through a lead agent.

The demo reveals several notable behaviors: the system spawns agents you did not explicitly specify (a researcher agent appeared in the second iteration), agents work in genuine parallel visible through tmux panes, the reviewer identifies issues and feeds them back for a second iteration, and the lead agent automatically orchestrates task delegation. The cost reality is sobering — approximately $7-8 for a single complex task, consuming roughly 50% of a Pro plan's session budget or allowing 8-10 tasks per five-hour Max plan window.

## Key Concepts

### Agent Teams vs. Sub-Agents

Sub-agents operate within one session and only communicate results back to the main agent. Agent teams allow direct interaction with individual teammates, cross-agent information requests (e.g., the writing agent asking the research agent for more data), and a supervisor agent that coordinates ordering and prevents duplication. The tmux setup makes each agent's work visible in separate terminal panes.

### Automatic Orchestration with Emergent Agents

Claude determines what agents are needed based on the task. In the demo's second iteration, the system spawned a "researcher" agent that was never specified in the original prompt — it emerged from the reviewer's feedback that statistics needed verification. This demonstrates the system's ability to dynamically allocate specialized roles beyond what the user explicitly requests.

### Built-in Quality Control Loop

The reviewer agent does not just flag issues — it produces actionable items that can be fed back to the lead agent for a second pass. In the demo, the reviewer identified five issues (unverified statistics, inconsistent tone, placeholder content), and the second iteration addressed all of them with the researcher replacing statistics with verified figures and preparing a sources document.

### Cost Reality

A single complex agent teams task cost approximately $7-8, consuming about 50% of a Pro plan session or fitting 8-10 tasks into a five-hour Max plan window. This makes agent teams unsuitable for simple tasks where a single agent suffices. The recommendation is to reserve agent teams for tasks with multiple distinct components requiring different expertise and built-in quality control.

## Practical Takeaways

- **Enable agent teams in settings.json**: Add the experimental feature flag to your Claude configuration — it is not enabled by default.
- **Install tmux for visibility**: Without tmux, all agents share a single conversation view; tmux provides separate panes showing each agent's individual work.
- **Specify team roles in your prompt**: While not strictly necessary, explicitly listing desired roles (strategist, copywriter, reviewer) produces more consistent results.
- **Do not use agent teams for simple tasks**: Reserve them for complex multi-component projects — use single agents or sub-agents for focused tasks.
- **Budget for iteration**: The first pass produces a draft; feeding reviewer feedback back for a second pass significantly improves quality but doubles cost.
- **Monitor usage via /usage**: At $7-8 per complex task, costs add up quickly on both Pro and Max plans.

## Notable Quotes

> "If you would try to prompt a single AI model to do this sort of task, usually it wouldn't have enough of the context window to really get into every single day, every single post and match every platform that we need." — Turing College

> "The classic AI rule to double-check everything still applies in this case." — Turing College

## Related Sources

- [020: Agent Teams Deep Dive](020-simon-scrapes-agent-teams.md) — Earlier deep dive on Claude agent teams architecture
- [193: Agent Design Patterns with ADK](193-google-cloud-tech-agent-design-patterns.md) — Foundational multi-agent patterns (single, sequential, parallel)
- [146: Pi Coding Agent](146-indydevdan-pi-coding-agent.md) — Alternative multi-agent orchestration approaches

## Related Curriculum

- [Module 05: Team Orchestration](../curriculum/05-team-orchestration/README.md) — Agent teams, multi-agent coordination
- [Module 04: Agentic Patterns](../curriculum/04-agentic-patterns/README.md) — Sub-agents, orchestration patterns, quality control loops
