# Case 003 v0.1.1 Grade — Project Meridian

**Protocol:** AI-Q v0.1.1  
**Frozen hidden-truth precommitment:** `356acbaddc7b8fcbcd9d2b50e85da8849d68f2dd09f9a3763be94c0a8dc70108`  
**Frozen evaluator-package SHA-256:** `0318eef9eb7fbb3b87337892332f502176cd7c54ccb2abbd99d4b9c27afaf89f`  
**Frozen v0.1.1 blind-report SHA-256:** `a76616dc0b493ba79a86cc6a44c552bf67123d1ed2d4e3b966138bb2dbc4b51d`  
**Decision:** **REPAIR AGAIN — narrow deterministic-runner defect; do not advance to Case 004 yet**

## Executive verdict

AI-Q v0.1.1 materially improved the Case 003 rerun. The repaired process operated on the actual frozen Project Meridian data room, verified the package hash and internal manifest, executed the supplied harness, preserved real artifact names, and substantially eliminated the unsupported moat-duration / parity / pricing / guarantee overreach seen in v0.1.

The blind report also correctly recovered the central transaction interpretation:

- the mature 83.9% autonomous-resolution result is real as scoped;
- the 18.4-point headline comparison is mathematically real but inflated by comparator choice;
- the more relevant normalized full-stack lift is ~8.6 points;
- architecture-only lift is ~5.1 points;
- mature customer-memory contribution is ~3.5 points and falls to ~0.3 points on recent onboarding;
- the ~$0.09 inference-cost statistic is real only under its narrow definition;
- recent-onboarding performance degrades materially;
- the ~34% labor reduction is observable but not causally identified.

However, v0.1.1 contains one severe deterministic-runner bug that directly corrupted the explicit thesis-strengthening finding: the runner searched for `incorrect_auto_resolution`, but the frozen case outcome label is `wrong_auto_resolution`. It therefore reported zero wrong-autonomous outcomes when the frozen truth contains nonzero wrong-auto errors.

Because AI-Q v0.1.1 defines deterministic code as the measurement boundary, a field-label bug at that boundary is a hard measurement failure. The correct response is a narrow runner repair and rerun on the same frozen case, not Case 004 yet.

## What v0.1.1 fixed

### Provenance — PASS

The clean run reconstructed the exact 125,597-byte package and matched the frozen evaluator SHA-256. The 16-file internal manifest passed. The supplied `08_EVALUATION_HARNESS.py` was executed against the actual package. The report cites real evaluator filenames rather than invented stand-ins.

### Inference firewall — PASS / major improvement

The v0.1 report invented specific competitor parity timelines, moat duration, pricing/guarantee numbers, R&D requirements, and precise test designs. The v0.1.1 report largely avoids those unsupported claims and explicitly marks unresolved competitive defensibility and buyer assumptions.

### Narrow-claim scope — PASS

C4 is correctly handled as a narrow claim that reproduces under its stated definition rather than being called false simply because broader production economics are worse.

### Symmetric diligence — INTENDED MECHANISM WORKED, MEASUREMENT INPUT FAILED

The report explicitly included a Thesis-Strengthening Evidence section and attempted to inspect wrong-autonomous behavior. This is the correct protocol behavior. The resulting safety conclusion is wrong because the deterministic runner used the wrong outcome label.

## Claim-level grade

| Claim | Ground-truth expectation | v0.1.1 result | Grade |
|---|---|---|---|
| C1 — autonomous resolution | ~83.9% mature real; ~70.1% recent onboarding; durability partial | Recovered both headline and transfer degradation correctly | **PASS** |
| C2 — proprietary architecture lift | 18.375 pp vs weak baseline; 8.625 pp full stack vs comparable; 5.125 pp architecture-only; 3.5 pp data contribution | Recovered the key attribution structure and normalized comparator | **PASS** |
| C3 — labor reduction | ~34% before/after real; causal attribution unresolved | Correctly treats observation as real and causality as insufficient | **PASS** |
| C4 — ~$0.09 cost | Narrow metric supported; broader production economics materially higher | Correctly preserves narrow claim and normalizes wider costs | **PASS / wording cleanup needed on denominator labels** |
| C5 — proprietary data | Real mature lift; nearly absent on new customers; long-run moat unresolved | Correctly identifies mature lift, fresh collapse, and insufficient evidence for long-run defensibility | **PASS** |
| C6 — generalization | Broad stability not supported; heterogeneous degradation with healthcare weakest | Correctly rejects broad transfer claim without declaring universal failure | **PASS** |

