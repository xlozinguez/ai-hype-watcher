---
source_id: "298"
title: "OWASP's Top 10 Ways to Attack LLMs: AI Vulnerabilities Exposed"
creator: "IBM Technology"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=gUNXZMcd2jU"
date: "2026-03-07"
duration: "25:11"
type: "video"
tags: ["security", "enterprise-ai", "prompt-engineering", "ai-sdlc"]
curriculum_modules: ["06-strategy-and-economics", "02-prompting-and-workflows"]
---

# 298: OWASP's Top 10 Ways to Attack LLMs: AI Vulnerabilities Exposed

> **Creator**: IBM Technology | **Platform**: YouTube | **Date**: 2026-03-07 | **Duration**: 25:11

# OWASP's Top 10 Ways to Attack LLMs: AI Vulnerabilities Exposed

## Summary

This IBM Technology video walks through the updated OWASP Top 10 list for Large Language Model security (revised from the 2023 original), covering the most common and impactful attack vectors teams encounter when deploying LLMs in production. The video focuses on the first four vulnerabilities in detail: prompt injection (still #1), sensitive information disclosure (up four spots to #2), supply chain vulnerabilities (#3), and data/model poisoning (#4). Each vulnerability is explained with concrete attack scenarios and paired with practical defensive countermeasures.

The core insight is that LLMs introduce fundamentally new security failure modes that don't map cleanly onto traditional application security. The inability of LLMs to reliably distinguish between instructions and user input makes prompt injection uniquely hard to eliminate. Meanwhile, the scale of open-source model ecosystems (2M+ models on HuggingFace, many with 1B+ parameters) makes traditional manual verification of supply chain components impossible.

For teams building AI-assisted development tools or deploying LLMs in enterprise contexts, this material is directly relevant: many of the attack surfaces described (plugin ecosystems, model training data, agentic tool execution) align precisely with how AI coding assistants and agent pipelines are architected today.

## Key Concepts

### Prompt Injection (Direct and Indirect)
The #1 vulnerability, unchanged since 2023. Direct injection occurs when an attacker crafts a user-facing prompt that overrides system prompt instructions — the model cannot reliably distinguish between "instructions I was given" and "new input telling me to do something else." Indirect injection is more insidious: a malicious payload is embedded in a document or external data source that the LLM is asked to process (e.g., "summarize this article"), and the embedded instructions hijack the model's behavior without the user doing anything suspicious. Notably, even prose-level safety controls can be bypassed by rephrasing requests as poetry or encoding them in Morse code, illustrating how brittle purely linguistic defenses are.

### Sensitive Information Disclosure and Model Inversion Attacks
Jumped four spots to #2, reflecting how underestimated this risk was in 2023. Risk comes from two directions: (1) PII, PHI, financials, or trade secrets embedded in training data can leak back out through carefully crafted prompts; (2) adversaries can systematically query a model — recording outputs iteratively — to harvest and reconstruct large portions of the model's learned knowledge, a technique called a **model inversion (extraction) attack**. This makes proprietary fine-tuned models a direct intellectual property liability if not properly access-controlled.

### Supply Chain Vulnerabilities
LLM deployments depend on a layered supply chain: training data, base model weights (typically sourced from open-source repositories like HuggingFace), application code, and underlying IT infrastructure. With 2M+ models publicly available — many too large to manually inspect — teams are routinely importing unvetted artifacts into their environments. Any layer can be a vector: poisoned training data, backdoored model weights, vulnerable dependencies, or misconfigured infrastructure. Defenses require provenance tracking (chain-of-custody for model artifacts), automated scanning, red team testing, and consistent patching across all layers.

### AI Gateways and Firewalls as a Cross-Cutting Defense
Multiple vulnerabilities are partially mitigated by inserting an **AI gateway/firewall** between users and the LLM. This component inspects both inbound prompts (detecting injection attempts, policy violations) and outbound responses (detecting data leakage, PII exposure, unexpected command outputs). It functions as a runtime enforcement layer that complements but doesn't replace system prompt hardening, access controls, and penetration testing.

### Access Controls and AI Security Posture Management
Across multiple vulnerabilities, inadequate access controls amplify risk: unrestricted access to the model itself enables extraction attacks; unrestricted access to training data pipelines enables poisoning; unrestricted user access enables prompt injection at scale. "AI security posture management" is framed as the discipline of ensuring security policies (encryption, strong authentication, up-to-date software, proper configuration) are consistently applied across the entire AI system stack — not just the model endpoint.

## Practical Takeaways

- **Don't rely solely on system prompt controls** — they're necessary but insufficient. System prompts cannot anticipate all bypass techniques (poetic rephrasing, encoding schemes, indirect injection via documents). Layer them with AI gateways and penetration testing.
- **Treat open-source model artifacts like untrusted third-party code** — implement provenance tracking, automated vulnerability scanning, and red team testing before ingesting any model from public repositories like HuggingFace into your environment.
- **Sanitize training data inputs AND model outputs** — use filtering pipelines to control what sensitive data enters model training, and deploy output-side inspection to catch leakage of PII, credentials, or proprietary content before it reaches end users.
- **Design LLM-connected agents with minimal permissions** — when an LLM has tool-use or command execution capabilities, a successful prompt injection becomes an arbitrary code execution vulnerability. Limit what the agent can do at the system level.
- **Red team your LLMs on a regular cadence** — send adversarial prompts systematically to identify what bypasses your current controls; this is the only reliable way to discover gaps before attackers do.

## Notable Quotes

> "The reason that this occurs is that the LLMs are not very good at separating — and making the distinction between — input and instructions. These are the instructions we've given it, but somebody can put new input into it and it will take those as new instructions."

> "If you're a poet and don't know it, well, maybe you could be a prompt injector as well... maybe they enter the prompt in Morse code and that gets past the protections that we had."

> "There were more than two million AI models on HuggingFace. That's a lot. And many of these have more than a billion parameters... This is way too big for anyone to manually inspect. Way too big. So that means we're taking in basically unverified information, putting that into our system, and now we're just hoping for the best."
