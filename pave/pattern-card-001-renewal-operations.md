# PAVE Pattern Card #001 — Renewal Operations

**Pattern ID:** PAVE-PC-001  
**Workflow:** B2B recurring-revenue renewal operations  
**Company archetype:** PE-backed B2B SaaS / recurring-revenue software company  
**Evidence basis:** Project Relay Case 001 v1 + repaired Case 001 v2 hybrid benchmark  
**Current status:** EARNED / synthetic proof gate passed  
**Use:** reusable deployment template for PE portfolio value-creation teams

---

## 1. Value-creation thesis

Renewal operations are a high-value AI automation target because they combine repetitive evidence gathering with commercially consequential decisions.

A renewal operator commonly has to reconcile:

- signed contract terms and amendments;
- billing/subscription records;
- CRM renewal state;
- product adoption and seat utilization;
- support health and unresolved incidents;
- payment delinquency;
- requested discounts;
- customer/account identity;
- commercial policy and approval thresholds.

The workflow is suitable for PAVE when AI is used to interpret and organize evidence while deterministic controls retain authority over money, permissions, contractual constraints, and irreversible actions.

The core architecture is therefore:

> **AI INTERPRETATION LAYER + DETERMINISTIC COMMERCIAL CONTROL LAYER + HUMAN EXCEPTION ROUTING**

The objective is not maximum autonomy. The objective is verified operating value with bounded commercial risk.

---

## 2. What the AI should own

The interpretation layer is well suited to:

- joining and summarizing account evidence;
- recognizing retention-risk signals;
- recognizing expansion signals;
- determining which policy route applies after deterministic hard gates are supplied;
- distinguishing routine renewals from cases that require human intervention;
- producing concise evidence-backed renewal briefs;
- drafting internal recommendations and customer communications;
- explaining why a case is autonomous or escalated;
- surfacing missing or contradictory evidence.

AI output should be treated as an interpreted recommendation, not the authoritative source for commercial arithmetic or legal permissions.

---

## 3. What deterministic controls should own

The Project Relay tests showed that commercially sensitive calculations should not be delegated to the model when explicit structured rules exist.

Deterministic code should own at minimum:

- standard renewal price calculations;
- contractual escalator application;
- notice-date arithmetic;
- discount-authority thresholds;
- payment-delinquency thresholds;
- account-ID consistency checks;
- explicit custom-term and amendment-conflict flags;
- mandatory escalation precedence;
- allowed CRM/billing state transitions;
- fixed operational-cost assumptions used in ROI measurement;
- final execution permission.

Recommended escalation precedence from Case 001 v2:

> **data quality > legal > commercial > retention > autonomous**

Expansion is a signal, not an override. A commercially or legally blocked account does not become autonomous simply because expansion evidence exists.

---

## 4. Required systems and minimum data

A real deployment should expect integrations with most of the following:

### CRM
Minimum fields:
- account/customer ID;
- renewal opportunity ID;
- renewal date;
- account owner;
- requested discount;
- renewal stage;
- current commercial notes.

### Contract repository / CLM
Minimum fields:
- signed customer/account identity;
- term start/end dates;
- notice requirements;
- renewal/escalator language;
- custom terms flag;
- amendments;
- amendment conflicts.

### Billing / subscription system
Minimum fields:
- billing account ID;
- current monthly recurring price;
- SKU/product plan;
- quantity/seats;
- billing cadence;
- delinquency status;
- payment aging.

### Product telemetry
Minimum fields:
- licensed quantity;
- active quantity / utilization;
- recent usage trend;
- 30/60/90-day growth or contraction signal;
- missing-data indicator.

### Support / customer-health system
Minimum fields:
- open ticket count;
- unresolved escalation severity;
- recent critical incidents;
- health indicator if available;
- customer-impact notes.

### Policy configuration
Minimum fields:
- price-escalator rule;
- allowed discount threshold;
- delinquency threshold;
- support-severity escalation rule;
- account/data-quality rules;
- legal/custom-term rules;
- policy version ID.

---

## 5. Recommended autonomy envelope

### Safe candidates for autonomous processing
A case may progress autonomously only when all required evidence is present and deterministic controls confirm that no hard gate is active.

