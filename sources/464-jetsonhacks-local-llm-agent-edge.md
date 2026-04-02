---
source_id: "464"
title: "First Look: NemoClaw on Jetson with a Local LLM"
creator: "JetsonHacks"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=7HQSFgP6vOE"
date: "2026-03-20"
duration: "14:34"
type: "video"
tags: ["security", "infrastructure", "agentic-coding", "multi-agent"]
curriculum_modules: ["04-agentic-patterns", "06-strategy-and-economics"]
---

# 464: First Look: NemoClaw on Jetson with a Local LLM

> **Creator**: JetsonHacks | **Platform**: YouTube | **Date**: 2026-03-20 | **Duration**: 14:34

# First Look: NemoClaw on Jetson with a Local LLM

## Summary

This video demonstrates running NemoClaw — NVIDIA's containerized wrapper around OpenClaw (described as the most popular open-source project in history) — on a Jetson AGX Thor edge device with a locally hosted LLM. The presenter walks through a deceptively difficult installation process, requiring five distinct fixes to kernel modules, networking configuration, IPv6 routing, and container resource access before OpenShell (NVIDIA's agent container manager) would function correctly on Jetson. The demo uses Mistral's Neatron 3 Nano 3B model served via vLLM inside Docker, with NemoClaw providing the agent interface on top.

Beyond the installation walkthrough, the video makes a substantive argument about AI agent security. OpenClaw agents operate with real system-level authority, and the presenter demonstrates how prompt injection — untrusted input masquerading as authority — can cause an agent to execute malicious commands. NemoClaw's containerization mitigates part of this risk but does not eliminate it. The closing remarks frame this tension directly: the risks of agentic systems are real, the opportunities are real, and the correct response is to build carefully rather than ignore either side.

The video is practically useful as a reference for anyone deploying local LLM agent infrastructure on ARM/edge hardware, and conceptually useful as a grounded illustration of why agent sandboxing and policy controls matter in production agentic systems.

---

## Key Concepts

### OpenShell and Container-Based Agent Management
NVIDIA's OpenShell is a container manager purpose-built for AI agent workloads. It enforces resource access policies per sandbox, logs rules and policy decisions, and provides the runtime environment in which OpenClaw agents operate. Getting it running on non-standard hardware (Jetson Thor) required patching kernel modules, reconfiguring bridge networking, disabling broken IPv6 paths, and adjusting container resource controls — a reminder that "one-liner install" claims rarely survive contact with edge hardware.

### Local LLM Serving with vLLM on Edge
The demo serves Neatron 3 Nano (a 3B reasoning model, ~19 GB) via vLLM inside a Docker container, with vLLM itself weighing in at ~35 GB — totaling roughly 55 GB on first download. The model's reasoning mode can be toggled via `kw_args` at server start. This setup represents a fully local inference stack: no cloud API calls, no external data leaving the device, with the trade-off of significant storage and a ~1-minute cold-start latency on the first request.

### Prompt Injection as a First-Class Agent Security Threat
The presenter demonstrates a concrete prompt injection attack: an agent passed unsanitized input to a system call, enabling command injection that caused a boot loop. In agentic contexts, this is categorically more dangerous than in traditional applications because the agent acts with real system authority. The key framing: *capability is not authority* — the fact that an agent can execute a command does not mean it has been granted permission to do so by the user.

### Policy Presets and Sandboxing as Partial Mitigations
NemoClaw's containerization and OpenShell's policy system reduce (but do not eliminate) the attack surface. During setup, users select policy presets governing what resources agents can access. Some requests are denied at the policy layer; others pass. This is meaningful defense-in-depth but the presenter is explicit that containment is partial — a contained agent can still do damage within its permitted scope if it receives malicious instructions.

### Agent Systems: Responsibility Follows Authority
The video closes with a philosophical framing that has practical implications: when an agent acts in your name, your reputation goes with it. Long-running agentic systems also accumulate state and can "fail by remembering badly" — a subtler failure mode than simple amnesia. The implication for builders: deploying an agent is not just a technical act but an accountability decision.

---

## Practical Takeaways

- **Don't trust one-liner installs on edge hardware.** Even NVIDIA's own tooling required five distinct kernel/networking fixes on Jetson Thor before it would run. Budget time for platform-specific debugging when deploying agent infrastructure outside standard x86 cloud environments.
- **Toggle reasoning mode explicitly at the server level when using reasoning models.** Neatron 3's reasoning behavior is controlled via vLLM `kw_args` at container start — there's no reliable in-prompt toggle. Run separate server configurations for reasoning-on vs. reasoning-off use cases.
- **Treat prompt injection as a systems security problem, not a prompt hygiene problem.** The demo shows that unsanitized inputs passed to system-adjacent agents can cause real damage. Containment (NemoClaw's approach) is the right architectural response, not just better prompts.
- **Plan for ~55 GB of storage for a modest local agent stack.** vLLM (~35 GB) plus a 3B model (~19 GB) is the floor for this kind of deployment. Larger models scale this significantly. Edge devices need to be sized accordingly.
- **Audit policy presets before deploying agents with external-facing inputs.** OpenShell's policy layer is the primary defense after containment. Review which resource access requests are permitted vs. denied for your specific agent use case before going live.

---

## Notable Quotes

> "Without containment, a system should be treated as unable to keep secrets. Privacy is not a feature you declare. It is a boundary you enforce."

> "Capability is not authority. Prompt injection is untrusted input pretending to be authority."

> "The machine bears the action, but you bear the responsibility. If the machine acts in your name, your reputation goes with it."

---
