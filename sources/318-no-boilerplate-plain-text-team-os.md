---
source_id: "318"
title: "The Unreasonable Effectiveness Of Plain Text"
creator: "No Boilerplate"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=WgV6M1LyfNY"
date: "2023-10-13"
duration: "14:37"
type: "video"
tags: ["specification", "ai-sdlc", "context-engineering"]
curriculum_modules: ["02-prompting-and-workflows", "06-strategy-and-economics"]
---

# 318: The Unreasonable Effectiveness Of Plain Text

> **Creator**: No Boilerplate | **Platform**: YouTube | **Date**: 2023-10-13 | **Duration**: 14:37

# The Unreasonable Effectiveness Of Plain Text

## Summary

This video argues that most team dysfunction—bad documentation, constant tool churn, ineffective meetings—stems from over-engineering collaboration infrastructure rather than under-engineering it. The core thesis is a "Ulysses Pact" argument: by committing to plain text (specifically Markdown stored in Git/GitHub) as the universal substrate for all team artifacts, you pre-commit against the future temptation of adopting new, incompatible tools that fragment institutional knowledge and create legacy data silos.

The practical recommendation is to build an entire team operating system on GitHub's native primitives: repositories for versioned files, wikis for documentation, issues for task capture, milestones for release planning, project boards for kanban-style visibility, and Actions for automation. This stack handles code, design assets, company documents, and process management in one unified, offline-capable, find-and-replaceable corpus—something no web SaaS alternative currently provides.

The deeper argument is about *permanence and portability*. Data stored in plain Markdown files in Git is readable by any tool, present or future, and mistakes are trivially reversible via pull requests. Conversely, data locked in proprietary SaaS tools degrades in value over time as tools deprecate and export formats prove lossy. The compound network effect of a unified plain-text corpus grows stronger with time rather than weaker.

## Key Concepts

### The Ulysses Pact as Tool Discipline
Odysseus had himself tied to the mast so his future self couldn't make bad decisions under the influence of the Sirens. Standardizing on plain text is the team equivalent: by pre-committing to a format that every future tool can read, you neutralize the future temptation to migrate to the next hot project-management SaaS. The overhead of tool churn isn't just migration cost—it's the cultural signal that "anything we write down will be legacy soon," which causes teams to stop writing things down at all.

### Plain Text as the Universal Substrate
Markdown is designed to be readable both as raw text and as rendered rich text. Unlike HTML or proprietary formats, it imposes just enough structure (headings, bold, links) without enabling the kind of elaborate formatting that distracts from content. Storing everything—code, documentation, meeting conclusions, design assets—in Git repositories means the entire corpus is searchable, diff-able, and offline-accessible. A global find-and-replace across 10,000 files is a five-second terminal command rather than an impossible SaaS limitation.

### GitHub as Minimum Viable Team OS
GitHub's native feature stack (repos, wikis, issues, milestones, project boards, Actions, PRs, organizations, teams) maps directly onto the core needs of any team: file versioning, documentation, task management, release planning, work visualization, automation, change review, and access control. Each feature is deliberately minimal—milestones have a title, description, date, and progress bar, nothing more—which prevents the "Jira effect" where tool complexity encourages teams to track metrics that add no value.

### Asynchronous Written Communication as Scale Infrastructure
Spoken conversation doesn't scale: it's ephemeral, memory of it is unreliable, and it requires synchronous presence. Written records in a versioned system allow asynchronous discussion, auditable decision history, and onboarding of new team members without tribal knowledge transfer. The ADR (Architecture Decision Record) pattern—recording not just what was decided but why—is cited as a specific practice that compounds in value over time.

### Actions as Automation Primitives
GitHub Actions, originally built for CI/CD on open-source code, generalize to arbitrary automation: rasterizing vector assets at all required resolutions, running audio through noise-removal plugins and uploading drafts, spell-checking documents before merge, enforcing style-guide rules as PR gates. Automating repeatable processes via code committed alongside the artifacts being processed gives teams a compounding quality and speed advantage without the overhead of maintaining separate automation infrastructure.

## Practical Takeaways

- **Treat documentation infrastructure as a Ulysses Pact**: choose the most boring, portable format (Markdown + Git) rather than the most feature-rich current tool, specifically to protect against future migration overhead and data rot.
- **Run standups by walking the board right-to-left**, time-boxing each person with an issue on the board; close with "any blockers?"—this surfaces real blockers in under 15 minutes and eliminates status theater.
- **Use GitHub's minimal project management primitives before reaching for Jira/Trello**: issues → milestones → project boards represents a progression you can stop at as soon as it's sufficient, avoiding complexity that generates busywork.
- **Store *all* team artifacts in Git repositories**, not just code—design files, company documents, policies, and runbooks—to get offline access, global search, and trivial rollback across the entire organizational knowledge base.
- **Encode best-practice enforcement as Actions**, not as policy documents: if "on-premise" is banned in company writing, a PR gate that rejects the phrase is more reliable than a style guide nobody reads.

## Notable Quotes

> "In order to do more you must have the discipline to do less."

> "The act of changing tools constantly is an enormous overhead for your team and one that gives the lasting impression that anything we write down is likely to be Legacy very soon, trapped in a deprecated app that we just don't use anymore. So why bother writing anything down?"

> "The magic of offline isn't necessarily that you don't need the internet—though that is a handy feature on a plane—but that it's fast. The data is right here on your computer and you can do anything with it."
