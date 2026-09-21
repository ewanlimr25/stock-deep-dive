# Phase 5 — Historical Context & VRP

**Ticker:** OKLO
**As-of date:** 2026-07-17
**Generated:** 2026-07-18T00:00:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-4-structure.md

## Summary

History **reinforces the bearish thesis and reframes the "bullish" flow tag as noise**.
OKLO is in a decisive **−37% downtrend over the last 30 sessions ($65.39 → $41.11)**, with
a ~10% gap-down from **$46 → $41 on 2026-07-16** that dropped it into — and kept it in — a
**persistent FULLY_NEGATIVE (short-gamma) GEX regime** all week. The `bearish_flow` signal
backtests **100% win (n=10, avg move −5.22%)** market-wide over the trailing window. The
telling divergence: **20 of the last 30 days were flow-tagged "bullish" yet price fell 37%**
— the bullish-flow read has been consistently wrong for this name, which is exactly why
phase-0.5 capped today's marginal +$398K net-bullish print. The one caution for structure
selection: IV is **rich (VRP +0.28, PREMIUM_SELLING)** — express the bearish view with
spreads/credit, not expensive naked long puts.

## Key signals

- **−37% / 30-session downtrend**: price_change `65.39 → 41.11`, 06-04→07-17 [HIST:trend]
- **Gap-down + short-gamma lock**: spot $45.43 (07-15) → $41.36 (07-16), regime
  FULLY_NEGATIVE every session 07-13→07-17, total_gex −9.47M on 07-16 [HIST:gex_time_series]
- **`bearish_flow` backtest 100% win, n=10, avg −5.22%** — edge-positive but small-N,
  market-wide base rate [HIST:signal_backtest]
- **VRP +0.28 → PREMIUM_SELLING** (IV30d 97.5% vs RV30 69.5%): "favour premium selling"
  [HIST:vrp]
- **Flow-tag unreliable here**: 20 bullish / 10 bearish flow-days over 30, price still −37%
  → discount raw net-flow sign [HIST:trend]

## Detailed findings

### IV regime — [HIST:iv_percentile_zscore / vrp]

- current_iv30d **0.9747 (97.5%)**, iv_percentile **76.1** (elevated, not extreme),
  iv_zscore 0.61, regime NORMAL.
- VRP **+0.2799** (IV30d 0.9747 − RV30 0.6948), regime **PREMIUM_SELLING** —
  "Options pricing more vol than realised — favour premium selling." Long naked options
  are over-paying ~28 vol points of premium.

### Cumulative premium flow (90d, 68 sessions) — [HIST:cumulative_premium_flow]

cum_bull **$924.2M** vs cum_bear **$876.5M** → net_flow **+$47.7M**, trend **MIXED**. Over
the quarter the net is *mildly* bullish but non-directional — **not** a stealth-accumulation
signal, and it coexists with a −37% price move (premium tagging ≠ price outcome here).

### P/C ratio z-score (20d) — [HIST:pc_ratio_zscore]

current_pc 0.7314, mean 0.6509, z **0.171**, extreme **NORMAL**. No sentiment extreme →
no contrarian mean-reversion trigger on this axis.

### GEX time series (30d) — [HIST:gex_time_series]

2 regime flips earlier in the window (06-18 → POSITIVE at spot $60.3, 06-22 → back NEGATIVE).
Recent trajectory is **FULLY_NEGATIVE every session** with price cascading down:

| Date | spot | regime | total_gex |
|---|---|---|---|
| 07-13 | 45.56 | FULLY_NEGATIVE | −4.70M |
| 07-15 | 45.43 | FULLY_NEGATIVE | −4.80M |
| **07-16** | **41.36** | FULLY_NEGATIVE | **−9.47M** |
| 07-17 | 41.41 | FULLY_NEGATIVE | −8.99M |

The gap from ~$46 to ~$41 (07-15→07-16) confirms the phase-2 **$45.5–$46 DP shelf was
distribution / a top**, not support. Short-gamma is *deepening* as price falls — downside
amplification is the live risk.

### OI trend (30d) — [HIST:oi_trend]

overall_trend **BUILDING**, consecutive_build_days 30, total_net_oi_change **+475,772**.
OI has grown steadily for a month (the LEAP-call base + accumulating put hedges of phase-3).
Building OI into a falling price = positions being *added* on the way down, not capitulation.

