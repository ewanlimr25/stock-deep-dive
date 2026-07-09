#!/usr/bin/env python3
"""Validate a trade-plan.json envelope. Pure stdlib -- no pip installs.

Enforces the structural rules the JSON Schema declares PLUS the cross-field
semantics a schema can't express, mirroring the stock-deep-dive
validate_decision.py contract:

  - conviction is one of the five M-01 bins
  - final_size_pct never exceeds cap_pct, and matches the capped fractional
    Kelly unless sizing.deviation_reason is supplied (deviating DOWN is fine)
  - a negative-edge (raw_kelly < 0) directional bias is not sized > 0
  - >= 1 stock_plan with a real direction (long/short) OR an explicit
    stand_aside, AND >= 1 options plan -- each options plan carries a
    target_date AND a target_price (goal #8)
  - reasons_for and reasons_against each list >= 2 items (goal #3)
  - gap_audit present with a verdict (goal #1/#2)
  - >= 3 citations

Usage:
    python3 validate_trade_plan.py --file trade-plans/NVDA/2026-06-18/trade-plan.json
Exit 0 = valid, 1 = invalid (errors to stderr).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

CONVICTION_BINS = (0.55, 0.65, 0.75, 0.85, 0.95)
BIAS = {"LONG", "SHORT", "NEUTRAL", "RANGE"}
HORIZON = {"intraday", "1-5d", "1-4w", "1-3m", "3-12m"}
GAP_VERDICT = {"SUFFICIENT", "USABLE_WITH_GAPS", "INSUFFICIENT"}
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

REQUIRED_TOP = [
    "ticker", "date", "generated", "bias", "conviction", "horizon",
    "spot_reference", "thesis", "reasons_for", "reasons_against",
    "levels", "patterns", "events", "invalidation", "sizing",
    "stock_plan", "options_plans", "gap_audit", "sources",
    "citations", "paths", "disclaimer",
]
REQUIRED_SIZING = ["p", "payoff_b", "raw_kelly", "fraction", "cap_pct",
                   "final_size_pct", "win_rate_source"]


def validate(data: dict) -> list[str]:
    errs: list[str] = []

    for k in REQUIRED_TOP:
        if k not in data:
            errs.append(f"missing required field: {k}")
    if errs:
        return errs

    if data["bias"] not in BIAS:
        errs.append(f"bias must be one of {sorted(BIAS)}; got {data['bias']!r}")
    if data["conviction"] not in CONVICTION_BINS:
        errs.append(f"conviction must be one of {CONVICTION_BINS}; got {data['conviction']!r}")
    if data["horizon"] not in HORIZON:
        errs.append(f"horizon must be one of {sorted(HORIZON)}; got {data['horizon']!r}")
    if not DATE_RE.match(str(data["date"])):
        errs.append("date must be YYYY-MM-DD")

    # --- reasons for / against (goal #3) ---
    for side in ("reasons_for", "reasons_against"):
        v = data.get(side)
        if not isinstance(v, list) or len(v) < 2:
            errs.append(f"{side} must list >= 2 items (goal #3)")

    # --- sizing / Kelly contract ---
    sizing = data["sizing"]
    for k in REQUIRED_SIZING:
        if k not in sizing:
            errs.append(f"sizing.{k} missing")
    if all(k in sizing for k in REQUIRED_SIZING):
        try:
            cap = float(sizing["cap_pct"])
            final = float(sizing["final_size_pct"])
            raw = float(sizing["raw_kelly"])
            frac = float(sizing["fraction"])
            if final > cap + 1e-9:
                errs.append(f"final_size_pct {final} exceeds cap_pct {cap}")
            kelly_ceiling = min(max(raw, 0.0) * frac * 100.0, cap)
            if final > kelly_ceiling + 1e-9 and not sizing.get("deviation_reason"):
                errs.append(
                    f"final_size_pct {final} exceeds Kelly ceiling "
                    f"{kelly_ceiling:.4f} without sizing.deviation_reason"
                )
            if raw < 0 and data["bias"] in {"LONG", "SHORT"} and final > 0:
                errs.append("negative raw_kelly with a directional bias must be sized 0")
        except (TypeError, ValueError) as e:
            errs.append(f"sizing numeric fields not parseable: {e}")

    # --- stock plan (goal #8: at least one pure long/short) ---
    sp = data["stock_plan"]
    if not isinstance(sp, dict):
        errs.append("stock_plan must be an object")
    else:
        if sp.get("direction") not in {"long", "short", "stand_aside"}:
            errs.append("stock_plan.direction must be long|short|stand_aside")
        if not isinstance(sp.get("targets"), list) or len(sp.get("targets", [])) < 1:
            errs.append("stock_plan.targets must list >= 1 target")
        for f in ("entry", "stop", "thesis_one_liner"):
            if f not in sp:
                errs.append(f"stock_plan.{f} missing")

    # --- options plans (goal #8: each with target_date + target_price) ---
    ops = data["options_plans"]
    if not isinstance(ops, list) or len(ops) < 1:
        errs.append("options_plans must list >= 1 plan (goal #8)")
    else:
        for i, op in enumerate(ops):
            if not isinstance(op, dict):
                errs.append(f"options_plans[{i}] must be an object")
                continue
            for f in ("structure", "strikes", "expiry", "target_date", "target_price", "max_loss"):
                if f not in op or op[f] in (None, ""):
                    errs.append(f"options_plans[{i}].{f} missing (target_date & target_price are required, goal #8)")
            if "target_date" in op and op["target_date"] and not DATE_RE.match(str(op["target_date"])):
                errs.append(f"options_plans[{i}].target_date must be YYYY-MM-DD")
            if "target_price" in op and op["target_price"] is not None:
                try:
                    float(op["target_price"])
                except (TypeError, ValueError):
                    errs.append(f"options_plans[{i}].target_price must be numeric")

    # --- gap audit (goal #1/#2) ---
    ga = data["gap_audit"]
    if not isinstance(ga, dict):
        errs.append("gap_audit must be an object")
    else:
        if ga.get("verdict") not in GAP_VERDICT:
            errs.append(f"gap_audit.verdict must be one of {sorted(GAP_VERDICT)}")
        for f in ("completeness", "have", "missing"):
            if f not in ga:
                errs.append(f"gap_audit.{f} missing")

    # --- events / levels presence ---
    if not isinstance(data.get("events"), list):
        errs.append("events must be a list (may be empty)")
    if not isinstance(data.get("patterns"), list):
        errs.append("patterns must be a list (may be empty)")

    # --- citations ---
    cites = data["citations"]
    if not isinstance(cites, list) or len(cites) < 3:
        errs.append("citations must list >= 3 tagged datapoints")

    # --- paths / disclaimer ---
    if not isinstance(data.get("paths"), dict) or "plan" not in data["paths"]:
        errs.append("paths.plan missing")
    if not str(data.get("disclaimer", "")).strip():
        errs.append("disclaimer must be present")

    return errs


def main() -> None:
    p = argparse.ArgumentParser(description="Validate a trade-plan.json envelope")
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
    print(f"OK: {args.file} is a valid TradePlan")


if __name__ == "__main__":
    main()
