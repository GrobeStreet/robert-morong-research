# PAVE Case 001 v2 — Evaluator Package Provenance

## Frozen package

**Filename:** `PAVE_Case_001_Project_Relay_v2.0.zip`  
**SHA-256:** `46643118e6e7b01fb17af320a8d47c6db6200a44e01f3709586158925191978d`

The package is synthetic and contains no real portfolio-company or customer data.

## Evaluator-facing inventory

- `00_DATA_ROOM_README.md`
- `01_RENEWAL_CASES.csv`
- `02_RENEWAL_POLICY.md`
- `03_BUILD_DETERMINISTIC_FACTS.py`
- `04_AGENT_OUTPUT_SCHEMA.csv`
- `05_SCORE_AGENT.py`
- `06_PRECOMMITTED_SUCCESS_GATE.md`
- `07_MANIFEST.sha256`

The internal manifest freezes every evaluator-facing artifact. The hidden answer key is not present in this ZIP.

## Hidden truth identity

**Hidden answer-key SHA-256:** `44853df407322945bb25191673fe43aabfdfd147934732efedb1b37b1d2baf13`

The hidden builder truth is stored separately in a private Google Drive document. Its contents must not be supplied to the fresh external blind evaluator.

## Benchmark construction

- 64 synthetic renewal cases
- randomized evaluator row order
- two policy configurations
- clean, expansion, retention, commercial, data-quality, legal, mixed-trigger, and edge-threshold cases
- stale CRM price records included on selected cases
- missing usage evidence included on selected cases
- overlapping exceptions evaluated under fixed precedence

## Deterministic / model boundary

The supplied deterministic facts builder computes policy-sensitive renewal pricing directly from the billing `current_monthly_price` and selected policy configuration. It also exposes explicit hard-gate flags that can be computed mechanically from the evaluator evidence.

The external model is evaluated on the remaining interpretation problem: route/action selection, autonomy decision, expansion recognition, and evidence-grounded explanation.

The final output is assembled by workflow code so that deterministic commercial calculations are not silently delegated back to the language model.
