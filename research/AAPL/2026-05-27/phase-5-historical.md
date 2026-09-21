# Phase 5 — Historical Context & VRP

**Ticker:** AAPL
**As-of date:** 2026-05-27
**Generated:** 2026-05-28T03:13:00Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md, phase-1-flow.md, phase-4-structure.md

## Summary

The historical context sets up a genuine tension: **vol is cheap** (IV30d 22.4%,
**6th percentile**, regime LOW_IV) and **flow has been persistently bullish** (90d
net +$587M, 21/30 bullish days, OI building **30 consecutive days**, +4.2M
contracts) — a constructive premium-buying backdrop — **but the stock is strongly
extended**: it has rallied **+24.4% over the window (249.94 → 310.85)**, is **up
16.2% in the past month**, sits **−0.31% from its 52-week high ($311.82)**, and
RSI is **78.85 (overbought)**. The bullish_flow signal backtest reads 85.7% but on
**n=7, in-sample** (low confidence). **Net: today's bullish lean is
historically edge-positive *but* it is chasing an overbought name at its 52-week
high into a dealer long-gamma pin — the extension materially tempers the edge.**

> **Gap caveat (MANDATORY):** the local window is non-contiguous — 21-session hole
> 2026-03-28→04-24. Every "252d"/"90d"/"30d" read below is really **~32 sessions**
> (IV percentile `dates_used 32`; trend `date_range 2026-03-18→05-27`). Percentiles
> and trends are over *available* sessions, not a calendar window — do not annualize.

## Key signals

- IV30d 22.4% at **6.25 percentile** (z −1.15), regime **LOW_IV** — vol cheap
  `[HIST:iv_percentile_zscore]`; VRP +0.0038 (FAIR vs realized 22.0%) `[HIST:vrp]`
- 90d cumulative flow net **+$587M bullish** ($5.93B bull / $5.34B bear) `[HIST:cumulative_premium_flow]`
- **30 consecutive OI-build days, +4.22M net contracts, trend BUILDING** `[HIST:oi_trend]`
- **EXTENDED: RSI 78.85, −0.31% from 52W high, +16.2% 1-month, above all SMAs** `[HIST:rsi fz]` `[HIST:52w_proximity fz]`
- bullish_flow backtest **win_rate 85.7%, n=7, avg fwd +5.06%/5d — in-sample, low-N** `[HIST:signal_backtest]`

## Detailed findings

### IV regime (percentile + z-score + VRP)

- current_iv30d **0.2242**, **iv_percentile 6.25**, iv_zscore −1.152, regime
  **LOW_IV** (dates_used 32). Vol is near the bottom of its available range.
- VRP **+0.0038** (iv30d 22.42% − realized 22.04%), regime **FAIR** — "IV close to
  realised, no clear edge from VRP alone." → **Absolute vol is cheap, but not cheap
  *relative to realized*.** Mild lean to **debit/long-premium** structures (cheap
  optionality, no VRP penalty for owning it) — but cheap IV in a low-vol year can
  still mean-revert higher on any shock.

### Cumulative premium flow (90d → ~32 sessions)

cumulative_bullish $5.93B vs cumulative_bearish $5.34B, **net +$586.9M, BULLISH**.
A ~10% net bullish tilt sustained across the window — persistent but *mild* (not a
forceful stealth build). Consistent with the rally, not ahead of it.

### P/C ratio z-score (sentiment extreme?)

current_pc 0.373 vs 20d mean 0.419, **z −0.478, extreme NORMAL**. Today's
call-heavy tilt is only mildly below its own 20d mean — **no sentiment extreme, no
contrarian trigger.** Confirms phase-1: the bullish lean is mild, not stretched.

### GEX time series (regime stability)

`gex-time-series` returned **no per-day rows** (toplevel note only) → no detectable
regime-flip dates in the window. Combined with phase-4 (long gamma now), treat the
**long-gamma regime as stable** over the window (no recent flip = no recent
vol-expansion trigger). Flagged under Tool errors (empty series).

### OI trend

overall_trend **BUILDING**, **consecutive_build_days 30**, total_net_oi_change
**+4,224,054**. OI has accreted every available session — genuine sustained
positioning. **But read against the extension:** building OI into a 52W-high,
RSI-79 name is *late-cycle* positioning, not early accumulation.

### Multi-day trend table (aggregate)

| Metric | Value |
|--------|-------|
| date_range | 2026-03-18 → 2026-05-27 (~32 sessions, gap excluded) |
| bullish_days / bearish_days | **21 / 9** |
| flow_direction_latest | bullish |
| **price_change** | **249.94 → 310.85 (+24.4%)** |
| iv_rank_change | 21.26 → 32.05 |

