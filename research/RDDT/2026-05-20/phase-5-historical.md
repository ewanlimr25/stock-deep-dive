# Phase 5 — Historical Context & VRP

**Ticker:** RDDT
**As-of date:** 2026-05-20 (data anchor 2026-05-18, with 2026-05-19
visible in some historical feeds)
**Generated:** 2026-05-19T01:00:00-04:00
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md,
phase-3-positioning.md, phase-4-structure.md

## Summary

Historical context **materially de-rates the bullish optimism** from
phases 1–4. Three findings dominate: (1) `historical_signal_backtest`
on `bullish_flow` shows **win rate 0.0% / avg move -3.05% over the last
5 trading days** across the entire tape — bullish-flow signals have
been a contrarian indicator in this regime (MSFT, AAPL, QQQ, SMH, META,
AVGO all down). (2) RDDT's own next session (2026-05-19) closed at
**$154.91, -2.64% from 5/18 $159.11** — the bullish thesis was already
being tested while the data we anchored on was still warm. (3) RDDT
GEX regime has flipped POSITIVE↔NEGATIVE **10 times in 28 sessions**
including on 2026-05-19 (POSITIVE → NEGATIVE) — the long-gamma pin
from phase-4 has historically been transient. Offsetting positives:
**OI buildup is on a 28-session consecutive streak**, **IV is cheap
(percentile 11.1, z-score -0.92, regime LOW_IV)**, and **30D VRP is
FAIR (-2.6%, IV ≈ realized)** — premium structures are roughly
fairly-priced, neither favoring debit nor credit dominance.

## Key signals

- `historical_signal_backtest(bullish_flow, 5d)` → **win_rate 0.0%,
  avg_move -3.05%** across the most recent 7 signals (MSFT, AAPL, UPS,
  QQQ, SMH, META, AVGO); current regime is fading bullish flow
  [HIST:signal_backtest].
- **Next-day reality check**: RDDT 5/19 close $154.91 vs 5/18 close
  $159.11 = **-2.64% one-day move**; both `historical_trend` and
  `historical_gex_time_series` confirm this drawdown
  [HIST:historical_trend, HIST:historical_gex_time_series].
- **IV percentile 11.1 (1-year), z-score -0.92, regime LOW_IV** —
  options are cheap relative to RDDT's own history; favors debit
  structures if directional view is strong [HIST:iv_percentile_zscore].
- **VRP -2.57% (FAIR)**: IV30 64.94% vs realized 30D 67.51% — no
  premium-selling edge; vol is realizing roughly what's being implied
  [HIST:vrp].
- **GEX regime flipped 10× in 28 sessions** including on the day after
  our anchor (5/19 POSITIVE → NEGATIVE at ZGL 158.21) — the pin
  structure from phase-4 is structurally unstable
  [HIST:gex_time_series].

## Detailed findings

### IV regime

| Metric | Value | Read |
|--------|-------|------|
| current_iv30d | 61.77% | |
| iv_percentile (252d) | **11.11** | 11th percentile → cheap |
| iv_zscore | -0.922 | nearly one stdev below mean |
| regime | **LOW_IV** | |

Read: RDDT IV is in the bottom decile of its 1-year range. Long-
premium structures (long calls, long puts, debit spreads, long
straddles) are CHEAP in relative terms. This is unusual given the
front-end 5/22 IV of 79% — the 1Y context tells us the OVERALL IV is
suppressed, with only the front weekly carrying acute event premium.

### VRP

| Metric | Value |
|--------|-------|
| iv30d | 64.94% |
| realized_vol (30d) | 67.51% |
| vrp | **-2.57%** |
| regime | **FAIR** |

Read: VRP is slightly negative — realized vol has been a touch above
implied. No structural edge for systematic premium selling. Combined
with the LOW_IV percentile read, the framework points toward
**directional long-premium** structures (debit verticals, long calls)
rather than premium-sale spreads, IF a directional thesis is confirmed.

### Cumulative premium flow (90d)

| Metric | Value |
|--------|-------|
| cumulative_bullish | $365,918,607 |
| cumulative_bearish | $360,420,816 |
| net_flow | +$5,497,791 |
| trend_direction | **MIXED** |
| sessions | 28 |

Read: over a 90-day window (gap-aware: 2026-03-13 → 2026-05-19), net
premium flow is **essentially balanced** ($5.5M long bias on $725M
gross). This is the LONG-WINDOW correction to the 5-session
`sweep_persistence` headline ($24.91M bullish, phase-1). **The
recent burst of bullish flow is a short-window anomaly inside a
longer-window balanced regime.** Either it marks a real regime
change (bullish) or it's late-cycle euphoria into the next event
(bearish for vol-buyers).

