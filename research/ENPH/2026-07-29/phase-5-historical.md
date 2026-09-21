# Phase 5 — Historical Context & VRP

**Ticker:** ENPH
**As-of date:** 2026-07-29
**Generated:** 2026-07-30T02:18:00Z
**Upstream phases cited:** `phase-0-intake.md`, `phase-0.5-context.md`, `phase-1-flow.md`, `phase-2-dark-pool.md`, `phase-3-positioning.md`, `phase-4-structure.md`

## Summary

**Today is session 26 of an established short-gamma downtrend, not a fresh event.**
`gex-time-series` shows `total_gex` turning negative on **2026-06-23** and staying negative
for **26 consecutive sessions**, over which spot fell **47.94 → 36.08 (−24.7%)**. Across the
30-session window `trend` reports `price_change` **50.26 → 35.07 (−30.2%)** with
**`bearish_days` 21 vs `bullish_days` 9**. Phase 4's short-gamma read is not a one-day
artifact — it is a five-week structural state that has already amplified a 30% decline.

**The single most valuable historical pattern: ENPH's big bullish premium spikes are
premium-sellers getting run over, and they are 3-for-3 wrong.** Cumulative `net_flow` over
30 sessions is **+$2,051,489 — essentially flat — despite 21 of 30 days printing bearish**,
because three large positive outliers offset dozens of small negatives. Every one was
followed by lower prices:

| Spike date | `net_flow` | Close | Outcome |
|---|---|---|---|
| 2026-06-17 | +$3,170,190 | 47.78 | → 43.07 by 07-02 (**−9.9%**) |
| 2026-07-16 | +$5,629,548 | 41.08 | → 39.46 by 07-20 (**−3.9%**) |
| 2026-07-23 | +$5,904,530 | 38.89 | → 35.07 by 07-29 (**−9.8%**) |

`phase-1-flow.md` established the 07-23 spike was **put *selling*** (`put_ask_bid_x` 0.508).
So the "bullish" premium in this name is short-vol yield harvesting, not accumulation — and
it has been repeatedly wrong. **Phase 9 must not read a bullish premium print in ENPH as an
accumulation signal.**

**Vol is cheap by percentile and rich by realized — and both are true.**
`iv-percentile-zscore` gives `iv_percentile` **28**, `iv_zscore` **−0.658**, `regime`
**NORMAL** (`current_iv30d` 0.797). But `vrp` gives `iv30d` 0.797 vs `realised_vol` 0.6703
→ **`vrp` +0.1267**, `regime` **PREMIUM_SELLING**. The reconciliation: realized vol has
fallen alongside implied, so IV sits low in its own range while still ~12.7 vol points above
trailing realized. **Caveat that matters:** `realised_vol` is a 30-day trailing figure that
mostly predates the event — today alone realized a **12.8% range**
(`phase-1-flow.md` §C). If ENPH keeps moving like this, realized catches up and the VRP
edge evaporates.

**Independent cross-source confirmation of the gap-and-crap.** `fz` technical view — a
completely separate data provider — returns `Gap` **+7.08%** and **`Change from Open`
−9.82%**, with `Change` −3.44%. That reproduces `phase-1-flow.md`'s OHLC finding (high
39.60, close 35.07, −11.44% from high) from non-UW data. `RSI` **31.60**, and price is below
all three moving averages: **SMA20 −15.38%, SMA50 −30.49%, SMA200 −12.34%**. `ATR` **3.24 =
9.2% of spot** — critical for phase 9 stop placement.

**The signal backtest returns a headline that must not be taken at face value.**
`bearish_flow` → `win_rate` **"100.0%"**, `total_signals` **9**, `avg_move_pct` **−14.59%**.
But the tool's own `methodology_notes` say *"In-sample backtest — not a robust live edge"*;
N=9 is **below the spec's 10-firing confidence floor**; the tool is **market-wide** and its
`results` rows are **TSLA, WOLF, AMD, GLD, MU, SNDK, SOXL, BE — ENPH is not in the sample
at all**; and all nine signals come from just **two dates (07-24 and 07-27)**. Reported
verbatim as the Kelly `p` per the spec, with an explicit instruction to phase 9 to cap it
hard.

**One reconciliation trap resolved:** `oi-trend` reports `overall_trend` **BUILDING** with
`total_net_oi_change` **+201,329** and **8 consecutive build days**, while `trend` shows
`total_open_interest` **falling 510,764 → 381,215 (−25.4%)**. Both are correct — new
positions built while ~330k contracts *expired* at the June and July OPEX. See §F.

## Key signals

- **`total_gex` negative 26 consecutive sessions** (2026-06-23 → 07-29); spot 47.94 → 36.08
  (**−24.7%**) inside that regime [HIST:gex_time_series]
- **`price_change` 50.26 → 35.07 (−30.2%)** over 30 sessions, `bearish_days` **21** /
  `bullish_days` **9** [HIST:trend]
- **Cumulative 30-session `net_flow` +$2,051,489 (flat) despite 70% bearish days** — three
  bullish spikes (06-17, 07-16, 07-23), **all three followed by lower prices**
  [HIST:trend]
- **`iv_percentile` 28, `iv_zscore` −0.658, `regime` NORMAL** on `dates_used` **75**
  (not 252 — see §I) [HIST:iv_percentile_zscore]
- **`vrp` +0.1267** (IV 0.797 vs realized 0.6703), `regime` **PREMIUM_SELLING**
  [HIST:vrp]
- **`fz`: `Gap` +7.08%, `Change from Open` −9.82%** — independent confirmation of the
  intraday reversal; `RSI` **31.60**; `ATR` **3.24 (9.2% of spot)** [HIST:rsi fz]
- **Price below all three SMAs: −15.38% / −30.49% / −12.34%** (20/50/200); **−52.44% from
  the 52-week high** [HIST:52w_proximity fz]
- **`signal-backtest bearish_flow`: `win_rate` "100.0%", `total_signals` 9,
  `avg_move_pct` −14.59%** — but in-sample, market-wide, **ENPH absent from the sample**
  [HIST:signal_backtest]
- **`oi-trend` BUILDING, 8 consecutive build days, today +18,048 (largest of the run)** —
  yet total OI **−25.4%** over 30 sessions [HIST:oi_trend]
