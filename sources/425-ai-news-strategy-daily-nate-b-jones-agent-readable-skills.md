---
source_id: "425"
title: "Anthropic, OpenAI, and Microsoft Just Agreed on One File Format. It Changes Everything."
creator: "AI News & Strategy Daily | Nate B Jones"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=0cVuMHaYEHE"
date: "2026-03-30"
duration: "26:19"
type: "video"
tags: ["skills", "agent-teams", "prompt-engineering", "context-engineering", "enterprise-ai", "skills-ecosystem"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns", "06-strategy-and-economics"]
---

# 425: Anthropic, OpenAI, and Microsoft Just Agreed on One File Format. It Changes Everything.

> **Creator**: AI News & Strategy Daily | Nate B Jones | **Platform**: YouTube | **Date**: 2026-03-30 | **Duration**: 26:19

## Summary

This video provides a six-month retrospective on Claude's skills system, arguing that skills have evolved from personal productivity shortcuts into organizational infrastructure and a cross-industry open standard. The creator, Nate B Jones, tracks three major shifts: skills are now deployed enterprise-wide by admins rather than built individually; agents have overtaken humans as the primary callers of skills; and skills have become an open standard backed by Anthropic, Microsoft, and OpenAI, making them a durable substrate for AI workflows rather than a proprietary feature.

The bulk of the video focuses on practical construction guidance for agent-readable skills. Jones walks through the anatomy of a skill file (a folder with a `skill.md` file containing metadata and methodology), the most common failure modes (vague descriptions, brittle step-by-step instructions without reasoning, missing edge cases), and the key design heuristic: invest 80% of effort in the description field that triggers the skill correctly, keep the body lean (under 100–150 lines), and include reasoning frameworks rather than just procedures so the LLM can generalize.

The broader strategic argument is that skills compound while prompts do not. People who have been iterating on skill files for six months are accruing a methodology asset that improves over time and works across Claude, ChatGPT, Copilot, and any LLM-backed tool. The video frames this as a community discovery process — unlike traditional software documentation, best practices for skills are emergent and collectively discovered, making open sharing more valuable than hoarding.

---

## Key Concepts

### Skills as Organizational Infrastructure

Skills have shifted from personal configuration tools to enterprise-grade infrastructure. Team and enterprise admins now roll out skills organization-wide as versioned, single-upload artifacts available across the Microsoft 365 suite (Excel, PowerPoint, Copilot) and Claude. The methodology of a business — previously locked in individuals' heads — can now live in a repository as a skills layer that is both agent-callable and useful for human onboarding.

### Agent-First Skill Design

The dominant caller of skills is now an agent, not a human. Agents can make hundreds of skill calls in a single run; humans might make a few per conversation. This changes failure modes: a human can catch and correct drift mid-conversation, but an agent running autonomously cannot. Skills must be designed to be robust and predictable without human intervention, with clear triggering descriptions, explicit edge cases, and reasoning frameworks that allow the LLM to generalize to unexpected inputs.

### The Description Field as the Critical Lever

Anthropic's own guidance notes that skills tend to under-trigger rather than over-trigger, so description fields should be "pushy" — specific about the document/artifact types produced, inclusive of trigger phrases, and explicit about output format. A critical technical constraint: the description must be a single line. Line breaks caused by code formatters will cause Claude to silently ignore the second line, causing the skill to behave unpredictably.

### Reasoning Over Procedures

A skill body built only from linear step-by-step procedures is brittle — it fails on any input it wasn't explicitly designed for. Effective skills include the *reasoning frameworks and quality criteria* behind the steps, not just the steps themselves. This allows the LLM to generalize. The recommended structure: reasoning/frameworks → specified output format → explicit edge cases → one example for pattern matching — all kept under ~150 lines.

### Skills Compound; Prompts Don't

Prompts are reusable but static. Skills are iteratively refined: practitioners update them based on output quality, add edge cases, and improve descriptions over time. This makes skills a compounding asset. Combined with ecosystem-level investment (the same skill file works across Claude, ChatGPT, and Copilot), the value of maintaining a skill library grows over time in a way that a prompt library does not.

---

## Practical Takeaways

- **Write descriptions for agents, not humans.** Include specific artifact names, explicit trigger phrases, and output format expectations. Make it "pushy" so the LLM confidently invokes it. Never let a code formatter wrap the description across multiple lines.
- **Keep skill files lean.** Target under 100–150 lines in the core `skill.md`. A short, reliably-triggering skill outperforms a long, comprehensive one with competing instructions. Supplementary examples can live in separate files in the same folder.
- **Include reasoning, not just steps.** Document the *why* behind your methodology — quality criteria, decision frameworks, principles. This is what allows the skill to handle edge cases and novel inputs gracefully.
- **Treat your skill library as a compounding asset.** After any output you're unhappy with, update the skill file rather than re-prompting. Six months of iteration produces a qualitatively different artifact than six months of prompt reuse.
- **Design for agent failure modes.** Because agents call skills autonomously and at scale, errors propagate silently. Build in explicit edge case handling and output format constraints that would catch failures a human would have noticed mid-conversation.

---

## Notable Quotes

> "Skills compound for you. Skills compound by the weight of industry investment in the ecosystem and by the weight of your own commitment to having a predictable pattern for doing something and writing it down. Prompts don't compound in the same way."

> "A skill that only has linear procedures is a very, very brittle skill. It's going to break when it hits a case that it doesn't recognize. Reasoning helps Claude generalize in this domain."

> "The best practices are discoverable, not known... With LLMs, we all discover the instruction book together."

---
