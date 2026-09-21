# Phase 5 — Historical Context & VRP

**Ticker:** SMH
**As-of date:** 2026-05-28
**Generated:** 2026-05-29T12:55:00Z
**Upstream phases cited:** phase-4-structure.md, phase-3-positioning.md, phase-1-flow.md, phase-0-intake.md

## Summary

Today's flow sits inside a **persistent net-short-gamma regime that has run the
entire $544→$600 rally** — SMH was FULLY_NEGATIVE GEX on 05-15/18/19/26/27 (total
GEX −$113M to −$37M) `[HIST:gex_time_series]`, meaning the +10% melt-up was
*dealer-amplified*, and a reversal would be amplified the same way down (the exact
risk the June puts hedge). **IV is rich** — 78.8th percentile (of 33 available
sessions), z +1.02, and **VRP +0.089 → PREMIUM_SELLING regime** (IV 46.2% vs
realized 37.3%) `[HIST:vrp]`, so debit put-buying is paying up and credit/premium-
selling structures are favoured. The name is **extremely extended** (`fz`: RSI 71.4
overbought, +24.8% over 50-DMA, +54.9% over 200-DMA, +66.6% YTD, −2.0% from the
52-wk high) `[HIST:rsi fz][HIST:52w_proximity fz]`. The historical edge of a
*bearish* bet is weak — **bearish_flow win-rate 55.6% (N=9)** vs **bullish_flow
100% (N=6)** `[HIST:signal_backtest]`: betting against semis has lost in this regime,
which corroborates that the put flow is **protective hedging, not directional short
conviction**.

## Key signals

- **Short-gamma regime persisted through the whole rally** — FULLY_NEGATIVE GEX
  most of mid/late May; today still net −$26.5M. Vol-expansion risk both ways
  `[HIST:gex_time_series]`.
- **VRP +0.089, PREMIUM_SELLING** (IV 46.2% > RV 37.3%) → favour credit structures;
  buying premium outright is expensive `[HIST:vrp]`.
- **IV 78.8th percentile, z +1.02** over 33 sessions (gap-limited, not a true 1y)
  `[HIST:iv_percentile_zscore]`.
- **Extremely extended** — RSI 71.4, +54.9% over 200-DMA, +66.6% YTD, −2.0% from
  52-wk high `[HIST:rsi fz]`.
- **Bearish edge weak:** bearish_flow 55.6% (N=9) vs bullish_flow 100% (N=6) — the
  regime has punished shorts `[HIST:signal_backtest]`.

## Detailed findings

### IV regime

| Metric | Value | Read |
|--------|-------|------|
| current IV30d | 0.4622 | — |
| IV percentile | **78.79** (33 sessions used) | rich, but window is gap-limited (not 1y) |
| IV z-score | +1.023 | ~1σ above mean |
| VRP (IV−RV30) | **+0.089** | **PREMIUM_SELLING** — IV 46.2% vs RV 37.3% |

`[HIST:iv_percentile_zscore][HIST:vrp]`. The vol-risk-premium is the cleaner edge
here than direction: options are pricing ~9 vol points over realized.

### P/C ratio z-score (20d)

current P/C **7.26**, 20d mean 3.87, std 1.88, **z +1.81**, extreme **NORMAL**
`[HIST:pc_ratio_zscore]`. Put-skew is elevated (+1.8σ) but **not a 2σ extreme** —
consistent with phase-4's NORMAL 30D skew: heavy but orderly hedging, not panic.

### GEX time series (30d) `[HIST:gex_time_series]`

| Date | Spot | Regime | total_gex |
|------|------|--------|-----------|
| 05-15 | 559.35 | FULLY_NEGATIVE | −134.1M |
| 05-18 | 544.23 | FULLY_NEGATIVE | −113.4M |
| 05-20 | 562.48 | FULLY_NEGATIVE | −58.1M |
| 05-22 | 576.82 | POSITIVE | +2.3M |
| 05-26 | 601.57 | FULLY_NEGATIVE | −17.0M |
| 05-27 | 594.25 | FULLY_NEGATIVE | −36.8M |
| 05-28 | 600.38 | "POSITIVE" (label) | **−26.5M** |

Regime-flip dates: 05-07 (NEG→POS, spot 540) and 05-14 (POS→NEG, spot 579). The
ZGL-based "regime" label is noisy (today says POSITIVE while total_gex is −26.5M);
the **total_gex sign is the reliable read: persistently net short gamma.** The note:
"regime flips empirically precede realised-vol expansion." SMH has flipped repeatedly
— vol expansion is the base case if a catalyst hits.

### OI trend (30d) `[HIST:oi_trend]`

**consecutive_build_days = 30** — OI built every available session. Largest build
days: 05-26 +342,916, 05-18 +361,120, 04-27 +182,432. Today +97,300 (1,126 strikes
up vs 427 down). Relentless OI accretion = sustained positioning (rally longs +
laddered put hedges), not a one-day spike. **Gap caveat:** the "30 consecutive"
spans the 21-session hole (03-28→04-24); it is 30 *available* sessions, not 30
contiguous calendar days.

