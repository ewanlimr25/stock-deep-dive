# Phase 5 — Historical Context & VRP

**Ticker:** FSLR
**As-of date:** 2026-07-31
**Generated:** 2026-07-31
**Upstream phases cited:** `phase-0-intake.md`, `phase-0.5-context.md`, `phase-1-flow.md`, `phase-2-dark-pool.md`, `phase-3-positioning.md`, `phase-4-structure.md`

## Summary

**This is a premium-selling regime in a downtrend that has stopped going
down — and today the stock touched the exact wall phase 4 identified, then
failed.** FSLR's intraday high was **217.1274** against phase-4's dominant
gamma strike of **217.50** (net_gex +2,344,544); it closed **211.03**, giving
back 6.10 points. The most heavily-evidenced level in this deep dive was
tested and rejected on the day it was identified.

The volatility read is unambiguous. `vrp` returns **+0.3587** —
`iv30d` 0.7378 against `realised_vol` 0.3791 — regime **PREMIUM_SELLING**,
*"Options pricing more vol than realised."* An independent DuckDB calculation
confirms it (30-day close-to-close annualized: **0.3821**), and realized vol
is **falling** (60d 0.5821 → 30d 0.3821 → 20d 0.3732), so the premium is
widening, not closing. Options price roughly **1.93× the vol the stock is
actually delivering.**

Context matters more than the headline decline. `trend` reports
**257.70 → 211.03 (−18.1%) over 30 sessions** with 19 bearish days to 11
bullish — but that damage was done by mid-July. For the last twelve sessions
FSLR has **based between 195.84 and 220.97**, and today's close sits at the
**top of that range**. The `oi-trend` reads **BUILDING**, `+184,105` net OI
over 30 sessions with **10 consecutive build days** — accumulation of
positions through a decline that stopped.

The structural change of the day is in `gex-time-series`: **the zero-gamma
level collapsed from ~300 to 215.03 in a single session** — 85 points, the
largest shift in the 30-day window. FSLR has spent a month with dealers deeply
short gamma and spot 30% below the flip; it now sits **1.9% below it**.

**The signal backtest must not be taken at face value.** `bullish_flow`
returns `win_rate = "100.0%"` on `total_signals = 9` — below the 10-firing
confidence floor, market-wide rather than FSLR-specific, and carrying the
tool's own disclaimer: *"In-sample backtest — not a robust live edge."*
`dark_pool_accumulation` — the class matching phase 2's dominant verdict —
returned **zero signals on two separate runs**.

## Key signals

- **VRP +0.3587** (IV30d 0.7378 vs realized 0.3791), regime
  **PREMIUM_SELLING**; independently verified at 0.3821 `[HIST:vrp]`
  `[HIST:realised_vol DUCKDB]`
- **Realized vol is decaying**: 60d 0.5821 → 30d 0.3821 → 20d 0.3732 — the
  premium is widening `[HIST:realised_vol DUCKDB]`
- **Today's high 217.1274 vs phase-4's 217.50 gamma wall — tested and
  rejected**, closing 6.10 points lower `[HIST:intraday_range DUCKDB]`
- **ZGL collapsed ~300 → 215.03 in one session**; no regime flip yet
  (`regime_flip_dates: null`) `[HIST:gex_time_series]`
- **OI BUILDING: +184,105 over 30 sessions, 10 consecutive build days**
  `[HIST:oi_trend]`
- **Price −18.1% over 30 sessions (257.70 → 211.03), 19 bearish vs 11 bullish
  days** — but flat for the last 12 `[HIST:trend]`
- **IV percentile 71.43 / z-score +0.751, regime NORMAL** — over **77**
  sessions, not the 252 requested `[HIST:iv_percentile_zscore]`
- **90-day cumulative flow essentially balanced**: +$17.3M net on $2.25B
  gross (0.77%), `trend_direction = MIXED` `[HIST:cumulative_premium_flow]`
- **P/C z-score −0.825, `extreme = NORMAL`** — call-skewed, not a sentiment
  extreme `[HIST:pc_ratio_zscore]`
- **`bullish_flow` backtest: 100.0% on n=9, in-sample, market-wide** — not a
  usable Kelly `p` `[HIST:signal_backtest]`
