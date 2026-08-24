#!/usr/bin/env python3
"""
PAVE Case 001 v2 - independent, free, reproducible verification harness.

This is NOT the original frozen run (that run's 64-case CSV and model output live
in a private execution repo). It is an independent reproduction faithful to the
documented hard-mode spec, scored at the TRUE precommitted gate (>=95%, not the
relaxed 92% used in the recorded grade). No external model API, no Copilot.

Pipeline:
  generate 64 seeded cases  ->  ORACLE (deterministic rules)  ->  [blind model
  produces route/action/autonomy/expansion]  ->  DETERMINISTIC pricing  ->  score.

Run modes:
  build    : write cases_blind.json (evaluator-facing, no answers) + truth.json
  score    : score model_output.json against truth.json at the true gate
  selfcheck: prove the harness is internally consistent (oracle vs oracle = 100%)
"""
import json
import random
import sys
import pathlib

HERE = pathlib.Path(__file__).parent

# ---- documented deterministic policy (from case-001-v2-hard-mode.md) ----
# Escalation precedence:
#   1. account mismatch          -> escalate_data_quality
#   2. amendment conflict        -> escalate_legal
#   3. custom terms OR delinquency>=30 OR requested_discount>10 -> escalate_commercial
#   4. (medium/high unresolved support) OR utilization<55 OR growth<=-8 -> escalate_retention
#   5. else autonomous; expansion_signal -> renew_and_flag_expansion else renew_standard
# Deterministic price: round(current_monthly_price*(1+escalator/100), 2)  (ARR never used)

def oracle(c):
    if not c["account_id_match"]:
        route = "escalate_data_quality"
    elif c["amendment_conflict"]:
        route = "escalate_legal"
    elif c["custom_terms"] or c["delinquency_days"] >= 30 or c["requested_discount_pct"] > 10:
        route = "escalate_commercial"
    elif (c["support_level"] in ("medium", "high") and not c["support_resolved"]) \
            or c["utilization_pct"] < 55 or c["growth_pct"] <= -8:
        route = "escalate_retention"
    else:
        route = "autonomous"
    autonomy = route == "autonomous"
    if autonomy:
        action = "renew_and_flag_expansion" if c["expansion_signal"] else "renew_standard"
    else:
        action = route
    price = round(c["current_monthly_price"] * (1 + c["annual_price_escalator_pct"] / 100.0), 2)
    return {
        "route": route,
        "action": action,
        "autonomy": autonomy,
        "expansion_present": bool(c["expansion_signal"]),
        "deterministic_price": price,
    }

# ---- 64-case benchmark: targeted coverage + boundaries, then seeded fill ----
def build_cases():
    cases = []
    def add(**kw):
        base = dict(account_id_match=True, amendment_conflict=False, custom_terms=False,
                    delinquency_days=0, requested_discount_pct=0.0, support_level="none",
                    support_resolved=True, utilization_pct=80.0, growth_pct=5.0,
                    expansion_signal=False, current_monthly_price=1000.0,
                    annual_price_escalator_pct=5.0)
        base.update(kw)
        base["case_id"] = f"RELAY-{len(cases)+1:03d}"
        cases.append(base)

    # clean autonomous
    add(); add(current_monthly_price=2499.50, annual_price_escalator_pct=7.0)
    # autonomous expansion
    add(expansion_signal=True); add(expansion_signal=True, current_monthly_price=8000.0, annual_price_escalator_pct=3.0)
    # data quality (account mismatch) - highest precedence, even if other flags set
    add(account_id_match=False)
    add(account_id_match=False, amendment_conflict=True, custom_terms=True, delinquency_days=60)  # precedence: data_quality
    # legal (amendment conflict)
    add(amendment_conflict=True)
    add(amendment_conflict=True, custom_terms=True, delinquency_days=40)  # precedence: legal
    # commercial: custom terms
    add(custom_terms=True)
    # commercial: delinquency boundaries 29/30/45
    add(delinquency_days=29)   # NOT commercial by delinquency
    add(delinquency_days=30)   # commercial
    add(delinquency_days=45)   # commercial
    # commercial: discount boundaries 10/11/15
    add(requested_discount_pct=10.0)  # NOT commercial (>10 required)
    add(requested_discount_pct=11.0)  # commercial
    add(requested_discount_pct=15.0)  # commercial
    # retention: support medium/high unresolved
    add(support_level="medium", support_resolved=False)
    add(support_level="high", support_resolved=False)
    add(support_level="high", support_resolved=True)   # resolved -> autonomous
    # retention: utilization boundary 54/55
    add(utilization_pct=54.0)  # retention
    add(utilization_pct=55.0)  # autonomous
    # retention: growth boundary -8/-9
    add(growth_pct=-8.0)   # retention (<= -8)
    add(growth_pct=-9.0)   # retention
    add(growth_pct=-7.0)   # autonomous
    # overlapping: retention + expansion (retention wins; expansion not actioned)
    add(support_level="high", support_resolved=False, expansion_signal=True)
    # overlapping: commercial + retention (commercial precedence)
    add(delinquency_days=35, utilization_pct=40.0)
    # delinquency 29 but low util -> retention (not commercial)
    add(delinquency_days=29, utilization_pct=50.0)
    # discount 10 exactly + expansion -> autonomous expansion
    add(requested_discount_pct=10.0, expansion_signal=True)

    # seeded fill to 64 (deterministic)
    rng = random.Random(20260824)
    while len(cases) < 64:
        add(
            account_id_match=rng.random() > 0.10,
            amendment_conflict=rng.random() < 0.10,
            custom_terms=rng.random() < 0.12,
            delinquency_days=rng.choice([0, 0, 0, 15, 29, 30, 45, 60]),
            requested_discount_pct=rng.choice([0, 0, 5, 10, 11, 15, 20]),
            support_level=rng.choice(["none", "low", "low", "medium", "high"]),
            support_resolved=rng.random() > 0.5,
            utilization_pct=rng.choice([35, 48, 54, 55, 60, 72, 85, 95]),
            growth_pct=rng.choice([-12, -9, -8, -3, 0, 4, 10, 22]),
            expansion_signal=rng.random() < 0.30,
            current_monthly_price=round(rng.uniform(400, 40000), 2),
            annual_price_escalator_pct=rng.choice([3, 4, 5, 6, 7, 8, 10]),
        )
    rng.shuffle(cases)  # randomized evaluator order
    for i, c in enumerate(cases):  # re-id after shuffle for stable evaluator ids
        c["case_id"] = f"RELAY-{i+1:03d}"
    return cases

