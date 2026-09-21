# Phase 5 — Historical Context & VRP

**Ticker:** MU
**As-of date:** 2026-07-28
**Generated:** 2026-07-28T22:06:00-04:00
**Upstream phases cited:** `phase-0-intake.md` (gap), `phase-0.5-context.md`, `phase-1-flow.md`, `phase-2-dark-pool.md`, `phase-4-structure.md`

## Summary

**The single most important historical finding is that MU's options are CHEAP, not rich — and
the whole market is trading them as if the opposite were true.** `vrp = -0.1308` with
`regime = "PREMIUM_BUYING"` and the tool's own words *"Vol cheap vs realised — favour premium
buying"*: 30-day **realised vol is 109.12% against IV30 of 96.04%**. Yet phase-1 measured
customers **net selling $120M of premium** into exactly that. **They are systematically selling
volatility that is already 13 vol-points too cheap** — a negative-edge trade, and the sharpest
internal contradiction in this run. Reinforcing it, `iv_percentile` is **48.65** (z-score
+0.365, `regime = "NORMAL"`) over the 74 sessions actually present: **MU's IV is at its own
median despite a -32.4% drawdown**, and `iv_rank_change` over the 30-session window is
**100 → 83.4835 while price fell 1087.99 → 820.53 (-24.6%)** — **implied vol went DOWN during a
25% decline.**

The regime read is unambiguous and stable: GEX has printed **`FULLY_NEGATIVE` on three
consecutive sessions (7/24, 7/27, 7/28)**, and the tool flags a **regime flip on 2026-07-23**
(POSITIVE → NEGATIVE, spot 988.43) — after which MU fell **-6.99%, -2.25%, -8.85% = -17.1% in
three sessions**, precisely the "realised-vol expansion" the tool says flips precede. Open
interest is `overall_trend = "BUILDING"` with **30 of 30 consecutive build days**. And the
price-context cross-check kills the reflexive dip-buy: **RSI 40.29 is not oversold**, MU sits
**-13.44% below its 20-DMA and -14.37% below its 50-DMA but still +61.28% ABOVE its 200-DMA**,
**-34.62% from the 52-week high yet +187.49% YTD and +637.56% on the year**, with **ATR 83.13 —
a 10.1% daily true range.**

## Key signals

- **`vrp = -0.1308`, `regime = "PREMIUM_BUYING"`** — RV30 **109.12%** > IV30 **96.04%**.
  [HIST:vrp]
- **`iv_percentile = 48.65`, `iv_zscore = 0.365`, `regime = "NORMAL"`, `dates_used = 74`** —
  median IV after a 32% drawdown. [HIST:iv_percentile_zscore]
- **GEX `FULLY_NEGATIVE` 3 sessions running; `regime_flip_dates` includes 2026-07-23** →
  -17.1% over the next three sessions. [HIST:gex_time_series]
- **90-day cumulative flow is a dead heat**: bullish **$100,571,622,792** vs bearish
  **$100,250,961,532** → `net_flow` **+$320,661,260** (**+0.16% of gross**),
  `trend_direction = "MIXED"`. [HIST:cumulative_premium_flow]
- **`overall_trend = "BUILDING"`, `consecutive_build_days = 30/30`**,
  `total_net_oi_change = +4,851,744`. [HIST:oi_trend]
- **`signal-backtest bearish_flow`: `win_rate = "80.0%"`, `total_signals = 10`,
  `avg_move_pct = -5.91`** — but market-wide and in-sample. [HIST:signal_backtest]
- **`bullish_flow`: `win_rate = "66.7%"` yet `avg_move_pct = -2.69`** — positive hit rate,
  **negative expectancy**. [HIST:signal_backtest]
- **RSI 40.29 — NOT oversold; +61.28% above the 200-DMA; ATR 83.13 (10.1%).**
  [HIST:rsi fz] [HIST:52w_proximity fz]

## Detailed findings

### IV regime (percentile + z-score + VRP)

`uw historical iv-percentile-zscore --symbol MU --lookback-days 252`:

| field | value |
|---|---:|
| `current_iv30d` | 0.9604 |
| **`iv_percentile`** | **48.65** |
| `iv_zscore` | +0.365 |
| **`regime`** | **`NORMAL`** |
| **`dates_used`** | **74** (not 252 — see gap note) |

