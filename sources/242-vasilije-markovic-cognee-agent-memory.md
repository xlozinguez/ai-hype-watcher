---
source_id: "242"
title: "Why Your AI Agents Keep Forgetting (And How To Fix That)"
creator: "Vasilije Markovic (Cognee)"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=E8-is7OH3UI"
date: "2026-02-15"
duration: "23:00"
type: "video"
tags: ["context-engineering", "agentic-coding", "multi-agent", "infrastructure", "ai-landscape"]
curriculum_modules: ["04-agentic-patterns", "05-team-orchestration", "06-strategy-and-economics"]
---

# 242: Why Your AI Agents Keep Forgetting (And How To Fix That)

> **Creator**: Vasilije Markovic (Cognee) | **Platform**: YouTube (Mastra) | **Date**: 2026-02-15 | **Duration**: 23:00

## Summary

Vasilije Markovic, founder of Cognee, presents a technical demo addressing two fundamental problems in AI systems: RAG's inability to handle semantic ambiguity (searching "Apple" returns both Apple computers and physical apples) and agents' statelessness (forgetting everything between sessions). Cognee solves this by building knowledge graphs on top of vector embeddings, creating a structured memory layer that agents can query, update, and learn from across sessions.

The talk demonstrates a customer support scenario where a user loses workspace access after payment. Three specialized agents (billing, support, supervisor) investigate the issue with isolated memory domains—each accessing only the data they need (billing records, support tickets, entitlements). The key innovation: agents provide feedback that updates the memory system itself, improving future queries. One agent discovers the root cause (delayed reconciliation between payment and entitlement systems) and records "for future queries, I should search invoice payment status AND billing account status AND webhook reconciliation timing"—actionable intelligence that persists across sessions.

Cognee's architecture combines Neo4j knowledge graphs with vector stores, enabling hierarchical memory, temporal state tracking, and what Markovic calls "memory domains"—isolation layers ensuring agents access appropriate data scopes. Backed by former OpenAI and Facebook AI Research founders, the project has 10,000 GitHub stars and 500,000+ monthly SDK runs.

## Key Concepts

### The Failure of Static and Dynamic RAG

Traditional RAG approaches couldn't handle real-world ambiguity and state management. "Back two, three years ago, people tried to bring their data to LLMs with static RAG—load data to a vector store, embed it, load that into context. The problem is static approaches didn't really work because you couldn't refresh, update, and know what's really going on" ([02:20](https://www.youtube.com/watch?v=E8-is7OH3UI&t=140)).