### P/C ratio z-score

| Metric | Value |
|--------|-------|
| current_pc_ratio | 0.53 |
| mean (20d) | 0.484 |
| std | 0.183 |
| z-score | +0.251 |
| extreme | **NORMAL** |

Read: P/C ratio is mildly elevated (more puts being traded relative to
the 20d baseline) but well within normal range. Sentiment is NOT at a
contrarian extreme — this is neither a "everyone-is-bullish-fade-it"
signal nor a "max-fear-buy-it" signal.

### GEX time series (30d)

Regime flips per `historical_gex_time_series` (10 flips in 28
sessions):

| Date | Spot | From | To | ZGL | ZGL Δ |
|------|------|------|----|----|-------|
| 2026-03-18 | 143.36 | NEG | POS |  115.09 | -32.88 |
| 2026-03-19 | 137.82 | POS | NEG |  196.88 | +81.79 |
| 2026-03-20 | 140.44 | NEG | POS |   56.92 | -139.96 |
| 2026-03-24 | 136.97 | POS | NEG |  192.02 | +135.07 |
| 2026-05-01 | 164.76 | NEG | POS |  157.63 | -10.64 |
| 2026-05-07 | 162.78 | POS | NEG |  174.04 | +15.49 |
| 2026-05-13 | 152.40 | NEG | POS |   90.69 | -83.57 |
| 2026-05-14 | 154.84 | POS | NEG |  158.44 | +67.75 |
| **2026-05-18** | **158.89** | NEG | POS | **158.39** | **-0.25** |
| **2026-05-19** | **156.50** | POS | NEG | **158.21** | **-0.18** |

Read: regime stability is poor. The phase-4 long-gamma read was
**already invalidated by 2026-05-19** — spot dropped through ZGL
within one session and the regime flipped to NEGATIVE. The
mechanically-bullish $160 wall has had only **one-day duration** in
the most recent flip. Historical pattern of flips on consecutive days
(3/18-3/20, 5/13-5/14, 5/18-5/19) shows the long-gamma magnet has
been narrow and brief.

Trajectory highlights (selected):

| Date | Spot | Total GEX | ZGL | Regime |
|------|------|-----------|-----|--------|
| 2026-03-27 | 121.88 | -$1.4M | n/a | FULLY_NEGATIVE |
| 2026-04-27 | 161.14 | $55.4M | 168.6 | NEG |
| 2026-04-30 | 147.41 | $152.3M | 168.3 | NEG |
| 2026-05-01 | 164.76 | **$437.4M** | 157.6 | POS |
| 2026-05-05 | 172.84 | $343.2M | 158.6 | POS (HIGH) |
| 2026-05-15 | 157.07 | $528.5M | 158.6 | NEG |
| **2026-05-18** | **158.89** | **$1,261.2M** | **158.39** | **POS** |
| **2026-05-19** | **156.50** | $986.6M | 158.21 | NEG |

Read: total GEX hit a 30-day high on 2026-05-18 ($1.26B, +44% vs
prior-day), then immediately drained on 5/19. **The $1.26B GEX
print may itself be the catalyst-week event** — extreme dealer
positioning ahead of a known event (earnings? phase-6).

### OI trend (30d)

| Metric | Value |
|--------|-------|
| consecutive_build_days | **28** |
| 5/19 net_oi_change | +10,642 |
| 5/19 contracts_with_increases | 407 |
| 5/19 contracts_with_decreases | 131 |
| 5/19 total OI (from historical_trend) | 416,830 |

5/19 top OI adds (one day after our anchor):

| Strike / Expiry | Δ OI | Vol |
|-----------------|------|-----|
| 5/22 170C | +739 | 2,410 |
| 6/18 140P | +643 |   993 |
| 5/22 165C | +539 | 1,457 |
| 5/29 160C | +468 |   571 |
| 5/22 175C | +400 |   600 |
| 6/18 200C | +347 |   564 |
| 5/22 180C | +306 |   619 |
| 5/22 187.5C | +291 |   301 |
| 8/21 90P | +270 |   334 |

Read: **OI is being built UP THE CALL CURVE** even as spot fell
-2.6% on 5/19 — the call ladder now extends 5/22 165/170/175/180/187.5,
deeper than what we saw on 5/18. Speculators are buying upside chase
into weakness. Simultaneously the **6/18 140P added +643 OI** (down
strike, down expiry) — pure downside hedge or fresh bearish bet.
Two-sided positioning expansion is consistent with **straddle/strangle
event positioning** rather than directional conviction.