- **`pc-ratio-zscore` `zscore` +0.482, `extreme` NORMAL** — no sentiment extreme; this
  **tensions with** phase 0.5's 87.5th self percentile (see §D) [HIST:pc_ratio_zscore]
- **`cumulative-premium-flow` `net_flow` +$25,008,497 over 76 sessions,
  `trend_direction` MIXED** — no stealth institutional build in either direction
  [HIST:cumulative_premium_flow]

## Detailed findings

### A — IV regime (percentile, z-score, VRP)

`uw historical iv-percentile-zscore --symbol ENPH --lookback-days 252`:

| Field | Value |
|---|---|
| `current_iv30d` | **0.797** |
| `iv_percentile` | **28** |
| `iv_zscore` | **−0.658** |
| `regime` | **NORMAL** |
| `lookback_days` (requested) | 252 |
| **`dates_used`** | **75** ⚠ |

`uw historical vrp --symbol ENPH --realised-window-days 30`:

| Field | Value |
|---|---|
| `iv30d` | 0.797 |
| `realised_vol` | **0.6703** |
| **`vrp`** | **+0.1267** |
| `regime` | **PREMIUM_SELLING** |
| `interpretation` | "Options pricing more vol than realised — favour premium selling." |

**These two look contradictory and are not.** IV at the **28th percentile** of its own
history says vol is *cheap relative to ENPH's recent past*; VRP **+12.67 vol points** says
vol is *rich relative to trailing realized*. Both hold because **realized vol fell too** —
IV compressed from a high base while realized compressed alongside it, leaving a positive
spread at a low absolute level. Corroborated by `phase-0.5-context.md`: `iv_rank` 47.05 sits
at ENPH's **15.6th self percentile**, and `iv30d` fell for 8 consecutive sessions
(1.017 → 0.797).

The spec's heuristics split cleanly here and neither fires alone:
- *"IV cheap + VRP < 0 → premium-BUYING"* — IV is cheap (28th pctile) but **VRP is
  positive**, so this does **not** fire.
- *"IV rich + VRP > 0 → premium-SELLING"* — VRP is positive but **IV is not rich**, so
  this does not cleanly fire either.

**Resolution: a mildly premium-selling environment at a low absolute vol level — which is
the worst of both worlds for a directional trader and matters less than the skew.** The
decisive structural fact is phase 4's `skew_ratio` **0.994** (25Δ puts *cheaper* than 25Δ
calls, `interpretation` COMPLACENT). A +12.67 VRP argues generically against buying premium;
a 0.994 skew ratio argues that **if** you buy premium, buy it on the **put** side where you
pay no skew, at the 10-16 expiry (curve trough, `avg_iv` 82.2%, phase 4 §D).

**The VRP caveat that could invert this read.** `realised_vol` 0.6703 is a **30-day
trailing** measure whose window is mostly *pre-event calm*. Today alone realized a **12.8%
range** (high 39.60, low 34.96, `phase-1-flow.md` §C), and `fz` reports `ATR` **3.24 = 9.2%
of spot**. Annualizing a 9.2% daily ATR gives roughly 145% vol — far above the 67% trailing
figure. **If post-event realized vol persists anywhere near today's, the +0.1267 VRP
disappears and premium-selling becomes the wrong side.** The spec's own pitfall applies:
*"VRP can flip on a single catalyst day — read the trailing-5d trend, not just today."* The
trailing `iv30d` trend is unambiguously down (§G); the trailing *realized* trend is about to
turn up.

### B — Cumulative premium flow (90d requested)

`uw historical cumulative-premium-flow --symbol ENPH --days 90`:

| Field | Value |
|---|---|
| `cumulative_bullish` | $441,590,914 |
| `cumulative_bearish` | $416,582,417 |
| **`net_flow`** | **+$25,008,497** |
| **`trend_direction`** | **MIXED** |
| `days` (requested) | 90 |
| **`dates_covered`** | **76 sessions**, 2026-03-13 → 2026-07-29 ⚠ **spans the gap** |

**Gap disclosure (mandatory).** The 90-day request returned **76 actual sessions**, and
**11 of them predate 2026-04-27** (2026-03-13, 03-16, 03-17, 03-18, 03-19, 03-20, 03-23,
03-24, 03-25, 03-26, 03-27). The window therefore **straddles the 21-session hole
2026-03-28 → 2026-04-24** flagged in `phase-0-intake.md`. The cumulative totals are sums
over present sessions — arithmetically valid — but this is **not** a contiguous 90-day
span and must not be described as one, nor annualized.

**Net +$25.0M bullish on $858.2M of gross premium is a +2.9% skew — noise.** The tool's own
`trend_direction` **MIXED** is the right label. The spec's heuristic *"cumulative premium
flow + and persistent ≥ 60d → stealth institutional build → high-confidence directional"*
**does not fire**: the flow is positive but explicitly not persistent.

**This is a genuinely useful negative.** Across 3½ months of data there is **no stealth
accumulation and no stealth distribution** in the options premium — consistent with
`phase-2-dark-pool.md` (ENPH absent from the dark-pool `ticker-summary` top-30, $39.5M vs a
$1.043B cutoff) and `phase-0.5-context.md` (total premium at the **26.6th self percentile**).
ENPH is not a name institutions are quietly building a position in, in either direction.
The one exception is the **$2,837,716 Jan-2028 P30 purchase** of `phase-3-positioning.md` —
a single decisive act, not a campaign.

### C — GEX time series (the regime-stability read)

`uw historical gex-time-series --symbol ENPH --days 30 --dte-max 45` → `days_analyzed` 30,
`trajectory` 30 rows, `regime_flip_dates` **1 entry**.

`regime_flip_dates`: `2026-06-22`, `from_regime` POSITIVE → `to_regime` NEGATIVE,
`spot` 53.4, `zero_gamma_level` 74.39, `zgl_delta` 54.39.
`note`: *"Regime flips identify dates where spot crossed the zero-gamma level. Empirically
precedes realised-vol expansion."*

**`total_gex` trajectory — the reliable series** (the `regime` label is broken, see §I):

