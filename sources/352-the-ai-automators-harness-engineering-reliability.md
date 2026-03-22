---
source_id: "352"
title: "Andrej Karpathy's Math Proves Agent Skills Will Fail. Here's What to Build Instead."
creator: "The AI Automators"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=I2K81s0OQto"
date: "2026-03-21"
duration: "19:26"
type: "video"
tags: ["multi-agent", "agent-teams", "context-engineering", "validation", "enterprise-ai", "agentic-coding", "skills"]
curriculum_modules: ["04-agentic-patterns", "05-team-orchestration", "06-strategy-and-economics"]
---

# 352: Andrej Karpathy's Math Proves Agent Skills Will Fail. Here's What to Build Instead.

> **Creator**: The AI Automators | **Platform**: YouTube | **Date**: 2026-03-21 | **Duration**: 19:26

# Andrej Karpathy's Math Proves Agent Skills Will Fail. Here's What to Build Instead.

## Summary

This video argues that agent skills (portable markdown-based prompts encoding domain procedures) are insufficient for production-grade reliability in complex business workflows. Drawing on Karpathy's "march of nines" framing, the creator shows how compounding failure rates across multi-step agentic workflows make prompt-only approaches unworkable at business scale — a 90% per-step success rate across a 10-step workflow produces 6+ failures per day. The SkillsBench evaluation of 84 real-world skills across all major models confirms that while skills improve pass rates, overall success remains well below what enterprises require for unattended operation.

The proposed solution is **harness engineering**: wrapping AI models in deterministic software scaffolding that gates, validates, and orchestrates each stage of a workflow rather than trusting prompts alone. The Stripe "minions" example is cited as a real-world proof point — automatically validating AI-generated code changes against a subset of 3 million tests, enabling 1,300 merged pull requests per week. The creator then demonstrates a contract review harness built in Python that implements phased execution, sub-agents with isolated context windows, RAG-based playbook lookup, programmatic document generation, and mixed model routing (Gemini 2.5 Pro as orchestrator, Gemini 2.5 Flash for sub-agents) to balance cost and accuracy.

The video concludes with 12 design principles for harness engineering, covering architecture patterns (specialized, DAG, hierarchical, autonomous), planning strategies (fixed vs. dynamic plans), virtual file systems for workspace persistence and resilience, task delegation for context isolation, and parallel sub-agent execution. The core thesis is that reliable enterprise AI requires moving domain logic from prompts into deterministic code — using AI for reasoning within tightly controlled programmatic rails.

---

## Key Concepts

### The March of Nines and Compounding Failure
Karpathy's reliability framing shows that each additional "nine" of reliability (90% → 99% → 99.9%) requires comparable engineering effort to the previous one. For multi-step agentic workflows this compounds brutally: a 10-step workflow at 90% per-step reliability yields only a 35% end-to-end success rate. This makes prompt-only approaches fundamentally inadequate for business-critical workflows requiring near-deterministic outcomes.

### Harness Engineering
A harness is the software layer wrapping an AI model that enforces structure, validates outputs, manages state, and orchestrates sub-processes. Unlike general-purpose agents (Claude Code, Manus), specialized harnesses encode a specific workflow's logic in Python (or equivalent), giving developers full control over execution order, validation gates, file I/O, and model selection per stage. This moves reliability guarantees from probabilistic prompting into deterministic code.

### Fixed vs. Dynamic Planning
Harnesses can use either fixed plans (predefined phases that always execute in sequence — appropriate for compliance, legal review, and other standardized SOPs) or dynamic plans (LLM-generated to-do lists that can reorder, add, and remove steps at runtime — appropriate for open-ended research tasks). Choosing the wrong planning mode for a workflow undermines reliability; high-stakes repeatable processes require fixed plans to stay on deterministic rails.

### Sub-Agents with Context Isolation
Delegating clause-level or task-level analysis to dedicated sub-agents prevents context rot in the main orchestrator. Each sub-agent gets a fresh, narrowly scoped context window with only the information it needs. This enables parallel processing at scale (34 clauses analyzed concurrently in the demo), allows cheaper/faster models to handle atomic tasks, and keeps the primary agent's context clean for high-level reasoning and user interaction.

### Programmatic Output Generation
Generating final deliverables (Word documents, reports) through code templates rather than asking an LLM to produce free-form output eliminates format variability and failure modes. The harness calls the template every time with validated structured data, guaranteeing consistent output shape regardless of model behavior — a critical reliability pattern for documents with legal or compliance significance.

---

## Practical Takeaways

- **Don't rely on skills/prompts alone for high-stakes multi-step workflows.** SkillsBench data confirms real-world pass rates fall well short of enterprise requirements; treat skills as a starting point to be codified into deterministic harness logic.
- **Gate every phase.** Structure complex workflows into discrete phases with validation between them, writing intermediate outputs to a file system so the process can be resumed mid-run without restarting from scratch.
- **Use model routing to control cost.** Assign expensive frontier models to orchestration and user-facing reasoning; use faster, cheaper models for narrow, repeated sub-agent tasks. The demo ran 323K total tokens while keeping the main agent at 7K, with flash models handling bulk sub-agent work.
- **Choose your planning mode deliberately.** Use fixed phase plans for standardized SOPs (legal review, compliance audit, onboarding); reserve dynamic planning for open-ended exploratory tasks where the LLM needs to adapt its approach.
- **Instrument everything.** Integrate observability tooling (the demo uses Langfuse) to trace token usage, sub-agent calls, and phase timing — essential for debugging, cost attribution, and demonstrating reliability to enterprise clients.

---

## Notable Quotes

> "There are ways that you can improve the performance of skills through eval and ment, but you will never reach incredibly high levels of reliability through prompting alone."

> "The solution is to harness the power of these AI systems by putting them on deterministic rails."

> "Because it's Python, you have total flexibility on how you want to actually do this… This is the beauty of specialized harnesses."

---
