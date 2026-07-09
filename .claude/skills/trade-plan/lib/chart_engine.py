#!/usr/bin/env python3
"""Deterministic chart / technical / pattern engine for the trade-plan skill.

This is the price-structure layer the Unusual Whales flow substrate lacks. It
turns daily OHLCV (sourced by ``ohlc.py``) into:

  * trend & momentum indicators (SMA/EMA stack, RSI, ATR, MACD, Bollinger),
  * swing pivots (fractals) and clustered horizontal support / resistance,
  * trendlines / channel slope and market structure (HH-HL vs LH-LL),
  * Fibonacci retracement / extension off the dominant swing,
  * chart-pattern heuristics: flag/pole, head-&-shoulders (+inverse),
    double top/bottom, triangles (asc/desc/sym), cup-&-handle,
  * an Elliott-wave working count with the rules it passes / violates,
  * a consolidated ``levels_to_watch`` ladder + ATR-based stop distances.

Every pattern verdict carries an explicit ``confidence`` and, where defined, a
``measured_target`` and ``invalidation`` so the LLM layer can quote falsifiable
numbers rather than eyeball the chart. The engine is intentionally conservative:
it would rather report ``detected: false`` than hallucinate a textbook pattern.

CLI:
    python3 chart_engine.py --ticker NVDA --date 2026-06-18 [--lookback 540]
Always exits 0 and prints a single JSON object (``available: false`` if no data),
mirroring the uw-daily-analysis enrichment-script contract.
"""

from __future__ import annotations

import argparse
import json
import sys
from typing import Any

import numpy as np
import pandas as pd

try:  # allow both "python3 chart_engine.py" and package import
    from ohlc import OHLCResult, load_ohlc
except ImportError:  # pragma: no cover
    from .ohlc import OHLCResult, load_ohlc


# --------------------------------------------------------------------------- #
# small helpers
# --------------------------------------------------------------------------- #
def _round(x: Any, n: int = 2) -> Any:
    try:
        if x is None or (isinstance(x, float) and (np.isnan(x) or np.isinf(x))):
            return None
        return round(float(x), n)
    except (TypeError, ValueError):
        return None


def _pct(a: float, b: float) -> Any:
    """(a-b)/b * 100, guarded."""
    try:
        if b == 0 or b is None:
            return None
        return round((a - b) / b * 100.0, 2)
    except (TypeError, ValueError, ZeroDivisionError):
        return None


# --------------------------------------------------------------------------- #
# indicators
# --------------------------------------------------------------------------- #
def _rsi(close: pd.Series, period: int = 14) -> pd.Series:
    delta = close.diff()
    gain = delta.clip(lower=0.0)
    loss = -delta.clip(upper=0.0)
    avg_gain = gain.ewm(alpha=1 / period, min_periods=period, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1 / period, min_periods=period, adjust=False).mean()
    rs = avg_gain / avg_loss.replace(0.0, np.nan)
    return 100 - (100 / (1 + rs))


def _atr(df: pd.DataFrame, period: int = 14) -> pd.Series:
    high, low, close = df["high"], df["low"], df["close"]
    prev_close = close.shift(1)
    tr = pd.concat(
        [(high - low), (high - prev_close).abs(), (low - prev_close).abs()], axis=1
    ).max(axis=1)
    return tr.ewm(alpha=1 / period, min_periods=period, adjust=False).mean()


