---
source_id: "004"
title: "Claude Code's New Agent Teams Are Insane (Opus 4.6)"
creator: "Bart Slodyczka"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=VWngYUC63po"
date: "2026-02-06"
duration: ""
type: "video"
tags: ["agent-teams", "multi-agent", "claude-code"]
curriculum_modules: ["05-team-orchestration"]
---

# 004: Claude Code's New Agent Teams Are Insane (Opus 4.6)

> **Creator**: Bart Slodyczka | **Platform**: YouTube | **Date**: 2026-02-06

## Summary

Bart Slodyczka demonstrates and compares two approaches to building applications with Claude Code: using a single agent versus the new Agent Teams feature introduced in Claude Opus 4.6. He builds the same task manager application with both approaches and evaluates the results side by side, covering setup, real-time development, and final feature comparison.

The key finding: build times were comparable between the two approaches, but the agent team delivered superior functional depth -- including features the user had not requested (board view, export/import, comprehensive settings) -- suggesting deeper architectural thinking by the specialized teammates.

## Key Concepts

### What Are Agent Teams?

Agent Teams are a new experimental feature in Claude Opus 4.6 that goes beyond the existing "sub-agents" (also called the Task tool). With Agent Teams:

- A **team lead** coordinates specialized **teammates**, each running in their own isolated Claude Code session.
- Teammates can **communicate directly with each other** (peer-to-peer), not just back to the lead.
- Each teammate operates in its own context window with independent token budgets, enabling higher-quality outputs.
- Users can interact with individual teammates directly without going through the lead.

This contrasts with sub-agents, which run within a single session and can only report results back to the parent agent.

### Sub-Agents vs. Agent Teams

| Aspect | Sub-Agents | Agent Teams |
|--------|-----------|------------|
| Sessions | Single instance | Each teammate gets an isolated session |
| Communication | Transactional, report back to parent only | Direct peer-to-peer dialogue between teammates |
| Complexity | Simpler, focused tasks | Complex collaborative problems |
| Token usage | Lower consumption | Higher (each teammate is a separate Claude instance) |
| Quality | Lower baseline | Higher output quality due to independent context windows |
| Coordination | Main agent manages all work | Shared task list with self-coordination |

### How to Enable Agent Teams

Setup requires modifying the Claude Code configuration:

1. Open your `settings.json` file.
2. Add the experimental environment variable:
   ```json
   {
     "env": {
       "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
     }
   }
   ```
3. Restart Claude Code in a new terminal session.
4. Preface prompts with "create an agent team to..." to trigger team creation.

**Model configuration options:**
- Opus 4.6 standard or the 1M token context version
- Reasoning effort toggle: low / mid / high
- High effort uses unrestricted tokens for complex projects

### Navigating Agent Teams

- Users toggle between the team lead and individual teammates using **Shift + Arrow keys**.
- In **in-process mode** (default): all teammates run inside the main terminal; use Shift+Up/Down to select a teammate and type to message them directly.
- In **split-pane mode** (requires tmux or iTerm2): each teammate gets its own terminal pane, allowing you to see everyone's output simultaneously.
- Press **Shift+Tab** to toggle delegate mode, which restricts the lead to coordination-only (no coding).

### The Experiment: Building a Task Manager App

Bart builds the same task manager application using both approaches with identical prompts.

#### Single Agent Results

- **Build time:** 6 minutes 55 seconds
- **Features produced:**
  - Subtasks with priority management
  - Calendar integration
  - Night/dark mode toggle
  - Right-click context menu (edit, reopen, priority change)
  - Multiple task views (inbox, work, personal)
  - Polished, immediately usable interface with emoji accents
- **Assessment:** Produced an engaging, emoji-rich design that was immediately usable. Included subtasks -- a feature typically found in professional task managers like ClickUp, but not usually seen in simple AI-built demos.

#### Agent Team Results

- **Build time:** 4 minutes 50 seconds (initial build) + ~1 minute 30 seconds (refinement/fixes) = ~6 minutes 20 seconds total
- **Features produced:**
  - Board view with drag-and-drop functionality
  - Comprehensive settings panel
  - Light/dark mode toggle
  - Export/import JSON data
  - Data clearing capabilities
  - More refined, professional visual design
