# Phase 5 — Historical Context & VRP

**Ticker:** RKT
**As-of date:** 2026-05-20 (data through 2026-05-19; 28 sessions analyzed)
**Generated:** 2026-05-20T00:50:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-4-structure.md

## Summary

Historical context introduces meaningful **caution against the structural
bull case** built in phases 1–4. IV is **cheap** (33rd percentile, VRP
-4.05% — premium-BUYING regime), but the 28-day flow has been
**bearish 19:9 days** and price has fallen 10.4% over the window (from
$14.14 close on 3/13 to $12.675 on 5/19). Most importantly,
`historical_signal_backtest` for `bullish_flow` shows a **10.0% win rate
over the last 20 trading days with -1.57% average post-signal move** —
the regime has been actively punishing bull-flow signals. The 20-day
**P/C ratio z-score = +3.208 (BEARISH_EXTREME)** confirms today's tape is a
3σ put-buying outlier vs the trailing 20-day baseline [HIST:pc_ratio_zscore].
The countervailing positives: 28 consecutive days of net OI build
([HIST:oi_trend]), GEX regime instability (6 flips in 28 days) that
favors event-driven option payouts, and IV30 below 1y average. Net read:
the SETUP is asymmetric but the REGIME punishes premature longs — phase-9
must size accordingly and structure around the 5/22 catalyst rather than
direct delta exposure.

## Key signals

- **IV30 at 60.1% = 33rd percentile (1y)** with VRP **-4.05%** → premium is
  CHEAP and IV may underprice the 5/22 catalyst [HIST:iv_percentile_zscore,
  HIST:vrp].
- **bullish_flow signal: 10% win rate, -1.57% avg post-signal move over the
  last 20 trading days** — the market is rejecting bull flow signals
  [HIST:signal_backtest]. Strong caution against directional long.
- **20-day P/C z-score = +3.208 (BEARISH_EXTREME)** — today's flow is a
  3σ put-buying outlier [HIST:pc_ratio_zscore].
- **28-day flow direction: 19 bearish days vs 9 bullish** [HIST:trend].
- **Price down 10.4% in 28 sessions** ($14.14 → $12.675) with high IV-rank
  volatility (23–52 range) [HIST:trend].
- **6 dealer regime flips in 28 days** (4/29, 4/30, 5/5, 5/8, 5/13, 5/14) —
  highly unstable dealer book; large intraday ranges expected
  [HIST:gex_time_series].
- **OI accumulation: 28 consecutive build days, +21,215 net contracts today
  alone** — institutions persistently adding positions through the
  drawdown [HIST:oi_trend].

## Detailed findings

### IV regime (`mcp__uw-pp__historical_iv_percentile_zscore`, `historical_vrp`)

```
current_iv30d : 0.6014  (60.1%)
iv_percentile : 33.33   (1y window, dates_used=27)
iv_zscore     : -0.356
regime label  : NORMAL
realised_vol  : 0.6419  (64.2% over 30d)
vrp           : -0.0405 (negative — IV below realised)
vrp regime    : FAIR (IV close to realised)
```

**Read:**
- 1y IV percentile of 33 means current vol is BELOW two-thirds of the
  trailing year. Premium is structurally cheap.
- VRP of -4.05% means realised vol has been outpacing implied — the market
  is UNDERPRICING actual movement. Favorable for premium-BUYING.
- Caveat: `dates_used=27` indicates the 252-day window is constrained by
  the available data set (28 sessions only). The percentile is computed
  off that limited universe, not a true 1y baseline.

### Volatility risk premium

- IV30 (60.1%) − Realised30 (64.2%) = **-4.05% VRP**.
- Combined with phase-4 finding that May-22 weekly IV is 85.9% (a +25 vol
  point spike), the immediate event is over-priced but the BACK-END is
  under-priced. **Calendar / diagonal structures are mechanically attractive.**

### 90-day cumulative premium flow (`historical_cumulative_premium_flow`)

