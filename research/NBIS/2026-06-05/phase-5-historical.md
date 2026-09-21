# Phase 5 — Historical Context & VRP

**Ticker:** NBIS
**As-of date:** 2026-06-05
**Generated:** 2026-06-06T20:45:00-0400
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md, phase-1-flow.md, phase-4-structure.md

## Summary

NBIS is three sessions into the violent unwind of a parabolic run: **$100.82 →
$265.33 (Jun-01) → $227.81**, i.e. +163% in ~10 weeks then −14% in four days.
IV sits at the **97.4th percentile** of its (39-session-actual) 1-year window —
yet **VRP is negative (−0.0841: IV30d 111.7% vs realized 120.1%)**, so the tool
labels the regime **PREMIUM_BUYING**: even 97th-percentile implied is cheap
against what the stock actually moves. The dealer book flipped from POSITIVE to
**FULLY_NEGATIVE on 2026-06-03** (spot 251.1 broke under the Jun-02 ZGL 257.97)
and has stayed negative for 3 straight sessions — phase-4's amplification regime
is fresh, not chronic. The option chain has expanded for **30 consecutive
build days** (+32k…+64k net OI/day) with no capitulation. The `bearish_flow`
signal class phase-1 leans toward backtests at **87.5% win rate — but N=8,
in-sample**, below the 10-firing confidence floor.

## Key signals

- IV percentile **97.44**, z-score 1.224, regime HIGH_IV — over **39 actual
  sessions** (`dates_used`), not 252 (gap caveat) `[HIST:iv_percentile_zscore]`
- **VRP −0.0841** (IV30d 1.117 < RV30 1.2012) → tool verbatim: "Vol cheap vs
  realised — favour premium buying." regime **PREMIUM_BUYING** `[HIST:vrp]`
- 90-day cumulative flow: bullish $3.6475bn vs bearish $3.6212bn → net
  **+$26.3M on $7.27bn two-way (0.4% skew), trend_direction MIXED** — no
  stealth directional build `[HIST:cumulative_premium_flow]`
- GEX regime flipped **POSITIVE → FULLY_NEGATIVE on 2026-06-03** and is 3-for-3
  negative since; ZGL was 248.78 (6/01) → 257.97 (6/02) → null
  `[HIST:gex_time_series]`
- OI: **30/30 consecutive net-build days**; latest builds led by Jun-12 205P
  **+6,884 (06-04 file) then +6,871 (06-05 file)** — the bear line was stacked
  two days running, pre-slide (confirms phase-3) `[HIST:oi_trend]`
- Backtest (`bearish_flow`, market-wide, 5-td forward): **win_rate 87.5%,
  total_signals 8, avg_move_pct −2.73%** — in-sample, N<10 → low-confidence
  `[HIST:signal_backtest]`

## Detailed findings

### IV regime (percentile + z-score + VRP)

- `iv_percentile` 97.44 / `iv_zscore` 1.224 / `current_iv30d` 1.117 / regime
  HIGH_IV. **Gap caveat:** `dates_used: 39` — the "1-year" percentile is over 39
  available sessions (2026-03-13…06-05 with the 03-28→04-24 hole, phase-0 list);
  treat as a ~2-month percentile, still extreme.
- VRP = 1.117 − 1.2012 = **−0.0841** → PREMIUM_BUYING. The heuristic "IV rich +
  VRP>0 → sell premium" does NOT fire; the regime favors **debit structures
  despite 90 IV-rank** because realized vol (Friday: −12.6% from Thursday's
  close, phase-2 path 252→217 intraday) keeps outrunning implied.

### Cumulative premium flow (90d → 40 sessions actual)

