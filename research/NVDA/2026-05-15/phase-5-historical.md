# Phase 5 — Historical Context & VRP

**Ticker:** NVDA
**As-of date:** 2026-05-15
**Spot reference:** $227.54 (per `historical_gex_time_series` trajectory tail)
**Upstream phases cited:** phase-1-flow.md, phase-4-structure.md
**Generated:** 2026-05-17T17:13Z

## Summary

The historical context **PARTIALLY UNDERMINES** the bullish stack from
phases 1–4. Three findings stand out:

1. **IV is at the 100th percentile** of the trailing 252-day window
   `[HIST:iv_percentile_zscore]` — z-score 1.65, regime HIGH_IV. Premium is
   expensive in absolute terms.
2. **VRP is +0.11** (IV30d 0.49 vs realized 0.38) — clearly a
   **PREMIUM-SELLING regime** `[HIST:vrp]`. Long-premium directional bets
   are paying carry.
3. **90-day cumulative premium flow is MIXED**: bullish $17.21B vs bearish
   $17.01B, net +$200M `[HIST:cumulative_premium_flow]`. The LEAP signature
   in phase-1 does NOT show up as a 90d structural accumulation — the
   long-term flow is essentially flat. NVDA has rallied 36% (March $167 →
   May $227) on roughly balanced options-premium support.

The dealer regime has been **POSITIVE GAMMA for all 26 sessions** of the
visible window — no regime flips, no short-gamma chaos. Total GEX has
**exploded from $12.6B (March) to $1.10T (today)** — dealers are now
*massively* long gamma, which mechanically suppresses realized vol. The IV
rank has climbed from 21 → 77 over the same window, suggesting market is
pricing for an upcoming event (consistent with phase-4 backwardation
pointing to 05-22 earnings).

**The contrarian flag:** `historical_signal_backtest` for `bullish_flow`
over the most recent 5-day forward window shows a **20% win rate** with
average move **-1.07%** `[HIST:signal_backtest]`. NVDA itself appears
twice — 05-13 bullish flow → -0.23%, 05-12 bullish flow → +2.06% — a wash.
Recent bullish-flow signals have NOT followed through. This argues for
defined-risk structures and sized conservatively.

## Key signals

- **IV percentile 100, z-score 1.654, HIGH_IV regime** `[HIST:iv_percentile_zscore]`
- **VRP +0.1086, PREMIUM_SELLING regime** `[HIST:vrp]`
- **90d cumulative net flow +$200M / ~0% bias, MIXED** `[HIST:cumulative_premium_flow]`
- **P/C z-score -0.307, NORMAL** (not extreme) `[HIST:pc_ratio_zscore]`
- **26 consecutive POSITIVE-gamma sessions, no regime flips** `[HIST:gex_time_series]`
- **bullish_flow win_rate 20% over last 5 trading days, avg -1.07%** `[HIST:signal_backtest]`

## Detailed findings

### IV regime

| Field | Value |
|-------|-------|
| Current IV30d | 0.4895 (49.0%) |
| IV percentile (252d) | **100** |
| IV z-score | **+1.654** |
| Regime | HIGH_IV |
| Dates used | 25 |

The data window is gappy (26 dates across March → May because of UW data
backfill gaps), so "100th percentile" should be read as "highest in the
visible record" — still a meaningful signal: NVDA IV has not been higher
in any observed session. This is consistent with phase-4 backwardation
pointing to the 05-22 event.

### Volatility risk premium

| Field | Value |
|-------|-------|
| IV30d | 0.4895 |
| Realized vol (30d) | 0.3809 |
| VRP | **+0.1086** |
| Regime | **PREMIUM_SELLING** |

Long-premium directional bets cost ~11 vol points of carry vs realized.
This is a meaningful tilt toward **credit / spread / fly structures** over
naked long calls or puts. Important constraint for phase-9.

### Cumulative premium flow (90d)

| Field | Value |
|-------|-------|
| Bullish premium | $17,208,331,452 |
| Bearish premium | $17,007,882,745 |
| **Net** | **+$200,448,707 (+1.2% bullish skew)** |
| Trend direction | **MIXED** |
| Dates covered | 26 (gappy) |

**Critical:** despite phase-1's bullish flow snapshot and the visible LEAP
buying today, the 90-day flow is FLAT. The 36% spot rally has occurred
without a persistent options-premium accumulation signature. This argues
against high-conviction long-LEAP sizing and supports a 0.55–0.65
conviction bin in phase-9.

### P/C ratio z-score

| Field | Value |
|-------|-------|
| Current P/C | 0.46 (call-heavy) |
| Mean (20d) | 0.5214 |
| Std | 0.2001 |
| Z-score | **-0.307** |
| Regime | **NORMAL** |

Not at an extreme. Sentiment is mildly call-skewed but within statistical
noise. No contrarian signal from this metric.

### GEX time series (26-day trajectory)

| Date | Spot | Total GEX | ZGL | Regime |
|------|------|-----------|-----|--------|
| 2026-03-13 | $181.72 | $12.6B | $29.01 | POS |
| 2026-03-27 | $168.61 | $11.0B | $33.56 | POS |
| 2026-04-27 | $212.55 | $186.3B | $74.40 | POS |
| 2026-05-01 | $199.53 | $157.9B | $69.56 | POS |
| 2026-05-08 | $215.70 | $359.1B | $10.57 | POS |
| 2026-05-11 | $219.75 | $517.6B | $74.62 | POS |
| 2026-05-13 | $226.12 | $662.2B | $99.94 | POS |
| 2026-05-14 | **$234.45** | $940.0B | $109.93 | POS |
| **2026-05-15** | **$227.54** | **$1.10T** | $72.29 | POS |

