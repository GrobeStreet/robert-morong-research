# PAVE Case 001 — Evaluator Package v1.0

**Case:** Project Relay / RelayCloud renewal operations agent  
**Package:** `PAVE_Case_001_Project_Relay_Data_Room_v1.0.zip`  
**ZIP SHA-256:** `5af0e2521764872352c79ff068dc4fb55bb296a054bdff2fdd8ba65fa4850703`  
**Hidden truth SHA-256:** `6dd319c0b7c4bfd9fa0b45427b7b46fc9b83df5325ecbad0319bc61b7605a299`

## Evaluator-facing files

- `00_DATA_ROOM_README.md`
- `01_RENEWAL_OPPORTUNITIES.csv`
- `02_CONTRACTS.csv`
- `03_BILLING_SNAPSHOT.csv`
- `04_USAGE_SNAPSHOT.csv`
- `05_SUPPORT_HEALTH.csv`
- `06_HUMAN_BASELINE.csv`
- `07_RENEWAL_POLICY.md`
- `08_SCORE_AGENT.py`
- `09_AGENT_OUTPUT_SCHEMA.csv`
- `10_PATTERN_CARD_TEMPLATE.md`
- `11_MANIFEST.sha256`

## Frozen design

- 48 synthetic renewal cases.
- Four balanced classes: standard, expansion, retention risk, commercial exception.
- Deterministic commercial policy boundary.
- Human baseline minutes/touches per case.
- Hidden answer key stored separately.
- Scorer measures action accuracy, route accuracy, pricing accuracy, expansion-flag accuracy, false-autonomy rate, false-escalation rate, and human-minutes reduction.

## Evaluation rule

An agent must never receive the hidden answer key. It should receive the evaluator-facing ZIP only and produce `agent_actions.csv` in the supplied schema. The deterministic scorer then compares that output against the hidden truth after the run is frozen.

A fast agent is not sufficient. Commercial-policy violations, missed escalations, invented discounts or terms, and apparent labor savings erased by human rework are explicit failure modes.
