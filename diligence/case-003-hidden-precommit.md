# Case 003 Hidden-Truth Precommitment

**Case:** Project Meridian / AI-Q Case 003  
**Hidden bundle version:** v1.0  
**Freeze date:** 2026-08-23  
**Status:** frozen before evaluator-facing data-room generation

The answer-bearing Case 003 builder truth has been stored outside the evaluator-facing public repository.

The hidden bundle defines:

- the true state of claims C1–C6;
- exact underlying synthetic values;
- the causal mechanism map;
- deterministic data-generation rules and RNG seeds;
- cost and human-review assumptions;
- customer-ROI data-generating assumptions;
- expected blind-evaluator discoveries;
- blind-run scoring expectations;
- rules forbidding post-hoc truth changes after the evaluator sees the case.

## SHA-256 precommitment

`356acbaddc7b8fcbcd9d2b50e85da8849d68f2dd09f9a3763be94c0a8dc70108`

This hash binds the canonical UTF-8 hidden specification used to generate the Case 003 v1.0 evaluator materials.

## Blind boundary

The hidden bundle must not be supplied to the AI-Q evaluator before the blind report is complete.

Any substantive answer-bearing change requires:

1. a new hidden-bundle version;
2. a new SHA-256 precommitment;
3. an explicit change log explaining why the previous frozen specification was superseded.

Bug fixes that do not alter the intended frozen truth may be made only if logged and shown to preserve the precommitted claim states and mechanisms.

The next step is to generate the evaluator-facing Project Meridian data room from the frozen hidden specification, then check for internal consistency and accidental answer leakage before the blind AI-Q run.
