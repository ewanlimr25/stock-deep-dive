# Phase 5 — Historical Context & VRP

**Ticker:** ADBE
**As-of date:** 2026-05-19
**Generated:** 2026-05-19T21:35:00Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-4-structure.md

## Summary

ADBE IV30d = **0.5555** ranks **100th percentile** (z-score **+2.27**) over
the 27 available trading days in the lookback — a **HIGH_IV regime** by
the tool's tag `[HIST:iv_percentile_zscore]`. VRP = **+11.35 vol-points**
(IV30d 0.5555 − realized 0.442) → **PREMIUM_SELLING regime**
`[HIST:vrp]`. OI has built for **17 consecutive sessions** (+219,392 net
contracts) — a sustained "BUILDING" trend tag `[HIST:oi_trend]`. Spot
trajectory 2026-04-27 close $239.31 → trough $234.80 on 2026-05-13 → up
to $255.05 on 2026-05-19, a **+8.6% recovery from the 5/13 low**
`[HIST:trend]`. GEX regime has been **highly unstable**: 10 of 17 sessions
were `FULLY_NEGATIVE` (most acutely 5/13-5/14 with total_gex down to
−$334M), with TWO regime flips in the last two sessions (5/18 NEG→POS,
5/19 POS→NEG) `[HIST:gex_time_series]`. P/C ratio z-score −0.426
(current 0.59 vs 17d mean 0.68) → **NORMAL** sentiment, slightly
call-heavier than average `[HIST:pc_ratio_zscore]`. 30-day cumulative
premium: bullish $1.18B / bearish $1.12B, **net +$58.2M bullish** but
tagged MIXED — close to balanced `[HIST:cumulative_premium_flow]`.
**Bottom line: IV is rich → favor credit/premium-selling structures; the
backdrop is recovery from a fully-negative-gamma washout that bottomed
~$235.**

## Key signals

- **IV30d 0.5555, percentile 100, z-score +2.27, regime HIGH_IV**
  `[HIST:iv_percentile_zscore]` — IV is at the top of its observable
  band. (Caveat: lookback `dates_used=27`, NOT the full 252 the tool
  request asked for — see phase-0 note re: gap in historical data.)
- **VRP +0.1135 (IV30d 0.5555 vs realized30d 0.442) — PREMIUM_SELLING**
  `[HIST:vrp]` — sellers are paid 11.35 vol-points over recent realized.
- **IV30d trajectory: 0.409 (5/01) → 0.516 (5/13) → 0.555 (5/19)**
  `[HIST:trend]` — IV climbed 14.6 vol-points across the selloff +
  recovery window, IV rank from 51 → 90.
- **Spot recovered +8.6% from 5/13 trough $234.80 to 5/19 close $255.05**
  `[HIST:trend]` — a textbook V-shape after a fully-negative-gamma flush.
- **OI build 17 consecutive days, net +219,392 contracts**
  `[HIST:oi_trend]` — positioning is layering on, not stale.
- **GEX regime instability: 10 of last 17 sessions FULLY_NEGATIVE,
  trough −$334M on 5/14; today total_gex now +$1.565B (largest in
  series)** `[HIST:gex_time_series]` — dealers went from massively short
  gamma to massively long in 4 sessions.
- **Two regime flips in the last 2 sessions** (5/18 NEG→POS at
  spot $252.90; 5/19 POS→NEG at $258.07) `[HIST:gex_time_series]` —
  spot is straddling ZGL.
- **P/C z-score −0.426 (NORMAL), 30d cumulative +$58.2M bullish but
  MIXED tag** `[HIST:pc_ratio_zscore] [HIST:cumulative_premium_flow]` —
  no sentiment extreme to fade.
- **Signal backtest for `dark_pool_accumulation` returned 0 historical
  firings** `[HIST:signal_backtest]` — backtest dataset is too sparse
  (likely because the dark-pool-tier classifier doesn't fire often at
  current thresholds); treat phase-2's accumulation read with no
  historical-edge calibration available.

## Detailed findings

### IV regime

| Metric | Value |
|--------|------:|
| Current IV30d | 0.5555 (55.55%) |
| IV percentile | **100** |
| IV z-score | **+2.27** |
| Lookback (effective) | 27 trading days |
| Regime tag | **HIGH_IV** |
| Realized vol30d | 0.442 (44.2%) |
| VRP (IV − realized) | **+0.1135** |
| VRP regime tag | **PREMIUM_SELLING** |

