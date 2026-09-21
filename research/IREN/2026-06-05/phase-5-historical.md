# Phase 5 — Historical Context & VRP

**Ticker:** IREN
**As-of date:** 2026-06-05
**Generated:** 2026-06-07T01:18Z
**Upstream phases cited:** phase-0-intake.md (gap list), phase-0.5-context.md, phase-1-flow.md, phase-3-positioning.md, phase-4-structure.md

> Latest-anchor note: every trailing read below anchors to the latest available
> date = **2026-06-05 = the as-of date** (phase-0-intake.md §UW availability),
> so this run is as-of-clean; a re-run after new sessions land will shift these.

## Summary

Today is the **violent end of a parabolic leg**: IREN ran 35.09 → 66.60
(03-27 → 06-02 closes, +89.8%) then gave back −18.4% in three sessions,
including **−12.1% today (61.86 → 54.35)** [HIST:trend]. The dealer-gamma
backdrop collapsed with it: total_gex +26.0M (06-02) → +3.8M (06-04) →
**−64.8M (06-05) — the deepest negative gamma in the 31-session window**, below
even the March low's −44.0M [HIST:gex_time_series]. Vol is NOT panicking: IV30
108.98% is only the 76.9th percentile (N=39 actual sessions), VRP is −0.048
("FAIR — no clear edge"), and the 20d P/C z-score is +1.47 (elevated, not
extreme) [HIST:iv_percentile_zscore, HIST:vrp, HIST:pc_ratio_zscore]. The OI
chain has built **30 consecutive sessions** (+43%: 1.72M → 2.46M contracts) —
engagement is rising into the crash, with a 2-day put-ladder (55P +29,438 on
06-04, 50P +29,735 on 06-05) chasing price down [HIST:oi_trend]. The
`bearish_flow` class backtests at **87.5% win, N=8** (market-wide, in-sample,
5-day horizon, avg −2.73%) — supportive of downside follow-through but low-N.

## Key signals

- **−12.1% today / −18.4% in 3 sessions off the 66.60 top** — close series
  66.60 (06-02) → 65.48 → 61.86 → 54.35 [HIST:trend daily_data].
- **Gamma collapse: +26.0M → −64.8M in 3 sessions** — largest negative print in
  the window; 7 ZGL regime flips in 30d incl. 06-04 POS→NEG
  [HIST:gex_time_series] (06-05 "POSITIVE" flip label is the degenerate-ZGL
  artifact phase-4 flagged; total_gex sign is the read).
- **IV 76.9th pctile + VRP −0.048**: RV30 (113.7%) is running ABOVE IV30
  (109.0%) — options are NOT rich relative to realized; no premium-selling
  edge despite the percentile [HIST:vrp].
- **OI built 30/30 sessions** (consecutive_build_days=30), net +50–128k/day
  through rally AND crash; put-ladder 55P→50P over 06-04/06-05
  [HIST:oi_trend].
- **90d cumulative flow is MIXED**: bullish $1.832B vs bearish $1.877B, net
  −$45.4M over 40 sessions — no stealth directional build; the tape is a
  two-way battleground [HIST:cumulative_premium_flow].

## Detailed findings

### IV regime [HIST:iv_percentile_zscore, HIST:vrp]

- iv_percentile **76.92**, iv_zscore 0.748, regime "NORMAL", current_iv30d
  1.0898. **dates_used = 39** (not 252 — gap-aware: the lookback only has 39
  sessions on disk; low-N caveat).
- VRP = **−0.0476** (iv30d 1.0898 − realised_vol 1.1374), regime "FAIR",
  interpretation verbatim: "IV close to realised — no clear edge from VRP
  alone."

### Cumulative premium flow — 90d requested, 40 sessions present [HIST:cumulative_premium_flow]

cumulative_bullish $1,831,655,302 vs cumulative_bearish $1,877,058,544 →
net_flow **−$45,403,242**, trend_direction "MIXED". Window crosses the
03-28→04-26 hole (dates_covered confirms 40 sessions, 03-13…06-05).

