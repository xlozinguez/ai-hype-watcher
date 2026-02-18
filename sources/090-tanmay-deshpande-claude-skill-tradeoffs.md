---
source_id: "090"
title: "I built Claude Skill for trade off analysis"
creator: "Tanmay Deshpande"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=vPDm2SPT0lM"
date: "2026-02-14"
duration: "5:21"
type: "video"
tags: ["skills", "claude-code", "specification"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns"]
---

# 090: I built Claude Skill for trade off analysis

> **Creator**: Tanmay Deshpande | **Platform**: YouTube | **Date**: 2026-02-14 | **Duration**: 5:21

## Summary

Tanmay Deshpande demonstrates a Claude Code skill he built for automated architecture trade-off analysis. The skill takes a one-paragraph scenario description — such as a fintech startup deciding between extracting a payment microservice, refactoring into a modular monolith, or optimizing the existing monolith — and produces a comprehensive architecture decision record. The output includes weighted scoring across architecture characteristics, Roger Martin's "What Would Have to Be True" strategic framework, second-order effects analysis (Conway's Law implications, discipline tax, technical debt accumulation), risk profiles, and a phased implementation roadmap.

The video is a brief (5-minute) walkthrough showing the skill in action on Opus 4.6, highlighting how a single prompt can replace what traditionally involves hours of whiteboarding where "the most senior person in the room wins and nobody documents why." While the demo is polished, it illustrates a practical pattern for encoding domain expertise into reusable Claude Code skills — turning a complex analytical framework into a repeatable, documented process that produces consistent artifacts.

## Key Concepts

### Architecture Decision Automation via Skills

The skill encodes a multi-step analytical framework into a single Claude Code skill invocation: context capture, option enumeration, weighted scoring against architecture characteristics, tension identification, reversibility assessment, and phased roadmap generation. This transforms what is typically an ad-hoc meeting-driven process into a structured, repeatable artifact. The output serves as a starting point for discussion rather than a final decision, but ensures consistent coverage of factors that are often overlooked in informal decision-making.

### Structured Decision Frameworks in AI Workflows

The skill incorporates established strategy frameworks — Roger Martin's "What Would Have to Be True" for each option, fitness functions for monitoring decisions post-implementation, and second-order effects analysis including Conway's Law implications. This demonstrates how Claude Code skills can encode domain expertise from management and architecture literature into automated workflows, making sophisticated analytical approaches accessible without requiring the user to know the frameworks by name.

### The Documentation Gap in Architecture Decisions

Deshpande's motivation stems from a common organizational failure: architecture decisions are made in meetings dominated by the most senior voice, with no documentation of the reasoning or alternatives considered. The skill addresses this by producing a comprehensive architecture decision record as its primary output, including scoring rationale, caveats to confidence levels, and monitoring strategies — creating an audit trail that traditional whiteboard sessions never produce.

## Practical Takeaways

- **Encode analytical frameworks into skills**: Complex decision-making processes with consistent structure (trade-off analysis, risk assessment, technology selection) are strong candidates for Claude Code skills
- **Use skills to democratize expertise**: A junior architect running this skill gets exposure to frameworks (Roger Martin, fitness functions, Conway's Law) they might not know to apply, leveling the analytical playing field
- **Treat AI-generated architecture decisions as starting points**: The skill's output includes confidence levels and caveats — use it to seed discussion and ensure comprehensive coverage, not to skip the human deliberation
- **Document the "why" automatically**: Skills that produce architecture decision records solve the pervasive problem of undocumented technical decisions

## Notable Quotes

> "Every architecture decision I have seen plays out the same way. Someone proposes microservices, someone else defends the monolith, 3 hours of whiteboarding later, the most senior person in the room wins and nobody documents why." — Tanmay Deshpande

> "You provide a 250 words long context and what you're getting is a detailed architecture trade-off analysis." — Tanmay Deshpande

## Related Sources

- [015: I finally CRACKED Claude Agent Skills](015-indydevdan-skills-engineering.md) — IndyDevDan's foundational skills engineering patterns that this skill builds upon
- [079: Anthropic's Full Claude Skills Guide](079-mark-kashef-claude-skills-guide.md) — Comprehensive guide to the skills system this skill leverages
- [013: Stop Using Claude Code Without Skills](013-leon-van-zyl-claude-code-skills.md) — The case for skills as the primary Claude Code workflow pattern
- [064: One Prompt Every AGENTIC Codebase Should Have](064-indydevdan-agentic-prompt.md) — Prompt engineering patterns relevant to encoding complex workflows

## Related Curriculum

- [Module 03: Claude Code Essentials](../curriculum/03-claude-code-essentials/README.md) — Skills system design and implementation, including how to encode domain expertise into reusable skills
- [Module 04: Agentic Patterns](../curriculum/04-agentic-patterns/README.md) — Structured workflow automation through skills and prompt engineering