Read: with IV at the top of the available band and an 11.35-vol-point
premium over realized, **risk-reversal / call-spread / put-spread credit
structures are objectively favored over outright debit calls/puts**. A
long-vega trade today is paying the richest IV of the lookback.

### Cumulative premium flow (30 sessions, ~17 unique trading days)

| Metric | Value |
|--------|------:|
| Cumulative bullish premium | $1.180B |
| Cumulative bearish premium | $1.122B |
| Net flow (bull − bear) | **+$58.2M** |
| Trend tag | **MIXED** |

Read: aggregate 30-day flow is balanced (bull/bear ratio ~1.05). No
stealth institutional one-way build. Today's tape (phase-1) is a
single-day reading inside a flat-to-slightly-bullish multi-week base.

### P/C ratio z-score

| Metric | Value |
|--------|------:|
| Current P/C ratio | 0.59 |
| 17d mean | 0.6801 |
| 17d std | 0.2116 |
| z-score | **−0.426** |
| Tag | **NORMAL** |

Read: P/C 0.59 is slightly call-heavier than the recent mean — directionally
consistent with phase-3's bullish OI build, but well inside one sigma so
no contrarian / extreme-fade play.

### GEX time series (17 sessions)

| Date | Close | Total GEX ($) | ZGL | Regime |
|------|------:|--------------:|----:|--------|
| 2026-04-27 | 240.73 | +195,651 | 384.29 | NEGATIVE |
| 2026-04-28 | 243.47 | **−10,746,922** | — | **FULLY_NEGATIVE** |
| 2026-04-29 | 241.21 | **−5,794,485** | — | FULLY_NEGATIVE |
| 2026-04-30 | 242.51 | **−134,154,788** | — | FULLY_NEGATIVE |
| 2026-05-01 | 250.16 | **−26,905,080** | — | FULLY_NEGATIVE |
| 2026-05-04 | 253.89 | +60,388,709 | 289.73 | NEGATIVE |
| 2026-05-05 | 254.38 | **−76,228,655** | — | FULLY_NEGATIVE |
| 2026-05-06 | 251.31 | **−66,201,365** | — | FULLY_NEGATIVE |
| 2026-05-07 | 257.08 | +149,206,201 | 285.84 | NEGATIVE |
| 2026-05-08 | 250.91 | +253,676,890 | 268.90 | NEGATIVE |
| 2026-05-11 | 246.67 | **−105,483,149** | — | FULLY_NEGATIVE |
| 2026-05-12 | 242.64 | **−128,311,143** | — | FULLY_NEGATIVE |
| 2026-05-13 | **234.80** | **−140,466,313** | — | FULLY_NEGATIVE |
| 2026-05-14 | 236.27 | **−334,242,681** | — | FULLY_NEGATIVE |
| 2026-05-15 | 245.58 | +120,472,190 | 277.92 | NEGATIVE |
| 2026-05-18 | 252.90 | +861,581,750 | **140.02** | **POSITIVE** |
| 2026-05-19 | 258.07 | **+1,565,257,615** | **259.48** | NEGATIVE |

Two **regime flips** detected:
- 2026-05-18: NEGATIVE → POSITIVE (ZGL Δ −137.9)
- 2026-05-19: POSITIVE → NEGATIVE (ZGL Δ +119.46)

Read: ADBE has gone through a **gamma-driven washout-and-recovery**.
Through 4/28-5/14, dealers were structurally short gamma (FULLY_NEGATIVE
total_gex on 10 of 13 sessions), which would have AMPLIFIED the selloff
to the 5/13 $234.80 trough. The OI build over 5/15-5/19 has reversed
total_gex to deeply positive, but the **ZGL has whipsawed $137 in two
sessions** — a sign that aggressive new positioning is still reshaping
the surface. Treat dealer flows as **unstable** for the next 2-3
sessions; the GEX picture from phase-4 ($260 mega wall) may shift if
volume keeps building.

### OI trend (17 sessions, top contracts per day)

