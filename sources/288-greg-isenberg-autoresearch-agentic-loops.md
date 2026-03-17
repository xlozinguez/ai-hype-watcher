---
source_id: "288"
title: "Karpathy's \"autoresearch\" broke the internet"
creator: "Greg Isenberg"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=qb90PPbAWz4"
date: "2026-03-11"
duration: "24:21"
type: "video"
tags: ["agentic-coding", "multi-agent", "ai-sdlc", "prompt-engineering", "ai-economics"]
curriculum_modules: ["04-agentic-patterns", "06-strategy-and-economics"]
---

# 288: Karpathy's "autoresearch" broke the internet

> **Creator**: Greg Isenberg | **Platform**: YouTube | **Date**: 2026-03-11 | **Duration**: 24:21

## Summary

Greg Isenberg provides an accessible explainer on Andrej Karpathy's "autoresearch" concept — an agentic loop that runs automated experiments on AI models or business metrics overnight, keeps winners, and discards losers. The core mechanic mirrors the RLHF-style loop applied to practical optimization: define a goal, let an agent plan and execute experiments, measure results, and iterate continuously without human intervention. The viral uptake from both Karpathy and Shopify CEO Toby Lütke signals this is being taken seriously as a general-purpose optimization primitive, not just an ML research tool.

Isenberg reframes autoresearch primarily as a business opportunity rather than a technical curiosity. He argues the pattern — goal → plan → execute → measure → iterate — applies equally to ML model training, A/B testing landing pages, trading strategy backtesting, CRM lead qualification, and financial operations. The key requirement is a GPU (Nvidia hardware or cloud) for ML workloads, plus access to the internet and relevant data sources for research tasks. The "you wake up to winners" framing positions this as async leverage for solo builders and small teams.

The video's practical contribution is mapping the autoresearch loop to eight concrete monetization vectors: niche agent products, conversion optimization agencies, research-as-a-service, SaaS "optimize" features, high-volume testing agencies, quantitative trading, CRM automation, and finance ops. While light on technical depth, it serves as an accessible on-ramp for non-ML practitioners to understand why autonomous experimentation loops represent a structural shift in how optimization work gets done.

## Key Concepts

### The Autoresearch Loop
The core pattern: (1) set a goal in natural language, (2) an agent plans an experiment and edits code or configs, (3) runs a short training or test on a GPU (~5 minutes), (4) reads metrics, (5) saves the config if improved or discards it, then (6) repeats. This is a general-purpose agentic optimization primitive applicable to ML fine-tuning, marketing copy, pricing rules, or any measurable system. The loop runs unsupervised while the operator sleeps.

### Goal Specification as the Key Lever
The human's main contribution is defining what "better" means: lower CAC, higher conversion rate, better model eval score, cheaper invoice processing. The quality of the goal specification directly determines the value of what the loop produces. Poorly specified goals produce local optima or irrelevant results. This is essentially prompt engineering at the objective level — defining the fitness function rather than the individual prompt.

### GPU Requirement and Cloud Accessibility
Autoresearch requires Nvidia GPU hardware for ML training experiments; it cannot run on consumer silicon like Apple M-series chips. However, cloud GPU rentals make this accessible without owned hardware. This is a meaningful barrier for pure business users but a low barrier for technically inclined builders who can provision cloud compute. For non-ML use cases (web research, document summarization), the GPU requirement is relaxed.

### Async Leverage and the "Wake Up to Winners" Model
The economic value proposition is time arbitrage: human attention is replaced by compute time during off-hours. Instead of a human analyst or developer iterating manually, the agent runs hundreds of experiments in parallel or sequence overnight. This compresses experimentation cycles from weeks to hours and shifts the human role from execution to goal-setting and result evaluation — a pattern consistent with broader agentic coding workflows.

### Research-as-a-Service as a Business Primitive
The autoresearch loop (search → read → summarize → compare → repeat) maps directly onto paid research services: competitor intelligence, M&A due diligence, regulatory tracking, market analysis. Continuous loops produce always-fresh reports rather than one-time snapshots. This creates subscription-model opportunities where the deliverable is a living dashboard rather than a static document.

## Practical Takeaways

- **Start with a measurable goal**: Autoresearch only works when "better" is quantifiable. Before building any loop, define the metric the agent will optimize — conversion rate, eval score, processing time. Vague goals produce useless experiments.

- **The niche agent product pattern is immediately actionable**: Pick a domain with clear optimization pain (e.g., Amazon listing CTR, email open rates for realtors), wrap an autoresearch loop around it, and charge a monthly subscription for "we show you the winner." The differentiation is domain-specific goal design, not novel ML.

- **Human-in-the-loop is non-negotiable for high-stakes loops**: Isenberg explicitly flags trading and financial automation as areas where blind trust in autoresearch outputs will cause losses. Any loop operating on real money, real customers, or production systems needs approval gates before deploying winners.

- **Embed autoresearch as a feature, not a product**: For existing SaaS builders, adding an "Optimize" button that triggers a mini autoresearch loop can justify a tier upgrade. The user experience (press button → come back to results) is intuitive and the value is immediately legible.

- **The agency pitch is simple and credible**: "We run 100x more tests than other shops at the same price" is a compelling value proposition when autoresearch handles the execution overhead. Performance-fee pricing (retainer + bonus on KPI lift) aligns incentives and is easy for clients to accept.

## Notable Quotes

> "Think of auto research as a research bot that runs experiments for you while you sleep, tries lots of ideas fast, and keeps the winners."

> "We do a 100 times more testing than other shops for the same or lower fee."

> "You need to have a human in the loop and you need to manage that obviously accordingly."
