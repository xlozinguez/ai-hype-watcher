---
source_id: "325"
title: "This can't be real"
creator: "ThePrimeagen"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=cahSKUYjuTE"
date: "2026-03-17"
duration: "8:20"
type: "video"
tags: ["ai-landscape", "ai-hype", "security"]
curriculum_modules: ["01-foundations", "06-strategy-and-economics"]
---

# 325: This can't be real

> **Creator**: ThePrimeagen | **Platform**: YouTube | **Date**: 2026-03-17 | **Duration**: 8:20

## Summary

ThePrimeagen investigates "Malice," a company (or satirical project -- the line is deliberately blurred) that uses AI to independently recreate open-source projects from scratch, producing "legally distinct code with corporate-friendly licensing." The pitch is brazen: no attribution, no copyleft, no problems. Primeagen initially assumes the site is satire, but then actually purchases the service for $0.50, successfully cloning the `is-number` npm package. The AI-generated version passes all 111 original tests despite having entirely different implementation code.

The video raises uncomfortable questions about AI's intersection with open-source licensing. While the Malice website reads like satire ("Those maintainers worked for free. Why should they get credit?"), it functions as a real service that accepts payment and delivers working code. Primeagen's key observation: the first job AI disrupted was not software engineering -- it was legal compliance. Companies can now potentially bypass open-source licensing obligations by having AI regenerate functionally identical code from scratch.

## Key Concepts

### AI as License Laundering

Malice represents a new category of AI application: using models to recreate open-source functionality without inheriting licensing obligations. The generated code is structurally different from the original (different variable names, different logic paths) but functionally identical (passes all tests). This raises questions about whether functional equivalence constitutes a derivative work, and whether AI-generated "clean room" implementations hold up legally.

### The Satire-Reality Collapse

The site markets itself with deliberately provocative copy that reads as satire, yet it accepts money and delivers working results. Primeagen's point is sharp: "When does satire stop? I was able to pay money. I was able to copy a library." The blurring of satire and real product is itself a commentary on how AI is eroding boundaries that previously seemed clear.

### AI-Generated Code Quality Tells

The AI-generated `is-number` implementation exhibits classic AI coding patterns: redundant checks (re-verifying `isFinite` after already checking for number type), verbose implementations of simple logic, and different algorithmic approaches that reach the same result. The code works but is recognizably machine-generated in its style.

## Practical Takeaways

- **Open-source licensing is entering uncharted territory**: AI can produce functionally equivalent code that may not legally constitute a derivative work, potentially undermining copyleft protections.
- **AI disrupted legal compliance before software engineering**: The ability to bypass attribution and licensing requirements is a more immediate disruption than replacing developers.
- **Test suites as specification**: The fact that AI-generated code passes all original tests highlights that test suites effectively function as specifications -- a concept relevant to AI-assisted development where tests guide generation.

## Notable Quotes

> "We thought AI was coming for our jobs. AI went for legal first."

> "When does satire stop? I was able to pay money. I was able to copy a library."

## Related Sources

- [264: IBM - OWASP LLM Attacks](264-ibm-owasp-llm-attacks.md) — security implications of AI systems

## Related Curriculum

- [Module 01: Foundations](../curriculum/01-foundations/README.md) — AI landscape, hype vs. reality
- [Module 06: Strategy and Economics](../curriculum/06-strategy-and-economics/README.md) — legal and security implications
