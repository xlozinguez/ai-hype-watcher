---
source_id: "013"
title: "Stop Using Claude Code Without Skills"
creator: "Leon van Zyl"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=vIUJ4Hd7be0"
date: "2026-02-09"
duration: "20:46"
type: "video"
tags: ["skills", "claude-code", "skills-ecosystem"]
curriculum_modules: ["03-claude-code-essentials"]
---

# 013: Stop Using Claude Code Without Skills

> **Creator**: Leon van Zyl | **Platform**: YouTube | **Date**: 2026-02-09 | **Duration**: 20:46

## Summary

Leon van Zyl provides a comprehensive, hands-on introduction to the Claude Code skills system -- from discovering and installing skills to building custom skills from scratch. The central thesis is that skills dramatically extend what Claude Code can accomplish by teaching it capabilities it does not possess natively, such as image generation, without permanently occupying context window space the way MCP server tool definitions do. Skills are markdown files containing precise instructions and supporting resources that Claude Code loads on demand based on conversational context.

The video walks through two ecosystems for finding skills: Anthropic's built-in plugin marketplace (accessible directly within Claude Code) and skills.sh, Vercel's open agent skills marketplace. Van Zyl demonstrates real results by comparing a fitness app landing page built without skills against the same page built with a front-end design skill and an AI image generation skill -- the difference is stark. The practical portion covers creating a custom image generation skill that uses Google's Nano Banana Pro model, including secure handling of API keys through environment variables, and an image optimization skill that reduced a 631KB image to 56KB by converting to WebP format.

The video is particularly effective at clarifying the frequently confused relationship between skills, MCP servers, and custom commands, establishing a clear mental model: MCP servers provide tools (always in context, always consuming tokens), skills provide workflows and knowledge (loaded on demand, minimal token footprint), and custom commands are simply reusable prompts.

## Key Concepts

### Skills as Lazy-Loaded Instructions

Skills are markdown files containing precise instructions and associated resources (scripts, reference material, domain knowledge) that Claude Code discovers and activates based on the conversation's context. Unlike MCP server tool definitions, which are preloaded into the agent's context and consume tokens whether or not they are used, skills take up minimal context until the agent determines it needs them. When a user asks Claude Code to generate an image, it recognizes it has an image generation skill available, loads the skill's markdown file into its working context, and follows the instructions. This "lazy loading" pattern is the fundamental architectural advantage of skills over tools for capabilities that are not needed in every session.

### Skills vs MCP Servers vs Custom Commands

The video provides the clearest taxonomy of these three extension mechanisms:

- **MCP Servers**: Provide new tools (browser control, database access, API integration). Tool definitions are always present in the agent's context, consuming tokens even when unused. Best for capabilities needed frequently across sessions.
- **Skills**: Provide workflows, domain knowledge, and step-by-step instructions. Loaded on demand based on conversational context. Best for specialized capabilities used occasionally (image generation, front-end design patterns, optimization techniques).
- **Custom Commands**: Simply reusable prompts triggered manually. No auto-activation, no tool integration. Best for frequently repeated prompt patterns.

Skills and MCP tools can be combined: a skill might instruct the agent to use a particular MCP tool in a specific way, layering workflow knowledge on top of raw tool capabilities.

### The Skills Ecosystem

Two main sources for discovering and installing skills:

1. **Anthropic's built-in plugin marketplace**: Accessed directly within Claude Code. Contains Anthropic's officially curated skills.
2. **skills.sh (Vercel)**: An open marketplace for community-contributed skills. Notable skills mentioned include: a "Find Skills" skill (meta-skill for discovering other skills), a "Skill Creator" skill (for building new skills), React best practices, front-end design, and browser use.

The ecosystem is still early but growing rapidly, with the skills.sh marketplace enabling community contribution and discovery.

### Building Custom Skills

Van Zyl demonstrates creating an image generation skill from scratch using the "Skill Creator" skill as a bootstrap. The process involves:

1. Defining the capability (generate images using Google's Nano Banana Pro model)
2. Writing the markdown instructions with the precise steps the agent should follow
3. Including a Python script that the agent executes to call the image generation API
4. Handling API keys securely through environment variables in a `.env` file excluded from git
5. Testing the skill by asking Claude Code to generate an image

The key insight is that skills can teach Claude Code to orchestrate any external tool or API by providing step-by-step instructions and supporting scripts -- the agent follows the recipe rather than needing native capability.

### Token Efficiency of Skills

The video demonstrates that installed skills consume very little context. Claude Code only loads the minimum metadata needed for skill discovery (name, description, activation conditions). The full skill content -- which can include extensive instructions, reference material, and examples -- is only loaded when the agent decides the skill is relevant to the current task. This is a significant advantage for users who want to extend Claude Code's capabilities broadly without bloating the context window.

### Practical Skill Composition

The video shows skills working together in sequence: the front-end design skill improves layout and aesthetics, the image generation skill creates a custom hero image, and the image optimization skill compresses it for web performance (631KB to 56KB). This composition pattern -- chaining skills for different phases of a task -- demonstrates how skills can form lightweight pipelines without formal orchestration infrastructure.

## Practical Takeaways

- **Install skills before starting projects**: Skills like front-end design dramatically improve output quality with zero additional prompting effort, since they activate automatically based on context.
- **Prefer skills over MCP servers for occasional capabilities**: If you only need image generation or optimization in some sessions, a skill avoids the constant token cost of an MCP tool definition.
- **Use environment variables for API keys in skills**: Never hardcode secrets in skill markdown files. Use `.env` files excluded by `.gitignore` and reference them in the skill's scripts.
- **Bootstrap custom skills with the Skill Creator skill**: Rather than writing skill markdown from scratch, use the meta-skill to generate a well-structured starting point.
- **Check both marketplaces**: Anthropic's built-in plugins and skills.sh offer different selections. The community marketplace (skills.sh) often has more specialized, niche skills.

## Notable Quotes

> "We can use skills to teach Claude Code how to do something that it couldn't do natively." -- Leon van Zyl

> "MCP servers simply provide new tools to the agent... skills actually take up very little context." -- Leon van Zyl

## Related Sources

- [001: Claude Code Task System: ANTI-HYPE Agentic Coding](001-indydevdan-claude-code-task-system.md) -- Skills complement the task system and meta-prompt patterns described here; skills provide capabilities while meta-prompts provide orchestration
- [011: Prompt Engineering is dead.](011-confluent-developer-context-engineering.md) -- The lazy-loading advantage of skills is a direct application of context engineering principles -- managing what occupies the context window and when
- [004: Claude Code's New Agent Teams Are Insane](004-bart-slodyczka-agent-teams.md) -- Agent team members can access skills, extending the team orchestration pattern with specialized capabilities

## Related Curriculum

- [Module 03: Claude Code Essentials](../curriculum/03-claude-code-essentials/README.md) -- Skills system setup, installation, and usage as a core Claude Code capability
