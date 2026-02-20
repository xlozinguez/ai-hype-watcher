---
source_id: "084"
title: "This Simple 60% Rule Stops Context Rot in ChatGPT, Claude & Gemini"
creator: "Dylan Davis"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=xaQG-eD9d58"
date: "2026-01-17"
duration: "17:49"
type: "video"
tags: ["context-engineering", "prompt-engineering", "chatgpt"]
curriculum_modules: ["02-prompting-and-workflows", "03-claude-code-essentials"]
---

# 084: This Simple 60% Rule Stops Context Rot in ChatGPT, Claude & Gemini

> **Creator**: Dylan Davis | **Platform**: YouTube | **Date**: 2026-01-17 | **Duration**: 17:49

## Summary

Dylan Davis explains the phenomenon of "context rot" -- the progressive degradation of AI performance as conversations grow longer and fill up the model's context window. He introduces the "60% rule": once you've used approximately 60% of a model's context window, performance starts to degrade noticeably, and by 95% it degrades rapidly. The video provides a practical mental model (the whiteboard analogy), concrete warning signs to watch for, and four tactical countermeasures.

The core insight is that most users treat AI conversations as unlimited, not realizing that every message (input, output, file attachments, and the model's thinking process) accumulates in a fixed-size memory. Davis frames context windows across the three major consumer platforms: ChatGPT (~60K tokens in UI, despite 400K API limit), Claude (~200K tokens), and Gemini (~1M tokens). He offers four tactics: (1) handoff summaries to fresh conversations, (2) strategic file management to minimize token waste, (3) experimentation to build intuition about task complexity limits, and (4) proactive in-thread summaries every 5-15 exchanges for users unwilling to start new conversations.

## Key Concepts

### The 60% Rule

Context window performance follows a degradation curve, not a cliff. Up to ~60% capacity, the AI maintains effective instruction-following. Between 60-95%, performance degrades progressively. Past 95%, models either fail dramatically or (in Claude's case) trigger automatic compaction. The practical rule: treat 60% of your model's context window as your effective working limit.

### The Four Warning Signs of Context Rot

Davis identifies four observable symptoms: (1) instructions getting ignored -- the AI stops following formatting or length constraints you set earlier, (2) self-contradiction -- the AI reverses earlier positions without justification, (3) fact disappearance -- specific data points you provided are hallucinated or dropped, (4) automatic compaction -- Claude's visible "organizing my thoughts" summarization, which loses nuance the user may need.

### The Handoff Strategy

When approaching the 60% threshold, create a new conversation and ask the degrading AI to produce a structured summary covering: what has been covered, key decisions made, current status in the to-do list, and specific next steps for the new conversation. This creates a deliberate, user-controlled context refresh rather than relying on automatic compaction.

### Strategic File Management

Different file types consume tokens at vastly different rates: text/Word documents are cheap, PDFs vary by complexity, images are expensive, complex Excel sheets are problematic, and video files can fill entire context windows. Davis recommends using Google AI Studio to check exact token counts, and slicing large files to include only the relevant sections for each task.

## Practical Takeaways

- **Monitor your context usage**: Use Google AI Studio (aistudio.google.com) to check token counts of files and conversations before uploading to any AI
- **Start new conversations at 60%**: Don't wait for degradation -- proactively hand off to a fresh conversation with a structured summary
- **Chunk files for tasks**: Instead of uploading entire documents, extract only the sections relevant to the current task
- **Decompose complex tasks across tabs**: If a task is too complex for one conversation, split it across multiple parallel AI conversations
- **Request periodic summaries**: Every 5-15 exchanges, ask the AI to summarize progress to refresh its effective working memory

## Notable Quotes

> "Imagine the AI's memory, its brain, is the size of a whiteboard. And every piece of information we add to that whiteboard, as it fills up, the AI gets dumber." — Dylan Davis ([00:28](https://www.youtube.com/watch?v=xaQG-eD9d58&t=28))

> "60,000 tokens equates to around half of a novel. 200,000 tokens equates to around a novel and a half. And then a million tokens equates to 7 to 8 novels." — Dylan Davis ([01:51](https://www.youtube.com/watch?v=xaQG-eD9d58&t=111))

> "We have no say in what's being summarized above. It could be summarizing things generically and the conversation gets worse as we go on." — Dylan Davis ([06:46](https://www.youtube.com/watch?v=xaQG-eD9d58&t=406))

## Related Sources

- [011: Prompt Engineering is dead](011-confluent-developer-context-engineering.md) — Context engineering as the successor to prompt engineering; Davis's tactics are practical implementations of these principles
- [040: Stop Feeding Claude Your Entire CLAUDE.md](040-charlie-automates-claudemd-context.md) — Context window management specifically for Claude Code users
- [048: Before You Build Another Agent, Understand This MIT Paper](048-brainqub3-recursive-language-models.md) — Academic research on context window limitations in recursive agent loops
- [024: You are Not Ready: Agentic coding in 2026](024-jo-van-eyck-agentic-coding-2026.md) — Context discipline as a core skill for agentic workflows
- [064: One Prompt Every AGENTIC Codebase Should Have](064-indydevdan-agentic-prompt.md) — Practical context engineering for developer workflows

## Related Curriculum

- [Module 02: Prompting and Workflows](../curriculum/02-prompting-and-workflows/README.md) — Context management tactics as core prompting discipline
- [Module 03: Claude Code Essentials](../curriculum/03-claude-code-essentials/README.md) — Context window management and compaction awareness for Claude users
