---
source_id: "332"
title: "Every Level of Claude Code Skills in 27 mins"
creator: "Simon Scrapes"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=-u_igSQHAIo"
date: "2026-03-19"
duration: "27:10"
type: "video"
tags: ["skills", "claude-code", "context-engineering", "skills-ecosystem", "meta-prompts"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns"]
---

# 332: Every Level of Claude Code Skills in 27 mins

> **Creator**: Simon Scrapes | **Platform**: YouTube | **Date**: 2026-03-19 | **Duration**: 27:10

# Every Level of Claude Code Skills in 27 mins

## Summary

This video walks through a progressive skill-building framework for Claude Code, from installing pre-built skills to constructing self-improving, business-aware AI workflows. The creator draws on hundreds of hours of hands-on experience and Anthropic's official skill-building documentation to identify the most common failure modes at each level — primarily that developers conflate "more information" with "better output," leading to bloated context windows and degraded performance.

The core technical insight is that Claude Code skills use **progressive disclosure** across three tiers: YAML front matter (always loaded), the `skill.md` body (loaded on activation), and reference/script/asset files (loaded only when explicitly needed by a step). Keeping `skill.md` under 200 lines is presented not as a style preference but as a hard constraint derived from how LLMs efficiently scan entry-point documents. Violating this constraint is the primary cause of context explosion, instruction drift, and missed skill activations.

The video also covers a practical workflow for importing marketplace skills — which often have excellent business logic but poor structure — and refactoring them using Anthropic's meta skill-creator skill. Beyond structure, the deeper value jump comes from injecting business-specific context (brand voice, product offerings, target audience) so that generic skills produce outputs that are actually usable rather than generic.

---

## Key Concepts

### Progressive Disclosure and the Three-Tier Loading Model

Claude Code skills load information in three tiers to avoid overwhelming the context window. **Tier 1** is the YAML front matter, which is always in context and used solely for skill selection — Claude reads this to decide whether to activate a skill. **Tier 2** is the `skill.md` body, loaded only when the skill activates. **Tier 3** is everything else — reference files, scripts, assets — loaded only when a specific step in `skill.md` explicitly calls for them, then unloaded when that step completes. This means a well-structured skill with extensive reference documentation costs almost no context until the exact moment that documentation is needed.

### The 200-Line Rule for `skill.md`

The 200-line ceiling on `skill.md` is grounded in how much an LLM can efficiently scan in a single pass to determine what to load next. The file should function as a **table of contents**, not an encyclopedia. Anything beyond a step-by-step process outline and pointers to reference files belongs in the `/references` folder. Violating this limit is the root cause of the most common performance issues: slow responses, instruction drift, and Claude ignoring parts of the prompt.

### Skill Activation and YAML Description Engineering

Marketplace skills reportedly activate only ~20% of the time due to poorly written YAML descriptions. A well-formed description requires three components: **(1) trigger keywords** — the specific phrases that should fire the skill; **(2) anti-triggers** — explicit statements of what should *not* activate it; and **(3) output description** — what the skill produces and who consumes it. Without all three, skills either never fire or fire on irrelevant tasks, wasting context on every invocation.

### Refactoring Marketplace Skills with the Meta Skill-Creator Skill

Rather than building from scratch, a practical workflow is to import marketplace skills (which often have valuable domain logic at 400–1,000+ lines) and use Anthropic's skill-creator skill to refactor them. The example in the video reduces a 400-line AI SEO skill to 148 lines (a 60% reduction) by abstracting content into four new reference files. The skill-creator skill handles both structural refactoring and description improvement, making it a force multiplier for onboarding external expertise quickly.

### Context as a Shared, Finite Resource

Skills share the context window with the active conversation. Every line loaded by a skill is a line unavailable for reasoning about the actual task. The framing introduced — "uncontrolled loading of unnecessary information is a direct performance tax on your conversation" — reframes skill design as resource allocation, not just instruction writing. The practical implication is that skill authors must think about context budget the same way a systems engineer thinks about memory allocation.

---

## Practical Takeaways

- **Audit installed skills immediately.** Check every skill's YAML front matter for trigger keywords, anti-triggers, and output description. If any of the three are missing, activation rates will be poor. Re-run through the skill-creator skill to fix them.
- **Treat `skill.md` as a table of contents.** Write process steps as high-level pointers to reference files. If a step requires detailed instructions, that detail goes in `/references/step-name.md`, not inline in `skill.md`.
- **The 15,000-character YAML limit is a hard ceiling.** Tier 1 YAML across all installed skills must fit within ~15,000 characters (~5 pages). Installing too many skills silently degrades performance by bloating the context before any conversation starts.
- **Use the skill-creator skill to refactor, not just create.** When importing a marketplace skill, pass it through the skill-creator skill with an explicit instruction to cap `skill.md` at 200 lines and externalize all reference material. The business logic is often preserved; the structure is repaired.
- **Business context transforms generic skills into production tools.** A skill without brand voice, product specifics, and audience detail produces outputs that require heavy editing. The next level of skill value comes from injecting company-specific context files that all skills can reference.

---

## Notable Quotes

> "The problem isn't lack of information, it's actually having too much irrelevant information."

> "Skills share the context window with your conversation. So uncontrolled loading of unnecessary information is basically a direct performance tax on your conversation."

> "You can think of the skill.md as a table of contents that tells Claude where to look if it needs more information."

---
