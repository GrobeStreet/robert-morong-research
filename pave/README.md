# PAVE — Portfolio AI Value Engine

**Status:** active research-and-build project  
**Owner:** GrobeStreet  
**Purpose:** identify, build, verify, and compound repeatable AI value-creation workflows across private-equity portfolio companies.

## Core question

> Where can AI measurably increase enterprise value across a PE portfolio, and can that improvement be deployed repeatedly rather than rebuilt from zero at every company?

PAVE is deliberately separate from pre-close AI technical diligence. It is a **post-close value-creation system**.

## Product thesis

A PE firm should not have to rediscover the same AI workflow opportunity independently at each portfolio company. PAVE is intended to create a reusable evidence base linking:

**company archetype → workflow → data requirements → agent architecture → controls → implementation burden → measured operating result → failure modes → reusable deployment package**

Over time, the accumulated library becomes portfolio intelligence: what worked, where, under what conditions, and with what measurable impact.

## Operating loop

1. **PORTFOLIO INGEST** — company type, systems, economics, workflow inventory.
2. **WORKFLOW MAP** — decompose recurring operating processes into observable steps.
3. **VALUE RANKER** — rank workflows by revenue/EBITDA/cash impact, frequency, data readiness, autonomy potential, and implementation risk.
4. **AGENT DESIGN** — define tools, systems of record, decision rights, escalation policy, and human control points.
5. **SHADOW RUN** — execute on historical or parallel cases without granting production authority.
6. **CONTROL TEST** — compare agent vs. existing process on predetermined metrics.
7. **VALUE VERIFY** — attribute measured revenue, retention, labor, cycle-time, quality, or cash impact without double counting.
8. **DEPLOY / KILL** — productionize only if the value threshold survives controls.
9. **PATTERN LIBRARY** — package the successful workflow so the next portfolio company starts from prior evidence rather than zero.

## Case-selection rules

A first PAVE case should be:

- common across many PE-owned software or services companies;
- attached directly to revenue, EBITDA, cash, or retention;
- measurable with pre/post or controlled operational data;
- bounded enough to permit deterministic checks;
- capable of human escalation rather than unsafe full autonomy;
- reusable across companies with modest configuration;
- economically meaningful even if model intelligence becomes commoditized.

## Case 001 selection

**Renewal Operations Agent for B2B recurring-revenue companies.**

Why this wedge:

- renewals exist across nearly every SaaS/subscription portfolio company;
- the workflow is high-frequency, structured, and tied directly to retained ARR and cash;
- required information typically already exists in CRM, billing, product-usage, support, and contract systems;
- AI can prepare and execute low-risk renewal steps while routing exceptions to humans;
- cycle time, touch count, save rate, renewal rate, discount leakage, and human minutes are measurable;
- the same basic workflow can be reused across portfolio companies;
- the resulting pattern library can later expand into onboarding, expansion, collections, and customer-success operations.

## What PAVE is not

- generic AI transformation consulting;
- a chatbot deployment service;
- a promise to replace employees;
- a collection of demos with no value measurement;
- an AI-Q / acquisition-diligence extension.

The product is the **repeatable, measured operating pattern**, not the model call.
