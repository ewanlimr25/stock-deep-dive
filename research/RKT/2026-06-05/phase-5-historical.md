# Phase 5 — Historical Context & VRP

**Ticker:** RKT
**As-of date:** 2026-06-05
**Generated:** 2026-06-06T17:28:00-04:00
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md, phase-1-flow.md, phase-4-structure.md

## Summary

RKT sits in a **LOW_IV / premium-buying regime inside a violent downtrend**. IV30
is at the **15.38 percentile** (z −0.974, over the **39 sessions actually
present**, not 252 calendar days — gap-aware) while 30d realized vol (0.6571)
exceeds IV30 (0.5719), giving **VRP −0.0852 → PREMIUM_BUYING**. The 30-session
tape is 19 bearish / 11 bullish flow days with price falling 13.67 → 12.65, and
the last week was brutal: 14.18 (06-01) → 12.65 (−10.8%), including a −7.8% day
on 06-03. Dealer long-gamma never flipped (POSITIVE 30/30) but **total GEX
collapsed 97% in five sessions** (47.6M → 1.33M), so the mean-reversion cushion
phase-4 leans on is nearly spent. `fz` confirms: price 2.18% above the 52-week
low, −27.5% below SMA200, RSI 37.7. The market-wide bearish_flow backtest wins
**87.5%** — but on only **N=8** firings (low-confidence per pitfall).

## Key signals

- `iv_percentile` **15.38**, `iv_zscore` −0.974, `regime` "LOW_IV",
  `dates_used` **39** (gap-aware N, not 252) [HIST:iv_percentile_zscore]
- `vrp` **−0.0852** (iv30d 0.5719 − realised 0.6571), `regime`
  **"PREMIUM_BUYING"**, verbatim: "Vol cheap vs realised — favour premium
  buying." [HIST:vrp]
- 30d trend: **bearish_days 19 / bullish_days 11**, `flow_direction_latest`
  "bearish", `price_change` "13.67 -> 12.65", `iv_rank_change` "40.157 ->
  29.9622" [HIST:trend]
- `total_gex` series: 47,609,090 (05-29) → 21,412,397 (06-01) → 3,624,619
  (06-03) → **1,333,718 (06-05)**; `regime_flip_dates` null — POSITIVE all 30
  sessions but the cushion is −97% in 5 [HIST:gex_time_series]
- OI `overall_trend` **"BUILDING"**: `total_net_oi_change` +540,341,
  `consecutive_build_days` **30/30** [HIST:oi_trend]
- bearish_flow backtest: `win_rate` **"87.5%"**, `total_signals` **8**
  (market-wide base rate, 5d horizon — N<10 = low confidence)
  [HIST:signal_backtest]
- Price context: RSI(14) 37.69; vs SMA20 −9.01% / SMA50 −12.94% / SMA200
  −27.54%; Perf YTD −34.66%; 52W low $12.38 just −2.18% below
  [HIST:rsi fz][HIST:52w_proximity fz]

## Detailed findings

### IV regime (percentile + z-score + VRP)

| Metric | Value |
|---|---|
| current_iv30d | 0.5719 |
| iv_percentile (1y requested) | 15.38 |
| iv_zscore | −0.974 |
| regime | LOW_IV |
| dates_used | **39** (the local non-contiguous window, phase-0 §Local data) |
| realised_vol (30d) | 0.6571 |
| vrp | **−0.0852** |
| vrp regime | PREMIUM_BUYING |

Caveat: "1y percentile" is actually computed over 39 sessions of local data —
treat as "low vs the last two months," not a true 252-day percentile. Even so,
options are cheap relative to what the stock is actually realizing — debit
structures are the right expression (heuristic: IV cheap + VRP<0 → buy premium).

### Cumulative premium flow (90d requested → 40 sessions present)

