# Phase 5 — Historical Context & VRP

**Ticker:** NVDA
**As-of date:** 2026-05-27
**Generated:** 2026-05-28T02:38:00Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md, phase-1-flow.md, phase-4-structure.md

## Summary

NVDA's bearish-flow regime is **real and 13 sessions deep, but historically
edge-poor**. The 30-day daily-trend table shows price topped at **$235.74 on
2026-05-14** and has rolled over to $212.60 today (−9.8% peak-to-now), with IV
rank halving (76.6 → 30.5) and `net_flow` negative in 11 of the last 13
sessions. Yet the `signal-backtest` for `bearish_flow` returns a **37.5% directional
win-rate (N=8 across universe)** — below the 45% downgrade threshold. The
NVDA-specific subsample within that backtest is **2/2 forward-down** (5/22 → −1.27%
in 5 sessions; 5/21 → −3.15% in 5 sessions), but N=2 is anecdotal. IV percentile
**25 (1y), VRP −0.86%, FAIR** — vol is cheap with realized just above IV,
favouring premium-buying (debit) structures. 90-day cumulative flow is
near-balanced (bearish $22.14B vs bullish $21.82B, +$318M bearish tilt) — *not*
a 90d directional campaign, the conviction is purely on the recent 13-session
rollover. GEX regime has been **POSITIVE every session in the trajectory except
2026-03-24** and `total_gex` has decayed from a $2.02B peak (2026-05-08) to
$192.9M today (10× compression) — the long-gamma cushion is shrinking.

## Key signals

- **IV percentile 25 / z-score −1.018 / regime NORMAL** [HIST:iv_percentile_zscore]
  — vol is cheap; debit structures favoured.
- **VRP −0.86% (IV30 0.375, RV30 0.384, regime FAIR)** [HIST:vrp] — IV slightly
  cheap to realized; mild premium-buying tilt.
- **30d trend: 16 bearish days / 14 bullish days; net_flow negative 11/13 most
  recent sessions** [HIST:trend].
- **Total GEX decay: $2.02B (5/08) → $192.9M (5/27) = 10× compression**
  [HIST:gex_time_series] — dealer long-gamma cushion eroding.
- **Backtest: `bearish_flow` win_rate 37.5% (N=8 universe), 100% (N=2 NVDA-only)**
  [HIST:signal_backtest] — universe edge weak, NVDA-specific anecdotal.

## Detailed findings

### IV regime (percentile + z-score + VRP) — [HIST:iv_percentile_zscore, vrp]

