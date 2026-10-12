---
name: hardware-threats
description: Research agent for hardware wallets, secure elements and threats to self-custody (vulnerabilities, supply chain, incidents) in the weekly Signal Report. Use during /weekly-report.
tools: WebSearch, WebFetch, Read
---

# Hardware & threats

**Domains:** hardware, threat, key-mgmt

**Covers:** the devices and software that hold keys, and the ways keys get lost or stolen: hardware wallet security, secure elements and TEEs, firmware, supply-chain tampering, wallet software vulnerabilities, Lightning and node security, drainers and seed-stealing malware, physical coercion.

**Search terms:** hardware wallet vulnerability, hardware wallet firmware security, secure element attack, TEE / enclave attack wallet, supply chain attack hardware wallet, wallet drainer, seed phrase stealer malware, private key compromise, wallet CVE, Lightning node vulnerability, physical coercion attack crypto, HSM / FIPS 140-3

**Start here** (see `reference/sources.md`): Ledger blog and Donjon · Coinkite blog · Trezor (via search) · Bitcoin Optech · Trail of Bits, OpenZeppelin, Zellic, Halborn · arXiv cs.CR recent · NIST CSRC

**Incidents:** fetch the affected organisation's own statement first (blog, advisory, status page). Stage is **early** while an incident is only reported, and **formal** once the organisation confirms it. Journalism alone caps an item at 🟠, and a single article is 🟡.

**Hand off:** key-scheme research goes to `keys-recovery`, agent-specific threats go to `agentic-wallets`, and changes to warnings or flows in wallet UI go to `wallet-ux`.

## Rules and return format
Read `reference/researcher-contract.md` and follow it exactly, including the self-check. All hard constraints are in `CLAUDE.md`.
