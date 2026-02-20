---
source_id: "058"
title: "The TRUTH About OpenClaw AI Agents (And How I'm Using Them)"
creator: "Jeremiah Krakowski"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=yKdqXV3QEZ8"
date: "2026-02-13"
duration: "21:57"
type: "video"
tags: ["ai-hype", "multi-agent", "security", "enterprise-ai", "ai-economics"]
curriculum_modules: ["01-foundations", "05-team-orchestration", "06-strategy-and-economics"]
---

# 058: The TRUTH About OpenClaw AI Agents (And How I'm Using Them)

> **Creator**: Jeremiah Krakowski | **Platform**: YouTube | **Date**: 2026-02-13 | **Duration**: 21:57

## Summary

Jeremiah Krakowski, an online business coach and marketer, presents his personal setup for running OpenClaw agents (formerly Claudebot/Moltbot) as "virtual employees" for his business. He walks through his hardware choices (an M1 Mac Mini purchased off eBay for under $300, plus cloud VPS instances on Hetzner), his communication layer (Slack channels per agent, Jump Desktop for remote access), and the various agent-built tools he uses daily -- a kanban project management board, ad generators, email writers, content calendars, and a telehealth platform for a client. He claims to run 14 agents simultaneously across multiple machines, powered by Claude Opus 4.6 via a Claude Max subscription at $200/month.

The video is notable less for technical depth and more as a case study of the "AI influencer/coach" pattern: the primary call to action is a waitlist for Krakowski's agent-setup-as-a-service offering (openclaw.jeremiahkrakowski.com), where he will configure OpenClaw agents for clients for a fee. He name-drops several adjacent platforms -- Lovable.dev, Manus.im, GenSpark AI, and Claude Co-work -- as alternative entry points for non-technical users. Throughout, he oscillates between genuine practical advice (isolate agents on dedicated hardware, do not give them access to your email, beware prompt injection) and hyperbolic claims ("superhuman intelligence," "PhD and higher level," a "thousand person team"). The video serves as a useful data point for how OpenClaw is being marketed to non-technical business audiences and what adoption actually looks like outside the developer community.

## Key Concepts

### OpenClaw as "Virtual Employee" Framing

