# PAVE Case 001 — Project Relay Blind Grade v1.0

**Frozen hidden truth SHA-256:** `6dd319c0b7c4bfd9fa0b45427b7b46fc9b83df5325ecbad0319bc61b7605a299`  
**Frozen evaluator ZIP SHA-256:** `5af0e2521764872352c79ff068dc4fb55bb296a054bdff2fdd8ba65fa4850703`  
**Blind workflow run:** `32672446664`  
**Blind workflow job:** `97275199786`  
**Decision:** **REPAIR — agent reasoning is promising, benchmark/runtime interface and pricing logic are not yet production-grade**

## Executive result

The fresh blind agent correctly recovered the case-routing pattern across all 48 synthetic renewal cases: 24 autonomous renewals, 12 retention-risk escalations, and 12 commercial escalations. It also identified all 12 expansion-signal cases and did not autonomously process the retention-risk or delinquency cases.

However, the run did not produce a valid `agent_actions.csv` artifact. The evaluator runtime prevented the Copilot agent from writing to `/tmp`, so the output validator failed. The agent's complete textual CSV was preserved immutably in the GitHub Actions job log, which allows analytical grading, but this is not equivalent to a successfully frozen output artifact.

More importantly, the agent's pricing logic was materially wrong. It explicitly derived renewal price as `(ARR × (1 + escalator%)) / 12`, while the frozen hidden truth is based on the supplied current monthly billing price and applicable contractual/policy escalator. The prompt itself had correctly instructed the model to derive the price from current monthly price, so this is a substantive reasoning failure rather than merely a formatting issue.

## Grade by dimension

| Dimension | Result |
|---|---|
| Case coverage | **PASS** — all 48 cases analyzed in the preserved text output |
| Autonomy decision | **PASS** — 24/24 autonomous cases and 24/24 escalation cases routed correctly at the high level |
| Retention-risk detection | **PASS** — all 12 medium-support-risk cases escalated |
| Commercial-risk detection | **PASS** — all 12 45-day delinquency cases escalated |
| Expansion detection | **PASS** — all 12 expansion cases flagged |
| False autonomy | **PASS** — no hidden-risk case was classified autonomous |
| False escalation | **PASS** — no clean standard/expansion case was escalated |
| Action taxonomy | **PARTIAL** — semantic routing was right, but action labels differed from the frozen canonical answer key (`surface_expansion` vs `renew_and_flag_expansion`, etc.) |
| Renewal pricing | **FAIL** — wrong source/formula used; only one autonomous case matched the frozen correct price exactly by coincidence |
| Price completeness | **FAIL** — escalated cases output `no` rather than the required numeric standard renewal price |
| Output artifact | **FAIL** — no valid `agent_actions.csv` was written/frozen because of runtime write restrictions |
| Operational-value proof | **NOT YET ESTABLISHED** — labor-time estimates were fixed by prompt, not measured; price errors prevent a clean value conclusion |

## Key substantive finding

The agent appears good at **classification and escalation**, but not yet reliable at **commercial arithmetic / source-of-truth selection**.

That is exactly the distinction PAVE must care about. A renewal agent that safely escalates the right cases but computes renewal economics from the wrong field can still create commercial leakage.

The preserved blind output even states the wrong formula explicitly:

`recommended_monthly_price = (ARR × (1 + annual_price_escalator_pct/100)) / 12`

The frozen truth uses the billing snapshot's current monthly price plus the applicable escalator. This must be moved out of LLM reasoning and into deterministic code.

## Benchmark weakness discovered

The first synthetic case is too patterned. The 48 rows repeat a four-case cadence: standard → expansion → retention risk → commercial exception. That makes routing easier than a realistic portfolio workflow and risks overstating generalization.

Before treating Case 001 as a reusable PAVE Pattern Card, the benchmark should be hardened with:

- randomized case ordering;
- mixed and overlapping exception types;
- custom terms and amendment conflicts actually present in the held-out set;
- account-ID mismatches;
- requested discounts above and below authority thresholds;
- missing/stale fields;
- conflicting sources where signed contract must outrank CRM/billing metadata;
- support-risk cases with multiple severities;
- non-expansion high-usage edge cases and true expansion cases with noisy evidence;
- multiple policy configurations to test portability.

## Required repair

1. Keep the LLM responsible for evidence synthesis, exception classification, and recommended routing.
2. Move renewal-price computation to a deterministic policy engine that consumes only approved source fields.
3. Make the model return the inputs used for each price calculation, so source selection is auditable.
4. Write outputs to the repository working directory rather than `/tmp`, or capture stdout as the canonical artifact.
5. Freeze the actual CSV plus SHA-256 before hidden-truth grading.
6. Harden Case 001 into a less patterned held-out set before claiming repeatability.
7. Re-run the same PAVE concept with the hardened benchmark.

## Decision

### **REPAIR**

Do not kill the renewal wedge. The high-level workflow choice still looks strong: the blind agent correctly separated routine renewals from risk-bearing renewals and surfaced expansion signals without false autonomy.

But **PAVE Case 001 has not yet proved verified operating value**. The pricing error is commercially material, and the benchmark is currently too regular to support a strong portability claim.

The next version should be a hybrid system: deterministic commercial calculations + model-based evidence synthesis/routing, tested on a harder randomized renewal set.
