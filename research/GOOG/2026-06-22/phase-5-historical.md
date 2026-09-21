# Phase 5 — Historical Context & VRP

**Ticker:** GOOG
**As-of date:** 2026-06-22
**Generated:** 2026-06-22
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md (DP supply $362–371 = 06-18 close $367.46), phase-4-structure.md (today short-gamma)

## Summary

Today's constructive micro-signals (phase-2 mega-tier DP accumulation, phase-3 upside
call OI) are firing into a **bearish multi-week context at a fresh low** — the single
most important framing this run. GOOG has fallen **$396.99 → $348.78 (−12.1%) over the
last 30 sessions** (18 bearish flow-days vs 12 bullish), and **$348.31 is a fresh 30-day
low**. fz confirms: **−9.38% on the month**, below the 20-day (−4.98%) and 50-day
(−4.51%) MAs, RSI **39.99** (weak, not yet oversold) — though still **+12.07% above the
200-day** and **+11.15% YTD** (long-term uptrend intact, sharp short-term pullback,
−13.77% off the 52-wk high $404.47). **Critically, today is the FIRST flip from
long-gamma to short-gamma in the 30-day GEX series** — `regime` was `POSITIVE` for **21
straight sessions (05-08 → 06-18)** and turned **`FULLY_NEGATIVE` on 06-22** at the lows;
the tool notes regime flips "empirically precede realised-vol expansion." Layer on **rich
IV (85.7th 1-yr percentile, over 49 available sessions)**, a **FAIR VRP (+0.0107, IV≈
realised)**, a **coin-flip bullish_flow backtest (win_rate 50.0%, n=8)**, and
**dark_pool_accumulation backtest empty (null)** — and the honest read is: the dip-buy is
**historically edge-neutral at best**, into an expensive, freshly vol-expanding tape.
Conviction that today's signal is edge-positive: **2/5.**

## Key signals

- **Fresh 30-day LOW**: $396.99 → $348.78 (−12.1%, 30 sess); 18 bearish vs 12 bullish
  flow-days; latest flow bearish `[HIST:trend]`
- **Gamma regime just flipped POSITIVE → FULLY_NEGATIVE today** (21 long-γ sessions
  ended 06-22) → vol-expansion risk `[HIST:gex_time_series]`
- **IV rich**: 1-yr percentile **85.7** (z 0.855, n=49 sessions); **VRP FAIR +0.0107**
  (realised 31.69%, IV≈realised — no premium edge) `[HIST:iv_percentile]` `[HIST:vrp]`
- **bullish_flow backtest 50.0% (n=8)** = coin flip; **dark_pool_accumulation empty
  (null, re-run confirmed)** `[HIST:signal_backtest]`
- fz: RSI 39.99, below 20/50-DMA, −9.38% month, **above 200-DMA +12.07%**, YTD +11.15%
  `[HIST:rsi fz]` `[HIST:52w_proximity fz]`; OI **BUILDING 30 consecutive days**
  (+1.11M) `[HIST:oi_trend]`

## Detailed findings

### IV regime (percentile + z-score + VRP) `[HIST:iv_percentile]` `[HIST:vrp]`

- `iv_percentile` = **85.71** (1-yr), `iv_zscore` = 0.855 — IV is high on the trailing
  window, **but `dates_used` = 49**, not 252 (limited local history + the 03-28→04-24
  gap), so "1-yr percentile" is over **49 available sessions** — moderate confidence.
- `vrp` = **+0.0107**, `realised_vol` = **0.3169** (31.69%), `regime` = **FAIR** — tool:
  "IV close to realised — no clear edge from VRP alone." High-vol environment where IV is
  rich on a 1-yr basis but fairly priced vs *current* (elevated) realized.
- **Implication:** not a clean premium-buying *or* premium-selling regime. With IV rich
  + realized high + short-gamma vol-expansion ahead, **naked long premium is expensive**;
  favor defined-risk / spreads over outright debit (carried to phase-9 structure choice).

### Cumulative premium flow (90d) `[HIST:cumulative_premium_flow]`

`cumulative_bullish` $5.092B vs `cumulative_bearish` $4.933B → **net_flow +$159.97M**,
`trend_direction` = **MIXED**. Mildly net-bullish premium accretion over the window but
**not** the persistent ≥60-day stealth build that would signal high-confidence
directional accumulation. (Window crosses the 03-28→04-24 gap; the 90 calendar days
contain fewer actual sessions — `dates_covered` works back contiguously from 06-22.)

