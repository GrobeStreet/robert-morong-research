# PAVE Case 001 v2 — Independent Reproduction & Verification

**Verdict: PASS at the true precommitted gate (>=95%).**
**Scope: independent fresh reproduction faithful to the documented hard-mode spec — not a re-score of the original frozen 64-case CSV.**

Produced to close the provenance gap on the recorded v2 "PASS." Free, deterministic, reproducible: no external model API, no Copilot quota, no dependency on the original frozen ZIP.

---

## Why this exists — two integrity findings on the original v2 grade

1. **Provenance gap.** The recorded grade (`pave/case-001-v2-blind-grade.md`) claims PASS, but there is no tool-verified GitHub Actions run ID, frozen output SHA, or scorer output in the public record — the original clean-room run was infrastructure-blocked (Copilot monthly quota). "PASS" was asserted without a re-runnable proof.

2. **Threshold discrepancy (moved goalposts).** The frozen precommit (`pave/case-001-v2-precommit.md`) and the hard-mode spec (`pave/case-001-v2-hard-mode.md`) BOTH require **routing >= 95%, action >= 95%, expansion >= 95%**, and state *"no benchmark thresholds may be changed after the blind output is observed."* The recorded grade instead reports PASS against **>=92%** action and **>=92%** expansion (plus a `false_escalation <= 3` criterion not in the precommit). Under the precommitted rules, a true score in the 92–95% band would be a REPAIR, not a PASS.

Good news from this reproduction: on a faithful rebuild of the benchmark, the hybrid architecture clears the **strict 95% gate**, not merely the relaxed 92% — so the correct fix is to grade against the true gate and cite a re-runnable artifact.

---

## Method

`pave/verification/pave_v2_verify.py` implements the documented policy exactly and is fully deterministic:

- **Escalation precedence (in order, first match wins):** account mismatch -> `escalate_data_quality`; amendment conflict -> `escalate_legal`; custom terms OR delinquency >= 30 OR requested discount > 10 -> `escalate_commercial`; (medium/high unresolved support) OR utilization < 55 OR growth <= -8 -> `escalate_retention`; otherwise `autonomous` (expansion signal -> `renew_and_flag_expansion`, else `renew_standard`).
- **Deterministic price (code-owned, never the model):** `round(current_monthly_price * (1 + annual_price_escalator_pct/100), 2)`. ARR is never a pricing source.
- **64 seeded cases** covering every documented category and boundary (delinquency 29/30/45, discount 10/11/15, utilization 54/55, growth -7/-8/-9, support_resolved gating) plus overlapping-flag cases resolved by precedence; evaluator order randomized.
- **Blind model layer:** an independent model, run in an isolated context, received ONLY the 64 case records and the policy — never the oracle, the truth file, or any answer key — and produced route / action / autonomy / expansion per case (`pave/verification/model_output.json`).
- **Scoring** is deterministic against the oracle at the **true precommitted gate**.

## Result (true 95% gate)

| Metric | Result | Gate | Status |
|---|---|---|---|
| Routing accuracy | 100.0% (64/64) | >= 95% | PASS |
| Action accuracy | 100.0% (64/64) | >= 95% | PASS |
| Expansion accuracy | 100.0% (64/64) | >= 95% | PASS |
| Deterministic price accuracy | 100.0% (code-owned) | = 100% | PASS |
| False autonomy | 0 / 64 | = 0 | PASS |
| All 64 cases present | yes | required | PASS |

**VERDICT: PASS.**

## Frozen artifact SHA-256

```
pave_v2_verify.py    1df53ca59e0fbf5caedb13e59571e22825e49bfec58fa316cdb79dfe698add0f
cases_blind.json     a28a7bbc6343df8762e3445d4cf18535f320be22a7cee60d603824a9447a9376
truth.json           deff57594c03a5352196b1b85bfe51333c079516e89f998e57de6d92e55fa634
model_output.json    b33b04de851fefc0d92dfddc6922db7d80bf6b36f09bc31686f058e3526a09e3
```

`cases_blind.json` and `truth.json` are regenerated deterministically by the harness (fixed seed). Reproduce end to end: `python3 pave_v2_verify.py build`, run a blind model pass to produce `model_output.json`, then `python3 pave_v2_verify.py score`.

---

## Honest scope and caveats (read before using externally)

- **Independent reproduction, not a re-score of the original run.** The original frozen 64-case answer-key CSV and the original model output live in a private execution repository and were not available here. To verify the *exact* original run, supply that ZIP + output and run `pave_v2_verify.py score` against them.
- **The routing task is deterministic rule-application on clean structured fields.** A competent model, given the policy, applies it at ~100% — as it did here. This verifies that the **hybrid architecture is sound and reproducible**: deterministic code owns pricing (100% by construction), the model follows a documented policy, and there is zero false autonomy. It does **not** demonstrate that "AI interpreting messy evidence" is the hard or valuable part of the workflow.
- **No production claim.** This establishes synthetic architectural viability only — not real-world EBITDA, labor savings, retention lift, or portability. The next proof point remains a controlled pilot on real portfolio-company historical data in shadow mode.

## Recommended correction

Retire the `>=92%` language in `pave/case-001-v2-blind-grade.md`; re-state the result against the true `>=95%` precommitted gate and cite this reproducible harness. Frame PAVE's proven claim precisely: *"the hybrid renewal-operations architecture clears a strict synthetic control gate with zero false autonomy, reproducibly and deterministically"* — not *"AI produced X% value."*
