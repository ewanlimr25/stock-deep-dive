# Phase 5 — Historical Context & VRP

**Ticker:** PATH
**As-of date:** 2026-08-12
**Generated:** 2026-08-13T02:20:00Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-4-structure.md

## Summary

The headline finding of this phase: PATH has run from **$11.55 to $15.26
(+32.2%)** over the 30 sessions from 2026-07-01 to 2026-08-12, with **OI
building on 29 of those 30 sessions** (`overall_trend=BUILDING`,
`total_net_oi_change=+318,061`) and **zero gamma-regime flips** — the dealer
book stayed `POSITIVE` (long gamma) throughout the entire rally. This is the
single most persistent structural signal surfaced anywhere in this deep dive.
Today, however, is the **smallest OI-build day of the past 29** (+2,637 vs. a
30-day median well into five figures), IV is **rich relative to realized**
(`VRP=+0.189`, `regime=PREMIUM_SELLING`), and `fz`'s independent RSI cross-check
reads **70.94 (overbought)**. Read together: a genuine multi-week structural
uptrend that is decelerating and technically stretched on the exact day this
dive is being run — consistent with every other phase's "normal pause, not
reversal" read. The signal-backtest for phase-2's dominant verdict
(`dark_pool_accumulation`) returned **zero historical firings** — no empirical
win rate available; phase-9 must size off the conviction bin, not a backtest
`p`.

## Key signals

- **29 of 30 sessions net OI-building**, `total_net_oi_change=+318,061`,
  `overall_trend=BUILDING` [HIST:oi_trend]
- **Zero GEX regime flips in 30 sessions** — dealer book never left
  `POSITIVE` even through a 30-session, +32.2% rally [HIST:gex_time_series]
- **VRP=+0.189, regime=PREMIUM_SELLING** — "Options pricing more vol than
  realised — favour premium selling" [HIST:vrp]
- IV percentile **71.76** (85 real sessions used, `regime=NORMAL`, z-score
  only 0.769 — elevated but not extreme) [HIST:iv_percentile_zscore]
- `fz` RSI(14)=**70.94** (overbought), price is **+65.87%** off the 52-week
  low but still **−23.08%** below the 52-week high [HIST:rsi fz, HIST:52w_proximity fz]
- `signal-backtest --signal-type dark_pool_accumulation` → **0 historical
  firings**; `win_rate_source=null` for phase-9 [HIST:signal_backtest]

## Detailed findings

### IV regime (percentile + z-score + VRP)

