---
source_id: "363"
title: "Claude Code Just Got Another Huge Upgrade"
creator: "Nate Herk | AI Automation"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=X6EGzi9qm3E"
date: "2026-03-24"
duration: "8:10"
type: "video"
tags: ["claude-code", "agentic-coding", "task-system", "security"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns"]
---

# 363: Claude Code Just Got Another Huge Upgrade

> **Creator**: Nate Herk | AI Automation | **Platform**: YouTube | **Date**: 2026-03-24 | **Duration**: 8:10

# Claude Code Computer Use — Desktop Automation Feature

## Summary

Anthropic released a new "computer use" feature for Claude Code (currently in research preview on macOS only) that allows the AI to natively control your mouse, keyboard, and take screenshots to operate desktop applications. The feature is accessible through the Claude Code desktop app settings and requires granting accessibility permissions to specific apps. The demo showcases Claude autonomously navigating ClickUp to send a file attachment, opening calculator apps, and even starting an OBS recording session — all with minimal user intervention.

The feature becomes significantly more powerful when paired with Claude's "Dispatch" capability, which allows users to trigger computer use sessions remotely from a phone. This combination effectively enables asynchronous desktop automation: you can fire off a task from anywhere, and Claude will execute it on your local machine while you're away, as long as the computer is awake (which Dispatch can also handle natively).

Key limitations at launch include: macOS-only support (Windows coming in weeks), browser interactions are restricted to read-only access for security reasons (requiring Chrome extension or Playwright for web automation), and the feature is only available on Pro plans, not Teams or Enterprise. The creator frames this as a rapidly iterating foundation — particularly exciting for legacy app automation, scheduled task pairing, and local app testing workflows.

## Key Concepts

### Computer Use in Claude Code
Claude can take screenshots of your desktop at intervals, analyze the visual state of applications, and issue mouse clicks and keyboard inputs to interact with any native app. It operates iteratively: screenshot → analyze → act → screenshot again. This loop allows it to navigate unfamiliar interfaces by "seeing" them rather than relying on APIs or structured integrations.

### Permission Model and App Allowlisting
On first use per session, Claude requests explicit permission to access each application it needs to interact with (e.g., Finder, ClickUp). Once granted within a session, it doesn't re-prompt for the same app. This opt-in model is a deliberate safety guardrail — users control which apps Claude can touch.

### Dispatch Integration for Remote Triggering
The Dispatch feature allows users to send instructions to their local Claude Code instance from a mobile device. Combined with computer use, this creates a remote-control-style workflow: message from phone → Claude wakes machine and executes desktop tasks locally. The creator positions this as a core unlock for asynchronous, human-out-of-the-loop automation.

### Browser Restriction and the Workaround
Native browser automation (Safari, Chrome via computer use) is intentionally restricted to read-only screenshot access for security reasons. For web automation, users must instead use a Chrome extension connector or a Playwright CLI. This is a meaningful gap for users expecting full web agent behavior, but local-app automation works well.

### Scheduled Tasks + Computer Use Pairing
Computer use can be triggered by Claude Code's scheduled tasks feature, enabling recurring automations (e.g., pull a report every Friday, scan email every morning) without any manual trigger. The creator describes this as approximating "a real human working on your laptop" for repetitive workflows.

## Practical Takeaways

- **Enable it explicitly in settings**: Go to Claude Code desktop app → Settings → General → Desktop App → Computer Use. Quit and relaunch after enabling. If Claude tries to use browser-based tools instead, be more explicit in your prompt: "use computer use to…"
- **Use native apps, not browsers**: For reliable automation, route tasks through desktop apps (Slack app, ClickUp app, Gmail app) rather than browser tabs. Browser use is currently read-only via computer use.
- **Pair with Dispatch for async workflows**: The highest-leverage use case is triggering desktop tasks remotely — useful for accessing locally stored files, running reports, or checking builds while away from your machine.
- **Strong fit for legacy/no-API tools**: Apps without public APIs (internal dashboards, legacy enterprise software) are prime targets, since computer use doesn't require any integration — just a visible UI.
- **Use for local app testing**: Having Claude click through your own app builds in a sandbox environment to find bugs or validate features reduces manual QA time significantly.

## Notable Quotes

> "It's pretty much going to be as if you have a real human working on your laptop."

> "At some point, Claude Code will be able to do this in the web and all this kind of other stuff. It's just going to take a little bit more time, but they're still shipping at an insane pace."

> "Even if you have different connectors like your Gmail app or your Slack app or ClickUp app — as you guys saw — it can use all of those perfectly fine."