| Date | Contracts ↑ | Contracts ↓ | Net OI Δ | Notable build |
|------|------------:|------------:|---------:|---------------|
| 2026-05-19 | 449 | 183 | **+15,976** | 5/22 $265C +1,135 |
| 2026-05-18 | 394 | 159 | +15,963 | 5/29 $300C +1,523, 5/29 $200P +1,393 |
| 2026-05-15 | 415 | 141 | +10,516 | 5/15 $247.5C +2,370 (0DTE), 5/15 $245C +1,512 |
| 2026-05-14 | 552 | 199 | +10,854 | 6/18 $150P +1,007 (deep OTM hedge) |
| 2026-05-13 | 426 | 167 | +8,241 | 6/18 $220P +1,154, 6/18 $260C +839 |
| 2026-05-12 | 518 | 167 | **+16,450** | 5/29 $280C +1,451, 6/17/27 $480C +1,388, 5/29 $300C +1,378 |
| 2026-05-11 | 445 | 176 | +10,163 | 6/18 $230P +1,271, 6/18 $270C +1,162, 6/18 $210P +951 |
| 2026-05-08 | 443 | 245 | +12,046 | 5/15 $265C **+3,572** (biggest single line) |
| 2026-05-07 | 425 | 174 | +9,436 | 5/8 $237.5P +721, 5/8 $242.5P +695 (selloff-day put hedging) |
| 2026-05-06 | 412 | 177 | +13,619 | 11/20 $515C +747, 11/20 $510C +734 (LEAP-distance call build) |
| 2026-05-05 | 511 | 219 | +15,268 | 5/8 $265C **+2,587**, 5/8 $275C +1,276 |
| 2026-05-04 | 427 | 199 | **+19,629** | 5/15 $265C +2,213, 6/18 $250C +1,016, 6/05 $230P +1,006 |
| 2026-05-01 | 374 | 197 | +10,960 | 5/01 $247.5C +1,592 (0DTE pin), 6/05 $220P +1,284 |
| 2026-04-30 | 322 | 161 | +3,777 | 5/01 $230P +1,274 (puts hedging earnings-adjacent) |
| 2026-04-29 | 386 | 158 | +11,507 | 5/01 $222.5P +1,965 (puts) |
| 2026-04-28 | 562 | 144 | **+21,924** | 6/18 $200P +1,824, 5/01 $252.5C +1,489, 5/01 $265C +1,450 |
| 2026-04-27 | 470 | 161 | +13,063 | 5/01 $285C +1,208, 5/8 $260C +869 |
| **TOTAL** | — | — | **+219,392** | **17 consecutive build days** |

Read: positioning is being layered on **methodically and persistently**.
The early-period (4/27-5/01) builds were heavy on near-term puts at $200-
$230 strikes (the May 13 selloff to $234.80 vindicated those buyers).
The mid-period (5/04-5/14) shifted to a mix of June OTM calls + puts.
The recent period (5/15-5/19) is **call-dominant** at $245-$282.5
strikes for the 5/22 and 5/29 expiries. **The buildup has rotated from
defensive to constructive across the 3-week window.**

### Multi-day trend table (17 sessions)

| Date | Close | IV30d | IV rank | P/C | Net flow ($M) | Flow tag |
|------|------:|------:|--------:|----:|--------------:|----------|
| 2026-05-19 | 255.05 | 0.5555 | **89.6** | 0.59 | −0.64 | bearish |
| 2026-05-18 | 255.64 | 0.5257 | 83.7 | 0.44 | +1.90 | bullish |
| 2026-05-15 | 247.61 | 0.5278 | 84.7 | 0.49 | +3.45 | bullish |
| 2026-05-14 | 237.01 | 0.5299 | 84.8 | 0.71 | +2.56 | bullish |
| 2026-05-13 | 236.07 | 0.5169 | 81.2 | 0.82 | −0.44 | bearish |
| 2026-05-12 | 240.83 | 0.5134 | 80.2 | 0.68 | −2.42 | bearish |
| 2026-05-11 | 246.15 | 0.5179 | 81.5 | 0.52 | −2.00 | bearish |
| 2026-05-08 | 253.06 | 0.4216 | 53.9 | 0.60 | −2.70 | bearish |
| 2026-05-07 | 256.51 | 0.4463 | 61.4 | 0.46 | +0.69 | bullish |
| 2026-05-06 | 250.17 | 0.4306 | 57.0 | 0.79 | +1.16 | bullish |
| 2026-05-05 | 255.61 | 0.4278 | 54.5 | 0.50 | +2.28 | bullish |
| 2026-05-04 | 253.96 | 0.4254 | 55.6 | 0.67 | +1.56 | bullish |
| 2026-05-01 | 250.71 | 0.4094 | 51.1 | 0.50 | −0.91 | bearish |
| 2026-04-30 | 246.25 | 0.4098 | 51.5 | 0.74 | −1.07 | bearish |
| 2026-04-29 | 243.57 | 0.4362 | 58.6 | 0.87 | −0.22 | bearish |
| 2026-04-28 | 243.20 | 0.4317 | 57.4 | 0.69 | −2.36 | bearish |
| 2026-04-27 | 239.31 | 0.4486 | 62.1 | 0.78 | −1.34 | bearish |

