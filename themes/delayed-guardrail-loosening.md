---
theme: Should loosening a guardrail take time?
status: emerging
first_seen: 2026-11-02
last_seen: 2026-11-23
weeks: 2
---
**Thesis so far:** Delegation designs are converging on asymmetric guardrails, where tightening is instant and loosening waits, which turns "undo" into a time window the user must notice rather than a setting they can flip.

## Evidence
- 2026-11-02 · 🟡 · Safe announces a Policy Engine (planned Q4 2026) in which removing or loosening a policy requires a delay. https://safe.global/blog/introducing-the-safe-policy-engine
- 2026-11-23 · 🟡 · Draft ERC "Policy-Enforced Agent Accounts" (ERCs PR #2196) publishes pending loosenings with an `effectiveAt` time, cancellations and an emergency stop. https://github.com/ethereum/ERCs/pull/2196

## Counter-evidence
- Both items are early: an announcement and a draft PR. Nothing in the archive has shipped the delay to users yet.

## Open question
When a delayed loosening is pending, who is told, and what can they do in the window?