### P/C ratio z-score (sentiment) `[HIST:pc_ratio_zscore]`

`zscore` = **−0.924** (20-day lookback) — current P/C is ~0.9 SD *below* its 20-day mean
(call-leaning), consistent with phase-4's COMPLACENT skew, **but |z| < 2 → not a
contrarian extreme**. No sentiment-extreme fade signal.

### GEX time series (regime stability) `[HIST:gex_time_series]`

The headline. Spot path and regime over 30 sessions:

| Date | Spot | Regime | total_gex |
|------|------|--------|-----------|
| 2026-05-08 | 396.73 | POSITIVE | +146.8M |
| 2026-05-22 | 379.54 | POSITIVE | +23.9M |
| 2026-06-02 | 359.55 | POSITIVE | +8.7M |
| 2026-06-10 | 354.38 | POSITIVE | −1.1M (intraday dip) |
| 2026-06-16 | 370.84 | POSITIVE | +76.7M (bounce) |
| 2026-06-18 | 366.42 | POSITIVE | +68.2M |
| **2026-06-22** | **348.31** | **FULLY_NEGATIVE** | **−3.84M** |

GOOG held a **long-gamma (POSITIVE) regime for 21 consecutive sessions** while grinding
down from ~$397 → ~$366, then **flipped to short-gamma (FULLY_NEGATIVE) today** as it
broke to $348. `regime_flip_dates` = **null** — but that is the ZGL-crossing detector
(and the ZGL series is visibly coarse/buggy for GOOG: values like 76.81 / 286.57 when
spot is $350–396). The **regime *label* unambiguously flipped today**; treat it as a
fresh transition. Tool note: regime flips "empirically precede realised-vol expansion" →
**expect wider ranges**.

### OI trend `[HIST:oi_trend]`

`overall_trend` = **BUILDING**, `total_net_oi_change` = **+1,113,606**,
`consecutive_build_days` = **30**. OI has built for 30 straight sessions even as price
fell — growing engagement, not capitulation (per-day `daily_data` came back empty; only
the summary scalars populated — noted under Tool errors).

### Multi-day trend table `[HIST:trend]`

`days_analyzed` 30, `date_range` 2026-05-08 → 2026-06-22 (**post-gap, contiguous** — does
not cross the 03-28→04-24 hole). `price_change` **396.995 → 348.78**; `iv_rank_change`
**27.92 → 39.78** (IV rank *rose* as price fell); `bullish_days` 12 / `bearish_days` 18;
`flow_direction_latest` bearish. Notably **06-18 close was $367.46** (= phase-2's
heaviest DP cluster) with *bullish* flow — that was the last bounce high before a sharp
2-session **−5.1% drop to $348.78** (06-19 Juneteenth holiday between). The $362–371 DP
zone is the failed-bounce supply now overhead.

### Price context (fz, advisory) `[HIST:rsi fz]` `[HIST:52w_proximity fz]`

RSI(14) **39.99**; price vs SMA20 **−4.98%**, SMA50 **−4.51%**, SMA200 **+12.07%**; Perf
Week −2.62%, Month −9.38%, YTD **+11.15%**; 52W High $404.47 (**−13.77%**), 52W Low
$163.33 (+113.54%). **Short-term downtrend inside an intact long-term uptrend.** RSI ~40
is weak but **not** oversold (<30) — no mechanical mean-reversion trigger yet. Tempers any
"clean breakout/bottom" thesis: this is a pullback that has not yet found a momentum floor.

### Signal backtest (Kelly p) `[HIST:signal_backtest]`

- `bullish_flow`: **win_rate 50.0%, total_signals 8** — market-wide base rate of the
  bullish-flow signal class over the last 5 days; a coin flip on small N.
- `dark_pool_accumulation`: **`{total_signals:0, "no backtest results"}` — re-run once,
  still empty → win_rate_source null** for that class.
