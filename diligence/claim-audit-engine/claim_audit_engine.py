#!/usr/bin/env python3
"""Deterministic core for the Claim Audit Engine.

Ingest one JSON case specification, verify local artifact manifests, compare
reported and regenerated metrics without overwriting either state, and emit a
machine-readable audit bundle plus a concise decision memo.

No network calls. No LLM calls. Evidence-state promotion remains rule-based.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

EVIDENCE_STATES = {"reported", "reconstructed", "regenerated", "independently_verified", "unresolved"}
FAILURE_LAYERS = ["provenance", "environment", "data", "harness", "stochasticity", "comparator", "attribution", "substantive_result", "unresolved"]


@dataclass(frozen=True)
class ArtifactResult:
    name: str
    path: str
    role: str
    exists: bool
    sha256: Optional[str]
    expected_sha256: Optional[str]
    checksum_match: Optional[bool]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def finite_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(float(value))


def load_case(path: Path) -> Dict[str, Any]:
    data = json.loads(path.read_text())
    if not isinstance(data, dict):
        raise ValueError("case JSON must be a top-level object")
    state = data.get("evidence_state", "reported")
    if state not in EVIDENCE_STATES:
        raise ValueError(f"invalid evidence_state: {state}")
    return data


def verify_artifacts(case: Dict[str, Any], case_dir: Path) -> List[ArtifactResult]:
    results: List[ArtifactResult] = []
    for idx, artifact in enumerate(case.get("artifacts", []), start=1):
        if not isinstance(artifact, dict):
            raise ValueError(f"artifact #{idx} must be an object")
        rel = str(artifact.get("path", ""))
        local = case_dir / rel if rel else None
        exists = bool(local and local.exists() and local.is_file())
        observed = sha256_file(local) if exists and local else None
        expected = artifact.get("sha256")
        match = None if expected is None or observed is None else observed.lower() == str(expected).lower()
        results.append(
            ArtifactResult(
                name=str(artifact.get("name") or (Path(rel).name if rel else f"artifact-{idx}")),
                path=rel,
                role=str(artifact.get("role", "evidence")),
                exists=exists,
                sha256=observed,
                expected_sha256=expected,
                checksum_match=match,
            )
        )
    return results


def compare_status(reported: Any, regenerated: Any, tolerance: Any) -> str:
    if not finite_number(reported) or not finite_number(regenerated):
        return "not_comparable"
    if finite_number(tolerance):
        return "within_tolerance" if abs(float(regenerated) - float(reported)) <= float(tolerance) else "outside_tolerance"
    return "observed"


def metric_comparisons(case: Dict[str, Any]) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for idx, metric in enumerate(case.get("metrics", []), start=1):
        if not isinstance(metric, dict):
            raise ValueError(f"metric #{idx} must be an object")
        reported = metric.get("reported")
        regenerated = metric.get("regenerated")
        delta = None
        relative_delta = None
        if finite_number(reported) and finite_number(regenerated):
            delta = float(regenerated) - float(reported)
            if float(reported) != 0:
                relative_delta = delta / abs(float(reported))
        rows.append({
            "name": metric.get("name", f"metric-{idx}"),
            "unit": metric.get("unit"),
            "reported": reported,
            "regenerated": regenerated,
            "delta": delta,
            "relative_delta": relative_delta,
            "tolerance": metric.get("tolerance"),
            "status": compare_status(reported, regenerated, metric.get("tolerance")),
        })
    return rows


def evidence_gate(case: Dict[str, Any], artifacts: Iterable[ArtifactResult]) -> Dict[str, Any]:
    state = case.get("evidence_state", "reported")
    provenance = case.get("provenance", {}) if isinstance(case.get("provenance", {}), dict) else {}
    artifacts = list(artifacts)
    artifact_exists = any(a.exists for a in artifacts)
    checksum_ok = all(a.checksum_match is not False for a in artifacts)

    requirements = {
        "reported": True,
        "reconstructed": artifact_exists or bool(provenance.get("source_artifacts")),
        "regenerated": all([
            bool(provenance.get("command")),
            bool(provenance.get("environment")),
            provenance.get("observed_result") is not None,
            checksum_ok,
        ]),
        "independently_verified": all([
            bool(provenance.get("command")),
            bool(provenance.get("environment")),
            provenance.get("observed_result") is not None,
            bool(provenance.get("independent_execution")),
            bool(provenance.get("external_receipt")),
            checksum_ok,
        ]),
        "unresolved": True,
    }

    return {
        "requested_state": state,
        "promotion_allowed": bool(requirements[state]),
        "requirements": requirements,
        "artifact_count": len(artifacts),
        "artifact_exists": artifact_exists,
        "all_expected_checksums_match": checksum_ok,
        "external_receipt_present": bool(provenance.get("external_receipt")),
        "independent_execution_present": bool(provenance.get("independent_execution")),
    }


def validate_tests(case: Dict[str, Any]) -> List[Dict[str, Any]]:
    tests: List[Dict[str, Any]] = []
    for idx, test in enumerate(case.get("tests", []), start=1):
        if not isinstance(test, dict):
            raise ValueError(f"test #{idx} must be an object")
        layer = test.get("failure_layer", "unresolved")
        if layer not in FAILURE_LAYERS:
            raise ValueError(f"invalid failure_layer in test #{idx}: {layer}")
        tests.append({
            "id": test.get("id", f"T{idx:02d}"),
            "hypothesis": test.get("hypothesis"),
            "intervention": test.get("intervention"),
            "expected_if_true": test.get("expected_if_true"),
            "expected_if_false": test.get("expected_if_false"),
            "observed": test.get("observed"),
            "result": test.get("result", "pending"),
            "failure_layer": layer,
            "decision_value": test.get("decision_value"),
        })
    return tests


def localize_failure(tests: List[Dict[str, Any]]) -> Dict[str, Any]:
    open_tests = [t for t in tests if t.get("result") in {"failed", "refuted", "discrepant", "pending", "unresolved"}]
    earliest = next((layer for layer in FAILURE_LAYERS if any(t.get("failure_layer") == layer for t in open_tests)), None)
    return {
        "earliest_open_or_failed_layer": earliest,
        "failed_or_refuted_tests": [t["id"] for t in tests if t.get("result") in {"failed", "refuted", "discrepant"}],
        "pending_or_unresolved_tests": [t["id"] for t in tests if t.get("result") in {"pending", "unresolved"}],
    }


def write_bundle(case: Dict[str, Any], case_path: Path, outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    artifacts = verify_artifacts(case, case_path.parent)
    metrics = metric_comparisons(case)
    gate = evidence_gate(case, artifacts)
    tests = validate_tests(case)
    failure = localize_failure(tests)

    bundle = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "case_id": case.get("case_id"),
        "claim": case.get("claim"),
        "decision_relevance": case.get("decision_relevance"),
        "evidence_gate": gate,
        "artifacts": [asdict(a) for a in artifacts],
        "metrics": metrics,
        "tests": tests,
        "failure_localization": failure,
        "limitations": case.get("limitations", []),
        "open_questions": case.get("open_questions", []),
    }
    (outdir / "audit_bundle.json").write_text(json.dumps(bundle, indent=2))

    lines = [
        f"# Claim Audit — {case.get('case_id', 'unnamed')}", "",
        "## Frozen claim", str(case.get("claim", "")), "",
        "## Decision relevance", str(case.get("decision_relevance", "")), "",
        "## Evidence state", f"Requested: **{gate['requested_state']}**", f"Promotion gate: **{'PASS' if gate['promotion_allowed'] else 'BLOCKED'}**", "",
        "## Metric comparison",
    ]
    if metrics:
        lines += ["| Metric | Reported | Regenerated | Delta | Status |", "|---|---:|---:|---:|---|"]
        for m in metrics:
            lines.append(f"| {m['name']} | {m['reported']} | {m['regenerated']} | {m['delta']} | {m['status']} |")
    else:
        lines.append("No metric pairs supplied.")

    lines += ["", "## Artifact verification"]
    if artifacts:
        for a in artifacts:
            state = "missing" if not a.exists else ("checksum mismatch" if a.checksum_match is False else "present")
            lines.append(f"- **{a.name}** — {state}; sha256={a.sha256 or 'n/a'}")
    else:
        lines.append("No local artifacts supplied.")

    lines += ["", "## Failure localization", f"Earliest open/failed layer: **{failure['earliest_open_or_failed_layer'] or 'none'}**", "", "## Integrity conclusion"]
    lines.append("The requested evidence state satisfies the deterministic promotion gate given the supplied record." if gate["promotion_allowed"] else "The requested evidence state is blocked. Do not upgrade the public claim until the missing prerequisites exist.")
    (outdir / "decision_memo.md").write_text("\n".join(lines) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a deterministic technical-claim audit bundle")
    parser.add_argument("case", type=Path, help="path to case JSON")
    parser.add_argument("--out", type=Path, default=Path("audit-output"))
    args = parser.parse_args()
    case = load_case(args.case)
    write_bundle(case, args.case, args.out)
    print(f"Wrote deterministic audit bundle to {args.out}")


if __name__ == "__main__":
    main()