`uw historical vrp --symbol MU --realised-window-days 30`:

| field | value |
|---|---:|
| `iv30d` | 0.9604 (96.04%) |
| **`realised_vol`** | **1.0912 (109.12%)** |
| **`vrp`** | **-0.1308** |
| **`regime`** | **`PREMIUM_BUYING`** |
| `interpretation` | *"Vol cheap vs realised — favour premium buying."* |

**This is the phase's headline and it inverts the naive structural read.** MU's options screen
"expensive" on any absolute measure (IV30 96%, IV rank 83.5) — but the stock is *actually
moving* 109% annualised. **Implied vol is 13.1 points BELOW realised.** Per the interpretation
heuristic (`IV cheap + VRP < 0` → premium-BUYING regime → favour debit structures), the
historically correct posture is **long premium, not short**.

**Three corroborations that this is real and not a one-day artifact:**
1. `iv_percentile` **48.65** — the median of MU's own distribution. Matches `phase-0.5`'s
   independent finding that IV rank 83.48 is only the **43rd self-percentile**.
2. `iv_rank_change` over the trend window: **100 → 83.4835** while **price fell -24.6%**. Vol
   *compressed* through a quarter-scale decline — the opposite of normal crash behaviour.
3. `phase-4-structure.md` found **`term_skew` = `NORMAL` (ratio 1.053)** — no crash premium
   either. Three independent lenses agree the vol surface is complacent.

**The contradiction to flag for phase 10:** `phase-1-flow.md` measured customers **net selling
$120.08M of premium** (LEAP puts -$68.1M, 46–180DTE calls -$51.9M) into a market where realised
exceeds implied by 13 vol points. Whatever the sellers' motive (income, overwriting, financing),
**they are short vol at a negative-carry price.** In a `FULLY_NEGATIVE` gamma regime
(phase-4) with a 10.1% ATR, that is a structurally fragile position.

### Cumulative premium flow (90d)

`uw historical cumulative-premium-flow --symbol MU --days 90` — `days = 90` requested,
**`dates_covered` length = 75** (the full available window; see gap note):

| field | value |
|---|---:|
| `cumulative_bullish` | $100,571,622,792 |
| `cumulative_bearish` | $100,250,961,532 |
| **`net_flow`** | **+$320,661,260** |
| **`trend_direction`** | **`MIXED`** |

**$200.8B of gross two-way premium over 75 sessions nets to +$320.7M — a tilt of +0.16%.**
This is the multi-month generalisation of phase-1's single-day finding (+1.0% net on $2.83B):
**MU's options tape has no persistent directional lean and never has.** Per the interpretation
heuristic, a "stealth institutional build" requires cumulative flow positive **and persistent**
≥60d — MU fails the persistence test outright with `trend_direction = "MIXED"`.

**Consequence for phase 9: any thesis resting on "institutions are accumulating MU through
options" is refuted by 75 sessions of data.** They are trading it two-way in enormous size.

### P/C ratio z-score

`uw historical pc-ratio-zscore --symbol MU --lookback-days 20`:

| field | value |
|---|---:|
| `current_pc_ratio` | 0.8671 |
| `mean_pc_ratio` | 1.0271 |
| `std_pc_ratio` | 0.1291 |
| **`zscore`** | **-1.239** |
| **`extreme`** | **`NORMAL`** |

Today's P/C of 0.867 sits **1.24 SD below** its 20-session mean of 1.027 — relatively
*call-heavy* versus MU's recent norm, but **short of the |z| > 2 contrarian threshold**. No
sentiment extreme; no contrarian setup on this axis. Mildly notable that on an -8.85% day the
P/C ratio *fell* rather than spiking — consistent with the "no panic" theme running through the
vol surface.

### GEX time series (regime stability)

`uw historical gex-time-series --symbol MU --days 30 --dte-max 45` (`days_analyzed = 30`).
The tool's note: *"Regime flips identify dates where spot crossed the zero-gamma level.
Empirically precedes realised-vol expansion."*

**`regime_flip_dates`:**

| date | from → to | spot | ZGL | `zgl_delta` |
|---|---|---:|---:|---:|
| 2026-06-23 | POSITIVE → NEGATIVE | 1053.58 | 1495.20 | +300.04 |
| 2026-06-24 | NEGATIVE → POSITIVE | 1032.89 | 35.13 | -1460.07 |
| **2026-07-23** | **POSITIVE → NEGATIVE** | **988.43** | 1048.93 | +1018.96 |