def compute_indicators(df: pd.DataFrame) -> dict[str, Any]:
    close = df["close"]
    spot = float(close.iloc[-1])
    n = len(df)

    def sma(p: int) -> float | None:
        return float(close.rolling(p).mean().iloc[-1]) if n >= p else None

    def ema(p: int) -> float | None:
        return float(close.ewm(span=p, adjust=False).mean().iloc[-1]) if n >= p else None

    sma20, sma50, sma200 = sma(20), sma(50), sma(200)
    ema9, ema21 = ema(9), ema(21)
    rsi = _rsi(close).iloc[-1] if n >= 15 else None
    atr = _atr(df).iloc[-1] if n >= 15 else None

    macd_line = close.ewm(span=12, adjust=False).mean() - close.ewm(span=26, adjust=False).mean()
    signal = macd_line.ewm(span=9, adjust=False).mean()
    macd_hist = float((macd_line - signal).iloc[-1]) if n >= 26 else None

    bb_mid = close.rolling(20).mean()
    bb_std = close.rolling(20).std()
    bb_upper = float((bb_mid + 2 * bb_std).iloc[-1]) if n >= 20 else None
    bb_lower = float((bb_mid - 2 * bb_std).iloc[-1]) if n >= 20 else None

    vol = df["volume"]
    vol_avg20 = float(vol.rolling(20).mean().iloc[-1]) if n >= 20 and vol.notna().any() else None
    vol_last = float(vol.iloc[-1]) if vol.notna().any() else None

    hi_52 = float(close.tail(252).max())
    lo_52 = float(close.tail(252).min())

    # MA stack: bullish if price>sma20>sma50>sma200
    stack = None
    if all(v is not None for v in (sma20, sma50, sma200)):
        if spot > sma20 > sma50 > sma200:
            stack = "bullish_stack"
        elif spot < sma20 < sma50 < sma200:
            stack = "bearish_stack"
        else:
            stack = "mixed"

    return {
        "spot": _round(spot),
        "sessions": n,
        "sma20": _round(sma20),
        "sma50": _round(sma50),
        "sma200": _round(sma200),
        "ema9": _round(ema9),
        "ema21": _round(ema21),
        "ma_stack": stack,
        "dist_to_sma50_pct": _pct(spot, sma50) if sma50 else None,
        "dist_to_sma200_pct": _pct(spot, sma200) if sma200 else None,
        "rsi14": _round(rsi),
        "rsi_state": ("overbought" if rsi is not None and rsi >= 70
                      else "oversold" if rsi is not None and rsi <= 30
                      else "neutral" if rsi is not None else None),
        "atr14": _round(atr),
        "atr_pct": _pct(spot, spot - atr) if atr else None,
        "macd_hist": _round(macd_hist, 3),
        "macd_state": ("bullish" if macd_hist and macd_hist > 0
                       else "bearish" if macd_hist and macd_hist < 0 else None),
        "bb_upper": _round(bb_upper),
        "bb_lower": _round(bb_lower),
        "vol_last": _round(vol_last, 0),
        "vol_avg20": _round(vol_avg20, 0),
        "vol_vs_avg": _round(vol_last / vol_avg20, 2) if vol_last and vol_avg20 else None,
        "high_52w": _round(hi_52),
        "low_52w": _round(lo_52),
        "pct_off_52w_high": _pct(spot, hi_52),
        "pct_above_52w_low": _pct(spot, lo_52),
    }


# --------------------------------------------------------------------------- #
# swing pivots + horizontal levels
# --------------------------------------------------------------------------- #
def find_pivots(df: pd.DataFrame, left: int = 3, right: int = 3) -> list[dict[str, Any]]:
    """Fractal swing highs/lows: a bar higher (lower) than ``left`` bars before
    and ``right`` bars after. Returns chronologically ordered pivots."""
    highs, lows = df["high"].values, df["low"].values
    idx = list(df.index)
    pivots: list[dict[str, Any]] = []
    for i in range(left, len(df) - right):
        win_h = highs[i - left : i + right + 1]
        win_l = lows[i - left : i + right + 1]
        if highs[i] == win_h.max() and (win_h.argmax() == left):
            pivots.append({"i": i, "date": str(idx[i]), "price": _round(highs[i]), "kind": "high"})
        elif lows[i] == win_l.min() and (win_l.argmin() == left):
            pivots.append({"i": i, "date": str(idx[i]), "price": _round(lows[i]), "kind": "low"})
    return pivots


def cluster_levels(pivots: list[dict], spot: float, tol_pct: float = 1.5) -> list[dict[str, Any]]:
    """Group pivots whose prices are within ``tol_pct`` into S/R levels, ranked
    by touch count then proximity to spot."""
    if not pivots:
        return []
    pts = sorted(pivots, key=lambda p: p["price"])
    clusters: list[list[dict]] = [[pts[0]]]
    for p in pts[1:]:
        anchor = clusters[-1][0]["price"]
        if abs(p["price"] - anchor) / anchor * 100.0 <= tol_pct:
            clusters[-1].append(p)
        else:
            clusters.append([p])

    levels = []
    for c in clusters:
        price = float(np.mean([p["price"] for p in c]))
        levels.append({
            "level": _round(price),
            "touches": len(c),
            "kind": "support" if price < spot else "resistance",
            "dist_pct": _pct(price, spot),
            "last_touch": max(p["date"] for p in c),
        })
    levels.sort(key=lambda x: (-x["touches"], abs(x["dist_pct"] or 999)))
    return levels