| Date | `total_gex` | Spot | | Date | `total_gex` | Spot |
|---|---|---|---|---|---|---|
| 2026-06-16 | **+10,562,024** | 51.16 | | 2026-07-13 | −2,182,459 | 42.93 |
| 2026-06-17 | **+9,070,044** | 49.05 | | 2026-07-14 | −876,085 | 44.84 |
| 2026-06-18 | **+14,229,287** | 51.87 | | 2026-07-15 | −1,216,059 | 43.72 |
| 2026-06-22 | **+707,865** | 53.40 | | 2026-07-16 | **−4,361,654** | 41.29 |
| **2026-06-23** | **−1,808,037** | 47.94 | | 2026-07-17 | −2,613,148 | 41.63 |
| 2026-06-24 | −2,138,690 | 47.89 | | 2026-07-20 | −763,473 | 39.73 |
| 2026-06-25 | −2,509,060 | 47.20 | | 2026-07-21 | −483,746 | 40.11 |
| 2026-06-26 | −3,680,894 | 47.32 | | 2026-07-22 | −816,948 | 40.07 |
| 2026-06-29 | −1,882,786 | 47.83 | | 2026-07-23 | −1,622,069 | 38.48 |
| 2026-06-30 | −848,813 | 49.36 | | 2026-07-24 | −2,199,041 | 37.05 |
| 2026-07-01 | −82,676 | 47.31 | | 2026-07-27 | −566,158 | 37.52 |
| **2026-07-02** | **−4,604,108** | 42.92 | | 2026-07-28 | −1,251,240 | 36.30 |
| 2026-07-06 | −1,365,605 | 44.97 | | **2026-07-29** | **−2,796,417** | **36.08** |
| 2026-07-07 | −2,647,029 | 42.77 | | | | |
| 2026-07-08 | −2,637,888 | 42.34 | | | | |
| 2026-07-09 | −1,863,384 | 45.06 | | | | |
| 2026-07-10 | −687,297 | 45.14 | | | | |

**Four findings:**

1. **`total_gex` has been negative for 26 consecutive sessions — every session from
   2026-06-23 to 2026-07-29 without exception.** The `regime_flip_dates` field reports only
   one flip (06-22), which understates the story; the *sign of `total_gex`* tells it
   properly. **The short-gamma state phase 4 measured today is five weeks old and
   uninterrupted.**
2. **Spot fell 47.94 → 36.08 (−24.7%) inside that negative-gamma regime.** This is exactly
   the amplification mechanic phase 4 described, observed over five weeks rather than
   asserted. The tool's own note — *"empirically precedes realised-vol expansion"* — is
   borne out: the flip on 06-22/06-23 preceded a 25% decline.
3. **Per the spec's heuristic, there is NO regime flip in the last 5 days** (last genuine
   sign change: 06-23). So this is **not** a dealer-hedging transition with expanding
   ranges ahead — it is an **established, stable** short-gamma regime. That *raises*
   confidence in phase 4's structural read while *lowering* the case for a near-term
   volatility-expansion trade on regime-change grounds.
4. **Today's −2,796,417 is the 4th most negative of 30 sessions**, behind 07-02
   (−4,604,108), 07-16 (−4,361,654) and 06-26 (−3,680,894). Firmly negative, **not
   extreme**. Both prior deeper readings were followed by further declines (07-02 at 42.92
   → 41.29 by 07-16; 07-16 at 41.29 → 39.73 by 07-20).

`zero_gamma_level` is **null in all 19 FULLY_NEGATIVE rows** and, where populated, jumps
implausibly (20.99 → 42.99 → 20.00 → 74.39 → 25.12 → 20.03 → 18.01 → 22.87 → 20.04 →
17.83). **The ZGL series is unusable** — independently confirming phase 4's decision to
source the flip level from `atm_flip_strike` (36) rather than `zero_gamma_level` (null).

### D — P/C ratio z-score

`uw historical pc-ratio-zscore --symbol ENPH --lookback-days 20`:

| Field | Value |
|---|---|
| `current_pc_ratio` | 0.726 |
| `mean_pc_ratio` | 0.5607 |
| `std_pc_ratio` | 0.3429 |
| **`zscore`** | **+0.482** |
| **`extreme`** | **NORMAL** |

**No sentiment extreme.** |z| = 0.48 against the spec's |z| > 2 contrarian threshold — not
remotely close. There is **no contrarian setup** available from put/call positioning.

> **Tension with phase 0.5, stated rather than hidden.** `phase-0.5-context.md` recorded
> the same 0.726 ratio as ENPH's **87.5th self percentile** and flagged it as "the *one*
> metric elevated vs self." Here the same value scores a merely NORMAL z-score. Both are
> correct and the difference is methodological: (a) different windows — **20 sessions here
> vs 65 there**; and (b) the distribution is **strongly right-skewed** with
> `std_pc_ratio` 0.3429 against a `mean_pc_ratio` of 0.5607 (a coefficient of variation of
> **0.61**), so a value can sit high in rank while remaining well inside one standard
> deviation. **The honest synthesis: today's P/C is high-ish by rank and unremarkable by
> dispersion. It is not evidence of a positioning extreme in either direction, and phase 9
> should not lean on it.** The 30-session series in §G shows why — P/C has ranged from
> 0.130 (07-10) to 1.537 (07-16) in six weeks.

### E — Multi-day trend table

`uw historical trend --symbol ENPH --days 30` → `days_analyzed` **30**,
`date_range` **2026-06-16 to 2026-07-29**, `daily_data` 30 rows.

| Field | Value |
|---|---|
| **`price_change`** | **50.26 → 35.07 (−30.2%)** |
| **`bearish_days` / `bullish_days`** | **21 / 9** |
| `iv_rank_change` | 48.0006 → 47.0523 (**≈flat**) |
| `flow_direction_latest` | **bearish** |
| **Σ `net_flow` (derived)** | **+$2,051,489** |