cumulative_bullish $3,647,518,791 vs cumulative_bearish $3,621,172,229 →
net_flow **+$26,346,562**, trend MIXED. `dates_covered` = the 40 local sessions
(03-13…06-05, hole excluded). No 60-day persistent build either way — the
LEAP-grade institutional money is two-sided (consistent with phase-1's balanced
ex-0DTE delta and phase-2's 0.50 buy ratios).

### P/C ratio z-score (20d)

current 0.97 vs mean 0.8822 (σ 0.2965) → **z = 0.296, extreme: NORMAL**.
No contrarian sentiment extreme despite the crash `[HIST:pc_ratio_zscore]`.

### GEX time series (30 sessions, 2026-03-27…06-05)

| Window | Regime | Spot path |
|---|---|---|
| 03-27 → 04-30 | FULLY_NEGATIVE | 101 → 138 (squeeze-up through short gamma) |
| 05-01 → 05-15 | POSITIVE | 154 → 220 (orderly, ZGL trailing below) |
| 05-18 → 05-27 | mostly NEGATIIVE→mixed | 197 → 208 (chop) |
| 05-28 → 06-02 | POSITIVE | 227 → **265.33 (06-01)** → 262.9; ZGL 248.78→257.97 |
| **06-03 → 06-05** | **FULLY_NEGATIVE** | 251.1 → 259.9 → **227.19**; total_gex −0.9M → −0.05M → **−12.5M** |

The 06-05 total_gex (−$12.5M) is the most negative since 03-27 (−$20.5M, when
the stock was $101). Note this name **rallied 38% inside a FULLY_NEGATIVE
regime in April** — short gamma amplifies *both* directions here; it is not a
bearish datapoint by itself.

### OI trend

`consecutive_build_days: 30` — every session in the window added net OI
(daily net +32,024…+64,425; 06-05 file: +38,682 = increases 48,701 vs decreases
−10,019). Two-day 205P build totals ~13.8k contracts (06-04: +6,884; 06-05:
+6,871) ≈ 1.38M share-equiv ≈ **0.69% of float** on one strike. Chain growth
through both the melt-up and the break = positioning intensity rising into the
event, no unwind yet.

### Multi-day trend (30 sessions, 03-27…06-05, crosses the gap)

bullish_days 14 vs bearish_days 16; flow_direction_latest **bearish**;
iv_rank_change **40.85 → 89.97**; price_change **100.82 → 227.81**
`[HIST:trend]`. A near-balanced daily flow count over a +126% price window —
the rally was never flow-consensus, and the tape has been bearish-tilted at the
margin while price doubled.

### Price context (advisory, `fz`)

RSI(14) **56.12** — neutral after the flush (no oversold signal yet)
`[HIST:rsi fz]`; price vs SMA20 +4.67%, vs SMA50 +31.97%, vs **SMA200 +94.45%**;
Perf YTD +172.16%, month +16.77%; 52W high **278.84 (−18.30% below)**, 52W low
41.40 (+450%) `[HIST:52w_proximity fz]`. Even post-crash the name is barely
back to its 20-day mean and massively extended vs long-term trend — "dip" by
last week's prices, still parabolic by any longer lens.

### Signal backtest (`bearish_flow`)

win_rate **"87.5%"**, total_signals **8**, avg_move_pct **−2.73%** (5 trading-day
forward), methodology verbatim: "In-sample backtest — not a robust live edge."
Market-wide base rate (tool takes no `--symbol`), not NBIS-specific. N=8 < 10 →
treated as low-confidence per phase pitfalls; phase-9 must apply the
N-conditional cap from `rubrics/sizing-rubric.md`.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw historical iv-percentile-zscore --symbol NBIS --lookback-days 252 --json` | 97.44 / 1.224 / dates_used 39 ← `.iv_percentile/.iv_zscore/.dates_used` | 39 sessions |
| `uw historical vrp --symbol NBIS --realised-window-days 30 --json` | vrp −0.0841, regime PREMIUM_BUYING ← `.vrp/.regime` | 1 |
| `uw historical cumulative-premium-flow --symbol NBIS --days 90 --json` | net +26,346,562 MIXED ← `.net_flow/.trend_direction`; 40 dates ← `.dates_covered\|length` | 40 sessions |
| `uw historical pc-ratio-zscore --symbol NBIS --lookback-days 20 --json` | z 0.296 NORMAL ← `.zscore/.extreme` | 20d window |
| `uw historical gex-time-series --symbol NBIS --days 30 --dte-max 45 --json` | trajectory table ← `.trajectory[].{date,regime,spot,total_gex,zero_gamma_level}` | 30 sessions |
| `uw historical oi-trend --symbol NBIS --days 30 --top-n 10 --json` | build_days 30; daily nets ← `.consecutive_build_days/.daily_data[].net_oi_change` (persisted output re-jq'd) | 30 sessions |
| `uw historical trend --symbol NBIS --days 30 --json` | 14/16 bull/bear; 40.85→89.97; 100.82→227.81 ← `.bullish_days/.bearish_days/.iv_rank_change/.price_change` | 30 sessions |
| `uw historical signal-backtest --signal-type bearish_flow --lookback-days 5 --top-n 20 --json` | 87.5% / 8 / −2.73% ← `.win_rate/.total_signals/.avg_move_pct` | 8 signals |
| `fz quote NBIS --agent` | RSI 56.12; SMA200 +94.45%; 52W high 278.84 −18.30% ← `.fundamentals.*` | 1 |

All trailing tools anchor to the latest available date = **2026-06-05 = as-of**
(phase-0), so this run is as-of-correct; a re-run after new sessions land will
shift every trailing read.

## Tool errors

- `uw historical trend` first jq pass used phantom keys (`.trend/.series`) →
  empty arrays; schema inspected (`keys`), re-read via `.daily_data` /
  top-level fields. No values transcribed from the bad parse.
- `daily_data` in `trend`/`oi-trend` is most-recent-first; the `[-5:]` slice in
  the first read returned the oldest rows — values quoted here come from the
  top-level summary fields and the correctly-ordered re-read.

## DATA NOTE / CORRECTION

- "1y" IV percentile is actually over 39 sessions; "30d/90d" windows cross the
  21-session hole (03-28→04-24) — all Ns quoted are actual session counts.
- GEX-series spot (227.19) vs screener close (227.81) differ ~0.3% — different
  snapshot moments within the same EOD file family; both quoted with source.

## Verdict for downstream phases

- **Volatility regime:** rich in level (97th pctile) but **cheap vs realized**
  (VRP −0.084) → **premium-BUYING environment; favor debit structures, avoid
  naked short vol** despite the 90 IV rank.
- **Premium-buying vs selling:** PREMIUM_BUYING (tool label, quoted).
- **Conviction today's signal is historically edge-positive:** 3/5 — the
  bearish_flow base rate is strong (87.5%) but N=8 and in-sample; the GEX flip
  + 30-day OI build are corroborating regime facts, not directional edge.
- **Three specific datapoints:** IV %ile **97.44** (39 sessions); VRP
  **−0.0841**; bearish_flow win rate **87.5% (N=8, market-wide, in-sample)**.
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:     bearish_flow
  signal_backtest_win_rate: 0.875
  win_rate_n:       8
  win_rate_source:  backtest
  ```
- **Open questions:** What catalyst broke the parabola on 06-03→06-05 and is
  it resolved (phase-6)? Is the 22.43% short float (phase-0) fuel for a
  squeeze-back given dealers must buy on rising IV (phase-4 vanna), or
  confirmation of the bear case (phase-7c)? Does the AI-infra complex weakness
  (phase-0.5 sector table) persist (phase-6)?