Typical autonomous actions:

- assemble renewal brief;
- calculate and attach deterministically generated standard price;
- classify renewal as standard;
- flag supported expansion opportunity;
- draft approved-template communication;
- create/update internal CRM tasks;
- prepare quote/order data for downstream approval or pre-authorized execution.

### Mandatory human escalation
Escalate when any of the following occurs:

- account/customer identity mismatch;
- custom contractual language requiring interpretation;
- conflicting amendment terms;
- requested discount beyond authority;
- delinquency beyond configured threshold;
- unresolved material support incident;
- retention/adoption risk above policy threshold;
- missing usage evidence where policy requires it;
- incomplete critical source data;
- unsupported model confidence or contradictory records.

Human escalation is not a benchmark failure. Incorrect autonomy is.

---

## 6. Principal failure modes

Project Relay exposed or deliberately tested the following failure classes:

1. **Wrong financial source of truth**  
   Example: calculating renewal price from ARR rather than the billing system's current monthly price.

2. **Hallucinated commercial terms**  
   Inventing discounts, legal terms, pricing, or amendments not present in evidence.

3. **Stale CRM dominance**  
   Trusting a CRM field over signed contract or current billing evidence.

4. **False autonomy**  
   Processing a case that should have been routed to legal, commercial, retention, or data-quality review.

5. **False escalation**  
   Sending routine cases to humans and erasing the labor benefit.

6. **Expansion overriding risk**  
   Treating upsell potential as permission to bypass a commercial or retention exception.

7. **Missing-data blindness**  
   Acting confidently when required evidence is absent.

8. **Identity mismatch**  
   Combining records from different customers/accounts.

9. **Policy-version error**  
   Applying one company's threshold rules to another portfolio company.

10. **Hidden rework cost**  
    Appearing faster while shifting effort into review, repair, escalation, or customer recovery.

---

## 7. Measurement framework

PAVE should compare the deployed workflow against a frozen human baseline or controlled shadow-mode population.

### Operating metrics
- human minutes per renewal;
- human touches per renewal;
- renewal preparation cycle time;
- percentage of cases requiring manual preparation;
- percentage safely processed autonomously;
- escalation volume and reason mix;
- rework minutes.

### Quality / commercial-risk metrics
- false-autonomy rate;
- false-escalation rate;
- routing accuracy;
- deterministic price accuracy;
- contract-fact accuracy;
- expansion-signal accuracy;
- unsupported-evidence rate;
- discount leakage;
- wrong customer/account actions;
- incorrect communications;
- unresolved-risk bypasses.

### Economic measurement

Use a normalized operating-value bridge rather than translating 'hours saved' directly into EBITDA.

> **Net annualized operating value = captured labor/vendor savings + measurable incremental gross profit / retained gross profit - AI/model cost - human review and rework - implementation and maintenance allocation - expected error/remediation cost**

Distinguish explicitly between:

- theoretical labor capacity released;
- actual spend eliminated or redeployed;
- retained revenue;
- incremental expansion revenue;
- working-capital effects;
- one-time implementation savings;
- recurring EBITDA-relevant savings.

Do not multiply synthetic time savings by an EBITDA multiple and present it as enterprise value.

---

## 8. Proven synthetic benchmark result

### Case 001 v1
The initial model demonstrated useful classification and escalation behavior but failed the commercial-control standard because it attempted to own renewal-price arithmetic and used the wrong source/formula.

Key lesson:

> **Models should not own deterministic commercial math when authoritative structured inputs and explicit rules exist.**

### Case 001 v2
The repaired hybrid architecture separated responsibilities:

- deterministic layer: pricing, explicit hard gates, fixed operating assumptions;
- fresh external model: action recommendation, autonomy decision, expansion interpretation, evidence explanation;
- final assembly: deterministic merge of controlled commercial facts and model interpretation.

The harder v2 benchmark contained 64 synthetic cases across two policy configurations, including overlapping exceptions and edge cases.

The precommitted gate required:

