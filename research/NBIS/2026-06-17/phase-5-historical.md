# Phase 5 — Historical Context & VRP

**Ticker:** NBIS (Nebius Group NV)
**As-of date:** 2026-06-17 (trailing tools latest-anchored to 2026-06-17)
**Generated:** 2026-06-18T00:42:01Z
**Upstream phases cited:** phase-1-flow.md, phase-3-positioning.md, phase-4-structure.md, phase-0.5-context.md

## Summary

History does **not** validate the bullish flow as edge-positive right now. Three findings dominate:
(1) **IV is HIGH but FAIR** — IV30d 113.1% sits at the 95.7th percentile (over the **47 sessions
actually present**, gap-aware), yet **VRP ≈ 0 (0.01, "FAIR")** because realized vol is 112.1% — the
stock genuinely moves this much, so the rich IV is justified, not a sell. (2) **The bullish_flow signal
class is historically EDGE-NEGATIVE** — market-wide signal-backtest win_rate **37.5% (N=8), avg forward
move −0.58%** (re-run confirmed, not a stub). Below the 0.45 floor → conviction downgrade. (3) **The
rally has been MIXED/two-sided, not a stealth build** — 90d cumulative premium flow nets only +$52.9M
on $9.4bn gross (MIXED), and the 30-day trend split is a perfect **15 bullish / 15 bearish days** even
as price ran $195→$281. OI is the one persistent positive: **BUILDING for 30 consecutive sessions
(+1.34M net OI)**. Price context (fz) is a flashing extension warning: **+127% above the 200-day, at
the 52-week high, +540% off the low**. Net: vol-neutral, edge-negative signal, parabolic extension →
**low historical conviction; size defensively.**

## Key signals

- **IV percentile 95.74 (HIGH_IV), z +1.16, but VRP 0.01 (FAIR)** — IV 113.1% ≈ realized 112.1%; no vol edge. [HIST:iv_percentile_zscore / vrp]
- **signal-backtest bullish_flow: win_rate 37.5%, N=8, avg_move −0.58%** — edge-NEGATIVE (the Kelly `p`). [HIST:signal_backtest]
- **90d cumulative flow MIXED:** +$52.9M net on $9.4bn gross (bull $4.752bn / bear $4.699bn). [HIST:cumulative_premium_flow]
- **30d trend: 15 bullish / 15 bearish days, price $195.09→$280.91** — two-sided rally. [HIST:trend]
- **OI BUILDING 30 consecutive days (+1,338,968 net)** — sustained engagement (two-sided). [HIST:oi_trend]
- **fz extension: RSI 68.6, +127% vs SMA200, at 52W high (+0.74%), YTD +235.6%.** [HIST:rsi fz / 52w_proximity fz]

## Detailed findings

### IV regime (percentile + z-score + VRP) [HIST:iv_percentile_zscore / vrp]

- current_iv30d **113.09%**, iv_percentile **95.74**, iv_zscore **+1.16**, regime **HIGH_IV**,
  dates_used **47** (the true N — a ~47-session percentile, NOT a clean 252-day year; gap-aware caveat).
