---
source_id: "363"
title: "Claude Code Just Got Another Huge Upgrade"
creator: "Nate Herk | AI Automation"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=X6EGzi9qm3E"
date: "2026-03-24"
duration: "8:10"
type: "video"
tags: ["claude-code", "agentic-coding", "task-system", "ai-landscape"]
curriculum_modules: ["03-claude-code-essentials", "04-agentic-patterns"]
---

# 363: Claude Code Just Got Another Huge Upgrade

> **Creator**: Nate Herk | AI Automation | **Platform**: YouTube | **Date**: 2026-03-24 | **Duration**: 8:10

# Claude Code Computer Use Feature — Demo & Limitations

## Summary

Anthropic has released a research preview of computer use functionality for Claude Code (and Claude.ai), enabling the AI to natively control a Mac's mouse, keyboard, and screenshots to operate desktop applications autonomously. The feature is demonstrated performing tasks like finding a PDF and sending it as a ClickUp DM, opening apps, and performing calculations — all triggered by the user without being physically present at the machine. Nate pairs this with Claude's "Dispatch" feature, which allows tasks to be sent from a phone, effectively making the local computer remotely operable from anywhere.

The video walks through the setup process (enabling computer use in Claude desktop app settings, granting accessibility permissions) and demonstrates the permission model, where Claude requests access to specific apps within a session but retains those permissions for the remainder of that session. The demos show Claude navigating unfamiliar UI by taking iterative screenshots, zooming in on interface elements, and inferring correct clicks — a slow but functional visual reasoning loop.

Key limitations are addressed directly: the feature is Mac-only in this research preview (Windows coming soon), restricted to Pro plan users, unavailable on Teams/Enterprise, and — most importantly — browsers are restricted to read-only access for security reasons. Web automation still requires a Chrome extension or Playwright. Nate frames the bigger picture as Anthropic shipping toward a fully integrated Claude Code that handles browser and desktop contexts natively, with scheduled tasks and Dispatch as force multipliers for async autonomous workflows.

---

## Key Concepts

### Computer Use via Visual Reasoning Loop
Claude Code controls the desktop by taking iterative screenshots, analyzing UI state, inferring where to click or type, and acting — then repeating. It zooms into interface elements to confirm button locations before acting. This is not API-level integration; it's pixel-level visual reasoning, which makes it app-agnostic but also slower and occasionally imprecise.

### Permission Model and Session Access
On first use within a session, Claude requests explicit user permission to access each application (e.g., Finder, ClickUp). Once granted for that session, subsequent uses of the same app don't require re-authorization. This is distinct from the OS-level permissions (screen recording, accessibility) that must be configured once at setup.

### Dispatch Integration for Remote Triggering
The Dispatch feature allows users to send Claude Code tasks from a phone (via text/message interface), which then execute locally on the user's desktop machine — as long as the machine is awake. Claude can also natively wake the computer. This combination effectively turns Claude Code into a remote desktop automation agent operable from anywhere.

### Browser Restriction as Security Boundary
Browsers (Safari, Chrome) are restricted to read-only access within computer use. Claude can open a browser but cannot type into or click within it. This is an intentional security decision. Web automation requires routing through a Chrome extension or Playwright CLI instead, which represents a meaningful workflow gap for web-heavy tasks.

### Scheduled Tasks as Autonomous Workflow Trigger
Computer use can be combined with Claude Code's scheduled task system to create fully autonomous, recurring desktop workflows — e.g., scanning email every morning or pulling a report every Friday — without any human trigger. This positions computer use as a component in longer-running agentic pipelines, not just ad-hoc commands.

---

## Practical Takeaways

- **Be explicit in prompts**: If Claude tries to use a browser extension or Playwright instead of native computer use, explicitly say "use computer use" in the prompt. Ensure the Claude desktop app is fully updated and restarted after enabling the setting.
- **Best for apps without APIs**: Computer use is most valuable for legacy desktop software, proprietary internal tools, or any app that lacks an accessible API — Claude can click through the UI just as a human would.
- **Browser automation still needs Playwright or Chrome extension**: Don't expect computer use to handle web tasks end-to-end. Plan your stack accordingly — use computer use for local/desktop apps and route browser tasks to Playwright or a browser extension.
- **Pair with Dispatch for async delegation**: The real productivity unlock is combining computer use with Dispatch to fire off desktop tasks remotely and return to find them completed — useful for checking builds, sending files, or running reports while away from the machine.
- **Use for QA and sandbox testing**: Having Claude Code click through a locally running app to find bugs or test features is a low-friction alternative to writing test scripts, especially during early development.

---

## Notable Quotes

> "It's pretty much going to be as if you have a real human working on your laptop."

> "I actually had Claude Code start up this recording for me... the recording was started by Claude Code."

> "Anthropic is shipping a new feature like every day. What this shows us is that they're moving towards having all of these features natively within Claude Code."

---
