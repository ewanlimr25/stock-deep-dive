#!/usr/bin/env python3
"""Validate a trade-plan eval.json. Pure stdlib -- no pip installs.

Enforces structure + cross-field semantics:
  - status / verdict enums valid
  - a finalized reasoning grade is not claimed on an OPEN trade
  - brier matches (conviction - outcome_bit)^2 for resolved trades
  - lesson ids look like L-####; ACTIVE lessons cite a scope
  - >= 1 reasoning component graded

Usage:
    python3 validate_eval.py --file trade-plans/NVDA/2026-06-18/eval-2026-07-10.json
Exit 0 = valid, 1 = invalid.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

OUTCOME = {"WIN", "LOSS", "OPEN", "INCONCLUSIVE"}
RGRADE = {"RIGHT", "WRONG", "UNRESOLVED"}
CONV = (0.55, 0.65, 0.75, 0.85, 0.95)
LID = re.compile(r"^L-\d{4}$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

REQUIRED_TOP = [
    "ticker", "plan_date", "review_date", "generated", "plan_path",
    "trade_taken", "outcome", "reasoning_review", "calibration",
    "attribution", "lessons", "disclaimer",
]


def validate(d: dict) -> list[str]:
    errs: list[str] = []
    for k in REQUIRED_TOP:
        if k not in d:
            errs.append(f"missing required field: {k}")
    if errs:
        return errs

    for f in ("plan_date", "review_date"):
        if not DATE_RE.match(str(d[f])):
            errs.append(f"{f} must be YYYY-MM-DD")

    out = d["outcome"]
    status = out.get("status")
    if status not in OUTCOME:
        errs.append(f"outcome.status must be one of {sorted(OUTCOME)}")

    rr = d["reasoning_review"]
    if rr.get("direction_call") not in (RGRADE | {None}):
        errs.append("reasoning_review.direction_call invalid")
    comps = rr.get("components")
    if not isinstance(comps, list) or len(comps) < 1:
        errs.append("reasoning_review.components must list >= 1 graded claim")
    else:
        for i, c in enumerate(comps):
            if c.get("verdict") not in RGRADE:
                errs.append(f"components[{i}].verdict invalid")
            if c.get("side") not in {"for", "against"}:
                errs.append(f"components[{i}].side must be for|against")

    # don't finalize a reasoning grade on an unresolved trade
    if status in {"OPEN", "INCONCLUSIVE"} and rr.get("direction_call") in {"RIGHT", "WRONG"}:
        errs.append("direction_call must be UNRESOLVED while outcome is OPEN/INCONCLUSIVE")

    cal = d["calibration"]
    if cal.get("conviction") not in CONV:
        errs.append(f"calibration.conviction must be one of {CONV}")
    bit = cal.get("outcome_bit")
    brier = cal.get("brier")
    if status in {"WIN", "LOSS"}:
        expect_bit = 1 if status == "WIN" else 0
        if bit != expect_bit:
            errs.append(f"calibration.outcome_bit must be {expect_bit} for {status}")
        if brier is not None and cal.get("conviction") is not None:
            exp = round((float(cal["conviction"]) - expect_bit) ** 2, 6)
            if abs(float(brier) - exp) > 0.001:
                errs.append(f"calibration.brier {brier} != (conviction-{expect_bit})^2 = {exp:.4f}")
    else:
        if bit not in (None,):
            errs.append("calibration.outcome_bit must be null for OPEN/INCONCLUSIVE")

    for i, le in enumerate(d["lessons"]):
        if not LID.match(str(le.get("id", ""))):
            errs.append(f"lessons[{i}].id must match L-#### (got {le.get('id')!r})")
        if le.get("status") not in {"CANDIDATE", "ACTIVE", "RETIRED"}:
            errs.append(f"lessons[{i}].status invalid")
        if le.get("status") == "ACTIVE" and not le.get("scope"):
            errs.append(f"lessons[{i}] ACTIVE lesson must carry a scope")

    if not str(d.get("disclaimer", "")).strip():
        errs.append("disclaimer must be present")

    return errs


def main() -> None:
    p = argparse.ArgumentParser(description="Validate a trade-plan eval.json")
    p.add_argument("--file", required=True)
    args = p.parse_args()
    path = Path(args.file)
    if not path.exists():
        print(f"File not found: {args.file}", file=sys.stderr)
        sys.exit(1)
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"Invalid JSON in {args.file}: {e}", file=sys.stderr)
        sys.exit(1)
    errs = validate(data)
    if errs:
        print(f"INVALID: {args.file}", file=sys.stderr)
        for e in errs:
            print(f"  - {e}", file=sys.stderr)
        sys.exit(1)
    print(f"OK: {args.file} is a valid TradePlanEval")


if __name__ == "__main__":
    main()
