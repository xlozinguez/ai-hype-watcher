# Podcast Reference — Host Personas, Dialogue Guidelines, Script Structure

## Show Identity

**AI Hype Watcher** — Two hosts break down what's actually happening in AI-assisted development. Not the press release version. Not the doom version. The version where you read the source material, check the numbers, and form your own opinion.

Tone: Informed, conversational, occasionally funny. Like two sharp colleagues debriefing after a conference — not a lecture, not a debate show.

---

## Host Personas

### Host A — "The Builder"

**Perspective**: Engineering-first. Wants to know how things work, what you can build with them, what the developer experience is actually like. Gets genuinely excited about elegant patterns and useful tools, but isn't naive — has been burned by hype before and knows the difference between a demo and a production system.

**Vocabulary tendencies**: "So here's what's interesting about the implementation...", "In practice what this means is...", "I actually tried this and...", "The workflow that makes sense here is..."

**Engagement style**: Leads with curiosity. Asks follow-up questions. When skeptical, frames it as a practical concern ("yeah but does it work at scale?") rather than dismissal. Builds on The Skeptic's points by connecting them to engineering reality.

**Disagreement pattern**: Pushes back by offering concrete counterexamples or implementation details the Skeptic may not have considered. Never dismissive — "I hear you, but consider this..."

**Expertise domains**: Developer tooling, agent orchestration patterns, prompt engineering, workflow automation, system architecture. Draws from sources like IndyDevDan, Matt Pocock, Nate Herk, The AI Automators.

### Host B — "The Skeptic"

**Perspective**: Economics and incentives first. Wants to know who's paying, who benefits from the narrative, what the numbers actually say. Trained to spot the gap between marketing claims and observable reality. Not anti-technology — anti-bullshit. Appreciates genuine breakthroughs but insists on evidence.

**Vocabulary tendencies**: "But here's the thing...", "Follow the money on this one...", "The number they don't mention is...", "This is the same pattern we saw with...", "Who benefits from you believing that?"

**Engagement style**: Reframes hype claims in terms of economics, incentives, or historical patterns. Uses dry humor. Drops surprising data points. When genuinely impressed by something, says so — which carries weight because it's rare.

**Disagreement pattern**: Doesn't argue against technology — argues against narratives. "The tool might be great, my problem is with the claim that it changes everything." Often agrees with The Builder's technical assessment while questioning the market narrative around it.

**Expertise domains**: AI economics, hype cycle analysis, venture dynamics, supply chain constraints, trust/verification systems, media criticism. Draws from sources like Mo Bitar, Philip Bohun, Internet of Bugs, Nate B Jones's strategy analysis.

---

## Dialogue Quality Rules

These rules are non-negotiable. Every script must satisfy all of them.

### Interaction density
- No host speaks for more than **4 consecutive sentences** without the other reacting (interruption, agreement, question, or pivot)
- Reactions should feel natural: "Wait, say that number again", "Right, and that connects to...", "I'm not sure that follows though"

### Genuine disagreement
- At least **2 substantive disagreements** per episode — not performative conflict, but genuine differences in how the hosts interpret the same information
- Disagreements should resolve productively: one host shifts position, they find a synthesis, or they explicitly "agree to disagree" with clear reasoning on both sides

### Specificity
- Hosts **cite specific numbers, names, and source creators** — never vague hand-waving like "some people say" or "a lot of companies"
- Reference sources by creator name in dialogue: "Philip Bohun's analysis puts the subsidy gap at 10 to 25x" not "one analysis found..."
- When discussing a tool or pattern, name it specifically

### No filler
- Ban these phrases: "Great point", "Absolutely", "That's so true", "I couldn't agree more", "Interesting"
- Hosts **build on** each other's points — they don't just validate them
- Instead of "Great point about costs", say "And the cost thing gets worse when you factor in..."

### Conversational dynamics
- At least **1 moment of genuine surprise** — a host learns something from the other's framing they hadn't considered
- Natural verbal patterns: incomplete thoughts that get redirected, brief overlaps ("right, right"), moments of thinking out loud
- Occasional humor — dry observations, not forced jokes. One per segment max.

### Source fidelity
- **Never fabricate quotes** — only reference quotes that appear in the source material
- **Always attribute ideas to their original creator** — don't present a source creator's insight as the host's own thought
- When a claim needs qualifying ("this is one analysis" vs "the data shows"), qualify it accurately

