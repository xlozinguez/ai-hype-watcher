---
source_id: "194"
title: "Claude Code Skills: Automatic Task-Specific Instructions"
creator: "Claude"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=bjdBVZa66oU"
date: "2026-02-27"
duration: "02:54"
type: "video"
tags: ["claude-code", "skills"]
curriculum_modules: ["03-claude-code-essentials"]
---

# 194: Claude Code Skills: Automatic Task-Specific Instructions

> **Creator**: Claude | **Platform**: YouTube | **Date**: 2026-02-27 | **Duration**: 02:54

## Summary

Anthropic's official explainer on Claude Code skills — markdown files that teach Claude how to perform specific tasks once, then activate automatically when relevant. The video distinguishes skills from other Claude Code customization mechanisms (CLAUDE.md files and slash commands) and explains the two storage scopes: personal skills in `~/.claude/skills` that follow a user across projects, and project skills in `.claude/skills` that ship with a repository.

The key differentiator is that skills are automatic and task-specific. Unlike CLAUDE.md files which load into every conversation, skills load on demand when their description matches the current request — only the name and description enter the context window until activated. Unlike slash commands which require explicit invocation, skills are triggered by Claude recognizing the situation.

## Key Concepts

### Skills as On-Demand Context

Skills solve the context window bloat problem. CLAUDE.md files load into every conversation regardless of relevance, consuming tokens. Skills only load their name and description, activating fully only when the request matches. This means a PR review checklist does not consume context during a debugging session.

### Two Storage Scopes

Personal skills (`~/.claude/skills`) follow the user across all projects — commit message style, documentation format, code explanation preferences. Project skills (`.claude/skills` in repo root) ship with the repository and apply to anyone who clones it — team coding standards, brand guidelines, company conventions.

### Skills vs. CLAUDE.md vs. Slash Commands

CLAUDE.md is for always-on configuration (e.g., "always use TypeScript strict mode"). Skills are for specialized, task-specific knowledge that loads on demand. Slash commands require explicit typing; skills activate automatically when Claude recognizes the relevant situation.

## Practical Takeaways

- **Use skills for repetitive explanations**: If you find yourself re-explaining the same thing to Claude, that is a skill waiting to be written.
- **Put personal preferences in personal skills**: Commit message style, documentation format, and code explanation preferences belong in `~/.claude/skills`.
- **Put team standards in project skills**: Coding standards, brand guidelines, and project conventions belong in `.claude/skills` within the repo.
- **Keep CLAUDE.md for always-on rules**: Only put things in CLAUDE.md that should apply to every single conversation.

## Related Sources

- [040: Automating CLAUDE.md Context](040-charlie-automates-claudemd-context.md) — Context engineering for Claude Code
- [154: Claude Code Power Features](154-diy-smart-code-claude-code-features.md) — Skills, MCP, and advanced Claude Code features
- [192: Applying Software Engineering Rigor to Context Engineering](192-ai-native-dev-context-engineering-rigor.md) — Eval and validation for skills and context

## Related Curriculum

- [Module 03: Claude Code Essentials](../curriculum/03-claude-code-essentials/README.md) — Skills, CLAUDE.md, and context discipline
