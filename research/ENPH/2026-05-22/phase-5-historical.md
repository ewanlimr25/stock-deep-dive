# Phase 5 — Historical Context & VRP

**Ticker:** ENPH
**As-of date:** 2026-05-22
**Generated:** 2026-05-25T22:43:20Z
**Upstream phases cited:** phase-0.5-context.md, phase-3-positioning.md, phase-4-structure.md

## Summary

The decisive context: **ENPH has already DOUBLED — ~$30.77 (4/29 low) → $63.93
(5/22) in ~3.5 weeks** — and today's bullish flow is piling into a stock at the **100th
IV percentile (z +2.6, regime HIGH_IV)**. The crucial nuance is **VRP is FAIR
(IV30 101% vs realized 100%, vrp +0.012)** — the options are *not* overpriced relative
to how violently ENPH actually moves (~6%/day), so there is **no clean vol-selling edge**;
naked premium-selling is dangerous and naked premium-buying isn't cheap → **defined-risk
spreads are the only structurally-sound expression.** Bullish flow is genuine and
relentless (16 of last 20 sessions bullish, **+$30.4M cumulative net premium, OI
BUILDING 20 consecutive sessions, +257,685 contracts**), and sentiment is **NOT extreme
(P/C z −0.47, NORMAL)** — so this isn't a blow-off top on positioning. But the **price
move itself is extended**, dealers are in a **stable, strengthening long-gamma regime
(7 sessions, pin $60–65)**, and the easy money ($30→$64) is banked. Net: the signal is
edge-positive *only with a fresh catalyst* to break $65; without one, mean-reversion
risk is high. **Conviction that today's setup is forward-edge-positive: 3/5.**

> **Gap note (mandatory):** the snapshot window is non-contiguous — 21-session hole
> 2026-03-28→04-24. The "252d"/"90d" tools actually had only **30–31 sessions**; treat
> all "1-year"/"90-day" figures as **~31-session** reads. The IV percentile/z-score below
> is over **30 sessions**, not a true year.

## Key signals

- **ENPH doubled $30.77 (4/29) → $63.93 (5/22)** — the move is largely banked [HIST:gex_time_series]
- **IV percentile 100, z +2.6, HIGH_IV** — but over 30 sessions, not 1y [HIST:iv_percentile_zscore]
- **VRP FAIR: IV30 101% ≈ realized 100% (vrp +0.012)** — no vol-selling edge; stock truly moves [HIST:vrp]
- **Cumulative net premium +$30.4M (31 sessions), BULLISH; OI building 20 straight days** [HIST:cumulative_premium_flow, HIST:oi_trend]
- **P/C z −0.47 → NOT a sentiment extreme** (bullishness is normal-for-recent-ENPH) [HIST:pc_ratio_zscore]
- **Long-gamma regime stable 7 sessions and strengthening** (last flip 5/13) [HIST:gex_time_series]

## Detailed findings

### IV regime (percentile + z-score + VRP)

`current_iv30d 1.0129`, `iv_percentile 100`, `iv_zscore 2.617`, `regime HIGH_IV`
(over **30 sessions**). IV is at the very top of its available range. **But VRP is FAIR**:
`iv30d 1.0129` vs `realised_vol 1.0013` → `vrp +0.0115`. ENPH has been *realizing*
~100% annualized vol (it doubled in a month) — so the rich IV is **earned, not a
mispricing.** Implication, correcting phase-4's "sell vol" lean: vol is rich on a
*rank* basis but *fair vs realized* → **sell vol only inside defined-risk spreads**, never
naked; the trade's edge must come from **direction**, not from harvesting VRP.

### Cumulative premium flow (≈31-session)

`cumulative_bullish $181.3M` vs `cumulative_bearish $151.0M` → **net +$30.4M, trend
BULLISH**. Persistent net-bullish accretion across the whole available window —
stealth-to-overt institutional build (corroborates phase-2 accumulation).

### P/C ratio z-score (sentiment)

`current_pc 0.392`, `mean 0.502`, `std 0.236`, **z −0.467, extreme NORMAL.** Today's
call-skew is only mildly below its 20-session mean — **no sentiment blow-off.** We are
not fading an exhausted positioning extreme; the bullishness is the regime, not a spike.

### GEX time series — the doubling, and the regime

Spot trajectory (45-DTE GEX series): $45.66 (3/16) → $37.64 (3/27) → **$30.77 (4/29,
bottom, FULLY_NEGATIVE −5.6M GEX)** → $33.9 (5/1) → $36.2 (5/8) → $42.1 (5/13) →
$47.7 (5/14) → $52.9 (5/15) → $62.1 (5/21) → **$63.93 (5/22)**. ENPH **doubled** off the
late-April low. The bottom printed in **short-gamma (FULLY_NEGATIVE)** — trend
amplification fuel — exactly what powered the rip. **Last regime flip 5/13
(NEGATIVE→POSITIVE)**; since then **7 sessions of stable, strengthening POSITIVE GEX**
(now +11.5M, series high). So the tape has transitioned from short-gamma momentum to
**long-gamma pin** — structurally, the explosive phase is maturing into range-bound.

### OI trend — relentless build

