---
source_id: "067"
title: "Learn 90% Of Claude Code Agent Teams in 22 Minutes (Opus 4.6)"
creator: "Bart Slodyczka"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=cSkoaCCmq0w"
date: "2026-02-13"
duration: "22:02"
type: "video"
tags: ["agent-teams", "multi-agent", "claude-code", "context-engineering", "skills"]
curriculum_modules: ["05-team-orchestration", "03-claude-code-essentials"]
---

# 067: Learn 90% Of Claude Code Agent Teams in 22 Minutes (Opus 4.6)

> **Creator**: Bart Slodyczka | **Platform**: YouTube | **Date**: 2026-02-13 | **Duration**: 22:02

## Summary

Bart Slodyczka delivers a comprehensive walkthrough of Claude Code's agent teams feature, structured as a course covering the full lifecycle: conceptual overview, environment setup, session management, team interaction via tmux, graceful shutdown, and reusable skills for future teams. The video is positioned as a follow-up to his earlier agent teams demo ([004](004-bart-slodyczka-agent-teams.md)), shifting from "look what this can do" to "here's how to use it properly."

The core pedagogical contribution is a clear three-mode mental model for Claude Code usage: default mode (single session), sub-agent mode (delegated tasks within one session), and agent teams mode (multiple independent sessions with peer communication). Bart uses a security team analogy throughout -- a control room dispatching guards to different floors of a building -- to make the architectural distinctions intuitive. He also demonstrates a practical research use case (not code) and covers cost awareness, model selection strategy, and the skill-creation workflow for turning ad hoc team processes into repeatable operations.

## Key Concepts

### Three Modes of Claude Code

Bart frames the three modes as a progression in session architecture:

1. **Default mode**: One terminal, one session, one agent. Useful as a "control panel" for configuration and simple tasks. Suffers from tunnel vision on large codebases -- the model gravitates toward one area and struggles to pull back out.

2. **Sub-agent mode**: Still one primary session, but the main agent can dispatch sub-agents to handle discrete tasks. The sub-agent goes away, completes the work, and returns only a summary -- preserving tokens in the main session's context window. Analogous to sending a security guard from the control room to investigate a specific floor and report back.

3. **Agent teams mode**: Each agent gets its own independent session with its own context window. A team leader understands the assignment, breaks it into tasks, creates prompts for each teammate, and coordinates. Agents can communicate with each other via walkie-talkie-style messaging. The key advantage: multiple agents examine the problem from different angles, avoiding the single-session tunnel vision problem.

### Token Conservation as Architectural Driver

The progression from default to sub-agents to teams is fundamentally about managing finite context windows. In default mode, a large codebase exhausts the token budget and the model starts hallucinating or losing earlier context. Sub-agents conserve the primary session's tokens by doing work externally and returning only summaries. Agent teams take this further by giving each teammate a fresh context window, enabling deeper investigation of their assigned area without polluting the shared context.

### Tmux as Agent Room Management

Bart frames tmux as giving each agent its own "room" rather than having all agents talk over each other in one terminal. Two interaction modes exist:

- **In-process mode** (default): All agents share one terminal -- noisy and hard to follow.
- **Split-pane mode** (requires tmux): Each agent gets a dedicated terminal pane, enabling you to observe and interact with individual agents independently.

Setup requires: (1) installing tmux, (2) setting `teamUx: "splitPanes"` to true in settings.json, and (3) starting a tmux session before launching Claude Code.

### Team Leader Delegation and Context Inheritance

When you prompt "create an agent team," the team leader analyzes the request, determines the tasks, crafts individual prompts for each teammate, and spools them up. Critically, teammates do not inherit the full conversation history from the main session. If you have been chatting for 30 minutes in default mode before switching to agent teams, the teammates will not have that context unless you explicitly provide it (e.g., via an MD file the team leader instructs them to read).

### Race Condition Protection

When multiple agents share a task list and finish their current work simultaneously, Anthropic's implementation includes race condition checks to prevent two agents from picking up the same task. This prevents duplicate token expenditure on overlapping work.

### Model Selection for Cost Optimization

