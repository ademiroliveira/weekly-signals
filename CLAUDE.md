# Weekly Signals

This repo holds AO's weekly **Self-Custody & Sovereignty Signal Report** and turns its history into articles about UX and product design.

AO is a product design leader working on self-custody wallets, agentic wallet UX and Web3 product strategy.

> **This repo is public.** Never write employer names, internal product names, or internal implications into any file here: reports, themes, ideas or drafts. `python3 scripts/signals.py validate` rejects known internal names.

It has two layers:

1. **Signals.** Every Monday a scheduled run executes `/weekly-report`. Five research agents and two verifiers produce a report. It is archived to `signals/YYYY-MM-DD.md` (append-only), then rendered into the live artifact by `scripts/signals.py`.
2. **Writing.** `/connect`, `/angle` and `/draft` read across all past reports to find themes and write articles.

Live artifact: https://claude.ai/artifact/G1ftZVaD68n3Guq65H7LSQ

## Repo map

| Path | What |
|---|---|
| `signals/YYYY-MM-DD.md` | One report per run, named by run date. Append-only. |
| `scripts/signals.py` | `prior` (window + already-covered items) · `validate` (format/vocabulary gate) · `render` (artifact HTML from all weeks) |
| `reference/sources.md` | Tested entry points per source tier, and the journalism allowlist |
| `reference/ux-patterns.md` | Controlled vocabulary for `ux_pattern` |
| `reference/report-style.md` | Visual spec for the artifact |
| `themes/*.md` | Recurring threads across weeks, maintained by `/connect` |
| `articles/` | `ideas.md` (from `/angle`), `drafts/`, `published/` |
| `.claude/agents/` | 5 domain researchers + the verifier |
| `.claude/commands/` | `/weekly-report`, `/connect`, `/angle`, `/draft` |

---

## Hard constraints: apply before including ANY signal

1. **Report window.** The window runs from the day after the previous report's window end through today, inclusive. It is never longer than 7 days. If the previous report is older than that, the window is today − 6 through today, and the gap is noted in the Source Audit. `python3 scripts/signals.py prior` prints the window.
   - Only items whose publication date falls inside the window qualify, and the date must be visible on the page itself.
   - Never estimate, extrapolate or infer a date. Sequential IDs (ePrint numbers, arXiv IDs, PR numbers) are not evidence of a date.
   - For ePrint, use the paper's "Received" date, not "last updated". For arXiv, use the v1 submission date.
   - A rate-limited or robots-blocked source means the item is excluded (not estimated, not included with a caveat), and the block is noted in the Source Audit.
2. **No repeats across weeks.** An item whose URL already appears in an earlier report is excluded (`prior` lists them). A story already covered may come back only if a **new primary document inside the window** moves it forward, for example a proposed rule published in the Federal Register, or a fix that ships. It is then titled "Update: …" and carries `update_of: <earlier id>`.
3. **One story, one item.** Within a report, each story appears once, in one section. Other coverage of the same story is merged into that item's `also:` list. It never becomes a second item. A UX item needs its own source describing a user-facing change: a security incident is not a UX item just because it has design consequences.
4. **Strength rating required**, assigned with the rubric below.
5. **Source type tag required**, copied verbatim from the tag table below. An invented or hybrid tag excludes the item.
6. **No social media** as a primary source (X/Twitter, Reddit, Farcaster, Nostr, LinkedIn). Developer mailing lists are allowed.
7. **Fetched URLs only.** Only URLs that were actually fetched and confirmed to exist. Never guess a URL.
8. **Relevance filter.** Does this change WHO holds the keys or HOW sovereignty is exercised? If not, exclude it. (Wallet UX uses the experience filter in its agent file instead.)
9. **The source must say it.** A summary reports only what the source states, and every figure, name, version and date in it must appear on the page. Interpretation belongs only in the `filter` line (and `design_read` for UX items), and even there it must not assert facts. No universal claims such as "no wallet does X".
10. **If a domain yields nothing, say so:** "No new signals this week." Never pad, and never move an off-domain item in to fill a gap.

## Source hierarchy: search in this order

Tested entry points for every tier are in `reference/sources.md`. Use those before WebSearch.

1. **Academic & cryptography**: IACR ePrint, arXiv (cs.CR, cs.HC, cs.DC), peer-reviewed venues, MIT DCI, Stanford CBR
2. **Standards & specs**: EIPs/ERCs, W3C, NIST, BIS, FSB, FATF
3. **Regulatory**: Federal Register, SEC, CFTC, FinCEN, OCC, IRS, ESMA/EBA, other national regulators, central banks, legislatures
4. **Institutional research**: Galaxy Research, Chainalysis, a16z crypto, Messari, Coinbase Institutional, Delphi Digital
5. **Security firms & vendor advisories**: Trail of Bits, OpenZeppelin, Zellic, Halborn, Ledger Donjon; incident statements from the affected organisation
6. **Protocol teams & GitHub**: wallet release pages, protocol/foundation blogs, Bitcoin Optech, developer mailing lists
7. **Journalism**, as a fallback only, when tiers 1–6 yield fewer than 2 items for a domain, and the agent must say so. Only the four allowed outlets in `reference/sources.md` qualify.

