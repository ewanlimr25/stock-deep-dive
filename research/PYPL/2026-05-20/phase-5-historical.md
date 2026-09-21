# Phase 5 — Historical Context & VRP

**Ticker:** PYPL
**As-of date:** 2026-05-19
**Generated:** 2026-05-20T00:50:00-04:00
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md,
phase-3-positioning.md, phase-4-structure.md

## Summary

Historical context **complicates the phase-2 accumulation story**. PYPL has
been in a downtrend from a post-earnings high of $50.94 (4/29) to $43.84
(5/19) — about **−14% in 14 sessions**. Over the same window, options flow
has been bearish 20 of 28 days (71%), 90-day cumulative net premium is
**−$22.7M bearish-tilted**, and PYPL appeared in `historical_signal_backtest`
**zero times as a "dark_pool_accumulation" signal** — so today's $29.6M
mega-buy is statistically novel for this name in the recent history. IV is
**at the 29.6 percentile of trailing 252d** and VRP = −1.28% (realized
slightly above implied → mild premium-buying edge). The GEX time series
shows persistent regime-flipping (9 flips in 28 days) — PYPL has been
caught around the ZGL all spring. Net read: **today is a potential
inflection / countertrend bid coming in against a still-bearish 90-day
backdrop**. Sizing should reflect that uncertainty.

## Key signals

- **IV30 = 33.5%, IV percentile (252d) = 29.63, IV z-score = −0.91 → IV is
  CHEAP-to-NORMAL** [HIST:historical_iv_percentile_zscore:lookback=252].
- **VRP = −1.28% (IV30 33.5% vs RV30 34.8%) → premium-BUYING regime, but
  edge marginal** [HIST:historical_vrp:2026-05-19].
- **90-day cumulative premium: bullish $137.6M, bearish $160.3M, net
  −$22.7M (BEARISH trend)** [HIST:historical_cumulative_premium_flow:90d].
- **28-day options trend: 20 bearish days vs 8 bullish days; latest
  flow_direction = bearish (5/19 net_flow −$1.13M)**
  [HIST:historical_trend:28d].
- **Stock down ~14% from 4/29 high $50.94 to 5/19 close $43.84 — IV rank
  crushed from 85.0 (4/29) to 22.0 (5/19)** [HIST:historical_trend].
- **`dark_pool_accumulation` backtest: 0 historical signals — today's
  $29.6M mega-buy is the first in the lookback window** [HIST:historical_signal_backtest].
- **PC ratio z-score = +0.68 (current 0.54 vs 20d mean 0.43, std 0.16) →
  modestly elevated puts but NOT extreme** [HIST:historical_pc_ratio_zscore].
- **GEX time series shows 9 ZGL-crossings in 28 days** — regime instability,
  large intraday ranges expected [HIST:historical_gex_time_series:30d].

## Detailed findings

### IV regime (percentile + z-score + VRP)

```
current IV30d:    33.54%
iv_percentile:    29.63 (vs trailing 252d, but using only 27 dated samples)
iv_zscore:        -0.91
regime label:     NORMAL
realized vol 30d: 34.82%
VRP (IV - RV):    -1.28%
VRP regime:       FAIR (IV roughly == realized)
```

[HIST:historical_iv_percentile_zscore, HIST:historical_vrp].

Interpretation: IV is below average for PYPL itself over the last year, but
realized vol has been running slightly above implied. This means **debit
structures (long premium) carry a mild positive theta-adjusted edge**.
Credit structures (short premium) are not punished but lack the usual VRP
tailwind. The 5/22 weekly 47% IV (phase 4) is the obvious exception — that
weekly is in the rich zone and is a SELL candidate if you can hedge it.

### Cumulative premium flow — last 90 days

```
cumulative_bullish:   $137,608,232
cumulative_bearish:   $160,258,442
net_flow:             -$22,650,210
trend_direction:      BEARISH
dates_covered:        28 sessions across 2026-03-13 → 2026-05-19
```

[HIST:historical_cumulative_premium_flow]. **Note the gap in dates** —
3/27 → 4/27 has a 31-day reporting gap (likely UW data not loaded for that
window) so the 90-day label overstates actual coverage; only 28 trading
sessions are represented. Within those, bearish premium is 14% greater
than bullish premium → real but not extreme tilt.

### 28-day flow trend (key columns)

