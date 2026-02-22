# AI Hype Watcher

Curated AI-assisted development learning resource — from fundamentals to agentic orchestration. Includes critical perspective on AI industry economics and hype cycles.

## What This Is

A structured collection of notes, analyses, and learning materials synthesized from YouTube videos, articles, and posts about the rapidly evolving AI-assisted development landscape. The emphasis is on **practical patterns for working engineers** alongside **healthy skepticism** about hype cycles and industry economics.

This repository is maintained with the help of Claude Code skills that automate content workflows — from scanning YouTube channels via RSS feeds, to extracting transcripts with Playwright, synthesizing source notes, compiling curriculum sections, and generating daily briefings.

> **136 sources** from **90 creators** · **11 synthesis docs** · **10 briefings** · **6 curriculum modules**

## Browse

```mermaid
graph LR
    S["📚 Sources<br/><i>136 notes</i>"]
    C["🎓 Curriculum<br/><i>6 modules</i>"]
    Y["🔬 Synthesis<br/><i>11 analyses</i>"]
    B["📋 Briefings<br/><i>10 entries</i>"]
    R["🔗 Resources"]
    W["📡 Watchlist"]

    S --> C
    S --> Y
    Y --> B
    W -.->|scan| S

    click S "sources/" "Individual source notes"
    click C "curriculum/" "Learning path"
    click Y "synthesis/" "Cross-source analyses"
    click B "briefings/" "Daily findings"
    click R "resources/" "External links"
    click W "watchlist/" "YouTube channels"
```

| Section | Description |
|---------|-------------|
| [**Sources**](sources/) | Individual video/article notes with structured metadata and key takeaways |
| [**Curriculum**](curriculum/) | Progressive 6-module learning path from foundations to team orchestration |
| [**Synthesis**](synthesis/) | Cross-source analyses that identify patterns across multiple sources |
| [**Briefings**](briefings/) | Dated entries covering recent AI development findings |
| [**Resources**](resources/) | Curated external links organized by skill level |
| [**Watchlist**](watchlist/) | YouTube channels monitored for new AI dev content |

## Curriculum

```mermaid
graph TB
    M1["<b>01 · Foundations</b><br/>AI landscape, capability overhang,<br/>separating progress from hype"]
    M2["<b>02 · Prompting & Workflows</b><br/>Prompt engineering, sticky workflows,<br/>specification-first development"]
    M3["<b>03 · Claude Code Essentials</b><br/>Setup, CLAUDE.md, skills system,<br/>context management"]
    M4["<b>04 · Agentic Patterns</b><br/>Builder/validator, task systems,<br/>meta-prompts, lifecycle hooks"]
    M5["<b>05 · Team Orchestration</b><br/>Agent teams, multi-agent coordination,<br/>observability"]
    M6["<b>06 · Strategy & Economics</b><br/>Infrastructure economics, AI-driven SDLC,<br/>security, adoption strategy"]

    M1 --> M2 --> M3 --> M4 --> M5 --> M6

    click M1 "curriculum/01-foundations/" "Module 01"
    click M2 "curriculum/02-prompting-and-workflows/" "Module 02"
    click M3 "curriculum/03-claude-code-essentials/" "Module 03"
    click M4 "curriculum/04-agentic-patterns/" "Module 04"
    click M5 "curriculum/05-team-orchestration/" "Module 05"
    click M6 "curriculum/06-strategy-and-economics/" "Module 06"
```

## Key Themes

**The tension between acceleration and judgment** — AI coding tools have reached a genuine inflection point, but the creators who are most effective exercise discipline: reusable systems, validated output, focused tasks, and healthy skepticism.

**The capability overhang** — Most knowledge workers still use AI at a 2023 level. The gap between what's available and what's adopted is the real story of early 2026.

**Infrastructure economics are physical** — DRAM, HBM, TSMC nodes, and GPUs are all supply-constrained. Efficiency isn't optional — it's competitive advantage.

**Security matters** — 36% of public agent skills contain security flaws. "Hallucination squatting" is a new class of supply chain attack. Build your own skills; vet everything.

## Top Contributors

Creators with 3+ sources in the collection:

| Creator | Sources | Focus |
|---------|:-------:|-------|
| [Nate B Jones](https://www.youtube.com/@NateBJones) | 16 | Claude Code workflows, agent patterns, skills ecosystem |
| [Matt Pocock](https://www.youtube.com/@maaborern) | 6 | TypeScript + AI tooling, context engineering |
| [IndyDevDan](https://www.youtube.com/@indydevdan) | 4 | Agentic coding patterns, multi-agent orchestration |
| [The PrimeTime](https://www.youtube.com/@ThePrimeTimeagen) | 5 | Industry commentary, engineering culture |
| [Prof G Markets](https://www.youtube.com/@TheProfGPod) | 3 | AI economics, bubble analysis, market dynamics |
| [Leon van Zyl](https://www.youtube.com/@leonvanzyl) | 3 | AI coding tutorials, practical workflows |
| [Pivot to AI](https://www.youtube.com/@PivotToAI) | 3 | AI hype critique, industry skepticism |
| [Simon Scrapes](https://www.youtube.com/@simonscrapes) | 3 | AI automation, practical tooling |

Plus **82 more creators** across the full [source index](sources/).

## Content Pipeline

```mermaid
flowchart LR
    scan["/scan-channels<br/><small>RSS feeds + keywords</small>"]
    transcribe["/youtube-transcriber<br/><small>Playwright extraction</small>"]
    synth["/synthesize-source<br/><small>Structured note</small>"]
    curriculum["/compile-curriculum<br/><small>Module integration</small>"]
    briefing["/daily-briefing<br/><small>Findings entry</small>"]

    scan --> transcribe --> synth --> curriculum
    synth --> briefing

    ingest["/ingest &lt;url&gt;<br/><small>Full pipeline</small>"]
    playlist["/playlist &lt;url&gt;<br/><small>Batch + parallel</small>"]

    ingest -.->|orchestrates| transcribe
    playlist -.->|orchestrates| synth

    style ingest fill:#f9f,stroke:#333
    style playlist fill:#f9f,stroke:#333
```

| Skill | Purpose |
|-------|---------|
| `/ingest <url>` | Full pipeline — transcribe, synthesize, and index in one step |
| `/playlist <url>` | Process entire YouTube playlist with parallel agent teams |
| `/scan-channels` | Scan YouTube watchlist RSS feeds for new relevant content |
| `/discover` | Browse YouTube beyond the watchlist — topic search, trending, scouting |
| `/synthesize-source` | Convert a URL + transcript into a structured source note |
| `/compile-curriculum` | Rebuild curriculum sections from tagged sources |
| `/daily-briefing` | Generate a dated findings briefing |

## Contributing

This is a personal learning resource that's public for anyone who finds it useful. If you spot errors, have suggestions, or want to recommend sources, open an issue.

## License

[MIT](LICENSE)