cumulative_bullish $57,279,160 vs cumulative_bearish $61,456,058 →
`net_flow` **−$4,176,898**, `trend_direction` "MIXED". `dates_covered` = the
full 40-session local list (2026-03-13 → 2026-06-05, hole 03-28→04-24 excluded).
No stealth institutional build in either direction — modest cumulative bearish
skew, consistent with phase-0.5's mid-pack self-history verdict.

### P/C ratio z-score (20d)

current 0.46 vs mean 0.4558 (σ 0.2547) → z **+0.017**, `extreme` "NORMAL".
Today's call-heavy volume ratio is exactly RKT's norm — no sentiment extreme, no
contrarian trigger.

### GEX time series (30 sessions, dte_max 45)

`regime_flip_dates: null` — spot never crossed ZGL; regime POSITIVE 30/30.
Tail: spot 14.35→12.59 while total_gex 36.9M → 47.6M (05-29 peak) → 21.4M →
18.5M → 3.6M → 4.4M → **1.33M**. ZGL drifted 10.57 → 7.71. The stabilizing
long-gamma book has been ground down to ~3% of its week-ago size as spot fell
into phase-4's $12–$14 negative pocket — **the regime label says
mean-reversion; the magnitude says the brakes are nearly gone.**

### OI trend (30 sessions, top-n 10)

`overall_trend` "BUILDING"; `total_net_oi_change` +540,341;
`consecutive_build_days` 30 — net OI grew **every single session** in the
window. Last 5: +25,321 (06-01), +21,047 (06-02), +5,561 (06-03), +8,122
(06-04), +6,226 (06-05). Today's top builds are call-side (Sep-18 13C +2,971,
Jun-12 14C +1,170, Jun-18 17C +394, Jul-17 15C +319; lone put build Sep-18 12P
+351) — the chain keeps adding upside exposure into a falling tape, matching
phase-3's bullish-build / capped-structure tension.

### Multi-day trend (selected rows; full series in tool output)

| Date | Close | net_flow | P/C | iv_rank | Flow dir |
|---|---|---|---|---|---|
| 2026-06-05 | 12.65 | −209,751 | 0.46 | 29.96 | bearish |
| 2026-06-04 | 13.23 | +296,260 | 0.345 | 26.58 | bullish |
| 2026-06-03 | 12.94 | −65,912 | 0.684 | 26.58 | bearish (**−7.8% day** from 14.03) |
| 2026-06-02 | 14.03 | +241,863 | 0.646 | 30.36 | bullish |
| 2026-06-01 | 14.18 | +246,239 | 1.141 | 30.96 | bullish |
| 2026-05-29 | 14.51 | −412,347 | 0.220 | 31.16 | bearish |
| 2026-05-27 | 14.27 | −708,065 | 0.237 | 34.54 | bearish |
| 2026-05-20 | 13.63 | −342,439 | 0.233 | 35.36 | bearish |
| 2026-05-13 | 13.84 | −992,353 | 0.388 | 22.87 | bearish |
| 2026-05-04 | 14.01 | −1,373,246 | 0.595 | 40.52 | bearish |
| 2026-03-27 | 13.67 | +849,981 | 0.679 | 40.16 | bullish |

`date_range` "2026-03-27 to 2026-06-05", `days_analyzed` 30 — window **crosses
the 03-28→04-24 hole**; 30 sessions actually present, no interpolation observed
(each row is a real local date). Pattern: persistent modest bearish net flow on
down days, small bullish pops that fail; the week of 06-01→06-05 lost 10.8%
with the 06-04 bounce (+2.2%) immediately given back.

### Price context (`fz`, advisory — EOD cross-check)

Price $12.65: **−9.01% vs SMA20, −12.94% vs SMA50, −27.54% vs SMA200**;
Perf Month −13.65%, Perf YTD −34.66%; 52W band $12.38–$24.36 → spot is **+2.18%
off the 52-week low** and −48.07% off the high; RSI(14) 37.69 (weak, not <30
oversold). [HIST:rsi fz][HIST:52w_proximity fz] — Independent confirmation of a
mature, unbroken downtrend: the phase-4 max-pain magnets above spot ($14/$14.5)
are fighting the primary trend, and "cheap IV" here is cheap-for-a-reason.

