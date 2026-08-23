# Case 003 Architecture — Project Meridian

**Case status:** architecture frozen for build-out  
**Case type:** synthetic AI-native SaaS acquisition diligence  
**Target:** *Project Meridian* — a deliberately fictional customer-support automation company  
**Purpose:** first blind validation of `AI-Q v0.1`  
**Evaluator protocol:** [`ai-q-v0.1-spec.md`](ai-q-v0.1-spec.md)

> This file defines the architecture of Case 003. It does **not** contain the hidden answer key. Hidden truth must remain outside the evaluator-facing repository/materials until the blind run is complete.

## 1. Transaction frame

Project Meridian is a fictional growth-stage B2B SaaS company selling AI customer-support automation to mid-market and enterprise customers.

The company is being evaluated in a hypothetical sponsor-led acquisition where a meaningful portion of the valuation premium depends on claims that its AI system:

- resolves a large share of support cases autonomously;
- produces measurable lift beyond a commodity frontier model;
- lowers customer labor requirements;
- operates at attractive per-resolution economics;
- benefits from proprietary customer interaction data;
- generalizes across customers and verticals.

The case should feel like a realistic mini data room, not a benchmark puzzle. Management need not be deceptive. Some claims should be true, some should be directionally true but overstated by methodology, some should weaken under normalization, and at least one should remain genuinely unresolved from the available evidence.

## 2. Why this target was chosen

Customer-support automation creates a useful first validation domain because the four AI-Q dimensions can all be tested in one transaction:

- **REAL:** resolution and quality metrics can be recomputed;
- **PROPRIETARY:** target-specific orchestration can be compared with a normalized base-model/scaffold baseline;
- **DURABLE:** fresh customers, task mixes, seeds, prompts, and operating limits can test transfer;
- **ECONOMIC:** retries, model calls, latency, human review, and fallback behavior can be included in cost per successful resolution.

It is also commercially legible to an investment committee: technical conclusions can map to moat, gross margin, implementation risk, and valuation weight without inventing a financial model.

## 3. Material management claims

The evaluator-facing data room will contain six primary claims. Exact reported values may be finalized during build-out, but the claim families are frozen here.

### C1 — Autonomous resolution

> Meridian autonomously resolves roughly four-fifths of eligible customer-support cases while meeting the represented quality threshold.

**Deal relevance:** product value, labor substitution, customer ROI, revenue durability.

### C2 — Proprietary architecture lift

> Meridian's proprietary orchestration layer materially outperforms the same underlying frontier model operating through a standard/generic scaffold.

**Deal relevance:** technical moat, replaceability, pricing power.

### C3 — Customer labor reduction

> Customers using Meridian reduce support labor hours materially after deployment.

**Deal relevance:** customer ROI, sales narrative, retention, post-close value thesis.

### C4 — Cost per successful automated resolution

> Meridian can deliver a successful automated resolution at a low single-digit-to-low-double-digit cents model/API cost.

**Deal relevance:** gross margin, scaling economics, competitive pricing.

### C5 — Proprietary-data advantage

> Meridian's accumulated customer interaction/feedback data creates measurable model-system performance lift that a new entrant cannot immediately reproduce.

**Deal relevance:** data moat, durability, competitive defensibility.

### C6 — Cross-customer / cross-vertical generalization

> Meridian's performance remains broadly stable when deployed to new customers and different support domains.

**Deal relevance:** TAM expansion, implementation risk, sales efficiency, scalability.

## 4. Hidden-case design requirements

The hidden construction must satisfy all of the following. These are **design constraints**, not the answer key.

1. At least one claim is genuinely strong and should survive AI-Q.
2. At least one claim is technically reproducible but becomes materially less impressive after proprietary attribution.
3. At least one claim is technically true under a narrow cost definition but weakens after production-economic normalization.
4. At least one claim degrades on a fresh holdout / distribution shift.
5. At least one claim cannot be fully resolved from the evaluator materials and should land on **INSUFFICIENT EVIDENCE**, not forced validation or rejection.
6. At least one positive technical property not emphasized by management should be discoverable if the evaluator investigates the evidence rather than merely attacking claims.
7. No hidden weakness may depend on trivia, wordplay, inaccessible real-world facts, or a secret rule the evaluator could not reasonably test.
8. Management materials should be defensible as optimistic corporate presentation rather than requiring fraud to make the case work.
9. The target should contain correlated claims so the evaluator must identify load-bearing mechanisms rather than treating every statement independently.
10. The case must be implementable with deterministic or seeded synthetic artifacts so the eventual ground truth is auditable.

## 5. Mechanism families the builder may use

