# AI-Q v0.1.1 — Independent Quality of AI Diligence Protocol

**Status:** internal protocol / Case 003 repair release  
**Supersedes for validation:** `ai-q-v0.1-spec.md`  
**Working name:** AI-Q (not trademark-cleared)  
**Purpose:** determine whether transaction-relevant AI claims are real, proprietary, durable, and economically meaningful while making every material conclusion traceable to an exact evidence path.

## 0. Why v0.1.1 exists

AI-Q v0.1 correctly separated several important claim types in the first Project Meridian blind run, but the run exposed two unacceptable failure classes:

1. **provenance overstatement** — an evaluator described calculations and artifacts as though it had executed or inspected them when it had not; and
2. **inference overreach** — an evaluator converted measured evidence into unsupported claims about moat duration, competitor parity, pricing, guarantees, R&D needs, and test design.

v0.1.1 preserves the original four-part measurement frame and adds hard execution, provenance, uncertainty, and recommendation boundaries.

## 1. Core decision question

> **Does the AI advantage a buyer is being asked to pay for appear real, proprietary, durable, and economically meaningful?**

The four dimensions remain:

- **REAL** — does the represented result reproduce or reconstruct from supplied evidence?
- **PROPRIETARY** — how much of the observed advantage is attributable to target-specific technology/data rather than commodity components or unequal operating budgets?
- **DURABLE** — does the advantage survive reasonable perturbation, transfer, holdout, version, and operating-condition changes?
- **ECONOMIC** — does the surviving technical advantage remain meaningful after decision-relevant production costs and constraints are counted?

AI-Q is a measurement module. It is not legal, accounting, security, privacy, regulatory, commercial, valuation, or full architecture diligence.

## 2. Governing evidence rule

AI-Q may say only what the evidence path licenses.

Every consequential statement must be one of:

1. **MEASURED / REPRODUCED** — directly computed from supplied artifacts under a preserved command/protocol;
2. **SOURCE-REPORTED** — stated by management/source material but not independently computed;
3. **EVIDENCE-SUPPORTED INFERENCE** — logically supported by measured/source evidence with assumptions stated;
4. **BUYER ASSUMPTION** — a decision input selected by the buyer, not established by the evidence;
5. **PROPOSED NEXT TEST** — a suggested experiment or diligence request whose design parameters are not represented as known facts;
6. **INSUFFICIENT EVIDENCE** — the available evidence cannot distinguish live alternatives.

A sentence that cannot be assigned one of these types should not appear in the report.

## 3. Exact provenance requirement

### 3.1 Artifact identity

Every artifact cited in an AI-Q report must use its **exact supplied filename/path**.

The evaluator must not:

- invent a plausible filename;
- rename an artifact in prose as if that were its actual name;
- imply that an artifact existed if it did not;
- claim to have inspected a file it did not inspect.

For a frozen diligence package, the report must preserve or reference:

- exact path;
- SHA-256 where supplied or generated;
- relevant command/script;
- execution output or calculation record.

**Invented artifact identity is a hard provenance failure.**

### 3.2 Execution verbs are controlled

Use:

- **"reproduced" / "regenerated" / "recomputed"** only if code was actually executed against the identified artifacts during the evaluation path;
- **"reconstructed"** when a conclusion is calculated from supplied frozen outputs without rerunning the underlying system;
- **"reported"** when merely taken from source material;
- **"not tested"** when the execution was not performed.

Do not say "we ran," "we verified," or "we recomputed" merely because a prior dossier contains a number.

### 3.3 Deterministic boundary

Where structured artifacts and executable scoring logic exist, deterministic code should compute measurable quantities before an LLM interprets them.

The LLM may:

- select high-value tests;
- interpret differences;
- identify missing evidence;
- translate results into bounded transaction language.

The LLM must not replace available deterministic arithmetic with free-form estimation.

## 4. Blind-validation execution rule

For a formal AI-Q blind validation:

1. the evaluator receives the **actual frozen evaluator-facing data room**;
2. the hidden builder truth remains inaccessible;
3. the evaluator or deterministic runner executes the supplied reproduction harness where feasible;
4. additional calculations are run directly against the actual supplied files;
5. stdout/results, commands, artifact hashes, and deviations are preserved;
6. the evaluator must inspect relevant source/limitation/Q&A materials, not just a pre-digested summary;
7. external web research is disallowed unless the case protocol explicitly authorizes it;
8. the final report is frozen before any comparison with hidden truth.

A pre-digested evidence summary may be used as an index, but it cannot substitute for access to the underlying data room in an end-to-end validation claim.

## 5. Evidence states

Material conclusions use:

