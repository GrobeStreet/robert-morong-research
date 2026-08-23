# Case 002 — When the Headline Survives but the Supporting Metrics Do Not

**Case type:** Reproducibility-first technical claims diligence  
**Underlying project:** `GrobeStreet/mmlu-robustness-audit`  
**Status:** Qwen arm regenerated with partial metric agreement; Llama arm and second-human verification remain outstanding.  
**Case date:** 2026-08-23

## Decision question

**What should a technical decision-maker conclude when a benchmark's central qualitative result regenerates, but several supporting quantitative claims do not?**

This case uses our own MMLU option-order audit because it creates a stronger test of diligence discipline than a success-only showcase. The historical record contained a compelling robustness/calibration story. A later execution of the surviving public harness reproduced the central robustness phenomenon but did **not** reproduce several supporting metrics.

The correct response was not to hide the mismatch, tune until the old table reappeared, or relabel the new run as full reproduction. The record was split into historical and regenerated evidence, alternative explanations were tested, and unsupported language was downgraded.

That behavior is the point of the case.

---

## 1. Claim ledger

### Historical claim family

The frozen historical record for `Qwen/Qwen2.5-0.5B-Instruct` reported, on 300 fixed-seed MMLU questions with four cyclic option rotations:

| Metric | Frozen historical value |
|---|---:|
| Headline accuracy | 42.7% |
| Accuracy across all rotations | 41.2% |
| Stable across all four rotations | 35.7% |
| Answer flips under reordering | 64.3% |
| Accuracy on stable questions | 56.1% |
| Accuracy on flipping questions | 35.2% |
| Expected calibration error | 0.28 |
| Mean four-label confidence | 69.1% |

A historical two-model follow-up reported Qwen versus Llama-3.2-3B as:

| Metric | Qwen | Llama |
|---|---:|---:|
| Headline accuracy | 42.7% | 56.7% |
| Answer flips | 64.3% | 52.5% |
| Accuracy on flipping questions | 35.2% | 34.9% |
| ECE | 0.28 | 0.09 |

The strongest narrative implication was that the larger model was more accurate and substantially better calibrated while still exhibiting option-order instability.

### Provenance limitation

The original local scripts/raw parquet artifact underlying the frozen historical values were unavailable when the public repository was reconstructed. Therefore the frozen values are preserved as **historical reported results**, not silently treated as outputs of the later public-harness execution.

---

## 2. Reproduction protocol

The surviving public harness was executed on 2026-08-12 using:

- `audit_full.py` without changing its scientific protocol;
- `--n 300 --seed 0`;
- four cyclic rotations per question;
- 1,200 predictions;
- `Qwen/Qwen2.5-0.5B-Instruct`;
- CPU;
- an initial bf16 execution followed by a float32 control.

This was a separate regeneration of the repository's own harness. It was **not** represented as byte-for-byte identity with the unavailable historical run and was **not** represented as second-human independent verification.

---

## 3. What happened

| Metric | Frozen | bf16 regeneration | fp32 control |
|---|---:|---:|---:|
| Headline accuracy | 42.7% | 43.7% | 44.0% |
| Accuracy across rotations | 41.2% | 43.6% | 43.1% |
| Stable across all rotations | 35.7% | 21.3% | 21.7% |
| Answer flips | 64.3% | 78.7% | 78.3% |
| Accuracy on stable questions | 56.1% | 76.6% | 75.4% |
| Accuracy on flipping questions | 35.2% | 34.6% | 34.1% |
| ECE | 0.28 | 0.132 | 0.137 |
| Mean four-label confidence | 69.1% | 56.8% | 56.8% |

### Regenerated

The following survived strongly enough to retain:

- headline accuracy was within 1.3 percentage points of the historical value;
- accuracy on flipping questions was within 1.1 points;
- the model still changed its underlying answer on a **majority** of questions under meaning-preserving answer-option reordering;
- when answers flipped, accuracy remained near the 25% four-choice chance floor;
- the regenerated flip rate was actually higher than the historical 64.3% under both tested precisions.

The central robustness finding therefore survived.

### Not regenerated

The following did not agree with the historical record:

- stable-across-rotations rate;
- accuracy on stable questions;
- expected calibration error;
- mean normalized four-label confidence.

The historical Qwen calibration value of 0.28 therefore could not be treated as a currently regenerated baseline.

Because the Llama arm had not yet been rerun, the historical `0.28 vs 0.09` two-model calibration contrast was downgraded to **historical/unconfirmed**.

---

## 4. Alternative explanation test #1 — argmax tie-breaking

The bf16 run produced exact top-score ties:

- 100 / 1,200 predictions = 8.3%;
- 81 / 300 questions were touched by at least one exact tie.

A plausible explanation was that positional `argmax` behavior artificially inflated the flip rate.

That hypothesis was tested rather than assumed.

| Tie policy | Flip rate |
|---|---:|
| Positional `argmax` | 78.7% |
| Uniform random tie-break over 200 reseeds | 78.5% [77.7, 79.3] |
| Exclude all tie-affected questions | 71.7% |

