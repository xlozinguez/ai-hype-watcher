---
source_id: "347"
title: "Karpathy Releases AutoResearch"
creator: "The Pretrained Pod"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=BJpdRgFOgtU"
date: "2026-03-19"
duration: "15:38"
type: "video"
tags: ["agentic-coding", "ai-landscape", "ai-sdlc", "multi-agent"]
curriculum_modules: ["01-foundations", "04-agentic-patterns"]
---

# 347: Karpathy Releases AutoResearch

> **Creator**: The Pretrained Pod | **Platform**: YouTube | **Date**: 2026-03-19 | **Duration**: 15:38

# Karpathy Releases AutoResearch

## Summary

Andrej Karpathy released a project called AutoResearch in early March 2026, which applies an agentic LLM framework (using tools like Codex or Claude Code as the agent harness) to autonomously improve a language model training codebase over a 12-hour window. Starting from an existing, expert-vetted baseline implementation of NanoChat, the agent made approximately 80 incremental commits, each attempting to improve model performance measured by validation bits-per-byte (a perplexity-like metric). The agent self-managed failure modes — memory errors, tensor shape mismatches, gradient explosions, CUDA crashes — by reverting to git history and trying alternative approaches.

The hosts discuss how AutoResearch fits into the broader pattern of agentic coding: the key insight is that feedback loops (metrics improving or degrading) give the agent grounding similar to how unit test feedback supercharges agentic software development. The project is framed as a "training loop search" analogous to evolutionary optimization — try a change, keep it if it helps, revert if it doesn't. The hosts note that the agent is effectively replaying known techniques from its training data (batch size tuning, learning rate schedules, warmdown) rather than inventing genuinely novel architectures.

The deeper question the conversation raises is whether AutoResearch represents a path toward genuine AI research creativity or is fundamentally limited to recombining known techniques. The hosts draw a parallel to neural architecture search (NAS) work from Google Brain in 2018 and note that ML research, unlike most software engineering, involves problems where we don't know if a solution exists until we find it — making autonomous creative discovery a much harder bar to clear.

## Key Concepts

### Agentic Feedback Loops as the Core Value
The critical mechanism enabling AutoResearch isn't just autonomous code generation — it's the feedback loop. The agent receives a training metric signal (validation bits-per-byte) after each experiment, allowing it to determine whether a change helped or hurt. This mirrors how agentic coding tools became dramatically more powerful than one-shot LLM code generation once they could receive test harness feedback. The harness (not included in the public repo) is provided externally via a tool like Codex or Claude Code.

### Git History as a Safety Net for Autonomous Agents
AutoResearch uses version control as its rollback mechanism. When an experiment fails — due to OOM errors, shape mismatches, or crashes — the agent reverts to a prior commit and tries a different approach. This pattern of "try → observe → commit or revert" is a reusable design principle for any autonomous agent operating on a codebase, making git not just a collaboration tool but an agent safety primitive.

### Regurgitation vs. Genuine Research Creativity
The hosts identify a key limitation: the improvements AutoResearch makes appear to be applications of known techniques the model encountered in training data (batch size scaling, learning rate scheduling, warmdown). True research creativity would require synthesizing across disciplines or proposing architectures with no prior precedent — something current models are not clearly capable of. This distinguishes "automated optimization within known solution space" from "AI-driven scientific discovery."

### Neural Architecture Search as Historical Precedent
Google Brain's 2018 neural architecture search (NAS) work, associated with Barret Zoph and Quoc Le, attempted something arguably more ambitious: training a meta-learning network to discover its own architecture during training. NAS didn't catch on largely due to training difficulty and compute costs. AutoResearch can be seen as a more tractable, lower-ambition cousin operating at the training loop level rather than the architectural level.

### ML Research as Non-Deterministic Engineering
The hosts draw a sharp distinction between software engineering (where sufficient headcount guarantees a solvable outcome) and ML research (where we genuinely don't know if a solution exists until it's found). This framing suggests that while AutoResearch is compelling for automating the known-technique optimization layer of ML work, the frontier research layer may remain resistant to automation for fundamental epistemological reasons.

## Practical Takeaways

- **Feedback signal design is foundational for agentic ML work**: Before deploying an autonomous research agent, define a clear, fast-to-compute metric that meaningfully captures progress. Without this, the agent has no basis for evaluating its own changes.
- **Git-as-rollback is a transferable pattern**: Any agentic workflow operating on a mutable codebase should treat the git commit graph as a recoverable state machine, not just a history log. This applies to agentic coding broadly, not just ML research.
- **AutoResearch is a junior researcher accelerator, not a senior researcher replacement**: The project automates the "apply known techniques from literature and test them" layer of ML work — exactly the work junior researchers do. Senior research judgment (novel hypothesis generation, cross-domain synthesis) is not what's being automated here.
- **The agent harness matters as much as the target codebase**: Karpathy published the NanoChat model code, not the AutoResearch harness itself. Practitioners building similar systems need to invest in the scaffolding (experiment tracking, metric reporting, agent prompting) as the primary engineering challenge.
- **Expect diminishing returns and non-monotonic progress**: The step graph showed meaningful gains through ~experiment 45, then diminishing returns with occasional step changes. Budget autonomous research sessions accordingly and set stopping criteria in advance.

## Notable Quotes

> "It's basically this way of just unleashing this auto research agent to fully do whatever it wants and if it messes something up, not a big deal. It can just go back in the git history and start a new."

> "It's almost going to say, 'Okay, I saw in my training data that smaller batch sizes might be good, so let me try that.' Didn't work. Okay, that's fine... And so it's doing that basically. It's almost like regurgitating what it's seen, applying it, and going from there."

> "ML is one of these disciplines where we actually don't know if it can be solved until we solve it."
