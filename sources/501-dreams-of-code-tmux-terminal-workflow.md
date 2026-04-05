---
source_id: "501"
title: "Tmux has forever changed the way I write code."
creator: "Dreams of Code"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=DzNmUNvnB04"
date: "2023-04-25"
duration: "13:30"
type: "video"
tags: ["agent-teams", "multi-agent", "agentic-coding"]
curriculum_modules: ["05-team-orchestration"]
---

# 501: Tmux has forever changed the way I write code.

> **Creator**: Dreams of Code | **Platform**: YouTube | **Date**: 2023-04-25 | **Duration**: 13:30

## Summary

Dreams of Code walks through how tmux—a terminal multiplexer—fundamentally changed his development workflow by enabling persistent, split-pane terminal sessions that replace the need for graphical IDEs. The video covers tmux's core object model (sessions, windows, panes), essential keybindings, and a complete configuration workflow including the TPM package manager, Vim-style navigation, and the Catppuccin color scheme.

The practical focus is on transforming tmux from its default "ugly green bar" state into a productive, aesthetically coherent environment. Key configuration changes include: installing `vim-tmux-navigator` for seamless neovim/tmux pane switching, enabling 24-bit color, remapping the prefix key to `Ctrl+Space`, enabling mouse support, fixing window indexing to start at 1, and configuring new panes to inherit the current working directory.

While the video is not directly about AI-assisted development, it is highly relevant to practitioners running multi-agent Claude Code workflows. Tmux is the standard infrastructure layer for running parallel AI coding agents in isolated terminal sessions—the same session persistence, split panes, and SSH-attach capabilities described here are exactly what enable multi-agent orchestration patterns in the terminal.

## Key Concepts

### Sessions, Windows, and Panes
Tmux organizes terminal work into a three-tier hierarchy. **Sessions** are the top-level containers (analogous to projects), each holding one or more **windows** (analogous to browser tabs). **Windows** are subdivided into **panes**, each representing an independent terminal process. This structure allows a single tmux session to manage an entire development environment—editor, shell, logs, test runner—within one attached connection.

### Session Persistence and Remote Attach
Tmux sessions survive terminal crashes and disconnections. The `tmux attach` command (or `tmux attach -t <name>`) re-connects to a running session with all panes intact. Combined with SSH, this enables "bed coding"—SSHing into a desktop machine and picking up an existing session exactly where it was left. For AI agent workflows, this means long-running agent processes continue even if the local terminal closes.

### Vim-Tmux Navigator Integration
The `vim-tmux-navigator` plugin (installed in both tmux via TPM and neovim as a plugin) allows `Ctrl+h/j/k/l` to move focus between panes seamlessly, whether the current pane contains a neovim instance or a plain shell. This effectively dissolves the boundary between editor splits and terminal splits, creating a unified tiling workspace.

### TPM (Tmux Plugin Manager)
TPM is the package manager for tmux, installed via git and sourced in `.tmux.conf`. It enables declarative plugin management: add a plugin line to config, press `prefix + I` to install. Plugins covered include `tmux-sensible` (sane defaults), `vim-tmux-navigator`, `catppuccin/tmux` (theming), and `tmux-yank` (clipboard integration).

### Configuration-Driven Workflow Optimization
Several quality-of-life configurations compound into a meaningfully better workflow: changing the prefix from `Ctrl+B` to `Ctrl+Space` (avoids terminal conflicts), setting window/pane indexing to start at 1 (keyboard-layout aligned), enabling mouse support (click-to-focus, scroll history), rebinding pane splits to inherit the current working directory, and remapping copy-mode to Vim-style `v`/`y` selections.

## Practical Takeaways

- **Use tmux as the infrastructure layer for multi-agent workflows**: session persistence, named sessions, and split panes map directly onto the pattern of running parallel AI coding agents—each agent in its own pane or window, all recoverable after reconnection.
- **Change the prefix to `Ctrl+Space`** immediately; `Ctrl+B` conflicts with too many other tools and editors.
- **Start window/pane indexing at 1** (`set -g base-index 1`, `set -g pane-base-index 1`) so keyboard navigation matches the physical number row layout.
- **Bind new pane splits to inherit CWD** so splitting a pane in a project directory opens the new pane in the same directory, avoiding constant `cd` repetition.
- **Install `vim-tmux-navigator` in both tmux and neovim** to create seamless `Ctrl+hjkl` navigation across the entire workspace—critical for keeping hands off the mouse during rapid multi-pane context switching.

## Notable Quotes

> "Tmux is perhaps the one piece of software that's had the biggest impact on the way I write code."

> "If I just want to do my favorite nighttime activity—bed coding—I can pick up my laptop, SSH into my desktop, and attach into my previous tmux session."

> "This helps to make tmux and neovim work as if they were one application."