**Trajectory (last 12 sessions):**

| date | `total_gex` | `zero_gamma_level` | `regime` | close | chg |
|---|---:|---:|---|---:|---:|
| 2026-07-13 | -30,339,260 | 5.00 | POSITIVE | 937.00 | -4.32% |
| 2026-07-14 | -6,068,860 | 41.91 | POSITIVE | 983.12 | +4.92% |
| 2026-07-15 | -67,435,734 | 70.13 | POSITIVE | 904.28 | -8.02% |
| 2026-07-16 | -70,524,218 | 45.52 | POSITIVE | 853.20 | -5.65% |
| 2026-07-17 | -69,027,904 | 63.68 | POSITIVE | 848.95 | -0.50% |
| 2026-07-20 | -31,892,899 | `null` | **FULLY_NEGATIVE** | 865.46 | +1.94% |
| 2026-07-21 | **+10,331,552** | 51.45 | POSITIVE | 970.82 | **+12.17%** |
| 2026-07-22 | +7,448,258 | 29.97 | POSITIVE | 959.48 | -1.17% |
| **2026-07-23** | +16,580,824 | 1048.93 | **NEGATIVE** (flip) | 990.21 | +3.20% |
| **2026-07-24** | -32,956,046 | `null` | **FULLY_NEGATIVE** | 920.95 | **-6.99%** |
| **2026-07-27** | -48,427,271 | `null` | **FULLY_NEGATIVE** | 900.20 | -2.25% |
| **2026-07-28** | **-45,676,585** | `null` | **FULLY_NEGATIVE** | 820.53 | **-8.85%** |

- **The 2026-07-23 flip is a live, working example of the tool's own claim.** Spot crossed below
  the ZGL on 7/23 and MU then fell **-6.99%, -2.25%, -8.85% — -17.1% in three sessions.**
- **MU has now been `FULLY_NEGATIVE` for three consecutive sessions**, the longest such run in
  the window, with `total_gex` deepening from -32.96M → -48.43M → -45.68M. The 7/28 value
  (-45,676,585) reconciles with phase-4's independent read (-45,676,510) to within 0.0002%.
- **Data-quality caveat (important):** the `regime` label is derived from spot-vs-ZGL, and the
  ZGL computation is visibly degenerate on several dates — **ZGL values of 5.00, 41.91, 45.52,
  63.68, 29.97 on an $850–980 stock are not credible zero-gamma levels.** Those sessions are
  labelled "POSITIVE" purely because spot > a near-zero ZGL, while `total_gex` was
  simultaneously **-30M to -70M**. **Trust `total_gex`'s sign and the `FULLY_NEGATIVE` label;
  distrust the "POSITIVE" labels attached to a sub-$100 ZGL.** Read this way, MU's `total_gex`
  was negative on **10 of the last 12 sessions** — the negative-gamma regime is far more
  persistent than the label column suggests.

### OI trend

`uw historical oi-trend --symbol MU --days 30 --top-n 10`:

| field | value |
|---|---:|
| **`overall_trend`** | **`BUILDING`** |
| **`consecutive_build_days`** | **30** (of 30 analysed) |
| `total_net_oi_change` | **+4,851,744** |
| 2026-07-28 `net_oi_change` | +128,274 |
| 2026-07-28 `contracts_with_increases` / `decreases` | 3,141 / 1,087 |

**Open interest has increased on every one of the last 30 sessions** — a sustained build, not a
spike. Today alone added +128,274 contracts net across 3,141 contracts rising vs 1,087 falling
(a 2.9:1 breadth ratio).

*Caveat on `total_net_oi_change` = +4,851,744:* this exceeds MU's entire current open interest
of 2,194,370 (phase-3 `term-structure`). The two reconcile because contracts **expiring** remove
OI without registering as a "decrease" in the changes dataset, so a 30-day sum of daily net
changes can exceed the standing total. Quoted verbatim; **read it as "OI built every day," not
as a stock figure.**

The top contracts driving today's build are the same ones phase-3 identified — 55P Aug-07
(+24,412), 500P Jul-31 (+11,767), 95P Jul-31 (+4,352), 570P Jul-29 (+3,689) — i.e.
**the build is concentrated in cheap downside tails**, plus the 1–3 DTE call lottery
(880C +2,735, 875C +2,635).

