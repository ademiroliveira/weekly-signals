---
description: Run the weekly Self-Custody & Sovereignty Signal Report — research, verify, archive to signals/, publish the artifact, notify.
---

Compile this week's **Self-Custody & Sovereignty Signal Report**. Follow `CLAUDE.md` for all hard constraints, the source hierarchy and the strength definitions.

## Step 1 — Research (8 agents IN PARALLEL)
Spawn all 8 at once: `key-management`, `hardware-enclaves`, `recovery-identity`, `regulatory-policy`, `sovereign-adoption`, `threat-vectors`, `agentic-wallets`, `wallet-ux`. Pass each one today's date and the 7-day cutoff date.

## Step 2 — Verify, then synthesize
Split all candidate items between **2 `verifier` agents** running in parallel. Drop every FAIL and keep the kill count and reasons for the Source Audit.

Apply the relevance filter (or the experience filter for wallet-ux items) to every surviving item, then build the report.

## Step 3 — Archive (append-only)
Write `signals/<today YYYY-MM-DD>.md`. **Never overwrite an existing file.** If one exists for today, stop and ask.

Use this exact structure so `/connect` can parse it:

```markdown
---
report: self-custody-sovereignty
week: YYYY-MM-DD..YYYY-MM-DD
generated: YYYY-MM-DD
verified: <n>
killed: <n>
items:
  - id: <yyyy-mm-dd>-<short-slug>
    title:
    section: top | ux | weak
    strength: strong | emerging | weak
    origin:
    domains: [..]
    source_type: "[..]"
    url:
    published: YYYY-MM-DD
    ux_pattern:        # wallet-ux items only
---

# Self-Custody & Sovereignty Signal Report — Week of <range>

## Top 3 Signals
### 1. <Title>
🔴/🟠/🟡 · origin · domains · [source type]
**Summary:** …
**Filter:** …
**Source:** [source type] <url> · <date>

## UX & Interaction Signals
(same format; "No new signals this week." if empty)

## Weak Signals to Watch
- **<Title>** · 🟡 · origin · domains — one sentence. [source type] <url>

## Pulses
- **Academic:** …
- **Regulatory:** …
- **Social sentiment** (mailing lists / GitHub / Optech only): …
- **Narrative shift:** …

## Porto / Agentic Wallet Lens
1–2 implications, only if supported by this week's verified findings. Weight wallet-ux findings most heavily. Skip if no direct connection.

## Source Audit
Kill count: <n>
- FAIL <title>: <reason>
- <domain>: fetched → blocked → in-window → verified → included
```

## Step 4 — Publish the artifact
Render the same content as self-contained HTML following `reference/report-style.md`. Update the existing artifact "Self-Custody & Sovereignty Signal Report" in place (use Artifact `list` to find it), or publish a new one if it's missing. Add a footer link to this repo's `signals/` folder so every past week stays reachable.

## Step 5 — Commit
`git add signals/ && git commit -m "signals: week of <range>" && git push`

## Step 6 — Push notification
Send the Top 3 titles with their strength, the date range and a note that the full report is in the artifact. If the UX section produced something notable, add one line for it. **If the notification fails, still count the run as complete:** the report and commit are what matter.
