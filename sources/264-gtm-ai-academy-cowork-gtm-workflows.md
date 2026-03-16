---
source_id: "264"
title: "The Cowork GTM Playbook: 3 Claude Cowork Workflows to supercharge your revenue team"
creator: "GTM AI Academy "
platform: "YouTube"
url: "https://www.youtube.com/watch?v=lDdzEtb0Z8o"
date: "2026-03-12"
duration: "50:11"
type: "video"
tags: ["skills", "multi-agent", "prompt-engineering", "agent-teams", "enterprise-ai"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns", "05-team-orchestration"]
---

# 264: The Cowork GTM Playbook: 3 Claude Cowork Workflows to supercharge your revenue team

> **Creator**: GTM AI Academy  | **Platform**: YouTube | **Date**: 2026-03-12 | **Duration**: 50:11

# The Cowork GTM Playbook: 3 Claude Cowork Workflows to Supercharge Your Revenue Team

## Summary

Victor Jeffri, a go-to-market enablement veteran with 15+ years of experience, demonstrates three agentic workflows using Claude's Cowork platform for B2B sales and GTM tasks. The core thesis is that Claude Cowork — released approximately six weeks before recording — represents a meaningful shift from chatbot-style AI interaction to true agentic execution: you define a goal, provide instructions, and the system acts on your computer, files, and folders autonomously. Victor argues that enablement professionals are uniquely positioned to leverage this because their existing skill of defining "what good looks like" translates directly into high-quality AI instructions.

The three workflows covered are: (1) intelligent lead research and prioritization from a raw prospect list, (2) mass call analysis across large volumes of recorded calls, and (3) creating Make (Integromat) automations using Cowork. The lead research demo shows Cowork reading an Excel file of ~360 conference leads, asking clarifying questions, then spawning parallel sub-agents to research multiple companies simultaneously — returning scored, prioritized leads with personalized outreach emails. The architecture relies heavily on pre-built Skills (reusable instruction packages) and Projects (knowledge bases with reference files) to keep prompts concise while delivering rich, consistent outputs.

A recurring theme is the compounding value of foundational enablement knowledge: the same frameworks Victor used to train human SDRs — how to research a prospect, how to structure a personalized email, what an ideal customer profile looks like — are now encoded directly into Skills and prompts, making AI outputs reliably high-quality rather than generically mediocre.

## Key Concepts

### Claude Cowork as an Agentic Platform
Cowork is Anthropic's computer-use agentic layer, positioned between conversational Claude and the developer-facing Claude Code CLI. It borrows Claude Code's multi-agent architecture but exposes it through a GUI rather than a command line. The key capability is taking actions on a local computer: reading and writing files and folders, opening documents, and orchestrating sub-agents — making it practical for non-technical GTM professionals to run agentic workflows without coding.

### Skills as Reusable Instruction Packages
Skills in Cowork function similarly to Custom GPTs but are designed to be stacked and composed more easily within agentic workflows. A Skill encodes the *how-to* for a specific task — in the lead research example, the skill contains detailed instructions on what to research about a prospect, what questions to answer, how to score fit, and what output format to produce. By packaging domain expertise into Skills, users can write simple, short prompts at execution time while the Skill supplies the depth. Reference files (e.g., ICP scoring rubrics, case studies) are attached to Skills to ground outputs further.

### Parallel Sub-Agents for Scale
A recently released Cowork capability allows the orchestrator to spawn multiple sub-agents running simultaneously rather than sequentially. In the demo, rather than researching 15 companies one by one, Cowork dispatches parallel agents to research all 15 at once. This dramatically reduces wall-clock time on research-heavy tasks and is a meaningful practical differentiator over single-threaded LLM conversations.

### Projects as Persistent Knowledge Bases
Projects in Cowork store a curated collection of reference materials — writing samples, offers, case studies, brand voice guidelines — that agents can draw from during execution. This allows personalization at scale: the lead research workflow pulls from Victor's actual email examples and content assets stored in an "active lead nurture bot" project, so personalized outreach emails reflect his authentic style and real offers rather than generic AI-generated copy.

### Enablement Expertise as Prompt Foundation
Victor argues that go-to-market enablement professionals have a structural advantage in AI adoption because their core competency — defining good performance, writing step-by-step playbooks, creating rubrics — maps directly onto what makes AI prompts and Skills effective. The same ICP criteria, email structure frameworks, and call scoring rubrics that were once written for human training now serve as AI instructions, with the benefit that AI follows them more consistently.

## Practical Takeaways

- **Invest in Skills before scaling usage.** The quality of agentic outputs is largely determined by how well the underlying Skill is built. Spend time encoding your domain expertise (ICP definition, scoring rubrics, output templates) into Skills rather than writing long prompts ad hoc each time.
- **Use Projects to inject brand-authentic materials.** Attaching real writing samples, case studies, and offer documents to a Project gives the agent enough context to produce personalized, on-brand outputs without manual editing — critical for outbound at scale.
- **Let Cowork ask clarifying questions before acting.** Victor highlights the value of the system pausing to ask "which category should I prioritize?" before executing. Design your workflows to allow for a clarification loop rather than fully automating past it — this catches assumptions early and improves output quality.
- **Treat simple prompts as a feature, not a shortcut.** When Skills and Projects are well-built, your execution prompt can be just a few sentences. Resist the temptation to over-prompt at execution time; the complexity should live in the reusable infrastructure.
- **Map your existing training materials directly into AI instructions.** If you have written playbooks, call scorecards, or email frameworks for human training, those documents are ready-made Skill content. Start there rather than prompting from scratch.

## Notable Quotes

> "What makes AI work well is understanding what good looks like — and that has come through the enablement training foundation. The same training that I used to give to humans and hope that they remember and implement it — now I give the same training to AI and it's a little bit more reliable in doing the right thing."

> "It's not 'let's have a conversation back and forth.' It's 'here's my goal, here's a bunch of instructions, execute on it, do it for me as opposed to me doing it myself.' That really crystallized the agent thing for me."

> "Even though I just wrote a couple of sentences, I've actually given it a ton of information about what I want — because it has access to the skill on prospect research and the project folder. If I didn't have that, I would have to write a gigantic prompt."
