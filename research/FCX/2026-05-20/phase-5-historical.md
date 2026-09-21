# Phase 5 — Historical Context & VRP

**Ticker:** FCX
**As-of date:** 2026-05-20 (effective data 2026-05-19)
**Generated:** 2026-05-20T20:25:00-04:00
**Upstream phases cited:** `phase-1-flow.md`, `phase-2-dark-pool.md`,
`phase-3-positioning.md`, `phase-4-structure.md`

## Summary

The historical lens **reframes the entire setup**. FCX rallied from $55.57 on
May-04 to **$67.16 on May-13** — then sold off **−12.6% in four sessions** to
$58.71 at today's close [HIST:historical_trend]. The dark-pool concentration
at $65.94–$68.50 [DP:price_levels@phase-2], the massive 65C/70C July OI
that just got unwound [OI:decrease_with_volume@phase-3], and the "5 of 5
sessions in top-sweep" persistence [FLOW:sweep_persistence@phase-1] all
trace to the rally-and-pullback that just happened. The current $58.71
print is at the FLOOR of a 4-session correction inside an existing up-trend
from May-04 lows, not the start of a fresh trend.

The vol regime tells the same story from the IV side. **IV30d is 49.91% —
40.7th percentile of FCX's own 1y range (z-score −0.44, regime "NORMAL")**
[HIST:iv_percentile_zscore]. What felt like elevated IV in absolute terms
(phase-4) is actually **CHEAP for FCX**. The Volatility Risk Premium is
**−7.4 pts** (IV 49.9% vs realised 57.3%) [HIST:vrp] — realised has been
outrunning implied for 30 sessions. The tool labels this **PREMIUM_BUYING**
regime: **favour debit structures (long premium) over credit structures**.
That is unambiguous guidance for phase-9's trade structure.

90-day cumulative premium flow is **net BEARISH** at −$22.8M (bull $209.7M
vs bear $232.5M) [HIST:cumulative_premium_flow]. **20 of last 28 sessions
were bearish-flow days**, only 8 bullish [HIST:historical_trend.bullish/
bearish_days]. So today's "leaning bullish" tape sits inside a multi-month
bearish flow context — bull conviction must clear that bar.

GEX regime has flipped **9 times in 28 sessions** [HIST:gex_time_series] —
extremely unstable. Today's flip (POSITIVE → NEGATIVE) is the most recent
inversion and matches the price break under $60. P/C ratio z-score −0.44 is
NORMAL (no contrarian extreme) [HIST:pc_ratio_zscore].

Finally, the market-wide **bullish_flow signal backtest is brutal**: 26.7%
win rate, avg 5-day move −1.08% across 15 recent firings (TSLA, NVDA,
META, AVGO, GOOGL, etc. all printed bullish flow then sold off)
[HIST:signal_backtest]. This is a CAUTION FLAG — the recent tape is
unfriendly to bullish-flow follow-through trades.

**Net read:** the setup is **a cheap-vol mean-reversion candidate after an
oversold 4-day flush**, sized small because the macro flow context is bear-
leaning and recent bullish-flow signals have underperformed. **Structure:
DEBIT vol-positive (long premium) preferred over credit, supporting a
long-call-spread or long-call thesis with put-spread protection.**
Conviction **4/5** on the historical read.

## Key signals

- **IV 49.9% = 40.7th percentile of 1y range, z −0.44, regime NORMAL**
  [HIST:iv_percentile_zscore] — IV is *cheap* for FCX, not rich.
- **VRP = −7.4 pts (IV 49.9% < realised 57.3%, regime PREMIUM_BUYING)**
  [HIST:vrp] — favour BUYING premium / debit structures.
- **Price trajectory:** $55.57 (May-04) → **$67.16 (May-13 high)** → **$58.71
  (May-19 close), −12.6% in 4 sessions** [HIST:historical_trend].
- **Cumulative 90d premium flow = NET BEARISH −$22.8M**
  [HIST:cumulative_premium_flow]; **20 of 28 sessions bearish-flow days**
  [HIST:historical_trend].
