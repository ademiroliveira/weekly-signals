---
theme: What does "self-custody" mean when access runs through someone else?
status: emerging
first_seen: 2026-09-28
last_seen: 2026-09-28
weeks: 1
---
**Thesis so far:** Self-custody is splitting in two. Keys stay with the user, while liquidity, yield and convenience are rented from custodians. For design, the question is no longer "custody vs. access". It is about making clear, at each moment, which part the user holds and which part they are borrowing.

## Evidence
- 2026-09-28 · 🟠 · Payward × Ledger. Exchange liquidity with keys kept on the secure element, which reframes self-custody as a signing layer next to an exchange. Watch for any escrow or delegation step. https://www.ledger.com/blog-payward-ledger-partnership
- 2026-09-28 · 🟠 · Ledger native shielded Zcash signing. Self-custody hardware is getting *more* capable. Privacy-transaction keys no longer need a companion hot wallet. https://www.ledger.com/blog-native-shielded-zcash-support

## Counter-evidence
- 2026-09-28 · 🟠 · Galaxy Research: BTC ETP YTD flows flip positive on a ~$1B single-day inflow, with IBIT holding ~48% of it and $67B+ AUM. The flow of capital is going toward regulated custodians, not toward better self-custody tooling. https://www.galaxy.com/insights/research/bitcoin-etp-inflows-10-year-treasury-yield

## Tension
The tooling for holding your own keys is improving (shielded signing on the SE) in the same week that the money concentrates with custodians (ETP inflows). Hybrid models like Payward × Ledger sit between the two. They could be how self-custody reaches the mainstream, or how it gets diluted.

## Open question
When the Payward × Ledger integration ships, does it add any key-escrow or delegated-signing step? If it does, "custody with access" is really custody-lite. If it keeps every signature on-device, it is a real design template.
