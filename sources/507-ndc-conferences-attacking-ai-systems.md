---
source_id: "507"
title: "Attacking AI - Jason Haddix - NDC Security 2026"
creator: "NDC Conferences"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=j51uMah-3js"
date: "2026-03-26"
duration: "55:48"
type: "video"
tags: ["security", "prompt-engineering", "multi-agent", "enterprise-ai"]
curriculum_modules: ["06-strategy-and-economics", "04-agentic-patterns"]
---

# 507: Attacking AI - Jason Haddix - NDC Security 2026

> **Creator**: NDC Conferences | **Platform**: YouTube | **Date**: 2026-03-26 | **Duration**: 55:48

# Attacking AI — Jason Haddix — NDC Security 2026

## Summary

Jason Haddix, a 22-year offensive security veteran, presents a practical methodology for assessing AI-powered systems developed over two years of hands-on LLM penetration testing engagements. The talk bridges traditional application security thinking with the new realities of LLM-backed enterprise systems, covering natural language prompt injection, agentic architectures, and holistic AI ecosystem testing. Haddix draws on CTF competition experience, real client engagements, and original research to build a structured taxonomy for what he calls "attacking AI."

The core insight is that modern AI deployments are not just chatbots — they are complex ecosystems of multiple models, RAG databases, workflow orchestrators, logging infrastructure, and tool-calling agents. Each layer introduces distinct attack surfaces. A complete AI security assessment must address all of these layers, not just the front-end model. This requires rethinking traditional pen testing assumptions, especially around determinism: because LLMs are non-deterministic, each attack must be repeated 5–15 times to distinguish true positives from noise.

Haddix's six-phase methodology — identify inputs, attack the ecosystem, attack the front-end model, attack prompt engineering, attack data stores, and attack the application layer — provides a structured approach for practitioners moving from traditional web app testing into AI assessment work. The talk is pitched as intro-to-intermediate, with the promise of resources for self-directed further learning.

---

## Key Concepts

### Natural Language Prompt Injection
The primary attack vector covered is prompt injection via natural language — injecting instructions into user-facing or data-channel inputs to override or subvert the system prompt's intended behavior. The classic payload "ignore all previous instructions" is used as an entry point, updated via a new XKCD-style framing where a student named "William Ignore All Previous Instructions" causes a generative AI grading system to malfunction. Unlike traditional injection (SQL, XSS), natural language injection exploits the LLM's own instruction-following capability rather than parsing bugs, making it semantically driven and context-dependent.

### The First-Try Fallacy (Non-Determinism in Testing)
Because LLMs are non-deterministic, the same prompt yields different outputs across runs. Haddix coins "the first-try fallacy" to describe the mistaken assumption that a failed or successful attack on one attempt is representative. In practice, each test case must be run 5–15 times to establish reliable signal. This fundamentally changes testing operations: more automated repetition is required, and reproducing findings for client reports becomes a social as well as technical challenge (clients may not reproduce the finding on first attempt).

### Multi-Agent / Agentic Architecture as Attack Surface
Modern enterprise AI deployments rarely consist of a single model. Haddix describes architectures with a front-end model, one or more RAG databases, and multiple back-end agents (potentially 5–7) each with tool-calling capabilities: code execution, CLI access, document parsing, Slack/Teams integration, and external SaaS API calls. Each agent and tool attachment represents an independent attack surface. The agentic era means attackers should prioritize reaching and exploiting back-end agents, not just the conversational front end.

### AI Ecosystem Infrastructure as Attack Surface
Beyond models and agents, enterprise AI deployments include significant supporting infrastructure: AI front ends, prompt caching layers, logging and observability tools, and workflow orchestrators. Many of these are open-source components. These auxiliary web applications sit in the traffic path between users and models and can be attacked using traditional web application techniques, expanding the total attack surface well beyond the LLM itself.

### Six-Phase LLM Assessment Methodology
Haddix's structured methodology covers: (1) **Identify inputs** — all text ingestion points; (2) **Attack the ecosystem** — agents, orchestrators, and auxiliary apps; (3) **Attack the front-end model** — traditional AI red teaming for safety bypasses; (4) **Attack prompt engineering** — leak or subvert system prompts across all models in the chain; (5) **Attack data stores** — RAG databases for sensitive data exposure; (6) **Attack the application** — web technologies (WebSockets, streaming) that surface the model to users. A final step is pivoting via AI system compromise to attack internal systems, demonstrating real-world impact.

---

## Practical Takeaways

- **Run attacks 5–15 times before concluding pass/fail.** Non-determinism means single-attempt results are unreliable. Automate repetition (Haddix used JavaScript bookmarklets and a personal database of attack strings in CTF contexts) and report findings with appropriate caveats about probabilistic reproduction.
- **Map the full AI architecture before testing.** Identify every model, RAG database, agent, tool attachment, and infrastructure component. The most impactful vulnerabilities often live in back-end agents with tool access (code execution, external APIs), not the front-end chat interface.
- **System prompt leakage is high-value reconnaissance.** Extracting the system prompt reveals the application's business logic and may expose constraints that can be exploited or bypassed. Test for this across every model in a multi-agent chain.
- **Treat AI infrastructure components as standard web targets.** Logging systems, orchestrators, and prompt caches are often open-source web applications with their own CVEs and misconfigurations. Holistic AI assessment includes conventional web app testing of these components.
- **Natural language is the primary attack medium for real-world engagements.** Character-level fuzzing is more relevant in lab settings. In production assessments against frontier models (Claude via AWS, GPT-4 via Azure), natural language prompt injection is the most effective and accessible attack surface.

---

## Notable Quotes

> "With AI, actually, when I test, I have to test each test case usually somewhere between 5 and 15 times in order to verify a true positive or a false positive result from the attack."

> "In a holistic test you don't want to just test the first model or even just the agents, you want to holistically test the whole system."

> "We are in what we call the agentic era right now, where almost every system that everybody is rushing to deploy now has this kind of architecture — multiple AIs in chorus."

---