### Multi-day trend (selected, 28 sessions)

| Date | Close | Δ | Bull$ | Bear$ | Net | PCR | IV30 | IV Rank | Flow |
|------|-------|---|-------|-------|-----|-----|------|---------|------|
| 5/19 | 154.91 | -2.6% | $4.0M | $5.6M | -$1.6M | 0.53 | 61.8% | 18.7 | bearish |
| **5/18** | **159.11** | +0.5% | $7.8M | $6.9M | +$0.9M | 0.53 | 64.9% | 24.2 | bullish |
| 5/15 | 158.31 | +1.3% | $7.9M | $7.1M | +$0.7M | 0.43 | 62.3% | 19.1 | bullish |
| 5/14 | 156.31 | +1.4% | $10.2M | $12.7M | -$2.5M | 0.40 | 62.1% | 17.8 | bearish |
| 5/13 | 154.12 | +1.2% | $6.6M | $8.8M | -$2.2M | 0.50 | 62.3% | 18.3 | bearish |
| 5/12 | 152.35 | -4.5% | $5.5M | $9.4M | -$3.8M | 0.38 | 61.1% | 15.6 | bearish |
| 5/11 | 159.51 | +1.3% | $8.1M | $9.3M | -$1.2M | 0.35 | 61.9% | 17.4 | bearish |
| 5/08 | 155.70 | -5.0% | $10.1M | $15.4M | -$5.3M | 0.37 | 59.8% | 13.7 | bearish |
| 5/07 | 163.95 | -1.6% | $8.2M | $10.6M | -$2.4M | 0.50 | 58.2% | 9.1 | bearish |
| 5/06 | 166.56 | -3.2% | $10.4M | $13.3M | -$2.9M | 0.37 | 63.2% | 20.4 | bearish |
| 5/05 | 171.97 | +1.7% | $21.3M | $16.9M | +$4.4M | 0.16 | 67.5% | 26.5 | bullish |
| 5/04 | 169.07 | +1.6% | $23.8M | $25.6M | -$1.8M | 0.29 | 65.7% | 25.8 | bearish |
| **5/01** | **166.48** | **+13.3%** | **$60.1M** | **$41.0M** | **+$19.0M** | 0.40 | 66.2% | 26.9 | bullish |
| 4/30 | 146.96 | -0.5% | $21.5M | $23.9M | -$2.3M | 0.44 | 89.6% | 69.8 | bearish |
| 4/29 | 147.75 | -0.1% | $6.7M | $8.0M | -$1.3M | 0.50 | 84.1% | 66.8 | bearish |
| 4/28 | 147.93 | -7.7% | $9.1M | $12.9M | -$3.9M | 0.75 | 84.1% | 66.9 | bearish |
| 4/27 | 160.21 |  n/a  | $12.7M | $10.2M | +$2.5M | 0.46 | 84.1% | 66.9 | bullish |
| 3/27 | 121.84 | n/a | $14.8M | $15.9M | -$1.1M | 0.93 | 81.0% | 37.1 | bearish |
| 3/13 | 132.36 | n/a |  $6.1M |  $6.1M | $0.0M | 0.65 | 70.9% | 23.1 | bullish |

Bullish days 12 / bearish days 16 over 28 sessions — flow is
**marginally biased bearish** over the recent month despite the
phase-1 5-session persistence read.

Notable patterns:
1. The **5/01 spike day** ($146.96 → $166.48, +13.3%, $60M bullish
   premium, IV rank dropped from 70 → 27) is consistent with a
   POST-EARNINGS or POST-CATALYST move where IV crushed and bulls
   jumped in. IV rank dropped from 70 on 4/30 to 27 on 5/01 = vol
   crush. This is the most likely earnings date.
2. **4/27→4/30 stretch** had IV rank pinned 66-69 = pre-event vol
   regime; resolution on 5/1 is the event.
3. Since the 5/05 peak ($171.97), stock has been in **distribution**:
   net flow negative on 7 of last 10 sessions, IV rank decayed from 27
   to 19, close drifting from $172 → $155.
4. **5/18-5/19 was a 2-day bounce attempt** ($154-$159) that already
   failed back to $155 on 5/19.

### Signal backtest (current regime)

`bullish_flow` (5-day forward):