| Date | Close | Net flow ($) | IV30 | IV rank | P/C | Direction |
|------|-------|--------------|------|---------|-----|-----------|
| 2026-05-19 | 43.835 | −1,134,013 | 33.5% | 22.0 | 0.54 | bearish |
| 2026-05-18 | 44.385 | −332,263   | 32.8% | 21.2 | 0.42 | bearish |
| 2026-05-15 | 44.380 | +410,141   | 31.5% | 17.0 | 0.49 | bullish |
| 2026-05-14 | 45.040 | −1,228,598 | 32.8% | 20.9 | 0.35 | bearish |
| 2026-05-13 | 45.230 | −403,003   | 34.5% | 26.6 | 0.21 | bearish |
| 2026-05-12 | 45.440 | −1,339,094 | 32.7% | 20.8 | 0.25 | bearish |
| 2026-05-11 | 45.070 | −555,533   | 33.5% | 23.3 | 0.43 | bearish |
| 2026-05-08 | 45.350 | −2,814,324 | 30.5% | 13.0 | 0.45 | bearish |
| 2026-05-07 | 46.220 | −1,218,722 | 29.6% | 10.4 | 0.50 | bearish |
| 2026-05-06 | 46.270 | +285,032   | 28.2% |  5.9 | 0.41 | bullish |
| 2026-05-05 | 46.485 | +1,282,300 | 35.5% | 32.8 | 0.45 | bullish |
| 2026-05-04 | 50.390 | −506,154   | 48.2% | 71.5 | 0.74 | bearish |
| 2026-05-01 | 50.440 | −2,488,527 | 49.3% | 75.4 | 0.42 | bearish |
| 2026-04-30 | 50.200 | −651,206   | 47.6% | 68.5 | 0.27 | bearish |
| 2026-04-29 | 50.940 | +1,428,687 | 52.3% | 85.0 | 0.26 | bullish |
| 2026-04-28 | 49.640 | −313,736   | 49.6% | 76.2 | 0.25 | bearish |
| 2026-04-27 | 49.770 | −2,563,958 | 48.3% | 71.9 | 0.51 | bearish |
| 2026-03-27 | 43.590 | −1,993,119 | 45.3% | 41.8 | 0.45 | bearish |
| 2026-03-26 | 45.200 | +647,612   | 43.3% | 37.4 | 0.90 | bullish |
| 2026-03-25 | 44.850 | −278,531   | 41.9% | 34.4 | 0.45 | bearish |
| 2026-03-24 | 44.210 | −790,874   | 41.9% | 34.4 | 0.32 | bearish |
| 2026-03-23 | 45.490 | +1,934,794 | 41.6% | 33.6 | 0.34 | bullish |
| 2026-03-20 | 44.010 | +1,258,261 | 41.7% | 33.9 | 0.72 | bullish |
| 2026-03-19 | 44.190 | −8,820,898 | 40.4% | 32.7 | 0.82 | bearish |
| 2026-03-18 | 44.590 | −1,084,056 | 39.6% | 29.2 | 0.40 | bearish |
| 2026-03-17 | 46.130 | +14,984    | 39.4% | 28.7 | 0.40 | bullish |
| 2026-03-16 | 45.420 | −762,836   | 40.7% | 31.6 | 0.71 | bearish |
| 2026-03-13 | 44.900 | −632,576   | 44.4% | 39.9 | 0.63 | bearish |

[HIST:historical_trend:28d]. Key observations:
- **PYPL had earnings in late April** (IV peaked at 85.0 IV rank on 4/29
  → crushed to 5.9 IV rank by 5/6; classic post-print vol crush). Stock
  popped to $50.94 high on 4/29 then **dropped −14% over 14 sessions**.
- **No bullish session in last 4** — 5/15 was last bullish day.
- **8 bullish vs 20 bearish days = 28.6% bullish hit rate** → trend is
  one-sided.
- The big bearish premium day was **3/19 (net −$8.82M)** — a $46M
  bearish premium day with bullish $15.9M, net −$8.8M. That was a
  campaign day, possibly tied to a Q4-2025 earnings or guidance event.

### PC ratio z-score (sentiment)

```
current_pc:    0.54
20d mean:      0.43
20d std:       0.16
zscore:        +0.68
extreme:       NORMAL
```

[HIST:historical_pc_ratio_zscore]. PC has drifted up but is not at an
extreme. **Not a contrarian setup** — no fear-driven sentiment to fade.

### GEX time series (28-day)

9 regime flips in 28 days — extremely unstable. Key crossings:

| Date | Regime change | Spot | ZGL | ZGL Δ |
|------|--------------|------|-----|--------|
| 2026-03-17 | NEG → POS | 46.44 | 29.20 | −20.0 |
| 2026-03-24 | POS → NEG | 44.52 | 47.69 | +19.7 |
| 2026-04-30 | NEG → POS | 50.09 | 49.76 | −2.5 |
| 2026-05-05 | POS → NEG | 45.61 | 49.88 | +20.4 (vol explosion) |
| 2026-05-12 | NEG → POS | 45.19 | 25.01 | −24.6 |
| 2026-05-13 | POS → NEG | 45.18 | 47.05 | +22.0 |
| 2026-05-14 | NEG → POS | 45.22 | 30.18 | −16.9 |
| 2026-05-15 | POS → NEG | 44.87 | 45.81 | +15.6 |
| **2026-05-19** | **NEG → POS** | **44.22** | **37.06** | **−8.6 (today)** |

[HIST:historical_gex_time_series]. Spring 2026 has been a structural
regime-flip storm for PYPL. The **5/19 flip from NEGATIVE to POSITIVE**
matches the phase-4 reading. Note the ZGL collapsed from $45.66 on 5/18 to
$37.06 on 5/19 — that's a meaningful structural change driven by today's
new positioning (the $50 wall buildup pushed total GEX positive and ZGL
down). Total GEX has been climbing rapidly: $1.7B (5/5), $2.2B (5/13),
$4.9B (5/18), then back to $2.2B on 5/19. The 5/18 peak was an anomaly
(probably end-of-week OI stacking).

