---
source_id: "256"
title: "Github might be in trouble"
creator: "The PrimeTime"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=f3u57jkwBFE"
date: "2026-03-09"
duration: "09:07"
type: "video"
tags: ["ai-landscape", "ai-hype", "agentic-coding", "infrastructure"]
curriculum_modules: ["01-foundations", "06-strategy-and-economics"]
---

# 256: Github might be in trouble

> **Creator**: The PrimeTime | **Platform**: YouTube | **Date**: 2026-03-09 | **Duration**: 09:07

## Summary

ThePrimeagen offers a bold prediction: version control is about to undergo a transformation bigger and faster than the shift from SVN to Git, and GitHub may be one of the first major developer tools to be radically disrupted by the AI revolution. The catalyst is OpenAI reportedly developing an internal alternative to GitHub, but Prime's argument extends well beyond that single data point.

The core thesis is that AI-powered coding tools (Codex, Cursor/Anysphere) are naturally positioned to build version control systems that are transparent to agents, abstracting away the complexity that git currently imposes. As new developers enter through AI-assisted tools, they will care about persistence and rollback capabilities but not about which platform hosts their code. GitHub's moat, he argues, is weaker than it appears because the next generation of developers has no loyalty to it.

Prime acknowledges he will personally continue using GitHub and recommends learning Git, but frames the current moment as an "extended period of weird tumultuous change" where two islands of developers will emerge: those fully enclosed in walled-garden AI ecosystems and those who maintain deep understanding of their tools while selectively using AI assistance.

## Key Concepts

### Version Control Is Ripe for Disruption

Prime predicts version control will change more dramatically in the next few years than the SVN-to-Git transition. Git is only about 20 years old, and its file-system-centric design reflects an era before AI agents. The combination of new AI-native developers who need version control but have no attachment to Git's workflow, plus AI companies seeking to build closed ecosystems, creates conditions for rapid change ([02:14](https://www.youtube.com/watch?v=f3u57jkwBFE&t=134)).

### Agent-Transparent Version Control

The key architectural insight is that AI coding tools like Codex and Cursor are positioned to create version control systems that are "effectively transparent to agent changes" ([05:07](https://www.youtube.com/watch?v=f3u57jkwBFE&t=307)). Agents would make commits automatically with every change, and users could walk through those changes, roll back, and restart from any point without needing to understand Git internals. This maps closely to how jj (Jujutsu) already operates.

### JJ as the Agent-Native VCS

Prime highlights jj (Jujutsu) as an excellent alignment with how agents operate: automatic change tracking, superior diffs, and a workflow model that matches the agent pattern of continuous small changes with rollback capability ([05:37](https://www.youtube.com/watch?v=f3u57jkwBFE&t=337)). He is impressed by JJ's diff presentation and notes this aligns naturally with agentic workflows despite never having used it personally.

### Cursor's Graphite Acquisition as Leading Indicator

When Cursor acquired Graphite (a stacked-diff tool), Prime expected this to signal the beginning of version control disruption. Graphite offered a "material approach to stacked diffs" that smoothed team collaboration with Git. While that acquisition has not yet produced the expected VCS revolution, it shows AI companies are already thinking about owning the version control layer ([06:29](https://www.youtube.com/watch?v=f3u57jkwBFE&t=389)).

### GitHub's Weak Moat

Prime argues GitHub does not have a stranglehold on developers. The next generation of builders coming through AI tools does not care whether code is on GitHub, GitLab, or elsewhere. They want their work to persist, nothing more. Meanwhile, AI companies have a powerful incentive to own the full development stack: capturing prompts, generated code, production releases, and quality signals as training data ([06:09](https://www.youtube.com/watch?v=f3u57jkwBFE&t=369)).

### The Two-Island Developer Future

Prime envisions two populations emerging: (1) developers fully enclosed in walled-garden AI ecosystems like Cursor, who develop, test, commit, and deploy without understanding the underlying systems, and (2) "artisanal" developers who maintain deep understanding of how computers work, mixing AI-assisted and manual coding while staying in control. The first group will be vastly larger but dependent; the second will be smaller but autonomous ([08:22](https://www.youtube.com/watch?v=f3u57jkwBFE&t=502)).

## Practical Takeaways

- **Learn Git now, but watch the alternatives**: Git remains essential today, but teams should track agent-native VCS alternatives like jj/Jujutsu that may become the next standard.
- **Evaluate AI tool lock-in risks**: As AI coding platforms build integrated version control, teams should assess how much of their workflow is portable versus locked into a single vendor.
- **Version control transparency matters for AI workflows**: When agents make frequent small changes, the VCS needs to support granular rollback without imposing cognitive overhead on the developer.
- **GitHub's value is social, not technical**: The moat is the developer network and open-source community, not the Git hosting itself. Any disruptor needs to match the social layer, not just the storage layer.

## Notable Quotes

> "I think version control is going to change a huge amount over the course of the next few years and I think it's going to be a bigger and faster change than it was from tortoise SVN to git." — The PrimeTime ([02:15](https://www.youtube.com/watch?v=f3u57jkwBFE&t=135))

> "These companies that are developing these tools such as Codex with OpenAI or really Cursor with Anysphere, to me it's like they're the ones that are truly positioned to just create version control systems that are effectively transparent to agent changes." — The PrimeTime ([04:53](https://www.youtube.com/watch?v=f3u57jkwBFE&t=293))

> "I don't think GitHub has some sort of stranglehold on developers. I don't think it really matters to this next generation of people coming in who are trying to develop software." — The PrimeTime ([06:09](https://www.youtube.com/watch?v=f3u57jkwBFE&t=369))

> "Giants in which I never thought would change such as GitHub I now foresee as one of the first things to actually get radically reduced in this AI revolution." — The PrimeTime ([07:07](https://www.youtube.com/watch?v=f3u57jkwBFE&t=427))

## Related Sources

- [027: Devs can no longer avoid learning Git worktree](027-joshua-morony-git-worktree.md) — Complementary view on evolving Git workflows for agentic development
- [137: I'm using claude --worktree for everything now](137-matt-pocock-worktree-workflow.md) — Agent-driven Git worktree usage as a stepping stone toward VCS abstraction
- [097: OpenAI Just Lost Its Biggest Partner](097-yongyea-openai-microsoft-split.md) — Context on the OpenAI-Microsoft relationship that makes OpenAI building a GitHub alternative plausible
- [199: Cloudflare's AI-Generated Next.js Fork](199-primetime-cloudflare-nextjs-fork-open-source.md) — Another PrimeTime analysis of AI disrupting established developer infrastructure
- [069: GitHub Agentic Workflows](069-eddie-aftandilian-agentic-ai-copilot.md) — GitHub's own vision for agent-centric development infrastructure

## Related Curriculum

- [Module 01: Foundations](../curriculum/01-foundations/README.md) — AI landscape shifts and platform disruption dynamics
- [Module 06: Strategy and Economics](../curriculum/06-strategy-and-economics/README.md) — Infrastructure economics, vendor lock-in risks, and the AI-driven SDLC transformation
