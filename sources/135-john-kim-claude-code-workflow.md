---
source_id: "135"
title: "His Claude Code Workflow Is Insane"
creator: "John Kim"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=WpQZlKiy3zo"
date: "2026-02-21"
duration: "22:29"
type: "video"
tags: ["claude-code", "agentic-coding", "context-engineering", "skills-ecosystem", "multi-agent"]
curriculum_modules: ["03-context-engineering", "04-agentic-patterns"]
---

# 135: His Claude Code Workflow Is Insane

> **Creator**: John Kim | **Platform**: YouTube | **Date**: 2026-02-21 | **Duration**: 22:29

## Summary

John Kim walks through the 13-tip workflow that Boris Cherny, the creator of Claude Code, shared via a thread post. Kim demonstrates each tip with live examples from his own projects, adding his own practical commentary about what works and what he has adopted. The video serves as both a documentation of Boris's setup and a hands-on tutorial showing how these patterns look in practice.

The workflow centers on running 5 parallel Claude Code terminal instances plus 5-10 web Claude sessions simultaneously, using Opus with thinking as the default model, and maintaining a shared team CLAUDE.md checked into git that gets updated multiple times per week. Boris's approach is notably "vanilla" — he emphasizes that Claude Code works well out of the box and doesn't over-customize. The most impactful practices include starting most sessions in plan mode before switching to auto-accept, using slash commands for every repeated inner-loop workflow, employing custom sub-agents for post-processing tasks like code simplification, and always giving Claude a way to verify its own work (the "most important tip" per Boris).

## Key Concepts

### Parallel Instance Management ([01:00](https://www.youtube.com/watch?v=WpQZlKiy3zo&t=60))

Boris runs 5 Claude Code instances in parallel across numbered terminal tabs, plus 5-10 web sessions on claude.ai/code. Kim demonstrates the teleport feature for handing off sessions between terminal and web, including syncing to the Claude iOS app for mobile monitoring. The key insight is that with multiple slow Opus sessions running, the bottleneck shifts from model speed to human context-switching ability. Kim compares the workflow to "playing Starcraft" — issuing commands across multiple fronts.

### Shared CLAUDE.md as Compound Engineering ([05:30](https://www.youtube.com/watch?v=WpQZlKiy3zo&t=330))

One CLAUDE.md file for the whole team, checked into git, updated multiple times per week. Anytime Claude does something incorrectly, it gets added to the CLAUDE.md so it won't repeat the mistake. Boris's personal CLAUDE.md is just two lines pointing to the team file. This is the core of compound engineering — the team's accumulated knowledge about how Claude should behave in their codebase, continuously refined through daily use.

### Plan Mode as Context Orchestration ([09:30](https://www.youtube.com/watch?v=WpQZlKiy3zo&t=570))

Most sessions start in plan mode (Shift+Tab twice). Boris goes back and forth with Claude until the plan is satisfactory, then switches to auto-accept edits mode where Claude can usually one-shot the implementation. Kim reveals that even when not actively coding, he uses plan mode extensively for investigating different parts of the codebase — performance optimization, debugging, app initialization. Plan mode is essentially a mechanism for building high-quality context-rich prompts.

### Verification as Quality Multiplier ([18:30](https://www.youtube.com/watch?v=WpQZlKiy3zo&t=1110))

Boris's "most important tip": give Claude a way to verify its work. With a feedback loop, results quality improves 2-3x. The Claude Code Chrome extension allows Claude to open browsers, test UI, take screenshots, and iterate until the implementation works. Kim demonstrates this with an end-to-end integration test where Claude navigates a website, clicks elements, and validates behavior — a form of agentic validation that replaces traditional written E2E tests.

## Practical Takeaways

- **Run multiple Claude instances, not faster single instances**: Using Opus across 5+ parallel sessions is more productive than a faster model in one session, because the bottleneck is model thinking time, not human interaction time.
- **Start with plan mode before implementation**: Going back and forth on a plan before switching to auto-accept produces dramatically better one-shot implementations.
- **Use slash commands for every repeated workflow**: The `/commit-push-pr` example shows how to encode inner-loop patterns that save repeated prompting and reduce back-and-forth with the model.
- **Invest in CLAUDE.md as a living document**: Every mistake Claude makes should be captured in CLAUDE.md so it never recurs. This is the highest-leverage compound engineering practice.
- **Always provide verification mechanisms**: Giving Claude access to browsers, test suites, or other feedback loops creates a 2-3x quality improvement over generate-and-hope workflows.

## Notable Quotes

> "Cloud code works great out of the box. So, I personally don't customize it much. There is no one correct way to use cloud code." — Boris Cherny, quoted by Kim ([01:00](https://www.youtube.com/watch?v=WpQZlKiy3zo&t=60))

> "Plan mode is essentially a way for you to create prompts, like gigantic prompts, really good prompts. Plan mode is where you do the orchestration to bring all the context that you need into that cloud instance so that the agent can execute correctly." — John Kim ([10:30](https://www.youtube.com/watch?v=WpQZlKiy3zo&t=630))

> "Don't manage your Claude Code instance manually. Just have Claude Code do it." — John Kim ([15:30](https://www.youtube.com/watch?v=WpQZlKiy3zo&t=930))

## Related Sources

- [103: Inside Claude Code With Its Creator Boris Cherny](103-y-combinator-boris-cherny-claude-code.md) — Boris Cherny's Y Combinator interview covering Claude Code's design philosophy
- [062: Every Level of Claude Code Explained](062-simon-scrapes-claude-code-levels.md) — Comprehensive Claude Code tutorial covering similar ground
- [015: I Finally Cracked Claude Agent Skills](015-indydevdan-skills-engineering.md) — Deep dive into skills and slash commands
- [067: Agent Teams Course](067-bart-slodyczka-agent-teams-course.md) — Sub-agents and agent teams patterns discussed here
- [064: One Prompt Every Agentic Codebase Should Have](064-indydevdan-agentic-prompt.md) — CLAUDE.md and context engineering for teams

## Related Curriculum

- [Module 03: Context Engineering](../curriculum/03-context-engineering/README.md) — CLAUDE.md as compound engineering, plan mode as context orchestration
- [Module 04: Agentic Patterns](../curriculum/04-agentic-patterns/README.md) — Parallel instance management, verification loops, sub-agents
