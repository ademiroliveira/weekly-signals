---
theme: Who decides what happens to a key that time has made unsafe?
status: emerging
first_seen: 2026-09-28
last_seen: 2026-09-28
weeks: 1
---
**Thesis so far:** Post-quantum migration will be the largest forced key rotation in self-custody's history. The protocol layer is already writing the rules, including freezing accounts and defining who can recover them, before anyone has designed how a user is told, warned or walked through it. This is a gap where UX can be written first.

## Evidence
- 2026-09-28 · 🟠 · Draft EIP PR #12383: Quantum Freeze and Account Recovery. It proposes freezing legacy ECDSA accounts that miss the migration window and defining successor recovery paths. In effect, control moves to whoever controls the recovery mechanism. https://github.com/ethereum/EIPs/pull/12383
- 2026-09-28 · 🟠 · SoK: Post-Quantum Multi-Party Signature Aggregation. A survey of 30+ PQ multi-party schemes with a blockchain taxonomy. The PQ replacement for today's MPC/multisig wallets is being mapped now. https://eprint.iacr.org/2026/2222
- 2026-09-28 · 🟡 · Threshold ML-KEM via MPC. Cuts threshold decapsulation from 384 rounds to as few as 35, which moves PQ threshold custody closer to practical latency. https://eprint.iacr.org/2026/2220
- 2026-09-28 · 🟡 · W3C VC Data Model Threat Model v2.1. Lists quantum obsolescence as an attack vector for credentials, not only for coins. https://www.w3.org/TR/2026/DNOTE-vc-data-model-threat-model-2.1-20260924/
- Context only (not a verified signal: killed on tag in the Source Audit): Bitcoin Optech #424 covered PQLN (post-quantum Lightning).

## Counter-evidence
- EIP #12383 is a draft PR pending editor review. Freeze proposals are politically contested and may never reach mainnet.
- Q-day timing is uncertain. Designing migration UX now may be premature relative to other priorities.

## Gap
**No UX signal yet.** Nothing in the archive shows a wallet designing a migration prompt, a "your account will be frozen" warning, or a PQ recovery flow. This is the thread to write first.

## Open question
Does EIP #12383 advance (editor review, Magicians consensus), or does a wallet ship any PQ-migration UI? Either would move this from gap to active thread. If the EIP stalls and no wallet moves, the theme cools.
