---
source_id: "261"
title: "Claude Code + Karpathy's Autoresearch = The New Meta"
creator: "Nick Saraev"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=4Cb_l2LJAW8"
date: "2026-03-12"
duration: "24:42"
type: "video"
tags: ["claude-code", "agentic-coding", "multi-agent", "meta-prompts", "prompt-engineering"]
curriculum_modules: ["04-agentic-patterns", "05-team-orchestration"]
---

# 261: Claude Code + Karpathy's Autoresearch = The New Meta

> **Creator**: Nick Saraev | **Platform**: YouTube | **Date**: 2026-03-12 | **Duration**: 24:42

# Claude Code + Karpathy's Auto Research = Autonomous Experimentation Pipeline

## Summary

Nick Saraev demonstrates how to adapt Andrej Karpathy's open-source `autoresearch` project — originally designed to autonomously run ML training experiments overnight — into a general-purpose self-improving agent loop for business optimization. The core insight is that Karpathy's pattern (hypothesis → experiment → measure → keep/discard → repeat) is domain-agnostic: any workflow with an objective metric and an API for triggering changes can be automated into a tight feedback loop using Claude Code as the orchestrator.

Saraev's primary working example is cold email copy optimization: an `orchestrator.py` runs every 4 hours, generates challenger variants against a baseline, queries the Instantly API for reply rates, logs learnings to a `resources.md` file, and uses that accumulated knowledge to inform the next generation of copy. The agent improves autonomously with zero human involvement, and the knowledge base compounds over time — the longer it runs, the more it knows about what works.

The broader framework applies to any sales/marketing surface: landing page CRO, ad creatives, chatbot scripts, product descriptions, YouTube titles, newsletter subject lines, and pricing pages. The three requirements are: (1) a cloneable version of the autoresearch repo, (2) a `test.md` file defining goal, metric, and test method, and (3) a scheduler (e.g., GitHub Actions, Modal) to run the loop on a defined cadence.

## Key Concepts

### The Auto Research Loop

Karpathy's pattern is a structured experiment loop: start with a hypothesis → implement a change → run for a fixed period → measure against an objective metric → keep or discard → log learnings → repeat. In ML, this means adjusting hyperparameters and measuring validation loss. In business applications, it means adjusting copy, UI, or configuration and measuring conversion/reply/satisfaction metrics. The loop's power scales with how tightly it can be run — shorter feedback cycles produce faster convergence.

### Objective Metric + API = Automatable Experiment

The minimum viable requirement for applying this pattern is two things: an objective metric you want to improve (reply rate, CVR, CSAT, revenue) and an API that lets the agent (a) make changes and (b) read results. If a native API isn't available, tools like Chrome DevTools MCP can substitute for direct UI manipulation. This framing reduces the problem of "what can I automate?" to a simple checklist, making the pattern broadly applicable across business domains.

### Baseline vs. Challenger (A/B Structure)

Each experiment cycle maintains a baseline (current best) and generates a challenger (modified variant). The agent runs both in parallel, harvests comparative metrics, selects the winner as the new baseline, and discards the loser. This is a programmatic A/B testing loop — but unlike traditional A/B testing, the agent generates the challengers autonomously based on a growing knowledge base of what has worked in prior rounds, rather than requiring human hypothesis generation.

### Compounding Knowledge Base (`resources.md`)

A critical architectural element is the persistent `resources.md` (or equivalent) log where the agent records learnings from each experiment cycle. This file becomes richer over time and is fed back into future prompt context, so each generation of experiments is informed by all prior results. The longer the system runs, the more domain-specific optimization knowledge it accumulates — creating a compounding advantage that would be impractical to build manually.

### Autonomous Scheduling via GitHub Actions / Modal

The loop is made fully autonomous by deploying the orchestrator to a cloud scheduler (GitHub Actions, Modal, etc.) on a fixed cadence. This removes the human from the loop entirely: the agent wakes up, runs experiments, logs results, and schedules itself to run again. Saraev notes the asymmetry explicitly — a human optimizer might run a few experiments per day; an automated loop can run 24+ per day with no fatigue, no distraction, and no context-switching cost.

## Practical Takeaways

- **Clone autoresearch as a template, not a constraint.** Karpathy's repo and its `program.md` prompt are a starting point. Karpathy himself acknowledges the prompt is rough — adapt the architecture to your domain and write a stronger orchestrator prompt tailored to your specific metric and API surface.

- **Define your experiment in three lines.** The `test.md` file only needs three things: goal (what you're trying to achieve), metric (how you'll measure success), and test method (how the agent should implement variants). This minimal spec is sufficient to drive autonomous iteration.

- **Prioritize tighter feedback loops over larger experiments.** A 5-minute cycle beats a 4-hour cycle if volume supports it. The key bottleneck is usually infrastructure (how fast you can deploy and measure), not intelligence. Scaling infrastructure to enable faster iteration is high-leverage.

- **Use `resources.md` as a compounding knowledge asset.** Ensure your orchestrator always reads prior experiment logs before generating new challengers. The accumulated domain knowledge in this file is what differentiates a mature loop (running for months) from a fresh one — treat it as the primary output artifact, not just a log.

- **Map your existing workflows to the pattern.** Walk through your current business metrics and ask: "Do I have an API for this?" Cold email → Instantly API. Landing pages → Webflow/Wix API or Chrome DevTools MCP. Ads → Facebook/Google Ads API. YouTube → YouTube Data API v3. Most modern platforms expose enough programmatic access to make this viable.

## Notable Quotes

> "The idea is to give an AI agent a small but real LLM training setup and just let it experiment autonomously overnight. It'll modify the code, train for 5 minutes, check if the results improved, keep or discard, and then just repeat. You wake up in the morning to a log of experiments and hopefully a better model."

> "Would I be making better decisions than the AI model? Like, probably. I'd be a much more efficient optimizer, but that doesn't really matter because the reality is I take a lot more time to optimize than a model does. I also eat, sleep, have to go to the washroom, and do a variety of other things with my day. AI agents don't."

> "As long as you have [an objective metric], you can then just pick the winner and then make a slight change before looping back. And depending on how tight this feedback loop is, you could theoretically do this in a minute or two."