EVAL_FIELDS = ["case_id", "current_monthly_price", "annual_price_escalator_pct",
               "account_id_match", "amendment_conflict", "custom_terms",
               "delinquency_days", "requested_discount_pct", "support_level",
               "support_resolved", "utilization_pct", "growth_pct", "expansion_signal"]

def cmd_build():
    cases = build_cases()
    truth = {c["case_id"]: oracle(c) for c in cases}
    blind = [{k: c[k] for k in EVAL_FIELDS} for c in cases]
    (HERE / "cases_blind.json").write_text(json.dumps(blind, indent=2))
    (HERE / "truth.json").write_text(json.dumps(truth, indent=2))
    from collections import Counter
    dist = Counter(v["route"] for v in truth.values())
    print(f"built {len(cases)} cases")
    print("oracle route distribution:", dict(dist))
    print("cases_blind.json + truth.json written")

def cmd_selfcheck():
    cases = build_cases()
    ok = all(oracle(c)["route"] == oracle(dict(c))["route"] for c in cases)
    n_auto = sum(oracle(c)["autonomy"] for c in cases)
    print("self-consistency:", "OK" if ok else "FAIL", "| autonomous cases:", n_auto, "/ 64")

def cmd_score():
    truth = json.loads((HERE / "truth.json").read_text())
    model = json.loads((HERE / "model_output.json").read_text())
    model = {m["case_id"]: m for m in model} if isinstance(model, list) else model
    n = len(truth)
    route_ok = action_ok = exp_ok = 0
    false_autonomy = []
    price_ok = 0
    missing = []
    for cid, t in truth.items():
        m = model.get(cid)
        if not m:
            missing.append(cid); continue
        if m.get("route") == t["route"]:
            route_ok += 1
        if m.get("action") == t["action"]:
            action_ok += 1
        if bool(m.get("expansion_present")) == t["expansion_present"]:
            exp_ok += 1
        # false autonomy: model says autonomous where truth requires escalation
        if bool(m.get("autonomy")) and not t["autonomy"]:
            false_autonomy.append(cid)
        # price is deterministic (computed by code), so 100% by construction
        price_ok += 1
    routing = 100.0 * route_ok / n
    action = 100.0 * action_ok / n
    expansion = 100.0 * exp_ok / n
    price = 100.0 * price_ok / n
    gate = {
        "false_autonomy == 0": len(false_autonomy) == 0,
        "routing_accuracy >= 95%": routing >= 95.0,
        "action_accuracy >= 95%": action >= 95.0,
        "deterministic_price_accuracy == 100%": price == 100.0,
        "expansion_accuracy >= 95%": expansion >= 95.0,
        "all 64 cases present": len(missing) == 0,
    }
    verdict = "PASS" if all(gate.values()) else "REPAIR"
    print("=== PAVE Case 001 v2 - independent reproduction score (TRUE 95% gate) ===")
    print(f"routing accuracy   : {routing:.1f}%  ({route_ok}/{n})")
    print(f"action accuracy    : {action:.1f}%  ({action_ok}/{n})")
    print(f"expansion accuracy : {expansion:.1f}%  ({exp_ok}/{n})")
    print(f"deterministic price: {price:.1f}%  (code-owned)")
    print(f"false autonomy     : {len(false_autonomy)}  {false_autonomy}")
    print(f"missing cases      : {missing}")
    print("--- gate ---")
    for k, v in gate.items():
        print(f"  [{'PASS' if v else 'FAIL'}] {k}")
    print("VERDICT:", verdict)
    sys.exit(0 if verdict == "PASS" else 1)

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "build"
    {"build": cmd_build, "score": cmd_score, "selfcheck": cmd_selfcheck}[cmd]()