- **GEX regime unstable — 9 flips in 28 sessions**
  [HIST:gex_time_series]; today's POSITIVE → NEGATIVE flip aligns with
  the break under $60.
- **Bullish_flow signal backtest: 26.7% win rate, −1.08% avg 5d move**
  [HIST:signal_backtest] — the recent tape is hostile to bullish-flow
  follow-through.

## Detailed findings

### IV regime [HIST:iv_percentile_zscore][HIST:vrp]

| Metric | Value | Read |
|--------|-------|------|
| Current IV30d | 49.91% | feels high in absolute terms |
| 1y percentile | **40.74** | **below median — CHEAP for FCX** |
| 1y z-score | −0.44 | mild negative — well within NORMAL band |
| Realised vol 30d | **57.34%** | **realised > implied** |
| **VRP** | **−7.43 pts** | **PREMIUM_BUYING regime** |
| Tool verdict | "Vol cheap vs realised — favour premium buying." | |

The phase-4 backwardation (front 9-DTE 64% vs 30-DTE 52%) is layered ON
TOP of an already-cheap baseline IV. **Net: any debit structure benefits
from both cheap baseline IV AND a high realised tail.** Credit structures
should be avoided here.

### Cumulative premium flow (90d) [HIST:cumulative_premium_flow]

| Component | Value |
|-----------|-------|
| Bullish premium | $209,722,131 |
| Bearish premium | $232,524,922 |
| **Net flow** | **−$22,802,791** |
| **Trend direction** | **BEARISH** |
| Dates covered | 28 sessions over 90 calendar days (gap 03-27 → 04-27) |

The bearish bias is modest in dollar terms (~10% imbalance) but consistent
— phase-1's bullish surface read is the EXCEPTION over 90d, not the rule.

### P/C ratio z-score (20d) [HIST:pc_ratio_zscore]

| Metric | Value |
|--------|-------|
| Current P/C | 0.41 |
| 20d mean | 0.535 |
| 20d std | 0.284 |
| **z-score** | **−0.44** |
| Label | NORMAL (not extreme) |

Today's PC of 0.41 (calls > puts) is consistent with the bullish-leaning
day, but not a contrarian extreme. No fade signal here.

### GEX time series — regime unstable [HIST:gex_time_series]

**Regime flip dates (9 flips in 28 sessions):**

| Date | From → To | Spot | ZGL |
|------|-----------|------|-----|
| 2026-03-16 | + → − | 57.60 | 57.67 |
| 2026-03-17 | − → + | 58.13 | 55.30 |
| 2026-03-26 | + → − | 55.54 | 58.19 |
| 2026-04-27 | − → + | 60.48 | 20.03 (artifact — sparse OI) |
| 2026-04-28 | + → − | 58.53 | 64.29 |
| 2026-04-29 | − → + | 57.06 | 30.04 (artifact) |
| 2026-05-04 | + → − | 56.29 | 59.79 |
| 2026-05-05 | − → + | 57.55 | 20.00 (artifact) |
| **2026-05-19** | **+ → −** | **58.95** | **64.09** |

Today's flip = **9th flip in 28 sessions = ~1 flip every 3 sessions.** This
is extreme regime instability — the dealer hedging map is being rebuilt
constantly. Trade structures should NOT lean on a stable gamma regime
holding for >2 sessions.

### OI trend [HIST:oi_trend]

**Tool error — output exceeded token limit.** See `## Tool errors` below.
Mitigation: phase-3 already captures the cross-sectional OI picture for
2026-05-19 and the 65C/70C July unwind story. The multi-day trend is
inferable from `historical_trend.total_open_interest`:

| Date | Total OI |
|------|----------|
| 2026-03-13 | 1,368,254 |
| 2026-03-19 | 1,391,284 |
| 2026-04-27 | 1,185,162 |
| 2026-05-04 | 1,236,578 |
| 2026-05-13 | 1,353,346 (peak with $67.16 spot) |
| 2026-05-15 | 1,383,096 (peak OI) |
| 2026-05-19 | **1,222,691** (today) |