**Verdict:** tie-breaking did not explain the majority-flip result. Even the conservative tie-excluded subset remained above the historical 64.3% flip rate.

---

## 5. Alternative explanation test #2 — numerical precision

Because `torch_dtype="auto"` resolved to bfloat16 for the initial run, quantization/precision was another plausible explanation for both exact ties and the discrepancy from the historical table.

The same protocol was rerun in float32.

Results:

- exact ties fell from 100 to 0;
- flip rate moved only 78.7% → 78.3%;
- ECE moved only 0.132 → 0.137;
- mean confidence remained 56.8%;
- the major stability/calibration discrepancy remained.

**Verdict:** numerical precision was refuted as the explanation for the historical-versus-regenerated gap.

---

## 6. Additional finding exposed by the audit

The regeneration also exposed a strong display-position asymmetry.

| | A | B | C | D |
|---|---:|---:|---:|---:|
| Predicted display position, bf16 | 290 | 378 | 377 | 155 |
| Predicted display position, fp32 | 272 | 379 | 383 | 166 |
| Underlying answer chosen, bf16 | 311 | 294 | 306 | 289 |
| Underlying answer chosen, fp32 | 308 | 290 | 309 | 293 |

Displayed labels were highly asymmetric while underlying answer identities remained close to uniform. That localizes the observed bias toward **display position**, rather than a simple preference for particular underlying answer contents.

This was not required to preserve the original claim. It emerged because the discrepancy investigation was allowed to discover something new instead of being constrained to validate the historical narrative.

---

## 7. Root cause: unresolved

Two tested explanations were eliminated:

- argmax tie-breaking;
- bf16 numerical precision.

The surviving record does not establish why the historical stability/calibration values differ from the regeneration. Plausible provenance differences include prompt formatting, checkpoint revision, or sample provenance, but none is asserted as the cause because the missing historical raw run prevents that inference from being verified.

This is a critical diligence rule:

> **Eliminating two explanations does not license inventing a third.**

The correct state is **unresolved provenance discrepancy**.

---

## 8. Decision interpretation

If this were a third-party target company's technical claim, the diligence conclusion would be:

> The core robustness claim receives meaningful evidentiary weight because the surviving harness independently regenerated the majority-flip phenomenon at two numerical precisions and the result survived explicit tie-breaking controls. However, several supporting quantitative metrics—including stability and calibration—did not regenerate. The historical calibration comparison should therefore not be used as current evidence of cross-model superiority until the second model is rerun and the provenance gap is resolved. We would retain the central finding while discounting the unsupported quantitative extensions.

That conclusion is intentionally neither "validated" nor "debunked."

It decomposes the claim.

---

## 9. What changed because of diligence

### Before regeneration

A reader could reasonably leave with the compact story:

> option ordering causes substantial answer instability, and the larger model is more accurate and much better calibrated but still flips.

### After regeneration

The evidence supports the narrower statement:

> option ordering produces substantial answer instability in the regenerated Qwen harness; the model flips on a majority of questions and performs near chance on questions where it flips. The historical stability/calibration values and the Qwen-vs-Llama calibration contrast are not currently regenerated.

This is a reduction in rhetorical strength but an increase in evidentiary quality.

---

## 10. Evidence ledger

Primary repository: https://github.com/GrobeStreet/mmlu-robustness-audit

Key artifacts:

- `RESULTS.md` — explicit separation of frozen historical and regenerated results;
- `regeneration/REGENERATION.md` — protocol, comparisons, controls, interpretation, and limitations;
- `regeneration/PROVENANCE.json` — machine-readable provenance record;
- `audit_full.py` — public audit harness;
- `analyze.py` — analysis implementation;
- `tests/` — analysis/evaluation tests;
- `inspect_eval/` — Inspect AI parity implementation and parity record.

Recorded regeneration environment:

- Python 3.11.15;
- torch 2.13.0;
- transformers 4.57.6;
- datasets 3.6.0;
- CPU.

The 2026-08-12 executions used then-default Hugging Face revisions and did not record immutable commit hashes at execution time. Future runs are pinned in the underlying repository to model revision `7ae557604adf67be50417f59c2c2f167def9a775` and dataset revision `c30699e8356da336a370243923dbaf21066bb9fe` with automatic SHA-256 provenance sidecars.

---

## 11. Open items

This case must not imply completion of work that remains outstanding.

- Llama-3.2-3B-Instruct has **not** been rerun.
- The historical Qwen-vs-Llama calibration contrast remains **unconfirmed**.
- No byte-level identity with the unavailable historical raw run is claimed.
- No second independent human verifier has executed the full package.

A future Llama regeneration should extend this case rather than overwrite its present state.

---

## 12. Why this case matters for technical diligence

Most diligence demonstrations select a clean success story. This one is more informative.

A reproducibility-first reviewer must be willing to discover that:

- part of a claim is robust;
- part is not;
- obvious explanations fail;
- the remaining discrepancy cannot be resolved from available evidence;
- public language therefore needs to become narrower.

That is exactly the behavior an investor, acquirer, research organization, or technical executive should want from an independent evaluator whose job is to determine **how much of an important technical claim survives contact with the evidence**.