# --------------------------------------------------------------------------- #
# trend / structure
# --------------------------------------------------------------------------- #
def trend_state(df: pd.DataFrame, pivots: list[dict], window: int = 60) -> dict[str, Any]:
    close = df["close"].tail(window)
    x = np.arange(len(close))
    slope = float(np.polyfit(x, close.values, 1)[0]) if len(close) >= 5 else 0.0
    slope_pct_per_day = _pct(close.iloc[-1], close.iloc[-1] - slope) if slope else 0.0

    highs = [p for p in pivots if p["kind"] == "high"][-3:]
    lows = [p for p in pivots if p["kind"] == "low"][-3:]
    structure = "indeterminate"
    if len(highs) >= 2 and len(lows) >= 2:
        hh = highs[-1]["price"] > highs[-2]["price"]
        hl = lows[-1]["price"] > lows[-2]["price"]
        lh = highs[-1]["price"] < highs[-2]["price"]
        ll = lows[-1]["price"] < lows[-2]["price"]
        if hh and hl:
            structure = "uptrend_HH_HL"
        elif lh and ll:
            structure = "downtrend_LH_LL"
        else:
            structure = "range_or_transition"

    return {
        "regression_slope": _round(slope, 4),
        "slope_pct_per_day": slope_pct_per_day,
        "direction": "up" if slope > 0 else "down" if slope < 0 else "flat",
        "market_structure": structure,
        "lookback_sessions": int(len(close)),
    }


# --------------------------------------------------------------------------- #
# Fibonacci off the dominant swing
# --------------------------------------------------------------------------- #
def fibonacci(df: pd.DataFrame, lookback: int = 120) -> dict[str, Any]:
    seg = df.tail(lookback)
    hi_i = seg["high"].idxmax()
    lo_i = seg["low"].idxmin()
    hi = float(seg["high"].max())
    lo = float(seg["low"].min())
    if hi == lo:
        return {"available": False}
    # direction of the dominant swing: did the high or the low come last?
    up_swing = list(seg.index).index(lo_i) < list(seg.index).index(hi_i)
    rng = hi - lo
    ratios = [0.236, 0.382, 0.5, 0.618, 0.786]
    if up_swing:  # retracements measured down from the high
        retr = {f"{r:.3f}": _round(hi - rng * r) for r in ratios}
        ext = {"1.272": _round(hi + rng * 0.272), "1.618": _round(hi + rng * 0.618)}
    else:  # downswing: retracements measured up from the low
        retr = {f"{r:.3f}": _round(lo + rng * r) for r in ratios}
        ext = {"1.272": _round(lo - rng * 0.272), "1.618": _round(lo - rng * 0.618)}
    return {
        "available": True,
        "swing_high": _round(hi),
        "swing_low": _round(lo),
        "swing_direction": "up" if up_swing else "down",
        "retracements": retr,
        "extensions": ext,
    }


# --------------------------------------------------------------------------- #
# pattern detectors  (each: {detected, confidence, ...})
# --------------------------------------------------------------------------- #
def detect_flag(df: pd.DataFrame, atr: float | None) -> dict[str, Any]:
    """Sharp pole (>= ~3 ATR over <=10 bars) then a tight, shallow drift."""
    if atr is None or len(df) < 20:
        return {"detected": False}
    close = df["close"]
    pole = close.iloc[-15] if len(df) >= 15 else close.iloc[0]
    pole_start = close.iloc[-20]
    pole_move = pole - pole_start
    if abs(pole_move) < 3 * atr:
        return {"detected": False}
    consol = close.tail(10)
    consol_range = float(consol.max() - consol.min())
    if consol_range > 1.5 * atr:  # consolidation too wide -> not a flag
        return {"detected": False}
    bull = pole_move > 0
    spot = float(close.iloc[-1])
    target = _round(spot + pole_move) if bull else _round(spot + pole_move)
    return {
        "detected": True,
        "type": "bull_flag" if bull else "bear_flag",
        "confidence": "medium",
        "pole_move": _round(pole_move),
        "consolidation_range": _round(consol_range),
        "measured_target": target,
        "invalidation": _round(float(consol.min()) if bull else float(consol.max())),
        "note": "measured move = consolidation breakout +/- pole height",
    }


