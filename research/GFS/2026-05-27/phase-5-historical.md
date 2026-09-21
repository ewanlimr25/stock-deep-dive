# Phase 5 — Historical Context & VRP

**Ticker:** GFS
**As-of date:** 2026-05-27
**Generated:** 2026-05-28T00:00:00Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md, phase-1-flow.md, phase-4-structure.md

## Summary

Today's tape sits at the **top of a violent multi-month parabola**: GFS is
**+91% over the available window** ($42.47 → $81.11), **+132.7% YTD**, and **+87.5%
above its 200-DMA** — extreme extension, with the −9.7% as-of day the first crack.
Vol is **HIGH** (IV30d 82.3%, 81st pctile of available history) but **VRP is FAIR
(+3.4 vol pts)** because realized vol (78.9%) caught up to implied during the run —
so there is **no clean premium edge from VRP alone today**, though vol-mean-reversion
favors sellers *if* the stock calms (it would re-richen IV vs a falling realized).
Sentiment is **NOT extreme** (P/C z −0.33, NORMAL). Trailing 90-day flow was
**BULLISH** (+$15.7M net) and OI has been **building 30 sessions straight** — the
run's footprint — but the latest flow direction is **bearish** and phase-3 showed the
near-term build is defensive. The `bearish_flow` backtest is **barely edge-positive
(58.3%, n=12, in-sample, market-wide)** — low confidence. Net: the dominant
historical fact is **extension/mean-reversion gravity**, not a clean directional
edge.

## Key signals

- **+91% over window** ($42.47→$81.11), IV rank 46.6→79.1; latest flow **bearish**
  `[HIST:trend]`.
- **+132.7% YTD, +87.5% vs 200-DMA, +36.5% vs 50-DMA, RSI 62.8** (cooled by the
  drop), 12.2% below the **$92.55 52-wk high** `[HIST:52w_proximity fz]`, `[HIST:rsi fz]`.
- **IV HIGH but VRP FAIR**: IV30d 82.3% (81st pctile, z +1.15) vs realized 78.9% →
  vrp +0.034, "no clear edge from VRP alone" `[HIST:iv_percentile_zscore]`, `[HIST:vrp]`.
- **90d cumulative flow BULLISH** +$15.7M (bull $64.8M / bear $49.1M) `[HIST:cumulative_premium_flow]`.
- **OI BUILDING** 30 consecutive sessions, net +83,365 `[HIST:oi_trend]`.
- **P/C NORMAL** (z −0.33) — no sentiment extreme to fade `[HIST:pc_ratio_zscore]`.
- `bearish_flow` backtest **win 58.3%, n=12**, in-sample, market-wide `[HIST:signal_backtest]`.

## Detailed findings

### IV regime `[HIST:iv_percentile_zscore]`, `[HIST:vrp]`

current IV30d **82.3%**, iv_percentile **81.25** (regime HIGH_IV), z-score **+1.15**.
VRP: iv30d 82.3% − realized 78.9% = **+3.4 vol pts → regime FAIR**. The high IV is
*earned* by the parabola's realized vol, so options aren't egregiously rich **yet** —
the premium-selling case rests on realized vol falling faster than implied as the
move exhausts (then VRP widens). **Caveat:** `dates_used=32`, not the requested 252
— this "1y percentile" is really a ~6-week percentile (gap-shortened); treat the
absolute number as directional, not precise.

### Cumulative premium flow (90d) `[HIST:cumulative_premium_flow]`

cumulative_bullish $64.77M, cumulative_bearish $49.05M, **net +$15.72M, BULLISH**.
The trailing options bias was bullish — but this is the run-up footprint and is
latest-anchored (spans the 03-28→04-24 gap). Modest in size relative to the move.

### P/C ratio z-score `[HIST:pc_ratio_zscore]`

current 0.3346 vs 20d mean 0.7029 (std 1.1259), z **−0.327**, extreme **NORMAL**.
Call-heavier than average but well inside one std — **no contrarian sentiment extreme**.

### GEX time series

`gex-time-series --days 30` returned **0 rows** (empty `time_series`) — see Tool
errors. Cannot confirm historical ZGL regime-flip dates; rely on phase-4's
point-in-time NEGATIVE/short-gamma read.

### OI trend `[HIST:oi_trend]`

overall_trend **BUILDING**, consecutive_build_days **30**, total_net_oi_change
**+83,365**. Sustained OI accretion through the run. Note: building OI during a
+91% advance is expected and is *direction-agnostic* — phase-3 showed the *recent*
build is mixed (near-term calls written, LEAP calls bought), so do not read this as
clean bullish accumulation.

### Multi-day trend `[HIST:trend]`

date_range 2026-03-18→2026-05-27, **30 sessions** (NOT calendar days — the
03-28→04-24 gap is excluded). bearish_days 16 vs bullish_days 14 (slight bearish
day-count edge), iv_rank 46.6→79.1, **price $42.47→$81.11 (+91%)**,
flow_direction_latest **bearish**.