### Multi-day trend table

`uw historical trend --symbol MU --days 30` — `days_analyzed = 30`,
`date_range = "2026-06-15 to 2026-07-28"`:

| field | value |
|---|---|
| `bullish_days` / `bearish_days` | **17 / 13** |
| `flow_direction_latest` | `bullish` |
| **`iv_rank_change`** | **100 → 83.4835** |
| **`price_change`** | **1087.99 → 820.53** (**-24.6%**) |

**Daily (most recent 8; note `daily_data` is returned in DESCENDING date order):**

| date | close | P/C | IV rank |
|---|---:|---:|---:|
| 2026-07-28 | 820.53 | 0.867 | 83.48 |
| 2026-07-27 | 900.20 | 0.991 | 79.88 |
| 2026-07-24 | 920.95 | 1.234 | 82.52 |
| 2026-07-23 | 990.21 | 1.110 | 85.55 |
| 2026-07-22 | 959.48 | 1.028 | 89.45 |
| 2026-07-21 | 970.82 | 1.207 | 90.32 |
| 2026-07-20 | 865.46 | 1.076 | 94.65 |
| 2026-07-17 | 848.95 | 0.912 | 91.91 |

**17 bullish days against 13 bearish while price fell 24.6%** is the cleanest possible statement
that **flow direction has had no predictive relationship to MU's price this month.** It also
means `flow_direction_latest = "bullish"` carries essentially no information — phase-9 must not
cite it.

### Price context (`fz` — independent EOD cross-check)

`fz quote MU` remains degraded (14/84 fields, per `phase-0-intake.md`), so RSI/SMA/52W were
sourced from `fz screen --view technical` and `--view performance`:

| technical | value | | performance | value |
|---|---:|---|---|---:|
| **`RSI`** | **40.29** | | **`Perf Week`** | **-15.48%** |
| `SMA20` | **-13.44%** | | **`Perf Month`** | **-27.54%** |
| `SMA50` | **-14.37%** | | `Perf Quart` | **+56.42%** |
| **`SMA200`** | **+61.28%** | | `Perf Half` | +110.88% |
| **`52W High`** | **-34.62%** | | **`Perf YTD`** | **+187.49%** |
| `52W Low` | +693.70% | | **`Perf Year`** | **+637.56%** |
| **`ATR`** | **83.13** | | `Volatility W` / `M` | 6.75% / 6.91% |
| `Beta` | **2.20** | | `Rel Volume` | 1.17 |
| `Gap` | -6.73% | | `Change from Open` | -2.27% |

`[HIST:rsi fz]` `[HIST:52w_proximity fz]` — **advisory only; does not enter the Kelly `p`.**

**This is the most important context for anyone tempted to buy the dip:**
- **RSI 40.29 is NOT oversold.** After -15.5% on the week and -27.5% on the month, MU has not
  even reached the conventional 30 threshold. There is no momentum-exhaustion signal.
- **MU is still +61.28% ABOVE its 200-day SMA** while sitting -13.4%/-14.4% below the 20- and
  50-day. The intermediate trend has broken; **the long-term trend has enormous unwound
  extension left.** A mean-reversion to the 200-DMA implies roughly **-38%** from spot.
- **+187.49% YTD and +637.56% on the year** — a -32.4% drawdown has retraced only a fraction of
  a parabola. Phase-0.5's local trough close was **355.46 (2026-03-26)**.
- **ATR 83.13 = 10.1% of spot**, with weekly/monthly realised volatility of 6.75%/6.91% and
  **Beta 2.20**. This independently confirms phase-4's warning: **any stop tighter than ~10% is
  inside a single average day's range.**
- `Gap -6.73%` with `Change from Open -2.27%` — MU **gapped down and then kept falling**, closing
  weak rather than reversing. Corroborates phase-2's dark-pool distribution and after-hours
  slide to $780.

### Signal backtest

Phase-2 (dark-pool **DISTRIBUTION**, conviction 4/5) and phase-4 (short gamma, conviction 4/5)
are the run's dominant signals, so `dark_pool_accumulation` and the directional flow classes
were all tested:

| `--signal-type` | `win_rate` | `total_signals` | `avg_move_pct` |
|---|---:|---:|---:|
| **`bearish_flow`** | **80.0%** | **10** | **-5.91** |
| `bullish_flow` | 66.7% | 6 | **-2.69** |
| `dark_pool_accumulation` | — | **0** | — |

