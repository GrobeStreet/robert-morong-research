# Public-Evidence Technical Diligence Case: SWE-bench Verified

**Status:** Public-evidence worked example, not a client engagement and not an independent rerun.

**Date:** 2026-08-23

## Question for an investment committee

**How much decision weight should an investor place on a headline SWE-bench Verified score when evaluating an AI coding-agent company?**

This memo demonstrates a narrow diligence workflow using only public primary-source evidence. It does **not** claim that any vendor is misrepresenting results, and it does **not** substitute for a fresh controlled rerun of a target company's system.

## Executive conclusion

A headline SWE-bench Verified percentage is useful evidence of software-engineering capability, but it should not be treated as a stand-alone measure of product quality or defensibility.

The current official SWE-bench materials show that reported results depend on at least four separable components:

1. the underlying model;
2. the agent/scaffold;
3. the scaffold release/evaluation protocol;
4. the economic budget required to obtain the result.

The official leaderboard now exposes both open-scaffold results and a normalized bash-only setting using mini-SWE-agent. This is valuable precisely because it lets diligence distinguish raw model capability from system-level engineering.

For a transaction, the correct question is therefore not simply **"What is the SWE-bench score?"** It is:

> **What portion of the observed score survives when model, scaffold, release, budget, retries, and evaluation harness are controlled?**

Until that decomposition is performed, the benchmark should receive **moderate**, not decisive, investment-committee weight.

---

## 1. Source ledger

Primary sources consulted:

- Official SWE-bench leaderboard: https://www.swebench.com/
- SWE-bench Verified details: https://www.swebench.com/verified.html
- Official evaluation guide: https://www.swebench.com/SWE-bench/guides/evaluation/
- Official benchmark overview: https://www.swebench.com/SWE-bench/
- Official FAQ: https://www.swebench.com/SWE-bench/faq/

All numeric observations below are source-state dependent and should be rechecked before use in a live transaction.

---

## 2. What SWE-bench actually measures

SWE-bench evaluates an AI system on real GitHub software issues. A system receives a codebase and issue description, generates a patch, and the benchmark applies that patch and runs repository tests inside a containerized evaluation environment.

SWE-bench Verified is a human-filtered subset of 500 tasks intended to remove ambiguous or unsolvable items.

This is a materially stronger benchmark than a self-reported coding demo because it uses real repositories, executable patches, and test-based evaluation. That makes it genuinely useful in technical diligence.

But the unit being evaluated is still not automatically "the model." In many leaderboard entries the observed result is the output of a model **plus** an agent scaffold, prompting policy, tool interface, retry policy, and other implementation choices.

---

## 3. Current public observations

At the time of this review, the official leaderboard displayed the following bash-only mini-SWE-agent results among recent entries:

| Model / configuration | SWE-bench Verified resolved | Average reported cost |
|---|---:|---:|
| Claude 4.5 Opus, high reasoning | 76.8% | $0.75 |
| Gemini 3 Flash, high reasoning | 75.8% | $0.36 |
| MiniMax M2.5, high reasoning | 75.8% | $0.07 |
| Claude 4.6 Opus | 75.6% | $0.55 |
| GPT 5.2 Codex | 72.8% | $0.45 |

The full/open-scaffold leaderboard also displayed systems at roughly 79.2% resolved, including Claude 4.5 Opus paired with non-mini-SWE scaffolds.

### Immediate diligence observation

A one-point difference in resolved rate can coexist with a very large cost difference.

For example, the public table showed:

- Claude 4.5 Opus high: 76.8% at $0.75 average reported cost;
- MiniMax M2.5 high: 75.8% at $0.07 average reported cost.

That is roughly a **10.7x difference in reported average cost for a one-percentage-point difference in resolved rate**.

Similarly, Gemini 3 Flash and MiniMax M2.5 were both shown at 75.8%, while their listed average costs differed by more than fivefold.

These figures do **not** establish that one product is economically superior in production. They do establish that the headline benchmark percentage alone is insufficient for economic diligence.

---

## 4. Scaffold attribution risk

The official leaderboard separates a normalized bash-only evaluation from entries using other agents/scaffolds. That distinction is economically important.

Suppose a target company markets a high SWE-bench score as evidence of a proprietary agent architecture. A diligence team should ask:

1. What does the same underlying model score under the normalized mini-SWE-agent harness?
2. What incremental gain is attributable to the target's scaffold?
3. Does that gain persist across multiple base models?
4. Does the gain persist under fixed budgets and retry limits?
5. Does the proprietary scaffold improve hard tasks specifically, or merely extract more attempts/tokens?

A high system-level score may reflect real agent engineering. But without the normalized comparison, an investor cannot know how much of the score is proprietary value versus increasingly capable commodity frontier models.

This is a direct diligence question about defensibility.

---

## 5. Protocol-version risk

The official SWE-bench Verified documentation warns that mini-SWE-agent release 1.x and 2.x results are **not necessarily directly comparable** because 2.x changed how actions are invoked. Earlier releases parsed actions from output strings; 2.x uses tool calling. The temperature policy also changed across these release families.

