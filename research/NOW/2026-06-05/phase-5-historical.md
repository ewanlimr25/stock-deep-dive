# Phase 5 — Historical Context & VRP

**Ticker:** NOW
**As-of date:** 2026-06-05
**Generated:** 2026-06-06T12:34:00-04:00
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md, phase-1-flow.md, phase-2-dark-pool.md, phase-4-structure.md

> **Latest-anchor note:** every trailing read below anchors to the latest
> available session = **2026-06-05 = the as-of date** (phase-0-intake.md §UW
> availability), so windows end exactly at as-of. Re-runs after new sessions
> land will shift these numbers.

## Summary

The as-of day is the 4th session of a **−17.2% unwind (135.86 → 112.45) of a
3-session +33% melt-up** (100.02 on 5/26 → 135.86 on 6/1, IV rank 97 at the
top). IV is at its **94.9th percentile** (z +1.61, HIGH_IV — over the 39
sessions actually present, not a true 1y), yet **VRP is −0.106
(PREMIUM_BUYING: realized 77.5% > IV 66.9%)** — vol is statistically high
but still *cheap versus what the stock is actually moving*. The P/C ratio
z-score is **+6.09, BEARISH_EXTREME** (0.80 vs 20d mean 0.33) — a sentiment
extreme that flags contrarian risk to fresh shorts. The bearish_flow signal
class phase-1 leans on carries an **87.5% 5-day win rate, but N=8**
(market-wide base rate, low confidence).

## Key signals

- **IV percentile 94.87, z-score +1.611, regime HIGH_IV** — `dates_used` =
  **39** (gap-aware true N, not 252) [HIST:iv_percentile_zscore].
- **VRP −0.1059** (iv30d 0.6693 vs realised_vol 0.7752, 30d window), tool
  verbatim: "Vol cheap vs realised — favour premium buying", regime
  **PREMIUM_BUYING** [HIST:vrp] — collides head-on with the tape's
  premium-selling behavior (phase-1 [FLOW:aggressor_ex0dte DUCKDB]) and
  phase-4's COMPLACENT skew.
- **P/C z-score +6.093 = BEARISH_EXTREME**: current 0.80 vs mean 0.33
  (σ 0.0771, 20d lookback) [HIST:pc_ratio_zscore] — |z| > 2 contrarian
  threshold blown through; today's put tilt is a 6-sigma event for this name.
- **GEX positive-regime cushion eroding**: total_gex 47.8M (5/20) → 21.6M
  (6/4) → **6.9M (6/5)**; 9 regime flips in 30 sessions, last flip 5/28 →
  POSITIVE [HIST:gex_time_series] — one more down day likely flips dealers
  short-gamma (ZGL 109.7, phase-4-structure.md).
- **OI BUILDING 30/30 consecutive sessions, +1,317,462 net** (biggest single
  day 6/2: +107,897) [HIST:oi_trend] — positions are being opened, not
  abandoned, through both the melt-up and the fade.

## Detailed findings

### IV regime (percentile + z-score + VRP)

[HIST:iv_percentile_zscore] current_iv30d 0.6693, iv_percentile **94.87**,
iv_zscore **+1.611**, regime **HIGH_IV**, dates_used **39** (the "252-day"
lookback only has 39 local sessions — low-N caveat).
[HIST:vrp] vrp **−0.1059**, iv30d 0.6693, realised_vol **0.7752** (30d),
regime **PREMIUM_BUYING**. Caveat: the realized window contains +14.4%
(5/29), +9.2% (6/1), −6.0%, −7.6%, −5.8% prints — realized is
spike-inflated, so negative VRP partly reflects the blow-off. Still, at IV
rank 79 the market is NOT overpricing vol relative to delivered movement —
**debit/defined-risk structures preferred over naked premium sales**
(`Interpretation heuristics`: IV cheap vs realized + VRP < 0 → premium-
BUYING regime).

### Cumulative premium flow (90d requested)

[HIST:cumulative_premium_flow] cumulative_bullish $1,748,552,718 vs
cumulative_bearish $1,638,542,769 → **net_flow +$110,009,949**,
trend_direction **MIXED**. `dates_covered` = **40 actual sessions**
(2026-03-13 → 2026-06-05, crossing the 21-session hole 03-30→04-24,
phase-0-intake.md §Local data) — a 90-calendar-day label over 40 true
sessions. No stealth directional build: +$110M net on $3.39B two-way is ~3%
— consistent with phase-0.5's busy-name profile.

