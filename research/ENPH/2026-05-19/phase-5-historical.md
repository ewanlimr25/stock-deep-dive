# Phase 5 — Historical Context & VRP

**Ticker:** ENPH
**As-of date:** 2026-05-19 (effective UW date 2026-05-15)
**Generated:** 2026-05-19T00:00:00-04:00
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-4-structure.md

## Summary

The historical context is **simultaneously the strongest confirmation and the
strongest cautionary signal of the run**. Confirmations: ENPH has just
executed a **+69.8% V-shaped recovery from $31.19 close on 2026-04-29 to
$52.94 close on 2026-05-15** [HIST:trend], **bullish flow direction in
20 of 26 sessions** [HIST:trend], **net cumulative bullish premium flow
of +$15.5M over 90 days** [HIST:cumulative_premium_flow], **OI building
for 26 consecutive sessions (+210,636 net OI)** [HIST:oi_trend], and a
**fresh GEX regime flip from FULLY_NEGATIVE/NEGATIVE back to POSITIVE on
2026-05-14** [HIST:gex_time_series] — the gamma squeeze structure phase-4
described is **brand-new**. Cautions: **IV30d 95.4% is at the 100th
percentile with z-score +3.12** [HIST:iv_percentile_zscore] (premium is
extremely expensive — long-vol entries are paying full price for the
move that already happened), **VRP only +11.5 vol points** suggests
modest premium-selling edge [HIST:vrp], and most importantly the
`bullish_flow` signal backtest across all qualifying tickers over the
last 20 days produced **win rate 14.3% and avg move −2.18%**
[HIST:signal_backtest] — every megacap-tech bullish_flow signal in the
cohort (QQQ, SMH, META, AVGO, TSLA, NVDA, GOOGL) FAILED. **The signal
type that is firing on ENPH today has been a fade in this regime.** Phase-9
must downgrade conviction and prefer defined-risk structures.

## Key signals

- **IV percentile 100 (1y), z-score +3.12, regime HIGH_IV**
  [HIST:iv_percentile_zscore] — premium-rich, dates_used=25 (caveat: thin
  history due to UW gap 3/27–4/27).
- **Bullish_flow signal backtest 20d: win_rate 14.3%, avg_move −2.18%**
  [HIST:signal_backtest] — **directional bullish flow is currently NOT a
  positive-edge signal in this regime**. Major red flag for naked long-call
  sizing.
- **GEX regime flip: FULLY_NEGATIVE (4/29) → POSITIVE (5/14)**
  [HIST:gex_time_series] — fresh long-gamma stabilization; today's setup is
  one day old.
- **OI consecutive_build_days = 26, net OI Δ +210,636 across the window**
  [HIST:oi_trend] — institutional accumulation is structural, not a spike.
- **Spot trajectory: $44.07 (3/13) → $31.19 trough (4/29) → $52.94 (5/15) =
  +69.8% in 12 trading days from the low** [HIST:trend] — sharp
  V-recovery, late-stage of move.

## Detailed findings

### IV regime (percentile + z-score + VRP)

| Metric | Value | Reading |
|---|---|---|
| current_iv30d | **0.9537** (95.4%) | Very high |
| iv_percentile (1y) | **100** | Top of range |
| iv_zscore (1y) | **+3.12** | Tail-event level |
| regime | **HIGH_IV** | Premium-selling baseline |
| dates_used | 25 | **Caveat: thin history** |

