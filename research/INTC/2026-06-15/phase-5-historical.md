# Phase 5 — Historical Context & VRP

**Ticker:** INTC
**As-of date:** 2026-06-15
**Generated:** 2026-06-16T01:24:55Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-4-structure.md

## Summary

Today's mildly-bullish flow sits inside a **euphorically extended, violently
volatile uptrend that has reached its structural ceiling.** INTC is **+33.5% over
the last 30 sessions ($95.78 → $127.86)** and **+246.5% YTD** (`fz`), **−3.7% from
its 52-week high** and **137% above its 200-day SMA** — but the path was a whipsaw
($96 → $128 → $100 → $128), which is why realized vol is **94.3%** [HIST:vrp] and
RSI is only **64** despite the move [HIST:rsi fz]. The single most important
counterweight: **the analyst consensus target is $99.98 — ~22% BELOW spot**
[HIST:target fz], and it lines up with the phase-4 max-pain gravity ($110–112) and
phase-3 $110 put-wall. On vol: IV percentile is high (84) but **VRP is NEGATIVE
(−0.085) → PREMIUM_BUYING regime** (vol cheap vs realized) — favor **debit**
structures, not credit [HIST:vrp]. OI has built **30 consecutive days (+4.64M
contracts)** [HIST:oi_trend] and dealer gamma has been **POSITIVE all 30 sessions,
no flips** [HIST:gex_time_series] — sustained engagement under a stable mean-reverting
cap. The bullish_flow signal backtests **100% (avg +8.1%)** but on **N=7,
market-wide** — nominally edge-positive, low-confidence [HIST:signal_backtest].
Net: the historical context says *the edge is in buying dips, not chasing the
extension into the $130 wall.* Conviction 3.

## Key signals

- **+246.5% YTD, −3.7% from 52w high ($132.75), +137% vs 200-SMA, +31.5% vs
  50-SMA** — extreme extension [HIST:perf fz][HIST:52w_proximity fz].
- **Analyst target $99.98 = −21.8% vs spot $127.86** — consensus says fair value is
  well below; aligns with max-pain $110–112 and $110 put-wall [HIST:target fz].
- **VRP −0.085, PREMIUM_BUYING** (iv30d 85.8% < realized 94.3%) — vol cheap vs
  realized → debit structures favored [HIST:vrp].
- **OI BUILDING 30 consecutive days, +4,643,912 net contracts** — sustained
  position accretion through the rally [HIST:oi_trend].
- **GEX POSITIVE all 30 sessions, 0 regime flips** — persistent dealer long-gamma /
  mean-reversion backdrop [HIST:gex_time_series].
- **bullish_flow backtest: win_rate 100%, avg_move +8.1%, N=7 (market-wide)** — the
  Kelly `p` input, but small-N/low-confidence [HIST:signal_backtest].
- **PCR z-score −0.11 (NORMAL), 90d cumulative flow MIXED (+$210M net on ~$8B each
  side)** — no sentiment extreme, flow two-sided [HIST:pc_ratio_zscore][HIST:cumulative_premium_flow].

## Detailed findings

### IV regime (percentile + z-score + VRP)

- `iv-percentile-zscore`: current_iv30d **0.8582**, iv_percentile **84.44**,
  iv_zscore **0.902**, regime **HIGH_IV**, **dates_used 45** (the 252-day lookback
  only had 45 sessions present — gap-shortened; treat percentile as a 45-session read).
- `vrp`: iv30d 0.8582 vs realised_vol **0.943** → **vrp −0.0848, regime
  PREMIUM_BUYING** ("Vol cheap vs realised — favour premium buying"). **Key for
  phase-9 structure:** despite high IV *rank*, options are cheap vs how much INTC
  actually moves → **debit/long-premium expression**, not premium selling.

### Cumulative premium flow (90d → 46 sessions, gap-crossing)

cumulative_bullish $8.03B vs cumulative_bearish $7.82B → **net +$210.6M (≈+1.3%),
trend_direction MIXED** over **46 dates** (2026-03-23→06-15, crosses the
03-28→04-24 hole — so "90d" = 46 actual sessions, not calendar). The 90-day flow is
**essentially balanced** — no overwhelming stealth accumulation; consistent with
phase-0.5 BUSY_NAME_NORMAL_DAY and phase-1's flat net_flow.

### P/C ratio z-score (sentiment extreme?)

current_pc_ratio 0.6051, mean 0.6273, std 0.2016, **z −0.11, extreme NORMAL** — no
P/C sentiment extreme; today's flow sits right at its 20-day norm. **No contrarian
PCR signal.**

### GEX time series (regime stability)

**30 sessions, regime POSITIVE every day, regime_flip_dates: null.** The trajectory
exposes the **violence of the move**: spot 96.46 (5/4) → 128.52 (5/11) → 100.09
(6/5) → **127.92 (6/15)** — total_gex swung from +$280M to −$74M intra-window. The
*labeled* regime stayed POSITIVE (spot always above the legacy-distorted ZGL), but
total_gex going negative on down days (5/15 −$158M, 6/5 −$74M) shows the
mean-reversion cap is real and the realized vol (94%) is no accident.

### OI trend (buildup vs spike vs decay)

overall_trend **BUILDING**, **consecutive_build_days 30**, total_net_oi_change
**+4,643,912**. Relentless 30-day OI accretion — institutions are *engaged* (both
sides; phase-3 showed the build is OTM calls + ITM writes + put tails). Sustained,
not a one-day spike.

### Multi-day trend table (30d: 2026-05-04 → 06-15, no gap crossing)