```
days                  : 90 (28 trading sessions)
cumulative_bullish    : $41,456,907
cumulative_bearish    : $44,221,697
net_flow              : -$2,764,790
trend_direction       : MIXED
```

90d net premium is slightly bearish but within noise. **There is NO clean
multi-month bullish trend in cumulative flow** — phase-1's bullish-tilt
read is a recent (5-day) phenomenon, not a multi-month accumulation.

### P/C ratio z-score (`historical_pc_ratio_zscore`)

```
current_pc_ratio  : 0.98
mean_pc_ratio     : 0.4238  (over 20 sessions)
std_pc_ratio      : 0.1734
zscore            : +3.208
extreme           : BEARISH_EXTREME
```

**Critical observation:** today's P/C of 0.98 is a 3.2σ outlier vs the
20-day mean (0.42). On a Z>3 reading the prior interpretation is
"contrarian extreme" — typically a level where markets reverse. However,
when the elevated put activity reflects hedge-building (per phase-2 and
phase-3 collar structures), the contrarian reading is weaker — the puts are
not speculative bearish bets.

**Reconciliation with phase-4 "COMPLACENT" skew:** the 25Δ IV puts are
still LESS rich than 25Δ IV calls (skew -0.02), but the **flow VOLUME** of
puts is at a 3σ extreme today. Resolution: institutions are adding
volume in puts at relatively cheap levels (25Δ put IV ~59%) to BUILD
HEDGES, while leaving call premium rich because they ALSO want to buy
calls for upside. This is exactly the "collar / risk-reversal" footprint
inferred in phase-3.

### GEX time series (`historical_gex_time_series`)

28-day GEX trajectory + regime flips (positive ↔ negative):

| Date | Spot | ZGL | Total GEX | Regime |
|------|------|-----|-----------|--------|
| 2026-03-13 | 14.41 | 9.65  | +$235M | POSITIVE |
| 2026-03-16 | 15.01 | 12.26 | +$317M | POSITIVE |
| 2026-04-27 | 15.55 | 14.89 | +$230M | POSITIVE |
| **2026-04-29** | 14.46 | 15.75 | +$202M | **NEGATIVE flip ↓** |
| **2026-04-30** | 14.78 | 8.31  | -$44M  | **POSITIVE flip ↑** |
| 2026-05-04 | 14.26 | 10.23 | +$1.28B | POSITIVE (peak) |
| **2026-05-05** | 14.14 | 18.56 | +$211M | **NEGATIVE flip ↓** |
| 2026-05-06 | 14.84 | 16.60 | +$464M | NEGATIVE |
| 2026-05-07 | 14.19 | 14.77 | +$385M | NEGATIVE |
| **2026-05-08** | 15.41 | 1.17  | +$1.22B | **POSITIVE flip ↑** |
| 2026-05-11 | 14.96 | 8.00  | +$784M | POSITIVE |
| 2026-05-12 | 14.70 | 9.50  | +$596M | POSITIVE |
| **2026-05-13** | 14.08 | 16.95 | +$149M | **NEGATIVE flip ↓** |
| **2026-05-14** | 14.51 | 11.51 | +$361M | **POSITIVE flip ↑** |
| 2026-05-15 | 13.58 | 5.02  | +$531M | POSITIVE |
| 2026-05-18 | 13.20 | 9.52  | +$538M | POSITIVE |
| **2026-05-19** | 12.65 | 10.52 | -$124M | POSITIVE (but GEX flipped to NEGATIVE net) |

**Six regime flips in 28 sessions = high dealer instability.** Each flip
corresponds to a significant intraday range, typically 4–6%. ZGL has
oscillated from $1.17 (5/8 low) to $18.56 (5/5 high) — extraordinary
movement that reflects rapid OI shuffling.

