# PAVE Case 001 v2 — Project Relay Hybrid Grade

**Verdict: PASS**

## What was tested

PAVE Case 001 v2 tested the repaired hybrid renewal-operations architecture on the frozen 64-case synthetic RelayCloud benchmark across two policy configurations.

The architecture intentionally separated responsibilities:

- deterministic control layer: policy-sensitive renewal pricing, explicit machine-checkable hard gates, and fixed 8/20-minute operating assumptions;
- fresh external interpretation model: action/routing classification, autonomy decision, expansion recognition, and evidence-grounded explanation;
- workflow assembly layer: deterministic merge and schema validation.

The external interpretation session was executed separately from the hidden builder truth. The builder-aware grading step occurred only after the model-owned output had been frozen.

## Frozen identities

- Archived evaluator ZIP SHA-256: `46643118e6e7b01fb17af320a8d47c6db6200a44e01f3709586158925191978d`
- Hidden answer-key SHA-256: `44853df407322945bb25191673fe43aabfdfd147934732efedb1b37b1d2baf13`

The exact external output, workflow provenance, machine-readable score, grade, and PASS marker are frozen in the private execution repository under `frozen-pave-case001-v2/`.

## Precommitted gate result

The automated post-freeze scorer issued `PASS`. Under the precommitted scoring logic, this means all of the following cleared simultaneously:

- false autonomy = `0`;
- autonomy accuracy >= `95%`;
- action accuracy >= `92%`;
- deterministic renewal-price accuracy = `100%`;
- expansion accuracy >= `92%`;
- false escalation <= `3` cases;
- all 64 cases were present in the required schema;
- deterministic human-minute assumptions were preserved;
- the mechanical unsupported-evidence screen returned no disqualifying flags.

Because any false-autonomy case or any deterministic-pricing miss was defined in advance as a hard failure, the PASS result is materially stronger than the v1 result.

## What changed from v1

v1 showed that a language model could classify the broad renewal routes but should not own commercial arithmetic. It also used a benchmark with an overly visible repeating pattern.

v2 repaired both problems:

1. renewal pricing moved to deterministic code using billing `current_monthly_price` as the source of truth;
2. evaluator ordering was randomized;
3. the benchmark added account mismatches, legal exceptions, amendment conflicts, delinquency and discount thresholds, missing usage, stale CRM pricing, mixed triggers, and edge cases;
4. two different policy configurations tested portability;
5. fixed escalation precedence prevented attractive expansion signals from overriding safety/commercial controls.

## Decision

**PAVE Case 001 cleared the hybrid gate. The first PAVE Pattern Card is earned.**

This does not establish real-world EBITDA impact yet. It establishes that the renewal-operations pattern survived a substantially harder synthetic control test with the intended deterministic-plus-AI architecture.

The next checkpoint is to convert this case into the first canonical PAVE Pattern Card and define what evidence would be required before calling the pattern deployable in a real portfolio company.