The 1y percentile is computed over a 25-day window because UW data has a
multi-week gap (3/27 → 4/27). Treat "100th percentile" as "near max of
the available recent history" rather than a true 1-year reading. Even so:
**absolute IV30d ~95% with realised vol ~84% is structurally elevated**
and is itself a sign that the market is pricing significant near-term
movement (corroborates phase-4's 5/22 IV spike to 121%).

`historical_vrp`:
- iv30d: 0.9537
- realised_vol30d: 0.8387
- **VRP: +0.115** (11.5 vol points)
- regime: **PREMIUM_SELLING** — "Options pricing more vol than realised —
  favour premium selling"

**Reading:** the premium-selling regime label is correct **directionally**
but the magnitude is modest. A more reliable premium-selling regime would
show VRP > 0.15–0.20. **Strategically: defined-risk credit structures
(short verticals) are slightly favored over debit structures from a
pure-vol-edge perspective.**

### Cumulative premium flow (90d net direction)

| Field | Value |
|---|---|
| cumulative_bullish | **$105,528,729** |
| cumulative_bearish | $90,035,695 |
| **net_flow** | **+$15,493,034** |
| trend_direction | **BULLISH** |
| days_covered | 26 (2026-03-13 → 2026-05-15, w/ 3/30–4/24 gap) |

**Reading:** modestly bullish — bullish is ~17% above bearish. Persistent
but not overwhelming. The persistence (phase-1 sweep_persistence 5/5)
matters more than the raw net here.

### P/C ratio z-score (sentiment extreme y/n)

`historical_pc_ratio_zscore` (lookback_days=20):
- current_pc_ratio: **0.27** (very low → bullish)
- mean: 0.585, std: 0.309
- zscore: **−1.02** (below 1 std)
- extreme: **NORMAL** (not yet |z| > 2)

**Reading:** P/C ratio is on the bullish side but **not at a contrarian
extreme** (would need z < −2). There is room for further bullish
positioning before the contrarian-fade trigger fires.

### GEX time series (30d) + regime flip dates

Regime flips detected in the 26-session window:

| Date | From → To | Spot | ZGL | Note |
|---|---|---|---|---|
| 2026-03-17 | POSITIVE → NEGATIVE | $44.72 | $48.83 | Start of vol expansion |
| 2026-03-20 | NEGATIVE → POSITIVE | $45.00 | $43.86 | Brief reclaim |
| 2026-03-23 | POSITIVE → NEGATIVE | $42.05 | $46.08 | Re-loss |
| 2026-03-26 | NEGATIVE → POSITIVE | $40.53 | $16.29 | Distorted reading |
| 2026-03-27 | POSITIVE → NEGATIVE | $38.21 | $47.86 | Sell-off continues |
| **2026-05-14** | **NEGATIVE → POSITIVE** | **$47.33** | **$44.54** | **The clean flip; today's regime is 1 day old** |

Spot/GEX trajectory snapshots:
- 2026-03-13: $44.39, POSITIVE, GEX +$103M
- 2026-04-27: $35.15, NEGATIVE, GEX +$83M
- 2026-04-28: $34.72, NEGATIVE, GEX +$262M
- **2026-04-29: $31.19, FULLY_NEGATIVE, GEX −$107M** ← capitulation
- 2026-05-01: $33.85, FULLY_NEGATIVE
- 2026-05-04: $32.45, FULLY_NEGATIVE
- 2026-05-13: $41.15, NEGATIVE, GEX +$1.4B
- **2026-05-14: $47.33, POSITIVE, GEX +$4.99B**
- 2026-05-15: $51.37, POSITIVE, GEX +$4.42B

**Reading:**
- Stock was in **FULLY_NEGATIVE gamma three sessions** (4/29, 5/1, 5/4) =
  classic short-gamma squeeze setup, dealer hedging amplified the rally.
- Regime flipped to POSITIVE only on **2026-05-14, one trading day before
  the snapshot**. The long-gamma stabilization is brand-new.
- Phase-9 should treat the regime as **transitional → positive**, with
  awareness that re-loss of $45 could trip negative-gamma again.

### OI trend (sustained buildup vs spike vs decay)

`historical_oi_trend` (days=30):
- **consecutive_build_days: 26** (every available session was net build)
- total_net_oi_change: **+210,636 contracts**
- overall_trend: **BUILDING**

Per-day net OI change (last 13 sessions):

| Date | Net OI Δ | Top contract built |
|---|---|---|
| 2026-05-15 | +25,079 | Jun-26 50C (+4,985) |
| 2026-05-14 | +9,949 | Jun-26 60C (+3,635) |
| 2026-05-13 | +3,414 | Aug-26 50C (+694) |
| 2026-05-12 | +9,990 | Jun-26 50C (+2,266) |
| 2026-05-11 | +7,986 | Sep-26 35C/35P balanced |
| 2026-05-08 | +4,592 | Jun-26 50C (+1,264) |
| 2026-05-07 | +2,684 | 0DTE 5/8 36C (+294) |
| 2026-05-06 | +15,607 | Jun-26 45C (+2,852); short-dated 35–40 calls bought |
| 2026-05-05 | +7,693 | 5/8 30P (+827) |
| 2026-05-04 | +8,251 | Nov-26 25P (+994); Nov-26 40C (+962) |
| 2026-05-01 | +6,158 | Jul-26 30P (+1,745) |
| 2026-04-30 | +1,300 | Jan-27 45C (+753); Jan-27 55C (+556) |
| 2026-04-29 | **+30,887** | 5/15 33P (+2,610); 5/1 50C (+2,064); 5/1 40C (+2,020) |

**Reading:** the **+30,887 build on 4/29 (the FULLY_NEGATIVE day at $31.19)**
is the most-aggressive accumulation day in the window. That was when
institutions stepped in. Every session since has been net build. The
build is **structural and persistent**, not a spike.

### Multi-day trend table (date / vol / premium / IV rank / PCR)

`historical_trend` highlights (last 13 sessions):

| Date | Close | Flow | Net Flow | IV30d | IV Rank | PCR |
|---|---|---|---|---|---|---|
| 2026-05-15 | **$52.94** | bullish | +$5.55M | 0.954 | **84.97** | **0.27** |
| 2026-05-14 | $48.01 | bullish | +$3.63M | 0.836 | 61.78 | 0.25 |
| 2026-05-13 | $42.00 | bullish | +$0.73M | 0.747 | 45.11 | 0.37 |
| 2026-05-12 | $37.48 | bullish | +$0.91M | 0.740 | 43.72 | 0.48 |
| 2026-05-11 | $37.65 | bullish | +$0.96M | 0.768 | 49.02 | 0.27 |
| 2026-05-08 | $36.41 | bullish | +$0.22M | 0.712 | 39.08 | 0.33 |
| 2026-05-07 | $35.47 | bullish | +$0.54M | 0.714 | 38.93 | 0.40 |
| 2026-05-06 | $35.80 | bullish | +$0.08M | 0.676 | 31.74 | 0.73 |
| 2026-05-05 | $36.03 | bullish | +$1.33M | 0.714 | 39.10 | 0.36 |
| 2026-05-04 | $32.54 | bullish | +$0.45M | 0.708 | 37.79 | 0.68 |
| 2026-05-01 | $33.85 | bullish | +$0.06M | 0.664 | 29.45 | 0.73 |
| 2026-04-30 | $32.95 | bullish | +$1.04M | 0.679 | 30.03 | 0.62 |
| 2026-04-29 | $31.19 | **bearish** | −$0.94M | 0.728 | 41.53 | 0.42 |

- **20 of 26 sessions** total in the window had bullish flow direction.
- Net flow accelerated dramatically into Friday 5/15: $5.55M is **~7× the
  prior-day average** of the period.
- **IV rank ramped from 31 (5/6) to 85 (5/15)** — premium just got
  expensive in the last 5 sessions, partly because the catalyst is now
  in pricing range.

### Signal backtest — bullish_flow over last 20 trading days

`historical_signal_backtest` (signal=bullish_flow, lookback=20):

| Metric | Value |
|---|---|
| total_signals (cohort) | **14** |
| win_rate | **14.3%** (2/14 up after 20d) |
| avg_move_pct | **−2.18%** |

Cohort entries (all megacap tech / broad indices):

| Ticker | Signal date | Move | Direction |
|---|---|---|---|
| QQQ | 2026-05-14 | −1.93% | down |
| SMH | 2026-05-14 | −5.56% | down |
| META | 2026-05-14 | −1.17% | down |
| AVGO | 2026-05-14 | −4.34% | down |
| TSLA | 2026-05-13 | −7.92% | down |
| NVDA | 2026-05-13 | −1.55% | down |
| GOOGL | 2026-05-13 | −1.41% | down |
| META | 2026-05-13 | −0.88% | down |
| QQQ | 2026-05-13 | −1.24% | down |
| NVDA | 2026-05-12 | +0.70% | up |
| QCOM | 2026-05-12 | −3.17% | down |
| CNC | 2026-05-12 | −1.82% | down |
| AAPL | 2026-05-12 | +1.03% | up |
| UNH | 2026-05-12 | −1.33% | down |

**Reading:** **Critical caveat for phase-9.** In the current market regime,
bullish_flow signals — even when accompanied by ask-side sweeps and
positive gamma flips — have produced **−2.18% average 20-day returns at a
14.3% win rate**. The cohort is megacap tech, which is more sensitive to
the macro tape than ENPH is, but the pattern is unambiguous: **chase-flow
into fading rallies has not worked in this regime**.

ENPH-specific override considerations:
- ENPH is a small-cap that just doubled off a deep oversold base.
  Mean-reversion mathematics differ from a megacap.
- The sweep persistence (5/5) and DP accumulation are CLEANER than the
  cohort.
- The 5/22 catalyst introduces a non-trend-following driver.

But the base rate is still negative. **Phase-9 must NOT pretend this
backtest result doesn't exist.**

## Cross-check vs phases 1–4

| Phase claim | Phase-5 says |
|---|---|
| Phase-1: bullish flow + sweep persistence | **Confirmed** — but with cohort backtest red flag. |
| Phase-2: DP accumulation $48–$54 | **Confirmed** — but spot has +69.8% in 12 trading days, so accumulation has been into a strong rally, not a fresh oversold base. |
| Phase-3: bullish OI roll-up | **Confirmed** — 26-day OI build trend. |
| Phase-4: positive-gamma regime, $50 wall | **Confirmed but FRESH** — regime flipped only on 5/14. |
| Phase-4: 5/22 IV 121% catalyst | **Confirmed pricing** — IV rank ramped from 31 to 85 in 5 sessions, market is pricing the event. |

## Tool calls (audit trail)

| Tool | Args | Result summary |
|---|---|---|
| `mcp__uw-pp__historical_iv_percentile_zscore` | symbol=ENPH, lookback_days=252 | iv_pct 100, z +3.12, HIGH_IV |
| `mcp__uw-pp__historical_vrp` | symbol=ENPH, realised_window=30 | VRP +0.115, PREMIUM_SELLING |
| `mcp__uw-pp__historical_cumulative_premium_flow` | symbol=ENPH, days=90 | net +$15.5M, BULLISH |
| `mcp__uw-pp__historical_pc_ratio_zscore` | symbol=ENPH, lookback_days=20 | PCR 0.27, z −1.02, NORMAL |
| `mcp__uw-pp__historical_gex_time_series` | symbol=ENPH, days=30, dte_max=45 | 6 regime flips; current POSITIVE since 5/14 |
| `mcp__uw-pp__historical_oi_trend` | symbol=ENPH, days=30, top_n=10 | 26 consecutive build days, +210k OI net |
| `mcp__uw-pp__historical_trend` | symbol=ENPH, days=30 | 20/26 bullish-flow sessions; +69.8% off lows |
| `mcp__uw-pp__historical_signal_backtest` | signal=bullish_flow, lookback=20, top_n=20 | 14 signals, **14.3% win rate**, avg −2.18% |

## Tool errors

None.

## Verdict for downstream phases

- **Volatility regime:** **RICH** (IV30d 95.4%, IV rank 85, percentile 100
  in available window, z +3.12). **Premium-selling slightly favored
  per VRP +0.115.**
- **Premium-flow environment:** Bullish-net for 90d at modest magnitude,
  bullish in 20/26 recent sessions.
- **Conviction that today's signal is HISTORICALLY EDGE-POSITIVE:**
  **2 / 5** — phase-1-5 signals are real and well-aligned, but the
  bullish_flow cohort backtest of 14.3% win rate / −2.18% avg move is a
  **major dampener**. The right reading is "the SETUP is strong on this
  ticker, but the REGIME has been punishing bullish-flow chases."
- **Three specific data points for phase-9:**
  1. **IV30d 95.4% / IV rank 85 / VRP +0.115** — pay up for long premium
     reluctantly; prefer credit structures or call spreads (not naked long
     calls).
  2. **GEX regime flip on 5/14** — long-gamma stabilization is 1 day old;
     a re-loss of $45 (phase-4) re-activates the negative-gamma trap.
  3. **Signal backtest 14.3% win rate / −2.18% avg** — penalize raw
     bullish-flow sizing; require ENPH-specific factors (sweep persistence
     5/5, DP buy_ratio 0.634, 5/22 catalyst) to do the directional work.
- **Open questions:**
  - Is the 5/22 catalyst a binary that justifies overriding the cohort
    backtest? (phase-6 must identify it.)
  - Does the ENPH-specific stack of dark pool buy-ratio + sweep persistence
    differ qualitatively from the cohort signals that failed? (phase-7
    insights_signal_confluence and phase-8 agents must opine.)
