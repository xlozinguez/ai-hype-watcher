---
source_id: "014"
title: "I Gave Opus 4.6 an Entire Dev Team - Claude Code Agent Teams"
creator: "Leon van Zyl"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=KCJsdQpcfic"
date: "2026-02-09"
duration: "7:30"
type: "video"
tags: ["agent-teams", "multi-agent", "claude-code"]
curriculum_modules: ["05-team-orchestration"]
---

# 014: I Gave Opus 4.6 an Entire Dev Team - Claude Code Agent Teams

> **Creator**: Leon van Zyl | **Platform**: YouTube | **Date**: 2026-02-09 | **Duration**: ~7:30

## Summary

Leon van Zyl demonstrates Claude Code's experimental Agent Teams feature, building a fitness tracker app called "Claude Fit" with a five-member team of specialized agents. The video provides one of the clearest explanations of how agent teams differ architecturally from sub-agents: sub-agents are one-way reporting mechanisms where each agent works in isolation and reports back to the parent, while agent teams share a task list and have direct peer-to-peer messaging capabilities. This shared coordination layer means team members can communicate with each other -- for example, a database expert and an API developer can align on schema design in real time rather than working from separate, potentially incompatible assumptions.

The demonstration is concise but technically precise. Van Zyl walks through the full lifecycle: crafting the prompt to specify team composition and model (Opus for each member), watching the team lead create a shared task list before spawning specialized agents, interacting with individual team members mid-execution (including interrupting the UI designer to inject a skill instruction), and observing the team lead coordinate shutdowns as agents complete their work. Each team member has its own full Claude Code instance -- its own context window, tool access, skills, and MCP servers -- making the team genuinely parallel rather than time-sliced.

The video positions agent teams as the right tool for complex, multi-faceted builds (like standing up an entire application from scratch) while clearly stating that sub-agents remain better suited for isolated, one-off tasks like file exploration or targeted code changes. This practical scoping guidance, combined with the clear architectural comparison, makes the video a strong companion to the more hype-oriented agent team demonstrations in other sources.

## Key Concepts

### Agent Teams vs Sub-Agents

The core architectural distinction:

- **Sub-agents**: The main agent spawns background agents for specific tasks. Each sub-agent has its own context window but cannot see what other sub-agents are doing. Communication is strictly one-way: sub-agent reports back to parent. "One sub-agent in theory could implement a change that's actually not compatible with what sub-agent 2 is doing."
- **Agent Teams**: The main agent becomes team lead and creates a shared task list. All team members can see the full task list and communicate directly with each other via peer-to-peer messaging. They coordinate automatically because they share the same coordination layer.

This is the difference between sending five people to work in separate rooms with instructions to report back versus bringing five people into the same room where they can talk to each other while working.

### Shared Task List as Coordination Layer

When an agent team is created, the first action the team lead takes is to build a task list. This list is shared across all team members and serves as the primary coordination mechanism. Team members can see what others are working on, understand dependencies, and communicate about interface boundaries (e.g., a database expert and API developer aligning on schema). This contrasts sharply with the sub-agent model where the parent agent is the sole coordination point.

### Individual Agent Autonomy

Each team member runs as a full Claude Code instance with its own context window, tool access, skills, and MCP servers. The video demonstrates this by pressing Escape to interrupt just the UI designer -- the other four agents continue running unaffected. Van Zyl then sends a message specifically to the interrupted UI designer ("please use the front end design skill to assist you with the UI design"), showing that individual team members can receive targeted instructions mid-execution without disturbing the rest of the team.

### Team Composition and Role Design

The demonstration uses five specialized roles: UX/UI designer, back-end developer, technical architect, database expert, and a devil's advocate who "will basically question everything the other team members do." The devil's advocate role is notable -- it functions as a built-in quality gate and stress-test agent, similar in spirit to the validator pattern from source #001 but operating as a team peer rather than a paired review agent. The prompt specifies Opus as the model for each team member.

### When to Use Agent Teams vs Sub-Agents

Van Zyl provides clear scoping guidance: "Agent teams is really meant to implement complex changes. If you just want to do like a once-off task, you should definitely use sub agents instead. But for complicated tasks like setting up an entire project from scratch, agent teams can definitely help you get way better results out of the box." This practical boundary -- complexity and inter-dependency of the work -- is the deciding factor.

### Setup and Configuration

Agent teams is an experimental feature enabled by adding a property to the Claude Code `settings.json` file. To create a team, you describe the desired team members in your prompt ("Create an agent team to explore this from different angles"), specify the model for each member, and enable delegation mode with Shift+Tab. The setup is lightweight -- no external infrastructure, no Docker containers, no tmux -- just configuration and a well-structured prompt.

## Practical Takeaways

- **Use agent teams for multi-faceted builds, sub-agents for isolated tasks**: The shared task list and peer-to-peer messaging of agent teams add coordination overhead that is only worthwhile for complex, interdependent work.
- **Include a devil's advocate or reviewer role**: Adding a team member whose job is to challenge assumptions and question decisions creates a built-in quality gate without requiring a separate validation pass.
- **Interact with individual agents mid-execution**: You can interrupt, redirect, and instruct specific team members without affecting the rest of the team -- use this to inject skills, correct course, or refine requirements on the fly.
- **Combine agent teams with skills**: Each team member can access installed skills, so the UI designer can leverage the front-end design skill while the back-end developer uses different capabilities -- skills compose naturally with the team model.

## Notable Quotes

> "This is the equivalent of bringing a bunch of people into the same room and they can converse with each other to work together to achieve a task." -- Leon van Zyl

> "One sub agent does not have a view of what another sub agent is doing. So, sub agent one in theory could implement a change that's actually not compatible with what sub agent 2 is doing." -- Leon van Zyl

## Related Sources

- [004: Claude Code's New Agent Teams Are Insane](004-bart-slodyczka-agent-teams.md) -- Bart's earlier agent teams walkthrough comparing single-agent vs team results; Van Zyl's video adds the sub-agent architectural comparison and individual agent interaction
- [010: Claude Code Multi-Agent Orchestration with Opus 4.6](010-indydevdan-multi-agent-orchestration.md) -- IndyDevDan's more advanced orchestration using tmux and E2B sandboxes; Van Zyl covers the simpler built-in agent teams path
- [001: Claude Code Task System: ANTI-HYPE Agentic Coding](001-indydevdan-claude-code-task-system.md) -- The task system underlying agent teams; the builder/validator pattern maps to Van Zyl's devil's advocate role concept
- [013: Stop Using Claude Code Without Skills](013-leon-van-zyl-claude-code-skills.md) -- Van Zyl's companion skills video; the UI designer instruction mid-execution demonstrates skills + teams composition

## Related Curriculum

- [Module 05: Team Orchestration](../curriculum/05-team-orchestration/README.md) -- Agent team setup, role design, shared task coordination, and sub-agent vs team decision framework
