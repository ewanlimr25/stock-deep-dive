# Phase 5 — Historical Context & VRP

**Ticker:** RKT
**As-of date:** 2026-07-17
**Generated:** 2026-07-19T19:48:00-04:00
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-4-structure.md

## Summary

History **undercuts the bearish-flow read and supports the constructive/range
thesis.** Over the trailing 30 sessions (2026-06-04 → 07-17) RKT **rose +9.9%
($13.23 → $14.54)** even though **18 of 30 were bearish-flow days** and cumulative
90-day premium flow is net-bearish (−$12.0M) — i.e. the bearish tape has coincided
with a *rising* stock, so bearish flow has been locally *wrong* (consistent with
phases 3–4: overwriting/hedging, not directional shorting). IV rank **doubled
(26.6 → 51.7)** and 1-year IV percentile is **89.6 (rich)** — but **VRP is only
+0.003 (regime FAIR)** because realized vol (0.69) is just as high, so there's no
clean premium-selling edge. Dealers held a **POSITIVE gamma regime for 30 straight
days with zero flips**, and **today is the first day total_gex went negative
(−$28.5M)** — ATM gamma compressing into the 07-30 earnings. OI is **BUILDING (4
consecutive build days, +552k net)**. The phase-1-matching `bearish_flow` backtest
prints 100% / N=10 — but it's a tiny, market-wide base rate that contradicts RKT's
own tape, so it should **not** anchor sizing.

## Key signals

- **Price +9.9% over 30 sessions despite 18/30 bearish-flow days** → bearish flow locally non-predictive `[HIST:trend]`
- **IV percentile 89.6 (rich, 1y) but VRP +0.003 / FAIR** → high vol is *earned*, not a sell-vol free lunch `[HIST:iv-percentile-zscore / vrp]`
- **30 consecutive POSITIVE-gamma days, 0 flips; total_gex first-ever-negative TODAY (−$28.5M)** → stable range regime now compressing at ATM into earnings `[HIST:gex-time-series]`
- **OI BUILDING — 4 consecutive build days, +551,973 net** → sustained structural buildup (the collar/overwrite + +45k Mar-27 $19C) `[HIST:oi-trend]`
- **P/C z-score +0.38 (not extreme), cumulative flow BEARISH −$12.0M / 68 sessions** → mild bearish tilt, no sentiment extreme `[HIST:pc-ratio-zscore / cumulative-premium-flow]`

## Detailed findings

### IV regime `[HIST:iv-percentile-zscore / vrp]`

- **1-year IV percentile: 89.55** (dates_used 67), current_iv30d **0.6943** → IV is
  in the top decile of its year → **rich by its own history** (pre-earnings + the
  backwardation from phase-4).
- **VRP = +0.0032, regime FAIR** (RV30 = 0.6911). IV30 ≈ RV30 → **no material vol
  risk premium**. The 89th-percentile IV is justified by equally-high realized vol,
  not mispricing. Implication: selling premium here isn't the free carry the IV
  percentile alone would suggest; and post-earnings the front-tenor IV will crush.

### Cumulative premium flow (90d) `[HIST:cumulative-premium-flow]`

- cumulative_bullish $108,440,655 vs cumulative_bearish $120,445,729 →
  **net_flow −$12,004,074**, `trend_direction: BEARISH`, over **68 sessions
  covered** (2026-06-04 → 07-17 densest). A modest, persistent bearish premium tilt —
  but see the trend section: it hasn't stopped price rising.

### P/C ratio z-score `[HIST:pc-ratio-zscore]`

- current P/C 0.5019, **z-score +0.376** → **not an extreme** (|z| < 2). No
  contrarian sentiment signal either way; positioning is unremarkable.

### GEX time series (30d) `[HIST:gex-time-series]`

- **Regime POSITIVE on all 30 sessions; `regime_flip_dates: null`** (spot never
  crossed ZGL, which sat steady ~$7–11, mostly ~$9.5). A durably long-gamma,
  range-suppressed month.
- total_gex trajectory: +$4.4M (06-04) → peak +$91M (06-18) → **−$28.5M (07-17,
  first negative of the window)**. Spot: $13.3 → peak $16.1 (07-01) → $14.57. The
  fresh ATM short-gamma pocket (phase-4) is a **new** development today, not a
  standing feature — gamma compressing into earnings.

### OI trend (30d) `[HIST:oi-trend]`

- `overall_trend: BUILDING`, **consecutive_build_days 4**, total_net_oi_change
  **+551,973**. Sustained accumulation of open interest (not a one-day spike, not
  decay) → structural positioning, matching phase-3's +45k Mar-27 $19C and the
  overwrite/collar builds.

### Multi-day trend table `[HIST:trend]`

| Metric (30d, 2026-06-04 → 07-17) | Value |
|---|---|
| price_change | **$13.23 → $14.54 (+9.9%)** |
| iv_rank_change | 26.58 → 51.66 (**doubled**) |
| bullish_days / bearish_days | **12 / 18** |
| flow_direction_latest | bearish |

The dissonance is the headline: **more bearish-flow days than bullish, yet price up
~10%.** Over this name's own recent history, bearish flow has been a *fade*, not a
signal — a strong caution against treating today's bearish tape as directional.

### Price context (`fz`)

**Unavailable** — `fz quote RKT` returns the reduced payload (no RSI/SMA/52W fields);
advisory cross-check skipped per phase-5 rule (`fz_available=yes` but fields absent).