- **RSI 43.00, price below SMA20/50/200, −34.25% from the 52w high, YTD
  −19.22%** `[HIST:rsi fz]` `[HIST:52w_proximity fz]`

## Detailed findings

### IV regime (percentile + z-score + VRP)

| Field | Value |
|-------|------:|
| `current_iv30d` | 0.7378 |
| `iv_percentile` | **71.43** |
| `iv_zscore` | +0.751 |
| `regime` | **NORMAL** |
| `lookback_days` requested | 252 |
| **`dates_used`** | **77** ⚠ |

**The 252-day lookback resolved to 77 actual sessions** — the local snapshot
only spans 2026-03-13 → 2026-07-31 (78 dates) with the 21-session hole
recorded in `phase-0-intake.md`. This is a **~3.5-month** IV percentile
labelled as one-year. Per the standing pitfall about 1-year metrics, it is
weaker still: a 71.43 percentile over 77 sessions says little about where
FSLR's IV sits in a genuine annual distribution.

Three IV percentile measures now exist across this run and they are **not in
conflict** — they measure different things:

| Measure | Value | Source | What it is |
|---------|------:|--------|------------|
| `iv_rank` | 81.94 | screener | Position in the high–low IV *range* |
| `iv_percentile` | 71.43 | phase-5, N=77 | Rank of `iv30d` across sessions |
| `self_pctile_iv_rank` | 39.4 | phase-0.5, N=67 | Percentile of the *iv_rank value* |

Phase 10 should not flag these as an internal contradiction.

**VRP:**

| Field | Value |
|-------|------:|
| `iv30d` | 0.7378 |
| `realised_vol` (30d) | **0.3791** |
| **`vrp`** | **+0.3587** |
| `regime` | **PREMIUM_SELLING** |
| `interpretation` | *"Options pricing more vol than realised — favour premium selling."* |

**Verified independently** (DuckDB, close-to-close log returns, annualized
×√252, post-gap window):

| Window | Realized vol |
|-------:|-------------:|
| 20 sessions | 0.3732 |
| **30 sessions** | **0.3821** |
| 60 sessions | 0.5821 |

The 30-session figure of **0.3821** matches UW's 0.3791 to within 0.003 —
**the VRP is real and correctly computed.** More importantly, the term shows
realized vol **collapsing**: the 60-session window (0.5821) still carries the
June–July decline; the recent 20 sessions run at 0.3732. **As the high-vol
period rolls out of the window, VRP widens further.**

Options are pricing **1.93×** the vol the stock is delivering. Combined with
phase-4's `term-skew` **COMPLACENT** and `front-end-iv-ratio` **FLAT**, the
conclusion is consistent: **sell premium, do not buy it.**

**One advisory caution** (`fz`, never enters Kelly `p`): Finviz reports
`Volatility M` **4.31%** and `Volatility W` **3.95%** — daily *range*
measures, not close-to-close. The DuckDB cross-check reconciles them:
average daily high-low range is **4.47%** while average absolute close-to-close
move is **1.99%**. Both metrics are correct; they are simply different. But it
means **intraday movement is roughly 2.2× the close-to-close measure the VRP
uses** — a short-premium position will experience considerably more
intra-day heat than a +0.3587 VRP suggests. `ATR 10.34` (4.9% of spot)
says the same thing.

### Cumulative premium flow (90d)

| Field | Value |
|-------|------:|
| `cumulative_bullish` | $1,133,472,521 |
| `cumulative_bearish` | $1,116,199,461 |
| **`net_flow`** | **+$17,273,060** |
| `trend_direction` | **MIXED** |
| `days` requested | 90 |
| **`dates_covered`** | **78** (2026-03-13 → 2026-07-31) ⚠ |

**Net flow is +0.77% of gross** — $17.3M on $2.25B two-way. That is noise, and
`MIXED` is the honest label. **Over three and a half months there is no
directional premium accumulation in FSLR.**

This directly rebuts the strongest possible bullish framing of phases 1–2. The
heuristic *"cumulative premium flow + and persistent ≥ 60d = stealth
institutional build"* **does not fire**: the flow is positive but not
persistent, and its magnitude is a rounding error.

