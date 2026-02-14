---
source_id: "046"
title: "The Rise of WebMCP"
creator: "Sam Witteveen"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=35oWt7u2b-g"
date: "2026-02-12"
duration: "10:05"
type: "video"
tags: ["mcp", "agentic-coding", "ai-landscape", "enterprise-ai"]
curriculum_modules: ["01-foundations", "04-agentic-patterns"]
---

# 046: The Rise of WebMCP

> **Creator**: Sam Witteveen | **Platform**: YouTube | **Date**: 2026-02-12 | **Duration**: 10:05

## Summary

Sam Witteveen breaks down WebMCP, a new standard jointly developed by Google and Microsoft that shipped as an early preview in Chrome. WebMCP allows websites to expose structured tools directly to AI agents through the browser, eliminating the need for DOM scraping or screenshot-based interaction. Instead of agents guessing which buttons to press by parsing raw HTML or processing images, websites register callable functions that agents can discover and invoke — turning each web page into what is effectively an MCP server.

The video traces the problem space (agents as "tourists who don't speak the language" of websites), explains the three-pillar architecture proposed at the Web AI Summit (context, capabilities, coordination), and details the two APIs — declarative for HTML forms and imperative for complex JavaScript interactions. Witteveen positions this as a human-in-the-loop-first design, where agents augment rather than replace user interaction with websites. He notes this is already available behind a flag in Chrome and expects broader rollout at Google Cloud Next or Google I/O.

## Key Concepts

### The Agent-Web Interaction Problem

Current approaches to web-based agent interaction rely on two fundamentally inefficient methods: screenshot-based interaction (passing images to multimodal models, consuming thousands of tokens per image) and DOM/HTML parsing (translating raw markup into actionable information while discarding irrelevant styling and structure). Both approaches amount to "speaking a foreign language" to the website — the agent must infer intent from presentation rather than receiving structured capability declarations.

### WebMCP's Three Pillars

The architecture, as presented at the Web AI Summit, rests on three pillars. **Context** encompasses all data agents need to understand what the user is doing, including content not currently visible on screen. **Capabilities** cover actions the agent can take on the user's behalf, such as filling out forms or executing searches. **Coordination** governs the handoff between user and agent — for example, when an agent sent to buy a specific product encounters an out-of-stock situation and needs to defer back to the user for a decision.

### Declarative vs. Imperative APIs

WebMCP provides two complementary APIs. The **Declarative API** annotates existing HTML forms with tool names and descriptions, making well-structured forms approximately 80% ready for agent interaction with minimal additional work. The **Imperative API** handles complex dynamic interactions requiring JavaScript execution, with schemas resembling tool definitions sent to the OpenAI or Anthropic API endpoints — but running entirely client-side in the browser.

## Practical Takeaways

- **For agent builders**: WebMCP replaces what could be dozens of screenshot-and-click interactions with a single structured tool call, dramatically reducing token costs and improving reliability. If you are building agents that interact with the web, this should be a priority to evaluate.
- **For web developers**: Well-structured HTML forms are already most of the way to WebMCP compatibility via the Declarative API. The Imperative API allows exposing richer, JavaScript-driven capabilities as callable tools.
- **Human-in-the-loop by design**: WebMCP is explicitly built for cooperative workflows where agents work alongside users, not fully autonomous browsing. The coordination pillar ensures graceful handoff when the agent encounters ambiguity.
- **Timeline**: Available now behind a flag in Chrome; broader rollout expected at Google Cloud Next or Google I/O in early-to-mid 2026. Developers can join the Chrome Early Preview Program for early access.

## Notable Quotes

> "Right now, when your agent visits a website, it's basically a tourist who doesn't speak the language of that site." — Sam Witteveen ([00:00](https://www.youtube.com/watch?v=35oWt7u2b-g&t=0))

> "This is a whole new standard that lets any website expose structured tools directly to AI agents. No more need for scraping. No more need for thousands of screenshots. Your agent just calls functions." — Sam Witteveen ([00:31](https://www.youtube.com/watch?v=35oWt7u2b-g&t=31))

> "You can imagine this sort of one tool call replaces what could have been dozens of interactions that would have been needed if you were just using a browser use kind of thing." — Sam Witteveen ([07:46](https://www.youtube.com/watch?v=35oWt7u2b-g&t=466))

> "If you're building AI agents or you're building websites and products that you want agents to use, this literally could be the most important thing to land in Chrome in years." — Sam Witteveen ([01:02](https://www.youtube.com/watch?v=35oWt7u2b-g&t=62))

## Related Sources

_No directly related sources in the collection yet._

## Related Curriculum

- [Module 01: Foundations](../curriculum/01-foundations/README.md) — WebMCP as an industry-shifting standard for how agents interact with the web
- [Module 04: Agentic Patterns](../curriculum/04-agentic-patterns/README.md) — Structured tool invocation as an alternative to browser-use scraping patterns
