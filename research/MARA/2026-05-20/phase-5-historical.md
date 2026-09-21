# Phase 5 — Historical Context & VRP

**Ticker:** MARA
**As-of date:** 2026-05-19
**Generated:** 2026-05-20T00:50:00-04:00
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-4-structure.md

## Summary

MARA sits in a **LOW_IV regime** (IV30d 84.2%, **14.8th percentile** of
1y range, z-score **-1.30**) with a **+13.8% volatility risk premium**
(IV − realized = 84.2% − 70.4%) → simultaneously **cheap optionality
by historical standards** *and* a **premium-selling regime by VRP**.
This dual read favors **spread structures** (own cheap longer-dated
optionality, sell rich front-end premium). OI has been **BUILDING for
14 consecutive sessions** with a 28-day net increase of **+1.72M
contracts**. GEX regime has been **stably POSITIVE for 22 consecutive
sessions** since the 4/27 regime flip at $11.28; today's GEX of $22.6B
is near the 28-day max ($23.7B on 5/18). The stock has rallied **+67%**
from a 3/27 low of $7.89 to a 5/11 peak of $13.39, and is now consolidating
at $12.47 (**-6.9% off the high**). The 5/11 peak aligns with the
phase-2 dark-pool resistance ($13.20-$13.29), phase-3 OI wall ($13C),
and phase-4 gamma wall ($13 strike) — **three independent S/R lines
all converge at $13**, the strongest level in the entire workup.

**Caveat:** historical_signal_backtest of generic `bullish_flow`
shows a **20% win rate** with -2.62% average 10-day move over the last
10 firings — a CONTRARIAN warning that recent market-wide bullish-flow
signals have been faded. Treat single-name MARA signals on their own
merits but do not lean on broad flow direction alone.

## Key signals

- IV30d = 84.2%, **14.8th percentile / z-score -1.30** → LOW_IV regime,
  cheap optionality [HIST:historical_iv_percentile_zscore]
- VRP = +13.8% (IV 84.2% − RV30 70.4%) → PREMIUM_SELLING regime
  [HIST:historical_vrp]
- OI trend: **BUILDING 14 consecutive days**, net +1,717,409 contracts /
  28 days [HIST:historical_oi_trend]
- GEX regime: stable POSITIVE for 22 sessions since 4/27 flip; today
  $22.6B near 28d max [HIST:historical_gex_time_series]
- Stock journey: $7.89 (3/27 low) → $13.39 (5/11 high) → $12.47 today
  (consolidation, -6.9% off peak) [HIST:historical_trend]
- 90d cumulative premium: bullish $183M vs bearish $189M, net **-$5.9M
  (MIXED)** — flow has been balanced over 90d, today's net-bullish lean
  is small in context [HIST:historical_cumulative_premium_flow]
- P/C z-score 0.50 (today 0.59 vs 20d mean 0.44) → NORMAL, no sentiment
  extreme [HIST:historical_pc_ratio_zscore]
- ⚠️ **`bullish_flow` signal backtest: 20% win rate / -2.62% avg 10d move**
  over last 10 firings (sample: AMZN, AMD, RCL, MSFT, AAPL, UPS, QQQ,
  SMH, META, AVGO) → contrarian fade signal in current market environment
  [HIST:historical_signal_backtest]

## Detailed findings

### IV regime + VRP

| Metric | Value | Reading |
|--------|-------|---------|
| Current IV30d | 84.19% | absolute level high (crypto-miner baseline) |
| 1y percentile | **14.8%** | bottom 15% of 1y range |
| 1y z-score | **-1.30** | 1.3σ below 1y mean |
| Realized vol 30d | 70.4% | actual recent realized |
| **VRP** | **+13.8%** | options pricing more vol than realized |
| Regime | LOW_IV / PREMIUM_SELLING | dual: cheap absolute + still rich vs RV |

