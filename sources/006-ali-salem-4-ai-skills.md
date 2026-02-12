---
source_id: "006"
title: "4 AI Skills That Set You Apart From 90% Of People"
creator: "Ali H. Salem"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=wuOCa50e3fk"
date: "2026-02-07"
duration: "16:33"
type: "video"
tags: ["prompt-engineering", "validation", "ai-landscape"]
curriculum_modules: ["02-prompting-and-workflows"]
---

# 006: 4 AI Skills That Set You Apart From 90% Of People

> **Creator**: Ali H. Salem | **Platform**: YouTube | **Date**: 2026-02-07 | **Duration**: 16:33

## Summary

Ali H. Salem, a director at a tech company, breaks down four practical AI skills that separate power users from everyone else, plus a bonus method for identifying what tasks to automate and what to leave alone. The core thesis is that the best AI users are not smarter or more experienced -- they just have better systems. They build compound output by reusing what works and discarding what does not.

The four skills form a complete system: sticky AI workflows (compounding reuse), prompt engineering (structured communication), AI tool stacking (minimalist tool selection), and a validation framework (reducing hallucination risk). The bonus section provides a three-step process for deciding where to apply AI automation based on pain-point severity and task characteristics.

## Key Concepts

### Skill 1: Sticky AI Workflows

The concept of "sticky AI workflows" means compounding AI enhancement into a repeatable system you actually use day-to-day. Once it sticks, going back to the old way feels more painful than it used to be.

Three core concepts to build sticky AI workflows:

1. **Link documents to chats** -- Copy the link to the AI chat you used and drop it into your working document so you can return to it later. Saves time and frustration of sifting through old chats when you need to recreate something or pick up where you left off.

2. **Build systems to reuse successful prompts:**
   - **Text expanders** -- Assign a short code that expands into a full prompt anytime you type it. Ali uses one called Espanso. Best prompts are always available instantly without copy-pasting or rewriting.
   - **Prompt library** -- Use Notion or even Excel to keep your highest-performing prompts accessible and reusable across tools and projects.

3. **Use Projects in your AI chat** -- ChatGPT and Claude both support "Projects" where every chat uses the same instructions/files and can pull from other chats in the same workspace. This means you stop re-explaining the same background, get more consistent outputs, and can reuse context across multiple chats without bleeding information into unrelated work. (Note: Gemini does not have a true equivalent; Gems are not the same as Projects.)

### Skill 2: Prompt Engineering

A reusable six-step prompting framework that works across ChatGPT, Claude, Gemini, and more:

1. **Role** -- Defines who the model is, who it is speaking to, and the tone. Answers are calibrated immediately. Without it, you get generic, mismatched advice.

2. **Task** -- States the action and the success criteria. The model executes instead of guessing. This is the actual ask you are making.

3. **Context** -- Provides a single source of truth: facts, documents, and background. Keeps responses grounded. When context is missing, models fill gaps with plausible guesses, leading to hallucination.

4. **Examples** -- Shows what good looks like (format, tone, depth). Without examples, outputs vary significantly even with the same ask.

5. **Output** -- Specifies the exact format, length, and structure. Without this, you will likely get a correct but inconveniently formatted output requiring follow-up prompts.

6. **Constraints** -- Sets guardrails on what to avoid and prioritize so the model does not drift. Without constraints, you risk fluff, overreach, and wrong style.

Key insight: Do not set up all six steps every time you prompt (it will be overwhelming). Instead, build and reuse successful prompts via the systems from Skill 1. For simpler tasks where accuracy matters less, a lighter approach is fine. For complex tasks, use the full framework.

### Skill 3: AI Tool Stacking

The common problem: getting lost in the noise of all the AI apps, ending up in analysis paralysis, and sticking only with ChatGPT.

The approach to simplify:

1. **Categorize AI tools into two buckets:**
   - **Generalist AIs** -- ChatGPT, Gemini, Claude
   - **Specialist AIs** -- Gamma (presentations), Lovable (vibe coding), etc.

2. **Follow this process:**
   - Pick the generalist AI you like to work with the most
   - Fit as many use cases into that generalist as possible
   - For use cases that do not make the cut (missing features or unsatisfying output), use your generalist AI to find a specialist AI
   - Try the specialist out; if it works, incorporate it into your stack

3. **Keep your stack small** -- Focus on mastering a small set rather than spreading thin. If you spread yourself thin, you master nothing and never get consistent adoption.

