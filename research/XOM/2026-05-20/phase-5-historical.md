# Phase 5 — Historical Context & VRP

**Ticker:** XOM
**As-of date (user request):** 2026-05-20
**Effective data date:** 2026-05-18
**Generated:** 2026-05-19T00:00:00Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-4-structure.md

## Summary

The historical context **partially corroborates and partially complicates**
the bullish setup. **Confirming the bull case:** XOM total GEX has expanded
from $3.85B (2026-05-14) to **$23.2B (2026-05-18) — a ~6× explosion in 4
sessions**, with the regime stable POSITIVE since 2026-05-08. Today added
+34,856 net OI contracts (317 increases vs 141 decreases) — the largest
single-day net build in the 27-day window. **Complicating the bull case:**
the `historical_signal_backtest(bullish_flow, 20d)` returned a **win_rate of
0.0% across 12 signals**, with an average 20-day move of **-3.39%**. The 90-day
cumulative premium flow is **MIXED** (bullish $425.2M vs bearish $431.5M, net
-$6.3M). IV regime is NORMAL (IV %ile 65.4, z 0.486) and VRP is essentially
zero (0.24 pts) → **no premium edge in either debit or credit structures**.
P/C ratio z-score is -0.738 (slightly below average, not extreme).

## Key signals

- **Total GEX 4-day surge: $3.85B → $23.2B (6.0×).** ZGL collapsed from
  $149.85 (May 13) → $55.03 (May 18), meaning dealer long-gamma exposure now
  extends much farther below spot. Regime stable POSITIVE for 8 consecutive
  sessions since the 2026-05-08 flip. [HIST:gex_time_series]
- **Today's net OI Δ +34,856 contracts** with 317 increases vs 141
  decreases — `consecutive_build_days = 1` (i.e., yesterday was not a build
  day, this is a regime change). [HIST:oi_trend]
- **`bullish_flow` signal backtest: 0.0% win rate over 12 signals in the
  last 20 days, avg 20-day move -3.39%.** The signals are mostly mega-cap
  tech (MSFT, AAPL, NVDA, TSLA, META, AVGO, GOOGL, SMH, QQQ) — XOM is not in
  the signal universe but the macro context is "fade the bullish-flow buyers".
  This is the **single most damaging signal in the run** for the bull case.
  [HIST:signal_backtest]
- **VRP = 0.0024 (IV30d 31.49% ≈ RV30 31.25%) — FAIR regime.** No edge
  selling premium, no edge buying premium. [HIST:vrp]
- **90-day cumulative premium flow: -$6.3M net** ($425.2M bullish vs $431.5M
  bearish). No sustained directional build — today's bullish OI is a regime
  shift, not the continuation of a months-long campaign. [HIST:cumulative_premium_flow]

## Detailed findings

### IV regime

| Metric | Value | Regime |
|--------|-------|--------|
| Current IV30d | 31.49% | NORMAL |
| 1-year IV percentile | 65.38 | Above median, not extreme |
| 1-year IV z-score | 0.486 | Mild positive |
| Realised vol 30d | 31.25% | Mid-range |
| **VRP (IV − RV)** | **+0.24 pts** | **FAIR** |
| Latest IV rank (per `historical_trend`) | 73.27 | Elevated within trailing window |

VRP near zero means options are *fairly priced* — there is no systematic
edge to selling premium (typical when IV > RV) or buying premium (when IV <
RV). For phase 9, this means **directional debit structures and credit
spreads are roughly equally fair**; selection should be driven by the
structural (phase 3 / 4) edge, not vol mispricing.

The IV percentile 65 vs IV rank 73 disagreement is methodological: percentile
is rank-based (where current IV sits in the 1y distribution), IV rank is
range-based (where current IV sits between 1y min and max). Both say
"elevated but not extreme."

### Cumulative premium flow (90d)

- Cumulative bullish premium: $425,221,698
- Cumulative bearish premium: $431,511,921
- **Net 90-day flow: -$6,290,223** (essentially balanced)
- Trend direction: **MIXED**

Dates covered: 27 sessions spanning 2026-03-13 to 2026-05-18 (the early-to-mid
April gap noted in phase 0 is real — the tool reports 27 dates of data over a
90-calendar-day window).

Interpretation: there is no quiet 90-day stealth campaign in either direction.
The Jun'26 165C +8,150 OI build (phase-3) is a **fresh** institutional bet —
not the climax of a slow accumulation. This raises execution risk: a single
large bull position can be unwound or rolled away just as quickly as it was
built.

### P/C ratio z-score (20-day window)

| Metric | Value |
|--------|-------|
| Current PC ratio | 0.3087 |
| 20-day mean | 0.4567 |
| 20-day std | 0.2004 |
| **z-score** | **-0.738** |
| Extreme | NORMAL |

Today's PC ratio (calls dominant) is ~3/4 of a standard deviation below the
trailing 20-day mean — directionally consistent with bullish OI build but
**not at an extreme that would warrant contrarian positioning** (|z| > 2 is
the contrarian threshold per skill rubric).

### GEX time series (30-day regime trajectory)

