---
source_id: "508"
title: "Attacking AI - Jason Haddix - NDC Security 2026"
creator: "NDC Conferences"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=j51uMah-3js"
date: "2026-03-26"
duration: "55:48"
type: "video"
tags: ["security", "enterprise-ai", "prompt-engineering", "multi-agent"]
curriculum_modules: ["06-strategy-and-economics", "04-agentic-patterns"]
---

# 508: Attacking AI - Jason Haddix - NDC Security 2026

> **Creator**: NDC Conferences | **Platform**: YouTube | **Date**: 2026-03-26 | **Duration**: 55:48

# Attacking AI — Jason Haddix — NDC Security 2026

## Summary

Jason Haddix, a veteran offensive security practitioner with 20+ years of experience, presents a practical methodology for assessing AI-powered systems. The talk emerged from two years of real-world AI pen testing engagements, where enterprise customers began requesting assessments of applications integrating LLMs. Haddix frames AI security not as an entirely new discipline but as an extension of traditional application security — the same injection logic that drove SQL injection now applies to natural language inputs feeding LLMs.

The core methodology covers six phases: identifying inputs, attacking the broader ecosystem (agents, middleware, infrastructure), attacking the front-end model, attacking prompt engineering (system prompt extraction), attacking data stores (RAG databases), and attacking the application layer itself. A critical operational insight is the **non-determinism problem**: unlike traditional vulnerabilities where a payload reliably reproduces, LLM exploits require 5–15 repeated attempts to confirm a true positive — fundamentally changing how findings are documented and verified for customers.

The talk situates AI security within the current "agentic era," where production systems commonly involve multiple chained AI agents with tool-call access to command lines, third-party APIs, databases, and SaaS platforms. This dramatically expands the attack surface beyond the front-end chat interface and makes lateral movement via AI agents a realistic red team objective.

---

## Key Concepts

### LLM Assessment Methodology (Six Phases)
Haddix's structured methodology for holistic AI system testing: (1) **Identify inputs** — all surfaces where text enters the system; (2) **Attack the ecosystem** — agents, orchestrators, middleware, logging/observability tools; (3) **Attack the front-end model** — traditional AI red teaming, safety-bypass attempts; (4) **Attack prompt engineering** — extract or manipulate system prompts which encode business logic; (5) **Attack data** — RAG stores, document pipelines, private data leakage; (6) **Attack the application** — web technologies hosting the model (WebSockets, streaming endpoints). The methodology culminates in pivoting to demonstrate real impact on internal systems reachable via the AI.

### Prompt Injection as the New SQL Injection
Natural language prompt injection is the LLM analogue of SQL injection — injecting adversarial instructions ("ignore all previous instructions") through user-controlled inputs that reach the model's context. The XKCD "Bobby Tables" parallel is used explicitly: just as unsanitized database inputs allowed code execution, unsanitized natural language inputs allow instruction hijacking. In enterprise deployments, this is the primary attack vector because attackers have direct access to natural language interfaces and don't require a lab copy of the model.

### Non-Determinism and the First Try Fallacy
Because LLMs are non-deterministic, the same prompt produces different outputs across invocations. This invalidates the traditional pen tester's assumption that a working payload will reproduce on demand. Haddix recommends running each test case **5–15 times** to distinguish true positives from false positives and to establish reliable reproduction rates. This has downstream consequences for reporting: customers may fail to reproduce a finding on first attempt, requiring explicit guidance about probabilistic exploit behavior.

### Agentic Architecture and Expanded Attack Surface
Modern enterprise AI systems are not single-model deployments. They typically consist of a front-end model, a RAG layer, and 1–7 back-end AI agents equipped with tool calls — code execution, CLI access, third-party API calls, document parsing, and integrations with platforms like Slack or Teams. Each agent and its tools represents an independent attack surface. The surrounding infrastructure (prompt caches, logging systems, observability tools, workflow orchestrators) adds further web-application attack surface that is often open-source and under-hardened.

### RAG Databases as Attack Targets
Retrieval-Augmented Generation (RAG) systems split documents into indexed chunks and retrieve relevant context at query time. From an attacker's perspective, RAG stores may contain sensitive organizational data, and the retrieval mechanism can be manipulated through crafted queries. RAG is now ubiquitous even in simple deployments (equivalent to uploading a document to ChatGPT), making it a near-universal component to probe during assessments.

---

## Practical Takeaways

- **Repeat every prompt injection test 5–15 times** before classifying a result; a single failed attempt does not rule out a vulnerability, and a single success should be reproduced to establish reliability for the customer report.
- **Map the full agent graph before testing** — identify every back-end agent, its tool calls, and the middleware (orchestrators, logging, caches) sitting between the user and each agent. The highest-impact vulnerabilities often live in agents with CLI or API access, not the front-end chat interface.
- **Treat system prompts as business logic worth extracting** — successful system prompt leakage reveals the application's intent, constraints, and often internal infrastructure details that lower the cost of subsequent attacks.
- **Include traditional web application testing against AI infrastructure** — workflow orchestrators, observability platforms, and prompt caching layers are frequently open-source tools with their own CVEs and misconfigurations, independent of LLM-specific vulnerabilities.
- **Use natural language attack strings in real engagements** — character-level fuzzing is useful in lab/research contexts but impractical against hosted frontier models; natural language injection techniques are broadly applicable and effective against enterprise deployments.

---

## Notable Quotes

> "When I find a SQL injection bug or a cross-site scripting bug, usually the syntax, if you use it over again, it works. With AI, I have to test each test case usually somewhere between 5 and 15 times in order to verify a true positive or a false positive result from the attack."

> "The system prompt is the business logic of your application. If I can leak that, I have a leg up as an attacker to understand how your system works and possibly instruct it to do things that are within its bounds, but probably against what you want me to be doing."

> "We are in what we call the agentic era right now, where almost every system that everybody is rushing to deploy now has this kind of architecture — multiple AIs in chorus."

---
