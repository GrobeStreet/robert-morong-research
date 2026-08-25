#!/usr/bin/env python3
"""Claim Audit Engine: deterministic verification core.

Never execute commands supplied by a case file. Verify local artifacts, compare
reported and regenerated metrics, verify an optional git pin, and emit byte-
stable outputs. Evidence-state promotion is rule-based.
"""
from __future__ import annotations

import argparse, hashlib, json, math, subprocess
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

EVIDENCE_STATES = {"reported", "reconstructed", "regenerated", "independently_verified", "unresolved"}
FAILURE_LAYERS = ["provenance", "environment", "data", "harness", "stochasticity", "comparator", "attribution", "substantive_result", "unresolved"]

@dataclass(frozen=True)
class ArtifactResult:
    name: str; path: str; role: str; exists: bool
    sha256: Optional[str]; expected_sha256: Optional[str]; checksum_match: Optional[bool]

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""): h.update(chunk)
    return h.hexdigest()

def canonical_bytes(obj: Any) -> bytes:
    return (json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n").encode()

def finite(v: Any) -> bool:
    return isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(float(v))

def load_case(path: Path) -> Dict[str, Any]:
    data = json.loads(path.read_text())
    if not isinstance(data, dict): raise ValueError("case JSON must be an object")
    if data.get("evidence_state", "reported") not in EVIDENCE_STATES: raise ValueError("invalid evidence_state")
    return data

def verify_artifacts(case: Dict[str, Any], root: Path) -> List[ArtifactResult]:
    root = root.resolve(); out = []
    for i, a in enumerate(case.get("artifacts", []), 1):
        rel = str(a.get("path", "")).strip(); p = (root / rel).resolve() if rel else None
        if p:
            try: p.relative_to(root)
            except ValueError as exc: raise ValueError(f"artifact path escapes root: {rel}") from exc
        exists = bool(p and p.is_file()); observed = sha256_file(p) if exists else None; expected = a.get("sha256")
        match = None if observed is None or expected is None else observed.lower() == str(expected).lower()
        out.append(ArtifactResult(str(a.get("name") or (Path(rel).name if rel else f"artifact-{i}")), rel, str(a.get("role", "evidence")), exists, observed, str(expected) if expected else None, match))
    return out

def metric_rows(case: Dict[str, Any]) -> List[Dict[str, Any]]:
    rows=[]
    for i,m in enumerate(case.get("metrics", []),1):
        r,g,t=m.get("reported"),m.get("regenerated"),m.get("tolerance"); d=float(g)-float(r) if finite(r) and finite(g) else None
        status="not_comparable"
        if finite(r) and finite(g): status="missing_tolerance" if not finite(t) else ("within_tolerance" if abs(d)<=float(t) else "outside_tolerance")
        rows.append({"name":m.get("name",f"metric-{i}"),"unit":m.get("unit"),"reported":r,"regenerated":g,"delta":d,"tolerance":t,"status":status})
    return rows

def repo_head(repo: Optional[Path]) -> Optional[str]:
    if repo is None: return None
    try: return subprocess.run(["git","-C",str(repo),"rev-parse","HEAD"],capture_output=True,text=True,check=True,timeout=10).stdout.strip()
    except Exception: return None

def pin_match(claimed: Any, actual: Optional[str]) -> Optional[bool]:
    if not claimed or not actual: return None
    c,a=str(claimed).lower(),actual.lower(); return a.startswith(c) or c.startswith(a)

def evidence_gate(case: Dict[str,Any], artifacts: Iterable[ArtifactResult], metrics: List[Dict[str,Any]], head: Optional[str]) -> Dict[str,Any]:
    state=case.get("evidence_state","reported"); p=case.get("provenance",{}) if isinstance(case.get("provenance",{}),dict) else {}; arts=list(artifacts)
    declared=bool(arts); present=declared and all(a.exists for a in arts); hashed=declared and all(a.expected_sha256 for a in arts); checks=declared and all(a.checksum_match is True for a in arts)
    mdecl=bool(metrics); mnumeric=mdecl and all(finite(m["reported"]) and finite(m["regenerated"]) for m in metrics); mtol=mdecl and all(finite(m["tolerance"]) for m in metrics); mmatch=mdecl and all(m["status"]=="within_tolerance" for m in metrics)
    claimed=p.get("git_pin"); pm=pin_match(claimed,head); pin_ok=(not claimed) or pm is True
    regen=all([p.get("command"),p.get("environment"),present,hashed,checks,mnumeric,mtol,mmatch,pin_ok])
    req={"reported":True,"reconstructed":present and checks,"regenerated":regen,"independently_verified":regen and bool(p.get("independent_execution")) and bool(p.get("external_receipt")),"unresolved":True}
    b=[]
    if state in {"reconstructed","regenerated","independently_verified"}:
        if not declared:b.append("no_artifacts_declared")
        elif not present:b.append("missing_artifact")
        elif not hashed:b.append("missing_expected_sha256")
        elif not checks:b.append("checksum_mismatch")
    if state in {"regenerated","independently_verified"}:
        if not mdecl:b.append("no_reported_vs_regenerated_metrics")
        elif not mnumeric:b.append("non_numeric_metric_assertion")
        elif not mtol:b.append("missing_metric_tolerance")
        elif not mmatch:b.append("reported_regenerated_mismatch")
        if not p.get("command"):b.append("missing_command_record")
        if not p.get("environment"):b.append("missing_environment_record")
        if claimed and head is None:b.append("git_head_unavailable")
        elif claimed and pm is not True:b.append("git_pin_mismatch")
    if state=="independently_verified":
        if not p.get("independent_execution"):b.append("missing_independent_execution")
        if not p.get("external_receipt"):b.append("missing_external_receipt")
    return {"requested_state":state,"promotion_allowed":bool(req[state]),"requirements":req,"blockers":b,"artifact_count":len(arts),"all_artifacts_present":present,"all_expected_checksums_match":checks,"metrics_match":mmatch,"claimed_git_pin":claimed,"actual_repo_head":head,"git_pin_match":pm,"external_receipt_present":bool(p.get("external_receipt")),"independent_execution_present":bool(p.get("independent_execution"))}

def validate_tests(case: Dict[str,Any]) -> List[Dict[str,Any]]:
    out=[]
    for i,t in enumerate(case.get("tests",[]),1):
        layer=t.get("failure_layer","unresolved")
        if layer not in FAILURE_LAYERS: raise ValueError(f"invalid failure_layer: {layer}")
        out.append({"id":t.get("id",f"T{i:02d}"),"hypothesis":t.get("hypothesis"),"intervention":t.get("intervention"),"observed":t.get("observed"),"result":t.get("result","pending"),"failure_layer":layer,"decision_value":t.get("decision_value")})
    return out

def localize(tests: List[Dict[str,Any]], gate: Dict[str,Any]) -> Dict[str,Any]:
    bm={"git_pin_mismatch":"provenance","git_head_unavailable":"provenance","missing_artifact":"provenance","checksum_mismatch":"provenance","missing_expected_sha256":"provenance","no_artifacts_declared":"provenance","missing_command_record":"provenance","missing_environment_record":"environment","reported_regenerated_mismatch":"substantive_result","non_numeric_metric_assertion":"substantive_result","no_reported_vs_regenerated_metrics":"substantive_result"}
    layers=[bm[x] for x in gate.get("blockers",[]) if x in bm]+[t["failure_layer"] for t in tests if t.get("result") in {"failed","refuted","discrepant","pending","unresolved"}]
    earliest=next((x for x in FAILURE_LAYERS if x in layers),None)
    return {"earliest_open_or_failed_layer":earliest,"failed_or_refuted_tests":[t["id"] for t in tests if t.get("result") in {"failed","refuted","discrepant"}],"pending_or_unresolved_tests":[t["id"] for t in tests if t.get("result") in {"pending","unresolved"}]}

def write_bundle(case: Dict[str,Any], outdir: Path, artifacts_root: Path, repo: Optional[Path]) -> None:
    outdir.mkdir(parents=True,exist_ok=True); arts=verify_artifacts(case,artifacts_root); metrics=metric_rows(case); head=repo_head(repo); gate=evidence_gate(case,arts,metrics,head); tests=validate_tests(case); failure=localize(tests,gate)
    payload={"case_id":case.get("case_id"),"claim":case.get("claim"),"decision_relevance":case.get("decision_relevance"),"evidence_gate":gate,"artifacts":[asdict(a) for a in arts],"metrics":metrics,"tests":tests,"failure_localization":failure,"limitations":case.get("limitations",[]),"open_questions":case.get("open_questions",[])}
    pack_hash=hashlib.sha256(canonical_bytes(payload)).hexdigest(); bundle={**payload,"audit_pack_hash":pack_hash}
    (outdir/"audit_bundle.json").write_bytes(canonical_bytes(bundle)); (outdir/"audit_pack_hash.txt").write_text(pack_hash+"\n")
    lines=[f"# Claim Audit — {case.get('case_id','unnamed')}","",f"Promotion gate: **{'PASS' if gate['promotion_allowed'] else 'BLOCKED'}**","","## Blockers"]+([f"- `{x}`" for x in gate["blockers"]] or ["- none"])+["","## Audit pack hash",f"`{pack_hash}`",""]
    (outdir/"decision_memo.md").write_text("\n".join(lines))

def main() -> None:
    ap=argparse.ArgumentParser(); ap.add_argument("case",type=Path); ap.add_argument("--out",type=Path,default=Path("audit-output")); ap.add_argument("--artifacts-root",type=Path,default=Path(".")); ap.add_argument("--repo",type=Path,default=None); args=ap.parse_args()
    write_bundle(load_case(args.case),args.out,args.artifacts_root,args.repo); print(f"Wrote deterministic audit bundle to {args.out}")

if __name__=="__main__": main()
