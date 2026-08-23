# Technical Claims Diligence — Pilot Module

**Purpose:** a narrow, reproducibility-first technical diligence module for one material AI or statistical claim.

This is not a replacement for full product, security, legal, commercial, architecture, or management diligence. It is designed to answer one question clearly:

> **How much of a technically material claim survives independent reconstruction, controlled stress testing, and evidence review?**

## Best-fit claims

Examples include:

- "Our proprietary agent architecture outperforms standard scaffolds."
- "Our model achieves 94% accuracy."
- "Our fine-tuning is responsible for the performance lift."
- "Our inference stack reduces cost by 60%."
- "Our system is robust to distribution shift."
- "This benchmark score demonstrates production superiority."

The strongest pilot claim is one that materially influences valuation, technical moat, integration risk, or post-close value creation.

## Inputs requested

Minimum viable inputs:

1. the exact claim being relied upon;
2. the source benchmark/report/slide where it appears;
3. the frozen model or product configuration used to generate it;
4. enough code, logs, outputs, or environment detail to reproduce the claim;
5. any stated comparator or baseline;
6. the decision the claim is intended to support.

If source access is incomplete, the engagement can begin as a public-evidence audit, but confidence will be labeled accordingly.

## Five-stage workflow

### 1. Freeze the claim

Create a claim ledger recording:

- exact wording;
- date;
- source;
- metric definition;
- benchmark/data version;
- comparison baseline;
- model/configuration;
- decision relevance.

### 2. Reproduce

Attempt the advertised result without silently changing the protocol.

Evidence preserved:

- code commit;
- environment;
- commands;
- data/model versions;
- logs;
- outputs;
- checksums where practical.

### 3. Stress-test

Run 3–5 controlled tests targeted at the claim's most plausible fragilities, such as:

- seed/retry sensitivity;
- prompt or option-order sensitivity;
- holdout/distribution shift;
- baseline or scaffold attribution;
- token, latency, compute, or dollar budget;
- calibration;
- data leakage or contamination risk;
- model/version dependence.

Only variables implicated by the evidence are changed.

### 4. Localize discrepancies

A failed reproduction is not treated as one undifferentiated failure.

Possible layers include:

- missing provenance;
- environment mismatch;
- data-version mismatch;
- evaluation-harness mismatch;
- stochastic instability;
- comparator mismatch;
- model/scaffold attribution;
- genuine scientific or product-performance discrepancy.

### 5. Translate into decision language

The final memo answers:

- What reproduced?
- What did not?
- Which alternative explanations were tested?
- What remains unresolved?
- How much decision weight should the claim receive now?
- What follow-up would most reduce remaining uncertainty?

## Deliverables

A pilot produces:

1. **2-page decision memo** — conclusion first, written for an investment or operating team;
2. **claim ledger** — exact claims, evidence status, and decision relevance;
3. **reproduction record** — protocol, observed result, and deviations;
4. **stress-test matrix** — 3–5 controlled tests and outcomes;
5. **failure anatomy** — where any disagreement first appears;
6. **evidence appendix** — code/version/command/log/checksum references;
7. **next-test recommendation** — the single most valuable remaining check.

## Evidence states

Every material statement is labeled implicitly or explicitly as one of:

- **reported** — present in source material;
- **reconstructed** — derived from available artifacts but not directly rerun;
- **regenerated** — rerun under a documented protocol;
- **independently verified** — reproduced by an independent execution path or external system;
- **unresolved** — evidence is insufficient to distinguish remaining explanations.

## Pilot success criterion

The pilot succeeds only if it changes the quality of a real decision by reducing material uncertainty.

Examples of useful outcomes:

- increase confidence in a claim because it survives reproduction and controls;
- reduce valuation weight on a claim because the observed lift disappears under normalization;
- identify a provenance gap that prevents the claim from carrying investment weight;
- isolate an integration/operating condition under which the claimed benefit holds or fails;
- specify the cheapest decisive follow-up test.

A longer report is not itself success.

## Public examples

- [Case 001 — SWE-bench public-evidence diligence](swebench-public-evidence-review.md)
- [Case 002 — MMLU regeneration audit](mmlu-regeneration-case-002.md)

## Scope boundary

This module is intentionally narrow. It does not certify an entire company, codebase, security posture, or investment. It is designed to complement broader diligence teams by making one important technical claim more falsifiable, reproducible, and decision-useful.
