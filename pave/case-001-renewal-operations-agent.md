# PAVE Case 001 — Renewal Operations Agent

**Codename:** Project Relay  
**Domain:** B2B recurring-revenue / SaaS portfolio company  
**Stage:** synthetic proof case  
**Goal:** determine whether a bounded AI agent can reduce renewal-cycle operating burden and protect retained recurring revenue without increasing commercial leakage or customer risk.

## 1. Why renewals

Renewal operations sit at the intersection of customer success, sales, finance, legal, and billing. The process is repetitive but not trivial: the operator must assemble contract terms, product usage, license counts, support history, customer health, commercial policy, pricing/discount authority, and exception conditions before taking action.

This makes renewals a strong PAVE wedge because the workflow has:

- direct revenue/retention linkage;
- structured systems-of-record;
- frequent repeat cases;
- objective timing and labor measurements;
- bounded action rights;
- natural human escalation;
- portability across software companies.

## 2. Case hypothesis

> A renewal agent can autonomously complete the routine preparation and low-risk execution steps for standard renewals, materially reducing human touches and cycle time while maintaining or improving renewal quality, pricing discipline, and exception handling.

PAVE does **not** assume that faster automation equals value. The case passes only if operating gains survive controls for renewal outcome, discount leakage, commercial errors, customer escalation, and human rework.

## 3. Synthetic company

**RelayCloud** — hypothetical PE-backed vertical SaaS business.

Operating profile for the synthetic case:

- recurring annual contracts;
- SMB and mid-market customer base;
- renewals handled by customer-success managers plus revenue operations;
- CRM is the commercial source of truth;
- billing system contains current subscriptions and payment status;
- product telemetry records seat/utilization trends;
- support system records open issues and escalation severity;
- contract repository contains term, notice, pricing, and amendment clauses.

No actual company data is used in Case 001.

## 4. Existing human workflow

A standard renewal currently requires an operator to:

1. identify the renewal window;
2. retrieve current contract and amendments;
3. verify term/end date and notice requirements;
4. retrieve current SKU, seats, billing cadence, and price;
5. inspect payment status;
6. inspect utilization/adoption;
7. inspect support incidents and open escalations;
8. calculate permitted renewal price under policy;
9. identify expansion/contraction signals;
10. prepare renewal recommendation;
11. draft customer communication;
12. route non-standard terms/discounts/issues to the correct human;
13. update CRM tasks/status;
14. create a billing or quoting action after approval;
15. preserve an audit record of the decision path.

## 5. Agent action envelope

The Case 001 agent may autonomously:

- gather records from approved systems;
- reconcile identifiers and flag mismatches;
- calculate contract dates and standard pricing under deterministic policy;
- classify cases as standard vs. exception;
- produce an evidence-backed renewal brief;
- draft communications;
- create internal tasks;
- recommend expansion, flat renewal, contraction review, or escalation;
- execute pre-approved low-risk actions in simulation.

The agent may **not** autonomously:

- change contractual language;
- grant an unapproved discount;
- waive debt;
- change legal terms;
- terminate a customer;
- commit to service credits;
- send a high-risk renewal communication;
- override an unresolved support or compliance flag.

Those cases must escalate.

## 6. Deterministic policy boundary

Commercial rules are encoded outside the LLM where possible.

Examples:

- renewal notice dates;
- approved price-escalator formula;
- discount authority thresholds;
- payment-delinquency thresholds;
- severity levels that force escalation;
- minimum data completeness required for autonomous processing;
- CRM state-transition rules.

The model can interpret unstructured evidence, summarize, and propose. Deterministic code validates policy-sensitive arithmetic and action eligibility before any simulated execution.

## 7. Synthetic dataset design

Case 001 should contain at least four classes of renewal:

### A. Standard / clean
Routine renewal, no support or payment exception, standard price policy.

### B. Expansion opportunity
Usage and seat-growth evidence supports expansion, but agent must not invent a price or sell outside policy.

### C. Retention risk
Low usage, unresolved support issue, or negative health signals require human intervention.

### D. Commercial exception
Non-standard contract language, delinquency, bespoke discount, amendment conflict, or data mismatch forces escalation.

The hidden truth for each case will specify:

- correct contract facts;
- correct policy calculation;
- permitted autonomous actions;
- required escalations;
- correct CRM/billing state transition;
- unacceptable commercial error modes.

## 8. Primary metrics

### Value metrics

- median renewal-cycle time;
- human minutes per renewal;
- human touches per renewal;
- percentage of cases completed without manual preparation;
- retained ARR processed per human hour;
- expansion signals correctly surfaced.

### Quality / risk metrics

- renewal-policy calculation accuracy;
- contract-fact extraction accuracy;
- false-autonomy rate: cases acted on that should have escalated;
- false-escalation rate: routine cases unnecessarily sent to humans;
- discount leakage;
- incorrect customer communication rate;
- unresolved-risk bypass rate;
- human rework minutes.

### Economic metric

Do not claim EBITDA impact directly from labor minutes alone.

Case 001 will calculate an **operating value bridge**:

`gross labor capacity released + measurable retained/expanded revenue benefit - model/infrastructure cost - human review/rework - implementation/maintenance allocation`

Any enterprise-value or EBITDA multiple effect remains a buyer assumption unless directly modeled and supplied by the buyer.

## 9. Control design

Case 001 compares:

**Human baseline** vs. **Agent shadow mode** on the same frozen renewal cases.

The agent does not receive hidden answers. Scoring is deterministic wherever possible.

Minimum comparisons:

- completion time;
- policy accuracy;
- escalation correctness;
- human rework;
- commercial leakage/errors;
- action completeness.

A faster agent that creates more commercial risk fails.

## 10. Success gate

Case 001 advances only if the agent demonstrates all of the following on a held-out synthetic test set:

1. materially lower human preparation burden;
2. no material deterioration in renewal-policy accuracy;
3. bounded false-autonomy rate;
4. correct escalation of risk/exception cases;
5. no systematic discount or contract-term leakage;
6. positive normalized operating value after AI and review cost;
7. stable performance across at least two customer/company policy configurations.

Exact numerical thresholds will be precommitted before the final blind test rather than selected after observing results.

## 11. Failure modes we want to expose

- hallucinated contract terms;
- stale CRM record trusted over signed contract;
- incorrect date arithmetic;
- unapproved discount recommendation;
- ignored delinquency;
- unresolved support severity omitted from renewal recommendation;
- mismatched customer/account IDs;
- expansion recommendation unsupported by utilization;
- confident action despite missing source evidence;
- unnecessary escalation that destroys the labor benefit;
- superficially impressive cycle-time gains erased by human rework.

## 12. PAVE-specific learning objective

The purpose of Case 001 is not merely to prove that an agent can handle renewals.

It must produce the first reusable **PAVE Pattern Card**:

- workflow name;
- company archetype;
- systems required;
- minimum data fields;
- deterministic controls;
- agent tools;
- allowed autonomy envelope;
- primary value metrics;
- principal failure modes;
- rollout prerequisites;
- measured outcome;
- portability limits.

That Pattern Card is the seed of the portfolio benchmark library.

## 13. Next build checkpoint

Build the frozen synthetic RelayCloud renewal data room and hidden answer key, including:

- customer/account master;
- renewal opportunities;
- contracts/amendments;
- subscription/billing snapshot;
- product-usage snapshot;
- support-health snapshot;
- deterministic renewal policy;
- human-baseline workflow record;
- hidden correct actions/escalations;
- deterministic scorer;
- first PAVE Pattern Card template.

Only after the data room and answer key are frozen should an agent be run against the case.