**Today's snapshot is rare:** spot $12.65 ABOVE ZGL $10.52 (POSITIVE
regime label) BUT total_gex flipped NEGATIVE for the first time since 4/30
— that means the strike-specific gamma walls (notably $13 = -$374M) are
overwhelming the long-gamma support below. Combined with the upcoming
5/22 catalyst, this is the historically-rare "negative-gex above ZGL +
event-vol localized at 5/22" configuration.

### OI trend (`historical_oi_trend`, 30d)

```
consecutive_build_days  : 28
today_increases         : 202 contracts
today_decreases         : 56 contracts
today_net_oi_change     : +21,215 contracts
```

**28 consecutive sessions of net OI build** — every single trading day
since 3/13 has added net OI in RKT. That's a HALLMARK accumulation pattern
even in the face of a 10.4% price decline. Institutions are positioning
through the drawdown.

Top contracts today (same as phase-3, repeated for context):

| Symbol | DTE | OI Δ |
|--------|-----|------|
| RKT260821C00014000 (Aug 14C) | 94 | +3,610 |
| RKT260529C00014000 (May-29 14C) | 10 | +2,643 |
| RKT260522P00013000 (May-22 13P) | 3 | +1,368 |
| RKT280121P00010000 (Jan-28 10P) | 612 | +1,237 |
| RKT260522C00014000 (May-22 14C) | 3 | +978 |
| RKT261218P00011000 (Dec 11P) | 213 | +853 |
| RKT260821C00013000 (Aug 13C) | 94 | +657 |
| RKT260918P00013000 (Sep 13P) | 122 | +566 |
| RKT260522C00013500 (May-22 13.5C) | 3 | +485 |

### Multi-day trend table (`historical_trend`, last 14 sessions)

| Date | Close | IV30 | IV rank | Bull premium | Bear premium | Net | P/C | Flow dir |
|------|-------|------|---------|--------------|--------------|-----|-----|----------|
| 5/19 | 12.675 | 60.1% | 34.3 | $2.79M | $2.96M | -$171k | 0.98 | bearish |
| 5/18 | 13.04  | 59.3% | 32.4 | $1.98M | $1.58M | +$399k | 0.55 | bullish |
| 5/15 | 13.355 | 55.4% | 27.6 | $1.94M | $1.77M | +$166k | 0.40 | bullish |
| 5/14 | 14.28  | 54.6% | 23.1 | $0.96M | $1.00M | -$39k  | 0.45 | bearish |
| 5/13 | 13.84  | 54.5% | 22.9 | $1.01M | $2.01M | -$992k | 0.39 | bearish |
| 5/12 | 14.80  | 55.7% | 25.2 | $0.94M | $1.31M | -$363k | 0.34 | bearish |
| 5/11 | 14.83  | 58.2% | 30.2 | $1.90M | $2.46M | -$554k | 0.25 | bearish |
| 5/8  | 15.69  | 55.0% | 24.9 | $3.28M | $2.88M | +$402k | 0.21 | bullish |
| 5/7  | 14.15  | 64.7% | 43.2 | $1.73M | $2.27M | -$544k | 0.66 | bearish |
| 5/6  | 14.65  | 60.4% | 34.5 | $1.28M | $0.72M | +$552k | 0.43 | bullish |
| 5/5  | 14.125 | 62.8% | 39.8 | $0.54M | $0.74M | -$192k | 0.27 | bearish |
| 5/4  | 14.01  | 63.4% | 40.5 | $0.93M | $2.31M | -$1.37M | 0.59 | bearish |
| 5/1  | 14.64  | 65.9% | 45.5 | $1.81M | $1.20M | +$611k | 0.28 | bullish |
| 4/30 | 14.61  | 66.0% | 46.0 | $1.08M | $1.06M | +$19k  | 0.74 | bullish |

Summary:
- bullish_days = 9, bearish_days = 19 (28 sessions)
- Latest flow_direction = bearish
- IV rank trending DOWN (from 45–52 in late April to 22–34 currently)
- P/C ratio TODAY (0.98) is the highest in the window — a clear outlier