27 days of GEX history. **11 regime flips** observed — the dealer book has
been volatile around the spot price. Last flip was 2026-05-08 (NEGATIVE →
POSITIVE). **Regime has been stable POSITIVE for 8 consecutive sessions.**

Recent trajectory (most consequential):

| Date | Spot | Total GEX | ZGL | Regime |
|------|------|-----------|-----|--------|
| 2026-05-06 | $148.25 | $1.91B | $153.59 | NEGATIVE |
| 2026-05-07 | $145.73 | $1.39B | $159.22 | NEGATIVE |
| 2026-05-08 | $144.84 | $-303M | $50.00 | **POSITIVE** (flip) |
| 2026-05-11 | $148.22 | $4.63B | $50.04 | POSITIVE |
| 2026-05-12 | $150.80 | $2.52B | $90.00 | POSITIVE |
| 2026-05-13 | $150.98 | $1.30B | $149.85 | POSITIVE |
| 2026-05-14 | $152.47 | $3.85B | $90.06 | POSITIVE |
| 2026-05-15 | $156.10 | $11.0B | $60.01 | POSITIVE |
| **2026-05-18** | **$160.09** | **$23.2B** | **$55.03** | **POSITIVE** |

Read: the POSITIVE regime flip on May 8 coincided with a near-term price low
($144.84) and the start of the +11% rally to $160.49. GEX has been expanding
since but the rate of expansion in the last 3 sessions (May 14 → May 18:
$3.85B → $23.2B) is **abnormal and largely driven by today's +8,150 OI build
on Jun'26 165C**. This is recency-biased — a single contract is doing most
of the work in the GEX number.

**Implication:** if the Jun'26 165C position is unwound (sold to close
through May 22 OPEX week), aggregate GEX could collapse just as rapidly,
flipping the dealer regime and removing the long-gamma support that
phase-4 leans on.

### OI trend (30-day, today vs trailing)

| Date | Total OI | Daily Δ |
|------|----------|---------|
| 2026-03-13 | 1,385,301 | (baseline) |
| 2026-03-20 | 1,394,193 | peak |
| 2026-03-27 | 1,248,741 | post-March OPEX |
| 2026-04-27 | 1,168,518 | low-mid |
| 2026-05-04 | 1,160,688 | drift |
| 2026-05-11 | 1,161,979 | drift |
| 2026-05-14 | 1,197,945 | building |
| 2026-05-15 | 1,143,263 | **post-monthly-OPEX drop** |
| **2026-05-18** | **1,025,686** | **-10.3% from May 15** |

May 15 was the May monthly OPEX. The 10% OI drop from 5/15 → 5/18 is the
expected post-OPEX roll-off. **Despite the gross OI decline, today the
chain ADDED +34,856 net OI contracts via 317 increases against 141
decreases** — a fresh repositioning into the now-emptier chain.

`consecutive_build_days = 1` confirms this is a **new** build day, not a
continuation of a multi-day campaign.

### Multi-day trend table (key dates)

Selected from `historical_trend` (full 27-day table available in source data):

| Date | Close | IV30 | IVR | Net flow ($) | PCR | Flow dir |
|------|-------|------|-----|--------------|------|---|
| 2026-03-13 | 156.12 | 32.8% | 45.8 | -201,653 | 0.30 | bearish |
| 2026-03-20 | 159.67 | 31.6% | 42.2 | +628,451 | 0.28 | bullish |
| 2026-03-27 | 170.99 | 34.3% | 50.4 | -4,432,062 | 0.38 | bearish |
| 2026-04-27 | 148.19 | 31.8% | 74.8 | -23,848 | 0.39 | bearish |
| 2026-04-30 | 154.41 | 31.5% | 74.4 | +95,486 | 0.55 | bullish |
| 2026-05-08 | 144.29 | 28.7% | 56.7 | -329,844 | 0.43 | bearish |
| 2026-05-13 | 151.57 | 29.2% | 60.9 | +2,807,403 | 0.61 | bullish |
| 2026-05-15 | 157.89 | 31.5% | 70.0 | -225,419 | 0.30 | bearish |
| **2026-05-18** | **160.49** | **31.5%** | **73.3** | **+306,031** | **0.31** | **bullish** |

The price round-trip is striking: from $170.99 on 2026-03-27 → $144.29 low on
2026-05-08 (-15.6%) → recovery to $160.49 today (+11.2% from low). Net
$170.99 → $160.49 = **-6.1% from late-March peak**. We are **mid-recovery**, not at a new
high.

13 bullish days vs 14 bearish days in the 27-day window confirms the MIXED
classification.

### Signal backtest (`bullish_flow`, 20-day forward, top 20)

**Win rate: 0.0% — 12 of 12 signals went DOWN.** Average 20-day move: **-3.39%**.

Signal universe (none are XOM, all are mega-cap tech / broad indexes that
appeared in bullish_flow lists 2026-05-13 to 2026-05-15):