### Signal backtest (matches current setup)

The **dark_pool_accumulation** signal returned 0 results across all
tickers in the recent lookback window
[HIST:historical_signal_backtest:dark_pool_accumulation] — meaning today's
$29.6M mega-buy pattern is novel in the recent population. No edge can be
read.

For comparison, market-wide:
- `bullish_flow` signals (10-day forward): 15 signals, **win_rate 26.7%,
  avg move −1.10%** — bullish flow has been a LOSING signal recently;
  market is in a downtrend.
- `bearish_flow` signals (10-day forward): 14 signals, **win_rate 71.4%,
  avg move −1.24%** — bearish flow has been winning; confirms the broader
  bear tilt.

[HIST:historical_signal_backtest:bullish_flow, bearish_flow].

This is a **critical context check**: the broad market has been
faded-on-bullish, vindicated-on-bearish over the past 10 sessions. Acting
on PYPL bullish accumulation against that tape requires either (a) a
strongly idiosyncratic catalyst (which phase 6 macro must check) or (b)
a structural reason this name escapes the market trend (M&A, activist).

### OI trend (28-day)

The `historical_oi_trend` response exceeded the inline-token limit and was
written to disk
(`/Users/ewan/.claude/projects/.../mcp-uw-pp-historical_oi_trend-1779307151611.txt`)
**without being re-read here** — phase 3's same-day OI data is the
actionable subset for trade design. **Flagging as a known gap**:
multi-day OI buildup analysis is not in this phase. If phase 8 sub-agents
need it, they should query that file directly with `jq`.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__historical_iv_percentile_zscore` | symbol=PYPL, lookback-days=252 | IV %ile 29.6, z −0.91, NORMAL |
| `mcp__uw-pp__historical_vrp` | symbol=PYPL, realised-window-days=30, date=2026-05-19 | VRP −1.28%, FAIR |
| `mcp__uw-pp__historical_cumulative_premium_flow` | symbol=PYPL, days=90 | net −$22.7M, BEARISH |
| `mcp__uw-pp__historical_pc_ratio_zscore` | symbol=PYPL, lookback-days=20 | z +0.68, NORMAL |
| `mcp__uw-pp__historical_gex_time_series` | symbol=PYPL, days=30, dte-max=45 | 9 regime flips in 28d |
| `mcp__uw-pp__historical_oi_trend` | symbol=PYPL, days=28, top-n=15 | (truncated to disk, NOT read) |
| `mcp__uw-pp__historical_trend` | symbol=PYPL, days=28 | 8 bull / 20 bear days |
| `mcp__uw-pp__historical_signal_backtest` | signal-type=dark_pool_accumulation, lookback-days=10 | 0 signals |
| `mcp__uw-pp__historical_signal_backtest` | signal-type=bullish_flow, lookback-days=10 | 15 signals, win 26.7%, avg −1.1% |
| `mcp__uw-pp__historical_signal_backtest` | signal-type=bearish_flow, lookback-days=10 | 14 signals, win 71.4%, avg −1.24% |

## Tool errors

- `historical_oi_trend` returned a payload too large for inline ingestion;
  result was written to disk. **Not retried** — phase-3 same-day OI data
  is sufficient for the trade plan.

## Verdict for downstream phases

- **Bias from this phase:** **mixed leaning cautious-bullish**. Two
  opposing themes:
  - SUPPORT for today's bullish DP/structure setup: low IV (29 %ile), VRP
    slightly negative (premium-buy edge), inverted skew (call demand),
    regime flip to POSITIVE today, novel dark-pool accumulation pattern
    not seen in lookback.
  - AGAINST: 90-day net premium is bearish, 71% of last 28 days were
    bearish-tape, broad-market bullish_flow win rate has been just 26.7%,
    stock is in a clear 14% downtrend with no bullish reversal print
    since 5/15.
- **Conviction:** **2 / 5** — historical context is the weakest link in
  the chain. The bullish signal is real today (phase 2/4) but lacks
  historical precedent in this name and runs against the recent tape.
- **Three data points later phases must remember:**
  1. **IV rank 22, VRP −1.3%** → premium-buying environment, debits
     favored, but no big edge (don't pay up).
  2. **20 of 28 trailing days were bearish flow** → today's bullish
     setup is countertrend.
  3. **bullish_flow signal win rate 26.7% over last 10 sessions** —
     ~3:1 against bullish setups historically in current market.
  4. (Bonus) Earnings was end of April, vol-crushed to IV rank 5.9 by
     5/6. **No upcoming earnings catalyst in next 60 days** (phase 6 to
     confirm).
- **Open questions:**
  - Is there a macro / sector / news catalyst making 5/19 the
    inflection? Phase 6 macro must answer.
  - Phase 7 `insights_institutional_accumulation` is the next direct
    signal triangulation — does the UW composite agree with the
    accumulation read?
  - Is there short-interest data or activist-investor flag for PYPL
    that explains the inverted skew (call demand)? Reserve as a phase-9
    risk monitor item.