- VRP: iv30d 113.09% − realised_vol **112.09%** = **vrp 0.01**, regime **FAIR** ("IV close to realised
  — no clear edge from VRP alone"). **The high IV is earned by high realized vol**, not a mispricing.

### Cumulative premium flow (90d / 48 sessions) [HIST:cumulative_premium_flow]

cumulative_bullish $4,752,049,032 vs cumulative_bearish $4,699,176,055 → **net_flow +$52,872,977**,
trend_direction **MIXED**. Net is 0.56% of gross — effectively balanced over the quarter. No persistent
stealth institutional build despite the price appreciation; the bid has been two-sided throughout.

### P/C ratio z-score (sentiment) [HIST:pc_ratio_zscore]

current_pc 0.8455, 20d mean 1.0033, std 0.256, **z −0.616, extreme NORMAL**. Today is mildly more
call-heavy than its 20-day norm but nowhere near an extreme — **no contrarian sentiment trigger**.

### GEX time series (30d regime stability) [HIST:gex_time_series]

**Whippy regime.** Flips: **06-12 POSITIVE→NEGATIVE** (spot 234.49), **06-15 NEGATIVE→POSITIVE** (spot
259.89); trajectory bounced POS/NEG/POS through 06-08→06-14, then **POSITIVE for the last 3 sessions
(06-15/16/17)**. The tool note: flips "empirically precede realised-vol expansion" — consistent with
the parabolic run. Currently stabilized positive (matches phase-4), but the recent instability lowers
confidence in regime persistence.

### OI trend (30d) [HIST:oi_trend]

overall_trend **BUILDING**, consecutive_build_days **30**, total_net_oi_change **+1,338,968**. OI has
grown every session for 30 days — sustained engagement. Two-sided (matches the barbell in phase-3),
so "building" ≠ "directional"; it confirms rising interest, not rising bullish conviction specifically.

### Multi-day trend table (recent 8) [HIST:trend]

| Date | Close | IV rank | PCR | Flow |
|------|-------|---------|-----|------|
| 2026-06-17 | $280.91 | 91.3 | 0.85 | bullish |
| 2026-06-16 | $265.10 | 85.2 | 1.21 | bearish |
| 2026-06-15 | $260.07 | 83.8 | 1.16 | bullish |
| 2026-06-12 | $232.36 | 83.5 | 0.55 | bearish |
| 2026-06-11 | $222.24 | 87.5 | 1.22 | bullish |
| 2026-06-10 | $211.69 | 94.8 | 0.82 | bullish |
| 2026-06-09 | $220.12 | 87.5 | 0.84 | bullish |
| 2026-06-08 | $218.00 | 91.3 | 0.82 | bearish |

+29% in 7 sessions ($218→$280.91) with flow alternating bull/bear; IV rank persistently 83–95. Summary:
days_analyzed 30, range 2026-05-06→06-17, bullish_days 15 / bearish_days 15, price_change 195.09→280.91,
iv_rank_change 86.6→91.3, flow_direction_latest bullish.

### Price context (fz, advisory cross-check) [HIST:rsi fz / 52w_proximity fz]

RSI(14) **68.57** (elevated, sub-70), price vs **SMA20 +20.17% / SMA50 +44.83% / SMA200 +126.65%**,
**Perf YTD +235.60%**, **52W High 278.84 → now +0.74% above it**, 52W Low 43.89 (+540%). Independent EOD
read: the name is **parabolically extended at new highs** — a strong mean-reversion/exhaustion flag that
tempers any breakout-continuation thesis. (Advisory; not in the Kelly `p`.)

### Signal backtest (current signal's historical edge) [HIST:signal_backtest]

`--signal-type bullish_flow --lookback-days 5` (market-wide): **win_rate 37.5%, total_signals 8,
avg_move_pct −0.58%**, note null. **Re-run once — identical** (not the empty stub). win_rate < 0.45 ⇒
heuristic: "today's setup has historically lost → downgrade conviction even if today's signals look
strong." N=8 is small (low confidence) and market-wide (a signal-class base rate, NOT NBIS-specific).

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← path | N / rows |
|------------------|--------------------|----------|
| `uw historical iv-percentile-zscore --symbol NBIS --lookback-days 252` | iv_pctile 95.74, z +1.16, iv30d 113.1%, dates_used 47, HIGH_IV ← top-level | 47 sessions |
| `uw historical vrp --symbol NBIS --realised-window-days 30` | vrp 0.01, realised 112.1%, FAIR ← `.vrp/.regime` | 30 |
| `uw historical cumulative-premium-flow --symbol NBIS --days 90` | net +$52.9M, MIXED ← `.net_flow/.trend_direction` | 48 sessions |
| `uw historical pc-ratio-zscore --symbol NBIS --lookback-days 20` | z −0.616, NORMAL ← `.zscore/.extreme` | 20 |
| `uw historical gex-time-series --symbol NBIS --days 30 --dte-max 45` | flips 06-12, 06-15; now POSITIVE 3d ← `.regime_flip_dates/.trajectory` | 30 |
| `uw historical oi-trend --symbol NBIS --days 30 --top-n 10` | BUILDING, 30 consec days, +1.34M ← `.overall_trend/.total_net_oi_change` | 30 |
| `uw historical trend --symbol NBIS --days 30` | 15 bull / 15 bear, $195→$281 ← `.bullish_days/.bearish_days` | 30 |
| `uw historical signal-backtest --signal-type bullish_flow --lookback-days 5 --top-n 20` (×2) | win_rate 37.5%, N=8, avg −0.58% ← top-level | 8 signals |
| `fz quote NBIS --agent` | RSI 68.6, SMA200 +126.65%, 52W high +0.74% ← `.fundamentals` | 1 |

## Tool errors

None. **Gap-aware note (not an error):** the 252-day IV-percentile lookback resolved to only **47
sessions** present locally (gap 03-28→04-24), so "95.7th percentile" is over ~47 sessions, not a true
year — read as a high-but-short-window percentile. 90d cum-flow used 48 sessions; 30d trend (05-06→06-17)
is entirely post-gap (no crossing).

## DATA NOTE / CORRECTION

None — first reads stood; signal-backtest re-run returned identical values (confirmed real, not stub).

## Verdict for downstream phases

- **Volatility regime:** **RICH absolute IV (95.7%ile) but FAIRLY priced (VRP ≈ 0)** — no debit/credit
  edge from VRP. Conditional risk: if realized vol cools, IV mean-reverts → feeds phase-4's negative-vanna downside.
- **Premium environment:** **neutral** (VRP fair). Put-writing (phase-3) harvests high *absolute*
  premium but it is compensated risk, not a free roll.
- **Conviction that today's signal is HISTORICALLY EDGE-POSITIVE:** **2/5 (LOW).** Against: win_rate
  37.5% (<0.45), MIXED 90d flow, 15/15 day split, parabolic extension (+127% vs SMA200). For: 30-day OI
  build, GEX now positive, latest flow bullish, P/C normal.
- **Three specific datapoints:** IV percentile **95.74** (FAIR vs realized); **VRP 0.01**; **signal
  win-rate 37.5% (N=8, avg −0.58%)**.
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:               bullish_flow
  signal_backtest_win_rate:   0.375
  win_rate_n:                 8
  win_rate_source:            backtest
  ```
  Market-wide base rate (not NBIS-specific), small N=8. p = 0.375 < 0.5 ⇒ edge-negative → phase-9 Kelly
  should floor size near zero / demand defined-risk; do not size up on conviction bin alone.
- **Open questions:** Will the 30-day OI build resolve bullish (LEAP calls win) or is it just rising
  two-sided engagement around a topping parabola? Does the FAIR VRP flip to a vol-crush after 06-18 OPEX
  (phase-4 vanna)? Do fundamentals (phase-7b) justify a name +540% off its low at P/E 93.7?