| Metric | Value | Read |
|--------|------:|------|
| current_iv30d | 0.3754 | (= today's screener iv30d) |
| iv_percentile (1y) | 25 | bottom quartile |
| iv_zscore (1y) | −1.018 | mildly low |
| regime | NORMAL | not extreme |
| realised_vol_30d | 0.3840 | slightly above IV |
| VRP | **−0.0086** | **FAIR / cheap** |

Vol is cheap with realized just above IV — small but real edge to **buy** premium
(debit structures) over selling it (credit structures). Latest-anchor caveat: this
read updates to whatever the *latest* available date is on the next run.

### 90-day cumulative premium flow — [HIST:cumulative_premium_flow]

| Metric | Value |
|--------|------:|
| cumulative_bullish | $21.82B |
| cumulative_bearish | $22.14B |
| net (bearish − bullish) | +$318M |

Functionally balanced over 90 sessions. The bearish lean of the recent 13
sessions has **not yet inverted the 90-day base** — i.e. today's bearish tilt is
not the tail of a long stealth-bearish campaign, it's a fresh-ish rollover from a
mid-May peak.

### P/C ratio z-score — [HIST:pc_ratio_zscore]

| Metric | Value |
|--------|------:|
| current_pc_ratio | 0.3962 |
| mean_pc_ratio (20d) | 0.4220 |
| zscore | −0.476 |
| extreme | **NORMAL** |

No sentiment extreme; P/C is just below its 20-day mean.

### GEX time series (30d, dte_max 45) — [HIST:gex_time_series]

Selected (gap-aware: 2 segments, 2026-03-18→03-27 then 2026-04-27→05-27):

| date | spot | ZGL | regime | total_gex |
|------|-----:|----:|--------|----------:|
| 2026-05-08 | 215.18 | 69.42 | POS | **+$2,020.3M** (peak) |
| 2026-05-14 | 235.71 | 56.84 | POS | +$788.2M |
| 2026-05-21 | 219.66 |  7.88 | POS | +$366.5M |
| 2026-05-22 | 215.45 | 136.71 | POS | +$132.8M |
| 2026-05-26 | 214.30 | 69.33 | POS | +$413.3M |
| **2026-05-27** | **212.56** | **138.94** | **POS** | **+$192.9M** |

Regime has been **POSITIVE on every session in the trajectory except 2026-03-24**
(brief NEGATIVE flip on a spot–ZGL crossover, reversed next day). The structural
read: dealers have been long-gamma throughout, but the cushion has **compressed
10× since 2026-05-08**, and ZGL has climbed from low double-digits (5/19: $16,
5/21: $7.88) to $138.94 today — the ZGL/spot gap has *narrowed*. The dealer
floor is rising.

### OI trend — [HIST:oi_trend]

- `consecutive_build_days`: **30** — uninterrupted daily net-OI build for 30
  sessions (in the available window). Today's net OI change +555,751 with 1,602
  contracts seeing increases vs 683 decreases. This is sustained buildup
  *somewhere* in the chain; the directional read is in phase-3 (3:1 bearish).

### Multi-day trend (selected, N=30 daily rows) — [HIST:trend]

| date | close | net_flow $M | iv30d | iv_rank | PCR |
|------|------:|------------:|------:|--------:|----:|
| 2026-05-27 | 212.60 | −66.3 | 0.375 | 30.5 | 0.396 |
| 2026-05-26 | 214.66 | −100.2 | 0.379 | 34.2 | 0.420 |
| 2026-05-22 | 215.33 | −97.0 | 0.371 | 27.3 | 0.470 |
| 2026-05-21 | 219.51 | **−189.7** | 0.385 | 34.2 | 0.432 |
| 2026-05-20 | 223.47 | +24.1 | 0.450 | 61.0 | 0.457 |
| 2026-05-15 | 225.49 | −42.6 | 0.490 | 76.7 | 0.460 |
| 2026-05-14 | **235.74** | +34.9 | 0.489 | 76.6 | 0.376 |
| 2026-05-13 | 225.83 | +71.5 | 0.483 | 74.2 | 0.386 |
| 2026-05-11 | 219.44 | +282.3 | 0.455 | 62.9 | 0.359 |
| 2026-05-06 | 207.83 | +112.1 | 0.457 | 61.8 | 0.292 |
| 2026-04-27 | 216.61 | +126.3 | 0.449 | 58.3 | 0.381 |
| 2026-03-27 | 167.52 | +8.5 | 0.394 | 21.4 | 0.913 |

Pattern: rally from $167 (3/27) → $235 (5/14) on positive net_flow, then 13-day
rollover with net_flow negative most days and IV halved.

### Price context (`fz`, advisory cross-check) — [HIST:rsi fz, HIST:52w_proximity fz]

| Metric | Value |
|--------|-------|
| Price | $212.60 |
| RSI (14) | 51.04 (neutral) |
| SMA20 | −0.95% (below — recent weakness) |
| SMA50 | +7.33% (above — uptrend intact) |
| SMA200 | +13.48% (above — long uptrend intact) |
| Perf YTD | +13.99% |
| Perf Week | −3.63% |
| Perf Month | −1.85% |
| 52W High | $236.54 (−10.12%) |
| 52W Low | $132.92 (+59.95%) |

The pullback is **modest in structural context** — NVDA is still above SMA50/200,
RSI is neutral, and the −10% drawdown from the May high is far from oversold.
Advisory only; not in Kelly p.

### Signal backtest — [HIST:signal_backtest]

`uw historical signal-backtest --signal-type bearish_flow --lookback-days 5 --top-n 20`

| Field | Value |
|-------|------:|
| N (total rows) | 8 |
| avg_move_pct (abs) | 1.84 |
| **down_count** | **3** |
| **down_rate (= win_rate for bearish signal)** | **37.5%** |
| methodology | "in-sample backtest — not a robust live edge" |

NVDA-specific (subset N=2): both signals (5/22, 5/21) forward 5d **down** −1.27%
and −3.15% → 2/2 = **100% NVDA-only** — but N=2 is anecdotal.

The universe `win_rate=0.375` is below the rubric's 0.45 downgrade threshold —
the bearish_flow signal has historically not paid out on average. Phase-9 sizing
must use **0.375** as Kelly `p` (with the N-conditional cap; N=8 is small).

## Tool calls (audit trail)

| Command | Result summary |
|---------|----------------|
| `uw historical iv-percentile-zscore --lookback-days 252` | pctile 25, z −1.018, NORMAL |
| `uw historical vrp --realised-window-days 30` | VRP −0.86%, FAIR |
| `uw historical cumulative-premium-flow --days 90` | bull $21.82B vs bear $22.14B (+318M bear) |
| `uw historical pc-ratio-zscore --lookback-days 20` | z −0.476, NORMAL |
| `uw historical gex-time-series --days 30 --dte-max 45` | regime POS 30/31; total_gex 10× decay |
| `uw historical oi-trend --days 30` | 30 consecutive build days; net +555,751 today |
| `uw historical trend --days 30` | 16 bearish/14 bullish; peak 5/14 $235.74 → 5/27 $212.60 |
| `uw historical signal-backtest --signal-type bearish_flow` | win_rate 0.375 (N=8); NVDA 2/2 |
| `fz quote NVDA --agent` | RSI 51, above SMA50/200, −10.1% from 52W high |

## Tool errors

(none — gap-aware: trend / GEX-trajectory honestly span 2 segments across the
2026-03-28→04-24 hole; line counts are *available* sessions, not calendar days)

## Verdict for downstream

- **Volatility regime:** CHEAP (IV pctile 25, VRP −0.86%) — premium-BUYING
  environment; debit structures preferred over credits.
- **Premium environment:** balanced 90d (no stealth campaign); 13-session
  bearish rollover is the dominant signal.
- **Conviction the signal is historically edge-positive:** **2/5** — universe
  win_rate 0.375 is below 0.45; NVDA-only N=2 is encouraging but anecdotal. The
  flow + structure are coherent (phases 1/3/4 all bearish) but the *backtested*
  edge is weak. Treat as low-conviction directional, high-quality vol setup.
- **Three specific data points:** IV pctile 25; VRP −0.86%; win_rate 0.375 (N=8).
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:              bearish_flow
  signal_backtest_win_rate:  0.375
  win_rate_n:                8
  win_rate_source:           backtest
  ```
- **Open questions:**
  - Why is the universe edge so weak on bearish_flow? Phase-6 / phase-7c may
    explain (e.g., bearish flow during a bullish-regime year fades on average).
  - Is NVDA's 2/2 recent down-only history coincidence or genuine
    ticker-specific edge? With N=2 we cannot tell — flag for calibration.