Krakowski consistently frames OpenClaw agents as employees rather than tools. He describes giving them their own email accounts, securely sharing passwords via password managers, assigning them to Slack channels, and checking their project management boards for status updates. This mental model -- treating an agent exactly like a remote human worker -- is the dominant adoption pattern for non-technical users. It creates intuitive onboarding ("you would give an employee their own email account... it's the same kind of thing") but also obscures the fundamental differences between agents and humans in terms of accountability, error modes, and trust calibration. ([2:03](https://www.youtube.com/watch?v=yKdqXV3QEZ8&t=123))

### Dedicated Hardware and Isolation Practices

The most substantive practical content in the video is the hardware and isolation guidance. Krakowski recommends running agents on a dedicated machine -- never on your primary computer -- and suggests an M1 Mac Mini (under $300 on eBay) or a Raspberry Pi 5 with 8GB RAM (around $150-$180 with enclosure) as budget options. For cloud hosting, he uses Hetzner VPS instances at roughly $10/month running three to four agents per instance. He stresses separating agent access from personal accounts and not giving agents access to email or other services where prompt injection is a risk. This isolation-first approach aligns with the security recommendations in source 032, though Krakowski's execution is less rigorous than what enterprise-oriented sources prescribe. ([6:05](https://www.youtube.com/watch?v=yKdqXV3QEZ8&t=365))

### The Human-in-the-Loop Reality

Despite claiming 14 autonomous agents, Krakowski repeatedly describes a reality that is heavily human-directed. He says "I'm directing everything" and describes a pattern where agents propose, draft, and build, but he reviews, selects, and approves. When agents cannot navigate a website (due to bot detection or interface complexity), they open a browser and tell him which buttons to click. He characterizes this as "being a human in the loop that helps it do what it needs to do." This matches the 70/30 human-agent split identified in source 032 -- even enthusiastic early adopters are not truly running autonomous operations. ([14:11](https://www.youtube.com/watch?v=yKdqXV3QEZ8&t=851))

### Cost Structure for Non-Technical Agent Adoption

Krakowski provides a concrete cost breakdown: Claude Max subscription at $200/month for running multiple agents, hardware at $150-$300 (one-time), and optional cloud hosting at $10/month per instance. He frames this as dramatically cheaper than human employees, which is true on a per-hour basis but obscures the significant time investment in direction, review, and troubleshooting. He also announces a consulting service to set up agents for clients, indicating that the technical barrier remains high enough to sustain a service business around it. ([10:09](https://www.youtube.com/watch?v=yKdqXV3QEZ8&t=609))

### Prompt Injection and Security Awareness (Surface Level)

Krakowski briefly acknowledges the prompt injection risk, noting that agents could be manipulated via email content, social media, or agent-to-agent platforms like Moldbook. He claims he is "not necessarily scared of that" because he uses Claude Opus 4.6 rather than "cheap language models," implying that model quality alone mitigates injection risk. This is a significant misunderstanding -- prompt injection vulnerability is orthogonal to model capability. The mention of Clawhub's VirusTotal partnership for skill security scanning is accurate but presented without nuance about the limitations of signature-based scanning for code intended to run with system-level access. ([10:09](https://www.youtube.com/watch?v=yKdqXV3QEZ8&t=609))

## Practical Takeaways

- **Isolate agents on dedicated hardware**: Do not run OpenClaw agents on your primary work machine. A used M1 Mac Mini (under $300) or Raspberry Pi 5 (8GB minimum) provides sufficient compute for multiple agents at low cost. ([6:05](https://www.youtube.com/watch?v=yKdqXV3QEZ8&t=365))
- **Use Slack as the agent communication layer**: Setting up per-agent Slack channels provides a persistent, searchable log of all agent interactions accessible from any device, including mobile. ([4:05](https://www.youtube.com/watch?v=yKdqXV3QEZ8&t=245))
- **Budget $200/month minimum for Claude Max**: The $100 tier is insufficient for sustained agent workloads. Factor this into ROI calculations alongside hardware costs. ([10:09](https://www.youtube.com/watch?v=yKdqXV3QEZ8&t=609))
- **Do not give agents direct access to your email or primary accounts**: Use dedicated credentials and password managers. Remote in manually when agents need to log into sensitive services. ([8:05](https://www.youtube.com/watch?v=yKdqXV3QEZ8&t=485))
- **Expect heavy human direction despite "autonomous" branding**: Even at 14 agents, the daily workflow involves significant prompting, reviewing, and manual intervention. Plan for a manager role, not a hands-off one. ([14:11](https://www.youtube.com/watch?v=yKdqXV3QEZ8&t=851))

## Notable Quotes

> "The way that you want to think about OpenClaw is that it is its own person or employee or thing that can function on its own the same way that a human employee would. If you brought an employee on in your business, you would give them their own email account, you would securely share passwords with them." -- Jeremiah Krakowski ([8:05](https://www.youtube.com/watch?v=yKdqXV3QEZ8&t=485))

> "I've stopped having to learn how everything works. I just ask my agent to go read the documentation and figure it out." -- Jeremiah Krakowski ([12:09](https://www.youtube.com/watch?v=yKdqXV3QEZ8&t=729))

> "It's not necessarily coming up with ideas and doing stuff autonomously on its own. I'm directing everything." -- Jeremiah Krakowski ([14:11](https://www.youtube.com/watch?v=yKdqXV3QEZ8&t=851))

## Related Sources

- [032: OpenClaw: 160,000 Developers Just Showed Us What People Actually Want From AI](032-nate-b-jones-openclaw.md) -- Analytical counterpart to Krakowski's anecdotal account; Jones covers the same platform with rigorous attention to security, governance, and the specification quality problem
- [017: Be Careful w/ Skills](017-primeagen-skills-security.md) -- Skills ecosystem security risks that Krakowski's surface-level treatment of Clawhub security underplays
- [004: Claude Code's New Agent Teams Are Insane](004-bart-slodyczka-agent-teams.md) -- Developer-oriented multi-agent setup; contrasts with Krakowski's non-technical approach
- [025: AI Productivity Bubble](025-natasha-bernal-ai-productivity-bubble.md) -- Critical perspective on the "virtual employee" narrative and enterprise AI adoption economics
- [033: Why CEOs Are Getting AI Wrong](033-prof-g-ethan-mollick-ai-wrong.md) -- Ethan Mollick's research on the gap between AI enthusiasm and measured productivity gains, relevant to Krakowski's uncritical claims

## Related Curriculum

- [Module 01: Foundations](../curriculum/01-foundations/README.md) -- AI landscape and hype dynamics; this video exemplifies how agent technology is being marketed to non-technical audiences
- [Module 05: Team Orchestration](../curriculum/05-team-orchestration/README.md) -- Multi-agent coordination patterns; Krakowski's Slack-based agent communication and sub-agent delegation, however informal
- [Module 06: Strategy and Economics](../curriculum/06-strategy-and-economics/README.md) -- Agent deployment cost structures, the human-in-the-loop reality vs. autonomous agent marketing, security considerations
