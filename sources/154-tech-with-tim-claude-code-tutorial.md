---
source_id: "154"
title: "Claude Code - Full Tutorial for Beginners"
creator: "Tech With Tim"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=ntDIxaeo3Wg"
date: "2026-02-27"
duration: "35:48"
type: "video"
tags: ["claude-code", "vibe-coding"]
curriculum_modules: ["03-claude-code-essentials"]
---

# 154: Claude Code — Full Tutorial for Beginners

> **Creator**: Tech With Tim | **Platform**: YouTube | **Date**: 2026-02-27 | **Duration**: 35:48

## Summary

Tech With Tim delivers a comprehensive beginner-oriented walkthrough of Claude Code, covering everything from installation through advanced features. The tutorial assumes zero prior knowledge and methodically covers setup (subscription options, terminal basics, PowerShell vs. Terminal), installation, Git/GitHub integration, working inside code editors like Cursor, modes (plan/ask/code), keyboard shortcuts, the CLAUDE.md file for persistent memory, background tasks, agents, MCP integrations, and skills.

The tutorial demonstrates building two projects from scratch — a tic-tac-toe game and a top-down shooter — to illustrate the plan-then-execute workflow. Tim emphasizes the importance of knowing what you want before prompting (to avoid runaway agent behavior), using plan mode to structure work, and leveraging Git checkpoints for safety. This is an accessible on-ramp for non-developers and beginners entering AI-assisted coding.

## Key Concepts

### Plan-First Workflow

Tim advocates starting in plan mode, streaming thoughts into Claude (optionally via voice dictation with Whisper Flow), and having Claude create a structured plan before executing. This prevents the agent from going off in unexpected directions and produces better results than open-ended prompting. Claude will even ask clarifying questions before proceeding.

### CLAUDE.md as Persistent Memory

When sessions end, Claude loses all context. The CLAUDE.md file serves as persistent memory across sessions — storing project rules, conventions, and instructions (like "always commit to Git"). Tim demonstrates using `/init` to auto-generate a CLAUDE.md, then customizing it with project-specific directives. This is the key mechanism for maintaining consistency across work sessions.

### Git as Safety Net

Tim emphasizes setting up Git and GitHub before serious work. Claude Code can create repositories, make commits, and push automatically. This provides checkpoints that allow reverting when Claude makes mistakes — essential for beginners who may not catch errors immediately. The tutorial walks through `gh login` and repository creation step by step.

### Modes, Shortcuts, and Background Tasks

The tutorial covers three modes (plan, ask, code) toggled with Shift+Tab, essential shortcuts (Escape x2 to clear, Alt+Enter for newlines, Ctrl+O for verbose logs, Ctrl+B for background), model selection (/model for Opus/Sonnet/Haiku), and background task management. Parallel Claude instances are mentioned as an advanced capability.

## Practical Takeaways

- **Start in plan mode**: Stream your thoughts, let Claude create a plan, review it, then execute — avoid jumping straight into code generation.
- **Set up Git immediately**: Use Claude to install Git, authenticate with GitHub via `gh login`, and create a repository before building anything serious.
- **Create CLAUDE.md early**: Use `/init` to generate the file, then add project-specific rules (like auto-committing) so new sessions inherit context.
- **Use a code editor alongside the terminal**: Open Claude Code inside Cursor/VS Code to see file changes in real time — press Ctrl+backtick to open the integrated terminal.
- **Choose models based on task complexity**: Opus for complex work, Sonnet for moderate tasks, Haiku for quick/cheap answers.

## Notable Quotes

> "The most important part about AI coding is actually knowing what you want. If you don't know what you want and you let the agent steer you, you're going to get horrible crazy results." — Tech With Tim

## Related Sources

- [148: Build Your AI Second Brain with Obsidian + Claude Code](148-noah-vincent-obsidian-claude.md) — Another beginner-friendly Claude Code setup approach

## Related Curriculum

- [Module 03: Claude Code Essentials](../curriculum/03-claude-code-essentials/README.md) — Installation, CLAUDE.md, modes, skills system
