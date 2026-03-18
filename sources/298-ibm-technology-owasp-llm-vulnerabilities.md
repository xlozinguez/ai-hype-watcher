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
curriculum_modules: ["06-strategy-and-economics"]
---

# 298: OWASP's Top 10 Ways to Attack LLMs: AI Vulnerabilities Exposed

> **Creator**: IBM Technology | **Platform**: YouTube | **Date**: 2026-03-07 | **Duration**: 25:11

# OWASP's Top 10 Ways to Attack LLMs: AI Vulnerabilities Exposed

## Summary

IBM Technology walks through the updated OWASP Top 10 for Large Language Models, a community-built security framework that catalogues the most critical vulnerabilities teams encounter when deploying LLMs in production. The video focuses on the first four entries: prompt injection (still #1 despite years of awareness), sensitive information disclosure (up four spots, now #2), supply chain vulnerabilities (#3), and data/model poisoning (#4). Each vulnerability is explained with concrete attack mechanics and paired with practical defensive controls.

The central concern is that LLMs blur the boundary between data and instructions in ways that traditional software doesn't, creating novel attack surfaces that standard IT security postures weren't designed to handle. A user input, a document fetched at runtime, or a poisoned training dataset can all become vectors for taking control of system behavior. These aren't theoretical risks — they're the most commonly observed failure modes in real-world LLM deployments.

The video is aimed at practitioners who are already deploying or planning to deploy LLMs and need a structured vocabulary for the threat landscape. Recommended defenses include AI firewalls/gateways, system prompt hardening, data sanitization pipelines, strong access controls, provenance tracking for models and datasets, and ongoing red team/penetration testing.

---

## Key Concepts

### Prompt Injection (Direct and Indirect)
The #1 LLM vulnerability occurs because models cannot reliably distinguish between instructions (system prompt) and user-supplied input. In **direct injection**, an attacker crafts a prompt that overrides or bypasses the system prompt's safety controls — including through unconventional encodings like poetry or Morse code that evade keyword-based filters. In **indirect injection**, malicious instructions are embedded inside a document or web page that the LLM is asked to process, so the attack vector is invisible to the user who triggered it. Consequences range from data leakage to arbitrary command execution on connected systems.

### Sensitive Information Disclosure
LLMs trained on proprietary data — customer PII, patient health records, financial data, internal IP — can regurgitate that data in response to cleverly constructed prompts if proper controls aren't in place. A separate threat vector is the **model inversion / extraction attack**, where an automated agent repeatedly queries the model and harvests responses over time, effectively stealing the intellectual property embedded in the model's weights. This vulnerability jumped four spots in the 2025 update, signaling it's more prevalent than initially anticipated.

### Supply Chain Vulnerabilities
Most organizations don't train their own LLMs — they pull pre-trained models from sources like Hugging Face (2M+ models, many with billions of parameters), which is far too large to manually inspect. The supply chain encompasses not just the base model but the training data, fine-tuning datasets, application code, and underlying IT infrastructure. Any of these layers can introduce compromised or malicious components. Defenses include vetting suppliers, establishing provenance/chain-of-custody for model artifacts, continuous scanning, and keeping all software patched.

### Data and Model Poisoning
If an attacker can influence the data used to train or fine-tune a model, they can subtly corrupt the model's behavior — causing it to produce biased outputs, leak specific information, or behave maliciously under certain trigger conditions. This is distinct from prompt injection (which happens at inference time) and represents a training-time attack. It ranked #4 in the updated list, having dropped one spot not because the risk decreased but because the other threats proved more operationally impactful.

### AI Firewalls / Gateways as a Primary Defense
Across multiple vulnerability categories, the video highlights **AI gateways** as a high-leverage control: a layer sitting between users and the LLM that inspects both inbound prompts and outbound responses. For prompt injection, it can detect and block malicious instructions before they reach the model. For sensitive information disclosure, it can detect and redact sensitive patterns (credit card numbers, PII) in model outputs. This positions AI gateways as the LLM equivalent of a WAF (Web Application Firewall) for traditional web apps.

---

## Practical Takeaways

- **Don't rely solely on system prompt controls** — they're insufficient alone. System prompt hardening is a useful first layer but will always have gaps; combine it with an AI gateway, penetration testing, and output scanning.
- **Treat AI supply chain with the same rigor as software dependencies** — vet base models, track provenance, scan for known vulnerabilities, and document where every model artifact came from before it hits production.
- **Implement AI-specific access controls at multiple layers** — restrict who can query the LLM, who can modify the model, and who can access the training data; don't assume existing IAM policies designed for traditional software cover these surfaces.
- **Run continuous red team / pen testing against your LLM endpoints** — because attack techniques evolve (poetic prompts, Morse code, multi-turn extraction), static defenses degrade quickly and need regular adversarial validation.
- **Sanitize training data before ingestion** — apply filters to prevent sensitive fields (full PII, raw financial records) from entering the model unless necessary, and use the AI gateway on the egress side to catch leakage that slips through.

---

## Notable Quotes

> "The LLMs are not very good at separating the — and making the distinction between — input and instructions. These are the instructions we've given it, but somebody can put new input into it and it will take those as new instructions."

> "We recently found out that even when LLMs have had protections against prompt injections that were written in normal language in prose... if someone rephrased it as a poem, it got past the protections that were in place."

> "Hugging Face is essentially like the GitHub for AI models. And at the last time I checked, there were more than two million AI models on Hugging Face... way too big for anyone to manually inspect."

---