| Ticker | Signal Date | Price on Signal | Price after 5d | Δ% |
|--------|-------------|-----------------|----------------|----|
| MSFT | 2026-05-15 | 422.05 | 417.42 | -1.10% |
| AAPL | 2026-05-15 | 300.37 | 298.97 | -0.47% |
| UPS  | 2026-05-15 |  99.00 |  96.83 | -2.19% |
| QQQ  | 2026-05-14 | 719.79 | 701.53 | -2.54% |
| SMH  | 2026-05-14 | 578.34 | 543.96 | -5.94% |
| META | 2026-05-14 | 618.43 | 602.61 | -2.56% |
| AVGO | 2026-05-14 | 439.79 | 411.07 | **-6.53%** |
| **win_rate** | | | | **0.0%** |
| **avg_move** | | | | **-3.05%** |

Read: every single recent bullish-flow signal across the tape went
DOWN over the next 5 days. The current regime is **fading bullish
flow**. SMH -5.9%, AVGO -6.5%, QQQ -2.5% suggest a broader risk-off
in semi/AI names. RDDT's own -2.6% next-day move fits the pattern.

`dark_pool_accumulation`: no backtest results in current dataset
(empty); cannot confirm phase-2 DP accumulation has a current
historical edge.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__historical_iv_percentile_zscore` | symbol=RDDT, lookback=252 | IV %ile 11.1, z -0.92, LOW_IV |
| `mcp__uw-pp__historical_vrp` | symbol=RDDT, date=2026-05-18, realised_window=30 | VRP -2.57%, FAIR |
| `mcp__uw-pp__historical_cumulative_premium_flow` | symbol=RDDT, days=90 | net +$5.5M, MIXED |
| `mcp__uw-pp__historical_pc_ratio_zscore` | symbol=RDDT, lookback=20 | z +0.25, NORMAL |
| `mcp__uw-pp__historical_gex_time_series` | symbol=RDDT, days=30, dte_max=45 | 10 regime flips in 28d |
| `mcp__uw-pp__historical_oi_trend` | symbol=RDDT, days=30, top_n=10 | consecutive_build_days=28 |
| `mcp__uw-pp__historical_trend` | symbol=RDDT, days=30 | 12 bull / 16 bear days; latest=bearish |
| `mcp__uw-pp__historical_signal_backtest` | signal=bullish_flow, lookback=5, top_n=20 | win 0%, avg -3.05% (n=7) |
| `mcp__uw-pp__historical_signal_backtest` | signal=dark_pool_accumulation, lookback=5, top_n=20 | empty (no results) |

## Tool errors

None. (`dark_pool_accumulation` returned empty — not an error, just
no signals in the recent window matching the backtest definition.)

## Verdict for downstream phases

- **Volatility regime:** LOW_IV (11th percentile) but FAIR VRP →
  premium-buying environment overall, no clear edge for premium-selling.
  However, FRONT-WEEK 5/22 IV at 79% is rich relative to back-month
  60-65% → calendar/diagonal structures could harvest the term
  backwardation.
- **Premium environment:** mixed; long-vol structures are cheap
  outright; short-vol structures lack edge.
- **Signal-edge conviction (current regime):** **2 / 5** — the same
  bullish_flow signature that phases 1-3 fired on has had a **0%
  hit rate** over the last week. Phase-9 must size DOWN or build in
  an explicit invalidation trigger.
- **Three specific data points:**
  1. IV percentile **11.1**, IV30 **61.77%**, VRP **-2.57%** → cheap
     vol, fair pricing.
  2. `bullish_flow` 5d backtest **win 0%, avg -3.05%** (n=7) — the
     dominant signal type from phases 1-3 has been a contrarian
     indicator this week.
  3. RDDT 5/19 close $154.91 = **-2.64% next-day** vs our 5/18
     anchor; GEX regime flipped POS→NEG; long-gamma pin lasted one
     session.
- **Open questions:**
  - Phase 6 must identify the catalyst that explains the 5/01 +13.3%
    spike (likely RDDT Q1 earnings; check date) and whether the
    8/21 IV hump implies Q2 earnings on/around Aug 5 (typical RDDT
    cadence).
  - Is the 28-session OI build durable structural growth or
    speculative chase that will unwind on a single risk-off day?
  - Phase 8 contrarian-scanner agent: is the "everyone bullish" flow
    + "complacent skew" + "0% recent signal win rate" + "after-hours
    aggressive buyer" a classic late-cycle blow-off-top setup, or is
    the institutional DP accumulation the real signal and the
    bullish-flow correlation is noise?
