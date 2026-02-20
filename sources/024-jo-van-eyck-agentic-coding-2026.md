---
source_id: "024"
title: "You are Not Ready: Agentic coding in 2026"
creator: "Jo Van Eyck"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=6W_-YWHKwZ4"
date: "2026-02-08"
duration: "31:04"
type: "video"
tags: ["agentic-coding", "claude-code", "multi-agent", "agent-teams", "context-engineering", "prompt-engineering", "skills", "capability-overhang"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns", "05-team-orchestration"]
---

# 024: You are Not Ready: Agentic coding in 2026

> **Creator**: Jo Van Eyck | **Platform**: YouTube | **Date**: 2026-02-08 | **Duration**: 31:04

## Summary

Jo Van Eyck delivers a comprehensive state-of-the-art overview of agentic coding in early 2026, arguing that most software engineers are underestimating the current capabilities and pace of change. Speaking as a self-described "AI skeptic" with 15 years of software engineering experience, Van Eyck identifies five key innovations that have shifted the landscape in recent months: LLMs fine-tuned specifically for agentic work, the Ralph Wiggum loop (deterministic verification wrapped around agents), Beats (persistent task management), Gas Town (multi-agent orchestration), and OpenClaw (AI personal assistant proof-of-concept).

The core framework is the AI Coding Maturity Ladder with five levels: Chat, Mid-Loop Generation, In-the-Loop Agentic, On-the-Loop Agentic, and Multi-Agent. Van Eyck emphasizes that engineers must master each level sequentially before advancing, with particular focus on spending months at the In-the-Loop stage to understand failure modes and build guard rails. He positions Claude Code as the most complete implementation of these agentic patterns, though warns about costs — multi-agent setups can require "multiple hundreds of dollars" for serious experimentation.

The talk concludes with a skills evolution framework: syntax and hand-coding in established codebases are fading; system design, architecture, work decomposition, and judgment remain evergreen; and prompt engineering, context engineering, and agentic workflow debugging are emerging as new core competencies. Van Eyck references Andrej Karpathy's observation that we're entering "the decade of agents" rather than just "the year of agents," suggesting software engineering job security remains but the nature of the work will fundamentally change.

## Key Concepts

### Fine-Tuned Models for Agentic Work
Recent models (Claude 4 family, GPT-5 range, Qwen Coder 3) are being specifically optimized for "long horizon work" — hours of autonomous execution without human intervention. This represents a shift from conversational chat optimization to sustained, multi-step tool-calling capability.

### Ralph Wiggum Loop
A simple but powerful pattern: wrapping a while loop around a coding agent with deterministic verification as the halting condition. If code doesn't compile or tests don't pass, the loop continues with a new session. This addresses the "lying agent" problem where models claim completion despite broken output. The deeper insight is that persistence matters more than raw intelligence — agents don't need AGI, they need to iterate until they reach a verifiable completion state.

### Autonomy Slider
Van Eyck describes his personal evolution from "babysitting" agents (watching every line of code) to "preparing a package of work, giving it off to an agent, and only coming back when it's in a stage of high quality and guaranteed completion." This shift represents moving from In-the-Loop to On-the-Loop coding.

### Beats (Persistent Task Management)
A "Trello board for your coding agents" — persistent memory outside the context window (implemented as JSON in a git repository). Enables breaking work into subtasks, identifying dependencies, and tracking completion state. Agents can query the next task and update status, creating a coordination mechanism beyond ephemeral context windows.

### Gas Town (Multi-Agent Orchestration)
The "logical conclusion" of Beats: managing a fleet of agents that pick up tasks from a shared board and update states. Described as "a bit of a fever dream" but representing the direction of the field. Multi-agent orchestration requires thinking about work decomposition, parallelization, and coordination at scale.

### OpenClaw
An AI personal assistant proof-of-concept that demonstrates current LLM capabilities given proper tool access. Van Eyck warns it's "wildly insecure" and "a security nightmare," but when run in a controlled environment ("nuclear bunker with nuclear grade defenses"), it shows that near-AGI assistant behavior is achievable with today's models plus tool integration.

### Claude Code as Integration Platform
Anthropic's Claude Code implements all the discussed patterns in experimental form: hooks (Ralph Wiggum-style verification), sub agents (separate context windows), teams (Gas Town-style orchestration), and improved plan mode (Beats-like persistent JSON task management). Van Eyck positions it as "poor man's OpenClaw" but effective for agentic coding workflows.

### AI Coding Maturity Ladder
A five-level progression model:

1. **Chat**: Using ChatGPT/Claude via web interface. Skills: basic prompt engineering, context window management.
2. **Mid-Loop Generation**: IDE autocomplete integration (Cursor, Copilot). Skills: using types, evaluating suggestions.
3. **In-the-Loop Agentic**: Human-supervised agent coding sessions. Critical learning phase — must spend 2-3 months here to understand failure modes, build prompt/skill libraries, and develop debugging instincts.
4. **On-the-Loop Agentic**: Agent works autonomously from specification to completion while human is away. Human verifies output but doesn't supervise execution.
5. **Multi-Agent Coding**: Claude Code teams, Gas Town-level orchestration. Cutting edge as of February 2026 — "everyone's figuring it out as they go."

Van Eyck emphasizes sequential mastery: skipping levels leads to dangerous outcomes. Starting with multi-agent without mastering guard rails, test automation, and reusable skills will "shoot yourself, your organization, and your friends in the foot."

### Skills Evolution Framework

**Fading Skills**:
- Syntax knowledge of programming languages
- Hand-coding in well-established codebases with existing patterns
- (Note: Van Eyck advises junior engineers to still write code by hand to build mental models)

**Evergreen Skills**:
- System design and architecture
- Creating "walking skeletons" (minimal functional vertical slices with good design)
- Taking fuzzy problems and making them concrete (PRDs, user stories, requirements)
- Work decomposition into small vertical chunks ("elephant carpaccio")
- Judgment and taste — knowing what good code looks like
- Ownership and accountability

**New Skills**:
- Prompt engineering
- Context engineering
- Harness engineering (setting up agentic workflows, custom pipelines)
- Agentic workflow debugging and improvement

### Cost Warning
Multi-agent experimentation with latest Sonnet/Opus models costs "multiple hundreds of dollars." Van Eyck advises solo developers to factor this into pricing and enterprise developers to wait for company-provided keys rather than paying out of pocket.

### Ownership and Accountability
Van Eyck stresses that AI agents "cannot become accountability sinks." Engineers must maintain ownership over code pushed to production, which requires understanding the code deeply enough to take responsibility. This necessitates periodic hands-on engagement even when using On-the-Loop or Multi-Agent approaches.

## Practical Takeaways

- **Start at your current level and master it before advancing**: The maturity ladder requires sequential progression. Jumping ahead without foundational skills creates risk.

- **Spend 2-3 months In-the-Loop**: Every engineer should spend extended time at level 3, watching agents struggle and building intuition about failure modes, guard rails, and prompt refinement.

- **Build guard rails before going On-the-Loop**: Test automation, security scanners, deterministic verification — these must be in place before giving agents autonomy.

- **Develop a prompt library and skill library**: Extract reusable patterns from interactive sessions. This is core In-the-Loop work that pays dividends at higher levels.

- **Focus on work decomposition**: As multi-agent orchestration becomes viable, the ability to break fuzzy problems into concrete, parallelizable tasks becomes critical. Learn "elephant carpaccio" techniques.

- **Maintain judgment through hands-on practice**: Even when delegating implementation to agents, periodically write code by hand to maintain understanding and cultivate a sense of what good code looks like.

- **Factor AI costs into pricing**: Multi-agent workflows are not cheap. Solo developers should include hundreds of dollars per project in their estimates; enterprises should provide keys rather than expecting developers to pay out of pocket.

- **Don't install OpenClaw on your machine**: It's a security nightmare. The lesson is about what's possible with proper tooling and constraints, not about running it in production.

- **Watch Claude Code for emerging patterns**: Anthropic is implementing cutting-edge agentic ideas (hooks, sub agents, teams, plan mode) in accessible form, making it a good laboratory for experimentation.

- **Prepare for the decade of agents**: This is not a one-year transition. The fundamental nature of software engineering work is shifting toward agentic workflow setup, debugging, and orchestration.

## Notable Quotes

> "I still see a lot of software engineers, especially older seasoned engineers, being very skeptical about how far AI coding agents will actually get. And I think there's a structural under appreciation of where we are right now. I think 2026 will be a sobering year for a whole lot of people." — Jo Van Eyck ([0:00](https://www.youtube.com/watch?v=6W_-YWHKwZ4&t=0))

> "Ralph is a while loop put around a coding agent. The halting condition or the break statement to jump out of the while loop is a deterministic way to verify whether or not work is done." — Jo Van Eyck ([3:10](https://www.youtube.com/watch?v=6W_-YWHKwZ4&t=190))

> "We do not need AGI, we do not need super smart models, we just need persistence." — Jo Van Eyck ([4:29](https://www.youtube.com/watch?v=6W_-YWHKwZ4&t=269))

> "Six months in my AI coding journey, things have shifted dramatically. I am not babysitting these things because of all the innovations we just discussed and the quality of code that meets my eyes for the first time is almost indistinguishable from the quality of code that I hand-rolled before." — Jo Van Eyck ([13:19](https://www.youtube.com/watch?v=6W_-YWHKwZ4&t=799))

> "When you see a coding agent doom loop, your mind should go, 'How can I help? Install guard rails, improve my prompt, improve the design of my codebase?'" — Jo Van Eyck ([18:20](https://www.youtube.com/watch?v=6W_-YWHKwZ4&t=1100))

> "If you start with a multi-agent coding setup and you have not implemented reusable skills, played around with MCP servers, put in guard rails like test automation, security vulnerability scanners — you will shoot yourself, your organization, and your friends in the foot." — Jo Van Eyck ([22:07](https://www.youtube.com/watch?v=6W_-YWHKwZ4&t=1327))

> "Learning languages on a syntax level doesn't make a lot of sense." — Jo Van Eyck ([22:41](https://www.youtube.com/watch?v=6W_-YWHKwZ4&t=1361))

> "AI coding agents cannot become accountability sinks. You need to have ownership over the code you're pushing into production." — Jo Van Eyck ([26:17](https://www.youtube.com/watch?v=6W_-YWHKwZ4&t=1577))

> "Thinking about Andrej Karpathy's quote that it's not the year of agents, it's the decade of agents. I think we will have job security as software engineers. But the job will change. A small-to-big part of the job will be setting up and debugging these agentic workflows." — Jo Van Eyck ([28:21](https://www.youtube.com/watch?v=6W_-YWHKwZ4&t=1701))

## Related Sources

- [004: Bart Slodyczka - Agent Teams](/Users/xlozinguez/Projects/ai-hype-watcher/sources/004-bart-slodyczka-agent-teams.md) — Early exploration of multi-agent coordination patterns
- [005: Nate B Jones - Vibe Coding Readiness](/Users/xlozinguez/Projects/ai-hype-watcher/sources/005-nate-b-jones-vibe-coding-readiness.md) — Preparation mindset for AI-assisted development
- [008: Nate B Jones - Phase Transition](/Users/xlozinguez/Projects/ai-hype-watcher/sources/008-nate-b-jones-phase-transition.md) — Recognizing fundamental shifts in development paradigm
- [010: IndyDevDan - Multi-Agent Orchestration](/Users/xlozinguez/Projects/ai-hype-watcher/sources/010-indydevdan-multi-agent-orchestration.md) — Practical multi-agent coordination patterns
- [011: Confluent Developer - Context Engineering](/Users/xlozinguez/Projects/ai-hype-watcher/sources/011-confluent-developer-context-engineering.md) — Managing context windows effectively
- [012: Nate B Jones - Career Collapse](/Users/xlozinguez/Projects/ai-hype-watcher/sources/012-nate-b-jones-career-collapse.md) — Skills obsolescence and adaptation
- [015: IndyDevDan - Skills Engineering](/Users/xlozinguez/Projects/ai-hype-watcher/sources/015-indydevdan-skills-engineering.md) — Building reusable agent skills

## Related Curriculum

- [Module 03: Claude Code Essentials](/Users/xlozinguez/Projects/ai-hype-watcher/curriculum/03-claude-code-essentials/README.md) — Practical usage of Claude Code's agentic features
- [Module 04: Agentic Patterns](/Users/xlozinguez/Projects/ai-hype-watcher/curriculum/04-agentic-patterns/README.md) — Core patterns like Ralph Wiggum loop, persistent task management
- [Module 05: Team Orchestration](/Users/xlozinguez/Projects/ai-hype-watcher/curriculum/05-team-orchestration/README.md) — Multi-agent coordination and Gas Town-style workflows