### Multi-day trend table — [HIST:trend]

- days_analyzed 30, range 2026-06-04 → 2026-07-17.
- **price_change 65.39 → 41.11 (−37.1%)**; iv_rank_change 32.20 → 32.66 (flat).
- bullish_days **20** / bearish_days **10**; flow_direction_latest "bullish".
- **Divergence flagged:** 2:1 bullish-flow-days yet a 37% decline → for OKLO the net-flow
  sign has NOT predicted price. This is the empirical basis for discounting today's
  +$398K net-bullish tag (phase-0.5 / phase-1).

### Price context (`fz` advisory)

`fz quote OKLO` returned the same degraded 14-field block as phase-0 — **RSI / SMA20-50-200
/ Perf YTD / 52W all null**. The independent EOD cross-check is **unavailable this run**;
skipped per skill guidance (advisory only, never enters Kelly `p`).

### Signal backtest — [HIST:signal_backtest]

`signal-type bearish_flow, lookback 5d`: **win_rate 100.0%, total_signals 10, avg_move_pct
−5.22%** (truncated_signals 10). Edge-positive for the bearish view; **market-wide base
rate, not OKLO-specific, and small N (10)** → phase-9 must apply the N-conditional Kelly cap.

## Tool calls (audit trail)

| Command | Key value(s) ← `jq` path | N/notes |
|---|---|---|
| `historical iv-percentile-zscore --lookback 252` | pctile 76.1, iv30d 0.9747 ← `.iv_percentile` | dates_used 67 |
| `historical vrp --realised 30` | VRP +0.28, PREMIUM_SELLING ← `.vrp/.regime` | RV30 0.6948 |
| `historical cumulative-premium-flow --days 90` | net +$47.7M MIXED ← `.net_flow` | 68 sessions |
| `historical pc-ratio-zscore --lookback 20` | z 0.171 NORMAL ← `.zscore` | |
| `historical gex-time-series --days 30` | FULLY_NEGATIVE, gap 07-16 ← `.trajectory` | 2 flips |
| `historical oi-trend --days 30` | BUILDING +475,772 ← `.overall_trend` | 30 build days |
| `historical trend --days 30` | −37% 65.39→41.11 ← `.price_change` | 20b/10br |
| `historical signal-backtest bearish_flow` | 100% win, n=10, −5.22% ← `.win_rate/.total_signals` | market-wide |

## Tool errors

None fatal. `fz` price-context fields null (degraded quote) — advisory cross-check skipped.
Trailing-anchor caveat: all no-`--date` commands anchor to latest available date (2026-07-17,
= as-of), so this run is as-of-consistent; a re-run after a new session would shift them.

## DATA NOTE / CORRECTION

Gap-awareness: the 90d/252d lookbacks cross the known 2026-03-28→04-24 hole; quoted the
tools' **own session counts** (dates_used 67, cum-flow 68 sessions) rather than the calendar
span, and did not annualize across the gap. The recent 30-session window (06-04→07-17) is
contiguous and gap-free.

## Verdict for downstream

- **Volatility regime:** IV **rich** (76th pctile, VRP +0.28) → **premium-SELLING**
  environment. Favor debit *spreads* / credit structures over naked long premium.
- **Historical edge on today's signal:** **EDGE-POSITIVE for bearish** — 37% established
  downtrend, deepening short-gamma, bearish_flow 100%/n10, and a flow-tag that has failed to
  the upside all month.
- **Conviction:** 4 / 5 that the setup is historically edge-positive on the **bearish** side
  (tempered from 5 by small backtest N and the mildly-bullish 90d cumulative flow).
- **Three specific datapoints:** IV %ile **76.1**; VRP **+0.28**; bearish_flow win-rate
  **1.00 (n=10, avg −5.22%)**.
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:     bearish_flow
  signal_backtest_win_rate: 1.00
  win_rate_n:       10
  win_rate_source:  backtest      # market-wide base rate, NOT OKLO-specific; small N → cap p
  ```
- **Open questions:** Is the 37% drop from $65 exhausted (mean-reversion toward the $47–50
  max-pain magnet) or does the deepening short-gamma carry it through the $35 put wall? Does
  phase-6 macro / theme rotation explain the collapse (nuclear-theme rotation into CCJ/GEV
  per phase-0.5)? Is the 08-10 earnings a floor-catalyst risk to a short?
