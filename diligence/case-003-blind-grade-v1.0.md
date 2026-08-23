# Case 003 Blind Grade v1.0 — Project Meridian

**Protocol:** AI-Q v0.1  
**Hidden-truth precommitment SHA-256:** `356acbaddc7b8fcbcd9d2b50e85da8849d68f2dd09f9a3763be94c0a8dc70108`  
**Frozen blind-report SHA-256:** `2e9e2f51f60aa919f8546c58bd388a911b70e5bd3409032a6ef0f74fcaabf5c6`  
**Blind evaluator:** fresh GitHub Copilot CLI session run through GitHub Actions  
**Product signal:** **REPAIR**

## Executive verdict

The Case 003 blind run validates the **core AI-Q reasoning architecture** but does **not** yet validate an end-to-end product.

The fresh evaluator recovered **11 of the 12 precommitted expected discoveries** from the evaluator evidence and correctly made the central distinctions AI-Q was designed to force:

- a claim can be real without the full headline lift being proprietary;
- a proprietary advantage can be measurable but weaker on new customers;
- a narrow cost statistic can reproduce while being incomplete for transaction economics;
- an observed labor reduction can be real while causal attribution remains unresolved;
- a broad generalization claim can fail without implying universal product failure.

However, the run exposed two material classes of defect:

1. **epistemic overreach by the evaluator** — especially unsupported moat-duration, competitor-parity, pricing, guarantee, and vertical-investment conclusions; and
2. **runner / provenance weakness** — the fresh model received a prepared evidence dossier containing deterministic recomputations rather than executing directly against the full 18-file evaluator data room. The report then overstated its own execution provenance and invented artifact filenames.

The correct decision is therefore **REPAIR**, not PRODUCT-ready and not REDESIGN.

The underlying four-part measurement frame — REAL / PROPRIETARY / DURABLE / ECONOMIC — worked. The next version must make the evidence boundary and inference guardrails much harder to violate.

## Claim-by-claim grade

| Claim | Frozen truth requirement | Blind result | Grade | Main issue |
|---|---|---|---|---|
| **C1 — Autonomous resolution** | Internal ~84% is real; fresh performance materially lower; durability only partial; do not call mature claim false; safety gating is a positive strength | Correctly reproduced 83.9%, identified 70.1% onboarding and 59% healthcare, classified REAL supported / DURABLE partial | **PASS** | Did not clearly elevate low wrong-autonomous rate / selective gating as the precommitted positive discovery |
| **C2 — Proprietary architecture lift** | 18.375pp arithmetic is real vs weak management baseline; normalized full-stack lift 8.625pp; architecture-only 5.125pp; data contribution 3.5pp; proprietary claim partial and durability partial | Correctly separated weak comparator, full-stack lift, architecture-only lift, and data contribution | **PASS** | Later narrative turns measured lift into stronger defensibility claims than evidence supports |
| **C3 — Customer labor reduction** | ~34% before/after observation is real; full causal attribution must remain INSUFFICIENT EVIDENCE | Correctly preserved 34% observation while refusing causal attribution | **PASS** | Proposed A/B test is directionally right, but exact n, duration, cost, and success thresholds were invented rather than evidence-derived |
| **C4 — ~$0.09 unit inference cost** | Narrow ~$0.09 statistic is real; decision-relevant cost is materially higher; ECONOMIC should be PARTIALLY SUPPORTED rather than treated as a false claim | Correct math: ~$0.0915 narrow, ~$0.157 model/infra normalized, ~$0.427 mature full variable, ~$0.814 onboarding | **PARTIAL** | Classified ECONOMIC as NOT SUPPORTED and DURABLE as NOT SUPPORTED; also asserted a cost advantage 'disappears and reverses' without a competitor cost comparator |
| **C5 — Proprietary-data advantage** | Mature data lift is real; fresh lift nearly disappears; durability partial; long-run unreplicability / moat duration must remain INSUFFICIENT EVIDENCE | Correctly measured +3.5pp mature and +0.3pp onboarding | **PARTIAL** | Violated the key uncertainty boundary by asserting `<12 months` time-to-parity, `≤12 month` defensibility, and eventual entrant parity without evidence |
| **C6 — Cross-customer / vertical generalization** | Broad stability claim NOT SUPPORTED; degradation is heterogeneous; healthcare is load-bearing weakness; do not generalize failure to every vertical | Correctly rejected broad claim and preserved ecommerce as relatively stronger | **PASS on core claim / PARTIAL on implication** | Added unsupported claims that healthcare is 'out-of-scope,' requires domain retooling / significant R&D, and carries unsupported economic conclusions |

## Precommitted expected-discovery check

The hidden bundle listed 12 discoveries a strong blind evaluator should make.

**Caught: 11 / 12.**

Caught:

1. reproduced ~84% mature automation;
2. detected ~70% fresh-customer degradation;
3. reproduced ~18pp headline comparison and identified comparator weakness;
4. distinguished ~5.1pp architecture-only lift from ~3.5pp data lift;
5. recognized that a real proprietary advantage survives normalization;
6. reconstructed narrow ~$0.09 cost and materially higher normalized cost;
7. preserved the ~34% labor reduction as observational rather than causal;
8. identified mature-vs-fresh collapse in customer-data lift;
9. rejected broad cross-customer / cross-vertical stability;
10. preserved at least one INSUFFICIENT EVIDENCE conclusion;
11. did not accuse management of fraud.

**Missed:**

12. explicitly recognize selective safety / quality gating and the low wrong-autonomous rate as a legitimate under-emphasized technical strength.

