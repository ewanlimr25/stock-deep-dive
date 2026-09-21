# Phase 5 — Historical Context & VRP

**Ticker:** SMR
**As-of date:** 2026-06-16
**Generated:** 2026-06-17T12:02:08Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-4-structure.md

## Summary

The multi-week context **confirms the bearish trend but warns the bearish *trade*
has been losing.** SMR is in a clear downtrend (**−16.8% over 30d, $11.88→$9.89, 20
bearish vs 10 bullish days**), down **−82.78% from its 52-week high** and only
+11.75% above its 52-week low — a falling knife near support. Vol is **cheap for
the name** (`iv_percentile=0`, `iv_zscore=−1.45`, LOW_IV) and **realized vol (307%)
is 3× implied (92%)** → **VRP −2.15, a PREMIUM-BUYING regime** (favour debit/long
options, not credit). GEX has been **stably long-gamma with zero regime flips in
30d** (range-bound). BUT the **`bearish_flow` signal-backtest win-rate is 28.6%**
(N=7, market-wide, in-sample, avg forward move **+1.66%**) — historically this
setup has gone the *wrong* way recently. Net: trend-bearish, but **edge-positive
conviction on the short is LOW** given the win-rate, the 52-week-low proximity, and
the 18% short float.

## Key signals

- **IV cheap for the name:** `iv_percentile=0`, `iv_zscore=−1.45`, `regime=LOW_IV`
  (current iv30d 92.2%, but 0th pctile of its own 1y) [HIST:iv_percentile_zscore].
- **Premium-BUYING regime:** `vrp=−2.1453`, realized_vol **3.067 (307%)** vs iv30d
  0.9217 → "Vol cheap vs realised — favour premium buying" [HIST:vrp].
- **Confirmed downtrend:** `price_change 11.88→9.89` (−16.8%), `bearish_days 20 /
  bullish_days 10`, iv_rank 46→27, `flow_direction_latest=bearish` [HIST:trend].
- **Bearish signal historically loses:** `signal-backtest bearish_flow win_rate
  28.6%`, `total_signals=7`, avg_move +1.66% (in-sample, market-wide)
  [HIST:signal_backtest].
- **Severe long-term breakdown (advisory):** −82.78% from 52W high $57.42, −30.2%
  YTD, below SMA20/50/200 (−52.8% vs SMA200), RSI 42, +11.75% off 52W low $8.85
  [HIST:52w_proximity fz][HIST:rsi fz].

## Detailed findings

### IV regime (percentile + z-score + VRP) — [HIST:iv_percentile_zscore][HIST:vrp]

- `current_iv30d=0.9217` (92.2% annualized — high in absolute terms, typical for
  SMR), but `iv_percentile=0` (bottom of its trailing range), `iv_zscore=−1.45`,
  `regime=LOW_IV`, `dates_used=46` (gap-aware; fewer than 252 calendar days).
- VRP: `realised_vol=3.067` (≈307%) vs `iv30d=0.9217` → `vrp=−2.1453`,
  `regime=PREMIUM_BUYING`. **Options are cheap relative to how much the stock
  actually moves** → phase-9 should favour **debit/long-premium** structures (long
  puts for the bearish lean), not credit selling.

### Cumulative premium flow (90d) — [HIST:cumulative_premium_flow]

`cumulative_bullish=136,665,576` vs `cumulative_bearish=141,847,407` →
**net_flow=−$5,181,831 (net bearish)**, `trend_direction=MIXED`. Over **47 actual
sessions** (the 90-day request spans the **03-28→04-24 gap**; `dates_covered` runs
03-13…06-16). A ~4% bearish tilt across the quarter — persistent but not decisive.

### P/C ratio z-score — [HIST:pc_ratio_zscore]

`current_pc_ratio=0.2626` vs `mean=0.3825`, `std=0.1639` → `zscore=−0.731`,
`extreme=NORMAL`. Today is more call-heavy than its 20-day norm but **not a
sentiment extreme** — no contrarian P/C signal.

### GEX time series (regime stability) — [HIST:gex_time_series]

`regime_flip_dates=null` — **no flips in 30 days**. ZGL hovered $2.4–5.5 (well
below spot), regime POSITIVE throughout; spot chopped $9.41–$10.8. The long-gamma /
range-bound regime (phase-4) is **stable, not transitioning** — supports a
range read over a trend-acceleration read near-term.

### OI trend (30d) — [HIST:oi_trend]

`overall_trend=BUILDING`, `consecutive_build_days=30`, `total_net_oi_change=
+611,969` contracts. **OI built every session for 30 days** — sustained accretion
*during* the price decline. Consistent with the phase-3 call-OI overwrite/
speculation stack growing into the downtrend (not capitulation/closeout).

### Multi-day trend table (30d, 2026-05-05→06-16; post-gap, contiguous) — [HIST:trend]

`price_change 11.88→9.89`, `iv_rank_change 46.04→26.68`, bullish 10 / bearish 20,
`flow_direction_latest=bearish`. Sample (early-window): 05-06 $13.52 → 05-18 $10.48
→ 06-16 $9.89 — a steady grind lower with IV bleeding out. Window does **not** cross
the gap (gap precedes 05-05).

