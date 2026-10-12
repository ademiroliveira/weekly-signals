---
description: Run the weekly Self-Custody & Sovereignty Signal Report. Sync, set the window, research, verify, synthesize, check the draft, archive, render, publish, update themes, commit, notify.
---

Compile this week's **Self-Custody & Sovereignty Signal Report**. All rules (window, repeats, tags, strength rubric, vocabularies) are in `CLAUDE.md`.

Artifact: `https://claude.ai/artifact/G1ftZVaD68n3Guq65H7LSQ`. Use the scratchpad for temporary files.

## Step 0: Sync the archive and set the window
1. **Sync.** List the artifact's files (Artifact `list`, `scope: "files"`, with the artifact URL). For every `signals/*.md` the artifact has and the repo doesn't, read it (`action: "read"`, `paths`) and copy it into `signals/` unchanged. Never overwrite a file that already exists in the repo.
2. **Window.** Run `python3 scripts/signals.py prior` and keep its output.
   - If `report_exists_for_today` is true, stop and send a notification. Never overwrite a report.
   - If `window.empty` is true, stop and send a notification.
   - Note `gap_days` for the Source Audit.

## Step 1: Research (5 agents IN PARALLEL)
Spawn `keys-recovery`, `hardware-threats`, `policy-institutions`, `agentic-wallets` and `wallet-ux` at once. Give each one:
- today's date
- the window start and end
- the full `seen` list (URL + title + report)

## Step 2: Route and merge
- **Hand-offs.** For each hand-off URL that no agent returned as an item, fetch it and write it up in the researcher format yourself.
- **Merge** items that cover the same story into one item. Keep the strongest primary source as `url` and move the rest to `also:`.
- **Drop** anything whose URL is in the `seen` list, unless it's a true Update (a new primary document in the window, titled "Update: …", with `update_of`).

## Step 3: Verify (2 verifiers IN PARALLEL, mode `items`)
Split the candidates evenly. Give each verifier the window and the seen list. Drop every FAIL and apply every ADJUST. Keep the reasons for the Source Audit.

## Step 4: Synthesize
- **Top 3:** the three items with the greatest effect on who holds keys or how custody works, chosen from 🟠/🔴 items (the rule is in `CLAUDE.md`).
- **UX & Interaction:** `wallet-ux` items, plus `agentic-wallets` items whose source shows a user-facing change. If an item's `ux_pattern` is `new:`, either adopt it (add a row to `reference/ux-patterns.md` and use the slug) or map it to an existing slug.
- **On the radar:** every other verified item.
- **Patterns across weeks:** compare this week's items with earlier reports (the `prior` output, `signals/` and `themes/`). Look for:
  - a `ux_pattern` seen before
  - an `update_of` chain
  - the same mechanism coming back in another domain (e.g. post-quantum migration in a standard, then a regulator, then a wallet)

  Write 1–4 bullets. Each bullet names the thread as a design question, says what came back, and cites item ids from at least two different reports. If nothing recurs, write "No recurring patterns this week."
- **Pulses:** one sentence each, or "None this week."
  - **Academic**
  - **Regulatory**
  - **Developer channels** (Optech, mailing lists, GitHub)
  - **Narrative shift**, only when two or more verified items this week point the same way, and cite them

## Step 5: Draft check
Write the report to a scratch file in the format below. Run one `verifier` in mode `draft` on it. Apply every REMOVE and FIX. Never add new claims at this stage.

## Step 6: Archive (append-only)
Copy the draft to `signals/<today>.md`. **Never overwrite an existing file.** Run `python3 scripts/signals.py validate signals/<today>.md`. Fix every error by correcting the format (never by changing facts) until it passes.

## Step 7: Render and publish
1. Run `python3 scripts/signals.py render --out <scratchpad>/index.html`.
2. Publish it to the artifact URL with `files: {"signals/<today>.md": "<repo>/signals/<today>.md"}`. Never pass `null` for an existing file.

The page is generated, so don't edit the HTML by hand.

## Step 8: Update themes
Follow `.claude/commands/connect.md` over the last 8 reports. Keep it brief: update the existing theme files, and add a new one only when a thread spans 2+ reports.

## Step 9: Commit
`git add signals/ themes/ reference/ux-patterns.md && git commit -m "signals: week of <window>" && git push`. Retry a failed push once at most. The week is already safe in the artifact.

## Step 10: Push notification
Send it with the summary in `<routine_summary>` tags. The first sentence is the banner. Include:
- the Top 3 titles with their strength
- the window
- one line for UX if there's a UX item
- one line for Patterns if any
- the kill count
- any problem: a failed push, a newly blocked source, a gap in the window, or a sync that copied weeks

If the notification fails, the run still counts as complete.

---

## Report format

```markdown
---
report: self-custody-sovereignty
week: YYYY-MM-DD..YYYY-MM-DD          # exactly the window from `prior`
generated: YYYY-MM-DD
verified: <n>
killed: <n>
items:
  - id: <yyyy-mm-dd>-<short-slug>
    title: "<title>"
    section: top | ux | radar
    stage: early | formal | in-force
    strength: strong | emerging | weak
    origin: academic | standards | regulatory | institutional | technical | journalism
    domains: [..]
    source_type: "[..]"
    url: <url>
    published: YYYY-MM-DD
    also: [<url>, <url>]        # optional
    update_of: <earlier id>     # Updates only
    ux_pattern: <slug>          # ux items only
---

# Self-Custody & Sovereignty Signal Report — Week of <Mon D – D, YYYY>

## Top 3 Signals

### 1. <Title>
🔴 Strong · <stage> · <origin> · <domains> · [source type]

**Summary:** what the source says, 1–3 sentences.
**Filter:** one sentence on WHO holds the keys or HOW sovereignty is exercised.
**Source:** [source type] <url> · <date>
**Also:** <url> · <url>

## UX & Interaction Signals

### <Title>
🟠 Emerging · <stage> · <origin> · <domains> · [source type] · `<ux_pattern>`

**What changed:** what the source states changed for the user.
**Experience filter:** what the user must now understand, decide or do.
**Design read (analysis):** one sentence of interpretation.
**Source:** [source type] <url> · <date>

(or "No new signals this week.")

## On the radar
- **<Title>** · 🟡 Weak · <origin> · <domains>: one sentence. [source type] <url> · <date>

## Pulses
- **Academic:** …
- **Regulatory:** …
- **Developer channels:** …
- **Narrative shift:** …

## Patterns across weeks
- **<Design question>:** what came back this week. (`<id>`, `<id>`)

## Source Audit
Window: <start>..<end> · previous report: <file> · gap: <n> days
Kill count: <n>
- FAIL <title>: <reason>
- ADJUST <title>: <field> <old> → <new>: <reason>

By agent:
- <agent>: <n> fetched → <n> blocked → <n> in window → <n> verified → <n> included

Source status changes: <any source whose status differs from reference/sources.md, or "none">
```