For incidents and product changes, find the affected organisation's own statement before any journalism.

### Source type tags

| Tag | Use for |
|---|---|
| [IACR paper] | IACR ePrint papers |
| [arXiv paper] | arXiv papers |
| [Usable security paper] | Peer-reviewed HCI or usable-security papers (SOUPS, CHI, CSCW, USENIX Security, IEEE S&P) |
| [EIP] | EIPs/ERCs, including draft PRs |
| [W3C spec] | W3C specs and group notes at any maturity |
| [NIST pub] | NIST publications and drafts |
| [BIS paper] · [FSB report] · [FATF guidance] | Publications of those bodies |
| [Regulatory filing] | Official publications of regulators, legislatures, courts and law-enforcement agencies: rules, proposals, notices, withdrawals, press releases, enforcement actions |
| [Institutional report] | Research from financial institutions and crypto research firms |
| [Audit] | A formal security audit report of a specific codebase or system |
| [Vendor security report] | Security research, advisories or incident disclosures from a security firm, or from a vendor about its own product |
| [GitHub release] | A GitHub release page or merged PR **with notes on the page** |
| [Protocol blog] | Official blogs and newsletters of protocols, foundations, open-source projects and wallet products (incl. Bitcoin Optech) |
| [Verified journalism] | The four allowed tier-7 outlets only |

## Signal strength rubric

Strength describes **how solid the evidence is**, not how important the item is.

**Stage** of the development:
- **Early**: preprint, research or idea post, draft EIP/spec, advance notice, consultation or request for comment, reported but unconfirmed incident
- **Formal**: proposed rule, W3C Candidate Recommendation, EIP in Review or Last Call, peer-reviewed paper, security advisory with a fix, beta or early-access product, incident confirmed by the affected organisation
- **In force**: final rule or withdrawal in effect, enforcement action, W3C Recommendation, final EIP, generally available release, ratified standard

**Independent sources** are primary or institutional sources that don't just repeat each other. A news piece rewriting a press release isn't independent, and neither is a second statement from the same agency.

| | 1 source | 2+ independent sources |
|---|---|---|
| Early | 🟡 Weak | 🟠 Emerging |
| Formal | 🟠 Emerging | 🔴 Strong |
| In force | 🔴 Strong | 🔴 Strong |

Cap: if the only sources are tier-7 journalism, the item is at most 🟠, and a single article is 🟡.

**Ranking the Top 3:** pick the three items with the greatest effect on who holds keys or how custody works, among items rated 🟠 or 🔴. Strength is displayed, not used to sort. A 🟡 item may enter the Top 3 only if fewer than three 🟠/🔴 items exist.

## Vocabularies (enforced by `validate`)

- `section`: `top` · `ux` · `radar` (older reports use `weak` for the radar section)
- `strength`: `strong` · `emerging` · `weak`
- `stage`: `early` · `formal` · `in-force`
- `origin`: `academic` · `standards` · `regulatory` · `institutional` · `technical` · `journalism`
- `domains`: `key-mgmt` · `recovery` · `identity` · `hardware` · `threat` · `post-quantum` · `regulation` · `sovereign-adoption` · `agentic` · `ux`
- `ux_pattern`: a slug from `reference/ux-patterns.md`

---

## Writing layer

### Why the archive matters
One week is news. A pattern across weeks is a thesis. Articles should be built from **recurrence and tension across reports**, not from a single item.

### AO's article voice
- A design leader writing for designers and product people, not for cryptographers. Explain the mechanism in one sentence, then move on to what it means for the person using the product.
- Take a position. Every piece has a thesis you could disagree with.
- Get to the interface: what the user sees, understands, decides or delegates. A signal only matters for the article when it changes the experience.
- Use concrete references (a named release, paper or spec from the archive) rather than generic claims. Every factual claim links to its source URL in `signals/`.
- Show taste: restraint, precision, no hype. Include the strongest counterargument.
- Short paragraphs. No listicle filler. No emoji in articles.

### Rules for writing
- Cite only what exists in `signals/`. Never add facts from outside the archive without flagging them as `[needs source]`.
- Keep the report's signal strength honest in prose: a 🟡 preprint is "early research suggests", not "research proves".
- No employer, internal product names or internal implications anywhere in this repo. It is public.