def detect_head_shoulders(pivots: list[dict], spot: float) -> dict[str, Any]:
    """Classic H&S (3 highs, middle highest) or inverse (3 lows, middle lowest)."""
    highs = [p for p in pivots if p["kind"] == "high"]
    lows = [p for p in pivots if p["kind"] == "low"]

    def shoulders_ok(a, b, c, top: bool) -> bool:
        head = b["price"]
        if top:
            return head > a["price"] and head > c["price"] and \
                abs(a["price"] - c["price"]) / head < 0.05
        return head < a["price"] and head < c["price"] and \
            abs(a["price"] - c["price"]) / max(head, 1e-9) < 0.05

    if len(highs) >= 3:
        a, b, c = highs[-3:]
        if shoulders_ok(a, b, c, top=True):
            neck = min(p["price"] for p in lows[-2:]) if len(lows) >= 2 else min(a["price"], c["price"])
            height = b["price"] - neck
            return {
                "detected": True, "type": "head_and_shoulders", "confidence": "medium",
                "neckline": _round(neck), "head": _round(b["price"]),
                "measured_target": _round(neck - height),
                "invalidation": _round(b["price"]),
                "note": "bearish; confirmed on a close below the neckline",
            }
    if len(lows) >= 3:
        a, b, c = lows[-3:]
        if shoulders_ok(a, b, c, top=False):
            neck = max(p["price"] for p in highs[-2:]) if len(highs) >= 2 else max(a["price"], c["price"])
            height = neck - b["price"]
            return {
                "detected": True, "type": "inverse_head_and_shoulders", "confidence": "medium",
                "neckline": _round(neck), "head": _round(b["price"]),
                "measured_target": _round(neck + height),
                "invalidation": _round(b["price"]),
                "note": "bullish; confirmed on a close above the neckline",
            }
    return {"detected": False}


def detect_double(pivots: list[dict], spot: float, tol: float = 0.03) -> dict[str, Any]:
    highs = [p for p in pivots if p["kind"] == "high"]
    lows = [p for p in pivots if p["kind"] == "low"]
    if len(highs) >= 2:
        a, b = highs[-2:]
        if abs(a["price"] - b["price"]) / max(a["price"], 1e-9) <= tol and spot < b["price"]:
            trough = min((p["price"] for p in lows if a["i"] < p["i"] < b["i"]), default=None)
            if trough:
                return {
                    "detected": True, "type": "double_top", "confidence": "medium",
                    "resistance": _round((a["price"] + b["price"]) / 2),
                    "neckline": _round(trough),
                    "measured_target": _round(trough - (b["price"] - trough)),
                    "invalidation": _round(max(a["price"], b["price"])),
                    "note": "bearish; confirmed on a close below the intervening trough",
                }
    if len(lows) >= 2:
        a, b = lows[-2:]
        if abs(a["price"] - b["price"]) / max(a["price"], 1e-9) <= tol and spot > b["price"]:
            peak = max((p["price"] for p in highs if a["i"] < p["i"] < b["i"]), default=None)
            if peak:
                return {
                    "detected": True, "type": "double_bottom", "confidence": "medium",
                    "support": _round((a["price"] + b["price"]) / 2),
                    "neckline": _round(peak),
                    "measured_target": _round(peak + (peak - b["price"])),
                    "invalidation": _round(min(a["price"], b["price"])),
                    "note": "bullish; confirmed on a close above the intervening peak",
                }
    return {"detected": False}