| Date | Ticker | Signal price | 20d-later price | % change |
|------|--------|--------------|-----------------|----------|
| 2026-05-15 | MSFT | 422.05 | 417.42 | -1.10% |
| 2026-05-15 | AAPL | 300.37 | 298.97 | -0.47% |
| 2026-05-15 | UPS | 99.00 | 96.83 | -2.19% |
| 2026-05-14 | QQQ | 719.79 | 701.53 | -2.54% |
| 2026-05-14 | SMH | 578.34 | 543.96 | -5.94% |
| 2026-05-14 | META | 618.43 | 602.61 | -2.56% |
| 2026-05-14 | AVGO | 439.79 | 411.07 | -6.53% |
| 2026-05-13 | TSLA | 445.27 | 404.11 | -9.24% |
| 2026-05-13 | NVDA | 225.83 | 220.61 | -2.31% |
| 2026-05-13 | GOOGL | 402.62 | 387.66 | -3.72% |
| 2026-05-13 | META | 616.63 | 602.61 | -2.27% |
| 2026-05-13 | QQQ | 714.71 | 701.53 | -1.84% |

**Caveat:** This is a market-wide tech-heavy signal universe. None of these
are XOM. The 20-day backward look picks signals from May 13-15, after which
a broader tech correction unfolded. **Energy may not be fully correlated**
with this backtest — but the macro environment in which "bullish flow
underperforms" is the regime we're in.

The honest read: in the **last 20 trading days**, every single "bullish flow"
top-20 signal has lost money over 20-day forward. That is a *very loud* macro
signal — independent of the strength of XOM's specific setup, the universe
of bullish flow signals has been a losing trade. Phase 9 must size this in.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__historical_iv_percentile_zscore` | symbol=XOM, lookback-days=252 | IV %ile 65.4, z 0.49, regime NORMAL |
| `mcp__uw-pp__historical_vrp` | symbol=XOM, realised-window-days=30, date=2026-05-18 | VRP +0.24 pts, regime FAIR |
| `mcp__uw-pp__historical_cumulative_premium_flow` | symbol=XOM, days=90 | bullish $425M, bearish $432M, net -$6.3M, MIXED |
| `mcp__uw-pp__historical_pc_ratio_zscore` | symbol=XOM, lookback-days=20 | PCR 0.31 vs mean 0.46, z -0.738, NORMAL |
| `mcp__uw-pp__historical_gex_time_series` | symbol=XOM, days=30, dte-max=45 | 27 days, 11 flips, last flip 2026-05-08 (→POSITIVE); GEX $23.2B (6× expansion in 4d) |
| `mcp__uw-pp__historical_oi_trend` | symbol=XOM, days=30, top-n=10 | Today net OI Δ +34,856; consecutive_build_days=1; Total OI 1.03M (-10% post-OPEX) |
| `mcp__uw-pp__historical_trend` | symbol=XOM, days=30 | 27d window: 13 bullish / 14 bearish days; latest flow=bullish; price -6.1% from 3/27 peak |
| `mcp__uw-pp__historical_signal_backtest` | signal-type=bullish_flow, lookback-days=20, top-n=20 | 12 signals, **0.0% win rate**, avg -3.39%, all mega-cap tech/indexes |

## Tool errors

None.

## Verdict for downstream phases

- **Volatility regime: NORMAL / FAIR.** IV %ile 65, z 0.49, VRP +0.24. No
  systematic edge to buying or selling vol. Phase 9 structure choice should
  be driven by directional thesis, not vol mispricing.
- **Premium environment:** **FAIR (debit and credit equally priced).** With
  call IV > put IV (phase 4 COMPLACENT skew), put-credit structures are
  marginally cheap relative to call-debit structures. Direction asymmetric
  but not edge-grade.
- **Conviction on HISTORICAL edge of today's signal:** **2/5.** The 0% win
  rate on bullish_flow backtest is a major drag, partially offset by the
  energy-vs-tech rotation argument (XOM is not in the backtest universe and
  energy has historically diverged from mega-cap tech in mid-cycle macro
  rotation). The 90-day cumulative premium flow is also flat (MIXED), so
  today's build is fresh and unsupported by months-long accumulation.
- **Three specific data points for phase 9:**
  1. **IV %ile 65.4, VRP +0.24** — fair-vol environment, structure-agnostic.
  2. **GEX $23.2B / 6× expansion in 4 days** — current dealer support is
     real but **fragile** (single-day repositioning could unwind it).
  3. **`bullish_flow` 20-day backtest win rate 0.0%** — macro is hostile to
     long-flow-following trades right now. Size SMALLER than confluence
     alone would suggest, or build invalidation into the entry.
- **Open questions:**
  - **How does XOM correlate with mega-cap tech in the May 2026 correction?**
    If energy is uncorrelated/inversely correlated, the 0% backtest may not
    apply. Phase 6 macro/oil regime must answer this.
  - **What was the catalyst for the 2026-03-27 → 2026-05-08 -15.6% decline?**
    Need to verify there's no recurring catalyst (e.g., OPEC meeting,
    inventory print, geopolitical event) ahead. Phase 6 will check.
  - **Why did GEX collapse to -$303M on 2026-05-08 and then re-expand 80×
    by today?** This kind of regime instability suggests a single dominant
    institutional book is moving XOM dealer mechanics — phase 7
    `insights_institutional_accumulation` may identify the actor.
