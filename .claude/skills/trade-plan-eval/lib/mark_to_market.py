#!/usr/bin/env python3
"""Path-aware mark-to-market for a taken trade-plan.

Given a plan's direction / entry / stop / targets and the OHLC path AFTER the
plan date, decide -- in chronological order, the way a real position fills --
whether the stop or the first target was hit first, how much reward:risk (R) was
realised, and the max favourable / adverse excursion. This is the deterministic
truth set the eval skill scores reasoning against; it mirrors the
``/deep-dive-calibration`` path-aware ±1R convention.

Reuses ``ohlc.py`` from the sibling trade-plan skill as the single OHLC source.

CLI:
    python3 mark_to_market.py --ticker NVDA --plan-date 2026-06-18 \
        --review-date 2026-07-10 --direction long \
        --entry 212.9 --stop 199.3 --targets 224.0,235.7 [--invalidation 199.34]
Always exits 0 and prints one JSON object.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# single source of truth for OHLC sourcing: the trade-plan skill's lib
_TP_LIB = Path(__file__).resolve().parents[2] / "trade-plan" / "lib"
sys.path.insert(0, str(_TP_LIB))

try:
    from ohlc import load_ohlc  # type: ignore
except Exception:  # pragma: no cover
    load_ohlc = None


def _f(x):
    try:
        return round(float(x), 2)
    except (TypeError, ValueError):
        return None


def mark(
    ticker: str,
    plan_date: str,
    review_date: str,
    direction: str,
    entry: float,
    stop: float,
    targets: list[float],
    invalidation: float | None = None,
) -> dict:
    if load_ohlc is None:
        return {"available": False, "error": "ohlc loader unavailable"}

    res = load_ohlc(ticker, review_date, lookback_days=400)
    if not res.available:
        return {"available": False, "error": f"no OHLC ({res.source})", "note": res.note}

    df = res.df
    # bars strictly after the plan date, up to and including the review date
    window = df[(df.index > __as_date(plan_date)) & (df.index <= __as_date(review_date))]
    if len(window) == 0:
        return {"available": True, "outcome": "OPEN", "note": "no sessions yet after plan date",
                "ticker": ticker.upper(), "days_held": 0}

    is_long = direction.lower() == "long"
    risk = abs(entry - stop)
    if risk == 0:
        return {"available": False, "error": "entry == stop (zero risk)"}

    target_hits = {str(_f(t)): None for t in targets}
    first_target = targets[0] if targets else None
    stop_hit_date = None
    first_target_date = None
    mfe = -1e18  # max favourable excursion (price terms, signed toward profit)
    mae = -1e18  # max adverse excursion (magnitude against the position)

    for dt, row in window.iterrows():
        hi, lo = float(row["high"]), float(row["low"])
        # excursions in profit-direction terms
        fav = (hi - entry) if is_long else (entry - lo)
        adv = (entry - lo) if is_long else (hi - entry)
        mfe = max(mfe, fav)
        mae = max(mae, adv)

        # path order within the bar is unknown; be conservative -> stop checked first
        stop_touched = (lo <= stop) if is_long else (hi >= stop)
        if stop_touched and stop_hit_date is None:
            stop_hit_date = str(dt)

        for t in targets:
            key = str(_f(t))
            reached = (hi >= t) if is_long else (lo <= t)
            if reached and target_hits[key] is None:
                target_hits[key] = str(dt)
                if t == first_target and first_target_date is None:
                    first_target_date = str(dt)

        # stop the path-walk once a terminal event has happened
        if stop_hit_date and (first_target_date is None):
            break
        if first_target_date and first_target_date <= (stop_hit_date or "9999"):
            break

    # resolve outcome path-aware: whichever terminal event dated first
    outcome = "OPEN"
    r_achieved = None
    if first_target_date and (stop_hit_date is None or first_target_date <= stop_hit_date):
        outcome = "WIN"
        r_achieved = round(abs(first_target - entry) / risk, 2)
    elif stop_hit_date and (first_target_date is None or stop_hit_date < first_target_date):
        outcome = "LOSS"
        r_achieved = -1.0
    else:
        # neither hit: mark to the last close
        last_close = float(window["close"].iloc[-1])
        signed = (last_close - entry) if is_long else (entry - last_close)
        r_achieved = round(signed / risk, 2)
        outcome = "OPEN"

    invalidation_hit = None
    if invalidation is not None:
        invalidation_hit = bool(
            (window["low"].min() <= invalidation) if is_long
            else (window["high"].max() >= invalidation)
        )

    return {
        "available": True,
        "ticker": ticker.upper(),
        "direction": direction.lower(),
        "source": res.source,
        "plan_date": plan_date,
        "review_date": review_date,
        "sessions_observed": int(len(window)),
        "entry": _f(entry), "stop": _f(stop), "targets": [_f(t) for t in targets],
        "outcome": outcome,
        "r_achieved": r_achieved,
        "first_target_date": first_target_date,
        "stop_hit_date": stop_hit_date,
        "target_hits": target_hits,
        "max_favorable_excursion": _f(mfe),
        "max_adverse_excursion": _f(mae),
        "mfe_R": round(mfe / risk, 2) if mfe > -1e17 else None,
        "mae_R": round(mae / risk, 2) if mae > -1e17 else None,
        "invalidation_price_hit": invalidation_hit,
        "last_close": _f(float(window["close"].iloc[-1])),
    }


def __as_date(s: str):
    from datetime import datetime
    return datetime.strptime(s, "%Y-%m-%d").date()


def main() -> None:
    ap = argparse.ArgumentParser(description="Path-aware mark-to-market for a trade plan")
    ap.add_argument("--ticker", required=True)
    ap.add_argument("--plan-date", required=True)
    ap.add_argument("--review-date", required=True)
    ap.add_argument("--direction", required=True, choices=["long", "short"])
    ap.add_argument("--entry", required=True, type=float)
    ap.add_argument("--stop", required=True, type=float)
    ap.add_argument("--targets", required=True, help="comma-separated target prices")
    ap.add_argument("--invalidation", type=float, default=None)
    args = ap.parse_args()

    targets = [float(t) for t in args.targets.split(",") if t.strip()]
    try:
        out = mark(args.ticker, args.plan_date, args.review_date, args.direction,
                   args.entry, args.stop, targets, args.invalidation)
    except Exception as e:
        out = {"available": False, "error": f"{type(e).__name__}: {e}"}
    print(json.dumps(out, indent=2))
    sys.exit(0)


if __name__ == "__main__":
    main()