| Metric | Value |
|--------|-------|
| price_change | **$95.78 → $127.86 (+33.5%)** |
| bullish_days / bearish_days | 14 / 16 (up days bigger) |
| iv_rank_change | 83.34 → 82.02 (flat, stayed elevated) |
| flow_direction_latest | **bearish** (today's tape) |

Recent leg matches phase-2's dark-pool shelf stack exactly: 6/11 $116.96 → 6/12
$124.57 → 6/15 $127.86 — institutions accumulated *into* each up-step (phase-2).

### Price context (`fz`, EOD cross-check)

| Field | Value | Read |
|-------|-------|------|
| RSI(14) | **64.26** | elevated, not yet overbought (the 6/5 dip reset it) |
| SMA20 / SMA50 / SMA200 | +11.5% / +31.5% / **+136.7%** | very extended, esp. long-term |
| Perf Month / Perf YTD | +10.3% / **+246.5%** | euphoric YTD move |
| 52W High / Low | **$132.75 (−3.68%)** / $18.97 (+574%) | near 52w high, 6.7× off the low |
| Analyst Target / Recom | **$99.98 (−21.8%)** / 2.53 (hold-ish) | **consensus fair value far below spot** |

This is the reality check: a +246% YTD name, near its high, 137% above its
200-SMA, trading **22% above where analysts peg fair value** — and the option
structure's gravity ($110–112 max-pain, $110 put-wall, $100 target) all cluster
*below*. The bullish flow is real but it is chasing an extreme.

### Signal backtest (current signal's edge)

- `signal-backtest --signal-type bullish_flow`: **win_rate 100.0%, total_signals 7,
  avg_move_pct +8.1%** (market-wide signal class, not INTC-specific). Nominally
  strong but **N=7 → low-confidence**; phase-9 must shrink heavily.
- `signal-backtest --signal-type dark_pool_accumulation`: **no backtest results,
  total_signals 0** (re-run once, still empty) → `win_rate_source=null` for the DP signal.

## Tool calls (audit trail)

| Command (`--symbol INTC`, trailing/latest-anchored = 2026-06-15) | Key value(s) ← `jq` path | N |
|------|------|---|
| `historical iv-percentile-zscore --lookback-days 252` | pctile 84.44, regime HIGH_IV, dates_used 45 ← `.iv_percentile` | 45 |
| `historical vrp --realised-window-days 30` | vrp −0.0848, PREMIUM_BUYING ← `.vrp`,`.regime` | 30 |
| `historical cumulative-premium-flow --days 90` | net +$210.6M, MIXED ← `.net_flow`,`.trend_direction` | 46 |
| `historical pc-ratio-zscore --lookback-days 20` | z −0.11, NORMAL ← `.zscore` | 20 |
| `historical gex-time-series --days 30 --dte-max 45` | POSITIVE×30, flips null ← `.trajectory[].regime` | 30 |
| `historical oi-trend --days 30 --top-n 10` | BUILDING, 30 build days, +4.64M ← `.overall_trend` | 30 |
| `historical trend --days 30` | +33.5%, 14/16 days ← `.price_change` | 30 |
| `historical signal-backtest --signal-type bullish_flow --lookback-days 5` | 100% / N7 / +8.1% ← top-level | 7 |
| `historical signal-backtest --signal-type dark_pool_accumulation` (×2) | empty, N0 | 0 |
| `fz quote INTC --agent` | RSI 64.3, target $99.98, +246.5% YTD ← `.fundamentals` | — |

## Tool errors

None. `gex-time-series` series lives in `.trajectory` (not `.series`); re-extracted
cleanly. `dark_pool_accumulation` backtest empty on both runs (expected — recorded
null, not an error).

## DATA NOTE / CORRECTION

- **Gap-awareness applied:** iv-percentile uses **45** actual sessions (not 252);
  CPF "90d" is **46** sessions crossing the 03-28→04-24 hole; the 30d trend window
  (05-04→06-15) is clean of the gap. N's quoted, not calendar spans.
- **Latest-anchor caveat:** all `historical` reads anchor to 2026-06-15 (= as-of).
  A re-run after a new session (esp. earnings 07-23) will shift IV30d, z-scores,
  build-day counts, and the win-rate.

## Verdict for downstream phases

- **Volatility regime:** **HIGH_IV rank (84) but CHEAP vs realized — PREMIUM_BUYING
  (VRP −0.085).** Favor **debit** structures; do not sell premium into 94% realized vol.
- **Premium environment:** premium-**buying**; 90d flow MIXED; OI BUILDING 30 days
  (engaged, two-sided).
- **Conviction that today's signal is HISTORICALLY EDGE-POSITIVE:** **3/5** — the
  bullish_flow backtest is nominally 100% but N=7/market-wide; the overwhelming
  price-context extension (+246% YTD, above analyst target, into the $130 gamma cap)
  says the historical edge favors **buying dips toward $110–120 support, not chasing**.
- **Three specific datapoints:** IV %ile **84.44** · VRP **−0.085 (premium-buying)** ·
  bullish_flow win_rate **1.00 (N=7)**.
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:              bullish_flow
  signal_backtest_win_rate:  1.00
  win_rate_n:                7
  win_rate_source:           backtest      # market-wide base rate, NOT INTC-specific; N=7 → apply N-conditional cap hard
  ```
- **Open questions:**
  - Does a +246% YTD name above its analyst target have the fundamentals to justify
    $128, or is this a mean-reversion trap? → **phase-7b (fundamentals veto)**.
  - Is the move crowded/euphoric (complacent call-skew, retail chase)? → **phase-7c**.
  - Catalyst to break the $130 gamma cap before earnings (07-23)? → **phases 6–7**.
