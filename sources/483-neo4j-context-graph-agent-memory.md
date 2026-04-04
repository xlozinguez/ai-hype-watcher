---
source_id: "483"
title: "Building Context Graphs for AI Agents, Will Lyon, Neo4j"
creator: "Neo4j"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=qMV64p-4Deo"
date: "2026-04-01"
duration: "20:46"
type: "video"
tags: ["multi-agent", "context-engineering", "enterprise-ai", "agent-teams", "validation"]
curriculum_modules: ["04-agentic-patterns", "05-team-orchestration", "06-strategy-and-economics"]
---

# 483: Building Context Graphs for AI Agents, Will Lyon, Neo4j

> **Creator**: Neo4j | **Platform**: YouTube | **Date**: 2026-04-01 | **Duration**: 20:46

# Building Context Graphs for AI Agents — Neo4j / Will Lyon

## Summary

Will Lyon, product manager on Neo4j's AI Innovation team, presents the concept of a **context graph**: a knowledge graph that captures not just *what* happened in a system but *why* decisions were made. He frames context graphs as the missing layer for AI agents that need to explain and audit their reasoning — particularly in high-stakes domains like financial services, where credit decisions, fraud flags, and policy applications must be traceable. The talk is grounded in a working demo app (credit limit approval agent) that uses Neo4j to store entities, transactions, decisions, and policies in a connected graph.

The second half of the talk covers Neo4j's open-source **Neo4j Agent Memory** Python package, which provides three tiers of memory for agents: short-term (conversation/session state), long-term (entity extraction into the graph), and reasoning memory (tool call traces and decision steps). A key insight is that entity extraction pipelines should avoid relying solely on LLMs for cost and speed reasons, instead using a staged approach: traditional NER (spaCy) → lightweight local models (GLiNER) → LLM fallback only when necessary.

Lyon also emphasizes **hybrid search** — combining vector similarity with graph traversal — as especially powerful for context graphs, and introduces graph embeddings (via Neo4j's fastRP algorithm) as a way to capture structural similarity between entities, not just semantic similarity of text. The Lenny's Podcast demo illustrates how the same agent memory architecture can construct context graphs from unstructured conversation transcripts, including geospatial enrichment from Wikipedia.

## Key Concepts

### Context Graph as "The Missing Why"
A context graph is a knowledge graph that captures the full decision-making context: events (transactions), entities (people, organizations), and the *why* (decisions, policies, precedents). Unlike a standard knowledge graph, it explicitly models causal chains — decision nodes link to each other as precedents — enabling both explainability for AI agents and organizational audit trails.

### Three-Tier Agent Memory Architecture
Neo4j's agent memory framework separates memory into three types that all land in one connected graph:
- **Short-term**: conversation and session state
- **Long-term**: entities and facts extracted from messages
- **Reasoning**: tool call traces, decision steps, and the entities retrieved to support them

This unified graph allows cross-system queries across all three memory types simultaneously, which is what enables full decision provenance.

### Staged Entity Extraction Pipeline
Rather than routing all messages to an LLM for entity/relationship extraction (expensive and slow), the recommended pipeline stages work as follows: (1) statistical NER via spaCy, (2) GLiNER — a small, CPU-runnable, fine-tuned extraction model — and (3) LLM fallback only for what the prior stages can't resolve. Domain-specific entity models (e.g., financial services vs. default POLE taxonomy) further improve relevance and reduce noise.

### Hybrid Graph + Vector Search
Effective retrieval for context graphs combines traditional vector similarity search with graph traversal. Graph embeddings (e.g., fastRP) complement text embeddings by encoding *structural* relationships — how an account connects to transactions, other accounts, and fraud patterns — rather than just semantic content. This makes relevant precedent retrieval significantly more accurate than text-only vector search.

### Reasoning Memory as a First-Class Abstraction
Most agent memory frameworks focus on episodic (conversation) and semantic (entity) memory but neglect procedural/reasoning memory — the record of *how* the agent reasoned to reach a decision, including which tools it called and which context nodes it retrieved. Lyon argues this is the most critical layer for context graphs supporting auditability and agent explainability.

## Practical Takeaways

- **Don't use LLMs alone for entity extraction at scale.** A staged pipeline (NER → GLiNER → LLM) dramatically reduces cost and latency while maintaining quality for long-running agent systems.
- **Model your domain explicitly.** Customize the entity/relationship schema for your domain (financial, healthcare, etc.) rather than using a generic graph schema — this controls what gets extracted and stored, keeping the context graph relevant and queryable.
- **Record tool call traces as first-class graph nodes.** Storing which tools an agent called, in what order, and which entities were retrieved creates the reasoning memory needed for auditing and for future agents to learn from precedent.
- **Use graph embeddings alongside text embeddings** to surface structurally similar entities — fraud pattern matching, for example, benefits from structural similarity in the graph topology, not just textual content.
- **Decision nodes should link to each other as precedents.** Designing the data model so that decisions explicitly reference prior decisions enables causal chain traversal — a key feature for both compliance and improved agent recommendations over time.

## Notable Quotes

> "A context graph is a knowledge graph that contains all of the information necessary to make decisions throughout the organization."

> "It's really important that the memory that we are saving to the graph is relevant for our domain... if we're financial services, we should be making sure that we're saving financial services related data and not unrelated things."

> "I think reasoning memory is one of the more important pieces for building context graphs. And I think it's this piece that we actually don't see a lot of support for in a lot of the AI agent memory frameworks that are out there."