| Date | Close | `net_flow` | `iv_rank` | P/C | Total OI | Dir |
|---|---|---|---|---|---|---|
| 2026-06-16 | 50.26 | −259,957 | 48.0 | 0.589 | 510,764 | bearish |
| 2026-06-17 | 47.78 | **+3,170,190** | 51.8 | 0.675 | 513,433 | bullish |
| 2026-06-18 | 52.28 | +1,303,555 | 61.4 | 0.469 | 510,189 | bullish |
| 2026-06-22 | 52.41 | +70,346 | 63.2 | 0.249 | **386,879** ← June OPEX | bullish |
| 2026-06-23 | 47.22 | +975,254 | 57.0 | 0.649 | 395,656 | bullish |
| 2026-06-24 | 47.82 | −412,731 | 70.0 | 0.300 | 402,370 | bearish |
| 2026-06-25 | 47.21 | +431,902 | 68.9 | 0.316 | 410,605 | bullish |
| 2026-06-26 | 47.58 | −451,773 | 63.5 | 0.813 | 413,260 | bearish |
| 2026-06-29 | 48.34 | −170,914 | 66.5 | 0.403 | 393,138 | bearish |
| 2026-06-30 | 49.24 | **−4,256,550** | 80.4 | 0.136 | 398,671 | bearish |
| 2026-07-01 | 46.84 | −1,522,701 | 77.9 | 0.271 | 435,980 | bearish |
| 2026-07-02 | 43.07 | −1,446,961 | 77.4 | 0.430 | 443,254 | bearish |
| 2026-07-06 | 44.55 | −99,302 | **83.2** ← IV peak | 0.189 | 407,550 | bearish |
| 2026-07-07 | 42.99 | +619,697 | 76.9 | 0.274 | 415,378 | bullish |
| 2026-07-08 | 43.02 | −336,379 | 76.5 | 0.594 | 419,316 | bearish |
| 2026-07-09 | 44.89 | −80,196 | 77.1 | 0.458 | 421,708 | bearish |
| 2026-07-10 | 44.84 | −85,271 | 77.4 | **0.130** | 421,949 | bearish |
| 2026-07-13 | 43.06 | −149,913 | 76.6 | 0.528 | 405,342 | bearish |
| 2026-07-14 | 44.985 | −1,014,887 | 76.6 | 1.174 | 410,406 | bearish |
| 2026-07-15 | 44.05 | −107,954 | 80.1 | 0.618 | 414,273 | bearish |
| 2026-07-16 | 41.08 | **+5,629,548** | 76.5 | **1.537** | 414,791 | bullish |
| 2026-07-17 | 41.57 | −727,023 | 80.9 | 0.493 | 411,642 | bearish |
| 2026-07-20 | 39.46 | −518,325 | 82.1 | 0.633 | **348,684** ← July OPEX | bearish |
| 2026-07-21 | 39.94 | +50,235 | 79.5 | 0.546 | 356,978 | bullish |
| 2026-07-22 | 39.58 | −215,563 | 75.0 | 0.405 | 359,659 | bearish |
| 2026-07-23 | 38.89 | **+5,904,530** | 65.2 | 0.947 | 361,654 | bullish |
| 2026-07-24 | 36.70 | −346,714 | 66.8 | 0.622 | 362,593 | bearish |
| 2026-07-27 | 38.01 | −258,731 | 69.8 | 0.547 | 355,935 | bearish |
| 2026-07-28 | 36.32 | **−3,162,110** | 63.3 | 0.680 | 363,227 | bearish |
| **2026-07-29** | **35.07** | **−479,813** | **47.1** | 0.726 | 381,215 | bearish |

> **Gap note:** this window (2026-06-16 → 2026-07-29) is **entirely inside the contiguous
> post-04-27 cluster** — `days_analyzed` 30 = 30 real sessions, **no gap crossing**. This
> is the one trailing read in the phase that needs no gap caveat.

**Five observations:**

1. **The decline is a grind, not a shock.** 30 sessions, −30.2%, with 21 bearish flow days.
   Only two sessions closed higher than they opened the window at. This context is essential
   for phase 9: ENPH is in an established downtrend, so a short is trend-following (higher
   base rate) and a long is counter-trend (requires a catalyst, and there is none until
   **2026-10-27**).
2. **The three bullish spikes are the phase's headline pattern** (Summary table). 06-17
   +$3.17M → −9.9% over 11 sessions; 07-16 +$5.63M → −3.9% over 2 sessions; 07-23 +$5.90M →
   **−9.8% over 4 sessions**. All three failed. Phase 1 identified the 07-23 mechanism as
   **put selling**; the 07-16 print carries the window's highest P/C (**1.537**), also
   consistent with put activity rather than call buying. **In ENPH, "bullish premium" has
   meant premium *collection*, and it has been a reliable contrarian sell signal 3 times
   out of 3.** N=3 is small — but it is 3/3 with an average subsequent decline of ~7.9%,
   and it is directly corroborated by the ask/bid mechanism in phase 1.
3. **The largest bearish print of the window is 06-30 (−$4,256,550) at a close of 49.24** —
   followed by 43.07 within 3 sessions (**−12.5%**). The second largest is **07-28
   (−$3,162,110)**, which `phase-3-positioning.md` proved was the **$2.84M Jan-2028 P30
   purchase**. Large bearish prints in ENPH have led price; large bullish prints have not.
4. **`iv_rank` round-tripped: 48.0 → 83.2 (07-06 peak) → 47.1.** Net change ≈ zero across a
   30% price collapse. Implied vol rose into the decline and then gave it all back through
   the event. **There is no residual event premium left to sell** — the crush is done, which
   caps the vanna fuel phase 4 flagged (§C there).
5. **Total OI fell 510,764 → 381,215 (−25.4%)**, with visible cliffs at June OPEX
   (510,189 → 386,879 on 06-22, **−123,310**) and July OPEX (411,642 → 348,684 on 07-20,
   **−62,958**). Neither was rebuilt. Combined with `phase-3-positioning.md`'s **zero
   `position-rolls`**, this is **de-risking and abandonment**, not repositioning.

### F — OI trend

`uw historical oi-trend --symbol ENPH --days 30 --top-n 10`:

| Field | Value |
|---|---|
| **`overall_trend`** | **BUILDING** |
| **`consecutive_build_days`** | **8** |
| **`total_net_oi_change`** | **+201,329** |
| `days_analyzed` | 30 |

| Date | `net_oi_change` | Contracts ↑ | Contracts ↓ |
|---|---|---|---|
| 2026-07-10 | +288 | 210 | 130 |
| 2026-07-13 | +4,647 | 172 | 84 |
| 2026-07-14 | +5,091 | 252 | 82 |
| 2026-07-15 | +3,868 | 229 | 75 |
| 2026-07-16 | +575 | 200 | 94 |
| 2026-07-17 | −2,771 | 212 | 125 |
| **2026-07-20** | **+12,748** | 238 | 69 |
| 2026-07-21 | +8,315 | 315 | 83 |
| 2026-07-22 | +2,687 | 227 | 68 |
| 2026-07-23 | +2,114 | 191 | 79 |
| 2026-07-24 | +1,153 | 268 | 119 |
| 2026-07-27 | +6,341 | 279 | 65 |
| 2026-07-28 | +7,348 | 300 | 90 |
| **2026-07-29** | **+18,048** | **368** | 76 |

