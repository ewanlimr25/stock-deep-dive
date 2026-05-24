#!/usr/bin/env python3
"""Validate a phase-9 decision.json envelope. Pure stdlib — no pip installs.

The skill runs no application code, so this validator depends only on the
Python standard library (json/argparse/math). It enforces the structural rules
the JSON Schema declares PLUS the cross-field semantics a schema can't express:

  - conviction is one of the five M-01 bins
  - final_size_pct never exceeds cap_pct
  - final_size_pct matches min(raw_kelly * fraction * 100, cap_pct) unless
    sizing.deviation_reason is supplied (the M-03 Kelly contract)
  - a negative-edge (raw_kelly < 0) directional trade is not sized > 0
  - a fundamentals VETO forces directional final_size_pct == 0
  - at least one directional AND one defined_risk structure
  - at least three citations

Usage:
    python3 validate_decision.py --file research/NVDA/2026-05-15/decision.json
Exit code 0 = valid, 1 = invalid (errors printed to stderr).
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

CONVICTION_BINS = (0.55, 0.65, 0.75, 0.85, 0.95)
BIAS = {"LONG", "SHORT", "NEUTRAL", "RANGE"}
HORIZON = {"intraday", "1-5d", "1-4w", "1-3m"}
FUND_GATE = {"CONFIRM", "CAUTION", "VETO", "NA"}
ROTATION = {"aligned", "adverse", "neutral"}

REQUIRED_TOP = [
    "ticker", "date", "generated", "bias", "conviction", "horizon",
    "spot_reference", "thesis", "entries", "levels", "invalidation",
    "sizing", "structures", "gates", "macro", "catalysts", "key_risks",
    "citations", "paths", "disclaimer",
]
REQUIRED_SIZING = ["p", "payoff_b", "raw_kelly", "fraction", "cap_pct",
                   "final_size_pct", "win_rate_source"]
REQUIRED_GATES = ["fundamentals", "correlation_cluster", "sector_rotation",
                  "debate_disconfirmed"]


def _approx(a: float, b: float, tol: float = 0.01) -> bool:
    return abs(a - b) <= tol


def validate(data: dict) -> list[str]:
    errs: list[str] = []

    for k in REQUIRED_TOP:
        if k not in data:
            errs.append(f"missing required field: {k}")
    if errs:
        return errs  # structure too incomplete to check semantics

    if data["bias"] not in BIAS:
        errs.append(f"bias must be one of {sorted(BIAS)}; got {data['bias']!r}")
    if data["conviction"] not in CONVICTION_BINS:
        errs.append(f"conviction must be one of {CONVICTION_BINS}; got {data['conviction']!r}")
    if data["horizon"] not in HORIZON:
        errs.append(f"horizon must be one of {sorted(HORIZON)}; got {data['horizon']!r}")

    sizing = data["sizing"]
    for k in REQUIRED_SIZING:
        if k not in sizing:
            errs.append(f"sizing.{k} missing")
    if not errs or all(k in sizing for k in REQUIRED_SIZING):
        try:
            cap = float(sizing["cap_pct"])
            final = float(sizing["final_size_pct"])
            raw = float(sizing["raw_kelly"])
            frac = float(sizing["fraction"])
            if final > cap + 1e-9:
                errs.append(f"final_size_pct {final} exceeds cap_pct {cap}")
            # Kelly contract: final must equal the capped fractional Kelly unless
            # a deviation reason is given (deviating DOWN is always allowed).
            kelly_ceiling = min(max(raw, 0.0) * frac * 100.0, cap)
            if final > kelly_ceiling + 1e-9 and not sizing.get("deviation_reason"):
                errs.append(
                    f"final_size_pct {final} exceeds Kelly ceiling "
                    f"{kelly_ceiling:.4f} without sizing.deviation_reason"
                )
            if raw < 0 and data["bias"] in {"LONG", "SHORT"} and final > 0:
                errs.append(
                    "negative raw_kelly with a directional bias must be sized 0 "
                    "(publish defined-risk carry only)"
                )
        except (TypeError, ValueError) as e:
            errs.append(f"sizing numeric fields not parseable: {e}")

    gates = data["gates"]
    for k in REQUIRED_GATES:
        if k not in gates:
            errs.append(f"gates.{k} missing")
    if gates.get("fundamentals") not in FUND_GATE:
        errs.append(f"gates.fundamentals must be one of {sorted(FUND_GATE)}")
    if gates.get("sector_rotation") not in ROTATION:
        errs.append(f"gates.sector_rotation must be one of {sorted(ROTATION)}")
    if gates.get("fundamentals") == "VETO" and data["bias"] in {"LONG", "SHORT"}:
        try:
            if float(sizing.get("final_size_pct", 1)) != 0:
                errs.append("fundamentals VETO requires directional final_size_pct == 0 (watch-only)")
        except (TypeError, ValueError):
            pass

    structs = data["structures"]
    if not isinstance(structs, list) or len(structs) < 2:
        errs.append("structures must list >= 2 entries")
    else:
        kinds = {s.get("kind") for s in structs if isinstance(s, dict)}
        if "directional" not in kinds:
            errs.append("need >= 1 structure with kind='directional'")
        if "defined_risk" not in kinds:
            errs.append("need >= 1 structure with kind='defined_risk'")

    cites = data["citations"]
    if not isinstance(cites, list) or len(cites) < 3:
        errs.append("citations must list >= 3 tagged datapoints (M-04)")

    kr = data["key_risks"]
    if not isinstance(kr, list) or not (1 <= len(kr) <= 5):
        errs.append("key_risks must list 1-5 items")

    return errs


def main() -> None:
    p = argparse.ArgumentParser(description="Validate a deep-dive decision.json")
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
    print(f"OK: {args.file} is a valid DeepDiveDecision")


if __name__ == "__main__":
    main()
