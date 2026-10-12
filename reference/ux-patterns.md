# UX pattern vocabulary

Every `ux` item gets **one** `ux_pattern` value from the **Pattern** column, so `/connect` can count the same pattern across weeks. Use the slug exactly.

If nothing fits, the wallet-ux agent may propose `new: <slug> — <one-line definition>`. Synthesis decides whether to adopt it. If it does, it adds a row here in the same run and uses the new slug. Never create a near-duplicate of an existing row. Widen the existing row's definition instead.

| Pattern | Definition | Seen |
|---|---|---|
| `comprehension-gate-before-delegation` | An explanation screen the user must pass before granting another party (co-signer, proposer, agent, spending limit) power over funds. | 2026-09-28 Safe proposer modal and spending-limits pre-flow |
| `bundled-protection-toggle` | Several protections (simulation, phishing checks, alerts) controlled by one all-or-nothing switch, so users trade them away together. | 2026-10-05 MetaMask Basic Functionality |
| `partial-enforcement-perimeter` | Limits or guards that apply to some of an agent's or app's actions but not others, without the boundary being shown to the user. | 2026-10-05 MetaMask Agent Wallet Guard Mode |
| `privacy-custody-tradeoff-disclosure` | Before entering a private or shielded mode, the user is told what verifiability, recovery or exit options change. | 2026-10-05 and 2026-10-07 Safe × Bermuda |
| `outcome-bound-signing` | The user signs a guaranteed outcome (assertion, post-condition) rather than raw calldata. The transaction reverts if the outcome isn't met. | 2026-10-07 Ethereum transaction assertions |
| `device-provenance-check` | Custody depends on confirming where a signing device came from and that it wasn't tampered with before seed generation. | 2026-10-12 Ledger reseller supply-chain attack |

## Older free-text values

Reports before 2026-10-19 used free-text `ux_pattern` sentences. `/connect` maps them like this:

| Original value (prefix) | Pattern |
|---|---|
| comprehension gate before delegation | `comprehension-gate-before-delegation` |
| binary security/privacy tradeoff gate at onboarding | `bundled-protection-toggle` |
| selective evaluation perimeter for agentic delegation | `partial-enforcement-perimeter` |
| opt-in privacy overlay on existing multisig confirmation flow | `privacy-custody-tradeoff-disclosure` |
| privacy-custody trade-off disclosure gate | `privacy-custody-tradeoff-disclosure` |
| assertion-backed authorization | `outcome-bound-signing` |
| device-provenance verification as an unscaffolded custody precondition | `device-provenance-check` |
