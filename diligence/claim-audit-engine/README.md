# Claim Audit Engine

**Status:** private-development architecture published as inspectable research tooling; deterministic core first.

The Claim Audit Engine turns one material AI/statistical claim into a structured, falsification-first audit pack.

## Design principle

> AI may propose tests. Evidence-state promotion remains deterministic, inspectable, and artifact-backed.

The engine is deliberately narrower than a general diligence platform. It answers:

**What exactly is being claimed, what evidence state has actually been earned, what is the cheapest discriminating next test, and what conclusion is supportable now?**

## Evidence states

- `reported` — present in source material.
- `reconstructed` — derived from preserved source artifacts.
- `regenerated` — rerun under a documented command/environment with an observed result.
- `independently_verified` — regenerated through an independent execution path or external receipt.
- `unresolved` — evidence cannot yet distinguish remaining explanations.

The engine must never promote a claim merely because the narrative is persuasive.

## v0.2 architecture

### 1. Claim freezer
Records exact wording, source, metric, benchmark/data version, configuration, comparator, and decision relevance.

### 2. Artifact manifest
Each evidence artifact receives path/URI, role, SHA256 when bytes are locally available, provenance note, and verification status.

### 3. Evidence-state gate
Rule-based requirements determine whether a requested evidence state is supportable.

### 4. Metric comparison
Stores reported and regenerated values separately and computes deltas without rewriting either source value.

### 5. Test registry
Each proposed test records the hypothesis, one-variable intervention, expected observation under competing explanations, result, and decision value.

### 6. Failure localization
Discrepancies are classified by earliest plausible divergence layer: provenance, environment, data, harness, stochasticity, comparator, attribution, or substantive result.

### 7. Decision memo generator
Outputs the surviving claim, unsupported pieces, eliminated explanations, unresolved uncertainty, and highest-value next test.

## Integrity invariants

1. Historical values remain historical values.
2. Regenerated values never overwrite reported values.
3. Missing provenance stays missing.
4. Every evidence-state promotion has explicit machine-checkable prerequisites.
5. Every test changes one load-bearing variable where practical.
6. Negative results are first-class outputs.
7. External receipts outrank self-reported completion claims.
8. The engine stops when remaining uncertainty cannot change the decision or when the next decisive test is identified.

## Next build

The next implementation layer is a local artifact ingester that calculates checksums, validates manifests, compares reported/regenerated metric records, and emits a deterministic audit bundle. An LLM layer should be added only after these verification primitives are stable.