`uw historical iv-percentile-zscore --lookback-days 252`: `dates_used=85`
(gap-aware — the requested 252-day lookback returns only the 85 sessions
actually present locally, per the mandatory gap-aware-lookback rule; quote 85,
not 252). `current_iv30d=0.8212`, `iv_percentile=71.76`, `iv_zscore=0.769`,
`regime=NORMAL` (tool's own label). IV sits in its own upper third over the
real 85-session window but the z-score says it's under 1 standard deviation
above the mean — elevated, not extreme, for this name.

`uw historical vrp --realised-window-days 30`: `iv30d=0.8212`,
`realised_vol=0.6322`, `vrp=+0.189`, `regime=PREMIUM_SELLING`. Interpretation
(quoted verbatim): *"Options pricing more vol than realised — favour premium
selling."* This directly informs phase-9's structure choice: **debit
(premium-buying) structures are working against a historically rich vol
environment right now.**

### Cumulative premium flow (90d net direction)

`uw historical cumulative-premium-flow --days 90`: **86 sessions actually
covered** (requested 90 calendar days; gap-aware — quote 86). `cumulative_
bullish=$159,409,223`, `cumulative_bearish=$153,202,833`, net
**+$6,206,390** — a slight bullish tilt but only ~2% of the ~$312.6M gross
two-way flow over nearly 4 months. Not a strong directional tell on its own;
consistent with today's flat whole-tape read (phase-1).

### P/C ratio z-score (sentiment extreme y/n)

`uw historical pc-ratio-zscore --lookback-days 20`: `current_pc_
ratio=0.4748`, `mean_pc_ratio=0.2581`, `std_pc_ratio=0.1302`, `zscore=1.665`,
`extreme=NORMAL` (tool's own threshold requires |z|>2). Not statistically
"extreme," but today's P/C ratio is **~84% above its own 20-day mean** — a
real, if sub-threshold, pickup in put activity relative to PATH's own recent
(very call-skewed) norm. Consistent with phase-3's near-term put OI adds and
phase-1's LEAP put sweep activity.

### GEX time series (regime flip dates if any)

`uw historical gex-time-series --days 30 --dte-max 45`: `regime_flip_
dates=null` — **the dealer book has been long-gamma (POSITIVE) on every one
of the 30 sessions analyzed**, spanning a spot range of **$10.30–$15.69**.
`zero_gamma_level` crept slowly from ~$6.75–7.51 in early July to $8.58–8.64
this week, tracking the rally but staying far below spot the entire time —
this rally happened entirely inside a stable, long-gamma (mean-reversion-
favoring) regime, without the destabilizing short-gamma trend-amplification
regime ever engaging.

### OI trend (sustained buildup vs spike vs decay)

`uw historical oi-trend --days 30 --top-n 10`: `overall_trend=BUILDING`,
`total_net_oi_change=+318,061`, `consecutive_build_days=29` (every session
except 2026-07-01, which was −24,249). Daily net-OI-change series (last 10 of
30): 25,356 → 10,254 → 19,347 → 2,061 → 16,410 → 22,256 → 9,485 → 1,387 →
45,673 → **2,637 (today)**. **Today's build is the smallest of the entire
29-day streak** except for 2026-07-24 (+1,387) and 2026-07-30 (+2,061) — a
genuine deceleration, not a reversal (the streak is still net-positive).

### Multi-day trend table

`uw historical trend --days 30` (`date_range=2026-07-01 to 2026-08-12`, 30
sessions, no gap in this window): `price_change="11.55 -> 15.26"` (**+32.2%**),
`iv_rank_change="35.9052 -> 63.1609"` (IV rank nearly doubled alongside the
rally), `bullish_days=14` vs `bearish_days=16` (slightly more bearish-flow
days by count over the window, despite the large net price gain — flow and
price direction have diverged at the day-count level), `flow_direction_
latest=bearish` (today, matching phase-1's derived net_flow).

### Price context (`fz` cross-check, advisory)

From phase-0's `fz screen --tickers PATH --view technical` recovery:
`RSI(14)=70.94` (overbought, >70), `SMA20=+18.18%`, `SMA50=+29.17%`,
`SMA200=+19.83%` (price trading well above all three moving averages — intact
uptrend structure), `52W High=-23.08%`, `52W Low=+65.87%`, `Beta=1.00`. The
overbought RSI **tempers** (per this phase's own interpretation heuristic) a
fresh-breakout thesis at today's price — this is a stretched tape technically,
even though it remains meaningfully below its 52-week high.

### Signal backtest (current signal's historical edge)

Phase-2's dominant, most-directional read (`mild accumulation`,
`large`-tier buy_ratio=0.678) is the closest match to a `signal-backtest`
category → ran `--signal-type dark_pool_accumulation --lookback-days 5
--top-n 20` **twice** (per the "empty stub can be transient" rule): both
times returned `{"note":"no backtest results","total_signals":0}` — a stable
null, not a transient stub. **`win_rate_source=null`** — phase-9 must fall
back to the conviction bin, not a backtest `p`, for this signal class.
(Diagnostic-only, not usable as PATH's `p`: `bullish_flow` — a signal phase-1
did *not* actually verify as PATH's own read — returned a populated
market-wide result, `win_rate=71.4%, n=7, avg_move_pct=5.03%`; noted for
completeness, excluded from sizing since it doesn't match what actually fired.)

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw historical iv-percentile-zscore --symbol PATH --lookback-days 252 --json` | `iv_percentile=71.76, dates_used=85` ← top-level | 1 |
| `uw historical vrp --symbol PATH --realised-window-days 30 --json` | `vrp=0.189, regime=PREMIUM_SELLING` ← top-level | 1 |
| `uw historical cumulative-premium-flow --symbol PATH --days 90 --json` | `cumulative_bullish=159409223, cumulative_bearish=153202833` ← top-level; `dates_covered\|length`=86 | 86 dates |
| `uw historical pc-ratio-zscore --symbol PATH --lookback-days 20 --json` | `zscore=1.665, extreme=NORMAL` ← top-level | 1 |
| `uw historical gex-time-series --symbol PATH --days 30 --dte-max 45 --json` | `regime_flip_dates=null` ← top-level; `.trajectory[]` for spot range | 30 |
| `uw historical oi-trend --symbol PATH --days 30 --top-n 10 --json` | `overall_trend=BUILDING, consecutive_build_days=29, total_net_oi_change=318061` ← top-level; `.daily_data[].net_oi_change` | 30 |
| `uw historical trend --symbol PATH --days 30 --json` | `price_change, iv_rank_change, bullish_days, bearish_days, flow_direction_latest` ← top-level | 30 |
| `uw historical signal-backtest --signal-type dark_pool_accumulation --lookback-days 5 --top-n 20 --json` (run twice) | `total_signals=0` both times ← top-level | 0 |
| `uw historical signal-backtest --signal-type bullish_flow --lookback-days 5 --top-n 20 --json` (diagnostic only) | `win_rate=71.4%, total_signals=7` ← top-level | 7 |
| (phase-0 carry) `fz screen --tickers PATH --view technical --agent` | `RSI=70.94, SMA20/50/200, 52W High/Low` | 1 |

## Tool errors

<none>

## DATA NOTE / CORRECTION

<none — first read stood. `dark_pool_accumulation` backtest confirmed null on
a deliberate re-run, per the "empty stub occasionally transient" rule — this
is the negative-result case, not an unretried stub.>

## Verdict for downstream phases

- **Volatility regime:** Rich vs. realized (`VRP=+0.189, PREMIUM_SELLING`);
  IV percentile elevated-but-not-extreme (71.76, z=0.769, `NORMAL`).
- **Premium-buying vs premium-selling environment:** **Premium-selling favored**
  — options are pricing more vol than the underlying has actually realized
  over the past 30 days. Phase-9 should weight credit/premium-selling options
  structures over debit structures, all else equal.
- **Conviction:** 3/5 on the *structural* multi-week signal (29/30-day OI
  build streak + zero gamma-regime flips through a +32% rally is a genuinely
  rare, persistent pattern), but **1/5 on today specifically** (smallest build
  day of the streak, overbought RSI, VRP argues against chasing more premium
  here) — net this phase nudges toward "the multi-week uptrend is real and
  structurally intact, but today is a pause, not a fresh entry signal."
- **Three specific data points:** IV percentile **71.76** (85 sessions);
  VRP **+0.189** (PREMIUM_SELLING); signal win rate **null** (0 historical
  `dark_pool_accumulation` firings — no empirical edge to size against).
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:              dark_pool_accumulation
  signal_backtest_win_rate:  null
  win_rate_n:                0
  win_rate_source:           null
  ```
- **Open questions:** Is today's deceleration (smallest OI build in 29 days)
  the start of the structural build stalling out, or normal noise inside a
  still-intact uptrend? Phase-6's macro/sector read and phase-7's fundamentals
  should help decide whether the +32% run has a catalyst underneath it worth
  the current IV premium, or whether this is purely flow-driven froth that
  the RSI(14)=70.94 read is warning about.
