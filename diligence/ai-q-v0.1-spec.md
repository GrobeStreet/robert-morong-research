# AI-Q v0.1 — Independent Quality of AI Diligence Protocol

**Status:** internal protocol draft / pre-commercial validation  
**Working name:** AI-Q (not trademark-cleared)  
**Purpose:** standardize how material AI claims in transactions are tested, evidenced, and translated into investment-committee decision language.

## Core decision question

> **Does the AI advantage a buyer is being asked to pay for appear real, proprietary, durable, and economically meaningful?**

AI-Q is not a full-company certification and is not a substitute for legal, security, commercial, accounting, architecture, management, regulatory, or full technical diligence. It is a standardized measurement layer for technically material AI claims.

## Design rule

AI-Q must never create confidence by presentation alone.

Every consequential conclusion must bottom out in:

- a frozen claim;
- primary-source evidence where available;
- a documented protocol;
- reproducible calculations or execution artifacts where feasible;
- explicit deviations and limitations;
- a falsifier or unresolved uncertainty;
- a stated transaction implication.

Numerical summary scores are **not** used in v0.1 unless they are directly measured quantities. Composite 0–100 ratings are deferred until they can be calibrated against a sufficiently large reference set. Until then, AI-Q uses evidence states and bounded categorical conclusions.

## The four AI-Q questions

### Q1 — REAL

**Can the material AI claim be reproduced or independently reconstructed from the available evidence?**

Typical tests:

- exact claim rerun;
- metric recomputation;
- benchmark/harness parity;
- version and environment reconstruction;
- repeatability across runs or seeds;
- audit of claimed numerator/denominator and exclusions.

Primary failure modes:

- missing provenance;
- irreproducible configuration;
- metric-definition mismatch;
- benchmark/version mismatch;
- unstable result;
- unsupported or non-reconstructable claim.

### Q2 — PROPRIETARY

**How much of the observed advantage is attributable to target-specific technology rather than commodity models, ordinary scaffolding, retries, hidden human work, or external infrastructure?**

Typical tests:

- base-model normalization;
- scaffold ablation;
- model swap;
- prompt/policy simplification;
- retry-budget normalization;
- human-in-the-loop removal or quantification;
- proprietary-data ablation where lawful and feasible;
- comparator reconstruction.

Key output:

> **Proprietary lift** = the measured incremental value that survives after relevant non-proprietary contributors are normalized.

No proprietary-lift percentage is reported unless the comparison is experimentally defensible.

### Q3 — DURABLE

**Does the claimed advantage survive reasonable changes that should not destroy a genuine capability?**

Typical tests:

- seed/retry sensitivity;
- prompt/format/order perturbation;
- fresh holdout or distribution shift;
- model/version dependence;
- calibration and failure anatomy;
- budget ceilings;
- latency or throughput constraints;
- transfer across representative subgroups or task types.

The test set should be selected to maximize decision value, not test count.

### Q4 — ECONOMIC

**Does the surviving technical advantage remain meaningful after production costs and operating constraints are counted?**

Typical tests:

- token/API/compute cost normalization;
- latency and throughput requirements;
- retries and fallback paths;
- human-review burden;
- infrastructure overhead;
- failure-remediation cost;
- unit-economics sensitivity;
- realistic production operating envelope.

AI-Q does not claim EBITDA impact unless the transaction evidence supports the financial translation. Where financial linkage is incomplete, the output identifies the missing bridge rather than inventing one.

## Claim eligibility

A claim belongs in AI-Q when it is both:

1. **technically testable**, and
2. **decision-relevant** to valuation, moat, integration risk, operating economics, product differentiation, or post-close value creation.

Examples:

- "Our proprietary agent resolves 83% of cases autonomously."
- "Our fine-tuning creates a 14-point lift over the base model."
- "Our inference stack reduces cost per successful task by 60%."
- "Our benchmark result demonstrates production superiority."
- "Our proprietary data creates a durable model advantage."
- "Our AI reduces human workload by 35%."

Claims that are primarily legal, security, privacy, regulatory, or accounting questions should be routed to the appropriate diligence workstream rather than forced into AI-Q.

## Minimum viable inputs

For each material claim:

1. exact claim wording;
2. source document / slide / report / benchmark;
3. metric definition;
4. model and system configuration;
5. dataset / evaluation set definition;
6. comparison baseline;
7. code, logs, outputs, or environment detail sufficient to reconstruct the result where available;
8. retry, budget, latency, and human-review policy where relevant;
9. decision the claim is intended to support.

If access is incomplete, AI-Q may perform a public-evidence or limited-access review, but the evidence state must reflect that limitation.

## Evidence states

Every material conclusion uses one of these states:

- **REPORTED** — present in target/source material but not independently reconstructed.
- **RECONSTRUCTED** — derived from available artifacts without a full rerun.
- **REGENERATED** — rerun under a documented execution protocol.
- **INDEPENDENTLY VERIFIED** — reproduced through a materially independent execution path or external verification route.
- **PARTIALLY SUPPORTED** — important subclaims survive but material components do not or remain unresolved.
- **NOT SUPPORTED** — the available evidence fails the defined claim test under the documented protocol.
- **INSUFFICIENT EVIDENCE** — available evidence cannot distinguish the live alternatives.

A failed rerun is not automatically evidence that management was deceptive. The protocol localizes the earliest proven discrepancy.

## Per-claim workflow

### Step 1 — Freeze

Record:

- claim text;
- source and date;
- metric;
- benchmark/data version;
- model/configuration;
- comparator;
- budget/retry policy;
- claimed economic implication;
- transaction decision sensitivity.

No decisive test may silently change the claim after results are observed.

### Step 2 — Reproduce

Attempt the advertised result with the closest defensible protocol.

Preserve:

- commit / version;
- environment;
- commands;
- inputs;
- model/data revisions;
- logs;
- outputs;
- checksums where practical;
- all deviations from the represented setup.

### Step 3 — Attribute

Identify what components are carrying the result.

Where feasible, separate:

- base-model capability;
- target scaffold/orchestration;
- proprietary data;
- prompt/policy layer;
- retries/search budget;
- humans in the loop;
- external services/infrastructure.

### Step 4 — Stress-test

Run the smallest set of high-information tests likely to change the deal interpretation.

Default maximum for an initial claim sprint: **3–5 controlled tests** unless additional tests are justified by new evidence.

### Step 5 — Normalize economics

Measure the claim inside the operating envelope the buyer actually cares about.

Examples:

- cost per successful task rather than raw cost per attempt;
- performance at a fixed dollar/token/latency ceiling;
- automation rate net of human review;
- quality after retries and fallback behavior are counted.

### Step 6 — Translate

For each claim, produce:

- what management/source reported;
- what AI-Q observed;
- evidence state;
- what changed after controls;
- unresolved uncertainty;
- the single highest-value next test;
- transaction implication.

## v0.1 conclusion categories

AI-Q v0.1 does **not** assign an arbitrary composite score.

Each of REAL / PROPRIETARY / DURABLE / ECONOMIC receives one of:

- **SUPPORTED**
- **PARTIALLY SUPPORTED**
- **NOT SUPPORTED**
- **INSUFFICIENT EVIDENCE**
- **NOT TESTED / NOT APPLICABLE**

The overall **AI Premium Support** conclusion uses the same bounded categories and must include a written basis.

A future numerical AI-Q index requires calibration against a reference corpus and evidence that the number improves decisions rather than merely making the report look precise.

## Required output format

### 1. Investment-committee summary

Maximum target length: 2 pages.

Must answer:

- What AI claims matter most to the deal?
- Which survived?
- Which weakened or failed?
- How much appears proprietary?
- What operating/economic constraints matter?
- What should change in the buyer's decision or follow-up diligence?

### 2. Claim matrix

| Claim | REAL | PROPRIETARY | DURABLE | ECONOMIC | Evidence state | Deal implication |
|---|---|---|---|---|---|---|

### 3. Reproduction record

Protocol, versions, commands, deviations, observed results.

### 4. Controlled test matrix

Test, hypothesis, variable changed, result, interpretation.

### 5. Evidence appendix

Code/version/log/hash/source references and unresolved gaps.

### 6. Next-test recommendation

The single additional test with the highest expected decision value.

## Decision language rules

AI-Q must distinguish:

- **the claim is false**;
- **the claim did not reproduce under this protocol**;
- **the evidence is insufficient**;
- **the claim is real but not proprietary**;
- **the claim is proprietary but not durable**;
- **the claim is technically strong but economically weak**;
- **the claim survives all tested controls within the stated scope**.

These are not interchangeable conclusions.

## Comparative-data capture

Every completed AI-Q case should store a sanitized internal measurement record where permitted, including:

- claim category;
- system type;
- underlying model family;
- baseline type;
- advertised metric;
- reproduced metric;
- measured proprietary lift if defensible;
- holdout degradation;
- cost-normalized performance;
- retry/human dependence;
- failure layer;
- evidence state;
- final deal interpretation.

This is the seed of the long-term reference corpus. No cross-deal benchmark claim may be made until comparability and confidentiality rules support it.

## Stop rules

Stop testing a claim when:

- the decision threshold is met;
- additional tests have low expected information value;
- missing access prevents meaningful discrimination;
- the surviving uncertainty cannot change the recommended action.

Do not perform more tests merely to increase report length.

## v0.1 validation target

The first validation target should be a realistic synthetic AI-native software acquisition case built so that:

- management makes multiple valuation-relevant AI claims;
- some claims are genuinely strong;
- some weaken under attribution or operating constraints;
- at least one important uncertainty remains unresolved;
- the evaluator does not receive the hidden answer key during the diligence run.

AI-Q v0.1 passes its first product test only if the blind report:

1. correctly distinguishes supported, weakened, unsupported, and unresolved claims;
2. identifies the load-bearing technical drivers;
3. produces a materially useful transaction interpretation;
4. preserves uncertainty without collapsing into vague language;
5. can be substantially reused on a second synthetic target without redesigning the protocol.

## Kill / redesign criteria

AI-Q v0.1 should be redesigned rather than commercialized if:

- outputs depend primarily on subjective LLM judgment;
- conclusions cannot be traced to evidence;
- every target requires a bespoke methodology from scratch;
- the report produces technical detail without changing a decision;
- the process cannot separate a real claim from a proprietary claim;
- cost and operating constraints cannot be integrated;
- a second case exposes major protocol instability.

## Commercial hypothesis

AI-Q's initial commercial hypothesis is not that it replaces technical diligence. It is that it becomes a standardized **AI-claims measurement module** that can be used by PE firms, growth investors, strategic acquirers, and existing diligence providers whenever transaction value materially depends on AI performance or differentiation.

The long-term ambition is for the process to become repeatable enough that the buyer asks not "Who can review this AI claim?" but "Has independent Quality of AI diligence been run on it yet?"
