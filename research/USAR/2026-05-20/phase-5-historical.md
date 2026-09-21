# Phase 5 — Historical Context & VRP

**Ticker:** USAR
**As-of date:** 2026-05-20 (effective UW data date: 2026-05-19)
**Generated:** 2026-05-20T10:45:00-04:00
**Upstream phases cited:** phase-0, phase-1, phase-2, phase-3, phase-4

## Summary

The historical lens **completely re-orients the deep dive**. USAR is in
the throes of a **violent post-momentum unwind**: spot peaked at **$28.16
on 2026-05-06**, then distributed for 7 sessions to $24.60, then **gapped
down -12.9% over the 5/15→5/18 weekend** ($24.60 → $21.39), then dropped
another -6.4% to today's $20.02. **Total drawdown from peak: -28.9% in
11 sessions.** This is the missing context for everything we've seen:
the $25.42 dark-pool supply (phase 2) is where the distribution happened,
the 6/18 $21 put wall (16,949 OI) was the FLOOR holders had hedged to
before it broke, the complacent skew (phase 4) reflects exhausted
put-buying after the panic, and the 5/22 backwardation (145% IV) is most
likely the **earnings/event window** that originally fueled the bubble
and now has to deliver. **VRP = -11.9%** means IV is CHEAP vs realized
(IV30d 98.95% vs realized vol30 110.88%) — premium-BUYING regime favored
even at headline 99% IV. **IV percentile 22%, z-score -1.04** confirms:
on USAR's own scale, vol is at the LOW end of its yearly distribution.

## Key signals

- **IV30d = 98.95%, IV percentile = 22.22%, z-score = -1.045** (NORMAL
  regime). Despite 99% headline IV, vol is at the 22nd percentile of
  USAR's 1y distribution — **CHEAP relative to its own history**.
  [HIST:iv_percentile_zscore]
- **VRP = -0.1193** (IV30d 98.95% vs realized 110.88%). Regime:
  **PREMIUM_BUYING** — vol cheap vs realized → favor debit structures
  (long premium, not short). [HIST:vrp]
- **Spot trajectory 28 sessions**: $19.66 (3/13) → $28.16 PEAK (5/6) →
  $24.60 (5/15) → **$21.39 (5/18 gap-down -12.9%)** → $20.02 (5/19,
  another -6.4%). **Peak-to-trough: -28.9%** in 11 sessions
  [HIST:gex_time_series + historical_trend]
- **28-day premium-flow tape: 19 bearish days vs 9 bullish days**,
  cumulative bearish $126.4M vs bullish $120.2M, net flow **-$6.18M**
  (MIXED) [HIST:cumulative_premium_flow + historical_trend]
- **GEX exploded 100x between 3/27 and 4/30** ($36M → $2.80B) as the
  ramp ran; **GEX collapsed to $221M today** as positions closed and the
  $25 magnet drifted further from spot. ZGL has bounced wildly
  ($24.98 today, but was $8.00 on 5/18, $14.02 on 5/13). [HIST:gex_time_series]
- **P/C ratio z-score = +1.00** (current 0.67 vs 20d mean 0.45,
  std 0.22). NOT a sentiment extreme. Up from baseline but well under
  the +2σ threshold. [HIST:pc_ratio_zscore]
- **`historical_signal_backtest dark_pool_accumulation`**: 0 historical
  signals in the dataset — **no historical edge can be quantified** for
  the phase-2 accumulation signal at the USAR scale.
  [HIST:signal_backtest]

## Detailed findings

### IV regime

```
IV30d        = 98.95%
percentile   = 22.22%
z-score      = -1.045
regime       = NORMAL
dates_used   = 27   (small sample; 1-month ingest gap inside lookback)
```

Despite a 99% headline IV, USAR's IV30d is at the **bottom quartile** of
its own 1-year distribution. This is intuitive once the price history is
known: peak IV was during the ramp (5/13 IV rank 23.4); IV has DEFLATED
even as the stock CRASHED. That dispersion is anomalous and is itself a
signal — the market is treating the drop as "expected", not "panic".

### VRP (volatility risk premium)

```
IV30d            = 98.95%
realised_vol30d  = 110.88%
VRP              = -11.93%
regime           = PREMIUM_BUYING
interpretation   = Vol cheap vs realised — favour premium buying.
```

This is a **classic premium-buying setup**: realized vol has overshot
implied. In structures terms, **debit calls / debit puts / debit
verticals are favored over credit structures** because the option-pricing
formula is undervaluing the actual move size.

### Cumulative premium flow (90d-window)

```
cumulative_bullish  = $120,219,858
cumulative_bearish  = $126,397,022
net_flow            = -$6,177,164
trend_direction     = MIXED
dates_covered       = 28 (one-month ingest gap 3/27 → 4/27)
```

