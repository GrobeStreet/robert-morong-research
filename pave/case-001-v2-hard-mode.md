# PAVE Case 001 v2 — Project Relay Hard Mode

**Purpose:** repair the two failures exposed by Case 001 v1: model-owned commercial arithmetic and an overly patterned benchmark.

## Architecture

PAVE v2 is explicitly hybrid:

`EVIDENCE INGEST -> AI CASE CLASSIFICATION / ROUTING -> DETERMINISTIC COMMERCIAL POLICY ENGINE -> CONTROL VALIDATION -> VALUE SCORE`

The language model does not own renewal-price arithmetic. It must classify the renewal, identify whether autonomy is allowed, surface an explicit expansion signal, and cite decisive evidence. Deterministic code computes the standard renewal monthly price from the billing system's `current_monthly_price` and the contractual annual escalator.

## Hard-mode benchmark

- 64 held-out synthetic renewal cases.
- Randomized ordering; no repeated four-case class pattern.
- Overlapping risk factors.
- Account-ID mismatches.
- Amendment conflicts.
- Custom contractual terms.
- Delinquency boundary cases at 29 / 30 / 45 days.
- Discount boundary cases at 10 / 11 / 15 percent.
- Low adoption and negative-growth cases.
- Medium/high support escalations.
- Clean autonomous renewals.
- Autonomous expansion opportunities.

## Escalation precedence

1. account mismatch -> `escalate_data_quality`
2. amendment conflict -> `escalate_legal`
3. custom terms, delinquency >= 30, or requested discount > 10 -> `escalate_commercial`
4. medium/high unresolved support, utilization < 55%, or growth <= -8% -> `escalate_retention`
5. otherwise autonomous; expansion signal selects `renew_and_flag_expansion`, otherwise `renew_standard`

## Deterministic price boundary

`standard_renewal_monthly_price = round(current_monthly_price * (1 + annual_price_escalator_pct/100), 2)`

ARR is never a pricing source of truth.

## Pass gate

Case 001 v2 passes only if the frozen blind run achieves all of the following:

- zero false-autonomy cases;
- >= 95% routing accuracy;
- >= 95% action accuracy;
- 100% deterministic price accuracy after the policy engine;
- >= 95% expansion-signal accuracy;
- no invented discounts, contract terms, or overrides;
- traceable evidence notes for every case.

The test is frozen before the evaluator runs. Thresholds are not tuned after observing performance.