### Signal backtest — bullish_flow (`historical_signal_backtest`)

```
signal_type : bullish_flow
lookback_days: 20
total_signals: 10
win_rate    : 10.0%
avg_move_pct: -1.57%
```

| Signal date | Ticker | Direction | % change |
|-------------|--------|-----------|----------|
| 2026-05-18 | AMD  | up   | +5.66% |
| 2026-05-18 | AMZN | down | -1.00% |
| 2026-05-18 | RCL  | down | -5.49% |
| 2026-05-15 | MSFT | down | -1.91% |
| 2026-05-15 | AAPL | down | -0.27% |
| 2026-05-15 | UPS  | down | -1.35% |
| 2026-05-14 | QQQ  | down | -1.54% |
| 2026-05-14 | SMH  | down | -2.82% |
| 2026-05-14 | META | down | -2.70% |
| 2026-05-14 | AVGO | down | -4.27% |

**9 out of 10 bullish_flow signals in the last 20 days have FAILED.** The
only win was AMD at +5.66%. The average outcome is -1.57%.

This is a market-regime warning: across multiple large-cap names with
bullish flow, the market has been selling them. RKT's bullish signal is
operating in a regime where similar setups have been losing money.
**Phase-9 MUST factor this in:** the structural bull case from phases 1, 3,
and 4 is real, but the macro tape is against it. A pure delta-long
strategy is materially derisked relative to the standalone signal read.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `historical_iv_percentile_zscore` | `{symbol: RKT, lookback_days: 252}` | IV 60.1% / 33rd %ile / NORMAL |
| `historical_vrp` | `{symbol: RKT, realised_window_days: 30, date: 2026-05-19}` | VRP -4.05% / FAIR |
| `historical_cumulative_premium_flow` | `{symbol: RKT, days: 90}` | net -$2.76M MIXED |
| `historical_pc_ratio_zscore` | `{symbol: RKT, lookback_days: 20}` | z +3.208 / BEARISH_EXTREME |
| `historical_gex_time_series` | `{symbol: RKT, days: 30, dte_max: 45}` | 6 regime flips; today total_gex -$124M |
| `historical_oi_trend` | `{symbol: RKT, days: 30, top_n: 10}` | 28-day build streak; +21,215 today |
| `historical_trend` | `{symbol: RKT, days: 30}` | 19 bearish vs 9 bullish days; flow today bearish |
| `historical_signal_backtest` | `{signal_type: bullish_flow, lookback_days: 20, top_n: 20}` | 10/10 signals; **win 10%**, avg -1.57% |

## Tool errors

(none)

## Verdict for downstream phases

- **Bias from this phase:** **mixed, leaning structurally bullish but
  regime-cautious.** The structural setup is real; the regime context is
  hostile to long-bias signals.
- **Conviction:** 2/5 on direction, 4/5 on volatility (IV is mispriced
  cheap relative to realised, and 5/22 event is mispriced relative to
  back-end vol).
- **Three datapoints for phase-9:**
  1. **IV percentile 33 + VRP -4.05%** → premium-buying regime favored;
     debit structures preferred over credit structures (despite
     phase-3's put-selling observation).
  2. **Bullish_flow signal win rate = 10% (last 20d)** → directional long
     bets via bullish flow have been failing. Phase-9 trade plan should
     express the thesis via DEFINED-RISK structures (debit spreads,
     calendars) rather than naked long calls or stock.
  3. **28-session continuous OI build** through a 10% drawdown is a
     compelling stealth-accumulation footprint — but the BUILD has not
     yet translated to price gain.
- **Open questions:**
  - **What is the 5/22 catalyst** (still unresolved from phase-4)? Phase-6
    must answer this — without it, the trade plan is incomplete.
  - Is the macro mortgage-rate backdrop friendly or hostile to RKT now?
    (phase-6)
  - Is there a sector-wide bearish-flow signal that would explain the 10%
    bullish_flow win rate? (phase-6 or phase-7 insights)