The team leader does not have to use the same model for all teammates. You can specify cheaper models (e.g., Sonnet) for team members doing simpler tasks while reserving Opus 4.6 for the lead or complex reasoning tasks. Bart recommends starting with the regular Opus model at low effort, then escalating effort level and model tier only as needed.

### Agent Shutdown and Persistence

- **Graceful shutdown**: The team leader iterates through agents, confirms tasks are complete, and closes sessions. Agents can reject shutdown requests if they believe their work is mission-critical.
- **Idle persistence for coding tasks**: For development work, the team leader often leaves agents idling after task completion so you can test results and send them back for fixes. This preserves the agent's context about what they worked on.
- **Shared memory files**: For cross-session persistence, create a shared MD file where agents log bugs, fixes, and issues. Future sessions can reference this file to inherit knowledge from previous runs.

### Skills for Repeatable Team Processes

Bart's final section covers turning ad hoc team workflows into Claude Code skills. His recommended approach:

1. Run the full process manually with Claude Code first (e.g., a research team workflow).
2. Iterate until the process is refined.
3. Prompt Claude to "turn whatever we just did into a skill" with configurable variables (topic, model, etc.).
4. The skill is stored in the repository and invoked via `/skillname` in future sessions.
5. Update the skill incrementally as the process evolves.

This creates a feedback loop: each team session improves the skill definition for future teams.

## Practical Takeaways

- **Start at low effort, escalate as needed**: Use Opus 4.6 at low effort for initial team runs. Increase effort level or switch to the 1M token context model only when you hit quality issues -- this avoids unnecessary cost.
- **Use tmux for any team with more than two agents**: In-process mode becomes unmanageable quickly. Tmux split panes let you monitor and interact with agents individually.
- **Provide context explicitly via MD files**: Teammates do not inherit conversation history. If context from prior work matters, write it to a shared file and instruct the team leader to have agents read it.
- **Define agent models in your prompt**: You can specify different models per teammate to optimize cost -- not every agent needs Opus 4.6.
- **Monitor costs after each team session**: Check the cost tab to understand per-session spending and refine your prompting and model selection for next time. Bart's research team example cost $1.15 for a 4-minute multi-agent session.
- **Convert repeatable team processes into skills**: If you find yourself running similar team configurations repeatedly, extract the process into a skill with configurable variables. Do not write skills from scratch -- run the process first, then have Claude generate the skill from the actual workflow.

## Notable Quotes

> "In default mode, these models tend to gravitate towards one specific area and kind of get tunnel vision and only focus on that one area." -- Bart Slodyczka, explaining why multi-agent approaches exist

> "The value of sub-agents is the way that you actually conserve the tokens for your primary session because these models don't have an infinity capacity." -- Bart Slodyczka, on the architectural motivation for sub-agents

> "The best way to create skills is not to just write it from scratch and upload it. It's to actually complete the skill as a process first using Claude Code and then get Claude Code to create that skill for you." -- Bart Slodyczka, on skill authoring workflow

## Related Sources

- [004: Claude Code's New Agent Teams Are Insane](004-bart-slodyczka-agent-teams.md) -- Bart's earlier demo comparing single agent vs. agent team output quality; this video is the pedagogical follow-up
- [020: How & When to Use Claude Code Agent Teams in 13 Mins](020-simon-scrapes-agent-teams.md) -- Simon Scrapes covers similar ground with a complexity-based decision heuristic (2/10 vs 6/10 vs 8/10)
- [010: Claude Code Multi-Agent Orchestration with Opus 4.6](010-indydevdan-multi-agent-orchestration.md) -- IndyDevDan's deeper dive into orchestration patterns
- [014: I Gave Opus 4.6 an Entire Dev Team](014-leon-van-zyl-agent-teams.md) -- Leon van Zyl's alternative perspective on team structuring
- [015: I finally CRACKED Claude Agent Skills](015-indydevdan-skills-engineering.md) -- Skills engineering patterns that complement the skill-creation workflow described here

## Related Curriculum

- [Module 05: Team Orchestration](../curriculum/05-team-orchestration/README.md) -- Core module for agent team coordination, tmux setup, and team lifecycle management
- [Module 03: Claude Code Essentials](../curriculum/03-claude-code-essentials/README.md) -- Skills system and configuration covered in this video
