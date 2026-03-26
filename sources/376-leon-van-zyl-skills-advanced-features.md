---
source_id: "376"
title: "Claude Code Skills Changed Everything (And Nobody Noticed)"
creator: "Leon van Zyl"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=epZy_NajGnA"
date: "2026-03-24"
duration: "20:38"
type: "video"
tags: ["skills", "claude-code", "context-engineering", "agentic-coding", "multi-agent", "skills-ecosystem"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns"]
---

# 376: Claude Code Skills Changed Everything (And Nobody Noticed)

> **Creator**: Leon van Zyl | **Platform**: YouTube | **Date**: 2026-03-24 | **Duration**: 20:38

# Claude Code Skills Changed Everything (And Nobody Noticed)

## Summary

Leon van Zyl walks through significant new capabilities added to Claude Code's agent skills system, arguing that most developers are still using skills in outdated ways. The video covers installation pathways (both Claude Code's native plugin command and the cross-tool `skills.sh` marketplace), the skill creator skill that automates skill authoring with built-in testing and blind A/B evaluation, and the distinction Anthropic draws between two skill types: *capability uplift* (adding or improving abilities the base model lacks) and *encoded preferences* (defining specific multi-step workflows the agent should follow).

The more technically substantial half of the video focuses on two advanced features. First, context forking via `context: fork` in a skill's front matter, which runs the skill in its own isolated session so its reference documents and processing don't pollute the main agent's context window. Second, dynamic context injection — a pre-processing step that executes a script to populate placeholders in the skill file with live project data before the agent ever reads the prompt, saving tokens and avoiding hallucinated lookups. The video also demonstrates running skills via background sub-agents to keep the main agent free during long-running tasks.

A practical through-line is the convergence of skills and custom commands: as of the time of filming, creating a skill is strictly superior to creating a custom command, since skills can be invoked the same way but carry richer metadata, instructions, and the new runtime features.

---

## Key Concepts

### Capability Uplift vs. Encoded Preferences
Anthropic categorizes skills into two types. *Capability uplift* adds or sharpens abilities the base model can't perform well natively — examples include generating images via an external API during web design work, or enforcing a specific frontend design style to avoid generic "AI sloppy" outputs. *Encoded preferences* define a required sequence of actions for workflows the agent could technically perform in arbitrary order — for instance, a pull-request review workflow that must retrieve docs, analyze diffs, and output structured risk assessments in a fixed sequence.

### Context Forking (`context: fork`)
Adding `context: fork` to a skill's front matter causes the skill to execute in its own isolated session with its own context window. Only the final summary or result is passed back to the main agent. This is critical for skills that pull in large reference document trees (e.g., a Next.js/React best practices skill that loads dozens of rule files), which would otherwise consume and muddy the primary context window. The trade-off: execution is synchronous, so the main agent waits rather than continuing other work.

### Dynamic Context Injection
A pre-processing mechanism that runs a script to populate placeholder values in the skill file before the agent reads it. Rather than asking the agent to spend tokens exploring the filesystem to discover project metadata (name, dependencies, git history, etc.), the script fetches that data at invocation time and injects it directly into the skill's context. This reduces latency, saves tokens, and makes skill behavior more deterministic.

### Background Sub-Agents for Long-Running Skills
Skills that take a long time (e.g., a PR review skill that may run for 20 minutes) can be wrapped in a sub-agent configured with `background: true`. This causes the sub-agent to run asynchronously in the background, freeing the main agent thread for other tasks. The operator can switch to the background agent's thread to monitor its progress at any time.

### Skills as the Successor to Custom Commands
The video makes explicit that skills and custom commands have merged in the current Claude Code architecture. Skills support all the invocation patterns of custom commands (e.g., `/skill-name` slash syntax) while adding front matter metadata, richer instructions, and the new runtime features (forking, injection, testing). Creating standalone custom commands is now considered redundant.

---

## Practical Takeaways

- **Use `context: fork` for any skill that loads large reference documents** — this prevents skill-specific docs from polluting the main conversation context and is a simple one-line addition to the skill's front matter.
- **Use the skill creator skill to bootstrap new skills**, not just for convenience but because it also runs tests and blind A/B evaluations — making it possible to validate whether a skill actually improves on the base model's native behavior, especially as new model versions are released.
- **Re-evaluate existing skills when new models ship** — a skill built to paper over a model limitation may become redundant (or actively harmful) after a capability jump like a new Opus release; the built-in evaluation tooling is specifically designed for this use case.
- **Wrap long-running skills in background sub-agents** rather than blocking the main agent thread; configure with `background: true` and delegate via a plain-language instruction.
- **Install cross-tool skills via `skills.sh`** if your team uses multiple agentic coding tools (Cursor, Open Code, Codex, etc.) — the installer symlinks into both `.claude/skills` and `.agents/skills`, making skills available universally.

---

## Notable Quotes

> "Skills and custom commands have actually merged. And at this point, there's really no point in creating custom commands anymore. Just create a skill and you can call it like a custom command."

> "As these models get progressively better, chances are that something that could be a limitation now... you can constantly evaluate your skills against these new models to see if they're actually still relevant or maybe your skill is performing worse than the native capabilities of the agents."

> "Without the fork context, all the processing is happening in this main thread... But if we add context fork, the readme gen skill is running within its own thread. The main agent is simply waiting for the result."

---