The builder will create discrepancies using realistic mechanism families. The mapping of mechanism -> claim and all exact hidden values belong only in the hidden truth bundle.

Permitted mechanism families include:

- denominator / eligibility-definition differences;
- comparator quality differences;
- base-model versus orchestration attribution;
- retries/search-budget dependence;
- first-pass cost versus cost-per-successful-resolution;
- omitted fallback or human-review cost;
- customer-selection / survivorship effects;
- temporal split versus random split;
- in-domain versus fresh-tenant holdout performance;
- proprietary-data contribution concentrated in specific segments;
- metric aggregation hiding subgroup degradation;
- version/configuration dependence;
- latency or throughput constraints;
- stochastic instability within plausible operating settings;
- observational ROI evidence that does not identify causal labor savings.

Not every mechanism should be used. Case 003 should remain small enough that a disciplined evaluator can identify the load-bearing issues.

## 6. Evaluator-facing data room manifest

The buyer/evaluator package will contain the following logical artifacts. Final file formats may be CSV/JSON/Markdown/Python as appropriate.

### A. Transaction and management materials

`00_DATA_ROOM_README.md`
- transaction framing;
- buyer question;
- scope and access limitations;
- explicit statement that the company and data are synthetic.

`01_CIM_AI_EXCERPT.md`
- management's concise AI/product narrative;
- key KPI claims;
- moat narrative;
- cost/economic narrative.

`02_MANAGEMENT_CLAIM_LEDGER.csv`
- claim ID;
- exact claim wording;
- represented metric;
- source;
- period;
- stated comparator;
- claimed decision relevance.

`03_PRODUCT_ARCHITECTURE.md`
- high-level system architecture;
- base model/provider abstraction;
- router/orchestration components;
- retrieval/data layer;
- escalation/fallback path;
- human-review points.

### B. Technical evaluation materials

`04_INTERNAL_BENCHMARK_REPORT.md`
- represented benchmark methodology;
- primary results;
- subgroup table;
- known limitations disclosed by management.

`05_EVAL_CASES.csv`
- seeded synthetic evaluation cases;
- customer/vertical/task metadata;
- ground-truth outcome fields that would ordinarily be available to the target evaluator;
- split labels only where management would plausibly expose them.

`06_SYSTEM_RUN_OUTPUTS.csv`
- per-case system outcomes;
- automated/escalated status;
- quality result;
- latency;
- retry count;
- model-call count;
- token/compute fields necessary for economic reconstruction.

`07_BASELINE_RUN_OUTPUTS.csv`
- comparable output for the represented baseline/generic scaffold;
- enough information to test the advertised proprietary lift.

`08_EVALUATION_HARNESS.py`
- deterministic scoring implementation;
- computes the represented headline metrics from run artifacts;
- documented assumptions and thresholds.

`09_REQUIREMENTS_OR_ENVIRONMENT.md`
- execution environment / dependency notes;
- deterministic seed and reproducibility instructions where relevant.

### C. Economic and customer evidence

`10_COST_MODEL.csv`
- model/API prices or synthetic unit costs;
- infrastructure variable costs represented in the case;
- retry/fallback-related inputs;
- explicit distinction between included and excluded cost categories where management materials disclose one.

`11_CUSTOMER_ROI_SUMMARY.csv`
- synthetic customer-level before/after support volume;
- staffing/labor-hour summary;
- adoption period;
- customer segment / vertical;
- enough structure to evaluate how strong the labor-reduction claim really is without fabricating causality.

`12_CUSTOMER_COHORT_NOTES.md`
- customer cohort construction;
- exclusions disclosed by management;
- implementation dates;
- material operational caveats.

### D. Management Q&A and limitations

`13_TECHNICAL_QA.md`
- realistic management answers to likely diligence questions;
- versioning, retries, evaluation method, data sources, baseline choice, human review.

`14_KNOWN_LIMITATIONS.md`
- limitations management acknowledges;
- unavailable evidence;
- items that cannot be fully resolved in the synthetic data room.

`15_DATA_DICTIONARY.md`
- exact field definitions across CSV/JSON artifacts.

## 7. Hidden builder bundle manifest

**This bundle must NOT be placed in the public/evaluator-facing repository before the blind run.**

It will be created separately at the next checkpoint and frozen before evaluator execution.

Planned hidden artifacts:

`H00_CASE_CONSTITUTION.md`
- what the builder is allowed and forbidden to change after freeze;
- pass/fail criteria for the synthetic case.

`H01_GROUND_TRUTH_CLAIM_MATRIX.json`
- true state for C1–C6;
- exact underlying values;
- intended AI-Q conclusion range;
- acceptable ambiguity.