**Aggregate OI peaked at 1.38M on May-15** (during the high spot) and has
since shed **−160k contracts in 4 sessions**. That matches the phase-3
finding: the 65C / 70C July unwind is part of a broader chain-wide
position-cutting event during the 4-session decline.

### Multi-day trend [HIST:historical_trend]

**Full price + flow trajectory (selected rows, 28 sessions analysed):**

| Date | Close | IV30d | IV rank | PCR | Net flow $ | Flow dir |
|------|-------|-------|---------|-----|------------|----------|
| 2026-03-13 | $56.38 | 59.0% | 54.7 | 1.09 | −1.06M | bearish |
| 2026-03-19 | **$53.62** | 55.3% | 47.0 | **1.28** | **−7.67M** | bearish |
| 2026-03-20 | $52.09 | 58.2% | 52.9 | 0.86 | −2.32M | bearish |
| 2026-03-25 | $57.09 | 58.0% | 52.4 | 0.85 | +1.18M | bullish |
| 2026-03-27 | $56.24 | 59.5% | 55.5 | 0.55 | +0.67M | bullish |
| 2026-04-27 | $60.57 | 47.6% | 45.5 | 0.51 | −1.02M | bearish |
| 2026-04-30 | $57.78 | 43.8% | 36.0 | 0.52 | −1.55M | bearish |
| 2026-05-01 | $56.55 | 45.2% | 38.3 | 0.63 | +1.03M | bullish |
| 2026-05-04 | **$55.57** | 46.4% | 41.8 | 0.35 | −0.20M | bearish |
| 2026-05-06 | $60.89 | 46.4% | 41.9 | 0.28 | −0.52M | bearish |
| 2026-05-08 | $61.71 | 49.1% | 46.0 | 0.54 | −1.50M | bearish |
| 2026-05-11 | $64.37 | 51.3% | 56.6 | 0.31 | −1.26M | bearish |
| 2026-05-12 | $66.03 | 52.7% | 60.9 | 0.30 | **+1.94M** | **bullish** |
| **2026-05-13** | **$67.16** | **54.0%** | **64.9** | 0.42 | −0.94M | bearish |
| 2026-05-14 | $66.14 | 51.5% | 57.5 | 0.67 | −0.50M | bearish |
| 2026-05-15 | $63.06 | 52.0% | 57.0 | 0.50 | +0.12M | bullish |
| 2026-05-18 | $60.50 | 49.3% | 50.7 | 0.23 | **−5.41M** | bearish |
| 2026-05-19 | **$58.71** | 49.9% | 54.9 | 0.41 | −0.39M | bearish |

**Read the trajectory:**
- **Mar 13 → 19:** $56 → $53.62 sell-off; bearish flow days (−$7.7M on
  Mar-19 alone with PCR 1.28).
- **Apr 27 (post data-gap):** stock back at $60.57, but pulls back to
  $55.57 by May-04. IV rank dropped from 55+ to 36 — calm.
- **May 4 → 13:** **+21% rally** in 7 sessions ($55.57 → $67.16). IV
  rank inflated from 36 → 65. **Flow during the rally was net BEARISH on
  most days** (only May-12 was a bullish-flow rally day) — the rally
  happened DESPITE bear flow, likely on copper price news or short-squeeze
  mechanics.
- **May 13 → 19:** **−12.6% reversal** ($67.16 → $58.71). May-18 saw
  −$5.4M net bear flow — the marquee distribution day.
- **IV behaviour:** IV rose with the rally (peak rank 65 on May-13, IV30
  54%) and is now compressing back (rank 55, IV30 50%) — but realised vol
  is HIGH because of the round-trip → VRP −7.4 pts.

The pattern is a **classic blow-off-and-flush** in a copper/cyclical name.
The question now is whether the flush completes (further downside to $55
short-gamma node) or stabilises here above the rally launching pad
($55.57 May-04 low).

### Signal backtest — bullish_flow [HIST:signal_backtest]

