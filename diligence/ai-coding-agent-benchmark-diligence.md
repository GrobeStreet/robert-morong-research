# Public Technical Diligence Demonstration: AI Coding-Agent Benchmark Claims

**Status:** Working demonstration — public evidence only; not a diligence opinion on any specific company.

**Purpose:** Show how an independent AI-evaluation auditor would stress-test a common transaction claim such as “our coding agent scores X% on SWE-bench” before an investor treats that number as evidence of product quality, technical moat, or enterprise readiness.

## Executive question

**How much decision weight should an investment committee place on a public coding-agent benchmark score?**

A benchmark score can be useful evidence, but only after separating at least five questions:

1. Is the reported number reproduced under the claimed configuration?
2. Does the score survive reasonable changes in task set, environment, model version, retry budget, and harness?
3. Is the benchmark vulnerable to contamination, overfitting, leakage, evaluator instability, or hidden compute advantages?
4. Does the benchmark measure something economically relevant to the target company's product and customers?
5. Does the target possess a durable technical advantage, or is the result primarily inherited from the underlying frontier model, benchmark-specific scaffolding, or unusually favorable evaluation choices?

The diligence objective is **not** to prove that a benchmark is “good” or “bad.” It is to quantify how much uncertainty remains after controlled reproduction and perturbation.

---

## Why this matters in AI M&A

AI coding products are often marketed using benchmark results because the numbers are compact and legible. The transaction risk is that a clean headline score can compress several hidden variables into one number: task composition, model access, retry budget, tool permissions, environment reliability, grader behavior, cost, latency, and benchmark exposure.

Recent benchmark work itself highlights these risks. SWE-bench Pro explicitly describes contamination, limited task diversity, unrealistic task simplification, and unreliable/reproducible testing as limitations of earlier software-engineering benchmarks. Its public leaderboard is also materially harder than SWE-bench Verified, illustrating how rankings and absolute performance can change when the task distribution changes.

Public references:
- SWE-bench / official benchmark organization: https://github.com/swe-bench
- SWE-bench Pro public leaderboard and methodology: https://labs.scale.com/leaderboard/swe_bench_pro_public
- SWE-bench-Live: https://swe-bench-live.github.io/

---

# Diligence framework

## Claim ledger

Every target claim should be written as a testable statement before running experiments.

| ID | Target claim | Evidence supplied | Verification state | Decision relevance |
|---|---|---|---|---|
| C1 | Agent achieves the advertised benchmark score | Public leaderboard / company materials | Unverified | High |
| C2 | Performance is attributable to the agent architecture rather than only the base model | Ablations / matched-model comparison | Unverified | High |
| C3 | Performance generalizes beyond the benchmark distribution | Alternate benchmark / held-out repository set | Unverified | High |
| C4 | Evaluation is reproducible | Frozen code, environment, seeds, harness | Unverified | High |
| C5 | Economics support the product thesis | Cost/task, latency, retry budget, infrastructure | Unverified | High |
| C6 | Advantage is durable | Unique wins, model portability, data/scaffold moat | Unverified | High |

No claim is promoted from **reported** to **verified** solely because it appears in marketing material or on a leaderboard.

---

## Audit 1 — Exact reproduction

Freeze:
- repository commit;
- agent version;
- base model and exact model version;
- benchmark release;
- task IDs;
- environment/container versions;
- tool permissions;
- max steps / retries;
- token and dollar budgets;
- random seeds;
- grading harness.

Run the advertised configuration without optimization.

Output:
- reproduced pass rate;
- confidence interval;
- failed-task list;
- variance across deterministic/repeated runs where applicable;
- exact cost and runtime;
- artifact manifest and checksums.

**Primary diligence question:** does the public number reproduce closely enough that an investor can treat it as real?

---

## Audit 2 — Base-model attribution

Run a matched comparison:

**A. Base model + minimal/reference scaffold**  
**B. Same base model + target agent**

Keep task set, model, compute budget, tools, and grader fixed.

Measure:
- absolute lift;
- relative lift;
- incremental cost;
- incremental latency;
- unique wins / regressions;
- failure-type shifts.

**Primary diligence question:** how much enterprise value should be attributed to the target's engineering rather than the upstream model provider?

