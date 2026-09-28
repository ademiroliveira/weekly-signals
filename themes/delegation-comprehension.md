---
theme: Does the user understand what they are handing over before they hand it over?
status: emerging
first_seen: 2026-09-28
last_seen: 2026-09-28
weeks: 1
---
**Thesis so far:** Delegation screens are where custody quietly changes hands, and the form should never be where users first learn what they are granting. Explanation has to come before configuration, and agent sessions need this more than any human co-signer role does.

## Evidence
- 2026-09-28 · 🟠 · Safe{Wallet} web-v1.101.0: proposer role modal. Before this release, users could give a third party transaction-queue rights with no explanation that a proposer can submit transactions without co-signing. The release adds a comprehension gate at that point. `ux_pattern: comprehension gate before delegation`. https://github.com/safe-global/safe-wallet-monorepo/releases/tag/web-v1.101.0
- 2026-09-28 · 🟠 · Safe{Wallet} web-v1.101.0: spending limits pre-flow. A new explanation screen appears before the ceiling is set, so users learn they are granting unilateral transfer rights. This is a second, independent gate in the same release. https://github.com/safe-global/safe-wallet-monorepo/releases/tag/web-v1.101.0
- 2026-09-28 · 🔴 (see caveat) · Budgeted Threshold Signatures (IACR 2026/2176). The paper gives 100M+ agent payments on one chain in under a year as its motivation, so the volume of delegation that needs explaining is growing fast. https://eprint.iacr.org/2026/2176

## Counter-evidence
- Both Safe items come from **one vendor in one release**. That is one team's design decision, not an industry pattern yet.
- Friction cost: expert users dismiss explanation modals. Nothing in the archive yet shows whether these gates change comprehension or only add clicks.

## Open question
Will a second wallet, ideally an agentic one (session keys, agent permissions), ship an explain-before-delegate step? Or will research show that users still misread scope after a gate like this? The first would confirm the thesis. The second would push it toward "explanation isn't enough, the scope must be visible after the grant as well".
