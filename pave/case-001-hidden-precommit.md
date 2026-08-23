# PAVE Case 001 — Hidden Truth Precommit

**Case:** Project Relay / RelayCloud renewal operations agent  
**Hidden builder truth SHA-256:** `6dd319c0b7c4bfd9fa0b45427b7b46fc9b83df5325ecbad0319bc61b7605a299`  
**Frozen evaluator ZIP SHA-256:** `5af0e2521764872352c79ff068dc4fb55bb296a054bdff2fdd8ba65fa4850703`

The hidden builder truth is stored separately from the evaluator-facing data room and must not be supplied to any agent under test.

The evaluator-facing package contains only synthetic, non-sensitive data and the deterministic scorer. The hidden answer key fixes the correct action, autonomy decision, policy-sensitive price, expansion flag, and required escalation route for each of 48 synthetic renewal cases before any agent evaluation.

Any subsequent agent run must use the frozen evaluator package unchanged unless a new version is explicitly created and re-precommitted.
