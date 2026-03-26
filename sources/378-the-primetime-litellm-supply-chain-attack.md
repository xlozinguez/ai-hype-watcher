---
source_id: "378"
title: "I did not expect this ending"
creator: "The PrimeTime"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=mx3g7XoPVNQ"
date: "2026-03-26"
duration: "8:38"
type: "video"
tags: ["security", "mcp", "vibe-coding", "cursor", "ai-hype"]
curriculum_modules: ["06-strategy-and-economics", "02-prompting-and-workflows"]
---

# 378: I did not expect this ending

> **Creator**: The PrimeTime | **Platform**: YouTube | **Date**: 2026-03-26 | **Duration**: 8:38

## Summary

The LiteLLM Python package — downloaded 97 million times per month — was compromised when the repository owner's GitHub account was hacked, allowing attackers to push malicious code into version 1.82.8. The poisoned package installed a `.pth` file that executes on every Python interpreter startup, silently exfiltrating SSH keys, cloud credentials (AWS, GCP, Azure), Kubernetes configs, database passwords, git credentials, crypto wallets, and environment variables — the full spectrum of developer secrets. The threat actor claims to have stolen over 500,000 credentials and 300 GB of compressed data, and is currently extorting multiple multi-billion dollar companies.

The story has three compounding layers of irony. First, a vibe coder (Callum McMahon) inadvertently discovered the attack because the malicious `.pth` file contained a fork bomb bug that crashed his machine by consuming all RAM — the hack failed through its own incompetence. Second, when the GitHub issue was opened to report the vulnerability, it was immediately flooded with hundreds of AI-generated bot replies ("Great explanation! Thanks for sharing!") that buried the real discussion and caused the maintainer to close the issue as "not planned" — a novel social engineering attack on open-source collaboration infrastructure. Third, LiteLLM's website displayed SOC 2 and ISO 27001 compliance badges issued by Delve, a Y Combinator-backed "AI-native compliance" company that is itself being accused of issuing fraudulent compliance reports. Both companies are YC-backed.

Prime uses the incident as a cautionary case study on multiple failure modes simultaneously: supply chain vulnerability, the danger of transitive dependencies in MCP/agentic workflows, AI-generated noise as an attack vector against open-source issue trackers, and the potential hollowness of AI-native compliance tooling.

---

## Key Concepts

### Supply Chain Attacks via Transitive Dependencies
LiteLLM was pulled in not by users directly installing it, but as a transitive dependency of an MCP plugin used inside Cursor. This is the canonical supply chain risk: you don't have to choose a malicious package — any tool you trust can pull it in for you. The `.pth` mechanism makes it particularly dangerous: Python automatically executes any `.pth` file on interpreter startup, meaning the payload runs before any user code and with no obvious trigger.

### AI Bot Spam as Issue Suppression
The attackers (or automated systems) flooded the GitHub issue report with hundreds of generic AI-generated affirmations to bury the legitimate security disclosure. The issue was closed as "not planned" in the noise. This is a novel attack surface — using LLM-generated content to degrade the signal-to-noise ratio of open-source collaboration, overwhelming maintainers and confusing investigators with hundreds of indistinguishable replies. Prime notes this friction tactic had never crossed his mind as a possible attack vector.

### `.pth` File Hijacking
Python's `.pth` (path configuration) files are executed automatically whenever the Python interpreter initializes. By placing malicious code in a `.pth` file via a package install, the attacker ensures payload execution on every Python process launch — no explicit import required. The exfiltrated data was double-Base64 encoded before transmission, which Prime notes is a "classic hacker signature."

### Vibe Coding as Accidental Security Research
Karpathy's framing (disputed as having "no evidence") is that vibe coding actually surfaced the vulnerability — a developer using AI-assisted tools inside Cursor triggered the fork bomb crash that exposed the attack. The fork bomb was an unintentional bug in the malicious payload: it spawned subprocesses recursively when run inside an MCP server environment, consuming all available RAM. The attacker's own code quality failure is what alerted the community.

### AI-Native Compliance Theater
LiteLLM displayed SOC 2 Type 1 and ISO 27001 badges from Delve, a YC-backed company marketing itself as "AI-native compliance." Delve is simultaneously facing accusations of issuing misleading or fabricated compliance certifications. This compounds the security failure: not only was the package compromised, but its compliance attestations may have been meaningless — illustrating how "AI-native" branding attached to security/compliance tooling does not substitute for actual rigor.

---

## Practical Takeaways

- **Rotate all credentials immediately** if you use LiteLLM or any tool that depends on it (e.g., certain Cursor MCP plugins). The threat actor claims 500k+ stolen credentials and is actively extorting victims.
- **Audit transitive dependencies** in your MCP server configurations and agentic tool stacks — you are exposed to every package in the full dependency tree, not just what you explicitly install.
- **Treat GitHub issue silence or closure as a potential signal, not resolution** — AI-generated comment floods can manufacture the appearance of noise around a legitimate critical issue and cause maintainers to dismiss it.
- **Do not rely on compliance badges as a proxy for security posture** — SOC 2 and ISO certifications on an open-source project's website require independent verification; "AI-native compliance" tooling is unproven and potentially misleading.
- **Package managers remain a systemic risk** — this is the second attack in this specific ecosystem (Trivy was also targeted). Consider pinning dependencies, using lockfiles, and monitoring for unexpected version changes in CI/CD pipelines.

---

## Notable Quotes

> "This vulnerability treated your tokens like Pokémon. They caught actually all of them."

> "It turns out that little PTH file apparently spawns itself over and over again, accidentally fork-bombing the victim — but it's only on an MCP server. Glorious."

> "Adding friction that I never even came across my mind as possible… all of these comments may have just caused the collaboration between everybody to kind of fall apart. It's really a unique way of just adding friction."

---
