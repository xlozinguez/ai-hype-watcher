---
source_id: "505"
title: "Beyond Instructions: How Beads Lets AI Agents Build Like Engineers"
creator: "AI Tinkerers"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=s96O9oWI_tI"
date: "2025-12-12"
duration: "47:49"
type: "video"
tags: ["agentic-coding", "vibe-coding", "validation", "mcp", "task-system", "prompt-engineering", "context-engineering"]
curriculum_modules: ["02-prompting-and-workflows", "04-agentic-patterns"]
---

# 505: Beyond Instructions: How Beads Lets AI Agents Build Like Engineers

> **Creator**: AI Tinkerers | **Platform**: YouTube | **Date**: 2025-12-12 | **Duration**: 47:49

# Beyond Instructions: How Beads Lets AI Agents Build Like Engineers

## Summary

Steve Yaggi, head of engineering at SourceGraph (makers of the AMP coding environment), discusses his open-source project Beads—a framework that gives coding agents persistent task management and memory to enable longer autonomous run times and more ambitious projects. Only four weeks old at the time of recording, Beads already has hundreds of contributors and works across major coding agents including Claude Code, Codex, and AMP. The conversation demonstrates what mature agentic workflows actually look like in practice: Yaggi runs multiple long-running agents simultaneously, including one porting a 30-year-old multiplayer game to a React client—a project he drives entirely through high-level direction rather than code-level intervention.

The discussion is notably candid about the difficulty of vibe coding, pushing back against the popular narrative that AI-assisted development is easy. Yaggi co-authored a book called *Vibe Coding* and emphasizes that supervising agents requires just as much cognitive effort as traditional coding—you're "wrestling with a bear all day long." The conversation covers specific productivity techniques including multimodal prompting with automated screenshots for visual validation, the "tracer bullet" approach to getting unstuck, and a scripted end-of-session cleanup workflow called "landing the plane."

Yaggi also gives a follow-up to his 2024 essay "The Death of the Junior Developer," arguing that developers at all levels must now understand AI workflows, build visible portfolios demonstrating those skills, and adapt to the new role of engineer-as-supervisor rather than engineer-as-coder. His setup illustrates the emerging pattern: a senior developer operating at the level of project manager and quality director, using tools like Playwright MCP for automated visual verification rather than reading diffs line by line.

## Key Concepts

### Beads: Task Management and Memory for Coding Agents
Beads is an open-source framework that addresses one of the core limitations of current coding agents: they lack persistent state and structured task management across sessions. By giving agents a to-do list system and memory, Beads enables much longer autonomous run times and allows agents to pick up where they left off. This is positioned as the missing layer that separates toy agentic demos from production-grade engineering workflows. It works as a wrapper across existing agents rather than replacing them.

### Multimodal Validation via Automated Screenshots
Rather than reviewing diffs, Yaggi uses a reference screenshot (taken from a working platform/client) as the ground truth for the agent's output. A Playwright MCP server remotely controls a browser, takes live screenshots, and feeds them back into the agent's context so it can self-evaluate visual progress. When the agent claims a task is complete, the workflow forces it to compare the actual rendered output against the reference—catching the common failure mode where agents declare success prematurely. This is a concrete implementation of the builder/validator pattern applied to UI work.

### The Tracer Bullet Technique
When an agent gets stuck cycling through many sessions without forward progress, the tracer bullet technique redirects effort toward finding the thinnest possible end-to-end path that actually works. Instead of trying to solve the whole problem, you identify the minimal slice—a single working protocol connection, a single rendering path—and hang everything else on that scaffold. For Yaggi's game client, this meant skipping all graphics and first establishing a working Telnet protocol connection, which unblocked the broader port.

### "Landing the Plane" — Scripted Session Cleanup
At the end of every working session, Yaggi runs a scripted cleanup command that handles commit syncing, cleans up old git branches, and surfaces the best candidate task for the next session. This structured handoff prevents the session entropy that accumulates over long agentic runs (stale branches, uncommitted work, unclear next steps) and makes it easier to resume work or hand off to another agent instance. It treats the end-of-session as a first-class workflow step rather than an afterthought.

### The Engineer as Supervisor
The emerging role Yaggi describes is not coding—it's directing, validating, and unblocking. He operates at the level of "what does the screenshot look like" and "prove it to me," not "what does line 47 do." He uses the car ergonomics metaphor for choosing between agents (they all do roughly the same thing, but the feel matters when you're in them all day). His workflow with a 30-year-old, half-million-line codebase illustrates that the primary skill is now workflow design and quality supervision, not language or framework fluency—he's building a React/TypeScript client without knowing either.

## Practical Takeaways

- **Use screenshots as ground truth for UI agents**: Establish a reference screenshot of the target state and require agents to automatically compare their output against it using Playwright or a similar MCP tool before declaring success. This breaks the "I'm done" hallucination pattern.

- **Apply tracer bullets when stuck**: If you've run 10+ sessions without forward progress, stop trying to fix the original problem and instead find the thinnest end-to-end slice that can work—even if it's trivially simple. Get that working, then build outward from it.

- **Script your session endings ("land the plane")**: Create a reusable cleanup command that commits work, resolves branch hygiene, and identifies the best next task. Running this consistently prevents compounding session entropy and makes agent handoffs cleaner.

- **Assume ~85% correctness as a baseline**: Anything an agent produces should be treated as a first draft requiring review. If you see it generating large volumes of code quickly, schedule an explicit code review step—don't assume the volume means quality.

- **Detach from diffs, attach to outcomes**: Reading every diff is a crutch that doesn't scale to agentic workflows. Instead, define verifiable outcome criteria (screenshot match, test pass, protocol response) and validate against those. The shape of the code output matters more than the line-by-line content.

## Notable Quotes

> "Man, it's just as hard as regular coding. You have to—you're wrestling with a bear all day long."

> "Everything that it does, just assume it's 85% correct. I mean statistically, empirically, it feels about like that or less—60%. They really half-ass it."

> "I made it catch itself by introducing a workflow where I say, 'Look, our screenshot has to match this reference screenshot.' ... Because unfortunately it's been really brittle and it breaks itself all the time—it's like, 'We're done, we're done.' And it's like the map's not even rendering anymore."
