---
source_id: "124"
title: "Skills.sh Just Launched. It's Already a Massive Security Risk"
creator: "Kathy Zant"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=-m6ovfQzEqc"
date: "2026-02-11"
duration: "25:41"
type: "video"
tags: ["security", "skills-ecosystem", "ai-safety", "agentic-coding", "claude-code"]
curriculum_modules: ["04-agentic-patterns", "06-strategy-and-economics"]
---

# 124: Skills.sh Just Launched. It's Already a Massive Security Risk

> **Creator**: Kathy Zant | **Platform**: YouTube | **Date**: 2026-02-11 | **Duration**: 25:41

## Summary

Cybersecurity researcher Kathy Zant examines the emerging AI agent skills marketplace ecosystem — specifically Vercel's skills.sh — and argues that the current model poses severe supply-chain security risks. Drawing on her extensive WordPress security background, Zant identifies structural parallels between today's AI skills marketplaces and the plugin ecosystems that made WordPress infamous for vulnerabilities, but notes that the AI version lacks even the basic safeguards that took the WordPress ecosystem years to develop.

The video walks through concrete attack vectors: prompt injection via hidden instructions in image alt text, dynamically fetched GitHub Markdown files with no version pinning that could be swapped out by compromised accounts, and the "find skills" meta-skill (180k+ installs) that essentially gives autonomous agents carte blanche to browse and install unvetted code. Zant references security researcher Zack Korman's demonstrations showing agents happily following sneaky instructions hidden in plain sight, and an article from Trapdoor Security ("Skills are borked and you can't fix it") that systematically catalogs every missing safeguard.

## Key Concepts

### AI Agent Skills Marketplaces ([1:15](https://www.youtube.com/watch?v=-m6ovfQzEqc&t=75))

Skills are reusable instruction packages that extend AI coding agents like Claude Code, Cursor, and Codex. Marketplaces like skills.sh and ClawHub aggregate these skills for discovery and installation. Unlike traditional package managers, these marketplaces lack version immutability, cryptographic signing, vulnerability scanning, sandboxing, and provenance verification — the fundamental protections that mature ecosystems like npm and NuGet spent years building.

### The "Find Skills" Meta-Danger ([3:40](https://www.youtube.com/watch?v=-m6ovfQzEqc&t=220))

One of the most popular skills on skills.sh (180k+ installs) is a "find skills" skill that lets an AI agent autonomously search for and install other skills. This creates a recursive trust problem: you're granting an autonomous agent permission to extend its own capabilities from an unvetted repository, with no human review of what it pulls in.

### Supply-Chain Attack Surface ([5:20](https://www.youtube.com/watch?v=-m6ovfQzEqc&t=320))

Skills often fetch content dynamically from GitHub Markdown files at runtime. There is no version pinning — a skill that works safely today could be replaced tomorrow by the original author or by someone who compromises their account. This mirrors classic supply-chain attacks (like event-stream in npm) but with an even larger blast radius because the agent operates with the developer's full system permissions.

### Prompt Injection via Hidden Instructions ([7:10](https://www.youtube.com/watch?v=-m6ovfQzEqc&t=430))

Security researcher Zack Korman demonstrated that malicious instructions can be hidden in image alt text, HTML comments, and other metadata fields that agents process but humans don't normally read. Because LLMs interpret natural language rather than structured code, traditional static analysis tools cannot detect these attacks. The "most insecure part of any system — the human element" is now being replicated at machine speed.

### The WordPress Plugin Parallel ([12:30](https://www.youtube.com/watch?v=-m6ovfQzEqc&t=750))

Zant draws on her WordPress security expertise to compare the current AI skills ecosystem to the early WordPress plugin era. WordPress plugins eventually developed review processes, automatic security scanning, and update mechanisms — but only after years of devastating exploits. AI skills marketplaces are repeating the same pattern but with higher stakes: agents have filesystem access, can execute code, and operate autonomously.

## Practical Takeaways

- **Never use "find skills" or auto-install skills**: Always manually review any skill before installing it. Copy-paste the instructions rather than importing dynamically fetched packages.
- **Treat skills like untrusted code**: Apply the same scrutiny you would to any third-party dependency — read the source, check the author, and understand what permissions it requires.
- **Pin and audit external references**: If a skill fetches from GitHub or other external sources, fork the content to a repo you control rather than trusting dynamic fetches.
- **Apply least-privilege principles**: Use permission modes that require human approval for filesystem writes, network access, and command execution. Don't run agents in bypass mode with marketplace skills.
- **Watch for hidden instructions**: Be aware that prompt injection can be embedded in image alt text, HTML comments, and metadata fields that are invisible in normal rendering.

## Notable Quotes

> "We are in the new Wild West, and the security risks are terrifying." — Kathy Zant ([0:00](https://www.youtube.com/watch?v=-m6ovfQzEqc&t=0))

> "The 'find skills' skill basically hands your AI the keys to go shopping in an unvetted repo." — Kathy Zant ([3:40](https://www.youtube.com/watch?v=-m6ovfQzEqc&t=220))

> "One popular skill fetches a GitHub Markdown file that could be replaced tomorrow — by you or by a hijacked account." — Kathy Zant ([5:20](https://www.youtube.com/watch?v=-m6ovfQzEqc&t=320))

> "Capabilities are outpacing security." — Kathy Zant ([19:30](https://www.youtube.com/watch?v=-m6ovfQzEqc&t=1170))

## Related Sources

- [017: Skills Security](017-primeagen-skills-security.md) — ThePrimeagen's earlier analysis of skills security risks
- [013: Claude Code Skills](013-leon-van-zyl-claude-code-skills.md) — Leon van Zyl's guide to Claude Code skills usage
- [079: Claude Skills Guide](079-mark-kashef-claude-skills-guide.md) — Mark Kashef's comprehensive skills walkthrough
- [093: OpenClaw Crypto](093-pivot-to-ai-openclaw-crypto.md) — Pivot to AI on the OpenClaw skills ecosystem concerns

## Related Curriculum

- [Module 04: Agentic Patterns](../curriculum/04-agentic-patterns/README.md) — Skills architecture, permission models, and trust boundaries
- [Module 06: Strategy and Economics](../curriculum/06-strategy-and-economics/README.md) — Marketplace dynamics and supply-chain risk in AI ecosystems
