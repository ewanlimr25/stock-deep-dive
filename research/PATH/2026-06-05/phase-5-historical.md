# Phase 5 — Historical Context & VRP

**Ticker:** PATH
**As-of date:** 2026-06-05
**Generated:** 2026-06-06T10:55:00-04:00
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md, phase-1-flow.md, phase-3-positioning.md, phase-4-structure.md

*Anchor note: all trailing tools anchor to the latest available date =
2026-06-05 = this run's as-of — windows align exactly this run (not
reproducible after the next session lands).*

## Summary

Vol is **cheap** (1y IV percentile **12.82**, z-score **−1.116**, regime
`LOW_IV` over 39 true sessions) with **fair VRP** (+0.0384: "IV close to
realised — no clear edge from VRP alone"), so long-premium structures aren't
taxed. But the *directional* history argues against chasing today's mild
bullish read: the 90-day cumulative tape is **net bearish −$2.77M (`MIXED`)**,
the post-earnings week ran **three consecutive bearish flow days (−$2.52M,
−$0.81M, −$0.61M)** before today's flat +$55.6k, and the market-wide
`bullish_flow` backtest shows **0.0% wins over 8 signals** in the last 5
days — a tape that is currently punishing bullish flow (SNDK −14.9%, MU
−20.0% after firing). GEX has stayed `POSITIVE` for 30 days but the cushion
is decaying (28.6M → 4.4M since 05-29).

## Key signals

- **iv_percentile 12.82 / iv_zscore −1.116 / regime LOW_IV** (current_iv30d
  0.6474; `dates_used: 39` actual sessions, not 252 — gap-aware)
  [HIST:iv_percentile_zscore]
- **VRP +0.0384 `FAIR`** (iv30d 0.6474 vs realised_vol 0.609) — verbatim: "IV
  close to realised — no clear edge from VRP alone." [HIST:vrp]
- 90d cumulative flow: bullish $82,722,971 vs bearish $85,488,386 → net
  **−$2,765,415, `MIXED`** (40 actual sessions in window) [HIST:cumulative_premium_flow]
- **`bullish_flow` backtest: win_rate 0.0%, total_signals 8** (market-wide,
  5-day lookback) [HIST:signal_backtest]
- Post-earnings flow sequence (trend daily head): 06-01 **+$2,176,334**
  bullish → 06-02 **−$2,519,050** / 06-03 −$810,002 / 06-04 −$614,672 bearish
  → 06-05 +$55,591 [HIST:trend]

## Detailed findings

### IV regime

iv_percentile **12.82** of the past year (39 sessions actually present —
window crosses the 2026-03-28→04-24 hole, phase-0 §Local data), z −1.116,
LOW_IV. IV rank trend within the 30d window: 46.87 → 40.03
(`iv_rank_change`), having peaked 53.32 on earnings day 06-01 and crushed to
36.47 by 06-04 [HIST:trend]. Vol is cheap both vs its year and post-event.

### VRP

iv30d 0.6474 vs realised 0.609 → **vrp +0.0384, regime FAIR**. Neither
premium-selling edge nor a free option. With IV %ile 12.8, the *level* is
cheap even if the spread to realised is fair — debit structures are not
penalized [HIST:vrp].

### Cumulative premium flow (90d requested → 40 sessions actual, gap excluded)

cumulative_bullish $82.72M vs cumulative_bearish $85.49M → **net −$2.77M,
trend `MIXED`**. No stealth institutional build in either direction — the
two-way tape phase-0.5 described extends across the whole window.

### P/C ratio z-score

current 0.39 vs 20d mean 0.4078 (σ 0.247) → **z −0.072, `NORMAL`** — today's
call-heavy tape is *typical for this name*; no sentiment extreme
[HIST:pc_ratio_zscore].

### GEX time series (30d)

Regime `POSITIVE` all 30 days except a one-day flip cluster **05-05
(POSITIVE→NEGATIVE, spot 10.70 < ZGL 11.55) and 05-06 back (ZGL → 7.51)** —
no flips in the last 5 sessions. Trajectory: total_gex 28,620,419 (05-29) →
18,114,309 (06-01) → 6,896,108 (06-03) → 12,332,414 (06-04) → **4,446,621
(06-05)**, ZGL steady 7.6–8.5 [HIST:gex_time_series]. The long-gamma
*cushion is thinning* even as the regime label holds — phase-4's $11
negative-GEX pocket matters more on a thin cushion.

### OI trend (30d)

overall_trend **`BUILDING`**, total_net_oi_change **+786,682** over 30
sessions; consecutive_build_days 1 (06-04 printed −7,388). Recent heads
[HIST:oi_trend]:

| date | net OI Δ | top contract |
|---|---|---|
| 06-05 | +3,595 | Aug-21 $12C +3,379 (the phase-3 write) |
| 06-04 | −7,388 | 0DTE 06-05 $11P +3,304 |
| 06-03 | **+54,701** | **Jun-18 $11P +22,202** |
| 06-02 | +49,438 | Jun-18 $18C +7,955 |
| 06-01 | +42,901 | 06-05 $13.5C +4,036 |

**Refines phase-3:** the Jun-18 $11P block (22.2k lots) was *opened 06-03*
into the fade — and ~9k of it was *closed 06-05* (phase-3 §rolls). The big
put holder is already de-grossing a 2-day-old hedge, not running for cover.

### Multi-day trend table (latest 6 sessions of 30; `days_analyzed: 30`,
`date_range: 2026-03-27 → 2026-06-05`, crosses the gap)

