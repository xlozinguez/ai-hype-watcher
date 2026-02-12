# AI Hype Watcher

Curated AI-assisted development learning resource — from fundamentals to agentic orchestration. Includes critical perspective on AI industry economics and hype cycles.

## What This Is

A structured collection of notes, analyses, and learning materials synthesized from YouTube videos, articles, and posts about the rapidly evolving AI-assisted development landscape. The emphasis is on **practical patterns for working engineers** alongside **healthy skepticism** about hype cycles and industry economics.

This repository is maintained with the help of four Claude Code skills that automate content workflows — from scanning YouTube channels for new content, to processing sources, compiling curriculum sections, and generating daily briefings.

## Browse

| Section | Description |
|---------|-------------|
| [**Sources**](sources/) | Individual video/article notes with structured metadata and key takeaways |
| [**Curriculum**](curriculum/) | Progressive 6-module learning path from foundations to team orchestration |
| [**Synthesis**](synthesis/) | Cross-source analyses that identify patterns across multiple sources |
| [**Briefings**](briefings/) | Dated entries covering recent AI development findings |
| [**Resources**](resources/) | Curated external links organized by skill level |
| [**Watchlist**](watchlist/) | YouTube channels monitored for new AI dev content |

## Curriculum Overview

| # | Module | What You'll Learn |
|---|--------|-------------------|
| 01 | [Foundations](curriculum/01-foundations/) | AI landscape, capability overhang, separating progress from hype |
| 02 | [Prompting & Workflows](curriculum/02-prompting-and-workflows/) | Prompt engineering, sticky workflows, specification-first development |
| 03 | [Claude Code Essentials](curriculum/03-claude-code-essentials/) | Setup, CLAUDE.md, skills system, context management |
| 04 | [Agentic Patterns](curriculum/04-agentic-patterns/) | Builder/validator, task systems, meta-prompts, lifecycle hooks |
| 05 | [Team Orchestration](curriculum/05-team-orchestration/) | Agent teams, multi-agent coordination, observability |
| 06 | [Strategy & Economics](curriculum/06-strategy-and-economics/) | Infrastructure economics, AI-driven SDLC, security, adoption strategy |

## Key Themes

**The tension between acceleration and judgment**: AI coding tools have reached a genuine inflection point — but the creators who are most effective are the ones exercising discipline: building reusable systems, validating output, breaking work into focused tasks, and maintaining healthy skepticism.

**The capability overhang**: Most knowledge workers still use AI at a 2023 level. The gap between what's available and what's adopted is the real story of early 2026.

**Infrastructure economics are physical**: DRAM, HBM, TSMC nodes, and GPUs are all supply-constrained. Efficiency isn't optional — it's competitive advantage.

**Security matters**: 36% of public agent skills contain security flaws. "Hallucination squatting" is a new class of supply chain attack. Build your own skills; vet everything.

## Skills (Claude Code)

This repo includes four skills for automated content workflows:

| Skill | Purpose | Usage |
|-------|---------|-------|
| `/scan-channels` | Scan YouTube watchlist for new relevant content | `/scan-channels` |
| `/synthesize-source` | Convert a URL into a structured source note | `/synthesize-source https://youtube.com/watch?v=...` |
| `/compile-curriculum` | Rebuild curriculum sections from tagged sources | `/compile-curriculum all` |
| `/daily-briefing` | Generate a dated findings briefing | `/daily-briefing` |

## Sources Tracked

18 sources analyzed so far — 16 YouTube videos + 1 article + 1 post. See the full [source index](sources/) and [reference table](resources/).

Creators covered: IndyDevDan, Nate B Jones, The PrimeTime, Bart Slodyczka, Ali H. Salem, Internet of Bugs, Leon van Zyl, ThePrimeagen, CircleCI, Matt Shumer.

## Contributing

This is a personal learning resource that's public for anyone who finds it useful. If you spot errors, have suggestions, or want to recommend sources, open an issue.

## License

[MIT](LICENSE)