Observations:
- **No regime flips** across 26 sessions — `regime_flip_dates: null`.
- Total GEX has grown **87×** from March to today.
- ZGL has climbed and now sits at $72.29 — still vastly below spot, so
  the long-gamma regime has a deep moat.
- Yesterday's intraday high of **$234.45** is a near-term resistance
  reference for phase-9 — it tagged the phase-2 $235.74 institutional level
  before pulling back to $227.54.

### OI trend (30d)

`historical_oi_trend` confirms **consecutive_build_days = 26** (no decline
days in the window), with today's net OI change at **+562,769**. This is a
relentless build, supportive of the bullish stack but consistent with
straight pre-earnings positioning rather than directional conviction.

### Multi-day flow direction (last 10 sessions)

| Date | Close | Flow direction | Net flow $ | IV30d | IV rank |
|------|-------|---------------|------------|-------|---------|
| 05-15 | $225.49 | bearish | -$42.6M | 49.0% | 76.7 |
| 05-14 | **$235.74** | bullish | +$34.9M | 48.9% | 76.6 |
| 05-13 | $225.83 | bullish | +$71.5M | 48.3% | 74.2 |
| 05-12 | $220.78 | bullish | +$41.9M | 45.8% | 64.2 |
| 05-11 | $219.44 | bullish | **+$282.3M** | 45.5% | 62.9 |
| 05-08 | $215.21 | bearish | -$17.9M | 45.2% | 63.9 |
| 05-07 | $211.50 | bullish | +$86.3M | 45.9% | 64.5 |
| 05-06 | $207.83 | bullish | +$112.1M | 45.7% | 61.8 |
| 05-05 | $196.49 | bullish | +$20.2M | 43.8% | 54.3 |
| 05-04 | $198.48 | bearish | -$65.8M | 42.7% | 49.8 |

Net over the last 10 sessions: ~+$520M bullish premium. **Most of the
recent rally was supported by real bullish flow**, peaking on 05-11 at
+$282M. Today's session was bearish flow (-$42.6M) AFTER a strong 05-14
($235.74 high). Reading: distribution day at the resistance level (matches
phase-2 mega-tier slight sell skew).

### Signal backtest — `bullish_flow` (5d forward)

| Field | Value |
|-------|-------|
| Total signals | 10 |
| Win rate | **20.0%** |
| Average move | **-1.07%** |
| Signal type | bullish_flow |
| Lookback | 5 trading days |

NVDA-specific results in the window:
- 2026-05-13 NVDA bullish_flow signal → -0.23% over 5d (LOSS)
- 2026-05-12 NVDA bullish_flow signal → +2.06% over 5d (WIN)

The overall 20% win rate (mostly Mag7 names: TSLA -5.2%, GOOGL -1.5%,
META -0.4%, QQQ -0.8%, QCOM -4.2%) is a **strong contrarian read** on the
current week's bullish-flow setups. Phase-9 should de-rate conviction by
one bin because of this.

## Tool calls (audit trail)

| Tool | Args | Result |
|------|------|--------|
| `mcp__uw-pp__historical_iv_percentile_zscore` | `symbol=NVDA, lookback-days=252` | percentile 100, z 1.65 |
| `mcp__uw-pp__historical_vrp` | `symbol=NVDA, date=2026-05-15` | VRP +0.1086, PREMIUM_SELLING |
| `mcp__uw-pp__historical_cumulative_premium_flow` | `symbol=NVDA, days=90` | net +$200M, MIXED |
| `mcp__uw-pp__historical_pc_ratio_zscore` | `symbol=NVDA, lookback-days=20` | z -0.307, NORMAL |
| `mcp__uw-pp__historical_gex_time_series` | `symbol=NVDA, days=30, dte-max=45` | 26 days, all POS, no flips |
| `mcp__uw-pp__historical_oi_trend` | `symbol=NVDA, days=30, top-n=10` | 26 consecutive build days, +562k today |
| `mcp__uw-pp__historical_trend` | `symbol=NVDA, days=30` | 16 bull / 10 bear days; today bearish |
| `mcp__uw-pp__historical_signal_backtest` | `signal-type=bullish_flow, lookback-days=5, top-n=20` | win_rate 20%, avg -1.07% |

## Tool errors

None.

## Verdict for downstream phases

- **Volatility regime:** **IV RICH** (100th %ile) — favor credit/spread
  structures, not naked long premium.
- **Premium-buying vs selling:** **PREMIUM_SELLING** (VRP +0.11) — same
  conclusion.
- **Conviction that today's signal is HISTORICALLY edge-positive:** **2/5**
  — bullish_flow win rate at 20% over the last 5d forward window is a
  contrarian flag.
- **Three specific datapoints:**
  1. IV percentile **100** + z-score **+1.65** → premium is expensive.
  2. VRP **+0.1086** → PREMIUM_SELLING regime.
  3. 90-day cumulative net flow **+$200M (flat)** vs +36% spot rally →
     positioning has NOT confirmed the price rally; sized down accordingly.
- **Open questions:**
  - Does phase-7 `insights_earnings_play` confirm the 05-22 NVDA earnings?
  - Does phase-7 `insights_price_vs_flow` flag a divergence (price up,
     flow flat) — that would corroborate the contrarian read.
  - Should phase-9 prefer a **call debit spread** (sells back-month vol to
     pay for front-month directional bet) rather than naked calls, given
     the HIGH_IV regime + low recent signal win rate?