⚠ **This window crosses the data gap.** `dates_covered` spans 2026-03-13 →
2026-07-31 — a 140-calendar-day range covered by **78 sessions**, with the
21-session hole (2026-03-28 → 2026-04-24) inside it. The figure is a sum over
78 available sessions, **not a contiguous 90 trading days**, and no rate or
trend should be fitted across it.

### P/C ratio z-score

| Field | Value |
|-------|------:|
| `current_pc_ratio` | 0.2791 |
| `mean_pc_ratio` (20d) | 0.9642 |
| `std_pc_ratio` | 0.8305 |
| **`zscore`** | **−0.825** |
| **`extreme`** | **NORMAL** |

Today's P/C of 0.2791 is the **most call-skewed reading in the visible
month** (the `trend` table below shows the 12-session range as 0.279–1.503),
yet the z-score is only −0.825 because **the standard deviation (0.8305) is
86% of the mean (0.9642)** — FSLR's P/C series is extremely noisy, which
mechanically suppresses any |z|.

**No sentiment extreme, no contrarian setup.** The heuristic requires |z| > 2.
Phase 9 should not build a squeeze or fade thesis on positioning sentiment.

### GEX time series (30 sessions, 2026-06-18 → 2026-07-31)

`regime_flip_dates: **null**` — spot never crossed the zero-gamma level in the
window.

| Date | `total_gex` | `zero_gamma_level` | `regime` |
|------|------------:|-------------------:|----------|
| 2026-07-16 | −4,805,851 | — | FULLY_NEGATIVE |
| 2026-07-17 | −4,422,707 | — | FULLY_NEGATIVE |
| 2026-07-20 | −2,043,806 | — | FULLY_NEGATIVE |
| 2026-07-21 | −1,808,565 | — | FULLY_NEGATIVE |
| 2026-07-22 | +561,379 | 296.65 | NEGATIVE |
| 2026-07-23 | +84,898 | 314.37 | NEGATIVE |
| 2026-07-24 | −912,407 | — | FULLY_NEGATIVE |
| 2026-07-27 | +116,219 | 309.29 | NEGATIVE |
| 2026-07-28 | −78,299 | — | FULLY_NEGATIVE |
| 2026-07-29 | −348,486 | — | FULLY_NEGATIVE |
| 2026-07-30 | +229,245 | 300.60 | NEGATIVE |
| **2026-07-31** | **+2,993,842** | **215.03** | NEGATIVE |

**Two structural facts:**

1. **The ZGL collapsed from 300.60 to 215.03 — an 85-point, 28% drop in one
   session**, and by far the largest move in the window. On every prior day a
   ZGL was computable it sat at **296–314**, i.e. **40–50% above spot**;
   dealers were unreachably short gamma and hedging purely amplified.
   **FSLR now sits 1.9% below its flip for the first time in the observable
   window.**
2. **`total_gex` jumped 13× to +2,993,842** — the largest reading in 30
   sessions, and consistent with phase-4's finding that a single strike
   (217.50, +2,344,544) now dominates the surface.

**Interpretation:** a genuine structural transition, mechanically driven by
today's flow — the 1,900-lot Aug-21 $230 block and the LEAP roll
(`phase-1-flow.md`) materially rewrote dealer inventory. Per the heuristic
*"GEX regime flip in last 5d → larger intraday ranges expected"*, no flip has
occurred **yet**, but the flip level has moved from unreachable to **2%
away**. Today's 5.1% intraday range (206.39–217.13) is what that transition
looks like in practice.

**Caveat:** `zero_gamma_level` is `null` on 7 of 12 recent sessions — the
series is intermittent, so "ZGL was ~300" describes the days it computed, not
a continuous line. And per phase-4, `total_gex` and `regime` disagree in sign
on today's row.

### OI trend (30 sessions)

| Field | Value |
|-------|------:|
| `overall_trend` | **BUILDING** |
| `total_net_oi_change` | **+184,105** |
| `consecutive_build_days` | **10** |
| `days_analyzed` | 30 (2026-06-18 → 2026-07-31, no gap) |

Last ten sessions, all positive:

| Date | Net OI Δ |
|------|---------:|
| 2026-07-20 | +8,139 |
| 2026-07-21 | +5,092 |
| 2026-07-22 | +7,797 |
| 2026-07-23 | +6,466 |
| 2026-07-24 | +1,530 |
| 2026-07-27 | +2,474 |
| 2026-07-28 | +5,547 |
| 2026-07-29 | +8,494 |
| 2026-07-30 | +3,627 |
| **2026-07-31** | **+9,631** |

**Cross-check passed:** today's +9,631 exactly equals phase-3's independently
computed net OI change (**+6,117 calls + 3,514 puts = +9,631**) from the raw
parquet. Both inherit the same one-session lag, so the "2026-07-31" row is the
**07-30 → 07-31** change and does not contain today's block.

**Positions built persistently through the entire decline** — 10 consecutive
build days, +184,105 contracts over 30 sessions. Per the phase-5 heuristics
this is **sustained buildup, not a spike**. Read with phase-3's structure
(far-dated calls, near-dated puts) and phase-2's five-day accumulation flip,
it points to **positioning being established into weakness** rather than
chased after strength.

### Multi-day trend table (30 sessions)

| Field | Value |
|-------|------:|
| `date_range` | 2026-06-18 → 2026-07-31 |
| `days_analyzed` | 30 (no gap crossing) |
| **`price_change`** | **257.70 → 211.03 (−18.11%)** |
| `iv_rank_change` | 88.4239 → 81.9358 |
| `bullish_days` / `bearish_days` | **11 / 19** |
| `flow_direction_latest` | **bearish** |

Last 12 sessions:

| Date | Close | IV rank | P/C ratio |
|------|------:|--------:|----------:|
| 2026-07-16 | 211.93 | 83.08 | 0.613 |
| 2026-07-17 | 211.99 | 91.99 | 0.651 |
| 2026-07-20 | 205.31 | 99.11 | 0.418 |
| 2026-07-21 | 206.05 | 97.03 | 1.144 |
| 2026-07-22 | 208.86 | 96.44 | 0.413 |
| 2026-07-23 | 205.92 | **100.00** | 1.117 |
| 2026-07-24 | 202.82 | **100.00** | 0.501 |
| 2026-07-27 | 205.83 | 98.35 | 0.533 |
| 2026-07-28 | 202.59 | **100.00** | **1.503** |
| 2026-07-29 | **199.24** | 91.10 | 0.354 |
| 2026-07-30 | 206.01 | 94.61 | 0.563 |
| **2026-07-31** | **211.03** | **81.94** | **0.279** |

**The −18.1% headline is misleading as a current-state description.** The
decline happened between 2026-06-18 (257.70) and 2026-07-16 (211.93). For the
**twelve sessions since**, FSLR has traded **199.24 – 211.99 on close**
(195.84 – 220.97 intraday) and gone precisely nowhere — 211.93 → 211.03.

**FSLR is not in a downtrend right now; it is in a two-week base, and today's
close is at the top of it.** This reframes phase 0.5's "10 of 12 sessions with
negative net-directional premium while price went nowhere": the bearish
premium has been **paid for and has not worked** for twelve sessions.

`flow_direction_latest = "bearish"` is inherited from the same
`bullish_premium − bearish_premium` convention that `phase-1-flow.md`
demonstrated **excludes $2,545,750 (9.5%) of today's tape**. It is not
independent evidence.

30-session price statistics (DuckDB): **low 199.24, high 263.11, mean
223.86**. Today's 211.03 is **below the 30-session mean** — the base is at the
low end of the quarter's range, not a topping pattern.

### The 217.50 test — today's single most informative price fact

| | |
|---|---:|
| Today's high | **217.1274** |
| Phase-4 dominant gamma strike | **217.50** |
| Distance | **0.17%** |
| Close | 211.03 |
| Give-back from high | **−6.10 (−2.81%)** |
| Today's range | 206.39 – 217.13 (**5.09%**) |

FSLR traded to within **37 cents** of the strike carrying **net_gex
+2,344,544** — 78% of the entire summed gamma surface — and closed 6.10 points
below it. Phase 4 predicted 214.00–217.50 would be "sticky" resistance where
"dealers sell into strength." **The prediction and the test occurred on the
same day, and the level held.**

This also explains phase-0.5's otherwise-puzzling *"gap +3.29%, faded −0.82%
from the open"*: the gap ran into the wall.

### Price context (`fz`, advisory)