**The 8-day build run is 07-20 → 07-29** (07-17 was the last negative day at −2,771),
summing to **+58,754** contracts. **Today's +18,048 is the largest single-session build in
the visible series**, on **368 contracts increasing** vs 76 decreasing.

> **The reconciliation trap — flagged so phase 10 does not read it as a contradiction.**
> `oi-trend` says OI is **BUILDING (+201,329)** while `trend` (§E) shows
> `total_open_interest` **falling 510,764 → 381,215 (−129,549)**. Both are right.
> `net_oi_change` sums per-contract increases minus decreases **among contracts present in
> the OI-changes file**; contracts that **expire** leave the chain entirely and are not
> booked as "decreases." The June and July OPEX retired roughly **330,000 contracts**
> (§E cliffs), which swamps the +201,329 of new positions. **Correct statement: ENPH is
> building new positions steadily into a chain that is shrinking faster through
> expiration.** Neither figure alone describes the book.

**Today's top OI builds** (identical to `phase-3-positioning.md` §C, cross-validating both
leaves): `ENPH280121P00030000` +2,000 (`dte` 541, vol 3,162) · `ENPH260918C00070000` +1,604
(`dte` 51) · `ENPH260918P00035000` +885 (`dte` 51) · `ENPH260731C00045000` +808 (`dte` 2).

Note today's `net_oi_change` **+18,048** vs the **+17,988** derived from the screener
parquet in `phase-0.5-context.md` — a **60-contract (0.33%) discrepancy** between the
OI-changes dataset and the screener dataset. Immaterial; recorded for completeness.

**Per the spec's heuristic, this is a sustained buildup rather than a spike** (8 consecutive
days, accelerating). But `phase-3-positioning.md` established the *composition*: premium-
weighted, the builds are **5.4 : 1 bearish** ($2,910,482 vs $535,495). **A sustained OI
build whose premium is 5.4:1 bearish is a sustained bearish buildup** — the trend metric and
the composition agree.

### G — Price context (`fz`, advisory cross-check)

`fz quote` is **degraded to 14 of 84 fields** with all technical fields `null`
(`phase-0-intake.md`), so the spec's `§1` recipe could not be used. **Workaround:**
`fz screen --tickers ENPH --view technical --agent`, the same substitution validated in
phase 0.

| Field | Value | Reading |
|---|---|---|
| `Price` | **35.07** | ✔ matches the verified close |
| **`Gap`** | **+7.08%** | **gapped up on the print** |
| **`Change from Open`** | **−9.82%** | **gave it all back and more** |
| `Change` | −3.44% | ✔ matches |
| **`RSI`** | **31.60** | approaching oversold, **not** below 30 |
| `SMA20` | **−15.38%** | price far below the 20-day |
| `SMA50` | **−30.49%** | price far below the 50-day |
| `SMA200` | **−12.34%** | price below the 200-day |
| `52W High` | **−52.44%** | ✔ matches phase 0.5's −52.4% |
| `52W Low` | **+36.06%** | ✔ matches phase 0.5's +36.1% |
| **`ATR`** | **3.24** | **9.2% of spot** |
| `Beta` | **1.65** | high-beta into a risk-off tape |
| `Volume` | 9,508,592 | |

**This is the phase's most valuable advisory input, for four reasons:**

1. **It independently confirms the gap-and-crap from a non-UW source.** Finviz measures
   `Gap` **+7.08%** (prev close → open) and `Change from Open` **−9.82%** (open → close).
   `phase-1-flow.md` measured, from UW/DuckDB OHLC, `high` 39.60 (+9.03% vs prev close) and
   close −11.44% from high. **Two entirely separate data providers describe the same
   violent reversal.** This retires any doubt about the finding that
   `phase-0.5-context.md`'s "whimper" framing missed.
2. **`ATR` 3.24 = 9.2% of spot is the single most important number for phase 9's stop.**
   A stop tighter than ~1 ATR ($3.24) will be noise-stopped in a name whose *average* day
   spans 9%. Note phase 4's `implied_move_perc` of **5.58%** for the front expiry is
   *below* the realized ATR — another sign the surface may be under-pricing forward
   movement (§A).
3. **Full bearish moving-average alignment**: price below SMA20, SMA50 and SMA200
   simultaneously. Implied levels: SMA50 ≈ 35.07 / 0.6951 = **50.45**; SMA200 ≈
   35.07 / 0.8766 = **40.01**. So **SMA50 (50.45) is still above SMA200 (40.01)** — the
   death cross has **not** yet occurred, but SMA50 is falling steeply toward it. Phase 9
   should treat **~40.01 (SMA200)** as a technically meaningful overhead level, which sits
   close to phase 3's `put_heavy` 40 strike (10,079 near-term OI) — **two independent
   methods placing resistance at 40**.
4. **`RSI` 31.60 tempers the bearish case honestly.** Approaching oversold without being
   there. Per the spec's intent for this cross-check, an oversold RSI argues against
   *chasing* a fresh short at 35.07 — but 31.60 is **not** an oversold *signal*, and in a
   sustained short-gamma downtrend RSI can sit in the 20s–30s for weeks. It is a caution
   about entry timing, not about direction.

### H — Signal backtest

`uw historical signal-backtest --signal-type bearish_flow --lookback-days 5 --top-n 20`.
Signal class chosen to match `phase-1-flow.md`'s verdict (**bearish**), which
`phase-2-dark-pool.md` (distribution), `phase-3-positioning.md` (puts bought) and
`phase-4-structure.md` (short gamma) all corroborate.

| Field | Value |
|---|---|
| `signal_type` | **bearish_flow** |
| **`win_rate`** | **"100.0%"** (returned as a **string**) |
| **`total_signals`** | **9** |
| `truncated_signals` | 9 |
| **`avg_move_pct`** | **−14.59** |
| `lookback_days` | 5 (trading days) |
| `methodology_notes` | *"win_rate = fraction of signals where forward move agrees with the signal's direction. Lookback is in TRADING days; selection is positional within the yfinance bar series. **In-sample backtest — not a robust live edge.**"* |

