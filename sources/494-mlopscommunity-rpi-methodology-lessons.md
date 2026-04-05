---
source_id: "494"
title: "Everything We Got Wrong About Research-Plan-Implement -  Dexter Horthy"
creator: "MLOps.community"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=YwZR6tc7qYg"
date: "2026-03-24"
duration: "26:46"
type: "video"
tags: ["prompt-engineering", "agentic-coding", "context-engineering", "meta-prompts", "ai-sdlc"]
curriculum_modules: ["02-prompting-and-workflows", "04-agentic-patterns"]
---

# 494: Everything We Got Wrong About Research-Plan-Implement -  Dexter Horthy

> **Creator**: MLOps.community | **Platform**: YouTube | **Date**: 2026-03-24 | **Duration**: 26:46

# Everything We Got Wrong About Research-Plan-Implement

## Summary

Dexter Horthy of MLOps.community delivers a candid retrospective on the Research-Plan-Implement (RPI) methodology for AI-assisted coding, which his team has been developing and refining since mid-2024. The methodology—designed to improve AI developer productivity by structuring agent workflows into discrete research, planning, and implementation phases—reached thousands of engineers at startups and Fortune 500s, but real-world deployment revealed significant gaps between how expert practitioners used it and how teams without deep prompt-engineering backgrounds experienced it. The core problem: the workflow depended on "magic words" and expert intuition to function correctly, and a prompt with 85+ instructions exceeded the reliable instruction-following budget of frontier LLMs (~150–200 instructions per context window).

Two specific failures dominated: (1) poor research quality when models were told what to build upfront, causing them to produce opinions rather than objective facts about the codebase; and (2) planning sessions that skipped the critical interactive question-and-answer steps, jumping straight to writing a plan without aligning with the engineer. The fix for research was architectural—separate context windows for question generation and codebase research, hiding the ticket from the research agent to enforce objectivity. The fix for planning was making the interactive steps structurally mandatory rather than relying on a magic phrase.

The talk also marks a significant position reversal: Horthy now explicitly advocates for reading the code, reversing earlier advice that plans were sufficient. He argues that vibe-coded, unread production code in regulated or user-facing systems is a professional liability, and that the 10x speed narrative is misleading if it produces rework and technical debt. The practical target he recommends is 2–3x improvement with near-human quality, not unchecked velocity.

---

## Key Concepts

### The Instruction Budget Problem
Frontier LLMs reliably follow approximately 150–200 instructions per context window. When a single planning prompt contains 85+ instructions, combined with system prompts, tools, and MCP configuration, total instructions routinely exceed this budget. The result is inconsistent adherence—the model "half-attends" to instructions, making workflow reliability probabilistic rather than deterministic. The fix is to decompose monolithic prompts into smaller, single-purpose context windows with fewer instructions each.

### Separating Research from Intent
A critical failure mode in RPI was giving the research agent knowledge of what was being built. This caused the model to generate opinions and implementation suggestions rather than objective facts about the existing codebase. The solution is query planning with context isolation: one context window generates research questions from the ticket, then a fresh context window—with no knowledge of the planned feature—executes the research. This enforces factual, objective codebase documentation as the research artifact.

### The "Magic Words" Anti-Pattern
Effective use of RPI originally required users to know phrases like "work back and forth with me starting with your open questions and outline before writing the plan" to trigger the interactive planning steps. Without these phrases, the model would skip alignment steps and write a plan immediately. This is a tool design failure: workflows that require expert incantations to function correctly cannot scale to teams. The fix is to make interactive steps structurally enforced rather than prompt-dependent.

### Read the Code (Reversed Position)
The talk explicitly reverses prior advice. Earlier RPI guidance suggested reading the plan was sufficient review; code reading was optional. After six months of not reading code in production systems, Horthy reports having to rip out and replace large parts of systems. The revised position: plans diverge from implementation, so reviewing a plan provides false assurance. Reading the actual code is the same amount of work as reading a long plan but provides ground truth. For production systems with real users, this is non-negotiable.

### Seek Leverage, Not Just Speed
The framing of "10x faster" is challenged directly. If 50% of output is rework cleaning up AI-generated slop from the previous cycle (citing prior research from Eigor), net throughput gains are much smaller than advertised. The goal should be 2–3x improvement with quality maintained at near-human levels. Leverage means doing less work to verify correctness—not skipping verification. Better architecture (isolated context windows, mandatory interactive steps) provides leverage; code review theater on unread plans does not.

---

## Practical Takeaways

- **Decompose monolithic prompts into smaller, single-purpose context windows.** If your planning prompt has 85+ instructions plus system prompts and tools, you're likely exceeding the ~150–200 instruction reliable-following budget of frontier models. Split responsibilities across separate agent steps.

- **Isolate research from implementation intent.** Never tell the research agent what you're building. Generate questions in one context window, then run a fresh context window against the codebase with no knowledge of the planned feature. This produces objective facts rather than pre-colored opinions.

- **Make critical workflow steps structurally mandatory, not prompt-dependent.** If a workflow step can be skipped unless the user says a specific phrase, it will be skipped by most users most of the time. Enforce interactive alignment steps through agent architecture, not through instructions that can be ignored.

- **Read the code, not just the plan.** Plans diverge from implementation. Reviewing a 1,000-line plan and then re-reviewing the code that differs from it is double work with no leverage. Treat the code as the source of truth and invest review effort there.

- **Target 2–3x throughput improvement with quality maintenance, not unchecked 10x velocity.** If your AI-assisted code is generating significant rework cycles, your effective throughput may be much lower than raw output metrics suggest. Measure net throughput including rework.

---

## Notable Quotes

> "If you built a tool that requires hours and hours of training and reps to get good results from, go fix the tool."

> "Going 10 times faster doesn't matter if you're going to throw it all away in 6 months. So shoot for 2 to 3x."

> "Please read the code. We tried not reading the code for like six months. It did not end well. We had to rip out and replace large parts of that system... If you have people who depend on your code, please, I'm begging you, please read it. We have a profession to uphold."

---