- **`dark_pool_accumulation` returned the empty stub** — `{"note":"no backtest results",
  "signal_type":"dark_pool_accumulation","total_signals":0}` — and was **re-run once per
  composition guidance, returning the identical stub.** Recorded as genuinely empty. *(It is
  also the wrong polarity for this run: phase-2 found distribution, not accumulation.)*
- **`bearish_flow`: `win_rate` 80.0% on n=10, `avg_move_pct` -5.91.** Both hit rate and
  expectancy are favourable.
- **`bullish_flow` is the cautionary result: a 66.7% `win_rate` on n=6 but `avg_move_pct` of
  -2.69%.** A majority of bullish-flow signals "won" while the average forward move was
  **negative** — the losers were far larger than the winners. **A positive hit rate with
  negative expectancy.** Given MU's headline is "+$1.43B bullish premium, #8 in the universe,"
  this is precisely the trap phase-9 must avoid: *the bullish-flow signal class does not pay,
  even when it is right more often than not.*

**Four caveats that materially limit this as a Kelly input** (all from the tool's own output or
the composition guidance):
1. **`methodology_notes`: *"In-sample backtest — not a robust live edge."*** The tool disclaims
   itself.
2. **Market-wide, not MU-specific** — `signal-backtest` takes no `--symbol`, so this is the base
   rate of the signal class **across the whole tape**, not MU's own record.
3. **n = 10 sits exactly at the low-confidence boundary** (the pitfall flags <10 firings as
   low-confidence).
4. **Class mismatch.** `bearish_flow` is a *flow* signal, but **phase-1's flow was MIXED, not
   bearish** — MU's bearish evidence comes from the dark pool and gamma structure, not from
   directional options flow. **The 80% is therefore an imperfect proxy**, and phase-9 should
   apply the N-conditional cap and treat it conservatively.

### Gap-aware N (mandatory)

Per `phase-0-intake.md`, the local window is **non-contiguous: 75 sessions spanning 2026-03-13
→ 2026-07-28 with a 31-day hole (2026-03-27 → 2026-04-27).** Actual N used, taken from each
tool's own session count rather than the calendar span:

| tool | requested window | **actual N** |
|---|---|---:|
| `iv-percentile-zscore` | 252 days | **`dates_used` = 74** |
| `cumulative-premium-flow` | 90 days | **`dates_covered` = 75** |
| `trend` | 30 days | `days_analyzed` = 30 (`date_range` 2026-06-15→07-28, post-gap, clean) |
| `oi-trend` | 30 days | `days_analyzed` = 30 (post-gap, clean) |
| `gex-time-series` | 30 days | `days_analyzed` = 30 (post-gap, clean) |
| `pc-ratio-zscore` | 20 days | 20 (post-gap, clean) |

**The two windows that cross the hole are `iv-percentile-zscore` (74 sessions, not 252) and
`cumulative-premium-flow` (75, not 90).** The 252-day IV percentile is therefore computed over
**less than 30% of the requested calendar span**, all of it within a single extraordinary
5-month regime in which MU ran from 355 to 1,214 and back to 820. **`iv_percentile = 48.65`
means "median for MU during the parabola and its unwind," not "median for MU historically."**
This materially widens the uncertainty on the vol-cheapness conclusion — though note VRP itself
is computed on a clean 30-session realised window and does not depend on the long lookback.

The 30- and 20-day windows sit entirely **after** the gap (earliest 2026-06-15) and are clean.