### P/C ratio z-score [HIST:pc_ratio_zscore]

current 0.91 vs 20d mean 0.5726 (σ 0.2295) → **z = +1.47**, extreme="NORMAL".
Put activity is 1.5σ elevated — stressed but not at the |z|>2 contrarian bar.

### GEX time series (30d, dte≤45) [HIST:gex_time_series]

- Trajectory (selected): 03-27 spot 35.03 / gex −44.0M (FULLY_NEGATIVE) →
  May rally regime POSITIVE with gex +23.9M…+57.0M (05-05→06-03) → 06-04
  +3.8M (NEGATIVE flip, spot 61.92) → **06-05 −64,788,478 (spot 54.23)**.
- 7 regime_flip_dates in the window (05-05, 05-20, 05-21, 05-22, 05-26,
  06-04, 06-05) — several driven by degenerate ZGL prints (5.12–79.93 range);
  the *economic* story is one clean arc: positive-gamma grind up May → gamma
  evaporation 06-03/06-04 → deep short gamma on the 06-05 crash.
- Heuristic hit: "GEX regime flip in last 5d → larger intraday ranges" —
  confirmed by today's 55.94→51.57→54.35 path (phase-1-flow.md).

### OI trend (30d) [HIST:oi_trend]

consecutive_build_days **30**; daily net_oi_change positive every session,
recent: 06-01 +127,536 · 06-02 +92,953 · 06-03 +64,179 · 06-04 +55,183 ·
06-05 +81,882. Total OI 1,719,367 (03-27) → 2,459,547 (06-05), **+43%**.
06-04 top build: **55P 06/12 +29,438** (at 61.86 close) + 55P 01/2028 +5,019
(long-dated puts) + 110C 06/2027 +2,725; 06-05 top build: **50P 06/12
+29,735** (phase-3). The hedge ladder is *following* price down, one strike
per day — reactive protection, not anticipatory.

### Multi-day trend table [HIST:trend] (last 8 of 30 sessions; 19 bearish / 11 bullish days)

| Date | Close | net_flow | PCR | iv_rank | flow_dir |
|---|---|---|---|---|---|
| 05-27 | 67.84* | +$30.77M | 0.51 | 59.4 | bullish |
| 05-28 | 64.05 | −$14.66M | 0.88 | 45.7 | bearish |
| 05-29 | 63.54 | −$11.83M | 1.02 | 46.3 | bearish |
| 06-01 | 65.33 | +$5.07M | 0.27 | 51.3 | bullish |
| 06-02 | 66.60 | +$12.24M | 0.34 | 48.3 | bullish |
| 06-03 | 65.48 | −$8.57M | 0.57 | 51.5 | bearish |
| 06-04 | 61.86 | −$4.31M | 0.74 | 38.2 | bearish |
| **06-05** | **54.35** | **−$18.83M** | **0.91** | **48.2** | **bearish** |

*05-27 close prints 67.84 in this series (intraday spot in gex series 67.71);
window high. Today's −$18.83M net_flow is the largest bearish day in the
window — matching the phase-0.5 self-history 0.0 percentile.

### Price context — fz advisory cross-check [HIST:rsi fz, HIST:52w_proximity fz]

RSI(14) **46.90** (neutral — the crash only unwound overbought, no oversold
signal yet); price vs SMA20 **−7.41%** / SMA50 **+8.95%** / SMA200 **+16.20%**
— short-term breakdown inside an intact longer uptrend; Perf Week **−14.46%**,
Month −10.87%, YTD +43.90%; 52W high 76.87 (**−29.3%** below it), 52W low 8.82
(+516%). Advisory read: this is a correction in a high-beta uptrend name, not
a broken chart — but it has NOT mean-reverted to oversold either; no
knife-catch signal from price alone.

### Signal backtest [HIST:signal_backtest]

