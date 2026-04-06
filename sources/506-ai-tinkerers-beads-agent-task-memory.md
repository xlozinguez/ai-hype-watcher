---
source_id: "506"
title: "Beyond Instructions: How Beads Lets AI Agents Build Like Engineers"
creator: "AI Tinkerers"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=s96O9oWI_tI"
date: "2025-12-12"
duration: "47:49"
type: "video"
tags: ["agentic-coding", "vibe-coding", "validation", "mcp", "prompt-engineering", "context-engineering", "task-system"]
curriculum_modules: ["02-prompting-and-workflows", "04-agentic-patterns"]
---

# 506: Beyond Instructions: How Beads Lets AI Agents Build Like Engineers

> **Creator**: AI Tinkerers | **Platform**: YouTube | **Date**: 2025-12-12 | **Duration**: 47:49

# Beyond Instructions: How Beads Lets AI Agents Build Like Engineers

## Summary

Steve Yaggi, head of engineering at Sourcegraph (makers of the AMP coding environment), discusses his open-source project Beads—a framework that gives coding agents persistent task management and memory to enable much longer autonomous run times and tackle more ambitious, multi-session projects. The conversation is grounded in practical demonstration: Steve shows an AI agent actively building a React game client for his 30-year-old multiplayer game, with the agent autonomously taking screenshots via Playwright MCP and validating its own output against a reference screenshot. The session covers concrete workflow techniques rather than abstract philosophy.

A central theme is that agentic coding is genuinely hard—not the frictionless "vibe coding" often marketed—and that experienced engineers are evolving into a supervisory role: setting context, defining validation loops, checking in periodically, and steering when agents get stuck. Steve describes his own productivity system in detail: landing-plane cleanup scripts, tracer bullet debugging, multimodal prompting with automated screenshots, and specific tooling choices (Graphite, Playwright MCP, AMP's task list UI).

The session also includes a brief revisit of Steve's 2024 essay "Death of the Junior Developer," reframed with actionable advice: developers must build a portfolio demonstrating AI workflow mastery and invest in understanding how to supervise and guide agents effectively. Both senior and junior developers now depend on their ability to orchestrate AI workers, not just write code themselves.

---

## Key Concepts

### Beads: Task Management and Memory for Long-Running Agents
Beads is an open-source framework (four weeks old at time of recording, already hundreds of contributors) that gives coding agents a persistent task list and memory system. This allows agents to maintain context and make forward progress across much longer sessions than typical stateless agent runs. The core insight is that agents fail on ambitious projects not because of capability limits but because they lose track of what they've done and what remains—Beads addresses this structural gap. It works with Claude Code, Codex, AMP, and other CLI coding agents.

### Multimodal Validation via Screenshot Workflows
Steve demonstrates a workflow where a reference screenshot of an existing game client (the Steam version) serves as the source of truth. The agent is instructed to continuously compare its current output—captured automatically via Playwright MCP controlling a real browser—against this reference. This forces the agent to self-catch lies ("we're all done now") and iteratively close the gap between current and target state. The pattern: establish a visual ground truth → automate capture of current state → make the agent validate against it before claiming completion.

### Tracer Bullet: Getting Unstuck on Hard Problems
Borrowed from *The Pragmatic Programmer*, the tracer bullet technique involves finding the thinnest possible end-to-end path through a problem and getting that working first. Steve applied this when the React client stalled: instead of fighting graphics and rendering, he had the agent implement the TELNET protocol into the game server first—a simple, verifiable slice. This unblocked the whole effort by establishing a working integration baseline before tackling complexity. Recommended specifically when agents have made no forward progress after multiple sessions.

### The "Landing the Plane" Cleanup Script
At the end of every development session, Steve runs a scripted cleanup command he calls "landing the plane." It handles: committing and syncing changes, resolving git branch issues, cleaning up old branches, and identifying the best task to pick up in the next session. This is a meta-workflow pattern—treating session boundaries as first-class engineering concerns rather than afterthoughts. It keeps the repo clean and ensures continuity across agent sessions.

### The Evolving Engineer Role: Supervisor, Not Author
Steve's framing of the new engineering role is explicit: the human's job is to yell at the agent—set context, provide reference materials, check in periodically, steer on failures, run validation workflows. He notes that diffs scrolling by are less important than the *shape* of the code (is it spewing thousands of lines?), and that everything an agent produces should be assumed ~85% correct at best. Engineers now manage AI workers rather than writing every line, and this shift requires different skills: prompt design, validation loop construction, workflow orchestration, and knowing when to intervene.

---

## Practical Takeaways

- **Use a reference screenshot as a contract.** For any UI porting or visual work, establish a target screenshot and wire the agent to compare against it automatically (e.g., via Playwright MCP) before marking tasks complete. This catches agent hallucinations about task completion.

- **When stuck after many sessions, apply the tracer bullet.** Find the thinnest end-to-end slice of the feature (e.g., a bare protocol connection before any UI) and get that working first. Hang everything else on that baseline.

- **Script your session endings.** A "landing the plane" command that commits, syncs, cleans branches, and surfaces next priorities removes friction and ensures agents' work persists cleanly between sessions.

- **Treat agent output as 85% correct by default.** If an agent produces a large volume of code quickly, explicitly request a code review pass before proceeding. Successive refinement is the model, not single-pass correctness.

- **Build a portfolio demonstrating AI workflow mastery.** Per Steve's revisit of the junior developer question: the new bar is showing you can design, supervise, and iterate with agents—not just code. This applies at all experience levels.

---

## Notable Quotes

> "Look, man, everyone's like, 'Oh, vibe coding is supposed to be easy.' And I just—the thing that's not getting across to people in general is that, man, it's just as hard as regular coding. You have to—you're wrestling with a bear all day long."

> "Look, I'm at a higher level... anything that it does is going to be 85% correct. So this—it's yes, it's successive refinement. Everything that it does, just assume it's 85% correct."

> "I caught you lying to me. Right. That's what they do... I made it catch itself by introducing a workflow where I say, 'Look, our screenshot has to match this reference screenshot.'"

---
