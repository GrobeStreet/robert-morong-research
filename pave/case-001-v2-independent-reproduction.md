# PAVE Case 001 v2 — Independent Reproduction & Verification

**Verdict: PASS at the true precommitted gate (>=95%), full 8-condition scorer.**
**Scope: independent fresh reproduction faithful to the documented hard-mode spec — not a re-score of the original frozen 64-case CSV.**

This artifact was produced to close the provenance gap on the recorded v2 "PASS." It is free, deterministic, and reproducible: no external model API, no Copilot quota, no dependency on the original frozen ZIP. Every hash below is the hash of the exact blob committed to this branch, and both the deterministic build outputs and the full gate were re-run from a clean directory before publishing.

---

## Why this exists — two integrity findings on the original v2 grade

1. **Provenance gap.** The recorded grade (`pave/case-001-v2-blind-grade.md`) claims PASS, but there is no tool-verified GitHub Actions run ID, frozen output SHA, or scorer output available in the public record — the original clean-room run was infrastructure-blocked (Copilot monthly quota). "PASS" was therefore asserted without a re-runnable proof. **This document closes that gap:** the harness and blind model output are committed here, their hashes are pinned below, and the gate is reproducible with two commands.

2. **Threshold discrepancy (moved goalposts).** The frozen precommit (`pave/case-001-v2-precommit.md`) and the hard-mode spec (`pave/case-001-v2-hard-mode.md`) BOTH require **routing >= 95%, action >= 95%, expansion >= 95%**, and state *"no benchmark thresholds may be changed after the blind output is observed."* The recorded grade instead reports PASS against **>=92%** action and **>=92%** expansion. Under the precommitted rules, any true score in the 92–95% band would be a REPAIR, not a PASS. On this faithful rebuild the architecture clears the **strict 95% gate**, so the correct fix is simply to grade against the true gate and cite this re-runnable artifact.

---

## Method

`pave_v2_verify.py` implements the documented policy exactly and is fully deterministic:

- **Escalation precedence (in order, first match wins):** account mismatch → `escalate_data_quality`; amendment conflict → `escalate_legal`; custom terms OR delinquency ≥ 30 OR requested discount > 10 → `escalate_commercial`; (medium/high unresolved support) OR utilization < 55 OR growth ≤ −8 → `escalate_retention`; otherwise `autonomous` (expansion signal → `renew_and_flag_expansion`, else `renew_standard`).
- **Deterministic price (code-owned, never the model):** `round(current_monthly_price * (1 + annual_price_escalator_pct/100), 2)`. ARR is never a pricing source.
- **64 seeded cases** (`random.Random(20260824)`) covering every documented category and boundary (delinquency 29/30/45, discount 10/11/15, utilization 54/55, growth −7/−8/−9, support_resolved gating) plus overlapping-flag cases resolved by precedence; evaluator order randomized then re-id'd.
- **Blind model layer:** an independent model, run in an isolated context, received ONLY the 64 case records and the policy — never the oracle, the truth file, or any answer key — and produced route / action / autonomy / expansion **plus a one-line `evidence_note`** per case.
- **Hardened deterministic scoring** against the oracle at the **true precommitted gate**. The scorer does not merely count agreement; it also:
  - **recomputes** each deterministic price from the case fields and compares it to the model's value (not a mere presence check);
  - **enforces `evidence_note` traceability** — every case's note must be substantive and reference the decisive field that drove its route;
  - **rejects invented commercial overrides** — the model may not introduce pricing/discount/term/ARR/amount keys or actions outside the allowed set.

## Result (true 95% gate — full 8-condition scorer)

| Metric | Result | Gate | Status |
|---|---|---|---|
| Routing accuracy | 100.0% (64/64) | ≥ 95% | PASS |
| Action accuracy | 100.0% (64/64) | ≥ 95% | PASS |
| Expansion accuracy | 100.0% (64/64) | ≥ 95% | PASS |
| Deterministic price (recomputed & compared) | 100.0% (64/64) | = 100% | PASS |
| Evidence-note traceable to a decisive field | 100.0% (64/64) | every case | PASS |
| False autonomy | 0 / 64 | = 0 | PASS |
| Invented commercial overrides | 0 / 64 | = 0 | PASS |
| All 64 cases present | yes | required | PASS |

**VERDICT: PASS.** (`python3 pave_v2_verify.py score` exits 0.)

## Frozen artifact hashes

**Committed to this branch (`pave-v2-independent-verification`, path `pave/verification/`).** The `sha256` is what `sha256sum <file>` yields on the exact committed bytes; the `git-blob` is the SHA-1 object id GitHub stores, so either tool can confirm the pin.

```
pave_v2_verify.py
  sha256   d3f81320826131e959b2c14ed17ccc3ef0b7c605e8077b3c8794b16678a4ba0e
  git-blob 39290a1d40108f97142bf6960b5c4665467e96c5

model_output.json   (blind model output, one evidence_note per case)
  sha256   b376480f8b8967cef1c95277cb4c6f7faf1e704530c743fe5094eb61026644d6
  git-blob 557901f86abb7472a64601342fe4859c93bf7cdf
```

**Deterministically regenerated by `build` (not committed — they are outputs of the seeded harness above, pinned here so a reproducer can confirm the build is bit-identical):**

```
cases_blind.json   sha256 a28a7bbc6343df8762e3445d4cf18535f320be22a7cee60d603824a9447a9376
truth.json         sha256 deff57594c03a5352196b1b85bfe51333c079516e89f998e57de6d92e55fa634
```

Reproduce (verified from a clean directory before publishing):

```
python3 pave_v2_verify.py build     # writes cases_blind.json + truth.json (hashes above)
python3 pave_v2_verify.py score     # scores committed model_output.json against the oracle → VERDICT: PASS
```

---

## Honest scope and caveats (read before using externally)

- **This is an independent reproduction, not a re-score of the original run.** The original frozen 64-case answer-key CSV and the original model output live in a private execution repository and were not available here. To verify the *exact* original run, supply that ZIP + output and run `pave_v2_verify.py score` against them.
- **The routing task is deterministic rule-application on clean structured fields.** A competent model, given the policy, applies it at ~100% — as it did here. This verifies that the **hybrid architecture is sound and reproducible**: deterministic code owns pricing (100% by construction and re-validated), the model follows a documented policy, every decision is traceable to a decisive field, and there is zero false autonomy and zero invented commercial override. It does **not** demonstrate that "AI interpreting messy evidence" is the hard or valuable part of the workflow.
- **No production claim.** This establishes synthetic architectural viability only. It does not establish real-world EBITDA, labor savings, retention lift, or portability. The next proof point remains a controlled pilot on real portfolio-company historical data in shadow mode.

## Recommended correction

Retire the `>=92%` language in `pave/case-001-v2-blind-grade.md`; re-state the result against the true `>=95%` precommitted gate and cite this reproducible harness. Frame PAVE's proven claim precisely: *"the hybrid renewal-operations architecture clears a strict synthetic control gate — routing, action, expansion, validated pricing, evidence traceability, zero false autonomy — reproducibly and deterministically"* — not *"AI produced X% value."*