Dynamic RAG emerged to solve the refresh problem—data updates from source systems automatically. But semantic ambiguity remained: "If you're searching for an Apple, it could be an Apple computer in your organization, it could be a physical Apple someone mentioned in some Slack somewhere. All of that led to RAG not really working out as we needed it" ([02:42](https://www.youtube.com/watch?v=E8-is7OH3UI&t=162)).

The second failure: agentic systems became more capable but "couldn't really keep the state. They would forget about every session and they would not really know what's happening if you turn them on like three, four weeks later" ([03:05](https://www.youtube.com/watch?v=E8-is7OH3UI&t=185)). Cognee's bet: "Something like Cognee would be needed for all the agents to run in production—thousands of agents communicating to each other would need some type of memory solution that's more than RAG and more than what typical data warehouses can offer" ([03:29](https://www.youtube.com/watch?v=E8-is7OH3UI&t=209)).

### Knowledge Graphs + Vector Embeddings = Structured Memory

Cognee creates knowledge graphs on top of embeddings using Neo4j, providing structured semantic representation that pure vector search lacks. "We create knowledge graphs on top of the embeddings. We use Neo4j for that... these knowledge graphs are really difficult to construct at times—you need to manually update them, handle them, deal with them. What we do to simplify that is we built a whole framework that allows you to just use simple Python and Pydantic structures to create and maintain and update these knowledge graphs" ([04:22](https://www.youtube.com/watch?v=E8-is7OH3UI&t=262)).

The framework supports auto-updates and feedback loops: "A lot of elements allow you auto-updates and feedback that can be fed into the system to readjust the things that you don't want to manually change" ([04:46](https://www.youtube.com/watch?v=E8-is7OH3UI&t=286)). The core primitives: ontologies (domain rules and schemas), feedback mechanisms (agent-driven memory updates), and knowledge graphs (structured semantic relationships).

Retrieval architecture combines vector search with graph traversal: "What you see it do is effectively retrieving information from the vector store. Then it's surfacing up to the graph. In the graph it's doing some type of graph traversal and retrieval. We have around 10 to 15 retrievers at this point. Some are specific to time awareness, some are doing more complex composition analysis, others are chain-of-thought type approach" ([14:48](https://www.youtube.com/watch?v=E8-is7OH3UI&t=888)).

### Memory Domains: Isolated, Scoped Agent Access

Cognee implements memory isolation through "memory domains"—logical partitions ensuring agents only access data appropriate to their role. "We can have some type of subscription core layer, billing finance layer, tickets layer, contracts layer—so we can isolate these memory domains in a soft and hard way and understand where to store these different graph/vector representations" ([09:59](https://www.youtube.com/watch?v=E8-is7OH3UI&t=599)).

The billing agent gets restricted access: "Billing agent has access to these specific data sets. We don't want to have a huge graph/vector representation of everything. We want to have these isolation layers... this agent has only access to a part of the information. Why? Because in general terms, when you're deploying an agent, you probably don't want it to have full access, read and write to everything" ([11:49](https://www.youtube.com/watch?v=E8-is7OH3UI&t=709)).

Support agent sees only support tickets. Supervisor agent has full cross-domain access to synthesize findings. Isolation isn't just security—it's cognitive focus. Agents reason better when their search space matches their responsibility scope.

### Agent Feedback Loops: Memory That Learns

The breakthrough: agents don't just query memory—they update it based on investigation outcomes, improving future performance. In the demo, the billing agent discovers a delayed reconciliation issue and records feedback: "For future queries, I should search invoice payment status AND billing account status. Webhook reconciliation timing should be taken into account, and any grace period rules that might be in effect should be taken into account—that's given back as feedback to the system which is going to change future queries. So you get to the solution faster" ([17:29](https://www.youtube.com/watch?v=E8-is7OH3UI&t=1049)).

After feedback is stored, a repeated search returns more targeted results: "We effectively get a better answer with a repeated search because we provided that feedback into the system—the data is more detailed and on point on what needs to be done" ([17:57](https://www.youtube.com/watch?v=E8-is7OH3UI&t=1077)).

This creates a self-improving memory layer. Each agent investigation that identifies a pattern or missing context enriches the ontology for all future queries. The system learns organizational knowledge: which data sources correlate, which temporal sequences matter, which edge cases require special handling.

### The Demo: Multi-Agent Customer Support Investigation

Three agents coordinate to diagnose why a paying customer lost workspace access:

**Scenario**: Customer reports "I paid but I can't access this. What happened?" Their subscription shows downgraded/blocked despite active payment ([06:28](https://www.youtube.com/watch?v=E8-is7OH3UI&t=388)).

**Scattered data across systems**:
- Contract terms and ontologies (meta-rules about how the system should work)
- Billing records, invoices, payments in relational stores
- Account status flags in production DB
- Workspace entitlement state defining access levels and seat limits ([06:53](https://www.youtube.com/watch?v=E8-is7OH3UI&t=413))

**Billing agent** investigates payment status, searches memory for invoice records, discovers: "Invoice status is paid, Stripe is captured... status of invoice becomes clear" ([15:17](https://www.youtube.com/watch?v=E8-is7OH3UI&t=917)). Continues investigation, connects dots: "We have a delayed reconciliation that didn't clear the status correctly. Entitlement cache resync was required to restore product access. One system didn't update the other—we need to manually trigger the update or ask the other agent that has access to that to trigger that update" ([15:42](https://www.youtube.com/watch?v=E8-is7OH3UI&t=942)).

**Root cause**: "The account remained in past-due status after payment... reconciliation was completed with 'event past due cleared' but explicit event emission for billing status change and resync of entitlement is required to restore full access" ([16:38](https://www.youtube.com/watch?v=E8-is7OH3UI&t=998)).

**Support agent** runs parallel investigation on the support ticket side, cross-referencing user reports with system state. **Supervisor agent** synthesizes findings from both specialized agents, determines resolution steps, updates timeline audit stream showing event sequence ([19:16](https://www.youtube.com/watch?v=E8-is7OH3UI&t=1156)).

### Production Use: Scientific Hypothesis Prediction

Beyond customer support demos, Cognee handles complex domain-specific cases. Bayer uses it for "scientific hypothesis prediction where we are decomposing elements of the scientific hypothesis and then calculating future possible states of these in the vector space—it gets quite tricky on what you can do with this type of representation both on the graph and the vector side" ([20:05](https://www.youtube.com/watch?v=E8-is7OH3UI&t=1205)).

Markovic emphasizes domain specialization: "We are really working with clients that have more specific needs in domain mapping in different memory domains like finance or healthcare or legal where we can effectively utilize the full use of Cognee. So the agents access what they need to access, and our specialty is this memory representation that we are building on top of graph and vector stores" ([20:30](https://www.youtube.com/watch?v=E8-is7OH3UI&t=1230)).

## Practical Takeaways

- **RAG alone is insufficient for production agents**: Semantic ambiguity (Apple computer vs. apple fruit) and lack of state persistence make pure RAG unsuitable for multi-session agentic systems. Memory layers require structured semantic representation (knowledge graphs) + vector embeddings.

- **Implement memory isolation for agent security**: "When deploying an agent, you probably don't want it to have full access, read and write to everything." Use memory domains to partition data by role/responsibility—billing agents see billing data, support agents see tickets, supervisors synthesize across domains.

- **Enable agent feedback loops to build organizational knowledge**: The most valuable insight isn't the agent's answer—it's the agent recording "for future queries, search X AND Y AND check Z timing." This actionable intelligence compounds across investigations, making the memory layer smarter over time.

- **Combine graph traversal with vector search for temporal reasoning**: Vector search retrieves similar content; graph traversal tracks causal chains, temporal sequences, and relational context. "Some retrievers are specific to time awareness... others are chain-of-thought composition." Use 10-15 specialized retrievers rather than one-size-fits-all search.

- **Persist agent sessions and reasoning state**: Don't start from scratch every run. Store per-agent, per-session reasoning in Neo4j: "When it comes next time, it would already have this information back. You don't always have to start from the fresh run" ([22:38](https://www.youtube.com/watch?v=E8-is7OH3UI&t=1358)).

- **Cognee implementation is lightweight**: "Three, four commands—you start by adding which registers the data, then cognify which transforms data into graph/vector representation using the default pipeline. After that, you can search" ([09:34](https://www.youtube.com/watch?v=E8-is7OH3UI&t=574)). Open source, integrates with LangGraph agents.

## Notable Quotes

> "Back two, three years ago, people tried static RAG—load data to a vector store, embed it, load into context. The problem is static approaches didn't work because you couldn't refresh, update, and know what's really going on." — Vasilije Markovic ([02:20](https://www.youtube.com/watch?v=E8-is7OH3UI&t=140))

> "If you're searching for an Apple, it could be an Apple computer in your organization, it could be a physical Apple someone mentioned in some Slack somewhere. All of that led to RAG not really working out." — Vasilije Markovic ([02:42](https://www.youtube.com/watch?v=E8-is7OH3UI&t=162))

> "Agentic systems became more capable but they couldn't really keep the state. They would forget about every session and not know what's happening if you turn them on three, four weeks later." — Vasilije Markovic ([03:05](https://www.youtube.com/watch?v=E8-is7OH3UI&t=185))

> "When deploying an agent, you probably don't want it to have full access, read and write to everything. So we isolate memory domains." — Vasilije Markovic ([11:49](https://www.youtube.com/watch?v=E8-is7OH3UI&t=709))

> "For future queries, I should search invoice payment status AND billing account status. That's given back as feedback to the system which changes future queries. So you get to the solution faster." — Vasilije Markovic ([17:29](https://www.youtube.com/watch?v=E8-is7OH3UI&t=1049))

> "We effectively get a better answer with a repeated search because we provided that feedback into the system—the data is more detailed and on point on what needs to be done." — Vasilije Markovic ([17:57](https://www.youtube.com/watch?v=E8-is7OH3UI&t=1077))

## Related Sources

- [099: How AI Agents Search Their Memory](099-damian-galarza-agent-memory-search.md) — Complementary perspective on agent memory architecture
- [182: How AI Agent Memory Systems Work: Sessions, Compaction, and Persistence](182-damian-galarza-agent-memory.md) — Memory session management and compaction strategies
- [208: Open Brain: Agent-Readable Memory Architecture with Postgres and MCP](208-nate-b-jones-open-brain-agent-readable-memory.md) — Alternative memory architecture using Postgres + MCP
- [213: OpenAI Leaked GPT-5.4. It's a Distraction. (The AI Lock-In No One Is Talking About)](213-nate-b-jones-openai-context-lock-in.md) — Strategic context on enterprise-scale memory and retrieval challenges
- [212: Minions Part 2 — Devboxes, Blueprints, and Context Management at Stripe](212-stripe-minions-technical-deep-dive.md) — Stripe's approach to context management in agentic systems

## Related Curriculum

- [Module 04: Agentic Patterns](../curriculum/04-agentic-patterns/README.md) — This source directly informs memory system design, agent feedback loops, and stateful reasoning patterns
- [Module 05: Team Orchestration](../curriculum/05-team-orchestration/README.md) — Demonstrates multi-agent coordination with isolated memory domains and supervisor synthesis
- [Module 06: Strategy and Economics](../curriculum/06-strategy-and-economics/README.md) — Infrastructure considerations for production memory layers (Neo4j, vector stores, retrieval architecture)
