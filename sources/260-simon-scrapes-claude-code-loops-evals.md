---
source_id: "260"
title: "Claude Code 2.0 Has Arrived (It’s Insane)"
creator: "Simon Scrapes"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=F4zSxfBe5R0"
date: "2026-03-12"
duration: "15:38"
type: "video"
tags: ["claude-code", "skills", "task-system", "agentic-coding", "mcp"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns"]
---

# 260: Claude Code 2.0 Has Arrived (It’s Insane)

> **Creator**: Simon Scrapes | **Platform**: YouTube | **Date**: 2026-03-12 | **Duration**: 15:38

# Claude Code 2.0 Has Arrived (It's Insane)

## Summary

This video covers four new Claude Code features: the `/loop` command for recurring in-session tasks, scheduled tasks for persistent daily/weekly automation, Google Workspace CLI integration for full Drive/Docs/Sheets access, and Skills 2.0 with built-in evaluation and testing. Together these features shift Claude Code from a reactive, session-bound tool into something closer to a persistent autonomous agent that can monitor, create, and iterate on work without continuous human prompting.

The loop and scheduled task features address a fundamental limitation of prior Claude Code sessions: every action required manual re-prompting. Loops create cron jobs within the current session (expiring after 3 days, dying if the session closes), while scheduled tasks run as fresh instances on a persistent daily or weekly schedule via the desktop app. Google Workspace access arrives via Google's open-source CLI tool rather than a native Claude Code update — this is notable because it produces properly formatted documents through bash commands rather than raw API calls that produce markdown-polluted output.

Skills 2.0 is positioned as the most impactful update for serious users: it adds automated evaluation runs using sub-agents, producing scored HTML reports against user-defined criteria. Rather than iterating blindly on skill quality, users can now test a skill five times in parallel, get pass/fail grades on specific criteria (e.g., "does it use curiosity gaps?"), and identify precisely which parts of a skill or reference file need improvement before moving to the next optimization target.

---

## Key Concepts

### `/loop` — Recurring In-Session Cron Tasks
The `/loop` command schedules a prompt to fire at a recurring interval within the active Claude Code session, using cron jobs under the hood (`cron_create`, `cron_list`, `cron_delete`). Loops expire after 3 days as a safety guard against runaway tasks, and they are destroyed if the terminal session closes — missed runs are not replayed. One-off reminders use the same mechanism but fire once. Best used for short-burst monitoring: watching an inbox during a sprint, tracking file changes across a project, or alerting on conditions during a working session.

### Scheduled Tasks — Persistent Automation
Scheduled tasks are the persistent counterpart to loops: each run starts a fresh Claude Code instance, reads project files, executes the configured skills, and terminates. They are configured in the desktop app (not the terminal or VS Code extension) and survive session closures — if a run is missed it catches up on next open. This is conceptually equivalent to building a workflow in n8n or Zapier, but driven by natural language prompts and Claude's skill library. Practical use case: daily content repurposing that checks YouTube for new videos and generates newsletters and tweets every morning at 9am.

### Google Workspace CLI Integration
Google released an open-source command-line interface (in beta) that gives Claude Code bash-level access to Drive, Gmail, Calendar, Docs, Sheets, and Slides through a single install with over 100 pre-built recipes. Unlike MCP-based or API-based approaches, the CLI generates natively formatted Google Docs with proper headers, links, and images rather than raw markdown. Installation can be guided entirely by Claude Code itself. This is not a native Claude Code feature but is treated as a critical gap-fill for users whose work lives in Google Workspace.

### Skills 2.0 — Automated Evaluation and Scoring
Anthropic updated the skill creator meta-skill to include structured evaluation runs. Users specify 1–3 targeted criteria (e.g., "does it use curiosity gaps?", "does it include founder stories?"), run the skill 5+ times in parallel via sub-agents, and receive a scored HTML report with per-run pass/fail breakdowns, token counts, and timing data. The key discipline is testing one optimization target at a time rather than trying to evaluate everything simultaneously. Results point directly at whether the skill `.md` file or a referenced resource (e.g., a persuasion toolkit) needs updating.

### Skill Iteration Loop with Evals
The recommended workflow is: build skill with clear trigger description, tool list, reference files, and step-by-step process → run targeted evals against specific criteria → identify failing criteria → update the skill `.md` or reference files → re-run evals to confirm improvement → move to next criterion. This replaces gut-feel iteration with a measurable feedback cycle, compressing the number of manual test runs needed to reach a production-quality skill.

---

## Practical Takeaways

- **Use loops for session-scoped monitoring, scheduled tasks for production automation**: loops are ephemeral and expire; scheduled tasks are persistent and catch up on missed runs. Match the tool to the time horizon of the need.
- **Install Google's open-source Workspace CLI rather than trying to wire Google Drive through MCP**: it produces properly formatted documents, requires minimal setup, and Claude Code can guide the installation itself.
- **When running Skills 2.0 evals, constrain to 1–3 criteria per test run**: testing too many dimensions at once makes it impossible to isolate what changed; narrow criteria produce actionable, specific improvement guidance.
- **Reference files (brand voice, ICP, persuasion toolkits) must be explicitly linked inside the skill `.md`**: evals will reveal when a skill isn't actually pulling from its reference files, which is a common failure mode for underperforming skills.
- **The HTML eval report benchmarks token usage and timing per run**: this data is useful not just for quality but for cost and latency optimization as skills mature toward production use.

---

## Notable Quotes

> "Think of loops as 'help me right now on this project' — like watch my inbox for important emails, track changes across a sprint, and anything where you need Claude checking in for the next few hours or days. It's not long-term."

> "Skills 2.0 is designed to fix that with built-in evaluation and testing. You can now automatically test your skills against specific criteria and get scored results back — not just simple did it work or not. You get actual grades on things that matter to you."

> "We're not trying to optimize for like six things at once because there would be way too many moving parts. So what we're doing is picking one to three things. We're testing it, we're then improving it and then moving on to the next one."

---