- **Total signals (15-session sample, top_n=25 limited to 15 returned)**
- **Win rate: 26.7%** (4 up / 11 down)
- **Avg 5-day move: −1.08%**
- Sample includes TSLA −6.3%, AVGO −5.0%, GOOGL −3.4%, META −1.9%/−2.2%,
  QQQ −0.9%/−0.2%, SMH −2.4%, NVDA −1.1%
- Wins: AMZN +0.06%, AMD +6.32%, RCL +0.51%, AAPL +0.63%

**Caveats:**
- This is **market-wide**, not FCX-specific.
- Sample is tech-heavy (AMZN/AMD/AAPL/MSFT etc.) and the past 2 weeks were
  a tech-led pullback. The signal may perform differently in a copper /
  cyclical name like FCX.
- N=15 is a small sample.

But the **direction of the prior is clear**: in the current market regime,
chasing bullish flow on the close has not paid. **Caution flag for any
aggressive long-only structure in phase-9.**

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `historical_iv_percentile_zscore` | symbol=FCX, lookback=252 | 40.7%ile, z −0.44, NORMAL |
| `historical_vrp` | symbol=FCX, realised=30d, date=2026-05-19 | VRP −7.43, PREMIUM_BUYING |
| `historical_cumulative_premium_flow` | symbol=FCX, days=90 | Net −$22.8M, BEARISH |
| `historical_pc_ratio_zscore` | symbol=FCX, lookback=20 | PCR 0.41, z −0.44, NORMAL |
| `historical_gex_time_series` | symbol=FCX, days=30, dte_max=45 | 9 regime flips / 28 sessions |
| `historical_oi_trend` | symbol=FCX, days=30, top_n=12 | **ERROR — output too large** |
| `historical_trend` | symbol=FCX, days=30 | 28 sessions, 20 bear / 8 bull, see table above |
| `historical_signal_backtest` | signal_type=bullish_flow, lookback=5, top_n=25 | **win_rate 26.7%, avg −1.08%** |

## Tool errors

```
mcp__uw-pp__historical_oi_trend (symbol=FCX, days=30, top_n=12):
Error: result (64,927 characters across 2,641 lines) exceeds maximum
allowed tokens. Output has been saved to a file but we did not read it
back — the multi-day OI question is adequately answered by the
`historical_trend.total_open_interest` time series above (peak 1.38M on
May-15 → 1.22M today = −160k contracts shed in 4 sessions).
```

## Verdict for downstream phases

- **Volatility regime:** **CHEAP** (IV40th %ile of own history, VRP
  −7.4 pts) → favour **DEBIT structures** / long premium / vol-positive
  structures.
- **Premium-buying vs premium-selling:** **PREMIUM-BUYING regime** —
  hard rule against selling credit unless paired against a long-vol leg.
- **Today's signal vs history:** **EDGE-NEGATIVE WARNING.** Market-wide
  bullish_flow signals have a **26.7% win rate** in the recent 15-firing
  sample. This is not FCX-specific but is a strong size-down prior.
- **Conviction:** **4/5** on the historical read itself (rich data,
  consistent story across IV / VRP / price / OI / flow / regime metrics).
- **Three numbers phase-9 must cite:**
  1. **IV30d 40.7%ile + VRP −7.4 pts** → debit > credit structures.
  2. **−12.6% drop from $67.16 (May-13) → $58.71 (May-19)** → setup is a
     **mean-reversion bounce candidate** off recent rally launching-pad
     support, not a fresh trend long.
  3. **Bullish_flow signal backtest 26.7% win rate** → **size down**;
     the recent tape punishes one-sided bullish-flow chasers.
- **Open questions:**
  - What drove the May-04 → May-13 rally? Copper price spike? Indonesia
    smelter news? Analyst upgrade? **Phase 6 macro must investigate.**
  - What drove the May-13 → May-19 reversal? Same catalyst reversed?
    Macro risk-off? China data? **Phase 6 macro.**
  - May-04 low $55.57 + 55-strike −$458M short-gamma node = **a clean
    support / cascade-trigger level**. If $55 holds, the 4-session pullback
    is just a healthy retest; if $55 breaks, the entire May rally was a
    bull-trap and downside extends to $50.
