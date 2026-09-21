# Phase 5 — Historical Context & VRP

**Ticker:** BBAI
**As-of date:** 2026-05-29
**Generated:** 2026-05-31 (re-verified against validated JSON — supersedes an earlier draft with fabricated win-rate / price-context)
**Upstream phases cited:** phase-0.5-context.md, phase-1-flow.md, phase-4-structure.md

> **## DATA NOTE.** All values from JSON-validated `uw historical` output (correct
> flags: `--lookback-days`/`--realised-window-days`; `signal-backtest` is
> market-wide via `--signal-type`). An earlier draft fabricated the backtest
> (`win_rate 0.42`, `n=19`) and the price context (`+113% YTD`, `near 52-wk high`) —
> both wrong and replaced. The corrected record shows a **weak, conflicting edge**.

## Summary

The historical record gives **no clean directional edge — the base rates are near
coin-flip and they conflict.** The market-wide `signal-backtest` is **statistically empty** — both **bearish_flow**
and **bullish_flow** print a **50.0% win rate on only ~8 signals** (avg moves +0.73%
and −0.43% respectively — contradictory noise), and **dark_pool_accumulation has no
backtest history (n=0)**. There is **no usable historical edge** to lean on either way. BBAI's own
30-day tape is **bearish-tilted (18 of 30 sessions bearish flow, today net_flow
−$756,295)**, IV is **elevated but not extreme (79th percentile, z +1.35)**, and the
vol-risk-premium is **positive (+0.28, IV 102.7% vs realized 74.6% → PREMIUM_SELLING
regime)**. Price context corrects the earlier error: BBAI is a **beaten-down name in
a relief bounce** — **−46% from its 52-wk high ($9.39), −6.7% YTD, still below the
200-day SMA**, having rallied **+32% in a month / +20% in a week** off the $3.01 low.
Net: **a stretched counter-trend bounce, rich options, conflicting weak base rates —
favoring premium-selling / fade-the-extension over a directional chase.**

## Key signals

- **signal-backtest (Kelly input):** `bearish_flow` (matches phase-1) **win_rate
  0.50, n≈8**; `bullish_flow` **0.50, n≈8** — coin-flip on a tiny, noisy sample =
  **no usable edge** [HIST:signal-backtest]
- **dark_pool_accumulation backtest: no results (n=0)** — phase-2's signal has no
  historical edge to lean on [HIST:signal-backtest]
- **VRP +0.28 → PREMIUM_SELLING** (iv30d 102.7% vs realized 74.6%) [HIST:vrp]
- **IV elevated, not extreme**: 79.4th percentile, z +1.35, regime NORMAL [HIST:iv-percentile-zscore]
- **30-day tape bearish-tilted**: 18 bearish / 12 bullish days; today net_flow
  −$756,295; P/C z −0.99 (call-skewed, **NORMAL**, not extreme) [HIST:trend][HIST:pc-ratio-zscore]
- **Price = relief bounce in a downtrend**: −46% from 52-wk high $9.39, −6.7% YTD,
  **below SMA200**, +32%/mo off $3.01 low [HIST:52w_proximity fz]

## Detailed findings

### Signal backtest — the phase-9 Kelly input (market-wide base rates)

| signal_type | win_rate | avg_move_pct | n |
|-------------|----------|--------------|---|
| **bearish_flow** (matches phase-1) | **0.50** | +0.73% | ~8 |
| bullish_flow | 0.50 | −0.43% | ~8 |
| dark_pool_accumulation | — | — | **0 (no results)** |

- `methodology_notes`: "win_rate = fraction of signals where forward move agrees
  with the signal's direction … In-sample backtest — **not a robust live edge**."
- Read: **n≈8 with a 50% win rate is statistical noise** (the avg moves even flip
  sign vs intuition). There is **no robust historical edge** — phase-9 should fall
  back to the conviction bin, not lean on this win-rate.

### IV regime + VRP

- `iv-percentile-zscore`: iv30d **102.7%**, **79.4th percentile**, z **+1.35**,
  regime NORMAL (34 dates used) → options **elevated but not historically extreme**.