**Implication:** for a name where IV typically trades 90-110% (per the
1y trajectory implied by z-score), today's 84% is cheap. This makes
**outright option buying** historically attractive on a percentile basis.
However, on a same-day VRP basis, options are still overpricing recent
realized — so premium **sellers** also have a tailwind. The trade
structure that monetizes BOTH signals: **calendar spreads** (sell rich
short-dated, own cheap longer-dated) or **diagonals** (own IV-cheap LEAP
+ sell front-month against it).

### Cumulative premium flow (90 sessions)

| Metric | Value |
|--------|-------|
| Cumulative bullish premium | $183,211,741 |
| Cumulative bearish premium | $189,076,745 |
| Net flow | **-$5,865,004** |
| Direction | **MIXED** (≈49.2% bullish / 50.8% bearish) |
| Days covered | 28 trading days (some non-trading dates skipped) |

**Reading:** over 90 calendar days (28 trading sessions in the dataset),
MARA's net premium flow is essentially flat — bears and bulls have
matched each other almost perfectly. Today's net +$320K is noise in this
context. This argues against treating the recent sweep persistence as
unilateral bullish positioning; it's two-way fighting at the highs.

### P/C ratio z-score

| Metric | Value |
|--------|-------|
| Current P/C ratio | 0.59 |
| 20-day mean | 0.44 |
| 20-day std | 0.30 |
| Z-score | **+0.50** |
| Extreme | NORMAL |

Slightly elevated (+0.5σ) — modest put demand relative to recent norm,
but well within the normal band. No sentiment extreme to fade.

### GEX time series & regime stability

**Regime flip events (28-day window):**

| Date | Spot | From | To | ZGL after |
|------|------|------|----|-----------|
| 2026-03-18 | $9.09 | POSITIVE | NEGATIVE | $28.08 |
| 2026-03-20 | $8.73 | NEGATIVE | POSITIVE | $1.00 |
| 2026-03-23 | $8.97 | POSITIVE | NEGATIVE | $9.56 |
| 2026-03-24 | $8.42 | NEGATIVE | POSITIVE | $2.00 |
| **2026-04-27** | **$11.28** | **NEGATIVE** | **POSITIVE** | **$3.50** |
| *(stable POSITIVE for 22 sessions through 2026-05-19)* | | | | |

**Trajectory highlights (selected):**

| Date | Spot | Total GEX | ZGL | Regime |
|------|------|-----------|-----|--------|
| 2026-03-13 | $9.51 | $0.32B | $8.82 | POSITIVE |
| 2026-03-25 | $8.28 | -$0.10B | n/a | FULLY_NEGATIVE |
| 2026-04-27 | $11.28 | $1.20B | $3.50 | POSITIVE (flip) |
| 2026-04-30 | $11.94 | $9.88B | $3.94 | POSITIVE |
| 2026-05-11 | $13.54 | $7.60B | $2.01 | POSITIVE (recent high) |
| 2026-05-14 | $13.30 | $6.75B | $4.50 | POSITIVE |
| 2026-05-18 | $11.92 | **$23.71B** | $4.51 | POSITIVE (max GEX) |
| 2026-05-19 | $12.08 | $22.61B | $4.65 | POSITIVE (today) |

**Reading:**
1. **Regime is durable.** No flips in 22 sessions. To get a flip back
   to NEGATIVE, spot would need to dump to ~$4.65 (full chain) or
   ~$7.85 (0DTE bucket) — both far below current spot.
2. **GEX magnitude has doubled in 7 sessions** (~$7.6B on 5/11 → $23.7B
   on 5/18). This is dealer long-gamma BUILDING as call writers added to
   their position into OPEX week. The mechanical effect is *increasing*
   mean-reversion pressure and *suppressing* realized vol.
3. **Realized vol is decompressing.** 30d RV = 70.4% while 28-day-ago
   IV30 was ~93%. Realized has rolled down even as IV stayed high → VRP
   widened, confirming premium-selling edge.

### OI trend (28d)

| Metric | Value |
|--------|-------|
| Days analyzed | 28 |
| Consecutive build days | **14** |
| Total net OI change | **+1,717,409 contracts** |
| Overall trend | **BUILDING** |

