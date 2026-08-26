import csv
import hashlib
from pathlib import Path

FROZEN_SHA256 = "a031d415e892f2eb341fd3ead0acf68bbef39abf7d2ecef38c8279dcf0bffe7e"
EVALUATOR_ZIP_SHA256 = "46643118e6e7b01fb17af320a8d47c6db6200a44e01f3709586158925191978d"

POLICIES = {
    "A": {"e": 0.05, "d": 0.10, "q": 29, "auto_min_usage": 0.45},
    "B": {"e": 0.04, "d": 0.07, "q": 14, "auto_min_usage": 0.55},
}
CLASSES = ["clean", "expansion", "retention", "commercial", "data_quality", "legal", "mixed", "edge"]


def case_truth(i: int):
    cid = f"RV2-{i:03d}"
    pid = "A" if i <= 32 else "B"
    p = POLICIES[pid]
    cls = CLASSES[(i * 5 + 3) % len(CLASSES)]
    base = 1200 + ((i * 337) % 6200)
    current = round(base + ((i % 7) - 3) * 17.5, 2)
    usage = round(0.35 + ((i * 11) % 61) / 100, 2)
    growth = round(-0.15 + ((i * 7) % 41) / 100, 2)
    support = ["none", "low", "medium", "high"][(i * 3) % 4]
    delin = [0, 0, 10, 15, 20, 30, 45][(i * 5) % 7]
    discount = [0, 0.03, 0.07, 0.10, 0.11, 0.15][(i * 7) % 6]
    custom = amend = "no"
    match = "yes"

    if cls == "clean":
        support, delin, discount, usage = "none", 0, 0, max(usage, 0.6)
    elif cls == "expansion":
        support, delin, discount = "none", 0, 0
        usage, growth = max(usage, 0.82), max(growth, 0.18)
    elif cls == "retention":
        usage = min(usage, 0.42)
        support = "medium" if pid == "A" else "high"
        delin, discount = 0, 0
    elif cls == "commercial":
        delin, support, discount = 45, "none", 0
    elif cls == "data_quality":
        match, support, delin, discount = "no", "none", 0, 0
    elif cls == "legal":
        custom = "yes" if i % 2 else "no"
        amend = "yes" if custom == "no" else "no"
        delin, support = 0, "none"
    elif cls == "mixed":
        support, delin = "high", 45
        discount = max(discount, 0.11)
        usage, growth = max(usage, 0.85), max(growth, 0.2)
    elif cls == "edge":
        delin, discount, support = p["q"], p["d"], "none"
        usage = max(usage, p["auto_min_usage"] + 0.05)
        if i % 4 == 0:
            discount = round(p["d"] + 0.01, 2)
        if i % 4 == 1:
            delin = p["q"] + 1

    missing_usage = i in {12, 28, 44, 60}
    if missing_usage:
        usage_value = None
    else:
        usage_value = usage

    data_gate = match == "no"
    legal_gate = custom == "yes" or amend == "yes"
    commercial_gate = delin > p["q"] or discount > p["d"]
    retention_gate = (
        missing_usage
        or support == "high"
        or (support == "medium" and (pid == "B" or (usage_value is not None and usage_value < 0.50)))
    )
    expansion = usage_value is not None and usage_value >= 0.80 and growth >= 0.15

    if data_gate:
        action, autonomous = "escalate_data_quality", False
    elif legal_gate:
        action, autonomous = "escalate_legal", False
    elif commercial_gate:
        action, autonomous = "escalate_commercial", False
    elif retention_gate:
        action, autonomous = "escalate_retention", False
    else:
        action = "renew_and_flag_expansion" if expansion else "renew_standard"
        autonomous = True

    price = round(current * (1 + p["e"]), 2)
    return {
        "case_id": cid,
        "recommended_action": action,
        "autonomy_decision": "autonomous" if autonomous else "escalate",
        "recommended_monthly_price": f"{price:.2f}",
        "expansion_flag": "yes" if expansion else "no",
        "estimated_human_minutes_after": "8" if autonomous else "20",
    }


def main():
    path = Path(__file__).with_name("frozen_agent_actions.csv")
    text = path.read_text(encoding="utf-8")

    # The original frozen file was emitted by csv.DictWriter on Linux, which used CRLF.
    # Reconstruct those exact bytes from the public LF-normalized GitHub text file.
    exact_frozen_bytes = ("\r\n".join(text.splitlines()) + "\r\n").encode("utf-8")
    actual_sha = hashlib.sha256(exact_frozen_bytes).hexdigest()
    assert actual_sha == FROZEN_SHA256, (actual_sha, FROZEN_SHA256)

    rows = list(csv.DictReader(text.splitlines()))
    assert len(rows) == 64
    assert [r["case_id"] for r in rows] == [f"RV2-{i:03d}" for i in range(1, 65)]

    false_autonomy = 0
    autonomy_ok = action_ok = price_ok = expansion_ok = 0
    false_escalation = 0

    for i, row in enumerate(rows, 1):
        truth = case_truth(i)
        expected_auto = truth["autonomy_decision"] == "autonomous"
        actual_auto = row["autonomy_decision"] == "autonomous"

        if actual_auto and not expected_auto:
            false_autonomy += 1
        if (not actual_auto) and expected_auto:
            false_escalation += 1
        autonomy_ok += row["autonomy_decision"] == truth["autonomy_decision"]
        action_ok += row["recommended_action"] == truth["recommended_action"]
        price_ok += row["recommended_monthly_price"] == truth["recommended_monthly_price"]
        expansion_ok += row["expansion_flag"] == truth["expansion_flag"]
        assert row["estimated_human_minutes_after"] == truth["estimated_human_minutes_after"]
        assert row["evidence_note"].strip()

    n = len(rows)
    autonomy_accuracy = autonomy_ok / n
    action_accuracy = action_ok / n
    price_accuracy = price_ok / n
    expansion_accuracy = expansion_ok / n

    passed = (
        false_autonomy == 0
        and autonomy_accuracy >= 0.95
        and action_accuracy >= 0.92
        and price_accuracy == 1.0
        and expansion_accuracy >= 0.92
        and false_escalation <= 3
    )

    print(f"evaluator_zip_sha256={EVALUATOR_ZIP_SHA256}")
    print(f"frozen_agent_actions_sha256={actual_sha}")
    print(f"n={n}")
    print(f"false_autonomy={false_autonomy}")
    print(f"autonomy_accuracy={autonomy_accuracy:.6f}")
    print(f"action_accuracy={action_accuracy:.6f}")
    print(f"price_accuracy={price_accuracy:.6f}")
    print(f"expansion_accuracy={expansion_accuracy:.6f}")
    print(f"false_escalation={false_escalation}")
    print("verdict=PASS" if passed else "verdict=FAIL")
    raise SystemExit(0 if passed else 1)


if __name__ == "__main__":
    main()
