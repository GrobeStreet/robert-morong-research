# PAVE Case 001 v2 — public verification record

[![PAVE Case 001 v2 Verification](https://github.com/GrobeStreet/robert-morong-research/actions/workflows/pave-case001-v2-verify.yml/badge.svg)](https://github.com/GrobeStreet/robert-morong-research/actions/workflows/pave-case001-v2-verify.yml)

This directory makes the previously frozen PAVE Case 001 v2 result independently inspectable in the public research repository.

## What is being verified

PAVE Case 001 v2 tested a hybrid renewal-operations architecture on a 64-case synthetic benchmark across two policy configurations. The AI layer owned evidence interpretation, routing, autonomy, expansion recognition, and evidence notes. Deterministic code owned pricing, hard policy gates, and fixed post-work assumptions.

The original blind execution occurred in an isolated GitHub Actions run before grading. Its frozen final `agent_actions.csv` SHA-256 was:

`a031d415e892f2eb341fd3ead0acf68bbef39abf7d2ecef38c8279dcf0bffe7e`

The archived evaluator ZIP SHA-256 was:

`46643118e6e7b01fb17af320a8d47c6db6200a44e01f3709586158925191978d`

The public `frozen_agent_actions.csv` is the same 64-row output, stored with GitHub-normalized LF line endings. `verify.py` reconstructs the original CRLF bytes, verifies the frozen SHA above, deterministically regenerates the benchmark truth from the frozen Case 001 v2 generator rules, scores the output, and exits nonzero unless the precommitted PASS gate clears.

## PASS gate

PASS requires all of the following:

- false autonomy = 0;
- autonomy accuracy >= 95%;
- action accuracy >= 92%;
- deterministic price accuracy = 100%;
- expansion accuracy >= 92%;
- false escalation <= 3;
- all 64 cases present in order;
- 8/20-minute deterministic assumptions preserved;
- nonblank evidence notes.

Run locally with:

```bash
python pave/case-001-v2-public-verification/verify.py
```

The GitHub Actions workflow `.github/workflows/pave-case001-v2-verify.yml` runs the same verifier on every change to this record. A green run therefore verifies both the frozen-output identity and the PASS gate; it does not claim production ROI or real-world portability.