Daily net OI changes (selected high-build days):
- 5/4: **+155,156** (Jun-18 12C, May-08 12-13.5C buildup)
- 4/27: +115,214 (May-01 12-13C buildup ahead of mid-month rally)
- 5/11: +127,992 (May-15 14.5-13-14C buildup before that OPEX)
- 5/18: +167,870 (May-22 13-14C — the walls observed today)

Pattern: **every OPEX week shows a big buildup ~4 sessions before expiry**
on the 12.5-14 calls. This is a recurring covered-call writing campaign
into upside, week after week. Today's 5/18 +168K and 5/19 +37K are
*the latest installment*; the call writer is operating systematically.

### Historical trend table (selected, 28 days)

| Date | Close | Net flow | Flow dir | IV30d | IV rank | PCR |
|------|-------|----------|----------|-------|---------|-----|
| 2026-05-19 (today) | 12.47 | +$320K | bullish | 84.2% | 35.9 | 0.59 |
| 2026-05-18 | 12.18 | -$388K | bearish | 86.1% | 37.2 | 0.51 |
| 2026-05-15 | 12.435 | +$416K | bullish | 84.7% | 32.3 | 0.17 |
| 2026-05-14 | 13.29 | +$629K | bullish | 83.9% | 34.2 | 0.36 |
| 2026-05-13 | 12.75 | -$505K | bearish | 83.9% | 34.2 | 0.48 |
| 2026-05-12 | 12.72 | -$1,061K | bearish | 82.2% | 31.9 | 0.31 |
| 2026-05-11 | **13.39** (recent high) | +$2,348K | bullish | 91.6% | 44.7 | 0.39 |
| 2026-05-08 | 12.96 | +$481K | bullish | 87.7% | 36.8 | 0.17 |
| 2026-05-07 | 12.70 | -$436K | bearish | 87.7% | 39.4 | 0.47 |
| 2026-05-06 | 13.03 | +$294K | bullish | 88.6% | 40.7 | 0.32 |
| 2026-05-05 | 12.145 | -$77K | bearish | 90.6% | 40.7 | 0.24 |
| 2026-05-04 | 11.83 | +$799K | bullish | 88.5% | 40.5 | 0.33 |
| 2026-05-01 | 11.46 | -$1,674K | bearish | 84.0% | 34.4 | 0.21 |
| 2026-04-30 | 11.99 | +$791K | bullish | 87.2% | 40.6 | 0.47 |
| 2026-04-29 | 10.72 | -$1,507K | bearish | 88.0% | 39.8 | 0.19 |
| 2026-04-28 | 11.02 | +$1,035K | bullish | 86.6% | 37.9 | 0.26 |
| 2026-04-27 | 11.18 | -$268K | bearish | 89.1% | 41.3 | 0.53 |
| ... | ... | ... | ... | ... | ... | ... |
| 2026-03-27 | **8.02** (recent low) | -$2,128K | bearish | 95.2% | 49.6 | 1.00 |
| 2026-03-13 | 9.32 | -$658K | bearish | 93.3% | 47.0 | 0.51 |

**Reading:**
- Stock journey: $9.32 (3/13) → $8.02 (3/27 capitulation low, PCR 1.00,
  IV rank 49.6) → $11.18 (4/27 regime flip) → $13.39 (5/11 peak) →
  $12.47 (today)
- **+67% rally from 3/27 low to 5/11 high** in 31 trading sessions
- **-6.9% consolidation from peak** to today
- 12 bullish days vs 16 bearish days, latest is bullish
- IV rank has DECLINED from 49.6 (3/27) → 35.9 (today) as price has
  consolidated — confirms IV crush hypothesis
- IV rank 31.8 → 35.9 today: still in the low end of recent range

### Signal backtest (`bullish_flow`, 10d lookback)

| Metric | Value |
|--------|-------|
| Signal type | bullish_flow |
| Lookback days | 10 |
| Total signals (last firings) | 10 |
| **Win rate** | **20.0%** |
| Avg 10d move | **-2.62%** |