def detect_triangle(pivots: list[dict]) -> dict[str, Any]:
    """Converging trendlines from the last >=3 highs and >=3 lows."""
    highs = [p for p in pivots if p["kind"] == "high"][-3:]
    lows = [p for p in pivots if p["kind"] == "low"][-3:]
    if len(highs) < 2 or len(lows) < 2:
        return {"detected": False}
    h_slope = float(np.polyfit([p["i"] for p in highs], [p["price"] for p in highs], 1)[0])
    l_slope = float(np.polyfit([p["i"] for p in lows], [p["price"] for p in lows], 1)[0])
    flat = lambda s, ref: abs(s) / max(ref, 1e-9) < 0.0008  # near-horizontal threshold
    ref = float(np.mean([p["price"] for p in highs + lows]))
    if h_slope < 0 and l_slope > 0:
        kind, bias = "symmetrical_triangle", "neutral"
    elif flat(h_slope, ref) and l_slope > 0:
        kind, bias = "ascending_triangle", "bullish"
    elif h_slope < 0 and flat(l_slope, ref):
        kind, bias = "descending_triangle", "bearish"
    else:
        return {"detected": False}
    return {
        "detected": True, "type": kind, "confidence": "low", "bias": bias,
        "upper_trendline_slope": _round(h_slope, 4),
        "lower_trendline_slope": _round(l_slope, 4),
        "note": "trade the break; converging trendlines",
    }


def detect_cup_handle(df: pd.DataFrame) -> dict[str, Any]:
    """Rough U-shape (rounded bottom) followed by a shallow handle near the rim."""
    if len(df) < 40:
        return {"detected": False}
    seg = df["close"].tail(60)
    left_rim = float(seg.iloc[:10].max())
    right_rim = float(seg.iloc[-15:-5].max())
    bottom = float(seg.min())
    bottom_i = int(np.argmin(seg.values))
    rim_match = abs(left_rim - right_rim) / max(left_rim, 1e-9) < 0.06
    rounded = 10 < bottom_i < len(seg) - 10  # bottom roughly central
    depth = (left_rim - bottom) / max(left_rim, 1e-9)
    handle = float(seg.iloc[-5:].min()) > right_rim * 0.95
    if rim_match and rounded and 0.12 < depth < 0.5 and handle:
        return {
            "detected": True, "type": "cup_and_handle", "confidence": "low",
            "rim": _round((left_rim + right_rim) / 2),
            "measured_target": _round(right_rim + (right_rim - bottom)),
            "invalidation": _round(bottom),
            "note": "bullish continuation; confirmed on a close above the rim",
        }
    return {"detected": False}


# --------------------------------------------------------------------------- #
# Elliott wave heuristic
# --------------------------------------------------------------------------- #
def elliott_wave(pivots: list[dict]) -> dict[str, Any]:
    """A *working* impulse count off the last alternating pivots, scored against
    the three hard Elliott rules. Deliberately low-confidence: it proposes a
    count for the LLM to sanity-check, it does not assert one."""
    if len(pivots) < 5:
        return {"detected": False, "note": "insufficient pivots for a 5-wave count"}
    seq = pivots[-6:] if len(pivots) >= 6 else pivots[-5:]
    # require alternating kinds for a clean impulse skeleton
    kinds = [p["kind"] for p in seq]
    alternating = all(kinds[i] != kinds[i + 1] for i in range(len(kinds) - 1))
    if not alternating or len(seq) < 5:
        return {"detected": False, "note": "pivot sequence not cleanly alternating"}

    p = [x["price"] for x in seq[-5:]]  # five points -> waves 1..4 legs + projection
    bullish = p[1] > p[0]  # first leg up?
    # leg magnitudes
    w1 = abs(p[1] - p[0])
    w2 = abs(p[2] - p[1])
    w3 = abs(p[3] - p[2])
    w4 = abs(p[4] - p[3])
    rules = {
        "wave2_not_beyond_wave1_origin": (p[2] > p[0]) if bullish else (p[2] < p[0]),
        "wave3_not_shortest": w3 >= w1 or w3 >= w4,
        "wave4_no_overlap_wave1": (p[4] > p[1]) if bullish else (p[4] < p[1]),
    }
    passed = sum(bool(v) for v in rules.values())
    conf = "medium" if passed == 3 else "low" if passed == 2 else "none"
    # next move projection: wave 5 ~= wave 1 length from the wave-4 pivot
    proj = _round(p[4] + (w1 if bullish else -w1))
    return {
        "detected": passed >= 2,
        "interpretation": ("impulse_up_wave5_pending" if bullish else "impulse_down_wave5_pending"),
        "confidence": conf,
        "rules_check": rules,
        "rules_passed": f"{passed}/3",
        "wave5_projection": proj,
        "note": "heuristic working count; treat as a hypothesis, validate against flow/structure",
    }