### Price context (`fz` — advisory cross-check, EOD)

| Field | Value | Read |
|-------|-------|------|
| RSI(14) | **78.85** | **overbought** (>70) `[HIST:rsi fz]` |
| 52W High | 311.82 (**−0.31%**) | **at 52-week high** `[HIST:52w_proximity fz]` |
| 52W Low | 195.07 (+59.35%) | well off lows |
| vs SMA20 / 50 / 200 | +5.95% / +13.92% / +18.46% | stretched above all MAs |
| Perf Month / YTD | **+16.16%** / +14.34% | up 16% in a month |

**This is the most important counter-signal in the whole workup.** Every flow/DP
signal so far is mildly bullish, but the underlying has *already* run +24% and now
sits overbought at its 52W high. A fresh long here is buying strength into
exhaustion territory with dealers long gamma (pin) above — poor risk/reward for
chasing; better for fading strength or waiting for a pullback into the $302–305
support.

### Signal backtest (current signal's edge)

| Field | Value |
|-------|-------|
| signal_type | **bullish_flow** (matches phase-1 lean) |
| **win_rate** | **85.7%** |
| total_signals (n) | **7** |
| avg_move_pct | +5.06% (5 trading days) |
| methodology | "In-sample backtest — not a robust live edge." |

dark_pool_accumulation backtest: **n=0, no results** → not usable. So the Kelly `p`
comes from bullish_flow: **0.857 but n=7** (below the 10-firing confidence floor,
and explicitly in-sample). Phase-9 must apply the N-conditional cap.

## Tool calls (audit trail)

| Command | Result summary |
|---------|----------------|
| `uw historical iv-percentile-zscore --lookback 252` | IV pctile 6.25, LOW_IV, dates_used 32 |
| `uw historical vrp --realised-window 30` | VRP +0.0038, FAIR |
| `uw historical pc-ratio-zscore --lookback 20` | z −0.48, NORMAL |
| `uw historical cumulative-premium-flow --days 90` | net +$587M BULLISH |
| `uw historical gex-time-series --days 30` | **empty (no per-day rows)** |
| `uw historical oi-trend --days 30` | BUILDING, 30 build-days, +4.22M |
| `uw historical trend --days 30` | +24.4% price, 21/9 bull/bear days |
| `uw historical signal-backtest bullish_flow` | win 85.7%, n=7, in-sample |
| `uw historical signal-backtest dark_pool_accumulation` | n=0, no results |
| `fz quote AAPL` (price context) | RSI 78.85, −0.31% from 52W high |

## Tool errors

- `uw historical gex-time-series --symbol AAPL --days 30 --dte-max 45` → returned
  toplevel note only, **0 per-day rows**. Cannot confirm/deny regime-flip dates;
  treated as "no flip detected" and cross-checked against phase-4 (long gamma now).
  Possible gap interaction (non-contiguous window). Not fatal.
- **Latest-anchor:** trailing tools (iv-percentile, pc-zscore, oi-trend,
  cumulative-flow, signal-backtest, vrp realized leg) anchor to latest available
  date = 2026-05-27 = as-of → valid for this run; would shift on re-run after a new
  session.

## Verdict for downstream

- **Volatility regime:** **CHEAP in absolute/percentile terms (6th %ile, LOW_IV)
  but FAIR vs realized (VRP ~0)** → favor **debit/long-premium** structures over
  credit; long optionality is not being overpaid for.
- **Premium environment:** **premium-BUYING** (cheap IV, no VRP penalty), with a
  persistent but mild bullish flow tilt.
- **Conviction that today's signal is HISTORICALLY EDGE-POSITIVE:** **3/5** — the
  backtest is nominally strong (85.7%) and flow/OI persistently bullish, but n=7
  is below the confidence floor *and* the **overbought-at-52W-high extension** is a
  powerful counterweight. Edge-positive on paper, risk-elevated in practice.
- **Three data points:** IV %ile **6.25** · VRP **+0.0038 (FAIR)** · bullish_flow
  win_rate **85.7% (n=7)**.
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:              bullish_flow
  signal_backtest_win_rate:  0.857
  win_rate_n:                7
  win_rate_source:           backtest
  ```
  (n=7 < 10 → apply the small-N Kelly cap in `rubrics/sizing-rubric.md`; the in-
  sample caveat argues for the conservative end.)
- **Open questions:**
  - Does the overbought/52W-high extension get confirmed as exhaustion by
    sentiment/positioning (phase-7c crowd + short interest)?
  - Is there a fundamental or macro reason for the run (phase-6, phase-7b) or is
    it momentum chasing cheap vol?
