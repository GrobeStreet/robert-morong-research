# Diligence Lab

A public demonstration of **reproducibility-first technical diligence for AI and statistical claims**.

The lab is not presented as a substitute for full M&A, security, commercial, legal, or management diligence. Its scope is narrower:

> **Take a material technical claim, freeze it, reconstruct the evidence chain, reproduce what can be reproduced, stress-test the result, localize any discrepancy, and translate the surviving evidence into decision language.**

## Operating standard

Each case follows the same sequence:

1. **Claim** — state the exact material claim being evaluated.
2. **Source evidence** — preserve the strongest available primary artifacts.
3. **Reproduction** — rerun or reconstruct the claim without silently changing the protocol.
4. **Controls** — test obvious alternative explanations and implementation artifacts.
5. **Perturbations** — vary decision-relevant assumptions one at a time.
6. **Result** — separate what reproduced from what did not.
7. **Decision interpretation** — explain how much weight the claim should receive after diligence.
8. **Evidence ledger** — preserve provenance, limitations, unresolved discrepancies, and falsifiers.

## Epistemic rules

- A historical reported value is not the same thing as a regenerated value.
- A regenerated value is not the same thing as an independently verified value.
- A successful rerun does not prove production transfer.
- A failed rerun does not automatically prove the original claim was false.
- Missing provenance remains missing; it is not reconstructed by inference.
- The objective is to reduce decision-relevant uncertainty, not to validate a preferred story.

## Cases

### Case 001 — SWE-bench public-evidence diligence

**Question:** How much decision weight should an investor put on a headline SWE-bench Verified score for an AI coding-agent company?

Artifact: [`swebench-public-evidence-review.md`](swebench-public-evidence-review.md)

Status: **public-evidence worked example; no independent leaderboard rerun claimed.**

The case shows how to separate base-model performance from agent/scaffold contribution, protocol/version effects, cost sensitivity, and fresh-distribution transfer risk.

### Case 002 — MMLU option-order regeneration audit

**Question:** What should a decision-maker conclude when the central qualitative result regenerates but several supporting quantitative claims do not?

Artifact: [`mmlu-regeneration-case-002.md`](mmlu-regeneration-case-002.md)

Status: **real internal/public research audit using preserved historical values and a separate public-harness regeneration.**

This case is intentionally self-critical: the audit did not manufacture agreement with the historical table. It preserved the majority-flip finding while downgrading unsupported stability/calibration claims.

## Pilot engagement shape

A first live diligence pilot should remain deliberately narrow.

**Input:** one material technical performance claim from an AI-enabled target, plus enough code/configuration access to test it.

**Output:**

- frozen claim ledger;
- reproduction result;
- 3–5 controlled sensitivity or adversarial tests;
- cost/latency normalization where relevant;
- failure-mode analysis;
- evidence appendix with commands, versions, hashes, and logs;
- concise decision memo explaining what changed after technical diligence.

**Success criterion:** the work must reduce a real decision uncertainty. Producing a longer technical report is not itself success.
