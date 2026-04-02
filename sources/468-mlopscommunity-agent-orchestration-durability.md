---
source_id: "468"
title: "Decomposing the Agent Orchestration System: Lessons Learned"
creator: "MLOps.community"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=H9fsxdK-NeQ"
date: "2026-03-31"
duration: "30:12"
type: "video"
tags: ["multi-agent", "infrastructure", "context-engineering", "agentic-coding", "enterprise-ai", "ai-sdlc"]
curriculum_modules: ["05-team-orchestration", "06-strategy-and-economics", "04-agentic-patterns"]
---

# 468: Decomposing the Agent Orchestration System: Lessons Learned

> **Creator**: MLOps.community | **Platform**: YouTube | **Date**: 2026-03-31 | **Duration**: 30:12

# Decomposing the Agent Orchestration System: Lessons Learned

## Summary

Neils Bantilan, Chief ML Engineer at Union and maintainer of the Flyte ML orchestration platform, presents hard-won lessons from productionizing agentic systems at scale. Drawing on five years building tools used by LinkedIn, Stripe, Spotify, and Mistral, he argues that the dominant failure mode in production agents isn't prompt quality or model capability—it's infrastructure. Agents fail at multiple layers simultaneously (infra, network, logical, semantic, tool execution), and recovering from those failures is nearly impossible without full cross-layer context.

The central thesis is that **context engineering is an infrastructure problem**. Standard eval harnesses test semantic correctness but ignore infrastructure-level failures: network timeouts, OOM errors, spot instance preemption, node pool crashes. When these events wipe agent state, all the carefully engineered context is lost with it. Bantilan's answer is to treat durability as a first-class primitive—not an afterthought—by building replay logs, global caching, and intermediate state persistence directly into the orchestration layer.

The talk introduces six design principles distilled from building Flyte 2.0 and internal agents like "Nody" (a Kubernetes node pool configuration agent). These principles converge on a core insight: agents are now capable of recovering from even infrastructure-level failures, but only if they are given the right context and self-healing capabilities to do so. The recommended stack centers on plain Python (or equivalent), functional durability hooks, infrastructure-as-context patterns, and human-in-the-loop as a final recourse.

---

## Key Concepts

### Replay Logs (Run-Level Micro-Cache)
A replay log records agent state and subtask outputs at a granular per-step level within a single run. If an agent executing a 1,000-step workflow fails at step 347, the replay log allows it to resume from exactly that point without re-executing prior steps. This prevents both compute waste and context/memory loss from crashes in the root agent process. Bantilan distinguishes this from global caching: replay logs are scoped to a single run, while global caches share deterministic outputs (e.g., web searches, DB reads) across all runs and all agents.

### Infrastructure as Context
A key design principle: the orchestration layer should surface infrastructure-level events (OOM errors, scheduler kills, spot preemptions, network timeouts) as first-class, catchable exceptions within the agent's reasoning loop. Python's `try/except` pattern becomes a natural delivery mechanism for infra failure context. The agent can then reason about—and potentially recover from—failures that previously would have been silent or unrecoverable. This closes the "evaluation gap" between semantic correctness testing and real-world infrastructure failure modes.

### Intermediate State Persistence
Rather than requiring engineers to write custom serialization/deserialization code, a well-designed orchestration layer should automatically persist outputs of every LLM call and tool call to object storage (e.g., S3). This provides data lineage out of the box, enables recovery from partial failures, and removes a class of boilerplate that's typically skipped under deadline pressure. Bantilan frames this as a "functional durability hook"—a decorator pattern that makes persistence declarative rather than imperative.

### The Evaluation Gap
Current eval harnesses are built to measure semantic correctness: hallucination rates, tool call argument formatting, answer quality. They systematically ignore infrastructure failure modes. This creates a gap where agents are well-tested for the problems they're less likely to encounter in short demo runs, but completely untested for the failures that dominate long-running production workflows. Closing this gap requires either extending evals to include infrastructure fault injection or—Bantilan's preferred approach—building the orchestration layer to handle infra failures transparently.

### Variable Compute in the Agent Inner Loop
ML and data science agents cannot run on a single fixed node. An agent may orchestrate tasks that span a lightweight CPU process (the agent itself) and a heavy GPU training job loading multi-gigabyte datasets. Without dynamic compute provisioning inside the agent loop, resource contention and degraded performance are inevitable. The orchestration layer must allow agents to provision their own compute resources on demand as part of normal task execution—a requirement largely absent from general-purpose agent frameworks.

---

## Practical Takeaways

- **Build durability before you need it.** Replay logs and intermediate state persistence should be infrastructure defaults, not features added after your first production outage. A 1,000-step agent that crashes at step 999 and replays from step 1 is a catastrophic user experience.

- **Use plain Python (or equivalent general-purpose language) as your agent substrate.** DSLs and proprietary agent frameworks add cognitive overhead for both humans and LLMs. Plain Python gives you loops, conditionals, async/sync, and try/except—and LLMs already know it well. Frameworks can be layered on top, not underneath.

- **Treat exceptions as context-delivery mechanisms.** Infrastructure errors that bubble up as catchable exceptions can be reasoned about by the agent itself. Don't swallow or log-and-continue infra errors—surface them as structured context so the agent has a chance to self-correct.

- **Separate caching strategies by determinism.** Use run-scoped replay logs for crash recovery; use global caches for deterministic, shareable work (data fetches, searches). Disable global caching selectively for steps where you want entropy (e.g., synthesis/composition steps).

- **Human-in-the-loop is a first-class architectural primitive, not a fallback.** Design the escalation path to human review into the agent loop from day one. Agents will fail at layers that no amount of self-healing can address; the question is whether the system gracefully hands off or silently degrades.

---

## Notable Quotes

> "The problem isn't that agents fail, it's that recovering from failure is challenging without the full context of how infra, networking, logical, semantic layers all interact so that the agent can figure out how to dig itself out of the hole it's found itself in."

> "Context engineering is not just shuffling tokens and getting more data sources... Context engineering is also an infra problem. If a failure wipes the agent state, then all the hard-earned context that you've implemented in your agent loop is worthless."

> "Agents can actually recover reliably from all the errors in the stack—even infrastructure-level ones—but only if you give them the right context and the right capabilities to dig themselves out of that hole."

---
