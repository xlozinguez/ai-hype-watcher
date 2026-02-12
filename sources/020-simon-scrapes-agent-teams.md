---
source_id: "020"
title: "How & When to Use Claude Code Agent Teams in 13 Mins (Opus 4.6)"
creator: "Simon Scrapes | AI Automation"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=y9IYtWELMHw"
date: "2026-02-11"
duration: "13:13"
type: "video"
tags: ["agent-teams", "multi-agent", "claude-code", "agentic-coding", "context-engineering", "task-system"]
curriculum_modules: ["05-team-orchestration", "04-agentic-patterns", "03-claude-code-essentials"]
---

# 020: How & When to Use Claude Code Agent Teams in 13 Mins (Opus 4.6)

> **Creator**: Simon Scrapes | AI Automation | **Platform**: YouTube | **Date**: 2026-02-11 | **Duration**: 13:13

## Summary

Simon Scrapes provides a practical guide to Claude Code's agent teams feature, explaining the progression from single agents to sub-agents to full agent teams. The video addresses a critical limitation of single-agent workflows: context rot. As context windows fill (especially around 95%), Claude begins compressing and summarizing information, losing key details that matter for larger projects. Agent teams solve this by enabling true collaboration between specialized agents through a shared task list, rather than the hub-and-spoke model of traditional sub-agents.

The tutorial includes hands-on configuration steps (enabling experimental features in settings.json), demonstrates three use cases ranked by complexity (2/10, 6/10, and 8/10), and provides clear decision heuristics for when to use single agents, sub-agents, or full agent teams. The key insight is that agent teams shine when tasks require genuine cross-agent collaboration and parallel execution, not just delegation.

## Key Concepts

### Context Rot and Single Agent Limitations
Single agents suffer from degraded performance as their context window fills. At approximately 95% capacity, Claude compresses and summarizes earlier information, making it unable to retrieve key details from thousands of tokens ago ([0:43](https://www.youtube.com/watch?v=y9IYtWELMHw&t=43)). This creates a fundamental bottleneck for larger projects where all details matter, not just isolated tasks.

### Sub-Agents: The Hub-and-Spoke Model
Sub-agents emerged as a community solution to context rot, offering two main benefits: improved output quality through specialization (hiring specialists vs generalists) and faster execution through parallel processing ([1:21](https://www.youtube.com/watch?v=y9IYtWELMHw&t=81)). However, sub-agents operate in a hub-and-spoke architecture where only the main agent coordinates all work. Sub-agents can only report back to the parent and cannot communicate with each other, creating a bottleneck where the main agent becomes overwhelmed coordinating multiple specialists ([3:01](https://www.youtube.com/watch?v=y9IYtWELMHw&t=181)).

### Agent Teams: Shared Task Lists and Cross-Collaboration
Agent teams solve the collaboration gap through a shared task list that enables both main-agent communication and peer-to-peer interaction between teammates ([3:37](https://www.youtube.com/watch?v=y9IYtWELMHw&t=217)). Each agent runs as its own Claude Code instance with its own context window, but unlike sub-agents, they can communicate with each other directly. The tradeoff is token cost: all teammates inherit access to the main agent's claude.md file and MCPs, putting everything into each teammate's context.

## Practical Takeaways

- **Enabling Agent Teams**: Set `"claude.code.experimental.agentTeams": true` in settings.json and ensure Claude Code version 2.1.32 or later. Restart the instance after configuration. ([4:26](https://www.youtube.com/watch?v=y9IYtWELMHw&t=266))

- **Use Case Ranking System**: Apply a 1-10 complexity scale to determine the right approach. Low complexity (2/10) like parallel content creation for different platforms doesn't need collaboration ([5:45](https://www.youtube.com/watch?v=y9IYtWELMHw&t=345)). Medium complexity (6/10) like content repurposing from transcripts benefits from consistency coordination ([6:22](https://www.youtube.com/watch?v=y9IYtWELMHw&t=382)). High complexity (8/10) like building a Next.js app with Stripe requires genuine cross-agent collaboration between API, frontend, and testing teams ([7:20](https://www.youtube.com/watch?v=y9IYtWELMHw&t=440)).

- **Decision Heuristic**: Start with single agents for straightforward tasks with one file or feature. Graduate to sub-agents as projects grow and context becomes too large, using specialists to improve quality and reduce costs. Reach for agent teams only when tasks genuinely need cross-collaboration and parallel execution with interdependencies. ([12:07](https://www.youtube.com/watch?v=y9IYtWELMHw&t=727))

- **Team Control**: Use shift+up and shift+down to navigate between teammates in the terminal. With T-Max installed, agents split into individual windows showing each agent's context and work. You can interrupt specific teammates and assign tasks directly to individuals. ([8:29](https://www.youtube.com/watch?v=y9IYtWELMHw&t=509))

- **Key Limitations**: Teammates don't inherit conversation history from the main workflow (no context inheritance). Permissions do propagate from main to teammates. Token costs multiply with more agents, so reserve agent teams for truly collaborative tasks. ([11:15](https://www.youtube.com/watch?v=y9IYtWELMHw&t=675))

## Notable Quotes

> "The longer it runs, the worse it gets. It's forgetting context, introducing bugs, and forcing you to repeat yourself." — Simon Scrapes ([0:00](https://www.youtube.com/watch?v=y9IYtWELMHw&t=0))

> "Sub agents acted like a hub and spoke model and they gave us delegation but they didn't give us collaboration and that's the gap that the agent teams actually fills." — Simon Scrapes ([3:01](https://www.youtube.com/watch?v=y9IYtWELMHw&t=181))

> "Start simple, graduate to sub agents as the project gets more complex and then reach for agent teams when the task genuinely needs that cross collaboration." — Simon Scrapes ([12:07](https://www.youtube.com/watch?v=y9IYtWELMHw&t=727))

## Related Sources

- [004: Bart Slodyczka - Agent Teams](004-bart-slodyczka-agent-teams.md) — Early exploration of multi-agent patterns in Claude Code
- [010: IndyDevDan - Multi-Agent Orchestration](010-indydevdan-multi-agent-orchestration.md) — Deeper dive into orchestration patterns and coordination strategies
- [014: Leon van Zyl - Agent Teams](014-leon-van-zyl-agent-teams.md) — Alternative perspective on when and how to structure agent teams

## Related Curriculum

- [Module 05: Team Orchestration](../curriculum/05-team-orchestration/README.md)
- [Module 04: Agentic Patterns](../curriculum/04-agentic-patterns/README.md)
- [Module 03: Claude Code Essentials](../curriculum/03-claude-code-essentials/README.md)
