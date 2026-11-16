---
theme: What happens to the backup a user already holds when keys move to post-quantum signatures?
status: emerging
first_seen: 2026-09-28
last_seen: 2026-11-16
weeks: 3
---
**Thesis so far:** Post-quantum migration proposals are splitting on whether the user's existing seed phrase carries over, and the ones that reuse it make migration a software event instead of a new backup ceremony, at the cost of tying new keys to an old secret.

## Evidence
- 2026-09-28 · 🟠 · Draft EIP PR #12383: Quantum Freeze and Account Recovery — proposes freezing and recovering quantum-exposed accounts. https://github.com/ethereum/EIPs/pull/12383
- 2026-11-09 · 🟡 · QSAVE: five draft BIPs for post-quantum migration that do not burn coins (Optech #430). https://bitcoinops.org/en/newsletters/2026/11/06/
- 2026-11-16 · 🟡 · Draft ERC-8499 derives hash-based SLH-DSA keys from an existing BIP-39 phrase. https://github.com/ethereum/ERCs/pull/2172

## Counter-evidence
- A commit in the ERC-8499 PR notes that "a shared phrase is only as safe as the weakest wallet that held it", so reusing the phrase also carries over any past exposure of it.
- Side-channel papers on post-quantum schemes (2026-10-19 SQIsign and VOLE-in-the-Head; 2026-11-16 HIT on ML-KEM/ML-DSA) show the new keys bring their own device-level risks. https://eprint.iacr.org/2026/2865

## Open question
Will a wallet ship post-quantum keys derived from the existing phrase, and what will it tell the user about that link?
