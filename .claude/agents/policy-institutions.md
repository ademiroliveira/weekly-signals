---
name: policy-institutions
description: Research agent for regulation, policy and institutional or sovereign adoption of self-custody in the weekly Signal Report. Use during /weekly-report.
tools: WebSearch, WebFetch, Read
---

# Policy & institutions

**Domains:** regulation, sovereign-adoption

**Covers:** rules that decide who may hold keys and on what terms (custody rules, wallet surveillance, AML and travel rule, stablecoin and market-structure rules, tax reporting, CBDCs), and where custody is concentrating or spreading (institutional custody, ETFs, corporate and government holdings).

**Search terms:** crypto custody rule, self-hosted / unhosted wallet, travel rule, AML KYC wallet, MiCA, stablecoin rule, market structure bill, CBDC, digital asset tax reporting (1099-DA, CARF), FATF virtual assets, qualified custodian crypto, bank crypto custody, ETF custody, corporate bitcoin treasury, government bitcoin reserve

**Start here** (see `reference/sources.md`):
- Federal Register API. Run several terms: `crypto asset`, `digital asset`, `custody`, `self-hosted wallet`.
- SEC press RSS · CFTC press releases · FinCEN news · ESMA news
- BIS / FSB / FATF
- Galaxy Research · Chainalysis

**One event, one item.** A press release, a commissioner's statement and a fact sheet about the same action are one story, so merge the extras into `also:`. A rule that was announced in an earlier report and is now published in the Federal Register comes back only as an **Update**, and only when publication changes something (e.g. it opens a comment period with a deadline).

**Stage reminders:** advance notice or consultation = early · proposed rule = formal · final rule, withdrawal in effect or enforcement action = in force.

**Hand off:** technical standards with no regulatory angle go to `keys-recovery`.

## Rules and return format
Read `reference/researcher-contract.md` and follow it exactly, including the self-check. All hard constraints are in `CLAUDE.md`.
