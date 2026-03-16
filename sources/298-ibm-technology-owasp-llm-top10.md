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

## Summary

IBM Technology walks through the updated OWASP Top 10 for Large Language Models (2025 revision), explaining how the threat landscape has evolved since the original 2023 list. The video focuses on why LLMs introduce a fundamentally new category of security risk: unlike traditional software, LLMs cannot cleanly separate instructions from input data, making them inherently susceptible to manipulation through carefully crafted text. The presenter covers the top four entries in depth — prompt injection, sensitive information disclosure, supply chain vulnerabilities, and data/model poisoning — with concrete attack scenarios and mitigation strategies for each.

The core insight is that deploying an LLM in production is not just a software engineering challenge but a security posture challenge. Traditional security controls (access controls, firewalls, patching) still apply, but they must be augmented with AI-specific defenses like AI gateways, data sanitization pipelines, and adversarial penetration testing. The fact that prompt injection remains #1 two years after the first list underscores that this class of vulnerability is structural, not easily patched away.

The video is aimed at practitioners and security teams beginning to govern AI deployments, offering a practical framework grounded in OWASP's community-built guidance rather than vendor-specific tooling.

---

## Key Concepts

### Prompt Injection (Direct and Indirect)
The #1 vulnerability on the updated list, unchanged from 2023. LLMs cannot reliably distinguish between system instructions and user-supplied input, so an attacker can override intended behavior through clever phrasing. **Direct injection** comes from the user prompt itself (e.g., roleplay framings, Morse code, poetic rephrasing to bypass safety filters). **Indirect injection** is more insidious: malicious instructions are embedded in external content the LLM is asked to process (e.g., "summarize this article"), allowing a third-party document or webpage to hijack the model's behavior without the user ever sending a malicious prompt.

### Sensitive Information Disclosure
Moved up four spots from 2023, reflecting how much worse this has gotten in practice. Training an LLM on proprietary or sensitive data (PII, PHI, financials, trade secrets) creates a retrieval risk: the model may reproduce that data when prompted cleverly. A related threat is **model inversion / extraction attacks**, where an automated agent repeatedly queries an LLM to harvest its underlying training data or intellectual property at scale — essentially stealing the model's knowledge base over many interactions.

### Supply Chain Vulnerabilities
LLMs depend on a multi-layer stack — training data, pre-trained base models (often sourced from open repositories like HuggingFace's 2M+ models), application code, and underlying IT infrastructure. Any layer can introduce compromised or malicious components. Because models can have billions of parameters, manual inspection is impossible, meaning organizations often deploy "unverified" third-party models and hope for the best. Provenance tracking (chain of custody for models and data), automated scanning, and vendor vetting are the primary defenses.

### Data and Model Poisoning
Attackers who can influence the training data or fine-tuning process can shape how a model behaves — introducing backdoors, biases, or malicious response patterns that activate under specific conditions. This threat dropped one spot on the list not because it improved but because the other vulnerabilities proved more immediately impactful in practice. It remains a top-four concern, particularly for organizations that fine-tune on user-generated or third-party data.

### AI Firewall / AI Gateway
A recurring defense pattern across multiple vulnerability types. An AI gateway sits between the user and the LLM, inspecting both incoming prompts and outgoing responses. It can detect and block injection attempts before they reach the model, and redact or block sensitive data leaking out in responses. This is positioned as the most broadly applicable technical control — addressing prompt injection, sensitive data disclosure, and partially supply chain risks — and maps conceptually to the role of a WAF in traditional web security.

---

## Practical Takeaways

- **Layer your defenses**: System prompt hardening alone is insufficient for prompt injection — you cannot anticipate every bypass (poems, Morse code, foreign languages). Pair it with an AI gateway and regular adversarial pen testing.
- **Sanitize data before it enters training**: Filter sensitive fields (PII, PHI, financials) from training datasets rather than relying solely on output controls. Assume anything in the training corpus can eventually be extracted.
- **Treat open-source models like unverified dependencies**: Pulling from HuggingFace carries the same supply chain risk as pulling from a public package registry. Establish provenance tracking, scanning, and red-team testing before deploying any third-party model.
- **Apply traditional security hygiene to AI infrastructure**: Strong access controls on the model, training data, and user access; encrypt data at rest; patch underlying platforms; audit for misconfigurations. AI-specific risks layer on top of, not instead of, conventional security practices.
- **Penetration test your LLM deployments**: Actively send adversarial prompts to your production system to discover gaps before attackers do. This is analogous to pen testing web apps but requires AI-specific attack repertoires.

---

## Notable Quotes

> "The LLMs are not very good at separating — and making the distinction between — input and instructions. These are the instructions we've given it, but somebody can put new input into it and it will take those as new instructions."

> "If someone rephrased it as a poem, it got past the protections that were in place. So if you're a poet and don't know it, well, maybe you could be a prompt injector as well."

> "You're getting it from an open source. So some of those are good and some of them — maybe not so much. So what I need to be able to do is vet all of this information."

---