**Latest-anchor caveat:** every tool in this phase except `vrp`'s IV leg is trailing and
anchors to the **latest available date, which is 2026-07-28 — identical to this run's as-of
date**, so all reads are point-in-time correct here. A re-run after 2026-07-29 lands will shift
every z-score, percentile, build-day count and win-rate.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|------------------|--------------------------|-----------|
| `uw historical iv-percentile-zscore --symbol MU --lookback-days 252 --json` | **iv_percentile=48.65**; iv_zscore=0.365; regime=`NORMAL`; current_iv30d=0.9604; **dates_used=74** | top-level |
| `uw historical vrp --symbol MU --realised-window-days 30 --json` | **vrp=-0.1308**; realised_vol=**1.0912**; iv30d=0.9604; regime=**`PREMIUM_BUYING`** | top-level |
| `uw historical cumulative-premium-flow --symbol MU --days 90 --json` | bullish=100,571,622,792; bearish=100,250,961,532; **net_flow=+320,661,260**; trend_direction=**`MIXED`**; dates_covered len=75 | 75 sessions |
| `uw historical pc-ratio-zscore --symbol MU --lookback-days 20 --json` | current=0.8671; mean=1.0271; std=0.1291; **zscore=-1.239**; extreme=`NORMAL` | 20 sessions |
| `uw historical gex-time-series --symbol MU --days 30 --dte-max 45 --json` | flips 06-23, 06-24, **07-23**; 7/28 total_gex=**-45,676,585**, zgl=`null`, regime=`FULLY_NEGATIVE` ← `.regime_flip_dates`, `.trajectory[]` | 30 sessions |
| `uw historical oi-trend --symbol MU --days 30 --top-n 10 --json` | **overall_trend=`BUILDING`**; **consecutive_build_days=30**; total_net_oi_change=+4,851,744; 7/28 net=+128,274 (3,141 up / 1,087 down) | 30 sessions |
| `uw historical trend --symbol MU --days 30 --json` | bullish_days=17 / bearish_days=13; **iv_rank_change="100 -> 83.4835"**; **price_change="1087.99 -> 820.53"**; date_range 06-15→07-28 ← `.daily_data[]` (DESC order) | 30 sessions |
| `uw historical signal-backtest --signal-type bearish_flow --lookback-days 5 --top-n 20 --json` | **win_rate="80.0%"**, **total_signals=10**, avg_move_pct=-5.91 (top-level fields) | market-wide |
| `uw historical signal-backtest --signal-type bullish_flow …` | win_rate="66.7%", total_signals=6, **avg_move_pct=-2.69** | market-wide |
| `uw historical signal-backtest --signal-type dark_pool_accumulation …` (×2) | `{"note":"no backtest results","total_signals":0}` — **re-run confirmed** | market-wide |
| `fz screen --tickers MU --view technical --agent` | **RSI=40.29**; SMA20=-13.44%; SMA50=-14.37%; **SMA200=+61.28%**; **ATR=83.13**; Beta=2.20; 52W High=-34.62%; Gap=-6.73% ← `.[0]` | 1 row |
| `fz screen --tickers MU --view performance --agent` | Perf Week=-15.48%; **Perf Month=-27.54%**; Perf YTD=+187.49%; Perf Year=+637.56%; Volatility W/M=6.75%/6.91% | 1 row |

## Tool errors

No command errored; all exited 0. Three **degradations / data-quality issues** recorded:

1. **`gex-time-series` returns degenerate `zero_gamma_level` values** — 5.00, 41.91, 45.52,
   63.68, 29.97, 51.45 on a stock trading $850–990. Because `regime` is derived from
   spot-vs-ZGL, those sessions are mislabelled **"POSITIVE"** while `total_gex` was
   simultaneously **-30M to -70M**. Surfaced as a data-quality caveat per the phase instruction;
   conclusions here rest on the **sign of `total_gex`** and the `FULLY_NEGATIVE` label, not on
   the ZGL column.
2. **`signal-backtest --signal-type dark_pool_accumulation` returns the empty stub**
   (`total_signals: 0`) on both the initial call and the mandated re-run.
3. **`fz quote MU` remains degraded** (14 of 84 fields; no RSI/SMA/52W/Perf — carried from
   `phase-0-intake.md`). The phase-5 `fz` cross-check specified in the instructions
   (`fz quote … | jq '{rsi, sma50, sma200, perf_ytd, high52, low52}'`) **would have returned all
   nulls**; it was re-sourced from `fz screen --view technical` and `--view performance`, which
   returned complete data. Values above come from those views.

## DATA NOTE / CORRECTION

Field-path corrections made **before** any number was written:

1. **`gex-time-series` series lives at `.trajectory`**, not `.series`/`.results`/`.data` — the
   first read aborted with `Cannot iterate over null (null)`.
2. **`trend` daily rows live at `.daily_data`** (not `.trend`/`.series`) **and are returned in
   DESCENDING date order.** The first read of `[-8:]` returned the *oldest* eight rows
   (2026-06-15…06-25) and was initially mistakable for recent data; re-read as `[0:8]` for the
   most recent sessions. The table above is the corrected, recent set. **`total_premium` does
   not exist on these rows** — the fields are `date`, `close`, `iv_rank`, `put_call_ratio`.
