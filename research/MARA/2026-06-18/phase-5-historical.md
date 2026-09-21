# Phase 5 — Historical Context & VRP

**Ticker:** MARA
**As-of date:** 2026-06-18 (trailing tools anchor to latest available = 2026-06-18 = as-of ✓ reproducible)
**Generated:** 2026-06-19
**Upstream phases cited:** phase-0-intake.md (gap), phase-1-flow.md, phase-4-structure.md

## Summary

History confirms the structural read and adds one important vol nuance. **GEX regime
had ZERO flips in 30 sessions — persistently POSITIVE / long-gamma** the entire window
→ the range-bound mean-reversion pin (phase-4) is **durable, not a one-day artifact.**
The vol setup is two-sided: **IV30d 79.7% sits at the 4.17th percentile of MARA's own
1-year range (LOW_IV)** — cheap *for this name* — yet **VRP is +6.3% (IV > realized →
premium-selling favored on carry).** So premium sellers have positive carry but are
short vol near 1-year lows (limited cushion if a BTC move re-expands IV). 90-day
cumulative flow is **MIXED** (net −$2.8M on ~$312M each side — balanced, no stealth
build), and the bearish_flow signal class backtests 85.7% **but on only N=7** (small,
market-wide). Net: a **premium-selling / range environment** with a *mild* recent
bearish flow tilt, not a high-conviction directional edge.

## Key signals

- **GEX regime: POSITIVE for all 30 days, `regime_flip_dates: null`** → stable
  long-gamma pin `[HIST:gex-time-series]`.
- **IV percentile 4.17 (LOW_IV)**, iv_zscore −1.24, over **48 gap-aware sessions** —
  IV cheap by MARA's own range `[HIST:iv-percentile-zscore]`.
- **VRP +6.3%** (IV30 79.7% vs RV30 73.4%) → **PREMIUM_SELLING** regime on carry
  `[HIST:vrp]`.
- **90d cumulative flow MIXED**, net −$2.79M (bear $314.3M vs bull $311.5M) → no
  directional campaign `[HIST:cumulative-premium-flow]`.
- **bearish_flow backtest: win 85.7%, N=7, avg move −15.58%** — market-wide base
  rate, small N `[HIST:signal-backtest]`.

## Detailed findings

### IV regime (percentile + z-score + VRP)

| Metric | Value | Read |
|--------|-------|------|
| current_iv30d | 0.7969 (79.7%) | — |
| iv_percentile (252d) | **4.17** | bottom 4% of 1y range → IV cheap *for MARA* |
| iv_zscore | −1.238 | below mean |
| regime | **LOW_IV** | — |
| dates_used | **48** | gap-aware N (not 252 calendar days) |
| realised_vol (30d) | 0.7339 (73.4%) | — |
| **VRP** | **+0.063 (+6.3%)** | IV > RV → **PREMIUM_SELLING** favored on carry |

**The nuance for phase-9:** carry favors *selling* (VRP+), but the *level* is at 1y
lows → selling vol here has limited downside cushion and asymmetric upside risk if a
BTC catalyst spikes IV. A long-vol / debit structure is correspondingly *cheap*.

### Cumulative premium flow (90d)

- cumulative_bullish $311.5M vs cumulative_bearish $314.3M → **net_flow −$2.79M**,
  `trend_direction` **MIXED**. Essentially balanced over the quarter — **no stealth
  institutional directional build**, consistent with phase-0.5 BUSY_NAME and phase-3's
  small standing footprint.

### P/C ratio z-score (sentiment extreme?)

- current_pc_ratio 0.1276, mean 0.4258, std 0.1832, **zscore −1.627**, `extreme` =
  **NORMAL**. Today is call-heavy vs MARA's 20-day norm (−1.6σ) but **not an extreme**
  (|z|<2) → no contrarian sentiment trigger.

### GEX time series (regime stability)

- `days_analyzed` 30, **`regime_flip_dates: null`** — POSITIVE every session
  (trajectory: 05-07 POSITIVE … 06-18 POSITIVE), ZGL low ($2.0–$4.5) throughout.
  **The long-gamma range regime has held for a full month** → high confidence the
  phase-4 pin is structural, not transient.

### OI trend (30d build history)

- Net OI **building** most days (06-18: 268 increases vs 124 decreases, +14,656 net).
  The dominant build was **06-15: +135,416 net** — that's when the giant **6/18 0DTE
  call wall** was created ($15C +39,119, $16C +38,816, $15.5C +16,845, $14.5C
  +15,895). The 0DTE pin wall was a 3-days-before-expiry construction, now expiring.
- Builds are **two-sided** across days (e.g. 06-17: $17C +4,463 *and* $14P +4,146,
  $14.5P +4,025) → straddle/strangle-style, **not directional accumulation** —
  reinforces MIXED.

### Multi-day trend (30 sessions, 2026-05-07 → 2026-06-18 — post-gap, clean)

- price **$12.70 → $14.22 (+12%)**; bullish_days **17** / bearish_days **13** (choppy);
  iv_rank **39.4 → 30.3** (declining). `flow_direction_latest` = **bearish**.
- Last 8 sessions flow: 6/18 bear, 6/17 bear, 6/16 bull, 6/15 bull, 6/12 bull, 6/11
  bull, 6/10 bear, 6/9 bear → **alternating, no persistence**; last 2 days bearish.