Summary: **7 bullish / 10 bearish days**, latest = bearish (5/19 net
−$0.64M). The bullish-flow days cluster around 5/04-5/07 and 5/14-5/18
(the dip-buy windows). IV30d expanded steadily from 0.41 to 0.55 across
the 3-week window — a **classic event-runup** pattern.

### Signal backtest

```
mcp__uw-pp__historical_signal_backtest(signal-type=dark_pool_accumulation,
  lookback-days=5, top-n=25) → {"total_signals": 0,
  "note": "no backtest results"}
```

Tool returned zero historical firings for the `dark_pool_accumulation`
signal in the lookback window. Possible causes:
- The classifier requires a higher tier mix that didn't materialize in
  the lookback (only 17 unique trading days available, see phase-0).
- ADBE-specific accumulation signals may rarely cross the threshold.

**No historical edge calibration available for the dominant
phase-2 signal.** Phase-9 conviction sizing must rely on the
qualitative read instead of a backtest win-rate.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__historical_iv_percentile_zscore` | symbol=ADBE, lookback-days=252 | IV percentile 100, z +2.27, HIGH_IV (effective lookback 27d) |
| `mcp__uw-pp__historical_vrp` | symbol=ADBE, date=2026-05-19 | VRP +0.1135, PREMIUM_SELLING |
| `mcp__uw-pp__historical_cumulative_premium_flow` | symbol=ADBE, days=30 | +$58.2M net, MIXED |
| `mcp__uw-pp__historical_pc_ratio_zscore` | symbol=ADBE, lookback-days=17 | z −0.426, NORMAL |
| `mcp__uw-pp__historical_gex_time_series` | symbol=ADBE, days=17, dte-max=45 | 2 flips, 10 FULLY_NEGATIVE sessions |
| `mcp__uw-pp__historical_oi_trend` | symbol=ADBE, days=17, top-n=15 | BUILDING 17 days, +219,392 net |
| `mcp__uw-pp__historical_trend` | symbol=ADBE, days=17 | 7 bull / 10 bear, latest bearish, IV30d 0.41→0.56 |
| `mcp__uw-pp__historical_signal_backtest` | signal-type=dark_pool_accumulation, lookback-days=5, top-n=25 | **0 results** |

## Tool errors

`historical_signal_backtest` returned no signals (not an error per se,
but a calibration gap — see above).

## Verdict for downstream phases

- **Bias from this phase:** **IV REGIME = RICH → favor credit structures.**
  Directionally **constructive-but-cautious**: recovery from washout,
  OI building, but GEX regime unstable and today's flow tagged
  bearish.
- **Premium-buying vs selling environment:** **PREMIUM SELLING** —
  VRP +11.35 vol-pts, IV at top of band.
- **Conviction this signal is historically edge-positive:** **2/5** —
  no historical backtest available for the dominant phase-2 signal;
  the IV rank + VRP combo is itself a well-validated premium-sell
  setup, but ADBE-specific calibration is missing.
- **Three specific data points for phase-9:**
  1. **IV30d 0.5555, percentile 100, z +2.27** — credit structures
     are objectively cheap to sell here.
  2. **VRP +11.35 vol-points** — sell premium / collect theta favored.
  3. **OI net +219,392 across 17 consecutive build days** —
     positioning is fresh and increasing; no sign of distribution.
  4. **Spot recovered +8.6% from 5/13 trough $234.80** — V-shape
     post fully-negative gamma washout; 5/13 low becomes the
     reference floor.
- **Open questions:**
  - Why the IV expansion? Earnings (phase 6) AND/OR macro tape (phase 6)?
  - Does the "MIXED" 30-day cumulative flow conceal a regime change
    in the most recent week? — phase-7 insights composite may help.
  - The signal backtest returned empty — is there a richer historical
    archive (>27d) we could request? Out of scope for this phase.