---

## Audit 3 — Distribution shift

Test against at least one credible alternate distribution, for example:
- a contamination-resistant or more recent benchmark;
- SWE-bench-Live;
- SWE-bench Pro where licensing/setup allows;
- a buyer-supplied private issue set;
- historical internal tickets sampled before the diligence process.

Do not tune on the alternate set before the first measurement.

Measure:
- retained performance ratio;
- rank stability;
- cost stability;
- failure-category drift;
- repository/language-specific degradation.

**Primary diligence question:** is the benchmark score a durable capability signal or a benchmark-local optimum?

---

## Audit 4 — Harness and budget sensitivity

Perturb one factor at a time:

- retry count;
- step budget;
- context size;
- tool access;
- grader/container version;
- timeout;
- temperature / stochastic settings;
- model minor version;
- task subset.

Plot score against cost and operational budget rather than reporting a single point estimate.

**Primary diligence question:** does the headline result depend on unusually generous or fragile evaluation settings?

---

## Audit 5 — Failure localization

Do not store a failed task simply as `FAIL`.

Classify the earliest meaningful divergence:

1. environment/setup;
2. repository understanding;
3. planning;
4. tool selection;
5. tool arguments;
6. code modification;
7. testing/replay;
8. grader incompatibility;
9. timeout/resource budget;
10. invalid final output.

This converts failure data into information about the actual engineering moat and operating risk.

---

# Investment-committee output

A completed diligence engagement would not return “the benchmark is valid” or “the benchmark is fake.” It would return an evidence-weighted conclusion such as:

> **Reported capability is substantially reproducible, but only part of the observed performance lift is attributable to the target's agent architecture. Performance degrades materially on fresher tasks and under a lower retry budget. The technology appears useful, but the public benchmark overstates the durability of the current moat.**

or:

> **The advertised result reproduces under a frozen environment, retains most of its advantage on a held-out task distribution, and generates unique wins not explained by the base model alone. The benchmark evidence therefore provides meaningful support for a differentiated engineering asset, subject to customer-level validation.**

The conclusion should always separate:
- **observed evidence**;
- **inference**;
- **remaining uncertainty**;
- **what evidence would change the investment conclusion**.

---

# Minimum deliverable for a live pilot

A narrow transaction pilot can be scoped around **one material AI claim** rather than a full company audit.

### Inputs
- access to the claimed model/agent configuration;
- benchmark or customer test set;
- code/environment sufficient for replay;
- agreed compute/API budget paid or supplied by the client;
- no requirement that the auditor spend personal funds.

### Deliverables
1. claim ledger;
2. frozen reproduction protocol;
3. exact-match reproduction result;
4. two or three controlled perturbation tests;
5. failure taxonomy;
6. cost/latency sensitivity;
7. provenance manifest;
8. concise investment-committee memo;
9. reproducibility appendix.

### Stop rule
The pilot stops when the remaining uncertainty is unlikely to change the investment decision or when the agreed evidence budget is exhausted.

---

# What this demonstration does **not** claim

This document does not claim:
- experience conducting completed private-equity transactions;
- that public coding benchmarks predict enterprise ROI by themselves;
- that any named vendor's score is misleading;
- that deterministic verification is possible for every commercial AI claim;
- that the current methodology has yet been validated on confidential M&A data.

Those are precisely the claims a real pilot would need to earn.

---

# Why this is relevant to the existing research portfolio

The proposed diligence workflow reuses capabilities already demonstrated across the public research portfolio:

- deterministic and machine-verifiable evaluation (`ai-eval-work-sample`);
- benchmark perturbation and robustness analysis (`mmlu-robustness-audit`);
- preregistration, explicit failure records, provenance, and reproducibility (`bobby-research-os`);
- externally scored scientific reproduction workflow (`fair-universe-2026`, currently in progress);
- out-of-sample validation and statistical hygiene across prior quantitative projects.

The commercial hypothesis is therefore narrow and testable:

> **Can reproducibility-first AI evaluation improve the quality of technical diligence on material AI product claims?**

This public demonstration is the first artifact toward answering that question. A real transaction or historical-diligence pilot would be the required next external receipt.