## Critical runner defect

The deterministic runner contains:

```python
wrong=sum(r['outcome']=='incorrect_auto_resolution' for r in s)
```

The frozen Case 003 outcome vocabulary uses `wrong_auto_resolution`.

Consequences:

- v0.1.1 reports 0 wrong-auto outcomes in the mature cohort;
- v0.1.1 reports 0 wrong-auto outcomes in recent onboarding;
- it converts this into a major thesis-strengthening claim that the escalation gate produced zero silent autonomous errors;
- that claim is false for the frozen case.

Frozen hidden truth:

- mature target: wrong-auto errors are nonzero, approximately 0.74% of autonomous outcomes;
- recent-onboarding target: wrong-auto errors are nonzero, approximately 2.17% of autonomous outcomes.

The correct positive conclusion is weaker but still useful: Meridian appears to keep wrong-autonomous outcomes low relative to its automation volume, while the rate worsens on fresh customers. The blind evaluator should identify selective safety gating as a strength **without claiming zero error**.

## Secondary wording issue — cost denominator

The report sometimes labels `$0.427` / `$0.814` as "per case" or "full production cost per case" while the frozen construction defines these decision-relevant totals as cost **per successful automated resolution** after allocating model/infra and variable review/fallback cost. This is less severe than the wrong-auto bug because the underlying numbers are largely correct, but denominator language must be made exact.

The deterministic runner and report schema should use explicit metric names such as:

- `narrow_ai_cost_per_successful_auto_resolution`;
- `all_model_infra_cost_per_successful_auto_resolution`;
- `human_review_fallback_cost_per_successful_auto_resolution`;
- `full_variable_cost_per_successful_auto_resolution`.

Avoid generic "per case" labels unless the denominator is literally all eligible cases.

## v0.1.1 validation dimensions

| Dimension | Grade |
|---|---|
| Claim identification | **PASS** |
| Raw package provenance | **PASS** |
| Exact artifact identity | **PASS** |
| Headline reproduction | **PASS** |
| REAL vs PROPRIETARY separation | **PASS** |
| Durability diagnosis | **PASS** |
| Economic normalization | **PASS with denominator-label repair** |
| Uncertainty preservation | **PASS** |
| Unsupported-inference firewall | **PASS** |
| Thesis-strengthening scan | **FAIL on measured result because of field-label bug** |
| Deterministic measurement reliability | **FAIL — wrong categorical value hard-coded** |
| Transaction usefulness | **PASS conditional on runner correction** |

## Decision

### **REPAIR AGAIN — narrow implementation repair**

Do not redesign AI-Q. Do not change the hidden truth. Do not change the evaluator data room. Do not advance to Case 004 yet.

The v0.1.1 protocol appears substantially stronger than v0.1; the remaining blocker is a deterministic implementation defect, not a thesis or methodology collapse.

Required repair:

1. eliminate hard-coded outcome strings where a data dictionary / observed vocabulary can be validated first;
2. assert that all expected categorical labels exist before calculating rates;
3. fail closed if a queried label is absent instead of silently returning zero;
4. add invariant checks such as `successful + wrong_auto + escalated == cohort_n`;
5. repair all cost denominator names;
6. rerun the same frozen Case 003 package under an implementation-only patch;
7. freeze and grade the resulting report before Case 004.

## Advancement gate

AI-Q earns Case 004 only if the implementation-only rerun:

- preserves all six substantive claim conclusions;
- reports the correct nonzero wrong-auto rates;
- still recognizes selective safety gating as thesis-strengthening evidence in bounded language;
- uses exact cost denominators;
- retains the v0.1.1 provenance and inference discipline.