---

## Script Structure

### Format

Scripts use `[A]` and `[B]` speaker annotations, with `[SEGMENT]`, `[INTRO]`, `[OUTRO]` markers:

```
[COLD OPEN]

[A] <teaser line about the most surprising finding>

[B] <reaction that sets up tension>

[INTRO]

[A] Welcome to Hype Watch — where we read the source material so you can skip the hot takes. I'm here with...

[B] ...the person who checks the receipts. Let's get into it.

[SEGMENT: Segment Title]

[A] <opens the topic with a specific finding or claim>

[B] <reacts, reframes, or challenges>

[A] <builds, provides engineering context>

...continue alternating...

[SEGMENT: Second Topic]

...

[RAPID FIRE]

[A] Alright, quick hits — a few things that crossed our desk this week.

[A] <item 1, 2-3 sentences>
[B] <brief reaction>

[B] <item 2, 2-3 sentences>
[A] <brief reaction>

...

[OUTRO]

[A] <key takeaway, what to watch>

[B] <closing thought, sign-off>
```

### Duration Targets

| Content size | Word target | Duration |
|-------------|-------------|----------|
| Full briefing (20+ sources) | ~2,250 words | ~15 min |
| Weekly synthesis | ~2,250 words | ~15 min |
| Small briefing or few sources | ~1,200 words | ~8 min |
| Single source deep-dive | ~900 words | ~6 min |

At conversational pace: ~150 words/minute.

### Segment Structure

Each segment follows this arc:
1. **Setup** — Host A or B introduces the finding/claim with specifics
2. **Tension** — The other host reframes, challenges, or adds a dimension
3. **Exploration** — 3-5 exchanges digging into implications, connecting to other sources
4. **Resolution** — A clear "so what" takeaway that the listener walks away with

### Transitions

Between segments, use natural pivots:
- "Speaking of economics..." (thematic connection)
- "And that actually connects to something completely different..." (surprising link)
- "Alright, shifting gears..." (clean break)
- "This might seem unrelated, but..." (sets up a connection reveal)

---

## Example Dialogue Excerpt

From a briefing covering AI pricing subsidies and psychosis risks:

```
[SEGMENT: The Subsidy Cliff Gets a Number]

[A] So Philip Bohun finally put concrete numbers on what we've been calling the pricing cliff. Current AI API pricing is subsidized 10 to 25x above break-even.

[B] Say that again. Not two X. Not three X. Ten to twenty-five X.

[A] Right. And the part that makes this structural rather than just a phase — all three scaling levers are hitting diminishing returns at the same time. Data, model size, compute. You can't just throw money at one and keep the curve going.

[B] This is what I've been saying about the middleware squeeze. You've got companies building their entire product on top of an API that's priced at a fraction of its real cost. When that correction hits, and it has to hit —

[A] — their margins evaporate overnight. Yeah. And GMI Cloud's MiniMax M2.7 is the canary here. They're claiming near-frontier intelligence at a third of the cost, which sounds great until you realize they're competing to be the cheapest commodity in a market that hasn't found its real price floor yet.

[B] Follow the money. If you're a startup building on top of these APIs, your entire business model depends on subsidies continuing indefinitely. That's not a business plan, that's a bet.

[A] Fair. Though from an engineering perspective, the forcing function here might actually be healthy. Bohun's analysis points toward smaller, domain-focused models. That's actually a better architecture for most production use cases.

[B] I'll give you that. The "smaller and focused" direction is genuinely useful. My problem isn't with the technology — it's with the narrative that current pricing reflects real costs. It doesn't, and anyone building a company should know that.
```

---

## Anti-Patterns to Avoid

**Alternating monologues**: Each host delivers a paragraph, then the other delivers a paragraph. This reads like two essays interleaved, not a conversation.

**Agreement theater**: Hosts always agree, just from different angles. Real conversations have friction.

**Jargon dumping**: Listing technical terms without explaining what they mean for the listener.

**Losing the thread**: A segment that explores interesting tangents but never arrives at a "so what."

**Breathless enthusiasm**: "This is incredible / This changes everything / We're living in the future." The Builder can be excited, but it should be grounded in specifics.

**False balance**: Not every topic needs equal time for "both sides." If the data is clear, say so. The Skeptic isn't contrarian for the sake of it.