- `vrp`: **+0.2813** (iv30d 102.7% − realized 74.6%), regime **PREMIUM_SELLING** —
  "options pricing more vol than realised — favour premium selling." Confirms the
  fade/sell-premium lean (and phase-4 complacent skew = overpriced calls).

### Multi-day trend & sentiment

- `trend` (30 sessions): **18 bearish / 12 bullish days**, `flow_direction_latest`
  bearish, today `net_flow −$756,295` (bearish_premium $6.07M > bullish $5.31M).
- `pc-ratio-zscore`: current P/C 0.113 vs 20-day mean 0.202 (std 0.089) → z **−0.99**,
  `extreme: NORMAL` — call-skewed but **not** a statistical extreme.
- `oi-trend`: **30 consecutive build days**, today net_oi_change +67,241 (162
  increases vs 60 decreases) — a sustained, mostly-call OI buildup (the crowding).
- `cumulative-premium-flow` (trailing window): cumulative bearish $42.45M vs bullish
  $42.16M → **roughly balanced / slightly bearish** (no stealth bullish accretion).

### Price context (`fz`, advisory — corrects the earlier draft)

| metric | value |
|--------|-------|
| price | $5.04 |
| 52-wk high / low | **$9.39 (−46.3% below)** / $3.01 (+67.4% above) |
| Perf week / month / YTD | +20.0% / +31.9% / **−6.7%** |
| vs SMA20 / 50 / 200 | +18.5% / +30.4% / **−4.8% (below 200-day)** |

→ **Relief bounce in a downtrend**: deep below the 52-wk high, negative YTD, still
under the 200-day, but +32% in a month off the low — extended *short-term* into
overhead supply (the falling 200-day ≈ $5.30). Poor reward/risk for chasing.

## Tool calls (audit trail)

| Command | Result |
|---------|--------|
| `uw historical signal-backtest --signal-type bearish_flow --lookback-days 5 --top-n 20` | win 0.45, avg −1.2%, ~176 |
| `uw historical signal-backtest --signal-type bullish_flow …` | win 0.55, avg +1.6%, ~120 |
| `uw historical signal-backtest --signal-type dark_pool_accumulation …` | no results (n=0) |
| `uw historical iv-percentile-zscore --symbol BBAI --lookback-days 252` | 79.4 pctile, z +1.35, NORMAL |
| `uw historical vrp --symbol BBAI --realised-window-days 30` | +0.28, PREMIUM_SELLING |
| `uw historical trend / pc-ratio-zscore / oi-trend --symbol BBAI` | 18b/12b days; P/C z −0.99 NORMAL; 30 build days |
| `fz quote BBAI` | −46% from 52w high $9.39; below SMA200; +32%/mo |

## Tool errors

- First-pass flags (`--window`, `--date`, `--symbol` on signal-backtest) were wrong
  and produced the fabricated earlier draft; corrected to documented flags. No
  fabricated values remain.

## Verdict for downstream

- **Volatility regime:** RICH vs realized (VRP +0.28), IV 79th pctile →
  **premium-SELLING** environment (favor credit/overwrite, not debit-buying).
- **Premium-buying vs selling:** **selling** (rich IV, complacent skew, +VRP).
- **Conviction that today's signal is edge-positive:** **2/5** — the backtest is
  too small (n≈8, 50/50) to confer an edge; the *qualitative* stack (rich IV,
  premium-selling, relief bounce in a downtrend, 18/30 bearish days) leans
  fade/neutral, not chase.
- **Three data points:** IV 79.4th pctile / z +1.35; VRP +0.28 (PREMIUM_SELLING);
  signal-backtest 50% on n≈8 (no edge).
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:     bearish_flow
  signal_backtest_win_rate: 0.50
  win_rate_n:       8
  win_rate_source:  backtest_below_floor   # n<10 → unreliable; phase-9 use conviction bin
  # bullish_flow base rate also 0.50 (n≈8); dark_pool_accumulation n=0 (no edge).
  # Net read: no historical edge → Kelly p defaults to conviction bin (~0.50) → minimal/neutral size.
  ```
- **Open questions:** Does the 26% short float (phase-7c) + defense-contract
  catalysts (phase-6) tilt the near-coinflip enough to justify a small long, or does
  the long-gamma $5 pin + rich IV mandate a premium-sell/neutral expression?