Therefore, a target-company slide that compares its current score to an older competitor score without aligning evaluation release and settings can create a misleading impression even when every individual number is technically genuine.

### Diligence control

Require a comparison table with:

- exact benchmark dataset/version;
- exact harness/scaffold version;
- exact model identifier;
- temperature/reasoning settings;
- retry policy;
- tool permissions;
- token or dollar budget;
- date of evaluation;
- public/private verification status.

No apples-to-oranges comparison should survive to the investment committee.

---

## 6. Reproducibility strength and residual risk

SWE-bench has unusually strong reproducibility infrastructure. The official evaluator applies model patches, runs repository tests, and records per-instance artifacts such as evaluation logs, test output, patch diffs, and reports.

That substantially lowers one common diligence risk: a vendor can provide predictions and a third party can independently rerun the harness.

Residual risks remain:

- benchmark contamination or training exposure;
- optimization specifically for SWE-bench task distribution;
- cherry-picked configuration or retries;
- stale comparisons against older model/scaffold releases;
- benchmark performance that does not transfer to the buyer's actual repositories;
- economically unattractive token/latency budgets;
- production reliability below benchmark-run reliability.

The benchmark is therefore best treated as **auditable evidence, not a complete product metric**.

---

## 7. Transaction test plan

If this were a live AI coding-agent diligence engagement, I would request a frozen target configuration and run the following tests.

### Test A — Claim reproduction

Reproduce the exact advertised SWE-bench result from a frozen commit and environment.

**Decision value:** establishes whether the headline claim itself is reproducible.

### Test B — Base-model attribution

Run the same base model using the benchmark's normalized mini-SWE-agent setup and compare against the target scaffold.

**Decision value:** estimates proprietary scaffold contribution.

### Test C — Cross-model scaffold transfer

Hold the target scaffold fixed and swap compatible base models.

**Decision value:** tests whether value comes from reusable agent architecture or one privileged model/configuration.

### Test D — Budget sensitivity

Run fixed caps on tokens, retries, wall-clock time, and/or dollar cost.

**Decision value:** determines whether the claimed performance survives an economically realistic operating envelope.

### Test E — Fresh-repository holdout

Build a small preregistered set of recent, target-relevant issues not used to select the system configuration.

**Decision value:** tests transfer away from the public benchmark distribution and reduces leaderboard overfitting risk.

### Test F — Failure anatomy

Classify unresolved tasks by earliest failure layer: repository understanding, localization, planning, tool use, patch generation, test interpretation, or recovery.

**Decision value:** distinguishes fixable product weaknesses from fundamental model limits.

---

## 8. Example investment-committee language

### If the target reproduces cleanly and survives controls

> The coding-agent benchmark claim is independently reproducible under the disclosed configuration. The proprietary scaffold retains measurable lift over a normalized base-model harness and preserves most of that lift under fixed-cost and fresh-holdout conditions. We therefore treat the benchmark as credible evidence of product-level technical differentiation, subject to production reliability and customer-workload validation.

### If the headline score reproduces but differentiation disappears

> The published benchmark score is genuine, but most observed performance appears attributable to the underlying frontier model rather than target-specific agent architecture. Under normalized scaffold and cost controls, proprietary lift is small. We would therefore discount the benchmark as evidence of durable technical moat and shift diligence toward workflow integration, proprietary data, distribution, and customer switching costs.

### If the claim does not reproduce

> We were unable to reproduce the advertised benchmark under the configuration represented to us. Until the discrepancy is explained with versioned artifacts and a successful rerun, we recommend treating the benchmark claim as non-reliable for valuation purposes.

---

## 9. What this worked example proves — and does not prove

### Demonstrates

- how public benchmark evidence can be translated into an investment question;
- how model capability can be separated from scaffold contribution;
- why cost and protocol version belong in benchmark diligence;
- how a benchmark claim can be converted into a preregistered test matrix;
- how conclusions can be written with evidence-calibrated language.

### Does not demonstrate

- a completed paid M&A diligence engagement;
- an independent rerun of the current SWE-bench leaderboard;
- that any named model/vendor is misrepresenting results;
- that benchmark results predict enterprise ROI without further evidence;
- a proprietary financial model or investment recommendation.

---

## 10. Pilot engagement definition

A defensible first commercial pilot would be deliberately narrow:

**Input:** one material technical performance claim from an AI-enabled target company, plus sufficient code/configuration access to reproduce it.

**Output:**

1. frozen claim ledger;
2. reproducibility result;
3. 3–5 controlled sensitivity/adversarial tests;
4. cost/latency normalization where relevant;
5. failure-mode analysis;
6. evidence appendix with commands, versions, hashes, and logs;
7. 2-page investment-committee technical conclusion.

**Success criterion:** the engagement must reduce a real transaction uncertainty—not merely produce more technical analysis.

The commercial hypothesis is that this reproducibility-first module can complement, rather than replace, established product, security, architecture, commercial, and management diligence.