### Price context (`fz`, advisory) `[HIST:rsi fz]`, `[HIST:52w_proximity fz]`

| metric | value | read |
|--------|------:|------|
| RSI(14) | **62.8** | elevated, **not** extreme (drop relieved it) |
| vs SMA20 | +9.78% | extended |
| vs SMA50 | +36.5% | very extended |
| vs SMA200 | **+87.5%** | **extreme** (parabola) |
| Perf YTD | **+132.7%** | more than doubled |
| Perf Month | +36.6% | |
| Perf Week | +14.8% | still green on the week post-drop |
| 52W High | **$92.55 (−12.2%)** | = the $91–92 DP supply zone (phase-2) |
| 52W Low | $31.51 (+157.9%) | nearly tripled off the low |

The +87.5% extension above the 200-DMA is the headline: **mean-reversion gravity is
strong**. RSI 62.8 is the one moderating note — the setup is "extended + first crack,"
not "RSI-85 blow-off top," so further mean-reversion is *plausible* but not
mechanically forced. The independent `fz` $92.55 high corroborates phase-2's $91–92
supply wall.

### Signal backtest `[HIST:signal_backtest]`

`bearish_flow`, lookback 5 trading days: **win_rate 58.3%, total_signals 12**,
avg_move 0.04. Market-wide (GFS-specific rows: 0), **in-sample** (tool's own note:
"not a robust live edge"). n=12 is borderline; treat as low-confidence. This is the
Kelly `p` candidate, subject to phase-9's N-conditional cap.

## Tool calls (audit trail)

| Command | Result |
|---------|--------|
| `uw historical iv-percentile-zscore --lookback-days 252` | IV %ile 81.25, HIGH_IV, z+1.15 (dates_used 32) |
| `uw historical vrp --realised-window-days 30` | vrp +0.034, FAIR |
| `uw historical pc-ratio-zscore --lookback-days 20` | z −0.33, NORMAL |
| `uw historical cumulative-premium-flow --days 90` | net +$15.7M, BULLISH |
| `uw historical gex-time-series --days 30` | **0 rows** (empty) |
| `uw historical oi-trend --days 30` | BUILDING, 30 build-days, +83,365 |
| `uw historical trend --days 30` | +91% price, latest flow bearish, 16 bear/14 bull days |
| `uw historical signal-backtest --signal-type bearish_flow` | 58.3% win, n=12, in-sample |
| `fz quote GFS` | RSI 62.8, +87.5% vs 200-DMA, +132.7% YTD, $92.55 52wH |

## Tool errors

- `uw historical gex-time-series --symbol GFS --days 30` → returned `days_analyzed:
  30` but **empty `time_series`** (0 rows). No error string; likely no per-day GEX
  reconstruction for this name. Cannot verify historical regime flips — flagged as a
  data-quality gap, not trusted-as-zero.
- **Gap caveat (MANDATORY):** all `--days`/`--lookback-days` windows cross the
  21-session hole (2026-03-28→04-24). IV-percentile used only **32 sessions**; trend
  "30 days" = 30 *sessions* over a 2.5-month calendar span. Do not annualize.
- **Latest-anchor caveat:** trailing reads (iv-percentile, pc-z, oi-trend,
  cumulative-flow, signal-backtest, vrp realized leg) anchor to the latest available
  date (2026-05-27 == as-of here, so valid this run, but not reproducible after a new
  session lands).

## Verdict for downstream

- **Volatility regime:** **RICH-but-earned** — IV HIGH (81st pctile) yet VRP FAIR
  (+3.4) because realized caught up. **No clean premium edge today**; the
  premium-selling case is *contingent* on realized vol falling as the move exhausts.
- **Premium environment:** mildly **premium-SELLING** when combined with phase-4's
  backwardation + complacent skew (sell front-month/near calls), but tempered — do
  not size a vol-sell on VRP alone.
- **Conviction that today's signal is HISTORICALLY EDGE-POSITIVE:** **3/5.** The
  bearish_flow backtest is only marginally positive and low-N; the *real* edge is the
  extreme extension (mean-reversion gravity) + phase-4 structure, not the flow itself.
- **Three datapoints:** IV %ile **81.25**; VRP **+0.034 (FAIR)**; bearish_flow win
  **58.3% (n=12)**.
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:               bearish_flow
  signal_backtest_win_rate:   0.583
  win_rate_n:                 12
  win_rate_source:            backtest
  ```
  (In-sample, market-wide, low N → phase-9 must apply the N-conditional shrink in
  `rubrics/sizing-rubric.md`; do not size on 0.583 at face value.)
- **Open questions:** Will realized vol actually fall (validating the premium-sell /
  vanna-selling thesis) or does a fresh catalyst sustain it? (phase-6, 7b). Does the
  +132% YTD / +87% above 200-DMA extension have a fundamental anchor (a real re-rate)
  or is it a momentum/squeeze melt-up vulnerable to a full retrace? (phase-7b/7c).
