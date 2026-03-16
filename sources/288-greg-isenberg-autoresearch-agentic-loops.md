---
source_id: "288"
title: "Karpathy's \"autoresearch\" broke the internet"
creator: "Greg Isenberg"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=qb90PPbAWz4"
date: "2026-03-11"
duration: "24:21"
type: "video"
tags: ["agentic-coding", "multi-agent", "prompt-engineering", "specification", "ai-sdlc", "ai-economics"]
curriculum_modules: ["04-agentic-patterns", "06-strategy-and-economics"]
---

# 288: Karpathy's "autoresearch" broke the internet

> **Creator**: Greg Isenberg | **Platform**: YouTube | **Date**: 2026-03-11 | **Duration**: 24:21

## Summary

Greg Isenberg provides a lay-audience explainer of Andrej Karpathy's "autoresearch" concept — an agentic loop that autonomously runs iterative experiments (code changes, training runs, or research tasks) on a GPU, evaluates results against a defined goal metric, keeps winners, discards losers, and repeats — all without human intervention. The core mental model is framing autoresearch as a "robot research intern" that operates overnight: you define what "better" means, give it access to compute and data, and return to a curated log of results. Karpathy's release and Shopify CEO Toby Lütke's endorsement (noting it works equally well for optimizing any software, not just ML models) drove significant viral attention.

The second half of the video catalogs eight business-opportunity archetypes built on top of autoresearch-style loops: niche optimization agents, autonomous A/B testing services, research-as-a-service, embedded "optimize" features inside existing SaaS, high-volume testing agencies, automated quant strategy generation, always-on CRM lead qualification, and finance-ops automation. Across all cases the value proposition is the same — running orders of magnitude more experiments than a human team could, then surfacing only the winning configurations. The monetization playbook consistently involves monthly retainers, per-report fees, or performance-based revenue sharing.

The video is oriented toward entrepreneurs and builders rather than ML practitioners, so it deliberately avoids deep technical detail. It does flag one real infrastructure constraint: autoresearch requires an NVIDIA GPU (local or cloud), ruling out consumer Apple Silicon machines for the ML-training variant of the loop.

---

## Key Concepts

### The Autoresearch Loop
The canonical loop has five stages: (1) set a measurable goal, (2) an AI agent plans an experiment (code edit, hyperparameter change, or search query), (3) the agent executes it (short training run or web/document search), (4) it reads metrics to evaluate whether the result is an improvement, and (5) it saves winning configurations and discards losers, then plans the next experiment. The loop runs unattended for hours, producing a prioritized log of successful changes. This is an agentic pattern generalized beyond ML — Lütke's framing extends it to any software optimization problem via a `program.md` spec file and a benchmark script.

### Goal Definition as the Critical Input
The quality of autoresearch output is entirely downstream of how precisely the goal is specified. Isenberg's examples span ML model accuracy, conversion rate, CAC/ROAS, lead close rate, and invoice-matching accuracy. The agent has no intrinsic understanding of business value; the human's job is translating a business objective into a measurable signal the loop can optimize against. This mirrors the CLAUDE.md / specification-first pattern seen in agentic coding workflows — a markdown document defining success criteria anchors the autonomous agent.

### Generalization Beyond ML Training
Although Karpathy's initial framing was about improving small AI models, Lütke's reframing — "works even better for optimizing any piece of software" — is the more commercially actionable insight. The same plan→act→evaluate→iterate loop applies to landing page copy, email sequences, trading rules, CRM scoring logic, or invoice-matching prompts. This positions autoresearch as a meta-pattern for autonomous optimization rather than an ML-specific tool.

### Compute Dependency and Access Model
The ML-training variant requires NVIDIA GPU compute; Apple Silicon is not a viable substitute for this workload. Isenberg notes cloud GPU rental as the alternative to local hardware. This is a meaningful barrier-to-entry consideration for the business models proposed — operators either need cloud GPU budgets or must scope their loops to tasks (web search, document reading, prompt iteration) that don't require gradient-based training.

### Autonomous A/B Testing as a Service Primitive
Several of the eight business models are essentially the same primitive applied to different niches: run far more experiments than a human team could, surface winners, charge for the result. This reframes traditional CRO, media buying, and market research services as experiment-throughput businesses where AI is the scaling lever. The competitive pitch — "we run 100x more tests for the same fee" — is a straightforward displacement argument against incumbent agencies.

---

## Practical Takeaways

- **Define your optimization metric before touching any tooling.** The autoresearch loop is only as useful as the success signal you give it — translate business goals (revenue, CAC, lead quality) into a concrete, automatable metric first.
- **The `program.md` + benchmark script pattern is the minimum viable setup.** Per Lütke's framing: create an auto folder, add a markdown file describing the goal and constraints, add a benchmark/eval script, branch, and run. This maps directly to spec-first agentic workflows already documented in the knowledge base.
- **Scope your loop to match your compute access.** If you lack GPU access, restrict autoresearch-style loops to tasks that don't require training (prompt optimization, web research, document synthesis, rule iteration). Reserve GPU-dependent loops for cloud environments with appropriate cost controls.
- **The "optimization agency" model is immediately actionable.** Offering clients a retainer + performance-fee structure where the agent runs continuous experiments is a low-capital business that leverages throughput advantages. Niche specificity (Shopify CRO, B2B SaaS pricing, email sequences) reduces competition and sharpens the benchmark design.
- **Keep a human in the loop for high-stakes domains.** Isenberg explicitly warns against fully autonomous operation in trading and finance contexts. The autoresearch output should be treated as a ranked shortlist for human review, not a direct action queue, especially where errors have financial or legal consequences.

---

## Notable Quotes

> "Think of auto research as a research bot that runs experiments for you while you sleep, tries lots of ideas fast, and keeps the winners."

> "We do 100 times more testing than other shops for the same or lower fee." *(Isenberg's pitch framing for an autoresearch-powered agency)*

> "Auto research works even better for optimizing any piece of software. Make an auto folder. Add a program.md… make a branch and let it rip." *(Toby Lütke, paraphrased)*

---