| date | iv_rank | P/C | net premium | direction |
|---|---|---|---|---|
| 06-05 | 40.03 | 0.39 | +$55,591 | bullish |
| 06-04 | 36.47 | 0.14 | −$614,672 | bearish |
| 06-03 | 45.24 | 0.30 | −$810,002 | bearish |
| 06-02 | 47.16 | 0.85 | −$2,519,050 | bearish |
| 06-01 | 53.32 | 0.26 | +$2,176,334 | bullish |
| 05-29 | 43.32 | 0.35 | +$232,542 | bullish |

Window totals: **13 bullish vs 17 bearish days**; price 10.69 → 11.24
(+5.1%) over the 30 sessions; `flow_direction_latest: bullish` [HIST:trend].

### Price context (fz, advisory)

RSI(14) **51.18** (neutral, fully unwound from 73.87 on 06-01 — phase-0
drift); price +2.30% vs SMA20, +4.60% vs SMA50, **−13.69% vs SMA200**;
−43.35% from 52W high ($19.84), +22.17% above 52W low ($9.20); YTD −31.42%,
month +7.05% [HIST:rsi fz][HIST:52w_proximity fz]. A broken long-term chart
in a 1-month recovery that just gave back its earnings pop — neither
overbought nor at structural support.

### Signal backtest (`bullish_flow`, market-wide, 5d lookback)

**win_rate 0.0% · total_signals 8** [HIST:signal_backtest]. Sample rows: SNDK
(sig 06-03) −14.86% in 5d; MU (06-03) −19.97%; META (06-03) −4.81%. Two
caveats for phase-9: (a) **N=8 < 10 → low-confidence** per common-pitfalls;
(b) the sample is concentrated on 06-03 signals straight into the
semis/tech sell-off phase-0.5 documented — it measures *this regime's*
hostility to bullish flow more than the signal class's long-run edge. It is
still the only empirical `p` available and it says the tape eats bullish
flow right now.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw historical iv-percentile-zscore --symbol PATH --lookback-days 252 --json` | 12.82 / −1.116 / LOW_IV / dates_used 39 ← top-level fields | 39 sessions |
| `uw historical vrp --symbol PATH --realised-window-days 30 --json` | vrp 0.0384 FAIR ← `.vrp/.regime` | aggregate |
| `uw historical cumulative-premium-flow --symbol PATH --days 90 --json` | net −2,765,415 MIXED ← `.net_flow/.trend_direction`; 40 dates ← `.dates_covered\|length` | 40 sessions |
| `uw historical pc-ratio-zscore --symbol PATH --lookback-days 20 --json` | z −0.072 NORMAL ← `.zscore/.extreme` | 20 sessions |
| `uw historical gex-time-series --symbol PATH --days 30 --dte-max 45 --json` | flips 05-05/05-06; gex 4,446,621 @06-05 ← `.regime_flip_dates/.trajectory[]` | 30 sessions |
| `uw historical oi-trend --symbol PATH --days 30 --top-n 10 --json` | BUILDING +786,682; Jun-18 $11P +22,202 @06-03 ← `.overall_trend/.daily_data[].top_contracts[0]` | 30 sessions |
| `uw historical trend --symbol PATH --days 30 --json` | 13 bull/17 bear; daily net_premium ← `.bullish_days/.daily_data[]{net_premium}` | 30 sessions |
| `uw historical signal-backtest --signal-type bullish_flow --lookback-days 5 --top-n 20 --json` | win_rate "0.0%", total_signals 8 ← top-level | 8 signals |
| `fz quote PATH --agent` | RSI 51.18, SMA200 −13.69% ← `.fundamentals.*` | snapshot |

## Tool errors

None. Data-quality caveats (not errors): `daily_data` arrays are
newest-first — first slice read the oldest rows; corrected (see DATA NOTE).
`trend.date_range` spans the 03-28→04-24 hole; all counts quoted are the
tools' own session counts (30/39/40), not calendar spans.

## DATA NOTE / CORRECTION

- `oi-trend`/`trend` `.daily_data` is sorted **newest-first**; initial `[-5:]`
  tail slices returned Mar/Apr rows. Re-read with `[0:5]`/`[0:6]` heads; all
  quoted recent-session values come from the corrected head reads.
- `gex-time-series` 06-05 total (4,446,621) differs from phase-4's `gex`
  total (4,446,767) by 146 (~0.003%) — same parquet, minor code-path rounding;
  both `POSITIVE`, immaterial.

## Verdict for downstream phases

- **Volatility regime:** **cheap** (12.8th %ile, z −1.1) with fair VRP →
  long-premium/debit structures appropriate; no edge selling vol
- **Premium-buying vs premium-selling environment:** premium-BUYING (cheap IV,
  fair VRP), but direction unproven
- **Conviction today's signal is HISTORICALLY EDGE-POSITIVE:** **1/5** —
  backtest 0/8, 90d cumulative net negative, 3-day post-earnings bearish
  streak just ended; only the OI `BUILDING` trend and cheap vol argue for
  engagement at all
- **Three specific datapoints:** IV %ile **12.82**; VRP **+0.0384 (FAIR)**;
  bullish_flow win-rate **0.00 (n=8, market-wide)**
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:     bullish_flow
  signal_backtest_win_rate: 0.00
  win_rate_n:       8
  win_rate_source:  backtest
  ```
  (N=8 < 10 → phase-9 must apply the low-N cap from
  `rubrics/sizing-rubric.md` §"Choosing the Kelly `p`"; sample is
  regime-concentrated on 06-03 tech-selloff signals.)
- **Open questions:** Does the macro phase confirm the tech-tape hostility is
  regime-wide (phase 6)? Is cheap IV cheap for a reason (phase-7b
  fundamentals quality)?