### P/C ratio z-score

[HIST:pc_ratio_zscore] current 0.80, 20d mean 0.33, σ 0.0771 → **z = +6.093,
extreme = BEARISH_EXTREME**. NOW is structurally a call-dominated name (mean
P/C 0.33); today's 0.80 is unprecedented in the window. Heuristic: |z| > 2 →
**contrarian setup possible** — the put-side rush is late to a move that
already happened.

### GEX time series (30 sessions)

[HIST:gex_time_series] **9 regime flips** in 30 sessions (4/30, 5/1, 5/4,
5/6, 5/15, 5/21, 5/22, 5/26, 5/28 — tool note: flips "empirically precede
realised-vol expansion"). Stable POSITIVE since 5/28, but total_gex decayed
47,841,830 (5/20) → 6,878,457 (6/5) — the long-gamma buffer is nearly gone.
**Data-quality caveat:** the ZGL series alternates implausibly between ~45–53
and ~104–109 on adjacent sessions (e.g. 5/29: 46.43, 6/2: 104.52, 6/3:
50.08, 6/4: 109.33) — treat the *regime labels* as usable and the raw ZGL
trail as noisy; phase-4's same-day ZGL 109.7 is the cleaner read.

### OI trend (30 sessions)

[HIST:oi_trend] overall_trend **BUILDING**, consecutive_build_days **30**,
total_net_oi_change **+1,317,462**. Recent builds: 6/1 +51,249, **6/2
+107,897**, 6/3 +50,615, 6/4 +21,377, 6/5 +33,873. Historical color: the
4/27 session (post-April-bottom) printed 14,983 fresh 55P 5/08 + 5,462 60P
5/08 — crash protection at the lows that expired worthless; the same
late-to-the-move put behavior phase-0.5/phase-1 see today.

### Multi-day trend table (10 most recent sessions)

[HIST:trend] days_analyzed 30, date_range "2026-03-27 to 2026-06-05"
(**crosses the data hole** — 1 session from the March cluster + 29 from the
post-gap cluster), bullish_days 15 / bearish_days 15, price_change "99.41 →
112.45", iv_rank_change "73.23 → 79.23", flow_direction_latest "bullish":

| Date | Close | Net flow | PCR | IV rank | Flow dir |
|---|---|---|---|---|---|
| 2026-06-05 | 112.45 | +1,783,036 | 0.80 | 79 | bullish |
| 2026-06-04 | 119.36 | −3,678,922 | 0.28 | 78 | bearish |
| 2026-06-03 | 117.90 | −17,163,632 | 0.38 | 80 | bearish |
| 2026-06-02 | 127.65 | −16,956,395 | 0.32 | 92 | bearish |
| 2026-06-01 | 135.86 | +24,673,741 | 0.42 | 97 | bullish |
| 2026-05-29 | 124.37 | +46,252,516 | 0.26 | 76 | bullish |
| 2026-05-28 | 108.73 | +29,639,728 | 0.32 | 63 | bullish |
| 2026-05-27 | 102.12 | +5,014,959 | 0.28 | 63 | bullish |
| 2026-05-26 | 100.02 | +1,992,020 | 0.36 | 64 | bullish |
| 2026-05-22 | 102.13 | +12,977,492 | 0.33 | 59 | bullish |

Read: huge bullish flow INTO the melt-up (+$46M 5/29, +$29.6M 5/28), bearish
flow riding the fade (−$17M × 2), and a flat/“bullish” +$1.8M on the as-of
day with PCR exploding to 0.80 — flow chased both legs; the as-of session is
the first stand-off. (6/4→6/5 close 119.36 → 112.45 = −5.8% matches phase-1's
intraday print trail 118.89 → 111.70.)

### Price context (`fz`, advisory)

[HIST:rsi fz] RSI(14) **54.53** — neutral; the −17% fade only unwound the
overbought melt-up. [HIST:52w_proximity fz] price 112.45 = **−46.83% below
the 52W high 211.48, +38.42% above the 52W low 81.24**; Perf Week −9.58%,
Perf Month **+26.28%**, Perf YTD −26.59%; price vs SMA20 **+6.94%**, vs
SMA50 **+13.52%**, vs SMA200 **−19.78%**. Shape: a deep-downtrend year, a
violent May rebound off 81, and a fade that hasn't even reached the rising
SMA20 (~105.1 implied). Advisory only — tempers both "breakdown" (still
above SMA20/50) and "dip-buy" (still −20% below SMA200, bear-market-rally
profile) readings.

### Signal backtest

[HIST:signal_backtest --signal-type bearish_flow --lookback-days 5]
win_rate **"87.5%"**, total_signals **8**, avg_move_pct **−2.73**. This is a
**market-wide base rate of the bearish_flow class over the trailing 5
sessions** (no `--symbol` exists) — not NOW-specific. N=8 < 10 → low
confidence (`Common pitfalls`); phase-9 must apply the N-conditional cap
(`rubrics/sizing-rubric.md`).

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw historical iv-percentile-zscore --symbol NOW --lookback-days 252 --json` | 94.87 / +1.611 / HIGH_IV / N=39 ← `.iv_percentile, .iv_zscore, .regime, .dates_used` | 39 sessions |
| `uw historical vrp --symbol NOW --realised-window-days 30 --json` | −0.1059 / PREMIUM_BUYING ← `.vrp, .regime` | 1 |
| `uw historical cumulative-premium-flow --symbol NOW --days 90 --json` | net +110,009,949 / MIXED / 40 dates ← `.net_flow, .trend_direction, .dates_covered\|length` | 40 sessions |
| `uw historical pc-ratio-zscore --symbol NOW --lookback-days 20 --json` | z 6.093 / BEARISH_EXTREME ← `.zscore, .extreme` | 20d window |
| `uw historical gex-time-series --symbol NOW --days 30 --dte-max 45 --json` | 9 flips; gex 6.9M on 6/5 ← `.regime_flip_dates, .trajectory[]` | 30 sessions |
| `uw historical oi-trend --symbol NOW --days 30 --top-n 10 --json` | BUILDING / 30 / +1,317,462 ← `.overall_trend, .consecutive_build_days, .total_net_oi_change` | 30 sessions |
| `uw historical trend --symbol NOW --days 30 --json` | 99.41→112.45; table ← `.daily_data[0:10]` (array is newest-first) | 30 sessions |
| `uw historical signal-backtest --signal-type bearish_flow --lookback-days 5 --top-n 20 --json` | 87.5% / N=8 / −2.73% ← `.win_rate, .total_signals, .avg_move_pct` | top-level |
| `fz quote NOW --agent` | RSI 54.53; SMA/52W block ← `.fundamentals.*` | 1 |

## Tool errors

- **Data-quality caveat (not an error):** `gex-time-series` ZGL alternates
  ~45–53 ↔ ~104–109 on adjacent sessions (see §GEX time series) —
  implausible jumps; regime labels retained, raw ZGL trail treated as noisy.

## DATA NOTE / CORRECTION

`historical trend` / `oi-trend` `daily_data` arrays are **newest-first**; an
initial `[-10:]` slice read the oldest rows (2026-03-27…05-07). Re-sliced
`[0:10]` on the saved JSON for the table above — no number from the wrong
slice was carried forward (the old slice is quoted only as historical color
in §OI trend, correctly dated).

## Verdict for downstream phases

- **Volatility regime:** statistically rich (94.9th %ile) but **cheap vs
  realized (VRP −0.106)** — "rich" is the wrong sell signal here.
- **Premium environment:** **PREMIUM_BUYING** (debit/defined-risk structures;
  avoid naked short options despite IV rank 79 — the tape that's selling
  them, phase-1, is fighting realized vol).
- **Conviction today's signal is historically edge-positive:** 3 / 5 —
  bearish_flow base rate 87.5% is strong but N=8; and the +6.09σ P/C extreme
  warns the bearish crowd is late.
- **Three specific datapoints:** IV %ile **94.87** (N=39); VRP **−0.1059**;
  bearish_flow win rate **87.5% (N=8, market-wide)**.
- **Sizing handoff block (phase-9 reads verbatim):**

```
signal_class:     bearish_flow
signal_backtest_win_rate: 0.875
win_rate_n:       8
win_rate_source:  backtest
```

- **Open questions:** What catalyst drove 5/29–6/1 (+33%) and the fade —
  news, guidance, AI-software rerating (phase 6/7c must identify it)? Does
  the 6.09σ put extreme mark capitulation-in-progress or the start of a
  regime change? Is the eroding GEX (47.8M→6.9M) the prelude to the
  short-gamma break phase-4 mapped below 110?
