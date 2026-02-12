---
source_id: "026"
title: "10 Claude Code tips I wish I knew from the start"
creator: "No Code MBA"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=BEIulrjHzMI"
date: "2026-02-02"
duration: "11:46"
type: "video"
tags: ["claude-code", "skills", "context-engineering", "agentic-coding"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns"]
---

# 026: 10 Claude Code tips I wish I knew from the start

> **Creator**: No Code MBA | **Platform**: YouTube | **Date**: 2026-02-02 | **Duration**: 11:46

## Summary

No Code MBA delivers a beginner-oriented walkthrough of ten Claude Code features and workflow tips, aimed at developers and non-developers who are starting to build with Claude Code and want to avoid the initial learning curve. The video prioritizes breadth over depth, introducing slash commands, sub-agents, skills, plan mode, CLAUDE.md configuration, and IDE integration as a cohesive starter toolkit.

The most valuable contribution is establishing a clear mental model for how the pieces fit together: slash commands are quick built-in actions, sub-agents are autonomous workers with isolated context windows, skills are reusable instruction sets that operate within your current context, and plan mode is a deliberation step that prevents premature code generation. While none of these features are covered in advanced depth, the video effectively maps the territory for newcomers and emphasizes that Claude Code's documentation is the definitive resource for going deeper. The security review slash command is highlighted as an emerging best practice for 2026 vibe coding workflows.

## Key Concepts

### Slash Commands as the Entry Point ([00:21](https://www.youtube.com/watch?v=BEIulrjHzMI&t=21))

Claude Code's slash commands are the primary discovery mechanism for built-in capabilities. Typing `/` in the terminal reveals the full command palette. The video highlights two particularly useful commands: `/compact`, which clears conversation history while preserving a summary in context (with optional custom summarization instructions to focus on specific topics), and the security review command, which audits pending changes on the current branch. The `/compact` command is positioned as essential for managing long sessions where accumulated context consumes tokens and degrades performance.

### Sub-Agents as Isolated Workers ([01:46](https://www.youtube.com/watch?v=BEIulrjHzMI&t=106))

Sub-agents are specialized workers that Claude can delegate tasks to, each operating with their own context window, custom system prompt, and tool set. The video demonstrates creating a "brand copywriter" agent through Claude's built-in agent creation workflow -- providing a description, selecting tool access level (e.g., read-only), choosing a model tier (Opus, Haiku, Sonnet), and assigning a visual color for terminal differentiation. The key architectural insight is isolation: sub-agents work in their own context space, which means invoking one does not pollute the main conversation's context window. Multiple instances of the same agent can run simultaneously, enabling parallel task execution. The video suggests creating purpose-built agents for different roles (UX/UI, planning, marketing) and even asking Claude to recommend which agents to create.

### Skills vs Sub-Agents: Shared Context vs Isolated Context ([05:11](https://www.youtube.com/watch?v=BEIulrjHzMI&t=311))

The video draws an important distinction that many beginners miss: skills operate within your current context window, while sub-agents operate in their own isolated context. This means skills can be stacked -- multiple skills active in the same conversation, each contributing domain knowledge or workflow instructions to the current task. Skills can be created directly within Claude Code (demonstrated with a YouTube title generator skill), downloaded from the plugin marketplace, or authored externally as markdown files and placed in the Claude skills directory. The composability of skills within a single context window is their primary advantage over sub-agents for tasks that benefit from shared state.

### Plan Mode for Deliberate Development ([07:13](https://www.youtube.com/watch?v=BEIulrjHzMI&t=433))

Plan mode (activated via `Shift+Tab` or `/plan`) prevents Claude from writing code immediately, instead forcing a planning and clarification phase. When enabled, Claude analyzes the request, examines the current directory, asks clarifying questions (workout types, features, tech stack, data storage), and proposes an implementation plan before writing any code. This is particularly valuable for beginners who might otherwise get a fully generated app that doesn't match their intent. The pattern enforces the spec-first development workflow that more advanced practitioners achieve through explicit specification documents.

### CLAUDE.md for Persistent Custom Instructions ([09:25](https://www.youtube.com/watch?v=BEIulrjHzMI&t=565))

The `claude.md` file is a project-level markdown file that Claude automatically loads at the start of every conversation. It serves as persistent custom instructions covering code styles, workflow rules (e.g., "run type check after making code changes"), project conventions, and behavioral constraints. The video notes that claude.md files can be authored manually, generated by Claude itself, or sourced from publicly shared examples on GitHub. This positions claude.md as the foundational context engineering mechanism -- the baseline context that shapes every interaction.

### IDE Integration for Visibility ([08:18](https://www.youtube.com/watch?v=BEIulrjHzMI&t=498))

Running Claude Code inside an IDE terminal (demonstrated with Cursor) rather than a standalone terminal provides immediate visibility into file structure and generated code. While Claude Code operates identically in both environments, the IDE context allows developers to inspect files, review generated code, and navigate the project without switching tools. The video notes that Claude Code and the IDE's own AI agent (e.g., Cursor's agent) can be used in tandem, though the demonstrated workflow uses Claude Code exclusively.

