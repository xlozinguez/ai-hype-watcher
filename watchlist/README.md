# Watchlist

YouTube channels and content sources monitored for AI-assisted development content.

## Channels

| Channel | Focus | Priority |
|---------|-------|----------|
| [Bart Slodyczka](https://www.youtube.com/@BartSlodyczka) | Claude Code tutorials, agent teams | high |
| [IndyDevDan](https://www.youtube.com/@indydevdan) | Principled agentic coding, hooks/skills/tasks | high |
| [Nate B Jones](https://www.youtube.com/@NateBJones) | AI strategy, infrastructure economics | high |
| [Confluent Developer](https://www.youtube.com/@ConfluentDeveloper) | Event streaming, AI + data platforms | medium |
| [The PrimeTime](https://www.youtube.com/@ThePrimeTimeagen) | AI tool reviews, security, critical perspective | medium |
| [Leon van Zyl](https://www.youtube.com/@LeonvanZyl) | Claude Code skills tutorials, agent teams | medium |
| [Internet of Bugs](https://www.youtube.com/@InternetOfBugs) | Critical AI analysis, hype debunking | medium |
| [Ali H. Salem](https://www.youtube.com/@AliHSalem) | AI productivity skills, workflows | low |

## Configuration

Channel definitions with keywords and priorities are in [`channels.yaml`](channels.yaml).

## Workflow

Use `/scan-channels` to check for new relevant content:

```
/scan-channels                    # Scan all high-priority channels
/scan-channels all                # Scan all channels
/scan-channels @indydevdan        # Scan a specific channel
```

When relevant content is found, use `/synthesize-source` to create source notes.