`--signal-type bearish_flow --lookback-days 5`: **win_rate 87.5%**,
total_signals **8**, avg_move_pct **−2.73%** over 5 trading days
(methodology verbatim: "In-sample backtest — not a robust live edge";
market-wide class base rate, NOT IREN-specific). Sample incl. NVDA 06-03
−4.49%, SPY 06-03 −2.21%; 1 of 3 shown went against (GOOGL +2.66%). N=8 < 10
→ low-confidence per pitfalls; phase-9 must apply the N-conditional cap.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw historical iv-percentile-zscore --symbol IREN --lookback-days 252 --json` | iv_percentile=76.92, dates_used=39 ← top-level | 1 |
| `uw historical vrp --symbol IREN --realised-window-days 30 --json` | vrp=−0.0476, regime="FAIR" ← `.vrp/.regime` | 1 |
| `uw historical cumulative-premium-flow --symbol IREN --days 90 --json` | net_flow=−45,403,242, trend="MIXED", 40 dates ← `.net_flow/.dates_covered\|length` | 40 sessions |
| `uw historical pc-ratio-zscore --symbol IREN --lookback-days 20 --json` | zscore=1.47, extreme="NORMAL" ← top-level | 1 |
| `uw historical gex-time-series --symbol IREN --days 30 --dte-max 45 --json` | 06-05 total_gex=−64,788,478 ← `.trajectory[-1]`; 7 flips ← `.regime_flip_dates\|length` | 31 rows |
| `uw historical oi-trend --symbol IREN --days 30 --top-n 10 --json` | consecutive_build_days=30; 06-04 55P +29,438 ← `.daily_data[1].top_contracts[0]` (persisted output re-extracted via jq) | 30 days |
| `uw historical trend --symbol IREN --days 30 --json` | bearish_days=19, price_change "35.09 -> 54.35", 06-05 net_flow=−18,832,787 ← `.daily_data[0]` | 30 days |
| `uw historical signal-backtest --signal-type bearish_flow --lookback-days 5 --top-n 20 --json` | win_rate="87.5%", total_signals=8, avg_move_pct=−2.73 ← top-level | 8 signals |
| `fz quote IREN --agent` | RSI 46.90, SMA20 −7.41%, 52W high −29.30% ← `.fundamentals` | 1 |

## Tool errors

(none. Gap handled: iv-percentile (dates_used=39), cumulative-flow (40
sessions), trend/oi-trend/gex (windows span the 03-28→04-26 hole — session
counts quoted, no annualization). No suspicious interpolation observed: every
series jumps 03-27 → 04-27 explicitly.)

## Verdict for downstream phases

- **Volatility regime:** FAIR — 77th pctile IV but RV above IV (VRP −0.048);
  options neither cheap nor rich. Backwardated front (phase-4) + fair VRP =
  no blanket premium-selling edge; structure choice should be delta-led, not
  vol-led.
- **Premium-buying vs selling:** Neutral-to-buying (VRP ≤ 0 heuristic), with
  the caveat that front-week IV 130% is the rich pocket if selling anything.
- **Conviction today's signal is historically edge-positive:** 3/5 — the
  bearish_flow class base rate is strong (87.5%) but N=8/in-sample, and IREN
  itself shows a two-way 90d tape (MIXED) rather than a persistent bearish
  build.
- **Three specific datapoints:** IV percentile **76.92** (N=39) · VRP
  **−0.0476** · bearish_flow backtest **87.5% win, N=8, avg −2.73%/5d**.
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:     bearish_flow
  signal_backtest_win_rate: 0.875
  win_rate_n:       8
  win_rate_source:  backtest
  ```
- **Open questions:** What broke the parabola on 06-03/06-04 (news? sector
  rotation? phase-6/7c)? Does the macro regime say today's gamma collapse is
  idiosyncratic or market-wide (phase-6 — note NVDA/SPY also fired
  bearish_flow on 06-03)? Is the 30-session OI build crowding (phase-7c
  positioning gate)?