### Price context (`fz`, advisory cross-check)

- RSI(14) **55.7** (neutral — not overbought) `[HIST:rsi fz]`.
- Price **+12.6% > SMA50, +13.4% > SMA200** (uptrend intact).
- 52W High **$23.45 → −39.4% below**; 52W Low **$6.66 → +113.5% above** → **mid-range**,
  well off the highs, far above the lows `[HIST:52w_proximity fz]`.
- Perf YTD **+58.35%**; analyst Target **$17.70 (+24% vs $14.22)** — room to target,
  but near-term capped by the $14.5/$15 gamma walls (phase-4).

### Signal backtest (Kelly `p` input)

- **`bearish_flow`** (matches phase-1's net-bearish flow verdict): **win_rate 85.7%,
  total_signals 7, avg_move_pct −15.58%.** Market-wide base rate; **N=7 < 10 →
  low-confidence**; re-confirmed populated (not the empty stub).
- `dark_pool_accumulation` (phase-2's signal): **0 firings** (re-ran once per rubric;
  still `total_signals 0`) → `win_rate_source=null` for that class.
- **Caveat:** MARA's actual setup is **range-bound/capped (premium-selling)**, which
  the directional `bearish_flow` class only loosely proxies — phase-9 should treat
  p=0.857 as a weak, small-N directional reference, not a literal edge.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|------------------|--------------------------|-----------|
| `historical iv-percentile-zscore --symbol MARA --lookback-days 252` | iv_pctile 4.17, LOW_IV, dates_used 48 ← `.iv_percentile,.regime,.dates_used` | 48 sess |
| `historical vrp --symbol MARA --realised-window-days 30` | vrp +0.063, PREMIUM_SELLING ← `.vrp,.regime` | 1 |
| `historical cumulative-premium-flow --symbol MARA --days 90` | net −2.79M, MIXED ← `.net_flow,.trend_direction` | 90d |
| `historical pc-ratio-zscore --symbol MARA --lookback-days 20` | z −1.627, NORMAL ← `.zscore,.extreme` | 20 |
| `historical gex-time-series --symbol MARA --days 30 --dte-max 45` | regime_flip_dates null, all POSITIVE ← `.regime_flip_dates,.trajectory[]` | 30 |
| `historical oi-trend --symbol MARA --days 30 --top-n 10` | 6/15 +135,416 build day ← `.daily_data[].net_oi_change` | 30 |
| `historical trend --symbol MARA --days 30` | +12%, 17/13, ivr 39→30, latest bearish ← `.price_change,.bullish_days,.flow_direction_latest` | 30 |
| `historical signal-backtest --signal-type bearish_flow --lookback-days 5` | win 85.7%, N=7 ← `.win_rate,.total_signals` | mkt-wide |
| `historical signal-backtest --signal-type dark_pool_accumulation` (×2) | N=0 ← `.total_signals` | 0 |
| `fz quote MARA --agent` | RSI 55.7, 52wH −39.4%, target $17.70 ← `.fundamentals.*` | 1 |

## Tool errors

(none — all reads valid JSON. `dark_pool_accumulation` N=0 re-confirmed on a second
call per the rubric. Gap note: `iv-percentile-zscore` `dates_used`=48 and `trend`
`days_analyzed`=30 are the **actual session counts**; the 30d trend window
(05-07→06-18) sits *after* the 03-28→04-24 hole, so it does not cross the gap.)

## Verdict for downstream phases

- **Volatility regime:** **cheap by level, rich by carry** — IV30 at the **4.17th
  percentile** of its 1y range (cheap for MARA) yet **VRP +6.3%** (richer than
  realized → premium-selling favored). Net: **PREMIUM-SELLING environment with a thin
  vol cushion.**
- **Premium-buying vs selling:** **SELLING** on carry (favors phase-1's overwriters /
  credit structures) — but note the level caveat makes cheap *long*-vol a viable
  contrarian hedge.
- **Conviction that today's signal is HISTORICALLY EDGE-POSITIVE:** **3/5.** The
  long-gamma range regime is stable (30d, no flips) and VRP supports a credit/range
  trade; but the directional bearish_flow backtest is tiny-N, 90d flow is MIXED, and
  IV at lows caps the seller's edge. Moderate, not strong.
- **Three datapoints:** IV %ile **4.17**; VRP **+0.063 (+6.3%)**; signal win rate
  **85.7% (N=7, bearish_flow, market-wide)**.
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:               bearish_flow
  signal_backtest_win_rate:   0.857
  win_rate_n:                 7
  win_rate_source:            backtest
  ```
  ⚠ N=7 → apply the N-conditional Kelly cap (`rubrics/sizing-rubric.md`); the class is
  a *loose* proxy for MARA's actual range/premium-selling setup — do not size as a
  clean directional short.
- **Open questions:**
  - With IV at the 4th percentile, is the overwriting edge (VRP+) real or is vol
    about to mean-revert *up* (a BTC catalyst would hurt the sellers)? → phase-6 macro
    / phase-7c sentiment.
  - The stable 30d long-gamma pin assumes no large BTC move — what's the catalyst
    calendar (phase-6) and is β 5.35 a tail-risk to the range thesis?
