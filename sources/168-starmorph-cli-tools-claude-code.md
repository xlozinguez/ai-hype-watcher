---
source_id: "168"
title: "Terminal Toolkit — 10 CLI Tools for Agent-Centric Development"
creator: "StarMorph AI"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=3NzCBIcIqD0"
date: "2026-02-22"
duration: "9:51"
type: "video"
tags: ["claude-code", "agentic-coding"]
curriculum_modules: ["03-claude-code-essentials"]
---

# 168: Terminal Toolkit — 10 CLI Tools for Agent-Centric Development

> **Creator**: StarMorph AI | **Platform**: YouTube | **Date**: 2026-02-22 | **Duration**: 9:51

## Summary

A practical walkthrough of 10 CLI tools that complement Claude Code for developers spending more time in the terminal. The video targets developers running AI coding agents who need better observability, navigation, and file management in terminal-centric workflows. The tools range from git monitoring (LazyGit) to system performance dashboards (btop, mactop), emphasizing the growing importance of terminal tooling as AI agents shift more development work to the command line.

## Key Concepts

### Git Observability with LazyGit

LazyGit provides a TUI for monitoring git changes in real time as Claude Code modifies the codebase. Developers can watch files change, view diffs, manage branches, and review commit history — all critical when an AI agent is making autonomous changes that need human oversight.

### Terminal-First Development Environment

The collection of tools reflects a broader trend: as AI coding tools like Claude Code operate in the terminal, the terminal itself becomes the primary development environment. Tools like Glow (markdown reader), Ranger (file browser), Eza (enhanced ls), and Zoxide (smart directory navigation) reduce friction in terminal workflows that would traditionally happen in an IDE.

### System Monitoring for Agent Workloads

btop and mactop provide system-level observability for developers running AI agents, particularly on remote Linux VMs. When spinning up Claude Code instances or orchestrating multiple agents, monitoring memory usage, CPU load, and system processes becomes essential for managing costs and performance.

## Practical Takeaways

- **LazyGit**: Monitor git changes in real time as Claude Code works. View diffs, manage branches, and track commit history in a terminal UI.
- **Glow**: Read markdown files (CLAUDE.md, agent outputs) with formatting directly in the terminal without needing a full editor.
- **Zoxide**: Smart directory navigation with fuzzy history. Type `z muse` instead of `cd /full/path/to/pixelmuse` — saves significant time across a full day of terminal work.
- **Eza**: Enhanced `ls` with icons, grid layout, and directory-first grouping. Alias `ls` to Eza for better file visibility, especially when managing multiple terminal windows and VMs.
- **btop/mactop**: System monitoring dashboards for tracking resource usage when running AI agents, especially useful when SSHing into Linux VMs.
- **LMFit**: Check which AI models can run locally on your hardware, ranked by score and memory usage.
- **models**: CLI reference for AI model providers with pricing, context windows, and benchmark data.
- **Ranger**: Terminal file browser for navigating codebases on headless machines without Finder or a GUI.
- **Chafa**: Render images in the terminal — useful for checking AI-generated images or visual assets without leaving the CLI.
- **CSV Lens**: TUI for viewing CSV files in the terminal.

## Notable Quotes

> "When you have 10 terminal screens open and you're on five VMs, it really helps to have things color-coded and organized so you know what you're looking at." — StarMorph AI

## Related Sources

- [165: The Pragmatic Engineer — Mitchell Hashimoto's New Way of Writing Code](165-pragmatic-engineer-hashimoto-ai-coding.md) — Hashimoto built Ghostty terminal precisely because terminal usage is surging due to AI coding tools

## Related Curriculum

- [Module 03: Claude Code Essentials](../curriculum/03-claude-code-essentials/README.md) — CLI companion tools for Claude Code workflows
