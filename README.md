# AI Hype Watcher

Curated AI-assisted development learning resource — from fundamentals to agentic orchestration. Includes critical perspective on AI industry economics and hype cycles.

## What This Is

A structured collection of notes, analyses, and learning materials synthesized from YouTube videos, articles, and posts about the rapidly evolving AI-assisted development landscape. The emphasis is on **practical patterns for working engineers** alongside **healthy skepticism** about hype cycles and industry economics.

This repository is maintained with the help of six Claude Code skills that automate content workflows — from scanning YouTube channels via RSS feeds, to extracting transcripts with Playwright, synthesizing source notes, compiling curriculum sections, and generating daily briefings.

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

This repo includes six skills for automated content workflows:

| Skill | Purpose | Usage |
|-------|---------|-------|
| `/ingest` | Full pipeline — transcribe, synthesize, and index in one step | `/ingest https://youtube.com/watch?v=...` |
| `/scan-channels` | Scan YouTube watchlist RSS feeds for new relevant content | `/scan-channels` |
| `/youtube-transcriber` | Extract video transcript via Playwright automation | `/youtube-transcriber https://youtube.com/watch?v=...` |
| `/synthesize-source` | Convert a URL + transcript into a structured source note | `/synthesize-source https://youtube.com/watch?v=...` |
| `/compile-curriculum` | Rebuild curriculum sections from tagged sources | `/compile-curriculum all` |
| `/daily-briefing` | Generate a dated findings briefing | `/daily-briefing` |

### Content Pipeline

```
/ingest <url>  — runs the full pipeline automatically:

/scan-channels → /youtube-transcriber → /synthesize-source → /compile-curriculum
    RSS feeds       Playwright extract     synthesize note       integrate into
    + keywords      transcript + metadata  + index               curriculum
```

## Sources Tracked

67 sources analyzed — 64 YouTube videos + 3 articles. See the full [source index](sources/) and [reference table](resources/).

### YouTube Channels

| Creator | Sources |
|---------|---------|
| [Nate B Jones](https://www.youtube.com/@NateBJones) | 9 |
| [IndyDevDan](https://www.youtube.com/@indydevdan) | 4 |
| [Simon Scrapes](https://www.youtube.com/@simonscrapes) | 3 |
| [The PrimeTime / ThePrimeagen](https://www.youtube.com/@ThePrimeTimeagen) | 3 |
| [Bart Slodyczka](https://www.youtube.com/@BartSlodyczka) | 2 |
| [Leon van Zyl](https://www.youtube.com/@leonvanzyl) | 2 |
| [Prof G (Scott Galloway)](https://www.youtube.com/@TheProfGPod) | 3 |
| [Brainqub3](https://www.youtube.com/@brainqub3) | 2 |
| [AI LABS](https://www.youtube.com/@AILABS-393) | 1 |
| [Agrici Daniel](https://www.youtube.com/@AgriciDaniel) | 1 |
| [Ali H. Salem](https://www.youtube.com/@Ali.H.Salem1) | 1 |
| [Awesome](https://www.youtube.com/@awesome-coding) | 1 |
| [Ben AI](https://www.youtube.com/@BenAI92) | 1 |
| [Better Offline](https://www.youtube.com/@BetterOfflinePod) | 1 |
| [Brooke Wright](https://www.youtube.com/@WrightMode) | 1 |
| [ByteByteAI](https://www.youtube.com/@TeamByteByteAI) | 1 |
| [Caleb Writes Code](https://www.youtube.com/@CalebWritesCode) | 1 |
| [Charlie Automates](https://www.youtube.com/@charlieautomates) | 1 |
| [Confluent Developer](https://www.youtube.com/@ConfluentDeveloper) | 1 |
| [DevForge](https://www.youtube.com/@devforgehq) | 1 |
| [Dwarkesh Patel](https://www.youtube.com/@DwarkeshPatel) | 1 |
| [Griffonomics](https://www.youtube.com/@Griffonomics) | 1 |
| [HR.com](https://www.youtube.com/@hrcom) | 1 |
| [IBM Technology](https://www.youtube.com/@IBMTechnology) | 1 |
| [Interface Studies](https://www.youtube.com/@interfacestudies) | 1 |
| [Internet of Bugs](https://www.youtube.com/@InternetOfBugs) | 1 |
| [Java Brains](https://www.youtube.com/@Java.Brains) | 1 |
| [Jeremiah Krakowski](https://www.youtube.com/@jeremykrak) | 1 |
| [Jo Van Eyck](https://www.youtube.com/@JoVanEyck) | 1 |
| [Joshua Morony](https://www.youtube.com/@JoshuaMorony) | 1 |
| [Lenny's Podcast](https://www.youtube.com/@LennysPodcast) | 1 |
| [Modern Software Engineering](https://www.youtube.com/@ModernSoftwareEngineeringYT) | 1 |
| [No Code MBA](https://www.youtube.com/@nocodemba) | 1 |
| [Novara Media](https://www.youtube.com/@NovaraMedia) | 1 |
| [Pivot to AI](https://www.youtube.com/@PivotToAI) | 1 |
| [Playwright](https://www.youtube.com/@Playwrightdev) | 1 |
| [Prompt Engineering](https://www.youtube.com/@engineerprompt) | 1 |
| [Sam Harris](https://www.youtube.com/@samharrisorg) | 1 |
| [Sam Witteveen](https://www.youtube.com/@samwitteveenai) | 1 |
| [The Tech Report](https://www.youtube.com/@TheTechReportTR) | 1 |
| [TheStandupPod](https://www.youtube.com/@TheStandupPod) | 1 |
| [Tim Fairley](https://www.youtube.com/@ConstructIQ) | 1 |
| [Traversy Media](https://www.youtube.com/@TraversyMedia) | 1 |
| [Two Minute Papers](https://www.youtube.com/@TwoMinutePapers) | 1 |
| [xCreate](https://www.youtube.com/@xcreate) | 1 |

### Articles & Blogs

| Creator | Publication |
|---------|-------------|
| Jacob Schmitt | [CircleCI Blog](https://circleci.com/blog/) |
| Matt Shumer | [shumer.dev](https://shumer.dev/) |
| David Gerard | [Pivot to AI](https://pivot-to-ai.com/) |

## Contributing

This is a personal learning resource that's public for anyone who finds it useful. If you spot errors, have suggestions, or want to recommend sources, open an issue.

## License

[MIT](LICENSE)