| Metric | Value |
|--------|------:|
| RSI (14) | **43.00** |
| Price vs SMA20 | −1.49% |
| Price vs SMA50 | **−13.93%** |
| Price vs SMA200 | −9.91% |
| 52W High | **−34.25%** (320.95) |
| 52W Low | **+22.70%** (171.99) |
| ATR | 10.34 (4.90% of spot) |
| Beta | **1.76** |
| Perf Week | +4.05% |
| Perf Month | −9.07% |
| Perf Quarter | +4.53% |
| Perf Half | −5.79% |
| **Perf YTD** | **−19.22%** |
| Perf Year | +20.77% |
| Rel Volume | 1.42 |

**Independent EOD confirmation of the base-not-breakdown read.** RSI **43** is
neutral — neither oversold (no bounce edge) nor overbought (no
exhaustion risk). Price is only **1.49% below SMA20** but **13.93% below
SMA50**: the short average has come down to meet price, which is what basing
looks like. SMA50 (≈245.2) sits **above** SMA200 (≈234.2), so the longer-term
structure has not broken even though price is beneath both.

**Beta 1.76** matters for sizing: FSLR carries 1.76× market risk, and phase
0.5 found **Technology is the day's worst sector at −$187.7M** net premium.
A long here is a leveraged bet on a sector currently being sold.

The tension worth carrying forward: **YTD −19.22% against Perf Year
+20.77%** — the twelve-month gain is entirely from a period now well behind;
2026 has been a persistent de-rating.

### Signal backtest

**Class matching phase-2's dominant verdict — `dark_pool_accumulation`:**

```json
{"note":"no backtest results","signal_type":"dark_pool_accumulation","total_signals":0}
```

**Re-run once per the phase-5 guidance; identical empty stub both times.**
→ `win_rate_source = null` for this class.

**Class matching phase-1's verdict — `bullish_flow`:**

| Field | Value |
|-------|------:|
| `win_rate` | **"100.0%"** (string, not float) |
| `total_signals` | **9** |
| `truncated_signals` | 9 |
| `avg_move_pct` | 8.66 |
| `lookback_days` | 5 |
| `methodology_notes` | *"win_rate = fraction of signals where forward move agrees with the signal's direction. Lookback is in TRADING days; selection is positional within the yfinance bar series. **In-sample backtest — not a robust live edge.**"* |

**A 100% win rate is a warning, not an edge.** Four independent reasons this
must not be used as a Kelly `p` at face value:

1. **n = 9 — below the 10-firing floor** the phase-5 pitfalls set for
   low-confidence classification.
2. **The tool disclaims itself**: *"In-sample backtest — not a robust live
   edge."*
3. **It is market-wide.** `signal-backtest` takes no `--symbol`, so 100% is
   the base rate of the `bullish_flow` class **across the whole tape over 5
   trading days**, not FSLR's rate. FSLR may never have fired this signal.
4. **A 5-day lookback with `avg_move_pct` 8.66** over a window in which the
   broad tape rallied ("US Stocks Rally to End a Turbulent Month" —
   `phase-0.5-context.md`) is close to measuring beta, not signal.