- **REPORTED** — present in source material only;
- **RECONSTRUCTED** — derived from supplied artifacts without rerunning the underlying represented system;
- **REGENERATED** — rerun through the supplied/defined execution path;
- **INDEPENDENTLY VERIFIED** — reproduced through a materially independent execution path;
- **PARTIALLY SUPPORTED** — important components survive but material components weaken or remain unresolved;
- **NOT SUPPORTED** — evidence fails the claim as scoped under the documented test;
- **INSUFFICIENT EVIDENCE** — evidence cannot distinguish the relevant alternatives.

A failed rerun is not evidence of deception. AI-Q localizes the earliest proven discrepancy.

## 6. Claim-scope rule

A narrow claim that reproduces under its stated definition remains real **as narrowly stated**, even when a broader decision-relevant metric is materially worse.

Example pattern:

> "AI inference cost is $0.09 per successful automated resolution" may reproduce under a disclosed inference-only definition.

If full variable cost is $0.43 after retries/fallback/human review, the correct language is:

- narrow claim: **SUPPORTED as defined**;
- broader transaction economics: **PARTIALLY SUPPORTED / unresolved as appropriate**;
- implication: the narrow metric should not substitute for full production cost.

Do not convert scope mismatch into a falsehood.

## 7. Prohibited inference leaps

Unless directly supported by evidence or explicitly labeled as a buyer assumption / proposed scenario, AI-Q must not assert specific values for:

- competitor time-to-parity;
- moat duration;
- future market share;
- acquisition price;
- EBITDA impact;
- valuation multiple change;
- pricing power;
- performance guarantees;
- required R&D spend;
- contract pricing or budget ranges;
- implementation timeline;
- test sample size, duration, cost, or success threshold;
- competitor unit economics;
- legal/IP defensibility;
- speed with which a competitor can acquire equivalent data or talent.

### 7.1 Counterfactual rule

Evidence that a proprietary component adds lift does **not** by itself prove long-run defensibility.

Evidence that a component contributes little on a new-customer cohort does **not** by itself establish how quickly competitors reach parity.

Evidence that one vertical underperforms does **not** by itself establish that the vertical is impossible, out-of-scope, or requires a particular amount of retooling.

### 7.2 Proposed decision rules

AI-Q may recommend a threshold or test only when clearly labeled:

> **PROPOSED BUYER DECISION RULE — not established by current evidence.**

It must explain why the rule would reduce decision uncertainty. Exact numerical thresholds require an evidence basis or must be presented as parameters for the buyer to choose.

## 8. Symmetric diligence rule

AI-Q is not an attack-only process.

Every case must include an explicit **Thesis-Strengthening Evidence Scan** asking:

- What survived stronger controls than management emphasized?
- What safety, quality, calibration, reliability, cost, transfer, or operational property is better than the headline narrative suggests?
- Did any ablation or stress test reveal a legitimate proprietary advantage?
- Are failure modes bounded or selectively escalated rather than silently wrong?
- Is there evidence that should increase, rather than decrease, deal confidence?

If no thesis-strengthening evidence is found, say so. Do not invent one.

## 9. Per-claim workflow

### Step 1 — Freeze

Record the exact claim, source, metric, data/benchmark, model/system version, comparator, retry/budget policy, economic implication, and decision sensitivity.

### Step 2 — Inventory and hash

Before interpretation:

- list actual supplied files;
- verify manifest where supplied;
- compute/preserve hashes where practical;
- identify which artifacts can support each claim.

### Step 3 — Reproduce / reconstruct

Run the represented harness where supplied and preserve stdout.

Then independently recompute high-value metrics from raw structured artifacts where practical.

### Step 4 — Attribute

Separate where feasible:

- commodity/base model;
- target orchestration/scaffold;
- proprietary data/memory;
- prompt/policy;
- retries/search budget;
- human intervention;
- external services/infrastructure.

Do not call the residual "proprietary moat" unless the comparison actually supports that language.

### Step 5 — Stress-test

Run the smallest set of high-information tests likely to alter decision weight.

Potential tests include:

- comparable-budget baseline;
- data/scaffold ablation;
- fresh-customer/holdout transfer;
- subgroup analysis;
- seed/order/prompt perturbation;
- cost/latency budget;
- model/version sensitivity.

### Step 6 — Normalize economics

Separate at minimum, where evidence permits:

- management-reported narrow metric;
- all model/retrieval/orchestration spend;
- retries/failed attempts;
- human review/fallback;
- omitted fixed or implementation costs.

Do not infer competitive cost advantage without a competitor cost comparator.

### Step 7 — Run thesis-strengthening scan

Explicitly record positive findings and whether they survive controls.

### Step 8 — Translate with evidence labels

