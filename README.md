# weekly-signals

AO's weekly **Self-Custody & Sovereignty Signal Report**, archived week by week and used to write articles on UX and product design.

## How it works

```
Monday (scheduled)       /weekly-report   sync → window → 5 research agents → 2 verifiers → draft check
                                          → signals/YYYY-MM-DD.md → validate → render artifact → themes → commit → notify
Whenever you're writing  /connect         all weeks → themes/        (recurring threads, tensions, gaps)
                         /angle           themes → articles/ideas.md (claims with evidence)
                         /draft <angle>   → articles/drafts/         (in AO's voice, every claim cited)
```

- `signals/`: one report per run. Append-only, nothing is ever overwritten. Each run covers the days since the previous report (7 at most), and never repeats an item.
- `scripts/signals.py`:
  - `prior`: the window and the already-covered items
  - `validate`: the format gate
  - `render`: the artifact page, with every week browsable in-page
- `reference/`:
  - `sources.md`: tested source entry points and the journalism allowlist
  - `ux-patterns.md`: the pattern vocabulary
  - `researcher-contract.md`: shared agent rules
  - `report-style.md`: the visual spec
- `.claude/agents/`: `keys-recovery`, `hardware-threats`, `policy-institutions`, `agentic-wallets`, `wallet-ux`, `verifier`.
- `themes/`: running design questions that show up across weeks.
- `articles/`: ideas → drafts → published.
- `CLAUDE.md`: hard constraints, the strength rubric, vocabularies and writing voice, shared by everything.

This repo is public, so no employer or internal product details go in it.

Open the folder in Claude Code (or a Cowork session with this repo as a source) and run any command.