Per the guidance to *"quote the raw win-rate; phase-9 applies the
N-conditional cap"*, **1.00 is recorded verbatim below** — but phase 9 must
apply the N-conditional cap aggressively, and the sizing rubric's
conviction-bin fallback is the more defensible input here. **Sizing on p = 1.00
would be indefensible.**

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` / SQL path | Rows used |
|------------------|--------------------------------|-----------|
| `uw historical iv-percentile-zscore --symbol FSLR --lookback-days 252 --json` | iv_percentile=71.43, iv_zscore=0.751, current_iv30d=0.7378, regime="NORMAL", **dates_used=77** ← `.` | 77 |
| `uw historical vrp --symbol FSLR --realised-window-days 30 --json` | vrp=0.3587, iv30d=0.7378, realised_vol=0.3791, regime="PREMIUM_SELLING" ← `.` | 30 |
| `uw historical cumulative-premium-flow --symbol FSLR --days 90 --json` | net_flow=17273060, cumulative_bullish=1133472521, cumulative_bearish=1116199461, trend_direction="MIXED"; **`dates_covered\|length`=78, min=2026-03-13, max=2026-07-31** | 78 |
| `uw historical pc-ratio-zscore --symbol FSLR --lookback-days 20 --json` | zscore=−0.825, current_pc_ratio=0.2791, mean=0.9642, std=0.8305, extreme="NORMAL" ← `.` | 20 |
| `uw historical gex-time-series --symbol FSLR --days 30 --dte-max 45 --json` | **regime_flip_dates=null**; 07-30 zgl=300.6 / 07-31 zgl=215.03, total_gex=2993842 ← `.trajectory[-2:]`; range 2026-06-18→2026-07-31 | 30 |
| `uw historical oi-trend --symbol FSLR --days 30 --top-n 10 --json` | overall_trend="BUILDING", total_net_oi_change=184105, consecutive_build_days=10 ← `.`; 07-31 net_oi_change=9631 ← `.daily_data[]` | 30 |
| `uw historical trend --symbol FSLR --days 30 --json` | price_change="257.7 -> 211.03", iv_rank_change="88.4239 -> 81.9358", bullish_days=11, bearish_days=19, date_range="2026-06-18 to 2026-07-31" ← `.` | 30 |
| `uw historical signal-backtest --signal-type dark_pool_accumulation --lookback-days 5 --top-n 20 --json` | `total_signals=0`, note="no backtest results" ← `.` (**run twice**) | 0 |
| `uw historical signal-backtest --signal-type bullish_flow --lookback-days 5 --top-n 20 --json` | **win_rate="100.0%" (string), total_signals=9**, avg_move_pct=8.66 ← `.` | 9 |
| `fz screen --tickers FSLR --view technical --json` | RSI=43.00, SMA50=−13.93%, SMA200=−9.91%, ATR=10.34, Beta=1.76, 52W High=−34.25% ← `.[0]` | 1 |
| `fz screen --tickers FSLR --view performance --json` | Perf YTD=−19.22%, Perf Year=+20.77%, Perf Month=−9.07%, Volatility M=4.31%, Rel Volume=1.42 ← `.[0]` | 1 |
| DuckDB realized vol, `STDDEV_SAMP(ln(close/prev))×√252` | 20d=0.3732, **30d=0.3821**, 60d=0.5821 | 67 |
| DuckDB avg move / range | avg_abs_move=1.99%, avg_hl_range=4.47% (n=30) | 30 |
| DuckDB price path | 30-session low=199.24, high=263.11, mean=223.86; **2026-07-31 high=217.1274, low=206.39** | 30 |

## Tool errors

No command errored — all nine exited 0 and every payload parsed.

Data-quality findings that qualify the numbers above:

1. **`iv-percentile-zscore` silently returned 77 sessions for a 252-day
   request** (`dates_used: 77`). The tool correctly reports its own N rather
   than interpolating — quoted as 77 throughout per the gap-aware rule.
2. **`cumulative-premium-flow --days 90` returned 78 `dates_covered` spanning
   2026-03-13 → 2026-07-31 — a window that crosses the 21-session hole**
   (2026-03-28 → 2026-04-24). The cumulative sums are valid; no rate or trend
   may be fitted across the discontinuity.
3. **`signal-backtest` returns `win_rate` as a string** (`"100.0%"`), not a
   float. Numeric comparison against a raw parse would fail silently.
4. **`gex-time-series` returns `zero_gamma_level: null` on 7 of 12 recent
   sessions**, so the trajectory is intermittent.
5. **`dark_pool_accumulation` returned the empty stub on both runs** —
   recorded as a genuine zero, not a transient.
6. **Latest-anchor caveat.** Every command in this phase except `vrp`'s IV leg
   is trailing and anchors to the **latest available date**, which today
   equals the as-of date (2026-07-31, confirmed in `phase-0-intake.md`). On a
   historical as-of re-run all of these would shift. Not reproducible as-of.

## DATA NOTE / CORRECTION

No correction to prior phases. One apparent conflict was investigated and
**resolved as a false alarm**: `fz` reports `Volatility M` **4.31%** against
UW's `realised_vol` **0.3791** (≈2.39%/day), an apparent 1.8× disagreement.
DuckDB reconciles them — average daily **high-low range** is **4.47%** (matching
`fz`) while average absolute **close-to-close** move is **1.99%** (matching
UW). Different metrics, both correct. **UW's VRP stands and was independently
verified at 0.3821 vs its reported 0.3791.** Phase 10 should not flag this.

The practical residue is real, though: intraday movement runs ~2.2× the
close-to-close measure, so a short-premium position will take more heat than
the VRP headline implies.

## Verdict for downstream phases

- **Volatility regime: RICH.** IV30d 0.7378 against verified 30-day realized
  0.3821 — options price **1.93×** delivered vol, and realized vol is falling
  (60d 0.5821 → 20d 0.3732). Reinforced by phase-4's **COMPLACENT** skew and
  **FLAT** front-end ratio. The one qualification is that `iv_percentile`
  71.43 rests on 77 sessions, and phase-0.5 found IV rank 81.94 is only
  FSLR's **39.4th self-percentile** — rich versus *realized*, ordinary versus
  its *own history*.
- **Environment: PREMIUM-SELLING.** Unambiguous, and the phase's most robust
  finding. Favour **credit structures**; debit structures start with a
  ~93% vol headwind. Phase 4's Aug-21 IV hump (79.6%, the ex-0DTE maximum) is
  the richest point on the curve.
- **Conviction that today's signal is HISTORICALLY EDGE-POSITIVE: 2 / 5.**
  Deliberately low. In favour: OI BUILDING (+184,105, 10 straight days), the
  ZGL collapsing to within 1.9% of spot, price basing after the decline, and
  phase-2's five-session accumulation flip. Against: **90-day cumulative flow
  is +0.77% of gross — no stealth build**; the stock is **−18.1% over 30
  sessions with 19 bearish days**; P/C z-score shows **no** sentiment extreme;
  the matching `dark_pool_accumulation` backtest has **zero** historical
  firings; and the `bullish_flow` 100% win rate is in-sample on n=9. **The
  bullish case is structural and current, not historically validated.**
- **Three specific data points:**
  1. **IV percentile 71.43** (N=77, not 252) · `iv_zscore` +0.751 · regime
     NORMAL
  2. **VRP +0.3587** (IV 0.7378 − realized 0.3791; verified 0.3821) —
     PREMIUM_SELLING
  3. **`bullish_flow` win rate 100.0% on n = 9** — in-sample, market-wide,
     below the confidence floor
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:              bullish_flow
  signal_backtest_win_rate:  1.00
  win_rate_n:                9
  win_rate_source:           backtest
  ```
  **Mandatory qualifications on this block:**
  - `dark_pool_accumulation` — the class matching phase-2's dominant
    verdict — returned `total_signals = 0` on two runs;
    `win_rate_source = null` for that class.
  - **`win_rate_n = 9` is below the 10-firing floor.** The N-conditional cap
    in `rubrics/sizing-rubric.md` must be applied at its most restrictive.
  - The rate is **market-wide, not FSLR-specific**, and the tool declares
    itself **in-sample**.
  - **Recommendation: phase 9 should fall back to the conviction bin rather
    than size on p = 1.00.** A Kelly fraction computed from a 100% in-sample
    win rate on 9 market-wide observations would produce a catastrophic
    over-size.
- **Open questions:**
  - **Does 217.50 hold on a second test?** Today's high of 217.1274 stopped
    0.17% short and gave back 6.10 points. One rejection is a level; two is
    resistance. This is the single most actionable follow-up.
  - **Does spot cross the 215.03 ZGL?** `regime_flip_dates` is null for 30
    sessions, but the flip has moved from ~300 to 1.9% away. A cross would be
    the first in the observable window and should expand realized vol —
    which would simultaneously **compress the VRP that underwrites the
    premium-selling verdict.** The two central conclusions of this phase are
    therefore linked: a breakout invalidates the vol trade.
  - **Why is 90-day net flow flat while 30-day OI builds +184,105?** Positions
    are being established without directional premium commitment — consistent
    with **spread and structure trading** (phase-1's LEAP roll, phase-3's
    far-call / near-put shape) rather than outright directional bets.
  - **Is Beta 1.76 into the worst-performing sector an acceptable risk?**
    Phase 6 must resolve whether Technology's −$187.7M is index hedging or
    genuine rotation before phase 9 sizes anything.