# --------------------------------------------------------------------------- #
# consolidation
# --------------------------------------------------------------------------- #
def levels_to_watch(spot: float, levels: list[dict], ind: dict, fib: dict) -> dict[str, Any]:
    supports = [l for l in levels if l["kind"] == "support"][:3]
    resists = [l for l in levels if l["kind"] == "resistance"][:3]
    ma_levels = [
        {"name": k, "level": ind[k]} for k in ("sma50", "sma200", "ema21")
        if ind.get(k) is not None
    ]
    return {
        "spot": spot,
        "nearest_support": supports[0]["level"] if supports else None,
        "nearest_resistance": resists[0]["level"] if resists else None,
        "supports": supports,
        "resistances": resists,
        "moving_averages": ma_levels,
        "fib_levels": fib.get("retracements") if fib.get("available") else None,
    }


def suggest_stops(spot: float, atr: float | None) -> dict[str, Any]:
    if not atr:
        return {"available": False}
    return {
        "available": True,
        "atr": _round(atr),
        "long_stop_1atr": _round(spot - atr),
        "long_stop_1_5atr": _round(spot - 1.5 * atr),
        "short_stop_1atr": _round(spot + atr),
        "short_stop_1_5atr": _round(spot + 1.5 * atr),
    }


# --------------------------------------------------------------------------- #
# orchestration
# --------------------------------------------------------------------------- #
def analyze(ticker: str, as_of: str, lookback_days: int = 540) -> dict[str, Any]:
    res: OHLCResult = load_ohlc(ticker, as_of, lookback_days)
    if not res.available:
        return {
            "available": False, "ticker": ticker.upper(), "as_of": as_of,
            "source": res.source, "note": res.note,
            "remedy": "install/enable yfinance network access, or ensure the UW "
                      "Stock Screener parquet covers this ticker/date.",
        }

    df = res.df
    ind = compute_indicators(df)
    pivots = find_pivots(df)
    spot = ind["spot"]
    levels = cluster_levels(pivots, spot)
    trend = trend_state(df, pivots)
    fib = fibonacci(df)
    atr = ind.get("atr14")

    patterns = {
        "flag": detect_flag(df, atr),
        "head_shoulders": detect_head_shoulders(pivots, spot),
        "double": detect_double(pivots, spot),
        "triangle": detect_triangle(pivots),
        "cup_handle": detect_cup_handle(df),
        "elliott_wave": elliott_wave(pivots),
    }
    detected = [
        {"pattern": k, **v} for k, v in patterns.items()
        if v.get("detected")
    ]

    return {
        "available": True,
        "ticker": ticker.upper(),
        "as_of": as_of,
        "source": res.source,
        "source_note": res.note,
        "indicators": ind,
        "trend": trend,
        "recent_pivots": pivots[-8:],
        "support_resistance": levels[:8],
        "fibonacci": fib,
        "patterns": patterns,
        "patterns_detected": detected,
        "levels_to_watch": levels_to_watch(spot, levels, ind, fib),
        "stops": suggest_stops(spot, atr),
    }


def main() -> None:
    ap = argparse.ArgumentParser(description="Chart/technical/pattern engine for the trade-plan skill")
    ap.add_argument("--ticker", required=True)
    ap.add_argument("--date", required=True, help="as-of date YYYY-MM-DD (look-ahead safe)")
    ap.add_argument("--lookback", type=int, default=540, help="calendar days of history to load")
    ap.add_argument("--json", action="store_true", help="(default) emit JSON")
    args = ap.parse_args()
    try:
        out = analyze(args.ticker, args.date, args.lookback)
    except Exception as e:  # never crash the caller; surface as structured error
        out = {"available": False, "ticker": args.ticker.upper(), "as_of": args.date,
               "error": f"{type(e).__name__}: {e}"}
    print(json.dumps(out, indent=2))
    sys.exit(0)


if __name__ == "__main__":
    main()