`results` rows (the tickers that generated the 9 signals):

| Ticker | Signal date |
|---|---|
| TSLA, WOLF, AMD, GLD | 2026-07-27 |
| MU, TSLA, SNDK, SOXL, **BE** | 2026-07-24 |

**Four reasons this 100% figure must be discounted hard, and I am stating them before the
number is used:**

1. **The tool disclaims itself.** `methodology_notes` says *"In-sample backtest — not a
   robust live edge."* That is the vendor's own assessment, not my scepticism.
2. **N = 9 is below the spec's confidence floor** (*"treat <10 historical firings as
   low-confidence"*). A 100% rate on 9 observations has a 95% lower confidence bound around
   **~66%** even taken at face value.
3. **The sample is market-wide and ENPH is not in it.** Per the spec, this leaf takes no
   `--symbol`, so `p` is *"the base rate of that signal class across the tape."* The nine
   signals are TSLA/WOLF/AMD/GLD/MU/SNDK/SOXL/BE — **eight distinct names, none of them
   ENPH**, and heavily semiconductor-weighted, matching the semis-dominated tape
   `phase-0.5-context.md` found. **This is not evidence about ENPH.**
4. **All nine signals come from just two dates (07-24 and 07-27).** A 5-trading-day forward
   window from those dates lands squarely in the same broad-market drawdown, so the nine
   observations are **not independent** — they are ~2 market events sampled 9 times. The
   `avg_move_pct` of **−14.59%** over 5 days across large caps is itself implausibly large
   for a repeatable edge and points to a regime-specific artifact.

**One genuinely useful signal inside it:** **BE** appears in the bearish_flow list for
07-24 — the fourth independent lane in which BE surfaces as the clean-energy name carrying
real institutional bearish conviction (`phase-0.5-context.md`: #9 most bearish universe-wide
at −$28.2M; `phase-2-dark-pool.md`: #26 in dark-pool premium; `phase-1-flow.md`: largest
option volume in the complex). The sector read is consistent even though the ENPH-specific
inference is not.

**Reported as required, with the cap instruction.** Per the spec I quote the raw win-rate
in the handoff block and let phase 9 apply the N-conditional cap from
`rubrics/sizing-rubric.md`. **My explicit recommendation to phase 9: treat `p` = 1.00 as
unusable and cap it aggressively** — the four objections above are cumulative, not
alternatives. For reference, the 2026-07-27 run recorded `p_raw` **0.556** on the same
`win_rate_n` of 9; a jump from 0.556 to 1.000 in two sessions on an unchanged sample size is
itself evidence of instability in this metric rather than of a real edge shift.

### I — Data-quality findings across the historical leaves

Three issues that materially affect how the above is read:

1. **The `regime` label in `gex-time-series` is broken across the whole series.** Seven rows
   report `regime` POSITIVE while carrying a **negative** `total_gex`: 06-24 (−2,138,690),
   06-25 (−2,509,060), 06-26 (−3,680,894), 07-01 (−82,676), 07-02 (−4,604,108), 07-15
   (−1,216,059), 07-28 (−1,251,240). Label counts are FULLY_NEGATIVE 19 / NEGATIVE 1 /
   POSITIVE 10, but **only 4 of 30 sessions actually have positive `total_gex`** (06-16,
   06-17, 06-18, 06-22). **This independently confirms `phase-4-structure.md`'s finding that
   the GEX `regime` field is unreliable** — there it was "FULLY_NEGATIVE" on a surface with
   25 positive strikes; here the label disagrees with its own row-level `total_gex`. §C uses
   the **sign of `total_gex`**, which is internally consistent.
2. **`zero_gamma_level` is unusable** — `null` in all 19 FULLY_NEGATIVE rows and wildly
   discontinuous where present (74.39 → 25.12 in one session). Confirms phase 4's use of
   `atm_flip_strike`.
3. **Window/N disclosures** (per the mandatory gap-aware rule — the tool's own session count
   is quoted, never the calendar span):

| Leaf | Requested | **Actual N** | Crosses the gap? |
|---|---|---|---|
| `iv-percentile-zscore` | 252 days | **`dates_used` 75** | **YES** |
| `cumulative-premium-flow` | 90 days | **`dates_covered` 76** | **YES** (11 dates ≤ 2026-03-27) |
| `trend` | 30 days | **`days_analyzed` 30** | **No** (06-16 → 07-29, contiguous) |
| `oi-trend` | 30 days | **`daily_data` 30** | **No** |
| `gex-time-series` | 30 days | **`trajectory` 30** | **No** |
| `pc-ratio-zscore` | 20 days | 20 (implied) | **No** |

**The `iv_percentile` of 28 is therefore a percentile over 75 sessions (~4.5 calendar
months, gap-straddling), not 252.** It is a *recent-history* percentile, not a one-year one,
and the spec's pitfall applies: a 28th percentile in a window whose own vol was elevated
throughout is not the same as cheap by long-term standards. Same caveat on `iv_zscore`
−0.658.

