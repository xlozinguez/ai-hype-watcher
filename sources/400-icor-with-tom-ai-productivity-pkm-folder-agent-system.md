---
source_id: "400"
title: "Claude just killed ALL Note-Taking Apps. Here is proof."
creator: "ICOR with Tom | AI Productivity"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=geIKyDaXwGg"
date: "2026-03-22"
duration: "55:32"
type: "video"
tags: ["claude-code", "agent-teams", "multi-agent", "prompt-engineering"]
curriculum_modules: ["04-agentic-patterns", "05-team-orchestration", "02-prompting-and-workflows"]
---

# 400: Claude just killed ALL Note-Taking Apps. Here is proof.

> **Creator**: ICOR with Tom | AI Productivity | **Platform**: YouTube | **Date**: 2026-03-22 | **Duration**: 55:32

# Claude just killed ALL Note-Taking Apps. Here is proof.

## Summary

Tom from ICOR argues that traditional PKM (Personal Knowledge Management) tools — Obsidian, Notion, Roam, Tana, Hepabase — are now obsolete because they constrain users within developer-defined scaffolds and plugin ecosystems. His core claim is that a plain folder on your local machine plus Claude (or any frontier AI) provides more flexibility, true ownership, and more powerful knowledge management than any specialized app. The final catalyst was a PKM vendor refusing to open an MCP server, which made him realize the dependency relationship itself was the problem.

The video demonstrates this by building a "Personal Knowledge Assistance" (PK**A**) system from scratch: a single folder with structured subfolders (`owner-inbox`, `team-inbox`, `team`) navigated via terminal and Claude Code. Rather than prompt engineering, Tom uses natural spoken language to instantiate an orchestrator agent ("Larry") who spins up specialized sub-agents ("Pax" the researcher, "Nolan" the HR director) stored as plain Markdown `.md` files in a hidden `.claude/agents/` directory. The whole system is model-agnostic — swap Claude for Gemini or GPT tomorrow and the folder structure and agent definitions remain yours.

A key philosophical point runs throughout: AI empowerment is individual, not organizational. The real productivity gain comes from each person building their own AI team tailored to their expertise, not from a company deploying a shared AI layer over its processes. This frames the PKA system as a professional productivity primitive, not just a personal hobby project.

---

## Key Concepts

### Personal Knowledge Assistance (PKA) vs. PKM
Tom explicitly reframes the category: PKM (Personal Knowledge *Management*) is the old paradigm where humans organize information inside a tool's structure. PKA (Personal Knowledge *Assistance*) is the new paradigm where an AI agent manages the folder/knowledge on your behalf. The distinction matters because PKM tools impose the developer's mental model; a plain folder + AI imposes only your mental model.

### Folder-as-Knowledge-Base with Model-Agnostic Portability
The entire system is a local directory with conventional subfolders (`owner-inbox` for AI outputs to review, `team-inbox` for inputs to give AI, `team` for agent definitions). Because it's just files, it's not locked to any AI provider — the "brain" managing the folder can be swapped. Agent identities, skills, and memory live as plain `.md` files under `.claude/agents/`, the same format Claude Code uses natively. This is structurally identical to Obsidian vaults (also `.md` files) but without any app dependency.

### Orchestrator + Specialist Agent Team Pattern
Rather than one monolithic AI assistant, the system uses a hierarchical multi-agent design: Larry (orchestrator) never does work directly but routes tasks to specialist agents. Pax (senior researcher, with web access, running Opus) and Nolan (HR director, creates new agents) are the bootstrap team. New specialists are hired by Nolan based on research from Pax when a new domain need arises. Each agent is defined by a plain-text file containing name, persona, model preference, and tool permissions.

### Natural Language Over Prompt Engineering
Tom repeatedly emphasizes that formal prompt engineering is no longer necessary with current models. He dictates agent setup instructions conversationally via Claude Code's voice mode (`/voice`), with typos and informal phrasing, and the model interprets intent correctly at Opus-level context (1M token window). The implication is that the barrier to building agentic systems has dropped to the level of verbal instruction.

### Terminal as Simpler Interface than GUI Apps
A recurring argument is that the terminal + Claude Code is *less* intimidating than it appears and ultimately simpler than GUI-based PKM apps. The setup is three steps: find the folder path (`option + right-click → Copy as Pathname` on Mac), `cd` into it, type `claude`. From that point, the AI manages complexity. Tom frames GUI PKM apps as adding friction through interface abstraction, while the terminal exposes direct control.

---

## Practical Takeaways

- **Start with three folders:** `owner-inbox` (AI delivers outputs here for your review), `team-inbox` (you drop inputs/docs here for AI to process), `team` (agent definition files live here). This structure alone gives you a working intake/output loop before any AI configuration.
- **Bootstrap your agent team with just two specialists first:** a researcher (to gather domain knowledge) and an HR/hiring agent (to define and create new specialists). Everything else grows from this root pair on demand.
- **Agent definitions are editable text files** — if an agent's behavior is wrong, open the `.md` file in any text editor and revise the persona, tools, or instructions directly. No settings UI required.
- **Use `/voice` in Claude Code** for setup and high-level instruction — it lowers the friction of describing complex agent configurations and keeps you out of "prompt engineering" mode.
- **Do not share this personal folder with your human team.** The PKA folder is a personal productivity layer; human collaboration happens through linked external resources or separate shared systems. Conflating the two undermines both.

---

## Notable Quotes

> "All I need is a single folder on my computer and Claude."

> "It's not Claude replacing the PKM tools. It's AI doing this because in the end, what I'm building in this folder is mine, created based on my specific needs. And I can simply swap the brain that manages this folder."

> "The real advantage in a business is empowering the employees to build their own AI teams to become more efficient in their field of expertise... It's not about applying AI on top of the business and manage the business. It's about giving each individual member the superpowers they need to accelerate their work."

---