This is a meaningful miss because AI-Q must not become an attack-only machine. It must surface evidence that strengthens the investment thesis as reliably as evidence that weakens it.

## Material evaluator overreaches

The frozen report contains several conclusions that are not licensed by the evaluator evidence:

- customer-data time-to-parity is `<12 months`;
- defensibility is on a `≤12 month` horizon;
- new entrants achieve parity once data accrues;
- buyer should require `12+ month` performance guarantees;
- onboarding contracts should budget `$0.81–$1.00` per successful resolution when the supplied normalized point estimate is ~$0.814 and no $1.00 bound is evidenced;
- Meridian's unit-cost advantage 'disappears and reverses' without a competitor cost comparator;
- healthcare is categorically 'out-of-scope' absent retooling and significant post-close R&D;
- an A/B test should specifically use `n ≥ 50`, `8–12 weeks`, `$15K–$40K`, and threshold rules such as ≥75% / <60% without those design parameters being derived from supplied evidence.

Some of these can be framed as **proposed decision rules** in future reports, but they cannot be written as evidence-supported facts unless the report labels them explicitly as assumptions or buyer-selected thresholds.

## Provenance / traceability failure

The most important process defect is not a wrong number. It is provenance.

The blind evaluator did **not** execute directly against the full frozen 18-file Project Meridian data room. It received a compact evaluator evidence dossier containing deterministic recomputations prepared from those files.

Therefore this run tests the **interpretation and transaction-translation layer** of AI-Q more strongly than it tests the complete ingestion / reproduction layer.

The frozen report nevertheless wrote as though it had personally recomputed the raw artifacts and named files such as:

- `core_mature_benchmark.csv`;
- `comparator_outputs.csv`;
- `onboarding_validation.csv`;
- `cost_ledger.csv`;
- `customer_roi_cohort.csv`.

Those are not the actual evaluator-package filenames. The real package uses files including `05_EVAL_CASES.csv`, `06_SYSTEM_RUN_OUTPUTS.csv`, `07_BASELINE_RUN_OUTPUTS.csv`, `10_COST_MODEL.csv`, and `11_CUSTOMER_ROI_SUMMARY.csv`.

This is an **AI-Q traceability failure** even though the numeric conclusions were mostly right. A diligence product cannot invent plausible artifact names or imply an execution step that did not occur.

## Blind-run grading dimensions

| Dimension | Grade | Reason |
|---|---|---|
| **A. Claim identification** | **PASS** | All six material claim families were identified and handled |
| **B. Reproduction accuracy** | **PARTIAL** | Supplied recomputations were interpreted accurately, but the fresh evaluator did not itself run the full raw data-room harness |
| **C. REAL vs PROPRIETARY separation** | **PASS** | Strong separation of headline arithmetic, normalized stack lift, architecture-only lift, and data contribution |
| **D. Durability diagnosis** | **PASS** | Correctly identified fresh-customer degradation and heterogeneous vertical transfer |
| **E. Economic normalization** | **PARTIAL** | Cost math was useful and largely correct, but C4 was classified too harshly and unsupported competitive-economics conclusions were added |
| **F. Uncertainty preservation** | **PARTIAL** | Strong on labor causality; weak on moat duration, parity timing, and several buyer thresholds |
| **G. Positive-strength recognition** | **FAIL** | Did not explicitly surface the precommitted safety-gating / low wrong-auto behavior as a positive finding |
| **H. Transaction usefulness** | **PARTIAL** | IC framing was useful, but several prescriptions exceeded the evidence boundary |
| **I. Evidence traceability** | **FAIL** | Invented artifact names and overstated direct recomputation provenance |

## Product decision

### **REPAIR**

Do **not** move directly to Case 004 yet.

The Case 003 result is too strong to justify a redesign: the central measurement framework found almost every intended substantive issue and preserved important uncertainty in several places.

It is also not strong enough to call the product validated: a PE-grade diligence system cannot tolerate invented provenance or unsupported moat / economics assertions merely because its central numbers are correct.

The next version should repair the evaluator boundary, not replace the company thesis.

## Required repair before rerun

AI-Q v0.1.1 should make the following changes before Case 003 is rerun:

1. the independent evaluator must receive and inspect the **actual frozen evaluator data room**, not a pre-digested evidence summary;
2. deterministic calculations must be executed by code against the actual CSV / Python artifacts, with command outputs preserved;
3. every evidence citation must use an exact artifact filename / hash / calculation record — invented artifact names are a hard failure;
4. the protocol must forbid unsupported claims about competitor time-to-parity, moat duration, pricing, guarantees, R&D requirements, financial-model thresholds, or test cost/timeline unless evidence or an explicitly labeled buyer assumption supports them;
5. narrow-but-valid claims must be distinguished from broader transaction metrics — reproducing a narrow cost definition and then showing a wider cost does not automatically make the narrow claim NOT SUPPORTED;
6. reports must explicitly search for and report **thesis-strengthening evidence**, not only failure modes;
7. recommendations must be separated into **evidence-supported conclusion**, **buyer assumption**, and **proposed next test / decision rule**;
8. the rerun must use the **same frozen hidden truth and same evaluator data room** so improvement measures the repaired AI-Q process rather than a redesigned synthetic target.

## Stop point

Case 003 v1.0 has now been graded.

The next checkpoint is **AI-Q v0.1.1 repair + a second blind run on the unchanged Project Meridian case**.

Only if the repaired run fixes provenance and overreach while preserving the core discoveries should the project advance to Case 004.
