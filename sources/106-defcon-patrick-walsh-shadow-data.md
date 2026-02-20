---
source_id: "106"
title: "DEF CON 33 - Exploiting Shadow Data from AI Models and Embeddings"
creator: "Patrick Walsh"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=O7BI4jfEFwA"
date: "2025-10-10"
duration: "48:23"
type: "video"
tags: ["security", "ai-safety", "enterprise-ai"]
curriculum_modules: ["06-strategy-and-economics"]
---

# 106: DEF CON 33 — Exploiting Shadow Data from AI Models and Embeddings

> **Creator**: Patrick Walsh (DEF CON) | **Platform**: YouTube | **Date**: 2025-10-10 | **Duration**: 48:23

## Summary

A DEF CON 33 talk by Patrick Walsh (CEO, IronCore Labs) demonstrating that private data embedded in AI systems — fine-tuned models, RAG contexts, vector embeddings, and logs — is far more accessible to attackers than the industry acknowledges. Through live demos, Walsh shows that fine-tuned model safety training can be defeated through simple persistence (repeatedly asking the same question), system prompts and RAG context can be extracted through basic prompt injection techniques, and vector embeddings can be inverted to recover original text with 90-100% accuracy using open-source tools.

The talk's central thesis is that AI systems proliferate private data into multiple unprotected locations (training sets, vector indices, prompts, logs, QA tools, prompt firewalls) while organizations focus security attention on the original data stores. Walsh argues that probabilistic AI outputs make traditional security guarantees impossible — "in application security, 99% is a failing grade" — and that the industry's rush to add AI features is far outpacing security investment. The talk concludes with four protection approaches: confidential compute, fully homomorphic encryption, partially homomorphic encryption, and tokenization/redaction.

## Key Concepts

### Shadow Data Proliferation

When enterprise data enters an AI pipeline, it multiplies across training sets, fine-tuned model weights, vector embeddings, RAG context, prompt logs, QA tool logs, and prompt firewall logs. Each copy has fewer access controls than the original. An attacker targeting a company's sensitive data would rationally target these AI shadow copies rather than the well-protected primary data stores like SharePoint.

### Probabilistic Security is No Security

Neural network outputs are selected with randomness. A model trained not to reveal private data will still leak it as a statistical outlier — the attacker just needs to keep trying. Walsh quotes Simon Willison: "You can train a model on a collection of previous prompt injection examples and get to a 99% score detecting new ones. And that's useless because in application security, 99% is a failing grade." If a firewall let through 1 in 100 packets, it would not be a firewall.

### Vector Embedding Inversion

Using the open-source tool Vec2Text, Walsh demonstrates recovering original text from vector embeddings with high accuracy. A sentence containing a patient name, diagnosis, date, and dollar amount was recovered nearly verbatim from its OpenAI Ada-2 embedding after 10 correction steps. The CEO of a major vector database company (who had raised over $50M) told Walsh that "vectors are like hashes" with no security implications — demonstrating widespread industry ignorance about this attack surface.

### RAG Context Extraction

Through demonstrations against a 40,000-message synthetic email database, Walsh shows that both system prompts and sensitive RAG context can be extracted despite model training and system prompt instructions to protect secrets. The key observation: attack success probability increases with longer conversation context, suggesting the model becomes more confused about what it should or shouldn't reveal as conversations grow.

### Real-World Attack Patterns

Walsh documents a repeating attack pattern against production systems: inject malicious context via email (or similar), trigger it to be pulled into RAG context, embed instructions that cause the LLM to exfiltrate data via crafted links. Microsoft's Copilot was hit with this exact attack twice — once in 2024 (patched) and again in 2025 with minor variations that bypassed the fix.

## Practical Takeaways

- **Audit AI data proliferation**: Map every location where sensitive data gets copied when it enters an AI pipeline — training sets, embeddings, logs, prompt firewalls, QA tools
- **Never rely on system prompts for security**: Every major model from every major company has had its system prompt stolen — system prompt instructions are guardrails, not security boundaries
- **Treat vector embeddings as sensitive data**: They can be inverted to recover original text with 90-100% accuracy using freely available open-source tools
- **Minimize log retention aggressively**: AI logs contain full prompts including RAG context, not just user questions — and legal holds can override retention policies anyway
- **Consider application-layer encryption**: Encrypt before sending data to AI systems; transparent disk/database encryption does nothing for running services
- **Hold vendors accountable**: Most SaaS vendors are adding AI features far faster than they're adding security for those features

## Notable Quotes

> "You can train a model on a collection of previous prompt injection examples and get to a 99% score detecting new ones. And that's useless because in application security, 99% is a failing grade." — Simon Willison, quoted by Patrick Walsh

> "If you had a firewall and it let through one in a hundred packets, that would not be a firewall. It would take a hacker 3 seconds to program something that just sent 100 packets for every packet it needed to send. And it's the same thing with AI." — Patrick Walsh

> "My grade school daughter can attack AI. All I did was just ask an LLM the same questions over and over in some cases. Grab some open source software, run it. I didn't even build the models I used." — Patrick Walsh

## Related Sources

- [017: PrimeAgen Skills Security](017-primeagen-skills-security.md) — Security concerns in the skills ecosystem
- [057: IBM Zero Trust AI Agents](057-ibm-zero-trust-ai-agents.md) — Enterprise security frameworks for AI agents

## Related Curriculum

- [Module 06: Strategy and Economics](../curriculum/06-strategy-and-economics/README.md) — AI security, enterprise deployment risks, data protection strategies
