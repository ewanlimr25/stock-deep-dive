# Phase 5 — Historical Context & VRP

**Ticker:** KWEB
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T00:00:00Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-4-structure.md

> **Gap caveat (MANDATORY):** the local series is non-contiguous — a 21-session
> hole 2026-03-28→04-24. All "30-day" / "90-day" windows below actually span the
> **31 sessions present** (2026-03-13…03-27 then 04-27…05-22), not a contiguous
> calendar window. N is small; treat percentiles/trends as low-to-moderate confidence.

## Summary

Today's setup is a **cheap-optionality, contrarian-bullish dip read fighting a
clear two-week downtrend**. IV30d (29.8%) sits at the **3.33 percentile** (z
−1.68, regime LOW_IV) and VRP is **−0.039** (realised 33.7% > implied 29.8%) → a
**premium-BUYING regime: favor debit/long structures, not credit**. Net premium
flow over the 31 sessions is a **modest persistent bullish lean (+$23.3M)**, and
the last two sessions are **bullish-skew days into a falling price** (05-21 net
+$16.1M, 05-22 +$2.65M) — a dip-accumulation signature. But price has fallen
**−12% from $30.59 (05-13) to $26.91**, total GEX has **collapsed $672M→$39M in 7
sessions** (the long-gamma pin is bleeding off → trending risk rising, confirming
phase-4's short-gamma-at-spot), and P/C is **normal** (no sentiment extreme). The
`bullish_flow` backtest reads 100% (13/13, +7.98% / 20d) — **but it is market-wide,
clustered in 05-19→05-21 (semis/index), and not KWEB**, so it signals a *supportive
late-May regime*, not a KWEB-specific edge.

## Key signals

- **IV cheap:** iv30d 29.8%, **iv_percentile 3.33**, z −1.675, regime LOW_IV
  `[HIST:iv_percentile_zscore]`.
- **VRP −0.039 (FAIR, realised>implied) → premium-buying** `[HIST:vrp]`.
- **GEX collapse:** total_gex $672M (05-13) → **$39M (05-22)**; 14 regime flips in
  31 sessions — pin weakening `[HIST:gex_time_series]`.
- **Cumulative flow BULLISH +$23.3M** (bullish $233.2M vs bearish $209.9M, 31
  sessions) `[HIST:cumulative_premium_flow]`.
- **Signal backtest bullish_flow 100% (13/13), +7.98%/20d — MARKET-WIDE, clustered,
  NOT KWEB** `[HIST:signal_backtest]`.

## Detailed findings

### IV regime (percentile + z + VRP)

- `iv_percentile` **3.33**, `iv_zscore` −1.675, regime **LOW_IV** — today's IV is
  near the bottom of the local window; the mid-May spike (iv_rank 88.8 on 05-13)
  pulled the range up, so iv_rank 38.9 (phase-0.5) but the *percentile* is low.
- `vrp` **−0.0394** (iv30d 0.2975 vs realised 0.3369), regime **FAIR** but realised
  > implied → **premium-buying**. Heuristic: IV cheap + VRP<0 ⇒ **favor debit
  structures** (buy calls/call spreads, do NOT sell premium). This is the single
  cleanest structural handoff to phase-9.

### Cumulative premium flow (31 sessions) `[HIST:cumulative_premium_flow]`

net_flow **+$23.3M** (bullish $233.2M / bearish $209.9M), trend **BULLISH** — a
~10% bullish skew, persistent but modest. Not a strong stealth-accumulation
footprint (would want a larger, monotone build); it is a mild standing bid.

### P/C ratio z-score `[HIST:pc_ratio_zscore]`

current 0.2506 vs mean 0.2249 (std 0.166), **z 0.154 → NORMAL**. KWEB is
structurally call-heavy; today is unremarkable for the name. **No contrarian
sentiment extreme** — do not read the low P/C as a fade signal.

### GEX time series (31 sessions) `[HIST:gex_time_series]`

- **Total GEX collapsed**: peak **$672M on 05-13** (spot $30.59) → $447M → … →
  $85M (05-21) → **$39M (05-22)**. As price fell away from the 29–31 call walls,
  the positive-gamma cushion bled off.
- **14 regime flips in 31 sessions** — KWEB whipsaws POSITIVE/NEGATIVE almost every
  other day, ZGL oscillating ~29.5 (negative days) vs 15–24 (positive days). Spot
  sits on a knife-edge gamma inflection.
- **Read:** the eroding GEX + frequent flips = **dealer pin weakening, larger
  ranges / more trend ahead** — corroborates phase-4 (short gamma at spot, "can
  trend rather than stick").

### OI trend `[HIST:oi_trend]`

`consecutive_build_days` **1**; 05-22 net OI +19,082 (217 increases vs 112
decreases). Today's build (Dec 30C, May 28.5C, Jul 25P — matches phase-3) is a
**single-session build, not a multi-day ramp** → tempers any "sustained stealth
accumulation" claim.

### Multi-day trend (selected) `[HIST:trend]`

| Date | Close | net_flow | IV rank | flow_dir |
|------|-------|----------|---------|----------|
| 05-13 | **30.59** | +8.70M | **88.8** | bullish (peak) |
| 05-15 | 28.18 | −2.24M | 63.8 | bearish |
| 05-18 | 28.06 | −1.15M | 52.0 | bearish |
| 05-20 | 28.12 | +0.40M | 39.7 | bullish |
| 05-21 | **27.63** | **+16.08M** | 45.5 | bullish (big two-sided: put prem $22.9M too) |
| 05-22 | **26.91** | +2.65M | 38.9 | bullish |

18 bullish / 12 bearish days. The tape is **bullish-flow into a falling price** for
the last two sessions — contrarian dip-buying, not trend confirmation. March had
the big bearish put days (03-23 net −$12.6M, 03-19 put prem $25.5M).

### Signal backtest (current signal's edge) `[HIST:signal_backtest]`

`signal_type=bullish_flow`, 20 trading-day forward: **win_rate 100% (13/13),
avg_move +7.98%**. **CRITICAL caveat:** these 13 signals are **MCHP, SNDK, MU,
QQQ, AMD, SPY, PANW, IWM, AMZN** — all semis/tech/index, all fired **05-19→05-21**,
and the late-May tape ripped. They are **highly correlated (~1–2 independent regime
draws), market-wide, and contain NO KWEB**. Reads as "the prevailing late-May
regime rewarded bullish flow," not a KWEB-specific historical edge. Phase-9 must
apply a strong N/independence haircut.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `historical_iv_percentile_zscore` | KWEB, 252 | iv %ile 3.33, z −1.68, LOW_IV (30 dates used) |
| `historical_vrp` | KWEB, 30 | vrp −0.039, FAIR, realised>implied |
| `historical_cumulative_premium_flow` | KWEB, 90 | net +$23.3M BULLISH (31 sessions) |
| `historical_pc_ratio_zscore` | KWEB, 20 | z 0.154, NORMAL |
| `historical_gex_time_series` | KWEB, 30, dte45 | GEX 672M→39M; 14 flips; pin weakening |
| `historical_oi_trend` | KWEB, 30, top10 | 1 consecutive build day; +19,082 today |
| `historical_trend` | KWEB, 30 | −12% 2-wk downtrend; 18 bull/12 bear days |
| `historical_signal_backtest` | bullish_flow, 20d, top20 | 100% (13/13) +7.98% — market-wide, NOT KWEB |

## Tool errors

No interpolation across the gap detected — `historical_trend` and
`cumulative_premium_flow` both list the actual 31 dates (gap 03-28→04-24 visible),
so the series is honest about the hole. Confidence is shrunk by the small true N
(31 sessions), not by silent interpolation.

## Verdict for downstream phases

- **Volatility regime:** **CHEAP** (IV 3.33 %ile, z −1.68) — options underpriced.
- **Premium environment:** **premium-BUYING** (VRP −0.039) → **favor DEBIT/long
  structures** (long calls or call spreads); do NOT sell premium into this.
- **Conviction that today's signal is HISTORICALLY EDGE-POSITIVE:** **3/5** — the
  *structure* (cheap calls) is favorably priced and the market regime rewards
  bullish flow, but KWEB itself is in a −12% downtrend with weakening gamma pin and
  the backtest is not name-specific.
- **Three specific data points:** IV %ile **3.33** (cheap); VRP **−0.039**
  (premium-buying); signal win rate **100% / n=13** (market-wide, low-independence).
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:              bullish_flow
  signal_backtest_win_rate:  1.00
  win_rate_n:                13
  win_rate_source:           backtest
  ```
  **Annotation for phase-9 (do not size to 1.00):** the n=13 is market-wide,
  clustered in a 3-day window, and excludes KWEB → effective independent N ≈ 1–2.
  Apply the N-conditional cap aggressively (`rubrics/sizing-rubric.md`); the
  *favorable-vol* signal (cheap IV / −VRP) is the more KWEB-relevant edge here.
- **Open questions:**
  1. Does KWEB **decouple** from the bullish US semis/index regime (it's China —
     own drivers)? phase-6/7c resolves.
  2. With the gamma pin eroding, is the next leg a **trend-down to 25–26** (phase-3
     put floor) or a **cheap-IV squeeze to 28–29** (phase-4 flip)? Macro + sentiment decide.