`consecutive_build_days 20`, `overall_trend BUILDING`, `total_net_oi_change +257,685`.
OI rose every session for 20 days. Notable structural footprint: on **5/18** a large
**2027-06 complex** was opened — **$70C +12,334 and $45P +12,308** (~equal size) — and
today's **$2.5M 2027-06 $60P** (phase-1) adds to that same expiry. This looks like a big
institutional **long-dated structured position** (strangle/collar around a stock book),
not a directional day-trade — consistent with phase-2's accumulation + phase-3's hedge.

### Multi-day trend table (selected, [HIST:trend], 20 sessions, 16 bull / 4 bear)

| Date | Close | net_flow ($) | IV rank | P/C | dir |
|------|-------|--------------|---------|-----|-----|
| 05-22 | 64.03 | +5.55M | 92.1 | 0.39 | bull |
| 05-21 | 62.34 | +7.45M | 90.2 | 0.29 | bull |
| 05-20 | 53.15 | +5.35M | 75.7 | 0.41 | bull |
| 05-19 | 46.83 | +2.06M | 58.2 | 0.63 | bull |
| 05-18 | 49.69 | −5.53M | 66.3 | 0.48 | bear |
| 05-15 | 52.94 | +5.55M | 85.0 | 0.27 | bull |
| 05-14 | 48.01 | +3.63M | 61.8 | 0.25 | bull |
| 04-27 | 35.24 | −0.72M | 72.0 | 0.35 | bear |

Close +82% over the table; IV rank climbed 72→92 alongside. Persistent bullish flow
throughout the doubling.

### Signal backtest — current signal's historical edge

`signal_type bullish_flow`, `lookback_days 20`, **`win_rate 100.0%`, `total_signals 8`,
`avg_move_pct +4.62%`.** **Heavily caveated:** (1) it is **market-wide** (AMD/SPY/MU/
SNDK/PANW/IWM/AMZN — semis & index), **not ENPH-specific**; (2) **n=8 (<10) — low
confidence**; (3) signals are dated 5/19–5/20, so the "20-day forward" is recent and the
sample sits inside a **broad bull-regime up-move** (100% up is a regime artifact, not a
durable edge). Surfaced for the sizing handoff, but phase-9 should apply the
N-conditional cap and **lean on the conviction bin**, not this number.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `historical_iv_percentile_zscore` | `{symbol: ENPH, lookback_days: 252}` | %ile 100, z +2.6, HIGH_IV (30 sessions used) |
| `historical_vrp` | `{symbol: ENPH, realised_window_days: 30, date: 2026-05-22}` | vrp +0.012, FAIR (IV 101% ≈ RV 100%) |
| `historical_cumulative_premium_flow` | `{symbol: ENPH, days: 90}` | net +$30.4M, BULLISH (31 sessions) |
| `historical_pc_ratio_zscore` | `{symbol: ENPH, lookback_days: 20}` | z −0.47, NORMAL (no extreme) |
| `historical_gex_time_series` | `{symbol: ENPH, days: 30, dte_max: 45}` | doubled off $30.77; long-γ stable since 5/13 |
| `historical_trend` | `{symbol: ENPH, days: 20}` | 16 bull/4 bear; close 35→64; IV rank 72→92 |
| `historical_oi_trend` | `{symbol: ENPH, days: 20, top_n: 10}` | 20 consecutive build days; +257,685; 2027-06 complex |
| `historical_signal_backtest` | `{signal_type: bullish_flow, lookback_days: 20, top_n: 20}` | win 100%, n=8 (market-wide, caveated) |

## Tool errors

None. (Data-quality caveat: all multi-week windows are truncated by the 03-28→04-24 gap
to ~30–31 sessions — surfaced inline, not an error.)

## Verdict for downstream phases

- **Volatility regime:** **RICH by rank (IV %ile 100) but FAIR vs realized (VRP ~0)** →
  **defined-risk only**; no naked-vol edge in either direction.
- **Premium environment:** persistent bullish-premium *buying* environment, but into a
  **doubled, extended price** at peak IV — the asymmetric easy money is behind us.
- **Conviction today's signal is HISTORICALLY EDGE-POSITIVE: 3/5** — flow is real and
  persistent, but the move is extended, vol is at the ceiling, and dealers now pin
  ($60–65). Needs a fresh catalyst to extend (→ phase 6/7c).
- **Three specific data points:** IV %ile **100** (z +2.6); VRP **+0.012 (FAIR, RV ~100%)**;
  signal win-rate **100% (n=8, unreliable)**.
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:              bullish_flow
  signal_backtest_win_rate:  1.00
  win_rate_n:                8
  win_rate_source:           backtest
  # CAVEAT: market-wide (not ENPH), n<10, bull-regime artifact →
  # phase-9 apply N-conditional cap; prefer conviction bin.
  ```
- **Open questions:**
  - Is there a fresh catalyst to justify chasing a doubled stock through the $65 gamma
    wall, or is this late-cycle FOMO? (→ phase 6 macro / phase 7c sentiment)
  - The 2027-06 70C/45P/60P complex — protective collar on a long, or a vol play? (→ phase 8b)