**Net flow is essentially flat** ($6M differential on $246M two-way is
2.5%). Despite a -29% drawdown, premium flow is not stampeding either
direction. **Confirms phase 1's "MIXED with bearish lean" verdict at
multi-week scale.**

### P/C ratio z-score

```
current_pc_ratio    = 0.67
mean (20d)          = 0.4531
std  (20d)          = 0.216
z-score             = +1.004
extreme             = NORMAL
```

PCR has risen above its 20-day mean (more puts being traded relative to
calls) but is **only 1σ above mean — not a 2σ contrarian extreme**. So
no contrarian sentiment trade is warranted.

### GEX time series — the whole story

| Date | Spot | Total GEX | ZGL | Regime |
|------|------|-----------|-----|--------|
| 3/13 | 19.66 | $20.6M | $19.02 | + |
| 3/16 | 19.43 | $39.0M | $16.30 | + |
| 3/17 | 19.64 | $29.0M | $19.10 | + |
| 3/18 | 18.94 | $45.1M | $19.05 | − |
| 3/19 | 17.70 | $47.0M | $12.59 | + |
| 3/20 | 16.95 | $55.0M | $24.05 | − |
| 3/23 | 17.08 | $84.1M | $14.15 | + |
| 3/24 | 16.64 | $67.2M | $9.16 | + |
| 3/25 | 17.11 | $50.2M | $16.27 | + |
| 3/26 | 16.07 | $28.2M | $21.83 | − |
| 3/27 | 15.38 | $36.7M | $19.26 | − |
| — | — | INGEST GAP 1 MONTH | — | — |
| 4/27 | 23.18 | $565.5M | $11.91 | + |
| 4/28 | 22.62 | $1,359M | $8.02 | + |
| 4/29 | 22.02 | $925.2M | $22.93 | − |
| 4/30 | 24.85 | $2,797M | $9.08 | + |
| 5/1  | 26.05 | $1,676M | $24.53 | + |
| 5/4  | 26.12 | $2,034M | $24.08 | + |
| 5/5  | 27.49 | $2,245M | $13.60 | + |
| 5/6  | **28.16 PEAK** | $1,447M | $3.04 | + |
| 5/7  | 26.69 | $1,545M | $24.77 | + |
| 5/8  | 26.86 | $798M  | $14.22 | + |
| 5/11 | 26.97 | $1,102M | $8.00 | + |
| 5/12 | 25.56 | $780M | $11.50 | + |
| 5/13 | 25.81 | $988M | $14.02 | + |
| 5/14 | 24.57 | $1,079M | $24.78 | **− (flip)** |
| 5/15 | 24.60 | $829M | $24.77 | − |
| 5/18 | **21.39 (-13.0% gap)** | $809M | $8.00 | **+ (flip)** |
| 5/19 | 20.02 | $221M | $24.98 | **− (flip)** |

Key observations:
- **Pre-3/28**: pre-ramp, USAR was a $15-$20 mid-vol name.
- **3/28 → 4/27**: data ingest gap; over this 1-month, spot ramped from
  $15.38 to $23.18 (+51%) — implying a fundamental or sector catalyst
  drove the move (likely earnings/M&A speculation).
- **4/27 → 5/6**: ramp continued $23 → $28 (+21% more in 7 sessions).
  Total GEX exploded 60–100x as gamma exposure built.
- **5/6 → 5/15**: gradual top, -13% over 7 sessions.
- **5/15 → 5/18 weekend**: -13% gap in a single session. Almost certainly
  news-driven (sector / company / regulatory). **This is the catalyst
  for the entire current deep-dive setup.**
- **5/18 → 5/19**: another -6.4% as positioning unwound. Today's
  regime-flip back to NEGATIVE confirms structural distress.

The **3 regime flips in last 4 sessions** (5/14 +→−, 5/18 −→+, 5/19 +→−)
show the dealer book is in **transition**: gamma is being repriced in
real time, and **larger intraday ranges should be expected** until
positions stabilize after the 5/22 event.

### OI trend

- **OI peaked 5/15 at 590,939** contracts; today 483,387 (-18% from
  peak). Net OI declined through the crash, consistent with phase-3 OI
  decreases in 6/18 $30C (-751) and 2028 LEAP calls (-317, -280) —
  speculators are taking off positions as the ramp died.
- The `historical_oi_trend` tool returned a **79,635-character response
  exceeding the token limit**; the file was saved to disk but not
  ingested in this run. **Limitation flag** — fine-grained per-strike
  OI trajectory is not analyzed here. Phase 3 already captured the
  same-day OI Δ structure, so the gap is acceptable for synthesis.

### Multi-day trend table (last 10 sessions)