**Latest-anchor caveat.** All eight leaves in this phase take **no `--date`** and anchor to
the **latest available date = 2026-07-29**, which is also this run's as-of date
(`phase-0-intake.md`), so every figure is as-of-correct **for this run only**. A re-run after
a new session lands will shift every trailing read — IV percentile, z-scores, build-day
counts and win rates all move. Engine behaviour, not a data error.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows / N used |
|---|---|---|
| `uw historical iv-percentile-zscore --symbol ENPH --lookback-days 252 --json` | `iv_percentile`=**28**, `iv_zscore`=−0.658, `current_iv30d`=0.797, `regime`=NORMAL, **`dates_used`=75** | 75 sessions |
| `uw historical vrp --symbol ENPH --realised-window-days 30 --json` | `vrp`=**+0.1267**, `iv30d`=0.797, `realised_vol`=0.6703, `regime`=**PREMIUM_SELLING** | 1 |
| `uw historical cumulative-premium-flow --symbol ENPH --days 90 --json` | `net_flow`=**+25008497**, `cumulative_bullish`=441590914, `cumulative_bearish`=416582417, `trend_direction`=**MIXED**; **`dates_covered`\|length=76**, 11 dates < 2026-04-27 ← `[.dates_covered[]\|select(.<"2026-04-27")]\|length` | 76 sessions |
| `uw historical pc-ratio-zscore --symbol ENPH --lookback-days 20 --json` | `zscore`=**+0.482**, `extreme`=**NORMAL**, `current_pc_ratio`=0.726, `mean_pc_ratio`=0.5607, `std_pc_ratio`=0.3429 | 20 sessions |
| `uw historical gex-time-series --symbol ENPH --days 30 --dte-max 45 --json` | `regime_flip_dates`=1 (2026-06-22 POSITIVE→NEGATIVE, `spot`=53.4); `total_gex` negative from 06-23 (−1808037) through 07-29 (−2796417) = **26 consecutive** ← `.trajectory[]`; only 4 of 30 rows have `total_gex`>0 | 30 sessions |
| `uw historical oi-trend --symbol ENPH --days 30 --top-n 10 --json` | `overall_trend`=**BUILDING**, `consecutive_build_days`=**8**, `total_net_oi_change`=**+201329**; today `net_oi_change`=**+18048** (368↑/76↓) ← `.daily_data[]` | 30 sessions |
| `uw historical trend --symbol ENPH --days 30 --json` | `price_change`="50.26 -> 35.07", `bearish_days`=**21**, `bullish_days`=**9**, `iv_rank_change`="48.0006 -> 47.0523", `days_analyzed`=30, `date_range`="2026-06-16 to 2026-07-29"; Σ`net_flow`=**+2051489** ← `[.daily_data[].net_flow]\|add`; spikes 06-17 +3170190 / 07-16 +5629548 / 07-23 +5904530 | 30 sessions |
| `uw historical signal-backtest --signal-type bearish_flow --lookback-days 5 --top-n 20 --json` | `win_rate`=**"100.0%"** (string), `total_signals`=**9**, `avg_move_pct`=**−14.59**, `methodology_notes` "In-sample backtest — not a robust live edge"; `results[].ticker` = TSLA/WOLF/AMD/GLD/MU/TSLA/SNDK/SOXL/**BE** — **no ENPH** | 9 signals, 2 dates |
| `fz screen --tickers ENPH --view technical --agent` | `Gap`=**+7.08%**, `Change from Open`=**−9.82%**, `RSI`=**31.60**, `ATR`=**3.24**, `SMA20`=−15.38%, `SMA50`=−30.49%, `SMA200`=−12.34%, `52W High`=−52.44%, `Beta`=1.65 ← `.[0]` | 1 |

All eight `uw` reads and the one `fz` read were captured to a file before being queried and
every value round-tripped through `jq` on validated JSON. Derived values, each stated
inline: Σ`net_flow` over 30 sessions (§E), the 26-session negative-`total_gex` run and the
positive-row count (§C), the 8-day build sum +58,754 (§F), `ATR` as % of spot, implied
SMA50/SMA200 levels (§G), and the gap-crossing date counts (§I). `win_rate` is a **string**
in the payload — converted to 1.00 for the handoff block, with the raw string preserved.

## Tool errors

No invocation failures — all eight `uw historical` calls returned exit 0 with parseable
JSON, and the `fz` workaround returned exit 0. **Four data-integrity findings**, all silent
(exit 0):

1. **`gex-time-series` `regime` label contradicts its own row-level `total_gex`** in 7 of 30
   rows (POSITIVE label on negative `total_gex`; §I). Label counts say 10 POSITIVE rows;
   only **4** rows actually have `total_gex` > 0. **Second independent confirmation** of the
   broken GEX `regime` field first found in `phase-4-structure.md`. §C uses the `total_gex`
   sign instead. Candidate phase-spec / `lib/uw-json-paths.md` note (**propose-only**).
2. **`gex-time-series` `zero_gamma_level` is unusable** — `null` in all 19 FULLY_NEGATIVE
   rows, and discontinuous where present (20.99 → 42.99 → 20.00 → 74.39 → 25.12 → 17.83).
3. **`iv-percentile-zscore` silently returns a 75-session window for a 252-day request**
   (`dates_used` 75) and that window **straddles the 2026-03-28 → 2026-04-24 hole**. The
   leaf does **not** interpolate — it simply uses the sessions present — but a caller quoting
   "1-year IV percentile" would be wrong by a factor of ~3.4 in window length. Same class of
   issue on `cumulative-premium-flow` (90 days requested → 76 sessions, 11 pre-gap).
   Disclosed in §A, §B, §I per the mandatory gap-aware rule.
4. **`signal-backtest` returns `win_rate` as a formatted string** (`"100.0%"`), not a
   number — a type trap for any downstream arithmetic. Also note the leaf is **market-wide**
   and its `results` rows contain **no ENPH**, despite being run in a single-ticker phase;
   this is documented engine behaviour, not a bug, but it means the value is a tape-wide base
   rate (§H).

Minor: `oi-trend` `net_oi_change` +18,048 vs the screener-derived +17,988 in
`phase-0.5-context.md` — a 60-contract (0.33%) inter-dataset discrepancy. Immaterial.

## DATA NOTE / CORRECTION

No value in this phase was revised after its first validated read.

**One upstream framing is reinforced with independent cross-source evidence**, and **one
apparent contradiction between two leaves in this phase is resolved rather than left
standing:**

**(1) The gap-and-crap is now confirmed by a second, non-UW data provider.**
`phase-1-flow.md`'s DATA NOTE corrected `phase-0.5-context.md`'s "whimper" framing using UW
OHLC (`high` 39.60, `close` 35.07, −11.44% from high). This phase corroborates it from
**Finviz**: `Gap` **+7.08%**, `Change from Open` **−9.82%**
(`fz screen --tickers ENPH --view technical --agent` → `.[0]`). Two independent providers,
same event. The correction stands and is now double-sourced.

**(2) "OI BUILDING" vs "OI down 25%" is not a contradiction.** `oi-trend`
`overall_trend`=BUILDING with `total_net_oi_change` **+201,329**, against `trend`'s
`total_open_interest` falling **510,764 → 381,215 (−129,549)**. Verified against
`.daily_data[].net_oi_change` (oi-trend) and `.daily_data[].total_open_interest` (trend).
`net_oi_change` counts increases minus decreases **among contracts still in the chain**;
expirations remove contracts without booking a decrease, and the June/July OPEX retired
~330k contracts (§E cliffs at 06-22 and 07-20). **Correct statement: new positions are being
built steadily into a chain shrinking faster through expiration.** Recorded here so phase 10
does not flag it as an internal contradiction.

## Verdict for downstream phases

- **Volatility regime: CHEAP by percentile, FAIR-to-RICH by realized — net FAIR, and the
  actionable edge is in the skew, not the level.** `iv_percentile` **28** /
  `iv_zscore` **−0.658** / `regime` NORMAL (on **75** sessions, not 252) says cheap;
  `vrp` **+0.1267** / `regime` PREMIUM_SELLING says rich vs trailing realized. Neither of
  the spec's two heuristics fires cleanly. **The decisive fact is phase 4's `skew_ratio`
  0.994** — 25Δ puts cheaper than 25Δ calls — so downside optionality is the one thing
  that is unambiguously cheap here.
- **Premium environment: mildly PREMIUM-SELLING on trailing data, but with a live risk of
  inverting.** `realised_vol` 0.6703 is a 30-day trailing figure dominated by pre-event
  calm, while `ATR` **3.24 (9.2% of spot)** and today's 12.8% realized range point far
  higher. **The front-expiry `implied_move_perc` of 5.58% is below the realized ATR** — if
  post-event realized persists, the +0.1267 VRP disappears. **Do not size a premium-selling
  structure on the assumption that VRP holds.**
- **Conviction that today's signal is HISTORICALLY EDGE-POSITIVE: 4 / 5.** The edge case
  rests on **ENPH-specific, multi-week evidence**, not the backtest: `total_gex` negative
  **26 consecutive sessions** while spot fell **−24.7%** (the amplification mechanic observed,
  not asserted); **21 of 30 bearish flow days** through a **−30.2%** decline; large *bearish*
  prints leading price (06-30 −$4.26M → −12.5% in 3 sessions; 07-28 −$3.16M = the Jan-2028
  P30 purchase); and large *bullish* prints failing **3 for 3** at an average subsequent
  −7.9%. Held at 4, not 5, because (a) the headline `win_rate` of **100%** is
  **unusable** — self-disclaimed as in-sample, N=9 below the confidence floor, market-wide
  with **ENPH absent from the sample**, and drawn from only 2 dates; (b) `trend_direction`
  is **MIXED** over 76 sessions with net premium flow essentially flat (+2.9% skew), so
  there is **no** stealth-build confirmation; (c) `pc-ratio-zscore` is **NORMAL** (+0.482) —
  no positioning extreme to exploit; (d) `RSI` **31.60** and price **−30.49% below SMA50**
  mean a fresh short is being initiated into an extended, near-oversold tape; and (e) the
  contrarian-spike pattern is only N=3.
- **Three specific data points:**
  1. **IV percentile 28** (`iv_zscore` −0.658, `regime` NORMAL) — on **75** sessions
     spanning the data gap, **not** 252. `iv_rank` 47.05 = ENPH's **15.6th self percentile**.
  2. **VRP +0.1267** (`iv30d` 0.797 vs `realised_vol` 0.6703, `regime` PREMIUM_SELLING) —
     with the inversion risk above.
  3. **Signal win rate 100.0% on `total_signals` 9, `avg_move_pct` −14.59%** — reported
     verbatim and **recommended for aggressive capping** (see §H and the handoff note).
- **Sizing handoff block (phase-9 reads these verbatim):**
  ```
  signal_class:               bearish_flow
  signal_backtest_win_rate:   1.00
  win_rate_n:                 9
  win_rate_source:            backtest
  ```
  **Mandatory qualifiers on this block, per §H — phase 9 must apply all four:**
  (1) the tool self-describes as *"In-sample backtest — not a robust live edge"*;
  (2) **N = 9 is below the spec's 10-firing low-confidence floor**, so the
  N-conditional cap in `rubrics/sizing-rubric.md` binds hard;
  (3) the leaf is **market-wide** — `p` is the tape-wide base rate for `bearish_flow`, and
  **ENPH does not appear in the 9-signal sample** (TSLA, WOLF, AMD, GLD, MU, SNDK, SOXL, BE);
  (4) all 9 signals originate on **just two dates (07-24, 07-27)**, so they are ~2
  correlated market events, not 9 independent observations. For calibration, the 07-27 run
  recorded `p_raw` **0.556** on the same `win_rate_n` of 9 — a 0.556 → 1.000 swing in two
  sessions at unchanged N is evidence of metric instability, not of a real edge change.
  **A `p` anywhere near 1.00 would produce an indefensible Kelly fraction; treat the
  conviction-bin fallback as the more honest input and say so in `decision.json`.**
- **Open questions:**
  - **Does the 3-for-3 "bullish premium spike = contrarian sell" pattern survive a longer
    lookback?** N=3 with a clear mechanism (put selling, phase 1) is suggestive, not
    established. If it holds, it is the most tradeable ENPH-specific regularity found in
    this run. (→ 9, and a candidate for `/deep-dive-calibration`)
  - **Will realized vol converge up to IV and kill the +0.1267 VRP?** `ATR` 3.24 (9.2%) and
    a 12.8% event-day range against a 5.58% front implied move say the surface may be
    under-pricing forward movement. (→ 4 cross-read, 9)
  - **How much does the 75-session (gap-straddling) window inflate or deflate
    `iv_percentile` 28 versus a true 252-day figure?** ENPH traded near 73.74 within the
    year, so a genuine one-year window would likely include far higher vol — plausibly
    pushing the percentile **lower**, i.e. vol even cheaper than 28. Unresolvable from local
    data. (→ 10)
  - **Is `RSI` 31.60 with price 30.49% below SMA50 an oversold bounce setup or trend
    continuation?** In a 26-session short-gamma regime, RSI can stay depressed for weeks —
    but it is the strongest timing caution against a fresh short at 35.07. (→ 8, 8b, 9)
  - **Why does BE keep appearing** — #9 most bearish universe-wide, #26 in dark-pool
    premium, largest option volume in the complex, and now in the `bearish_flow` signal
    sample — **while ENPH clears no aggression screen?** Is ENPH already too de-rated to
    attract fresh institutional shorting? (→ 6, 7b, 7c)