### Signal backtest (bearish_flow, 5d lookback, market-wide)

`win_rate` "87.5%", `total_signals` 8, sample top rows: NVDA 06-03 (−4.49%,
win), SPY 06-03 (−2.21%, win), GOOGL 06-03 (+2.66%, loss for the bear signal).
**This is a market-wide base rate of the signal class, not an RKT-specific
rate** (tool takes no `--symbol`), and N=8 < 10 → low-confidence per pitfall.
Latest-anchor note: window ends at latest available = 2026-06-05 = as-of, so
the read is correctly aligned for this run but will shift on any re-run.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw historical iv-percentile-zscore --symbol RKT --lookback-days 252 --json` | 15.38 ← `.iv_percentile`; N ← `.dates_used` | 1 |
| `uw historical vrp --symbol RKT --realised-window-days 30 --json` | −0.0852 ← `.vrp`; `.regime` | 1 |
| `uw historical cumulative-premium-flow --symbol RKT --days 90 --json` | −4,176,898 ← `.net_flow`; N ← `.dates_covered\|length` | 40 |
| `uw historical pc-ratio-zscore --symbol RKT --lookback-days 20 --json` | z 0.017 ← `.zscore` | 1 |
| `uw historical gex-time-series --symbol RKT --days 30 --dte-max 45 --json` | flips ← `.regime_flip_dates`; tail ← `.trajectory[-7:]` | 30 |
| `uw historical oi-trend --symbol RKT --days 30 --top-n 10 --json` | BUILDING ← `.overall_trend`; +540,341 ← `.total_net_oi_change` | 30 |
| `uw historical trend --symbol RKT --days 30 --json` | 19/11 ← `.bearish_days`/`.bullish_days`; rows ← `.daily_data[]` | 30 |
| `uw historical signal-backtest --signal-type bearish_flow --lookback-days 5 --top-n 20 --json` | 87.5%/8 ← `.win_rate`/`.total_signals` (top-level) | 8 signals |
| `fz quote RKT --agent` | RSI/SMA/52W ← `.fundamentals.*` | 1 |

All trailing commands are latest-anchored (no `--date`); latest available =
2026-06-05 = as-of, so windows align for this run (engine behavior noted per
gap-aware guidance).

## Tool errors

None. Two outputs exceeded the display buffer and were persisted to files by the
harness; values were re-pulled with narrowed `jq` (summary fields only) rather
than read from truncated previews.

## DATA NOTE / CORRECTION

None — all numbers from validated `jq` round-trips on the narrowed re-runs.

## Verdict for downstream phases

- **Volatility regime:** **cheap** (15.4 pctile over N=39; VRP −0.085) — but
  "cheap in a downtrend," not cheap-and-quiet.
- **Premium environment:** **premium-BUYING** — debit structures favored; selling
  premium into RV 0.66 vs IV 0.57 is mispriced risk.
- **Conviction today's signal is historically edge-positive:** 3/5 — the
  bearish-tilt signal class wins 87.5% over 5d but N=8; trend/MA/52w-low context
  independently supports downside continuation; offsetting upward OI gravity
  (phase-4) caps conviction.
- **Three specific data points:** IV %ile **15.38** (N=39) · VRP **−0.0852** ·
  bearish_flow win_rate **87.5% (N=8, market-wide)**
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:     bearish_flow
  signal_backtest_win_rate: 0.875
  win_rate_n:       8
  win_rate_source:  backtest
  ```
  (Raw rate quoted; phase-9 applies the N-conditional cap per
  `rubrics/sizing-rubric.md` — N=8 is below the floor for full Kelly credit.)
- **Open questions:** What broke on 06-03 (−7.8% day) — macro or name news
  (phase-6/7c)? Is the 30/30 OI build call-buying-the-dip or covered-call
  supply? Does the GEX-cushion collapse + 52w-low proximity override the
  max-pain upward pull (phase-8 debate)?