Ali shares his own stack on screen. He notes that even as someone running an AI-focused YouTube channel, his core tool set is quite small. Behind it is a long tail of tools he tests occasionally, but the repeat workflows use a minimal set.

### Skill 4: Validation Framework

Three practical tips to reduce the risk of hallucinations:

**Tip 1: Use tools with strong grounding built in**
- **NotebookLM** -- Built around answering based on sources you provide. Takes more effort but dramatically reduces hallucinations because the model is anchored in real material.
- **Perplexity** -- Goes out and finds information online to support responses by default, making it easier to sanity-check what you are reading instead of just trusting a confident paragraph.

**Tip 2: Use self-evaluation prompts (three techniques)**
1. Ask the AI to score its statements with a confidence level so you can quickly see which parts are shaky and focus your cross-checking energy where it matters.
2. Tell the AI to base answers only on the documents/materials you attach (stops the model from pulling in random guesses).
3. Explicitly give the AI permission to say it does not know. Without this, it will try to be "helpful" by filling in gaps, which is where hallucinations sneak in.

**Tip 3: Cross-check outputs by letting different AIs critique each other's work**
- Example: Create something in ChatGPT, then let Gemini poke holes in it (what looks weak, what sounds made up, what needs sources).
- Analogy: Self-driving cars use redundant systems. One system does the driving, a second completely separate system (built on a different architecture) kicks in if something goes wrong. Using different LLMs to critique each other works the same way -- they do not reason in the exact same way, so you can use those differences to catch issues.

Important caveat: You can never fully eliminate hallucinations because LLMs are probabilistic in nature and no technique today can enforce causality. But these three tips dramatically reduce the risk.

### Bonus: How to Identify What to Automate

A common mistake: expecting AI can automate everything. Using AI for everything actually makes you less effective.

**Three-step process to find your automation candidates:**

**Step 1: Find candidates for automation**
- Break down your day or week into individual tasks (professional or personal)
- Goal: save time or elevate quality of outputs
- Rule of thumb: Anything that is **repeatable**, **digital**, and where you can **clearly describe what good looks like** is a candidate for AI automation
- This does not mean you automate it -- you just map it

**Step 2: Decide if the pain point is high enough**
- If the task is not annoying or tedious enough, you will not adopt the automation
- If you do not feel the pain, you will not adopt the system, and it becomes another thing you set up once and never touch again

**Step 3: Find a way to solve them effectively**
- Start with your generalist AI chat
- If it does not work or you are not happy with the outcome, turn to specialist AIs built for that use case
- Make it sticky: put it in a system that is easy to reuse, add to, and enhance over time (Skill 1)

The result: a holistic approach where you know what to automate, what not to automate, which tools to use, which tools not to use, and how to incorporate changes into your actual workflows. You are not just experimenting -- you are compounding.

## Practical Takeaways

- **Build sticky systems, not one-off prompts**: Link chats to documents, use text expanders, maintain a prompt library, and use AI Projects to compound your effectiveness over time.
- **Use the 6-step prompting framework for high-stakes tasks**: Role, Task, Context, Examples, Output, Constraints -- but do not apply the full framework to every interaction; calibrate effort to task importance.
- **Keep your AI tool stack minimal**: Pick one generalist, fit as many use cases as possible, only add specialists when the generalist falls short.
- **Layer validation techniques**: Use grounded tools (NotebookLM, Perplexity), self-evaluation prompts (confidence scoring, source restriction, permission to say "I don't know"), and cross-model critique.
- **Automate selectively**: Only automate tasks that are repeatable, digital, clearly definable, and painful enough that you will actually adopt the automation.

## Notable Quotes

> "The absolute best users of AI aren't necessarily smarter or more experienced. They just have better systems." -- Ali H. Salem

> "If you spread yourself thin, you will master nothing and you will never get consistent adoption of these tools in your day-to-day." -- Ali H. Salem

> "You never fully get rid of hallucinations because LLMs are probabilistic in nature and no technique today can enforce causality." -- Ali H. Salem

## Related Sources

- [007: Super Bowl Commercial Bubble Curse: AIs Imitate Dot-Coms](007-internet-of-bugs-ai-bubble.md) -- Broader AI landscape context
- [008: The Capability Overhang](008-nate-b-jones-phase-transition.md) -- How power user patterns differ from average usage

## Related Curriculum

- [Module 02: Prompting and Workflows](../curriculum/02-prompting-and-workflows/README.md) -- Prompt engineering framework and workflow systems directly applicable
