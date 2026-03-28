---
source_id: "396"
title: "this is crazy."
creator: "Low Level"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=uwSjgv4otAk"
date: "2026-03-25"
duration: "11:11"
type: "video"
tags: ["security", "ai-sdlc", "enterprise-ai"]
curriculum_modules: ["06-strategy-and-economics"]
---

# 396: this is crazy.

> **Creator**: Low Level | **Platform**: YouTube | **Date**: 2026-03-25 | **Duration**: 11:11

# this is crazy. — LiteLLM Supply Chain Attack via Trivy Compromise

## Summary

This video dissects the LiteLLM supply chain attack of early 2026, in which a cascading compromise touched users including Stripe, Netflix, OpenAI, and Google. LiteLLM is a popular Python adapter library that provides a unified interface (`completion()`) over heterogeneous LLM APIs (OpenAI, Anthropic, Gemini, etc.), making it widely embedded in production AI infrastructure. The attack vector was not a direct breach of LiteLLM itself, but rather a poisoned security tool that the maintainer was using in good faith.

The chain began with a misconfigured GitHub Actions workflow in the Trivy security scanner repository. An AI-powered autonomous agent (OpenClaw/Hackerbot Claw) exploited a `pull_request_target` workflow misconfiguration to steal a privileged personal access token, then used it to force-push malicious commits onto 75 of 76 version tags in the Trivy Action repo. Because LiteLLM's CI pipeline ran Trivy as a GitHub Action pinned to a mutable tag, the maintainer's credentials were exposed to the now-malicious Trivy code. Attackers used the harvested token to push two compromised LiteLLM versions (1.8.27 and 1.8.28) to PyPI, the second of which executed malware at `pip install` time—no explicit invocation required.

The malware collected an extensive payload: hostnames, environment variables, running processes, SSH private keys, `.env` files, git credentials, API keys, shell history, Slack/Discord tokens, and CI/CD configuration. The creator candidly admits there is no clean remediation playbook here: the structural vulnerabilities—mutable tags, broad personal access tokens, `pull_request_target` misuse—are endemic to the open-source supply chain ecosystem, and the incident was partly a follow-on operation enabled by incomplete credential rotation after an earlier compromise.

---

## Key Concepts

### Supply Chain Attacks via Transitive Dependencies
A supply chain attack does not need to target your code directly. By compromising a widely-trusted tool (here, a security scanner), an attacker can poison every downstream project that depends on it. LiteLLM's maintainer did nothing wrong in intent—they used a reputable security tool—yet their users were compromised because that tool's distribution was corrupted upstream. The blast radius scales with how many projects depend on the poisoned artifact.

### `pull_request_target` vs. `pull_request` in GitHub Actions
Standard `pull_request` workflows run in the *source* branch's context using the contributor's limited credentials. `pull_request_target`, added in August 2020, runs in the *target* branch's context—meaning it has access to the target repo's secrets and tokens. When a project exposes `pull_request_target` to external contributors without strict protections, any attacker can submit a PR and execute arbitrary code with elevated privileges. Trivy's repository had this misconfiguration, which was the initial foothold.

### Mutable Git Tags as a Security Liability
A git commit hash is immutable—once created, it cannot be changed. A tag, however, is a mutable pointer. Pinning a dependency to a tag like `v0.69.4` rather than a specific commit SHA means the tag can silently be redirected to a malicious commit by anyone who controls the repository or its tokens. The attackers force-pushed 75 of 76 Trivy Action tags to point to compromised commits, making every CI pipeline using those tag references immediately vulnerable without any visible change on the consumer side.

### Malware Execution at Install Time (`setup.py` / `pyproject.toml`)
Python package installation via `pip` can execute arbitrary code through `setup.py` or build hooks. LiteLLM version 1.8.28 embedded malware in the file executed during the installation process itself—meaning merely running `pip install litellm==1.8.28` triggered the credential-harvesting payload without any subsequent use of the library. This is a well-known but underappreciated attack surface in the Python ecosystem.

### AI-Powered Autonomous Attack Agents
The initial Trivy compromise was attributed to "Hackerbot Claw," described as an AI-powered autonomous agent that scanned for and exploited the `pull_request_target` misconfiguration programmatically. This is a live example of agentic AI being deployed offensively at scale—automatically identifying misconfigured repositories and executing multi-step exploitation chains (token theft → tag hijacking → downstream poisoning) with minimal human intervention. The creator notes this is the same OpenClaw tooling Jensen Huang had recently been promoting.

---

## Practical Takeaways

- **Pin dependencies to commit SHAs, not mutable tags.** In GitHub Actions and package manifests alike, use immutable commit hashes rather than version tags. A tag can be silently redirected; a hash cannot.
- **Never use `pull_request_target` for workflows that access secrets unless you have ironclad controls** (e.g., manual approval gates, no checkout of PR code). The default mental model most developers have of CI permissions does not apply to this event type.
- **Rotate credentials aggressively and completely after any compromise.** Part of why this attack succeeded as a follow-on operation is that credentials from an earlier breach were not fully invalidated. Treat every token as compromised and roll all of them, not just the ones you think were exposed.
- **Scope personal access tokens to the minimum necessary permissions** and prefer short-lived tokens (OIDC/workload identity) over long-lived PATs for CI/CD workflows. A stolen scoped token limits blast radius.
- **Treat security tooling itself as part of your attack surface.** Integrating a scanner, linter, or formatter via a GitHub Action or pip package introduces transitive trust. Audit the supply chain of your supply chain tooling—at minimum, check that you're pinning to a hash and that the tool's own CI is not `pull_request_target`-exposed.

---

## Notable Quotes

> "I need to highlight the irony, the tragedy, just the insanity behind the fact that Light LLM was compromised because the maintainer of Light LLM used a security tool."

> "By pip installing LiteLLM 1828, you triggered the malware. It executed. It ran."

> "When it comes to this world—the GitHub Actions, Python repos, node npm, supply chain compromise situation—I literally have no idea what to do. I think one of the answers is just like delete all the passwords."

---
