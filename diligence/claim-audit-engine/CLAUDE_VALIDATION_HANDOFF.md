# Claude Validation Handoff — Claim Audit Engine

**Target core:** `d62ac055578eee1e07467ab101d025e866fa5f9d`
**Case fixture:** `1d0937ab9b18c56b8d21fbe8f3aec04ec97c3ba0`
**Validation priority:** real FAIR EXP-001 discrepancy first, synthetic adversarial fixtures second, canonical FAIR package third.

## Objective

Validate that the Claim Audit Engine catches real evidence-integrity failures before we trust it on diligence work.

The first real case is FAIR EXP-001 because the current handoff reports two material inconsistencies:

1. **Provenance-pin mismatch** — package metadata claims organizer execution pin `f5def09c...`, while the artifact was reportedly produced from a fresh `master`/HEAD clone rather than that frozen commit.
2. **Artifact non-equivalence** — two baseline implementations are in circulation (reported as seed `12345` / ~117-line script vs seed `5566` / ~191-line streaming script) and they produce different sample scores.

If the engine accepts that package as a clean `regenerated` or `independently_verified` record, treat that as a false-negative defect.

## A. Real FAIR broken-package test

Create a case JSON that preserves the package exactly as found. Do not repair it before testing.

Expected detections:

- claimed execution revision differs from actual producing checkout;
- artifact lineage is ambiguous or contradictory;
- two baseline artifacts claiming the same role are not byte-equivalent and/or do not reproduce the same metric output;
- evidence-state promotion must be BLOCKED until one canonical lineage is established.

Expected failure localization:

1. `provenance` first for revision/lineage mismatch;
2. then `stochasticity`, `harness`, or `substantive_result` only if the evidence shows the discrepancy persists after provenance is fixed.

Preserve:

- both scripts;
- both seeds;
- actual `git rev-parse HEAD` values from producing directories;
- SHA256 for scripts, inputs, outputs, ZIP/result artifacts;
- exact commands;
- environments;
- sample score outputs;
- any current metadata that asserts a different pin.

## B. Adversarial gate suite

Attack the engine with at least these fixtures. Each fixture should have one expected PASS/BLOCK result and one expected failure layer.

| ID | Attack | Expected behavior |
|---|---|---|
| ADV-01 | Tamper artifact after recording SHA256 | BLOCK regenerated/verified promotion; checksum mismatch explicit |
| ADV-02 | `reported != regenerated` beyond declared tolerance | Preserve both values; mark outside tolerance; do not overwrite either |
| ADV-03 | Missing command/environment/observed_result | BLOCK `regenerated` promotion |
| ADV-04 | Claim `independently_verified` without external receipt or independent execution | BLOCK |
| ADV-05 | Same nominal configuration produces differing outputs across repeated runs | Flag stochasticity/non-determinism; do not call deterministic reproduction |
| ADV-06 | Wrong `ood_scores` length for FAIR artifact | BLOCK artifact/schema validity before scientific interpretation |
| ADV-07 | Metadata pin differs from producing checkout pin | BLOCK; provenance mismatch must be first-class |
| ADV-08 | Two artifacts claim to be the canonical baseline but differ in hash/config/metric | BLOCK canonical promotion; require lineage resolution |

Report any fixture the engine incorrectly accepts as **false negative**. Report any valid fixture it incorrectly blocks as **false positive**.

## C. Canonical truthful FAIR package

After the broken package and adversarial suite are frozen, build exactly one canonical FAIR baseline package.

Requirements:

- one baseline implementation only;
- one predeclared seed only;
- actual producing Git commit recorded from the checkout used to execute;
- no metadata field may name a commit that was not the producing checkout;
- current organizer/data version explicitly recorded;
- streaming-safe implementation if required by the dataset/runtime;
- exact command and environment captured;
- script/input/output/submission SHA256 values recorded;
- local metric/schema validator output preserved;
- repeated replay from a fresh directory produces the same artifact or an explicitly explained deterministic-equivalent result;
- Codabench receipt remains blank/pending until #10902 approval and actual scoring.

Expected engine result before Codabench:

- `regenerated`: PASS if all local prerequisites are genuinely present;
- `independently_verified`: BLOCK because external receipt/independent execution is not yet present.

Expected engine result after Codabench score is returned and recorded:

- external receipt can satisfy the relevant verification requirement only if all lineage/provenance checks also remain clean.

## Return package to ChatGPT

Return these artifacts, not a prose-only summary:

1. `fair-broken-case.json`
2. `fair-broken-audit_bundle.json`
3. `fair-broken-decision_memo.md`
4. `adversarial-results.json` with PASS/BLOCK expectation vs observed result for ADV-01..08
5. any engine traceback or silent acceptance bug
6. canonical FAIR case JSON
7. canonical audit bundle + memo
8. manifest of all test artifacts with SHA256
9. exact engine commit tested
10. concise bug list ranked `critical / high / medium / low`

## Scientific boundary

Do not optimize the FAIR model while doing this work. This validation is about evidence integrity and reproducibility, not leaderboard performance.

Do not mark EXP-001 complete until the actual Codabench external score exists and is recorded against the canonical artifact lineage.
