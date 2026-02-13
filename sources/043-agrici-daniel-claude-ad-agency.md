---
source_id: "043"
title: "Claude Code just replaced your ad agency - here's how"
creator: "Agrici Daniel"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=Kf7ejOtl5KU"
date: "2026-02-12"
duration: "12:13"
type: "video"
tags: ["claude-code", "skills", "skills-ecosystem", "prompt-engineering", "context-engineering", "mcp"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns"]
---

# 043: Claude Code just replaced your ad agency - here's how

> **Creator**: Agrici Daniel | **Platform**: YouTube | **Date**: 2026-02-12 | **Duration**: 12:13

## Summary

Agrici Daniel demonstrates "Cloudy Ads," a comprehensive Claude Code skill he built for paid advertising audit and campaign planning. The skill covers Google Ads, Meta, YouTube, LinkedIn, TikTok, and Microsoft Ads with over 190 audit checks, industry-specific templates, and parallel sub-agent delegation. The video is a full walkthrough of using the skill to plan an ad campaign for a real SaaS product (Rankenstein Pro, an AI SEO content engine) on a $1,000/month budget, starting from zero existing ads.

The demo shows the skill's interactive workflow: it asks structured questions (business type, advertising goal, budget range, current ad status), then reads its internal skill files (SaaS-specific markdown, budget allocation guides, conversion tracking references) before crafting a strategy. The skill reasons through platform selection based on budget constraints -- at $1,000/month, it recommends Meta (Facebook/Instagram) only, ruling out LinkedIn (too expensive) and Google Search (conversion-focused, not awareness-focused). The agent then generates a full strategic plan with competitive landscape analysis (it researches actual competitors online), campaign architecture, budget allocation, creative briefs, and expected performance metrics.

The most impressive demonstration is the PDF generation workflow: when asked to convert the strategy into a well-designed PDF with charts, the agent writes a Python script to generate an HTML report with charts, converts it to PDF, self-reviews the output for formatting issues, and fixes them autonomously -- all in roughly three minutes. The resulting PDF includes branded styling, competitive analysis, messaging strategy, and timeline charts.

The skill's knowledge base draws from approximately 2,500 websites on advertising best practices, encoded as markdown files that the agent reads on demand. Daniel emphasizes extensibility -- users can connect MCP servers to Google Analytics, request different platforms, change budgets, or ask for feedback on existing ads. The core message is that the skill pattern can encode domain expertise (in this case, ad agency knowledge) into a reusable, extensible Claude Code capability.

## Key Concepts

### Domain-Expert Skills as Agency Replacements

The video frames Claude Code skills as a way to package entire professional domains -- in this case, paid advertising strategy -- into an installable, reusable capability. The "Cloudy Ads" skill does not just generate ad copy; it performs the full workflow of a junior ad strategist: gathering business context through structured questions, analyzing budget constraints, selecting appropriate platforms, researching competitors, building campaign architecture, and projecting performance metrics. The skill's 190+ audit checks and industry-specific templates represent encoded domain expertise that would traditionally require an agency relationship.

### Structured Interrogation Pattern

The skill uses a multi-round question-and-answer workflow to gather context before generating output. The first round captures high-level parameters (business type, goal, budget, current status). Based on those answers, the agent reads relevant skill files (SaaS-specific strategies, budget allocation frameworks) and then asks a second round of more targeted questions (B2B vs B2C, video production capability, product description). This progressive refinement pattern avoids the common failure mode of generating strategy based on insufficient context.

### Budget-Aware Platform Selection

The agent demonstrates genuine reasoning about platform economics rather than generic recommendations. At $1,000/month for brand awareness: Meta is recommended (lowest CPM for awareness), LinkedIn is explicitly ruled out (too expensive for the budget), Google Search is deprioritized (conversion-focused, not awareness-focused), and YouTube/TikTok are noted as viable only if video content is available. This kind of constraint-based reasoning is what distinguishes a useful skill from a generic prompt.

### Autonomous PDF Report Generation

When asked to produce a PDF, the agent self-orchestrates a multi-step workflow: designing an HTML report with charts, writing a Python script for PDF conversion, generating the output, self-reviewing for formatting issues, and fixing problems without human intervention. This demonstrates the agentic pattern of tool use combined with self-validation -- the agent acts as both builder and reviewer of its own output.

### Skills Knowledge Base at Scale

The Cloudy Ads skill draws from approximately 2,500 websites worth of advertising best practices, encoded as four core markdown documents. This illustrates how skills can serve as a knowledge compression mechanism -- distilling vast amounts of domain knowledge into a format that the agent can load and apply on demand. The markdown format is key: it is both human-readable for maintenance and agent-readable for execution.

## Practical Takeaways

- **Skills can encode entire professional workflows, not just single tasks**: The Cloudy Ads skill covers the full ad planning lifecycle from business analysis through campaign architecture to report generation. Think about what professional workflows in your domain could be similarly encoded.
- **Use progressive questioning to gather context before generating output**: The two-round interrogation pattern (broad questions, then targeted follow-ups after reading relevant skill files) produces better results than a single upfront prompt.
- **Budget and constraint reasoning makes skills practical**: Generic recommendations are useless. Skills that encode platform economics and budget thresholds (e.g., "LinkedIn is too expensive below $X/month") provide genuinely actionable output.
- **Combine skills with MCP servers for live data**: Daniel mentions connecting MCP servers to Google Analytics for real-time campaign data, extending the skill from planning into ongoing optimization.
- **The skill is free and open source**: Available on GitHub for forking and customization. Users can extend it with additional MCP servers, modify the knowledge base, or adapt it for specific industries.

## Notable Quotes

> "Meet Cloudy Ads, a comprehensive paid advertising audit optimization skill for cloud code. It covers Google Ads, Meta, YouTube, LinkedIn, TikTok, and Microsoft ads with over 190 audit checks, industry specific templates, and also parallel sub agent delegation." -- Agrici Daniel ([0:00](https://www.youtube.com/watch?v=Kf7ejOtl5KU&t=0))

> "If you want to connect it through an MCP server straight away to Google Analytics you can also do that. So you can easily just build on top of this cloudy ads skill with ease. So anything you want can be done only if you request it properly." -- Agrici Daniel ([5:00](https://www.youtube.com/watch?v=Kf7ejOtl5KU&t=300))

> "It's over 2,500 websites by the way, give or take, in regards to the best ads practices." -- Agrici Daniel ([11:00](https://www.youtube.com/watch?v=Kf7ejOtl5KU&t=660))

> "This is mostly like what an ad agency is doing and afterwards I can just build on top of that. We have a full plan of action in regards to advertisement, is giving us metrics, is giving us what to do." -- Agrici Daniel ([9:00](https://www.youtube.com/watch?v=Kf7ejOtl5KU&t=540))

## Related Sources

- [013: Stop Using Claude Code Without Skills](013-leon-van-zyl-claude-code-skills.md) -- Van Zyl's skills tutorial covers the foundational skills architecture that Cloudy Ads builds upon; this video is a domain-specific case study of those principles at scale
- [015: I finally CRACKED Claude Agent Skills](015-indydevdan-skills-engineering.md) -- IndyDevDan's engineering breakdown of skill anatomy and composition patterns explains the architectural decisions behind a complex skill like Cloudy Ads
- [017: Be Careful w/ Skills](017-primeagen-skills-security.md) -- ThePrimeagen's security concerns are relevant here: a skill with 190+ checks and 2,500-website knowledge base is powerful but warrants review before installation
- [011: Prompt Engineering is dead.](011-confluent-developer-context-engineering.md) -- The progressive questioning pattern and on-demand knowledge loading in Cloudy Ads are practical applications of context engineering principles

## Related Curriculum

- [Module 03: Claude Code Essentials](../curriculum/03-claude-code-essentials/README.md) -- Skills installation, marketplace discovery, and the skill knowledge base pattern demonstrated by Cloudy Ads
- [Module 04: Agentic Patterns](../curriculum/04-agentic-patterns/README.md) -- The autonomous PDF generation workflow demonstrates builder-validator patterns and multi-step tool orchestration within a skill