## Practical Takeaways

- **Start with `/compact` in long sessions**: Clear accumulated context while keeping a summary. Add custom instructions to focus the summary on what matters for your current task.

- **Use `/security-review` before merging**: Run the security review slash command on pending branch changes as a lightweight security audit, especially relevant for vibe-coded projects.

- **Create role-specific sub-agents early**: Define agents for recurring specialized tasks (copywriting, UX review, planning) so they are available across sessions without re-prompting.

- **Use skills for composable, stackable capabilities**: When you need multiple specialized behaviors in a single conversation (title generation + script writing), skills are better than sub-agents because they share context.

- **Enable plan mode for unfamiliar projects**: Before building anything new, toggle plan mode to force a requirements-gathering phase that prevents misaligned implementations.

- **Set up a claude.md file immediately**: Even a minimal claude.md with code style preferences and workflow rules improves every subsequent Claude Code session.

- **Run Claude Code inside your IDE**: Use the IDE's terminal for Claude Code rather than a standalone terminal to get file tree visibility and easy code inspection alongside the agent.

## Notable Quotes

> "As your chat window gets really long... that is using a lot of context and tokens as you're chatting. So if you have a really long chat window but you want to clear conversation history but keep a summary in the context, all you have to do is do slash compact." -- No Code MBA ([00:48](https://www.youtube.com/watch?v=BEIulrjHzMI&t=48))

> "Agents are specialized sub-agents that Claude can delegate tasks to. You can think of them almost like employees. They have their own context window, their own custom system prompt, and their own specific tools." -- No Code MBA ([01:54](https://www.youtube.com/watch?v=BEIulrjHzMI&t=114))

> "Sub-agents are working on their own context window, their own custom instructions. Skills are going to work within the context window that you're already in and you can stack them." -- No Code MBA ([06:23](https://www.youtube.com/watch?v=BEIulrjHzMI&t=383))

> "With plan mode on, it is going to plan out the app without actually creating it first... the nice thing about plan mode is it's going to talk to us and it's not going to actually write code until we accept the plan." -- No Code MBA ([07:27](https://www.youtube.com/watch?v=BEIulrjHzMI&t=447))

## Related Sources

- [013: Stop Using Claude Code Without Skills](013-leon-van-zyl-claude-code-skills.md) -- Provides the deep dive on skills that this video introduces at a surface level, including the skills vs MCP servers distinction and custom skill creation
- [024: You are Not Ready: Agentic coding in 2026](024-jo-van-eyck-agentic-coding-2026.md) -- Covers many of the same features (skills, agents, context engineering) at an intermediate-to-advanced level, making it a natural next step after this beginner overview
- [021: Claude's Best Release Yet + 10 Tricks](021-ai-labs-claude-code-tricks.md) -- Another "tips" format video that goes significantly deeper on advanced patterns (hooks, worktrees, adversarial agents), complementing this beginner-oriented list
- [004: Claude Code's New Agent Teams Are Insane](004-bart-slodyczka-agent-teams.md) -- Expands on the sub-agent concept introduced here into full multi-agent team orchestration

## Related Curriculum

- [Module 03: Claude Code Essentials](../curriculum/03-claude-code-essentials/README.md) -- Slash commands, CLAUDE.md configuration, skills system, and plan mode as core Claude Code capabilities
- [Module 04: Agentic Patterns](../curriculum/04-agentic-patterns/README.md) -- Sub-agent delegation and the isolated-context-vs-shared-context distinction between agents and skills