### Multi-day trend (IV rank / PCR) `[HIST:trend]`

IV rank persistently high (71–93 over the window; today 84.6). P/C ratio elevated
and choppy (2.5–9.3; today 7.26). Vol/premium fields returned null (parsing) — IV
rank and PCR are the usable columns. The takeaway: **IV has stayed rich through the
whole rally**, and put-skew has been consistently elevated — hedging has been a
standing feature, not a one-day event.

### Price context (`fz`, advisory) `[HIST:rsi fz][HIST:52w_proximity fz]`

| Field | Value | Read |
|-------|-------|------|
| RSI(14) | **71.39** | overbought (>70) |
| vs SMA20 | +7.65% | extended |
| vs SMA50 | +24.80% | very extended |
| vs SMA200 | **+54.89%** | extremely extended |
| Perf YTD | **+66.56%** | parabolic YTD |
| 52W High | 612.30 (**−2.04%**) | at the highs |
| 52W Low | 235.37 (+154.85%) | up 155% off the low |

Independent EOD confirmation that SMH is overbought at the highs on enormous gains —
**tempers any fresh-breakout long** and makes the protective hedging entirely
rational (holders insuring a +66% YTD position). Advisory only; not in the Kelly `p`.

### Signal backtest (current signal's edge) `[HIST:signal_backtest]`

| Signal type | win_rate | N | avg_move | read |
|-------------|----------|---|----------|------|
| **bearish_flow** (matches phase-1) | **55.6%** | **9** | 0.47% | barely edge-positive, low N |
| bullish_flow (context) | 100.0% | 6 | 2.09% | regime rewards longs |
| dark_pool_accumulation | n/a | 0 | — | no signals (≡ phase-2 mixed) |

Market-wide, in-sample backtest ("not a robust live edge" per tool). The bear edge
is weak *and* the regime has rewarded the opposite side — a strong caution against
sizing a directional short. Latest-anchor: all trailing reads anchor to the latest
available date (2026-05-28 = as-of), so reproducible for this run.

## Tool calls (audit trail)

| Command | Result summary |
|---------|----------------|
| `uw historical iv-percentile-zscore --symbol SMH --lookback-days 252` | 78.8 %ile, z +1.02 (33 sessions) |
| `uw historical vrp --symbol SMH --realised-window-days 30` | +0.089, PREMIUM_SELLING |
| `uw historical pc-ratio-zscore --symbol SMH --lookback-days 20` | z +1.81, NORMAL |
| `uw historical gex-time-series --symbol SMH --days 30 --dte-max 45` | persistent short-gamma; flips 05-07/05-14 |
| `uw historical oi-trend --symbol SMH --days 30` | 30 consecutive build days |
| `uw historical trend --symbol SMH --days 30` | IV rank 71–93, PCR elevated |
| `uw historical signal-backtest --signal-type bearish_flow/bullish_flow/dark_pool_accumulation` | 55.6%/100%/n-a |
| `fz quote SMH` (advisory) | RSI 71.4, +54.9% over 200-DMA, +66.6% YTD |

## Tool errors

- `uw historical trend` returned null `total_volume`/`total_premium` (field-name
  mismatch); IV rank + PCR usable.
- **Gap-affected reads:** `iv-percentile-zscore` used only **33 sessions** (not 252)
  and `oi-trend`'s "30 consecutive build days" spans the 21-session hole
  (03-28→04-24) — both report *available* sessions, not calendar windows. Treat IV
  percentile as a ~6-week percentile, not a 1-year one. (Per phase-0 date list /
  `lib/duckdb-cuts.md § gap`.)

## Verdict for downstream

- **Volatility regime:** **RICH** — IV 78.8 %ile, z +1.02, **VRP +0.089
  (PREMIUM_SELLING)**. The cleaner edge is the vol-risk-premium, not direction.
- **Premium environment:** **premium-SELLING favoured** — debit put-buying pays up;
  credit/defined-risk structures monetize the rich IV. (Phase-9: lean credit, not
  debit, for any expression.)
- **Conviction that today's signal is HISTORICALLY EDGE-POSITIVE:** **2/5 for a
  directional-bearish read** (55.6%, N=9, and bullish_flow is 100% in this regime —
  shorts have lost); **3–4/5 that the vol-rich/premium-selling read is edge-positive.**
- **Three specific datapoints:** IV %ile **78.8** (33 sessions); VRP **+0.089**
  (PREMIUM_SELLING); bearish_flow win-rate **55.6%** (N=9).
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:               bearish_flow
  signal_backtest_win_rate:   0.556
  win_rate_n:                 9
  win_rate_source:            backtest
  ```
  (Market-wide, in-sample, low N — phase-9 applies the N-conditional Kelly cap;
  with N=9 and p≈0.556 the empirical edge is thin and should size *small*.)
- **Open questions:** Does phase-6 identify the ~June 4–5 catalyst the front-end IV
  (84%) is pricing? Given rich IV + persistent short-gamma + extreme extension, the
  highest-expectancy expression may be **defined-risk premium-selling around the
  $585–620 pin** rather than a directional bet — confirm against macro (phase-6) and
  the desk views (phase-8).
