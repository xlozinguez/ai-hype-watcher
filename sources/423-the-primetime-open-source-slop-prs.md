---
source_id: "423"
title: "Worst Advice Ever"
creator: "The PrimeTime"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=DAHZJAoZ3OM"
date: "2026-03-30"
duration: "11:25"
type: "video"
tags: ["agentic-coding", "vibe-coding", "security", "ai-sdlc"]
curriculum_modules: ["02-prompting-and-workflows", "06-strategy-and-economics"]
---

# 423: Worst Advice Ever

> **Creator**: The PrimeTime | **Platform**: YouTube | **Date**: 2026-03-30 | **Duration**: 11:25

# Worst Advice Ever — Satirical Guide to Attracting AI Slop PRs

## Summary

Prime reacts to a satirical post by "Andrew" laying out 10 tongue-in-cheek strategies for maximizing the volume of low-quality, AI-generated pull requests on open-source projects. The joke runs the other way from the real problem (TLDraw closing PRs due to AI spam): Andrew's fictional project has *no* AI PRs and wants them badly, so his "advice" is deliberately structured to expose exactly what makes a repository vulnerable to agentic slop contributions.

The video is a comedic but technically grounded tour of the failure modes that emerge when AI agents are given ambiguous signals, loose permissions, and low-friction contribution pathways. Each "tip" — vague issues labeled "good first issue," removing type annotations and tests, committing `node_modules`, using JavaScript, disabling branch protection — is a real anti-pattern that genuinely degrades repository quality and invites autonomous agent chaos, including self-sustaining chains of bots fixing each other's mistakes.

Beneath the satire is a serious observation about the current state of AI-assisted development: the same properties that make a project welcoming to human contributors (open backlogs, permissive contribution guides, lots of issues) are now double-edged, because AI agents read those same signals and respond with volume over quality. The video implicitly argues that maintainers need to think about repository hygiene and contribution guardrails in an era where agents are perusing GitHub at scale.

---

## Key Concepts

### Ambiguity as Attack Surface
Vague issue titles like "performance could be better" or "improve code quality" with no description are comedy gold in the video, but they reflect a real dynamic: AI agents treat open-ended issues as broad mandates. The less specification in an issue, the larger the surface area an agent will attempt to touch, producing sprawling, hard-to-review PRs that change many files for loosely justified reasons.

### Self-Sustaining Slop Chains
The video describes a scenario where removing types and tests triggers one bot to add them back, whose changes then trigger another bot to fix regressions, producing "chains of seven or eight dependent PRs from different bots, each fixing something the previous one introduced." This is a real emergent failure mode of multi-agent environments with no human-in-the-loop validation gate — agents optimizing locally produce globally incoherent codebases.

### Repository Signals as Agent Prompts
Several tips exploit the fact that AI agents read repository metadata as implicit instructions: a large open backlog signals "help needed," a `CONTRIBUTING.md` that says "we accept contributions from all sources" is effectively an opt-in prompt, and a `.github/copilot-instructions` file (tip nine) can be used to directly instruct visiting agents to fix anything they notice, with or without an open issue. Repository configuration is increasingly a form of prompt engineering.

### Language and Typing as Noise Reduction
The "3.8x more AI PRs in JavaScript vs. Python" joke points at something real: loosely typed, dynamically structured codebases offer more degrees of freedom for agents to propose changes. When there's no type system or test suite to fail, there's no automated check that a change is wrong — which means agents (and the humans merging their PRs) lose a critical feedback signal. Strong types and tests are a form of agent guardrail.

### Contribution Covenant as Inclusion Signal
The final tip — amending the contributor covenant to explicitly welcome AI contributors regardless of "runtime environment or training data" — is absurd, but it highlights an emerging norm question: should open-source projects have explicit policies about AI-generated contributions? The joke works precisely because no such norm yet exists, leaving a vacuum that agents (and the humans running them) are already filling.

---

## Practical Takeaways

- **Write specific, well-scoped issues.** Vague issues labeled "good first issue" are a magnet for low-effort AI PRs; concrete acceptance criteria and scope limits filter for contributors (human or agent) who can actually satisfy them.
- **Keep type annotations and tests intact.** Types and tests are not just correctness tools — they are the primary automated guardrail that rejects low-quality AI contributions before human review is needed.
- **Audit your `.github/copilot-instructions` and `CONTRIBUTING.md`.** These files are now read by agents as behavioral prompts; review them for unintentional open-ended directives that could invite unsolicited changes.
- **Branch protection and PR review requirements are non-negotiable.** Disabling them may feel like friction reduction; in an agentic era it's the equivalent of leaving your `main` branch unlocked to the internet.
- **A large open backlog is now a dual signal.** It communicates project health to humans *and* "work to do" to agents — consider triaging and closing stale issues to reduce the target surface for automated PR spam.

---

## Notable Quotes

> "Some of my colleagues report self-sustaining chains of seven or eight dependent PRs from different bots, each fixing something the previous one had introduced."

> "The data is unambiguous. JavaScript repositories receive 3.8x more AI-authored PRs than the next most targeted language, which is Python."

> "If you just follow these 10 simple steps, you can take your project from a well-maintained project into a slop factory in as few as 3 weeks."

---