`H02_CAUSAL_MECHANISM_MAP.md`
- which hidden mechanism(s) generate each discrepancy;
- dependencies among claims;
- which mechanisms are load-bearing.

`H03_HOLDOUT_TRUTH.csv`
- fresh-tenant / distribution-shift ground-truth results not labeled as such to the evaluator beyond what a real diligence process could request or derive.

`H04_ECONOMIC_TRUTH.csv`
- complete variable-cost ledger;
- retries, fallbacks, human review, and other hidden-but-discoverable cost components;
- true cost-per-successful-resolution calculation.

`H05_DATA_GENERATION_SPEC.md`
- deterministic synthetic data-generating process;
- seeds;
- distributions;
- relationships among variables.

`H06_GENERATOR_AND_VALIDATION_SCRIPT.py`
- regenerates evaluator-facing artifacts from the frozen hidden specification;
- asserts internal consistency.

`H07_EXPECTED_DISCOVERIES.md`
- what a strong blind evaluator should notice;
- what it should *not* be expected to infer;
- expected false-positive traps to avoid.

`H08_FREEZE_MANIFEST.sha256`
- hashes of all hidden-truth artifacts after freeze.

A public precommitment record may expose only the combined hash/timestamp before the blind run, not the hidden contents.

## 8. Blind boundary

The Case 003 evaluation is invalid if the evaluator has access to the hidden truth.

Rules:

- evaluator receives AI-Q v0.1 and the evaluator-facing data room only;
- hidden files must not be committed to the public `robert-morong-research` repository before evaluation;
- hidden-truth filenames must not leak answer-bearing semantics into evaluator-facing metadata;
- the data room may include limitations and imperfect evidence exactly as a real deal would;
- no post-hoc edits to hidden truth after freeze;
- if an evaluator requests a reasonable follow-up artifact, the builder may supply it only if the frozen construction already determines the answer and the request would be plausible in live diligence;
- all such follow-up disclosures must be logged.

## 9. Expected AI-Q work product

The evaluator must produce the v0.1 required outputs:

1. two-page maximum IC summary;
2. claim matrix covering REAL / PROPRIETARY / DURABLE / ECONOMIC;
3. reproduction record;
4. controlled-test matrix;
5. evidence appendix;
6. one highest-value remaining test.

The evaluator is specifically forbidden from inventing a composite 0–100 AI-Q score.

## 10. Case 003 pass conditions

Case 003 is successful as a **test of AI-Q**, not because AI-Q reaches a predetermined bearish or bullish answer.

The blind run should demonstrate that AI-Q can:

- identify C1–C6 or equivalent material claim decomposition;
- reproduce the represented metrics where sufficient artifacts exist;
- distinguish a real result from a proprietary result;
- identify at least one load-bearing attribution issue;
- detect economically misleading metric construction where evidence permits;
- identify holdout / durability weakness where evidence permits;
- preserve at least one genuinely unresolved question as unresolved;
- recognize at least one legitimate strength;
- write transaction-relevant conclusions without claiming to value the company;
- trace every consequential conclusion to an artifact, calculation, or explicit inference.

## 11. Failure / redesign signals

The case or protocol needs redesign if:

- the hidden issue can only be found by guessing the builder's intent;
- the evaluator must rely mainly on subjective LLM scoring;
- the data room is so rich that the answer is trivial;
- the data room is so sparse that every conclusion becomes insufficient evidence;
- the AI-Q protocol cannot separate REAL from PROPRIETARY;
- economics cannot be reconstructed from available artifacts;
- the report becomes generic technical commentary rather than a changed decision view;
- the builder has to alter hidden truth after seeing the blind result.

## 12. Build order

The build must proceed in this order:

1. **Architecture** — this document. **DONE.**
2. **Hidden-truth design** — specify exact truth/mechanisms privately.
3. **Hidden freeze** — generate/hash the answer-bearing bundle.
4. **Evaluator-facing data room** — generate from frozen truth.
5. **Integrity checks** — confirm all visible artifacts are internally consistent and no hidden answer leaks.
6. **Blind AI-Q run** — fresh evaluator receives no hidden truth.
7. **Score against ground truth** — compare findings with the frozen hidden matrix.
8. **Protocol repair** — only evidence-justified changes.
9. **Case 004** — materially different target to test transfer.

## 13. Current stop point

Do **not** build the evaluator-facing files yet.

The next checkpoint is to define the exact hidden truth for C1–C6, the causal mechanism map, the synthetic data-generating process, and the precommitted evaluation expectations. Only after that hidden layer is frozen should the buyer-facing data room be generated.