### Signal backtest `[HIST:signal-backtest]`

- **`bearish_flow` (matches phase-1): win_rate 100.0%, total_signals 10** —
  market-wide base rate, **N=10 (small)**. It is *not* RKT-specific and directly
  conflicts with RKT's own +9.9% run under bearish flow. Use with the N-conditional
  cap; do not let it drive sizing.
- **`dark_pool_accumulation` (phase-2 dominant/reconciling signal): empty stub
  (`total_signals 0`, "no backtest results") on both the first call and the mandated
  re-run** → `win_rate_source = null` for the accumulation class.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows / N |
|---|---|---|
| `uw historical iv-percentile-zscore --symbol RKT --lookback-days 252` | pctile 89.55, iv30d 0.6943 ← `.iv_percentile` | 67 dates |
| `uw historical vrp --symbol RKT --realised-window-days 30` | vrp +0.0032, FAIR, RV30 0.6911 ← `.vrp`/`.regime` | 1 |
| `uw historical cumulative-premium-flow --symbol RKT --days 90` | net −$12.0M, BEARISH ← `.cumulative_bullish−.cumulative_bearish` | 68 |
| `uw historical pc-ratio-zscore --symbol RKT --lookback-days 20` | z +0.376, not extreme ← `.z_score` | 20 |
| `uw historical gex-time-series --symbol RKT --days 30 --dte-max 45` | 30d all POSITIVE, 0 flips; 07-17 total_gex −28.5M ← `.trajectory[]` | 30 |
| `uw historical oi-trend --symbol RKT --days 30` | BUILDING, 4 build days, +551,973 ← `.overall_trend`/`.consecutive_build_days` | 30 |
| `uw historical trend --symbol RKT --days 30` | +9.9% price, 12/18 bull/bear days ← `.price_change`/`.bearish_days` | 30 |
| `uw historical signal-backtest --signal-type bearish_flow --lookback-days 5` | 100.0%, N=10 ← `.win_rate`/`.total_signals` | mkt-wide |
| `uw historical signal-backtest --signal-type dark_pool_accumulation` (×2) | empty stub, N=0 ← `.note` | mkt-wide |

## Tool errors

None. `dark_pool_accumulation` empty stub confirmed on the mandated second run →
recorded `win_rate_source=null`, not treated as an error. `fz` price-context fields
absent (reduced payload) → advisory section skipped, not an error.

## DATA NOTE / CORRECTION

Gap-awareness: the 30-day window (2026-06-04 → 07-17) is **entirely after** the
known 2026-03-28→04-24 hole (phase-0), so no gap crosses this lookback — session
counts (`days_analyzed 30`, `dates_used 67`, `dates_covered 68`) are contiguous and
quoted from the tools' own counters, not calendar spans. **Latest-anchor caveat:**
all trailing commands anchor to latest available date = **2026-07-17** (= as-of), so
this read is reproducible today; a re-run after the 07-30 earnings session will shift
every trailing IV/z-score/win-rate. First-pass null fields (iv30, net_flow, etc.)
were key-name mismatches — re-read against the real keys (`.iv_percentile`,
`.cumulative_bullish`, `.trajectory`) before transcribing.

## Verdict for downstream phases

- **Volatility regime:** **RICH by percentile (89.6) but FAIRLY-priced (VRP ~0),
  front-loaded by earnings backwardation.** Neither a clean premium-buy nor
  premium-sell regime — the vol is real; the edge is in *structure/timing* around
  07-30, not in a static vol mispricing.
- **Premium environment:** mildly **premium-selling-favorable in the range** (long
  gamma, pin), but front-tenor IV is event-rich and will crush post-earnings — any
  short-vol must be out of the earnings tenor or defined-risk.
- **Conviction that TODAY's (bearish) signal is HISTORICALLY EDGE-POSITIVE: 2 / 5**
  — the market-wide `bearish_flow` backtest is nominally 100%/N=10, but RKT's own
  30-session tape shows bearish flow coinciding with a +9.9% rally, so the local
  edge of the bearish read is weak-to-negative. The durable, edge-positive facts are
  the **stable long-gamma range + building OI + underlying uptrend**.
- **Three specific datapoints:** IV %ile **89.6**; VRP **+0.003 (FAIR)**;
  `bearish_flow` win-rate **1.00 (N=10, market-wide, conflicts with RKT tape)**.
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:              bearish_flow          # matches phase-1 verdict
  signal_backtest_win_rate:  1.00                  # market-wide base rate
  win_rate_n:                10                    # small
  win_rate_source:           backtest              # but see caveat — market-wide, conflicts w/ RKT +9.9% tape
  ```
  Caveat for phase-9: this `p` is a **market-wide** base rate for the bearish_flow
  class, **not** RKT-specific, and RKT's own history contradicts it. The
  reconciling/dominant `dark_pool_accumulation` class has **no** backtest
  (`win_rate_source=null`). Given the conflict and small/market-wide N, phase-9 should
  fall back to the **conviction bin** and treat the 1.00 as non-dispositive.
- **Open questions:** what does macro (phase-6) say about mortgage-rate direction
  into 07-30 — the real driver of RKT? Do analysts/fundamentals (7b) justify the
  +9.9% run or flag it as extended? Does the earnings history (7b/earnings-scout)
  show RKT typically moves more than the $14–15 cage implies (validating the straddle)?
