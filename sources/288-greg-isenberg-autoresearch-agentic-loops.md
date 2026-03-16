---
source_id: "288"
title: "Karpathy's \"autoresearch\" broke the internet"
creator: "Greg Isenberg"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=qb90PPbAWz4"
date: "2026-03-11"
duration: "24:21"
type: "video"
tags: ["agentic-coding", "multi-agent", "ai-economics", "prompt-engineering", "ai-landscape"]
curriculum_modules: ["04-agentic-patterns", "06-strategy-and-economics"]
---

# 288: Karpathy's "autoresearch" broke the internet

> **Creator**: Greg Isenberg | **Platform**: YouTube | **Date**: 2026-03-11 | **Duration**: 24:21

## Summary

Greg Isenberg provides an accessible overview of Andrej Karpathy's "autoresearch" concept — an agentic loop where an AI autonomously plans experiments, edits code, runs short GPU training runs, reads metrics, and iterates toward a user-defined goal. The core mechanic is a closed feedback loop: set a goal, let the agent run experiments while you sleep, and wake up to the best-performing configuration saved automatically. Isenberg notes the system requires NVIDIA GPU hardware (or cloud compute) and positions autoresearch as a practical extension of the broader "agent runs 24/7 while you sleep" workflow pattern.

The bulk of the video is a business idea brainstorm: Isenberg enumerates eight monetizable use cases built on autoresearch-style loops, ranging from niche optimization-as-a-service products to embedded "optimize" buttons inside existing SaaS tools. The framing throughout is entrepreneurial — autoresearch is presented primarily as a mechanism for generating sellable products and services rather than as a research tool for ML practitioners. Shopify CEO Tobi Lütke's public endorsement (suggesting any software folder can become an autoresearch target) is cited as a signal of mainstream applicability.

Isenberg's mental model is intentionally simplified: autoresearch equals "a research boss you can boss around." You give it a goal, grant access to code/GPU/internet, and the loop plans → acts → reads results → updates plan. While technically shallow, the video is valuable for illustrating the breadth of domains where autonomous experiment loops could be applied — marketing, finance ops, CRM, trading, and more — and for demonstrating how non-ML practitioners are already interpreting and commercializing Karpathy's ideas.

---

## Key Concepts

### The Autoresearch Feedback Loop
The core pattern is a closed agentic loop: (1) user sets a goal in natural language, (2) agent plans an experiment, (3) agent edits code/config, (4) short training/test run executes on GPU (~5 min), (5) agent reads metrics, (6) if improved → save config, if not → log and discard, (7) repeat. This is the "RLHF loop for software" generalized to any optimization target — model accuracy, conversion rate, lead quality, etc.

### Goal Specification as the User's Primary Job
The user's only required input is defining what "better" means: lower CAC, higher ROAS, better test score, more conversions. The quality of the goal specification determines the quality of the output. This mirrors broader prompt engineering principles but applied at the experiment-planning level rather than single-inference level.

### Compute Dependency and Access Tiers
Autoresearch requires NVIDIA GPU compute — it cannot run on consumer Apple Silicon. This creates a hardware gatekeeping layer, but cloud GPU options exist. This constraint is practically important for anyone evaluating adoption cost and positions cloud GPU providers as an enabling layer for autoresearch-style products.

### Autonomous Experimentation as a Service Model
The recurring business pattern Isenberg identifies is: wrap an autoresearch loop around a painful niche problem → run experiments automatically → deliver winners to clients → charge monthly retainer + performance bonus. Examples span e-commerce listing optimization, email sequence tuning, SaaS pricing, trading signal generation, and finance ops. The value proposition is volume of experiments (hundreds vs. a few) at the same or lower cost.

### Embed-the-Loop as a SaaS Feature
For existing SaaS builders, Isenberg suggests embedding an autoresearch-style "Optimize" button as a premium feature. Users trigger a mini experiment loop; the system suggests better settings or configurations. This positions autonomous experimentation as a product differentiator and upsell mechanism rather than a standalone product.

---

## Practical Takeaways

- **Define your optimization target precisely before deploying any autoresearch-style loop.** Vague goals produce useless iterations; concrete metrics (conversion rate, model accuracy, CAC) drive useful experiments.
- **The niche-optimization-as-a-service model is the lowest-barrier entry point:** pick a domain you understand, design a tight experiment loop around one painful metric, and charge for the winners — not the process.
- **Cloud GPU access removes the hardware barrier** for individuals without NVIDIA hardware; factoring compute cost into pricing is essential for any autoresearch-based service business.
- **Always keep a human in the loop for high-stakes domains** (trading, finance, compliance). Isenberg explicitly flags that blindly trusting autoresearch output in trading will cause financial losses.
- **Tobi Lütke's framing is operationally useful:** any folder with a program + a benchmark script is a candidate for an autoresearch loop. Think in terms of "what do I already have that has a measurable score?"

---

## Notable Quotes

> "You write a clear task… the bot then runs a loop — it plans, it acts, it reads results, it updates the plan — and then you just come back later… and you see if it's logged everything, charts and metrics, and then it gives you a written summary in normal language."

> "We do 100 times more testing than other shops for the same or lower fee." *(Isenberg's proposed pitch for an autoresearch-powered optimization agency)*

> "Auto research works even better for optimizing any piece of software. Make an auto folder. Add a program MD… a bench script, make a branch and let it rip." *(Tobi Lütke, paraphrased by Isenberg)*

---
