---
source_id: "369"
title: "​Context graphs as the control plane for the agentic enterprise, Dave Bennett, Indykite"
creator: "Neo4j"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=GiOWEN4E7Mo"
date: "2026-03-24"
duration: "23:29"
type: "video"
tags: ["multi-agent", "enterprise-ai", "security", "mcp", "agent-teams"]
curriculum_modules: ["05-team-orchestration", "06-strategy-and-economics"]
---

# 369: ​Context graphs as the control plane for the agentic enterprise, Dave Bennett, Indykite

> **Creator**: Neo4j | **Platform**: YouTube | **Date**: 2026-03-24 | **Duration**: 23:29

# Context Graphs as the Control Plane for the Agentic Enterprise

## Summary

Dave Bennett, a solutions engineer at IndyKite, presents the case for using context graphs as a governance and control layer for enterprise multi-agent systems. The core thesis is that as organizations deploy increasingly complex networks of AI agents, the traditional approach of embedding permissions and policies directly into each agent creates an unmanageable, fragmented mess. IndyKite's answer is to decouple agent intelligence from agent governance by centralizing control in a context graph that tracks identity, delegation chains, and access policies dynamically at runtime.

The architecture relies on OAuth token exchange to construct a full calling chain — from the original human user through every agent invocation — so that at each hop the system can verify whether the workflow is valid and whether the calling user is actually permitted to trigger it. Agents have no standing privileges; instead, they inherit scoped context from their callers. This means a user's effective access within a given agentic workflow is the intersection of the user's own permissions and the permissions associated with every agent in the chain, dramatically limiting blast radius from misconfigured or compromised agents.

The demo illustrates the concept using a fictional bank scenario: a customer service rep (Leslie) interacts with a chatbot that routes through an orchestrator agent and a retriever agent, each validated through IndyKite's agent gateway before reaching an MCP server. The context graph stores agent catalog metadata, tool ownership, policy documents ingested from enterprise systems (SharePoint, Salesforce, Workday), and decision traces — making every authorization decision queryable and auditable after the fact.

## Key Concepts

### Context Graphs vs. Traditional Knowledge Graphs
Traditional knowledge graphs encode static facts as triples (e.g., "Employee A works in Department B"). Context graphs extend this with provenance, temporal validity, and materialized decision traces. Because authorization decisions are stored as graph objects, lineage can be traced backward through many decisions — answering not just *what* happened but *why*, *how*, and in *what sequence*. This makes context graphs a natural fit for audit and compliance requirements in agentic deployments.

### Decoupling Agent Intelligence from Agent Governance
IndyKite's central design principle is that the intelligence layer (LLMs, orchestration logic) should be fully separated from the governance layer (identity, access control, policy enforcement). This means new agents can be introduced without rebuilding governance from scratch, and governance policies can evolve without requiring changes to agent code. The context graph serves as the stable control plane that both layers interact with independently.

### OAuth Token Exchange and Delegation Chains
Rather than assigning fixed roles to agents, IndyKite uses the OAuth token exchange specification to dynamically mint tokens that encode the full calling chain. When a human user triggers a workflow, the IDP issues a token where the human is the *subject* and the first agent is the *actor*. As the request propagates to downstream agents, each hop mints a new token appending the next agent as actor. The resulting token carries the complete delegation chain (user → agent 1 → agent 2), enabling the system to validate at every step: is this a known workflow, and is this user permitted to invoke it?

### Least Privilege at Runtime via Calling Context
Because the full calling chain is embedded in the token, access can be scoped to the intersection of all participants' permissions. Even if a user nominally has broad data access, the effective permissions within a specific agentic workflow are constrained by what each agent in the chain is allowed to do. This enforces least privilege dynamically without manual policy configuration per workflow — the graph computes the intersection at query time.

### Agent Identity and Catalog in the Graph
Agents are materialized as first-class objects in the context graph, with ownership metadata maintained through adjacent graph nodes. This creates an enterprise-wide catalog of agents, skills, and tools — solving the immediate operational problem most enterprises face today: no one knows which agents exist, who owns them, or what they can access. The graph also tracks MCP server connections, flagging the explosion of internal and external tool integrations as a data exposure risk that needs governance.

## Practical Takeaways

- **Treat agent identity as a first-class concern from day one.** Cataloging agents in a graph with ownership metadata prevents the "shadow agent" problem where deployed agents become ungoverned and unauditable.
- **Use token exchange (OAuth RFC 8693) to propagate human identity through agent chains**, rather than letting agents authenticate independently with their own credentials. This preserves the human-in-the-loop accountability chain even in fully automated pipelines.
- **Materialize authorization decisions in the graph**, not just data facts. Storing decision traces as queryable graph objects enables post-hoc audit, debugging, and regulatory compliance without separate logging infrastructure.
- **Scope agent permissions to the intersection of the calling chain**, not the maximum of any participant. This is the practical implementation of least privilege in multi-agent systems and significantly reduces blast radius from a compromised or misbehaving agent.
- **Separate data ingestion from graph storage.** Temporal or telemetry data that's only needed at a single point in time doesn't need to live in the graph — the control plane can reach out via API at query time, keeping the graph focused on durable context rather than transient data.

## Notable Quotes

> "It's not just enough to have data now. We need to operationalize it... in order to make AI deployable with the least amount of friction, we need to up our game in the control layer."

> "Agents have no standing privilege in our world, but instead get their context from a calling human or another calling agent."

> "Even though Joe might have access to all kinds of things, in the little slice of this transaction, Joe plus agent two plus agent one only has this much access."