Recent firings table:

| Date | Ticker | Direction | 10d move |
|------|--------|-----------|----------|
| 2026-05-18 | AMZN | down | -1.88% |
| 2026-05-18 | AMD | up | +1.96% |
| 2026-05-18 | RCL | down | -6.23% |
| 2026-05-15 | MSFT | down | -2.37% |
| 2026-05-15 | AAPL | up | +0.09% |
| 2026-05-15 | UPS | down | -2.71% |
| 2026-05-14 | QQQ | down | -2.08% |
| 2026-05-14 | SMH | down | -4.34% |
| 2026-05-14 | META | down | -3.04% |
| 2026-05-14 | AVGO | down | -5.55% |

**Reading:** Across the broad market in mid-May 2026, generic
"bullish_flow" alerts have been faded 80% of the time, with the median
firing followed by a -2.6% pullback over 10 days. This is a *market-wide*
contrarian signal — large-cap names with bullish flow have rolled over.
**This is the single biggest yellow flag in the entire workup so far.**
The MARA-specific tape may diverge, but the macro tape is fading
bullish-flow setups. Phase 6 (macro regime) must check whether broad-market
risk is rolling.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__historical_iv_percentile_zscore` | `{symbol: MARA, lookback_days: 252}` | IV 84%, 14.8%ile, z=-1.30, LOW_IV |
| `mcp__uw-pp__historical_vrp` | `{symbol: MARA, date: 2026-05-19, realised_window_days: 30}` | VRP +13.8%, PREMIUM_SELLING |
| `mcp__uw-pp__historical_cumulative_premium_flow` | `{symbol: MARA, days: 90}` | Net -$5.9M, MIXED |
| `mcp__uw-pp__historical_pc_ratio_zscore` | `{symbol: MARA, lookback_days: 20}` | z=+0.50, NORMAL |
| `mcp__uw-pp__historical_gex_time_series` | `{symbol: MARA, days: 28, dte_max: 45}` | 22-session POSITIVE streak; GEX 22.6B near max |
| `mcp__uw-pp__historical_oi_trend` | `{symbol: MARA, days: 28, top_n: 15}` | 14d build streak, +1.72M contracts net |
| `mcp__uw-pp__historical_trend` | `{symbol: MARA, days: 28}` | 12 bullish vs 16 bearish days; rally +67% from 3/27 low |
| `mcp__uw-pp__historical_signal_backtest` | `{signal_type: bullish_flow, lookback_days: 10, top_n: 20}` | **20% win rate, -2.62% avg 10d** |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** **structurally constructive (long-gamma,
  building OI, low IV) but tactically cautious** (signal-backtest fade
  warning, balanced 90d flow, +67% prior rally pending mean-reversion)
- **Conviction on historical edge:** 3/5. The mechanics are favorable
  for spread structures, but recent market-wide bullish-flow signals
  have been faded with high reliability.
- **Three specific datapoints for phase 9:**
  1. IV 14.8th percentile + VRP +13.8% → favor **calendar/diagonal
     spreads** (sell rich front, own cheap back)
  2. GEX has been POSITIVE for 22 sessions; spot $12.08 vs ZGL $4.65 →
     huge buffer before regime flip — only a >35% selloff threatens
     long-gamma mean-reversion
  3. **+67% prior rally + -6.9% consolidation** = textbook digestion phase;
     stat-significant trend with breathing room, neither blown out nor
     broken
- **Open questions:**
  - Why is generic `bullish_flow` failing 80% of the time in mid-May
    2026? Phase 6 must check: SPY/QQQ regime, VIX trend, sector
    rotation, BTC trend (relevant for crypto-miner)
  - Is the 90d balanced premium flow consistent with a "trapped" stock
    where bulls and bears fight the $13 wall? If yes, the trade is the
    *range itself*, not direction.
  - Does today's OI build (especially the 13C/14C call writing) suggest
    the writer is the same desk that put on this pattern weekly for the
    last 5 OPEX weeks? Phase 7 should test sweep persistence + writer
    consistency.
