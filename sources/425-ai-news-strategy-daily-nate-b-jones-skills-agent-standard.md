---
source_id: "425"
title: "Anthropic, OpenAI, and Microsoft Just Agreed on One File Format. It Changes Everything."
creator: "AI News & Strategy Daily | Nate B Jones"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=0cVuMHaYEHE"
date: "2026-03-30"
duration: "26:19"
type: "video"
tags: ["skills", "agent-teams", "multi-agent", "enterprise-ai", "context-engineering", "prompt-engineering", "skills-ecosystem"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns", "05-team-orchestration"]
---

# 425: Anthropic, OpenAI, and Microsoft Just Agreed on One File Format. It Changes Everything.

> **Creator**: AI News & Strategy Daily | Nate B Jones | **Platform**: YouTube | **Date**: 2026-03-30 | **Duration**: 26:19

## Summary

Nate B Jones provides a six-month retrospective on Claude's skills system, arguing that what launched in October 2025 as a personal productivity feature has matured into organizational infrastructure and an open cross-industry standard. The core thesis is that Anthropic, Microsoft (Copilot), and OpenAI have converged on skills-as-markdown as a shared format, meaning skills now function as a portable context layer that works identically across Claude, ChatGPT, Copilot, Excel, and PowerPoint. This convergence fundamentally changes the calculus: skills are worth investing in because the ecosystem now has gravity.

The video's most important shift is the change in *caller*: skills were primarily human-invoked in October, but agents now account for the majority of skill calls because a single agent run can make hundreds of invocations. This reframes how skills should be authored — they must be designed agent-first, with highly precise trigger descriptions, explicit reasoning frameworks (not just linear steps), and lean file sizes to avoid context bloat. The failure modes are also different in agentic contexts: humans can catch drift mid-conversation, but agents will silently compound errors across hundreds of calls before anyone notices.

The video closes with a community-oriented argument: best practices for skills are *discoverable*, not pre-known, so open sharing accelerates collective learning faster than closed hoarding. Jones announces a community skills repository and draws an analogy to the compounding value of skills versus prompts — prompts are one-time uses while skills accumulate refinement over time, making early adopters who invest in skill-building increasingly difficult to match.

---

## Key Concepts

### Skills as Organizational Infrastructure (Not Personal Config)
The shift from individual to organizational deployment is structural: enterprise and team admins now roll out skills workspace-wide as versioned, single-upload packages available across the entire Microsoft/Anthropic toolchain. The methodology of an organization — previously held in people's heads — can now live in a repository. This also has a human onboarding benefit: new team members can read the skill files to understand processes, not just use them as agent inputs.

### Agent-First Skill Design
Because agents can make hundreds of skill calls in a single run, the majority of skill invocations are now non-human. This means skill authors must optimize for agent readability and reliable triggering rather than human UX. The practical implication is that the **description field is the most critical component** — Anthropic's own guidance notes that skills tend to *under*-trigger rather than over-trigger, so descriptions should be written to be "pushy," including specific artifact types, trigger phrases, and expected output shapes. A key technical constraint: the description must remain on a single line or Claude will silently drop everything after the first line break.

### The Skill Construction Formula
A well-formed skill has five components in the methodology body: (1) **reasoning frameworks**, not just linear steps — brittle skills break on unrecognized edge cases while reasoning enables generalization; (2) **specified output format** with exact fields or structure; (3) **explicit edge cases** that a human would handle through common sense; (4) **a worked example** so the model can pattern-match against "what good looks like"; (5) **leanness** — 100–150 lines maximum in the core file, with ~80% of attention on the description and the remainder on general reasoning. A short skill that fires reliably beats a long skill with competing instructions.

### Skills Compound; Prompts Don't
Prompts are consumed and discarded. Skills are iteratively refined — you can update a skill file based on output failures and those improvements persist across every future invocation, by any caller (human or agent). People who have been building and refining skills for six months now have a compounding advantage over people who have been re-prompting from scratch. The analogy used: prompts are the basic 4×4 Lego brick; skills are the specialized pieces that let you build something complex.

### Open Standard Dynamics and Alpha in the AI Age
The convergence on skills-as-markdown as an open standard inverts the usual closed-source intuition. Because best practices are *discovered* rather than pre-known, open sharing accelerates learning for everyone and the person sharing gets reputation/talent-signaling value. Jones draws an explicit parallel to open-source AI projects functioning as developer resumes that attract acqui-hire offers. The community trading skills "like baseball cards" is framed as the optimal learning strategy given that no one has the instruction manual yet.

---

## Practical Takeaways

- **Audit your description fields first.** Most skills fail because the description is too vague to trigger reliably. Rewrite descriptions to include specific document/artifact types, exact trigger phrases, and a statement of expected output format — all on a single unbroken line.
- **Design for agent callers, not human callers.** Assume your skill will be invoked hundreds of times in an automated run. Failures will compound silently. Prioritize deterministic triggering and unambiguous output specs over conversational flexibility.
- **Keep skill files lean.** Target ≤150 lines in the core `skill.md` file. Put examples in separate files within the folder. Competing or redundant instructions degrade performance more than they help.
- **Build the orchestrator pattern.** For complex workflows, create a top-level orchestrator skill that analyzes incoming requests and routes to specialist sub-skills (research, coding, docs, UI). This makes multi-step agentic work predictable without requiring per-task human direction.
- **Start a versioned skills repository now.** Treat skills as organizational infrastructure: version-control them, document them like code, and share them internally so methodology lives in the repo rather than in individuals' heads.

---

## Notable Quotes

> "Skills compound for you. Skills compound by the weight of industry investment in the ecosystem and by the weight of your own commitment to having a predictable pattern for doing something and writing it down. Prompts don't compound in the same way."

> "The methodology doesn't live in someone's mind anymore. It lives in a repository."

> "The best practices are discoverable, not known... we all discover the instruction book together. And that goes for how we use them with tools and skills as well. It works faster if we discover it in a community."

---