- **Issues encountered:** Initially required JavaScript fixes for button functionality.
- **Assessment:** Delivered deeper feature implementations *without explicit prompting*. The board view and export/import capabilities were unprompted additions, suggesting deeper architectural thinking by the specialized teammates.

#### Side-by-Side Comparison

| Metric | Single Agent | Agent Team |
|--------|--------------|-----------|
| Build time | 6 min 55 sec | 4 min 50 sec (initial) + ~1.5 min (refinement) |
| Core features | Subtasks, priorities, calendar | Board view, settings panel, import/export |
| Visual polish | Emoji-rich, engaging interface | Refined, professional appearance |
| Unprompted additions | Minimal | Board view, export/import, comprehensive settings |
| Initial functionality | Worked immediately | Required a quick JavaScript fix |

### Architecture Details

An agent team consists of:

| Component | Role |
|-----------|------|
| **Team Lead** | The main Claude Code session that creates the team, spawns teammates, and coordinates work |
| **Teammates** | Separate Claude Code instances that each work on assigned tasks |
| **Task List** | Shared list of work items that teammates claim and complete (with dependency tracking) |
| **Mailbox** | Messaging system for communication between agents |

Teams and tasks are stored locally:
- Team config: `~/.claude/teams/{team-name}/config.json`
- Task list: `~/.claude/tasks/{team-name}/`

### Advanced Use Cases

Bart references Anthropic's recommended use cases for Agent Teams:

- **Code Review:** Assign distinct team members to different areas of the codebase for comprehensive, parallel review coverage. Specialized reviewers can focus on security, performance, and test coverage simultaneously.
- **Complex Analysis / Debugging:** Enable separate exploration of competing hypotheses. Multiple teammates investigate different theories and actively try to disprove each other, reducing anchoring bias.
- **Cross-Layer Coordination:** Changes spanning frontend, backend, and tests can each be owned by a different teammate.
- **Research and Review:** Multiple teammates investigate different aspects of a problem simultaneously, then share and challenge each other's findings.

### Known Limitations

- No session resumption with in-process teammates (`/resume` and `/rewind` do not restore teammates)
- Task status can lag (teammates sometimes fail to mark tasks as completed)
- Shutdown can be slow (teammates finish current work before shutting down)
- One team per session; no nested teams
- The lead is fixed for the team's lifetime
- All teammates start with the lead's permission settings
- Split-pane mode requires tmux or iTerm2 (not supported in VS Code terminal, Windows Terminal, or Ghostty)
- Significantly higher token consumption (~5x for a 5-person team)

## Practical Takeaways

- **Agent Teams excel at functional depth**: The team approach produced more features (including unprompted ones) with deeper architectural thinking, while single agents produced more visually polished output.
- **Build times are comparable**: Do not expect significant time savings from Agent Teams -- the advantage is in quality and feature depth, not speed.
- **Direct collaboration is the key differentiator**: Peer-to-peer communication between teammates (e.g., frontend asks backend for an API endpoint) eliminates the bottleneck of routing everything through a coordinator.
- **Token cost scales linearly**: A 5-person agent team uses roughly 5x the tokens. Use teams for complex, multi-faceted tasks where the quality improvement justifies the cost.
- **Expect initial bugs**: Agent team output may require refinement fixes that single-agent output does not, but the overall feature set compensates.

## Notable Quotes

> "The agent team delivered deeper feature implementations without explicit prompting." -- Bart Slodyczka, on the board view and export/import features appearing without being requested

## Related Sources

- [001: Claude Code Task System: ANTI-HYPE Agentic Coding](001-indydevdan-claude-code-task-system.md) -- Covers the underlying task system that Agent Teams build upon
- [003: Opus 4.6 AND ChatGPT 5.3 SAME DAY???](003-primetime-opus-46-chatgpt-53.md) -- Broader comparison of Opus 4.6 capabilities vs. GPT-5.3

## Related Curriculum

- [Module 05: Team Orchestration](../curriculum/05-team-orchestration/README.md) -- Multi-agent coordination patterns, team lead architecture, and when to use teams vs. single agents