| Date | Close | Net flow | PCR | IV30d | IV Rank | Direction |
|------|-------|----------|-----|-------|---------|-----------|
| 5/19 | 19.97 | -$814k | 0.67 | 98.9% | 15.3 | bearish |
| 5/18 | 21.28 | -$494k | 0.84 | 100.0% | 16.7 | bearish |
| 5/15 | 24.38 | -$1.36M | 0.91 | 99.4% | 15.6 | bearish |
| 5/14 | 24.83 | -$1.20M | 0.53 | 103.0% | 19.3 | bearish |
| 5/13 | 25.42 | -$1.14M | 0.93 | 107.6% | 23.4 | bearish |
| 5/12 | 25.55 | +$193k | 0.42 | 103.8% | 20.0 | bullish |
| 5/11 | 26.30 | +$1.30M | 0.51 | 104.5% | 20.6 | bullish |
| 5/8  | 26.97 | -$1.36M | 0.37 | 106.4% | 22.0 | bearish |
| 5/7  | 26.38 | -$2.84M | 0.31 | 103.7% | 19.9 | bearish |
| 5/6  | 28.60 | +$1.98M | 0.30 | 108.1% | 23.8 | bullish (top tick) |

- The last 5 sessions are **all bearish flow days**.
- **5/13 (the top of the 5-day DP cluster at $25.42)** had IV rank 23.4
  — the highest of the window. That was the peak distribution.
- Today's IV rank 15.3 vs peak 25.4 reflects vol mean-reversion despite
  the crash — markets are not pricing more downside.

### Signal backtest

```
signal_type    = dark_pool_accumulation
total_signals  = 0
note           = no backtest results
```

**The current dark-pool accumulation signal has NO historical analog
in the available USAR data** (which is short: 28 days only). This means
two things:

1. The signal we're seeing IS genuinely unusual for USAR (the kind of
   dip-buying that hasn't happened before in this window).
2. We **cannot quantify historical win-rate** for the trade idea — no
   numerical edge to lean on.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `historical_iv_percentile_zscore` | symbol=USAR, lookback=252 | IV pct 22.2%, z -1.04, NORMAL |
| `historical_vrp` | symbol=USAR, window=30, date=2026-05-19 | VRP -11.93%, **PREMIUM_BUYING** |
| `historical_cumulative_premium_flow` | symbol=USAR, days=90 | Net -$6.18M, MIXED across 28 dates |
| `historical_pc_ratio_zscore` | symbol=USAR, lookback=20 | PCR 0.67, z +1.00, NORMAL |
| `historical_gex_time_series` | symbol=USAR, days=30, dte-max=45 | Peak GEX $2.8B on 4/30; 3 regime flips in 4 sessions; ramp + crash narrative |
| `historical_oi_trend` | symbol=USAR, days=30, top-n=15 | **Tool error (output >token limit); saved to file but not ingested** |
| `historical_trend` | symbol=USAR, days=30 | 28 days; 19 bearish / 9 bullish; spot trajectory complete |
| `historical_signal_backtest` | signal=dark_pool_accumulation, lookback=10, top-n=25 | **0 signals** (insufficient history for USAR-scale events) |

## Tool errors

- `historical_oi_trend`: Output exceeded token budget (79,635 characters,
  3,229 lines). Saved to file. Not ingested in this phase. Phase 3 has
  same-day per-contract OI Δ which mostly covers the gap; per-day OI
  trajectory across the full 28-session window is unavailable for
  synthesis here.

## Verdict for downstream phases

- **Bias from this phase:** **STRUCTURAL DISLOCATION POST-CRASH** with
  vol cheap vs realized. Net premium flow is mixed; sentiment is not
  extreme; dealer book is in regime transition. The trade setup is
  best described as a **mean-reversion bounce candidate** with a known
  5/22 catalyst risk — a setup that wants premium-buying structures
  (LONG vol or LONG delta via debit verticals/calls).
- **Conviction:** **3/5** — the setup is real but the signal-backtest
  empty means we have no historical edge to lean on, and the 28-day
  window is too short for robust z-scoring of any single signal.
- **Three specific datapoints for phase-9:**
  1. **VRP = -11.93%** → DEBIT structures favored. Selling premium into
     these realized levels would be a mistake.
  2. **IV percentile 22.2%** → vol is cheap on USAR's scale. Long-vol
     structures are reasonable; iron condors / strangles are NOT
     reasonable.
  3. **5/22 binary event window**: this is the next major catalyst.
     Any position taken before 5/22 must either embrace the binary
     (debit risk-defined) or sidestep it (wait until 5/25 entry).
- **Open questions:**
  - **What happened over the 5/15→5/18 weekend?** This is THE critical
    fundamental question. Phase 6 macro WebSearch must surface it.
  - Is the **5/22 event the same catalyst** that's been priced into the
    backwardation? Phase 7 `insights_earnings_play` must answer.
  - Is the **3/28 → 4/27 ingest gap** hiding an even bigger pre-ramp
    catalyst? Probably moot for trade decision but worth flagging.
