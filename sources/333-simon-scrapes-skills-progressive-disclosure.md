---
source_id: "333"
title: "Every Level of Claude Code Skills in 27 mins"
creator: "Simon Scrapes"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=-u_igSQHAIo"
date: "2026-03-19"
duration: "27:10"
type: "video"
tags: ["claude-code", "skills", "context-engineering", "skills-ecosystem", "meta-prompts"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns"]
---

# 333: Every Level of Claude Code Skills in 27 mins

> **Creator**: Simon Scrapes | **Platform**: YouTube | **Date**: 2026-03-19 | **Duration**: 27:10

# Every Level of Claude Code Skills in 27 mins

## Summary

This video walks through a progressive skill-building framework for Claude Code, moving from basic skill installation through advanced multi-skill orchestration. The creator, who has built 20+ production skills running live business operations, argues that most practitioners plateau at early levels because they misunderstand the fundamental architecture of skills—treating them as monolithic instruction documents rather than structured, layered knowledge systems. The core insight is that skills are not about packing in maximum information; they're about progressive disclosure: loading only what Claude needs, exactly when it needs it.

The video's practical spine is the three-tier loading model: (1) YAML front matter always loaded to signal when a skill applies, (2) the skill.md body loaded only on activation, and (3) reference/script/asset files loaded on-demand during specific steps. Breaking this model—by dumping thousands of lines into a single skill.md—causes context bloat, instruction drift, and degraded output quality. The 200-line limit for skill.md files is presented as a hard engineering constraint, not a stylistic preference. Beyond structure, the video covers importing marketplace skills (often high-quality content, poor structure), refactoring them with Anthropic's skill creator meta-skill, and layering in business-specific context to move from generic to genuinely useful outputs.

The higher levels (partially captured in the transcript) focus on connecting skills into coordinated workflows and eventually self-improving systems—the vision of an AI workforce where skills collaborate rather than operate in isolation. The practical example throughout is a real AI SEO skill refactored from 400 lines to 148 lines with four new reference files, achieving a 60% context reduction and demonstrably better focused execution at each step.

## Key Concepts

### Three-Tier Progressive Disclosure
Skills load information in three tiers to avoid context bloat. **Tier 1**: YAML front matter (always in context) — a small description used for skill-selection decisions, capped at ~15,000 characters total across all installed skills. **Tier 2**: The skill.md body (loaded on activation) — a process document capped at 200 lines acting as a table of contents, not an encyclopedia. **Tier 3**: References, scripts, and assets (loaded on-demand per step) — detailed documentation, templates, and executable code that Claude pulls in and discards as specific steps require. This architecture means Claude is never holding irrelevant information, which directly improves accuracy and token efficiency.

### The 200-Line skill.md Rule
The 200-line ceiling on skill.md files is grounded in how LLMs scan documents to decide what to load next. If the entry point is too long, Claude cannot efficiently parse it to make smart loading decisions. The skill.md should function as a table of contents — each step pointing outward to a references file rather than embedding the details inline. Violating this rule creates what the video calls a "performance tax": slowness, instruction drift, and Claude ignoring obvious directives. The example refactor (400 → 148 lines) demonstrates the principle concretely.

### Skill Activation via YAML Trigger Design
A poorly written skill description causes activation rates as low as 20% in marketplace skills (one in five eligible situations). Effective descriptions need three components: (1) explicit trigger keywords/situations ("research what's trending"), (2) explicit exclusions ("does not trigger for general web browsing"), and (3) a clear output statement ("produces a research brief other skills can consume"). This three-part structure gives Claude the signal resolution to correctly decide whether to activate a skill for any given user request.

### Importing and Refactoring Marketplace Skills
Many marketplace skills have excellent domain knowledge but poor structure — walls of text, no references folder, no progressive disclosure. The workflow: install the skill, use Anthropic's **skill creator meta-skill** to refactor it, specifying the 200-line target and directing detail into references files. The skill creator also audits and improves the YAML description for better activation. This allows practitioners to bootstrap specialist domain expertise (AI SEO, Cloudflare configuration, etc.) in an afternoon without building from scratch.

### Business Context Layering
A skill without business-specific context produces generic outputs indistinguishable from a raw LLM prompt. The next level of skill sophistication is injecting brand voice, product offerings, target audience, and existing content strategy into the skill's references layer. This transforms a general "AI SEO audit" skill into one that knows the specific site's positioning and produces outputs that are immediately usable rather than requiring heavy post-processing.

## Practical Takeaways

- **Audit every installed skill's YAML front matter** for the three-part trigger structure (triggers on / does not trigger for / produces). If it lacks all three, activation will be unreliable regardless of the body quality.
- **Keep skill.md under 200 lines** — if yours exceeds this, use the Anthropic skill creator meta-skill to extract detailed sections into a `/references` folder with named files that step instructions point to explicitly.
- **Don't install too many skills simultaneously** — the YAML front matter for all installed skills shares a ~15,000 character budget. Exceeding this bloats the context before any conversation begins.
- **Use marketplace skills as content sources, not production-ready tools** — the business logic is often valuable, but structure refactoring is almost always necessary before deployment in a real workflow.
- **Reference files should be step-specific** — name them to match the step that calls them (e.g., `ai-visibility-audit.md` called only during Step 2), so Claude loads and then discards them rather than holding everything in context throughout the workflow.

## Notable Quotes

> "The problem isn't lack of information, it's actually having too much irrelevant information. Skills share the context window with your conversation. So uncontrolled loading of unnecessary information is basically a direct performance tax on your conversation."

> "Keep your skill.md under 200 lines max. That 200 line limit is not arbitrary. It's effectively based on how much context an LLM can efficiently scan through to decide what to load next."

> "A skill without your business context is basically not worth having at all… An AI SEO skill that knows your brand voice, your product offering — that's a massive jump in value."
