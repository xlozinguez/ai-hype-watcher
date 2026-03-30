---
source_id: "414"
title: "Delve faked SOC2. That's worse than SOC2 itself."
creator: "Zack Korman"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=Z5Gg3kpTEuo"
date: "2026-03-28"
duration: "15:50"
type: "video"
tags: ["ai-hype", "security", "enterprise-ai"]
curriculum_modules: ["06-strategy-and-economics"]
---

# 414: Delve faked SOC2. That's worse than SOC2 itself.

> **Creator**: Zack Korman | **Platform**: YouTube | **Date**: 2026-03-28 | **Duration**: 15:50

## Summary

Zack Korman delivers a pointed critique of Delve, a compliance startup that was caught fabricating SOC 2 and ISO 27001 audit reports. Rather than engaging with the genuine fraud, a vocal segment of the security community responded with "SOC 2 has always been meaningless anyway" — a hot take Korman argues is both intellectually lazy and actively harmful. The core scandal: Delve blurred the line between compliance platform and auditor so completely that they were effectively generating their own audit reports, rubber-stamped by US shell companies backed by teams in India who did no real work.

Korman traces the structural progression that enabled this fraud: legitimate compliance platforms like Vanta introduced "trusted auditor networks" for convenience, which gradually eroded the independence that makes third-party audits meaningful. Delve took this to its logical extreme — customers never spoke to auditors, reports were copy-pasted boilerplate with identical typos across hundreds of companies, and no exceptions were ever noted (a statistical impossibility in real auditing). When the scandal broke, several Delve customers quietly removed Delve branding from their trust centers while continuing to display the fraudulent certifications — behavior Korman characterizes as knowing complicity.

The broader argument is that cynicism about compliance standards creates the conditions for fraud to thrive. When GRC professionals dismiss SOC 2 as theater, they inadvertently signal to companies that cutting corners — or outright cheating — carries no real reputational cost. Korman insists that imperfect standards with genuine audit processes are categorically better than fraud, and that companies cannot scale enterprise trust without some form of third-party verification, however imperfect.

---

## Key Concepts

### Auditor Independence as a Structural Safeguard
The foundational principle of compliance auditing is that the compliance platform (evidence collection, workflow tooling) and the auditor (independent verification) must remain separate. When Korman went through ISO 27001 at his prior company, his Vanta-unfamiliar auditor's annoyance was a feature, not a bug — it demonstrated genuine independence. Delve systematically dismantled this separation until customers never interacted with auditors at all, making fabrication trivially easy.

### Trusted Auditor Networks as a Slippery Slope
Platforms including Vanta introduced preferred auditor referral networks ostensibly for customer convenience. Korman identifies this as the inflection point: once a small audit firm depends on platform referrals for deal flow, it has a structural incentive not to create friction for platform customers. This dynamic degrades audit rigor even without explicit fraud, and created the organizational infrastructure Delve later exploited.

### Compliance Fraud Enablement via Customer Complicity
Several Delve customers responded to the scandal by quietly removing Delve branding while continuing to display the fraudulent certifications. This is distinguishable from ignorance: the audit reports contain claims (e.g., contractor sampling, workstation inspection) that companies would know to be false about their own operations. Korman argues these companies are complicit, not merely unfortunate victims, and should face accountability.

### The "Standards Are Theater" Fallacy
A recurring security community response to the scandal was "SOC 2 was always fake anyway." Korman argues this creates a race to the bottom: if GRC professionals signal that certifications are meaningless, companies rationally deprioritize genuine compliance investment, which further degrades standards quality, which confirms the cynics' priors. The alternative — imperfect but genuinely pursued standards — is strictly preferable to fraud, even if neither is perfect security assurance.

### Scalability Requirement for Enterprise Trust
Korman's defense of compliance frameworks rests on a practical argument: large enterprises like Coca-Cola cannot audit every vendor directly. Third-party standards exist to make trust relationships scalable. There is no realistic alternative that doesn't involve either universal vendor auditing (impossible at scale) or some form of certification framework. Dismissing these frameworks without proposing alternatives is not a serious position.

---

## Practical Takeaways

- **Verify auditor identity and independence**: When reviewing a vendor's SOC 2 or ISO 27001 report, check the named audit firm independently. If the auditor is unknown or difficult to verify as a real operating entity, treat the certification with skepticism.
- **Red flags in audit reports**: Identical boilerplate language across different companies' reports, zero exceptions noted, and vague sampling claims ("we selected a sample of contractors") when the company has no contractors are signs of fabricated reports rather than legitimate audits.
- **Customer never speaking to auditor is a structural failure**: If your compliance platform offers to handle all auditor interaction on your behalf, insist on direct auditor engagement. Absence of that interaction should be treated as a disqualifying red flag, not a convenience feature.
- **Complicity has reputational and legal exposure**: Companies that knowingly circulate fraudulent certifications to close enterprise deals face real downstream liability when the fraud surfaces, regardless of whether they were the ones who fabricated the reports.
- **Cynicism about standards accelerates their degradation**: Security practitioners who publicly dismiss compliance frameworks create cover for companies to pursue fraudulent shortcuts. Constructive criticism of standards is distinct from wholesale dismissal.

---

## Notable Quotes

> "There is some subset of the compliance infosec cybersecurity community that has just lost their minds on this issue. They have this desire to be so edgy that they have to hit you with this hot take about how their personal pet peeve with SOC 2 is somehow underlying Delve committing fraud."

> "If you as a company put a lot of work into your ISO 27001 and then you go to sell to Coca-Cola and the first thing you encounter is a GRC person who says 'standards are fake' — damn it, okay, next time we need to do it, we're hiring the fraud one. Why? Cause you don't care anyways."

> "You don't get to self-decide that you believe your audit was real because I'm looking at your audit and it looks fake."

---