For every material claim output:

- **Claim as frozen**
- **Measured/reported result**
- **REAL**
- **PROPRIETARY**
- **DURABLE**
- **ECONOMIC**
- **Evidence state**
- **Evidence path**
- **Unresolved uncertainty**
- **Evidence-supported transaction implication**
- **Buyer assumption(s), if any**
- **Proposed next test, if any**

## 10. Conclusion categories

Each dimension uses only:

- **SUPPORTED**
- **PARTIALLY SUPPORTED**
- **NOT SUPPORTED**
- **INSUFFICIENT EVIDENCE**
- **NOT TESTED / NOT APPLICABLE**

No arbitrary 0–100 AI-Q score is permitted.

## 11. Required output format

### 1. Investment-Committee Summary

Maximum target length: ~2 pages. State:

- the overall **AI Premium Support** conclusion;
- material claims that survive;
- material claims that weaken/fail;
- measured proprietary contribution where defensible;
- durability/transfer limitations;
- economic normalization;
- thesis-strengthening evidence;
- highest-impact unresolved uncertainties.

### 2. Claim Matrix

| Claim | REAL | PROPRIETARY | DURABLE | ECONOMIC | Evidence state | Exact evidence path | Deal implication |
|---|---|---|---|---|---|---|---|

### 3. Reproduction Record

Must include:

- exact files inspected;
- hashes / manifest status;
- exact commands/scripts executed;
- stdout or compact output record;
- deviations;
- what was **not** executed.

### 4. Controlled-Test Matrix

For each test:

- hypothesis;
- variable changed;
- exact artifacts used;
- calculation/command;
- result;
- bounded interpretation;
- affected AI-Q dimension.

### 5. Thesis-Strengthening Evidence

A dedicated section containing only evidence-supported positive findings.

### 6. Evidence Appendix

Exact artifact paths, relevant hashes, calculations, source references, and limitations.

### 7. Highest-Value Next Test

Must contain three labeled fields:

- **EVIDENCE GAP** — what remains unresolved;
- **PROPOSED TEST** — what test would reduce it;
- **DESIGN PARAMETERS** — either evidence-derived parameters or explicitly **TBD / buyer-selected**. Do not invent precise n, duration, cost, or threshold values.

## 12. Recommendation-language firewall

All transaction recommendations must be divided into:

### A. Evidence-supported implication

A conclusion directly licensed by current evidence.

### B. Buyer assumption / policy choice

A parameter the investment committee must choose, such as acceptable error rate, required margin, performance threshold, or risk tolerance.

### C. Proposed diligence action

A request/test designed to reduce a named uncertainty.

Do not collapse B or C into A.

## 13. Hard report failures

A blind validation report automatically fails the provenance/epistemic-quality gate if it:

- invents an artifact filename/path;
- claims an execution that did not occur;
- cites a metric not reproducible from identified artifacts;
- provides a numerical moat duration / parity timeline without evidence;
- provides unsupported pricing, guarantee, R&D, valuation, or EBITDA numbers as facts;
- converts a narrow valid claim into "false" solely because a broader metric differs;
- omits material evidence that strengthens the thesis when that evidence is discoverable;
- uses external web knowledge during a no-web blind case;
- hides an unresolved uncertainty behind confident prose.

## 14. Stop rules

Stop testing when:

- the buyer-relevant decision threshold is met;
- another test has low expected information value;
- access limitations prevent discrimination;
- remaining uncertainty cannot change the recommended diligence action.

Do not add tests for report length.

## 15. Case 003 v0.1.1 rerun rule

The v0.1.1 repair test must use:

- the **same Project Meridian hidden truth**;
- the **same evaluator-facing data-room files**;
- the existing evaluator-package SHA-256 / manifest;
- no answer-bearing changes to the target.

The independent evaluator must operate on the real data room, not the v0.1 summary dossier.

Improvement is demonstrated only if the second blind run:

1. preserves the core substantive discoveries from v0.1;
2. cites exact real artifacts and actual execution steps;
3. removes unsupported time-to-parity / moat-duration / pricing / guarantee / R&D assertions;
4. scopes the $0.09 claim correctly;
5. explicitly surfaces genuine thesis-strengthening evidence;
6. clearly separates evidence-supported implications from buyer assumptions and proposed tests.

Only after this gate should AI-Q advance to a materially different Case 004.

## 16. Commercial hypothesis

Unchanged: AI-Q is being tested as a standardized **AI-claims measurement module** for transactions in which AI performance or differentiation materially affects the investment thesis.

The commercial product is not the LLM's opinion. The product is the controlled evidence path from **claim → artifact → execution → attribution → stress → economics → bounded transaction implication**.