- Using **bullish_flow (0.50, n=8)** as the empirical Kelly `p`; it is a **market-wide
  base rate, not GOOG-specific**, and N is small → phase-9 must apply the N-conditional
  cap (`rubrics/sizing-rubric.md`).

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← path | Rows / N |
|------------------|--------------------|----------|
| `uw historical iv-percentile-zscore --symbol GOOG --lookback-days 252 --json` | iv_pct 85.71, z 0.855, dates_used 49 ← `.iv_percentile` | 49 sess |
| `uw historical vrp --symbol GOOG --realised-window-days 30 --json` | vrp +0.0107, realised 0.3169, FAIR ← `.vrp`/`.regime` | — |
| `uw historical cumulative-premium-flow --symbol GOOG --days 90 --json` | net_flow +159.97M, MIXED ← `.net_flow` | 90d |
| `uw historical pc-ratio-zscore --symbol GOOG --lookback-days 20 --json` | zscore −0.924 ← `.zscore` | 20d |
| `uw historical gex-time-series --symbol GOOG --days 30 --dte-max 45 --json` | flip POSITIVE→FULLY_NEGATIVE on 06-22 ← `.trajectory[].regime` | 30 sess |
| `uw historical oi-trend --symbol GOOG --days 30 --top-n 10 --json` | BUILDING, +1.11M, 30 consec ← `.overall_trend` | 30 sess |
| `uw historical trend --symbol GOOG --days 30 --json` | 396.995→348.78, 12 bull/18 bear ← `.price_change` | 30 sess |
| `uw historical signal-backtest --signal-type bullish_flow --lookback-days 5 --top-n 20 --json` | win_rate 50.0%, n=8 ← `.win_rate`/`.total_signals` | mkt-wide |
| `uw historical signal-backtest --signal-type dark_pool_accumulation …` (×2) | total_signals 0 (empty) ← `.note` | mkt-wide |
| `fz quote GOOG --agent` | RSI 39.99, SMA50 −4.51%, Perf Month −9.38% ← `.fundamentals` | EOD |

## Tool errors

- `uw historical signal-backtest --signal-type dark_pool_accumulation`: returned
  `{"total_signals":0,"note":"no backtest results"}` on **both** the first call and the
  re-run → recorded `win_rate_source=null` for that signal class (per phase guidance).
- `uw historical oi-trend`: summary scalars populated (BUILDING / +1.11M / 30 consec) but
  `daily_data` came back as `[]` — used the summary, did not fabricate per-day rows.
- `gex-time-series.regime_flip_dates` = null despite an obvious POSITIVE→FULLY_NEGATIVE
  label change; the ZGL series is coarse/implausible for GOOG (e.g. 286.57 vs spot ~$360).
  Reported the **regime-label** flip, not the (unusable) ZGL crossing.

## DATA NOTE / CORRECTION

No mis-read. Gap caveat applied: iv-percentile "252-day" = **49 actual sessions**;
90-day cumulative-premium crosses the 03-28→04-24 hole (fewer real sessions); the 30-day
`trend`/`gex` windows are **post-gap and contiguous** (05-08→06-22), so those are clean.

## Verdict for downstream phases

- **Volatility regime:** **RICH (1-yr) but FAIR vs realised** — IV 85.7th pct, VRP
  +0.0107. High-vol tape; long premium is expensive. **Premium-neutral**, leaning to
  defined-risk / spreads over outright debit, especially with short-gamma vol-expansion.
- **Premium environment:** neither clean buy nor sell — VRP FAIR. The edge is **not** in
  vol; it is (if anywhere) in direction, which is contested.
- **Conviction today's signal is HISTORICALLY EDGE-POSITIVE:** **2 / 5.** The
  constructive micro-signals fire against a 30-day downtrend, at a fresh low, into a
  freshly short-gamma (vol-expanding) regime, with a 50% (n=8) coin-flip backtest and no
  dark-pool-accumulation backtest support. Context is **risk-elevated, not edge-confirmed.**
- **Three specific datapoints:** IV percentile **85.7** (n=49); VRP **+0.0107 (FAIR)**;
  bullish_flow signal win rate **50.0% (n=8)**.
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:              bullish_flow
  signal_backtest_win_rate:  0.50
  win_rate_n:                8
  win_rate_source:           backtest        # market-wide base rate, NOT GOOG-specific; small N
  ```
- **Open questions:** Is today's mega-DP accumulation genuine institutional dip-buying at
  the $348 low, or knife-catching ahead of a short-gamma flush toward the $340 −GEX/put
  wall? Does macro (phase-6) explain the −12% mega-cap Comm/Tech derate (rotation to
  semis, per phase-0.5), and is it ongoing? Earnings 7/22 — does the recovery thesis need
  to survive to (and through) that catalyst, or resolve before it?
