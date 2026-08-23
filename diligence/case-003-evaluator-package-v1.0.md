# Case 003 Evaluator Package v1.0

**Case:** Project Meridian  
**Purpose:** blind validation of AI-Q v0.1  
**Build date:** 2026-08-23  
**Status:** evaluator-facing package generated and integrity-checked

The evaluator-facing package has been generated separately from the answer-bearing builder specification.

## Package

Archive name:

`AI-Q_Case_003_Project_Meridian_Evaluator_Data_Room_v1.0.zip`

Archive SHA-256:

`0318eef9eb7fbb3b87337892332f502176cd7c54ccb2abbd99d4b9c27afaf89f`

The archive contains 18 evaluator-facing files:

- `00_DATA_ROOM_README.md`
- `01_CIM_AI_EXCERPT.md`
- `02_MANAGEMENT_CLAIM_LEDGER.csv`
- `03_PRODUCT_ARCHITECTURE.md`
- `04_INTERNAL_BENCHMARK_REPORT.md`
- `05_EVAL_CASES.csv`
- `06_SYSTEM_RUN_OUTPUTS.csv`
- `07_BASELINE_RUN_OUTPUTS.csv`
- `08_EVALUATION_HARNESS.py`
- `09_REQUIREMENTS_OR_ENVIRONMENT.md`
- `10_COST_MODEL.csv`
- `11_CUSTOMER_ROI_SUMMARY.csv`
- `12_CUSTOMER_COHORT_NOTES.md`
- `13_TECHNICAL_QA.md`
- `14_KNOWN_LIMITATIONS.md`
- `15_DATA_DICTIONARY.md`
- `16_INTEGRITY_REPORT.md`
- `17_MANIFEST.sha256`

## Integrity checks completed

- 3,300 unique evaluation cases generated;
- 2,400 core mature-benchmark cases and 900 recent-onboarding validation cases;
- target, comparator, and ablation case IDs reconcile exactly;
- no duplicate case IDs;
- outcome vocabularies validated;
- no negative cost or review values;
- retry counts stay inside the documented range;
- the supplied headline reproduction harness runs successfully and reproduces the represented management headline metrics;
- evaluator-facing performance, comparator, cohort, unit-cost, and ROI relationships match the frozen builder specification;
- evaluator-facing files were scanned for answer-key/classification language, builder-only mechanism labels, and generator-seed strings; no scanned answer-key tokens were detected.

## Blind-run boundary

The evaluator should receive only:

1. `diligence/ai-q-v0.1-spec.md`; and
2. the evaluator archive listed above.

The evaluator must not receive or search for the separate answer-bearing Case 003 builder bundle before its report is frozen.

The next checkpoint is the blind AI-Q v0.1 evaluation of Project Meridian. Only after that report is complete should it be compared with the precommitted builder specification.
