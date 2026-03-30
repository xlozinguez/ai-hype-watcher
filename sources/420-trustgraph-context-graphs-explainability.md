---
source_id: "420"
title: "Context Graphs in Action | TrustGraph"
creator: "TrustGraph"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=sWc7mkhITIo"
date: "2026-03-21"
duration: "26:52"
type: "video"
tags: ["enterprise-ai", "context-engineering", "ai-sdlc", "prompt-engineering"]
curriculum_modules: ["01-foundations", "06-strategy-and-economics"]
---

# 420: Context Graphs in Action | TrustGraph

> **Creator**: TrustGraph | **Platform**: YouTube | **Date**: 2026-03-21 | **Duration**: 26:52

# Context Graphs in Action | TrustGraph

## Summary

TrustGraph co-founders Daniel and Mark Adams demonstrate their context graph system built on London-area venue data (pubs, restaurants, event spaces), walking through how the graph is constructed from documents, how ontologies structure the knowledge, and how explainability surfaces which graph nodes and relationships grounded a given LLM response. The core thesis is that grounding LLMs in semantically structured knowledge graphs — what they're calling "context graphs" — produces more precise, auditable, and trustworthy AI answers than retrieval-augmented generation alone.

The video distinguishes TrustGraph's RDF-based approach from property graph systems like Neo4j, arguing that RDF's support for reification (metadata about edges), multi-language representation, and semantic web standards makes it better suited for explainable AI retrieval at scale. Ontologies play a central role: by defining allowed classes, relationships, and types in advance, they force the language model into a precise knowledge structure rather than generating free-form, inconsistent triples.

A practical highlight is the live comparison of two semantically similar queries ("where can I drink craft beer in a pub?" vs. a broader phrasing) that return the same answer but activate measurably different subgraph concepts — illustrating that the *path* through the graph, not just the answer, is now observable and auditable. The team positions this as the fulfillment of a long-standing vision from semantic web and semantic network research, now made practical by LLMs.

## Key Concepts

### Context Graphs and Explainability
A context graph is a knowledge graph where the retrieval process is fully traceable: when a question is answered, the system surfaces the exact subgraph — nodes, edges, and source documents — that contributed to the response. This allows users to verify whether an answer is accurate, whether the source data is current, and why a particular response was generated. The explainability layer is structurally built into the graph via edge-to-source tracing, not bolted on afterward.

### Ontology-Guided Graph Construction
An ontology defines the allowed classes, relationship types, and structures within a knowledge graph — analogous to a database schema but designed to capture semantic meaning. TrustGraph uses ontologies to constrain how LLMs populate the graph during document ingestion, preventing the "same concept, different names" inconsistency that appears in free-form triple extraction. The tradeoff is reduced flexibility for domains that don't map cleanly to a predefined ontology, but the gain in retrieval precision is significant.

### RDF vs. Property Graphs for AI Retrieval
TrustGraph deliberately chose the RDF ecosystem over labeled property graphs (e.g., Neo4j) primarily because RDF supports *reification* — the ability to attach metadata (provenance, temporal validity, accuracy) to edges themselves rather than only to nodes. This is structurally important for explainability: tracing an answer back through edges to source documents requires edges to carry that provenance information. RDF's multi-language support and alignment with semantic web standards were additional factors.

### Semantic Similarity + Graph RAG
The original TrustGraph architecture used semantic similarity search as the entry point to a flat triple store: find a starting node via embedding search, then extract a subgraph. Adding ontologies layered on top improved precision and retrieval accuracy by giving the graph more structured topology. Both approaches remain valid for different domains — the flat/free-form approach is more flexible, the ontology-constrained approach is more precise.

### Context Graphs as Revived Semantic Networks
The presenters situate context graphs within a 60-year lineage of semantic network research, arguing that previous knowledge graph deployments (fraud detection, AML/KYC, cybersecurity anomaly detection) prioritized pattern matching over linguistic semantics. The current moment — where LLMs need to be grounded in richer semantic structures — resurrects the original semantic web vision and makes it practically achievable for the first time.

## Practical Takeaways

- **Ontologies materially improve graph RAG precision**: Free-form triple extraction via LLM produces inconsistent relationship naming; defining an ontology upfront constrains the LLM to a consistent schema and dramatically improves retrieval accuracy.
- **Build explainability into the graph structure, not the prompt**: Tracing answers back to source documents requires edge-level provenance metadata (reification in RDF), which must be an architectural decision, not a post-hoc addition.
- **The subgraph path matters, not just the answer**: Two semantically different queries can return identical answers while activating entirely different graph regions — tracking which concepts were engaged is essential for auditing AI behavior in high-stakes contexts.
- **Context graphs are a builder primitive, not an end-user tool**: Graph visualization and workbench tools are for developers understanding system behavior; production UX should be purpose-built on top of the graph APIs (TrustGraph offers TypeScript libraries for this).
- **LLM coding agents can generate graph visualizations from scratch**: The team found that modern coding assistants can build sophisticated graph visualization UIs without off-the-shelf graph libraries, reducing toolchain dependencies.

## Notable Quotes

> "We can see the grounding has actually broadened the concepts that were available to us. So that now even though we've gotten the same response just by asking the question in a slightly different semantic way, we see how many different concepts have been engaged."

> "With an ontology we force it into a much more precise structure... Without an ontology the language model is having to determine the relationships and you know sometimes there are relationships that are the same thing with different names."

> "Graphs never really achieved the success that they could potentially have achieved and the world has been kind of ruled by tabular information... This is a bit of an old use case becoming new again with the need for being able to ground LLMs in more richer semantic structures."