- zero false-autonomy cases;
- at least 95% autonomy accuracy;
- at least 92% action accuracy;
- 100% deterministic pricing accuracy;
- at least 92% expansion accuracy;
- no more than 3 false escalations;
- full 64-case schema compliance;
- correct fixed labor assumptions;
- no disqualifying unsupported-evidence failure.

**Result: PASS.**

Canonical v2 benchmark identities:

- evaluator ZIP SHA-256: `46643118e6e7b01fb17af320a8d47c6db6200a44e01f3709586158925191978d`
- hidden answer-key SHA-256: `44853df407322945bb25191673fe43aabfdfd147934732efedb1b37b1d2baf13`

This is a synthetic proof of architecture and control logic. It is not yet evidence of real-company EBITDA impact.

---

## 9. Deployment playbook

### Phase 0 — Scope
Select one portfolio company with recurring contracts, sufficient renewal volume, stable systems of record, and a measurable human baseline.

### Phase 1 — Data contract
Map each required field to an authoritative source. Explicitly define source precedence where systems disagree.

### Phase 2 — Policy encoding
Convert commercial thresholds and action rights into versioned deterministic rules. Legal/commercial owners sign off on the autonomy envelope.

### Phase 3 — Shadow mode
Run the hybrid workflow without customer-facing execution. Compare every recommendation to the human process.

### Phase 4 — Controlled autonomy
Allow only the lowest-risk standard cases to execute pre-approved internal actions. Retain human review for communications or quotes if required.

### Phase 5 — Outcome verification
Measure captured labor reduction, error/rework cost, retention outcomes, expansion outcomes, and net operating value.

### Phase 6 — Pattern normalization
Record the company's policy deltas, system mappings, exception rates, economics, and failure modes so the next portfolio deployment begins from this pattern rather than zero.

---

## 10. Rollout prerequisites

Do not deploy autonomous renewal operations unless the company has:

- identifiable authoritative sources of contract and billing truth;
- versioned renewal policy;
- explicit approval/discount authority;
- reliable customer/account identifiers;
- sufficient historical renewal volume to establish baseline metrics;
- human owners for legal, commercial, retention, and data-quality escalation queues;
- audit logging;
- rollback/manual override;
- monitoring for policy drift and data-source drift.

---

## 11. Portability assessment

**High portability** across B2B SaaS and recurring-revenue software businesses when core systems are CRM + billing + contract + product usage + support.

**Moderate portability** when companies have highly bespoke contracts, channel/reseller structures, consumption pricing, usage-based billing, complex multi-product master agreements, or decentralized renewal ownership.

**Low portability without redesign** for businesses where renewal is primarily negotiated legal work rather than operational processing.

The reusable component is not a single universal agent prompt. It is the architecture, control boundary, evidence schema, measurement method, and rollout process.

---

## 12. PAVE reusable pattern

The portable pattern extracted from Case 001 is:

> **For workflows where unstructured evidence interpretation and structured commercial rules coexist, let AI interpret the evidence, let deterministic systems control money/permissions, route exceptions to humans, and verify value against a frozen baseline.**

This is broader than renewals and can be tested next in other portfolio workflows such as collections, support resolution, onboarding, finance operations, procurement, or sales operations.

---

## 13. Current confidence

**Technical architecture confidence:** HIGH within the bounded synthetic environment.  
**Operational portability confidence:** MODERATE until tested on a real company's systems and exception distribution.  
**Economic-value confidence:** UNPROVEN in production; requires a real shadow-mode deployment and captured-cost measurement.  
**Safety/control confidence:** PROMISING because false autonomy is treated as the primary disqualifying error and commercially sensitive arithmetic is deterministic.

---

## 14. Next evidence required

Pattern Card #001 becomes institutionally meaningful when one real portfolio-company pilot establishes:

1. actual renewal volume and baseline human cost;
2. production system-integration burden;
3. real exception distribution;
4. shadow-mode routing/autonomy performance;
5. real review/rework burden;
6. captured labor/vendor savings rather than theoretical hours;
7. renewal/retention and expansion outcomes;
8. net annualized operating value;
9. repeatability on a second company with a different policy configuration.

Until then, this card should be described as a **synthetically validated deployment pattern**, not a production-proven ROI benchmark.