3. **`fz screen` rows again return `"Ticker":"MMU"`** (the mangled-ticker quirk from
   `phase-0-intake.md`). `Price = 820.53` and `Change = -8.85%` match the UW screener close
   exactly, confirming the row is MU's; the `Ticker` field itself remains untrustworthy.

No value in this file was transcribed from an unparsed or failed read.

## Verdict for downstream phases

- **Volatility regime: CHEAP.** `vrp = -0.1308` (RV 109.12% vs IV 96.04%), `regime =
  PREMIUM_BUYING`, `iv_percentile = 48.65`, `regime = NORMAL`. Despite headline IV of 96% and IV
  rank 83.5, **MU's options are underpriced relative to how the stock is actually moving.**
- **Environment: PREMIUM-BUYING → favour DEBIT structures.** Phase-9 should prefer long-premium
  expressions (debit spreads, outright long options) over credit/short-vol structures. **This
  directly contradicts what the tape did today** (phase-1: customers net sold $120M of premium)
  and that contradiction is the run's key insight.
- **Conviction that today's signal is HISTORICALLY EDGE-POSITIVE: 2 / 5 (low).** The dominant
  bearish read (phase-2 distribution + phase-4 short gamma) maps only imperfectly onto a
  backtestable class: `dark_pool_accumulation` is empty, and `bearish_flow`'s 80% is
  market-wide, in-sample, n=10, and describes a *flow* signal that **phase-1 did not actually
  produce** (flow was MIXED). Meanwhile the class that *does* match MU's headline —
  `bullish_flow` — carries **negative expectancy (-2.69%)**. The honest read: **the historical
  record does not validate a high-conviction directional bet in either direction.**
- **Three specific datapoints:**
  1. **IV percentile = 48.65** (z +0.365, `NORMAL`, over 74 actual sessions)
  2. **VRP = -0.1308** (realised 1.0912 vs implied 0.9604) → `PREMIUM_BUYING`
  3. **Signal win rate = 80.0% on n=10** (`bearish_flow`, market-wide, in-sample,
     avg_move -5.91%)
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:              bearish_flow
  signal_backtest_win_rate:  0.80
  win_rate_n:                10
  win_rate_source:           backtest
  ```
  **Mandatory qualifiers phase-9 must carry into the Kelly calculation** (per
  `rubrics/sizing-rubric.md` §"Choosing the Kelly `p`"):
  - This is a **market-wide base rate**, not MU-specific — `signal-backtest` accepts no
    `--symbol`.
  - The tool self-disclaims: **"In-sample backtest — not a robust live edge."**
  - **n = 10 is at the low-confidence floor** → apply the N-conditional cap; do not size on a
    raw 0.80.
  - **Class-match is imperfect**: phase-1's flow verdict was **MIXED**, not `bearish_flow`. The
    bearish thesis rests on phase-2/phase-4, for which no backtest exists
    (`dark_pool_accumulation` = 0 signals).
  - Cross-reference: `bullish_flow` won 66.7% of the time with **-2.69% average move** —
    evidence that hit rate alone is a poor guide on this signal family.
- **Open questions:**
  - **Why is implied vol below realised, and why did IV *fall* through a -24.6% decline?** Is
    the market genuinely relaxed about MU (orderly rotation) or is vol mispriced with a
    `FULLY_NEGATIVE` gamma regime underneath? **→ phase-6 (catalyst calendar: does FOMC 7/28–29
    or a memory event justify buying cheap vol?), phase-8b (this is the crux).**
  - **Does the vanna-squeeze setup (phase-4) survive a negative VRP?** A vanna squeeze needs IV
    to *fall*; but IV is already below realised, so further compression is unlikely absent a
    genuine calm. **The two bullish structural arguments may be mutually exclusive.**
  - **Is the 200-DMA (+61.28% below spot) a realistic downside objective, or is the parabola's
    base too far to matter on a 1–3 month horizon?** → phase-8/9 must bound the tail.
  - `signal-backtest` has no MU-specific mode — is there a DuckDB cut that could build a
    name-specific win rate from the 75-session local window? Out of scope here; **flagged for
    `/deep-dive-calibration`.**
