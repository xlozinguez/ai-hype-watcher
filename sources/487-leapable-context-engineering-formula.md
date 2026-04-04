---
source_id: "487"
title: "Context Engineering Is a Formula — Here's the Only Way to Think About Building AI Systems"
creator: "Leapable"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=dLkVspcJ1m0"
date: "2026-04-02"
duration: "21:21"
type: "video"
tags: ["context-engineering", "specification", "validation", "multi-agent", "agentic-coding", "prompt-engineering"]
curriculum_modules: ["02-prompting-and-workflows", "04-agentic-patterns"]
---

# 487: Context Engineering Is a Formula — Here's the Only Way to Think About Building AI Systems

> **Creator**: Leapable | **Platform**: YouTube | **Date**: 2026-04-02 | **Duration**: 21:21

# Context Engineering Is a Formula — Here's the Only Way to Think About Building AI Systems

## Summary

The creator presents a unified mental model for AI interaction: context engineering reduces to a formula with fixed variables — a defined **start state**, a defined **end state**, and an AI model that finds the optimal connection between them. Drawing on the concept of "epistemic symmetry" (the idea that LLMs can generate questions from answers with high semantic fidelity, making the two bidirectional), the argument is that all productive AI work begins with clearly articulating the desired output, then working backward to describe the current state. The AI's job is to construct the path between those two points using the full breadth of its training.

A significant portion of the video is spent arguing against parallel agent strategies in favor of iterative optimization: build one connection between start and end, verify it thoroughly via full state verification (passing data through every function, testing edge cases), then strengthen that connection. The creator frames the parallel-agents approach as wasteful — making five mediocre connections and comparing them is inferior to making one connection and refining it. This maps directly to a spec-first workflow: generate a spec doc from the initial prompt, verify the spec reflects the desired output, then use the verified spec to drive actual implementation.

The latter portion demos OCR Provenance, a proprietary context engineering dashboard and RAG system with provenance-aware chunking (linking retrieved chunks back to source documents), multi-model OCR processing, and a vision language model layer for image-to-text conversion. The system is positioned as an "infinite context" solution for agents — siloed databases that any number of agents can query simultaneously, with full billing/activity tracking.

## Key Concepts

### Start State / End State as the Core Formula
Every AI interaction should begin by clearly defining two variables: where you are now (start) and where you want to be (end). The AI model, treated as a repository of human knowledge, finds connections between these two points. The quality of the output is directly proportional to how precisely both states are articulated in the context window. Providing rich documentation of the current system state (e.g., 16 up-to-date project docs) fulfills the start requirement; a detailed feature spec or desired output fulfills the end requirement.

### Epistemic Symmetry and Bidirectionality
The creator's theoretical grounding: LLMs can derive questions from answers (and vice versa) with >90% semantic similarity, making questions and answers functionally equivalent. This justifies starting with the desired output and working backward — the model can reconstruct the necessary framing. Practically, this means you can ask an LLM to generate the spec/prompt that would produce a given output, then use that generated spec to drive implementation.

### Spec-First Loop as a Verification Gate
Before building anything, pass the initial prompt through the model to generate a spec document. Read that spec to confirm the model understood the intent. Only then pass the verified spec back through as the driver for implementation. This two-pass approach (prompt → spec → verify → build) catches misalignment early and ensures the model's interpretation of "end state" matches yours.

### Full State Verification Over Parallel Agents
Rather than spawning multiple parallel agents and comparing results, the preferred approach is: build one implementation, then systematically verify it via full state verification — tracing data transformations through every function and class, testing 5–10 edge cases per function, and confirming tool usage. This produces robust, well-understood systems. Parallel strategies are critiqued as generating multiple shallow attempts rather than one deeply optimized solution.

### Provenance-Aware RAG for Infinite Context
Standard RAG returns decontextualized chunks. Adding provenance means every retrieved chunk carries a pointer back to its source document, allowing the model to retrieve full context when needed. Combined with siloed databases (one per knowledge domain), multi-model OCR, and vision-language image description, this creates an "infinite context" architecture where agents operate on clean, semantically searchable knowledge bases without being bottlenecked by context window size.

## Practical Takeaways

- **Always define both endpoints before prompting**: Document your current system state (ideally as maintained reference docs) and articulate the desired output with equal rigor. The AI's output quality is bounded by the clarity of these two variables.
- **Use the spec-doc loop as a verification gate**: Let the model generate a spec from your initial description, review it for alignment, then use the verified spec to drive implementation — don't skip the human review step between generation passes.
- **Prefer iterative optimization over parallel agent spawning**: Build one solid implementation, verify it end-to-end, then refine. Avoid the instinct to run parallel attempts and compare; it trades depth for breadth at the cost of architectural coherence.
- **Watch for context window degradation in long sessions**: In extended agentic runs (multi-hour Claude Code sessions), older context gets condensed/pruned. Monitor for drift and reintroduce critical state information proactively rather than reactively.
- **Add provenance to any RAG system**: Bare chunk retrieval loses document context. Linking chunks to source locations lets the model escalate from a quick keyword match to full document comprehension when precision matters.

## Notable Quotes

> "Geoffrey Hinton said the AI is the most creative tool ever given to humanity because of its ability to create analogies — the AI can create connections between any two or more points."

> "You just make one [connection] and optimize it. Instead of making five bad connections and then being like, 'oh well, let me now look over them all and see which one's the best.' That's stupid."

> "I will need to do full state verification, manually testing of everything and fine-tuning at each step till I get everything perfectly just the way I want it before I move on to the next step — make sure you're building on good architectural building blocks."