### Price context (`fz`, advisory cross-check) — [HIST:rsi fz][HIST:52w_proximity fz]

| Metric | Value | Read |
|--------|-------|------|
| RSI(14) | 42.25 | neutral, **not yet oversold** (room lower) |
| vs SMA20 / SMA50 | −11.69% / −13.84% | below short/medium trend |
| vs SMA200 | **−52.84%** | deep long-term downtrend |
| Perf YTD / Month | −30.20% / −11.93% | sustained weakness |
| 52W High | $57.42 → **−82.78%** | severe drawdown from highs |
| 52W Low | $8.85 → **+11.75%** | near support / bounce zone |

Independent EOD confirmation of the downtrend — **and** a flag that price sits just
above its 52-week low with RSI not oversold: a zone where short-covering bounces
(18% short float) are most violent. Advisory; not in the Kelly `p`.

### Signal backtest (current signal's edge) — [HIST:signal_backtest]

`signal_type=bearish_flow`, `win_rate=28.6%`, `total_signals=7`, `avg_move_pct=
+1.66%`. Market-wide (signals were ADBE/UNH/MO/IBIT/ALB/SLV/MSFT — **not SMR**),
last-5-trading-day, **in-sample** (`methodology_notes`: "not a robust live edge").
**Below the 0.45 floor → downgrade conviction on the short.** Re-ran once; result
stable (not the empty stub). N=7 is small → low confidence; phase-9 applies the
N-conditional cap and will lean on the conviction bin.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|------------------|--------------------------|-----------|
| `uw historical iv-percentile-zscore --symbol SMR --lookback-days 252` | iv_percentile=0, z=−1.45 ← top-level; `dates_used=46` | 46 sess |
| `uw historical vrp --symbol SMR --realised-window-days 30` | vrp=−2.1453, realised=3.067 ← `.vrp/.realised_vol` | 30d |
| `uw historical cumulative-premium-flow --symbol SMR --days 90` | net_flow=−5,181,831 ← `.net_flow`; 47 dates | 47 sess |
| `uw historical pc-ratio-zscore --symbol SMR --lookback-days 20` | z=−0.731, NORMAL ← `.zscore/.extreme` | 20d |
| `uw historical gex-time-series --symbol SMR --days 30 --dte-max 45` | regime_flip_dates=null ← top-level; 30 traj pts | 30 sess |
| `uw historical oi-trend --symbol SMR --days 30 --top-n 10` | BUILDING, +611,969 ← `.overall_trend/.total_net_oi_change` | 30 sess |
| `uw historical trend --symbol SMR --days 30` | 11.88→9.89, 20 bearish days ← `.price_change/.bearish_days` | 30 sess |
| `uw historical signal-backtest --signal-type bearish_flow --lookback-days 5 --top-n 20` | win_rate=28.6%, n=7 ← top-level | 7 signals |
| `fz quote SMR --agent` | RSI 42.25, −82.78% vs 52W high ← `.fundamentals` | EOD |

## Tool errors

(none — all reads jq-validated. Note: `trend` daily_data is newest-first, so the
`[-10:]` tail shown is the *oldest* 10 sessions; headline aggregates used. GEX
`time_series` is under `.trajectory[]`, not `.results[]` — adjusted.)

## DATA NOTE / CORRECTION

All trailing tools anchor to the **latest available date = 2026-06-16** (== our
as-of), so this run is reproducible today; a later re-run after a new session lands
would shift every trailing read (IV z-score, win-rate, build-day count). Gap-aware:
90d cumulative-flow spans the 03-28→04-24 hole (47 real sessions); the 30d trend
window (05-05→06-16) is post-gap and contiguous. Session counts quoted from the
tools' own fields, not the calendar span.

## Verdict for downstream phases

- **Volatility regime:** **CHEAP** — IV at 0th pctile, realized 3× implied →
  **PREMIUM-BUYING** environment.
- **Premium environment:** **BUYING** (favour debit/long options; long puts for
  the bearish lean — credit selling is disfavoured here).
- **Conviction that today's signal is HISTORICALLY EDGE-POSITIVE:** **2/5.** The
  30d trend confirms bearish, but the `bearish_flow` win-rate (28.6%) is
  edge-negative, the stock sits at its 52W-low bounce zone, and 18% short float +
  premium-buying regime raise squeeze risk.
- **Three datapoints:** IV %ile **0**; VRP **−2.15** (realized 307% vs IV 92%);
  signal win-rate **28.6%** (N=7).
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:              bearish_flow
  signal_backtest_win_rate:  0.286
  win_rate_n:                7
  win_rate_source:           backtest   # market-wide base rate, in-sample, small N
  ```
- **Open questions:** Does the macro/sector regime (phase-6) explain the steady
  bleed, or is it idiosyncratic? Do fundamentals (phase-7b) justify a falling knife
  vs a value/squeeze bounce? How crowded is the short and what's the borrow
  (phase-7c) — the single biggest risk to a fresh short here?
