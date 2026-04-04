---
source_id: "482"
title: "I can’t believe they put ads there"
creator: "The PrimeTime"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=UwJp5xm1MNc"
date: "2026-04-03"
duration: "7:15"
type: "video"
tags: ["ai-hype", "enterprise-ai", "ai-landscape", "security"]
curriculum_modules: ["01-foundations", "06-strategy-and-economics"]
---

# 482: I can’t believe they put ads there

> **Creator**: The PrimeTime | **Platform**: YouTube | **Date**: 2026-04-03 | **Duration**: 7:15

# I Can't Believe They Put Ads There

## Summary

Microsoft Copilot briefly injected promotional content into GitHub pull request descriptions, affecting approximately 11,400 PRs before being pulled within hours of discovery. The content advertised Raycast—a third-party launcher app with a Microsoft partnership—framed internally as a "product tip" about Copilot's Raycast integration. Microsoft's official explanation was that the tips were intended as helpful feature suggestions but "surfaced more frequently than intended," though Prime is skeptical this was accidental rather than a deliberate experiment in AI-assisted promotion.

The incident sits within a broader pattern Prime identifies at GitHub post-Microsoft acquisition: a platform suffering significant reliability problems (90 incidents in 90 days, ~90.84% uptime) while leadership redirects engineering focus toward AI feature adoption metrics. The argument is that GitHub's reliability issues are being deprioritized because the incentive structure rewards Copilot adoption numbers—a VP's bonus is tied to AI adoption, not uptime—rather than core platform quality.

Prime frames this as emblematic of Microsoft's strategic repositioning of GitHub: not primarily as a developer collaboration platform, but as an AI product distribution channel. The ad injection incident, however brief, crystallized this tension—developers using a platform built for them found AI features inserting commercial content into their work artifacts without consent.

## Key Concepts

### AI Platform Capture of Developer Infrastructure

GitHub is being operated less as a developer-first coding platform and more as a vehicle for Microsoft's AI product distribution. When a platform designed for developers begins injecting promotional content into core work artifacts (pull requests), it signals that developer experience is subordinate to AI adoption KPIs. This pattern—legacy platform repurposed as AI distribution channel—is a meaningful structural risk for any critical dev infrastructure owned by an AI-first company.

### Incentive Misalignment in Enterprise AI Adoption

The underlying mechanism Prime identifies is straightforward: organizational incentives reward AI adoption metrics over platform reliability. A VP gets a "seven-figure bonus" for Copilot usage numbers; nobody gets rewarded at the same scale for reducing incident count. This creates systematic deprioritization of foundational quality in favor of visible AI feature velocity—a pattern likely present across many enterprise AI deployments, not just GitHub.

### Consent and Context in AI-Assisted Workflows

Even setting aside the commercial dimension, Copilot editing PR *descriptions* (not just code) without explicit instruction to do so represents a meaningful boundary violation. When an AI agent modifies the communicative artifacts surrounding work—not just the work itself—it raises questions about where agent authority should begin and end. Developers expect AI assistance on code; finding AI-inserted promotional text in their documentation is a qualitatively different experience.

### Platform Trust and Reliability Debt

GitHub's 90-incident-in-90-days figure illustrates how reliability debt accumulates when it isn't treated as the primary metric. Prime's framing—"you can't go a day or two without seeing a unicorn"—points to a UX degradation that erodes the low-friction trustworthiness that made GitHub dominant. Trust in developer tooling is slow to build and fast to destroy; reliability incidents compound reputationally.

## Practical Takeaways

- **Audit what your AI tools touch:** Copilot modified PR descriptions—not code—without explicit instruction. Know precisely which artifacts your AI coding tools have write access to, and consider restricting agent scope to code changes only.
- **Treat AI-modified artifacts with provenance awareness:** If Copilot or similar tools can edit shared team documents (PRs, wikis, commit messages), establish team norms about what AI modification looks like vs. human authorship so reviewers aren't surprised.
- **Watch for incentive-driven feature injection in vendor tooling:** When an AI vendor also owns the platform (GitHub + Copilot, VS Code + Copilot), be alert to features that serve vendor adoption metrics rather than developer needs—these can arrive silently via updates.
- **Platform reliability should be a first-order selection criterion for critical infrastructure:** Uptime and incident rates for platforms like GitHub are now trackable. Factor reliability history into decisions about which platforms and tools anchor your development workflow.
- **Skepticism about "it was just a tip" framing is warranted:** When AI-injected content includes third-party commercial links and reads like marketing copy, the "accidental surfacing" explanation deserves scrutiny regardless of what the vendor says.

## Notable Quotes

> "Microsoft Co-Pilot is now injecting ads into pull requests on GitHub. If this does not send a shiver down your spine, you have no soul, my friend."

> "This pro tip was really just a means to increase more co-pilot usage such that some VP somewhere can get that pat on the back and that big seven-figure bonus for making the company's bottom line get bigger because they're doing what the company needs more of, which is AI adoption instead of just doing what everybody actually wants them to do."

> "The reason why GitHub is under the core AI of Microsoft is because it's not going to be a coding platform, it is an AI platform."
