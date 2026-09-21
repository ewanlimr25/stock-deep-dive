# Phase 5 — Historical Context & VRP

**Ticker:** MU
**As-of date:** 2026-06-23
**Generated:** 2026-06-23
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md, phase-1-flow.md, phase-4-structure.md

## Summary

History reframes the whole setup: MU is a **parabolic momentum name pulling back into a
binary**. It ran **+50% in six weeks** ($795 on 2026-05-11 → a $1195 peak on 06-22), then
**dropped −11.9% in a single session today** ($1195.18 → $1053.58) on the eve of earnings,
leaving it **−13.3% off its $1213.56 52-week high** yet still **+268% YTD** and **+156%
above its 200-DMA**. Two structural-history facts dominate: (1) **GEX flipped
POSITIVE→NEGATIVE *today* (2026-06-23)** after **30 consecutive positive-gamma sessions** —
a fresh short-gamma regime, and today's −12% drop is that amplification firing; (2) **OI
has built 30 days straight** (+4.89M net contracts) — sustained accretion into the catalyst.
IV sits at the **100th 1-year percentile** (z +1.29) but **VRP is −0.098 → PREMIUM_BUYING**
because realized vol (117%) has outrun even the 107% implied (a parabola-distorted reading —
treat with care into an IV crush). The decisive edge signal: in the current tape **bearish_flow
has won 88.9% (n=9) while bullish_flow has won 0.0% (n=8)** — the regime is rewarding downside
and punishing longs.

## Key signals

- Price ran **+50%** ($795→$1195) in 30 sessions then **−11.9% today** ($1195→$1053.58); −13.3% off 52w high, +268% YTD `[HIST:trend]` `[HIST:52w_proximity fz]`
- **GEX regime flip TODAY**: POSITIVE→NEGATIVE on 2026-06-23 after 30 days positive; ZGL leapt to 1495.2 (Δ+300) `[HIST:gex_time_series]`
- **OI building 30 consecutive days**, total_net_oi_change +4,890,618 — sustained pre-earnings buildup `[HIST:oi_trend]`
- IV **100th percentile** (z +1.29, HIGH_IV) but **VRP −0.098 / PREMIUM_BUYING** (IV 107% < realized) `[HIST:iv_percentile_zscore]` `[HIST:vrp]`
- Backtest asymmetry: **bearish_flow 88.9% win (n=9)** vs **bullish_flow 0.0% (n=8)**; dark_pool_accumulation no results (n=0) `[HIST:signal_backtest]`

## Detailed findings

### IV regime — `[HIST:iv_percentile_zscore]` `[HIST:vrp]`

- `iv_percentile` = **100** (top of 1-year range), `iv_zscore` = **1.293**, `current_iv30d`
  = 1.0721 (107%), `regime` = HIGH_IV. **N = 50 `dates_used`** in the 252-day window (gap +
  limited history — the percentile rests on 50 sessions, not 252; medium confidence).
- `vrp` = **−0.098** (iv30d 1.0721 vs realised_vol 1.1701), `regime` = **PREMIUM_BUYING** —
  options are *cheap relative to realized*. **Caveat:** realized is inflated by the
  parabolic +50%/−12% path; post-earnings realized typically collapses, so the
  premium-buying signal is unreliable directly into the print. Favors debit *structure* but
  do not over-weight against the certain IV crush.

### Cumulative premium flow (90d, 51 sessions) — `[HIST:cumulative_premium_flow]`

`cumulative_bullish` $67.50B vs `cumulative_bearish` $67.12B → **net_flow +$382M**,
`trend_direction` = **MIXED**. Over the trailing window flow is essentially balanced
(+0.3% net bullish) — the two-sidedness seen today is a **90-day characteristic**, not a
one-day artifact. Today's −$145M bearish is a blip against a slightly-net-bullish base.

### GEX time series (the regime story) — `[HIST:gex_time_series]`

- `regime_flip_dates`: exactly one — **2026-06-23, POSITIVE→NEGATIVE**, spot 1053.58, ZGL
  1495.2, zgl_delta +300.04.
- `trajectory`: POSITIVE every session 2026-05-11 → 06-22 (ZGL hugging spot, 35–150), then
  flips today. On 06-22 spot $1195 with ZGL $1195.16 (on the cusp); the −12% drop today
  punched below the flip and the book went short-gamma. **A fresh short-gamma regime the
  day before earnings ⇒ expect amplified post-print ranges** (per heuristic: GEX flip in
  last 5d → hedging in transition → larger ranges).

### OI trend — `[HIST:oi_trend]`

`overall_trend` = **BUILDING**, `consecutive_build_days` = **30**, `total_net_oi_change`
= **+4,890,618**. Uninterrupted 30-session OI accretion = sustained engagement (not a
one-day spike) into the catalyst — both sides loading per phases 1/3.

### Multi-day trend (30d, 2026-05-11 → 06-23) — `[HIST:trend]`

| Field | Value |
|---|---|
| `price_change` | **795.33 → 1051.77** (+32% window; +50% to the 06-22 peak then −12% today) |
| `bullish_days` / `bearish_days` | 18 / 12 |
| `iv_rank_change` | 100 → 100 (pinned max all window) |
| `flow_direction_latest` | **bearish** |
| `days_analyzed` | 30 (window 05-11→06-23 is gap-free; the 03-28→04-24 hole is earlier) |

Last row 06-23: close 1051.77, iv_rank 100, pcr 1.012. First row 05-11: close 795.33,
pcr 0.669 (started call-tilted, now balanced).

### Price context (`fz`, advisory EOD cross-check) — `[HIST:rsi fz]` `[HIST:52w_proximity fz]`

| Metric | Value | Read |
|---|---|---|
| RSI(14) | **57.04** | neutral — the −12% day cooled an overbought condition |
| vs SMA20 / SMA50 / SMA200 | +4.85% / +38.17% / **+156.0%** | strong uptrend, extended long-term |
| Perf YTD | **+268.51%** | monster momentum name |
| 52W High / Low | 1213.56 (**−13.33%**) / 103.38 (+917%) | −13% off ATH; far above lows |

Independent confirmation of the UW picture: extended secular uptrend, sharp short-term
pullback, RSI neutralized — neither overbought-blowoff nor oversold-washout into the print.

### Signal backtest (current signal's historical edge) — `[HIST:signal_backtest]`

| Signal class | win_rate | n (total_signals) | note |
|---|---|---|---|
| **bearish_flow** | **88.9%** | **9** | matches the net-directional tag (phase-0.5 #1 bearish) |
| bullish_flow | 0.0% | 8 | recent longs failing |
| dark_pool_accumulation | — | 0 | "no backtest results" (re-run confirmed empty) → not sizable |

Market-wide base rates (no `--symbol`), `--lookback-days 5`. The bearish/bullish
asymmetry (88.9% vs 0%) says the **current regime rewards downside flow** — but n=8–9 is
small (N-conditional cap applies) and this is a binary-event name where a directional
base rate is a weak prior. dark_pool_accumulation (phase-2's bullish signal) is **not
backtestable here** → the only populated directional edge is bearish.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | N / anchor |
|---|---|---|
| `historical iv-percentile-zscore --symbol MU --lookback-days 252` | iv_percentile 100, z 1.293 ← `.iv_percentile,.iv_zscore` | 50 dates_used |
| `historical vrp --symbol MU --realised-window-days 30` | vrp −0.098, PREMIUM_BUYING ← `.vrp,.regime` | latest-anchor 06-23 |
| `historical cumulative-premium-flow --symbol MU --days 90` | net +$382M, MIXED ← `.net_flow,.trend_direction` | 51 sessions |
| `historical pc-ratio-zscore --symbol MU --lookback-days 20` | pcr 1.013, z 0.782 (not extreme) ← `.zscore` | 20d |
| `historical gex-time-series --symbol MU --days 30` | flip 06-23 POS→NEG ← `.regime_flip_dates[0]` | 30 sessions |
| `historical oi-trend --symbol MU --days 30` | BUILDING, 30 build-days ← `.overall_trend,.consecutive_build_days` | 30 sessions |
| `historical trend --symbol MU --days 30` | 795→1052, latest bearish ← `.price_change,.flow_direction_latest` | 30, gap-free |
| `historical signal-backtest --signal-type bearish_flow/bullish_flow/dark_pool_accumulation` | 88.9%/n9, 0%/n8, n0 ← `.win_rate,.total_signals` | market-wide, 5d |
| `fz quote MU` | RSI 57.04, +156% vs SMA200, +268% YTD ← `.fundamentals` | EOD advisory |

## Tool errors

(none. `gex-time-series`/`oi-trend` expose `.trajectory`/`.daily_data` not `.series` — a
shape lookup, not an error. `dark_pool_accumulation` empty stub is a genuine no-result,
re-run once per guidance and confirmed n=0 → `win_rate_source=null` for that class.)

## DATA NOTE / CORRECTION

(none — initial `jq` used generic field aliases that returned null; re-read against the
tools' actual field names before transcribing any value. No null/partial value written.)

## Verdict for downstream phases

- **Volatility regime:** **RICH in absolute terms (IV 100th %ile)** but **PREMIUM_BUYING by
  VRP** (realized > implied) — an unstable pre-earnings reading; the post-print IV crush is
  the dominant vol fact, so phase-9 should favor structures that are *not* naked-long IV
  into the print (define risk, or harvest the crush).
- **Environment:** premium-SELLING by IV rank, premium-BUYING by VRP — **conflicted**; the
  honest call is "expensive vol that has been *earned* by realized, about to crush."
- **Conviction today's signal is HISTORICALLY EDGE-POSITIVE:** **3/5, tilted bearish** — the
  bearish_flow 88.9% vs bullish_flow 0% asymmetry + fresh short-gamma flip + a name −13% off
  ATH after a −12% day argue the path of least resistance is *down/volatile*; but small N
  and the binary event cap conviction.
- **Three datapoints:** IV percentile **100** (z +1.29); VRP **−0.098** (PREMIUM_BUYING);
  bearish_flow win_rate **88.9% (n=9)**.
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:              bearish_flow
  signal_backtest_win_rate:  0.889
  win_rate_n:                9
  win_rate_source:           backtest
  ```
  Notes for phase-9 Kelly: (a) **market-wide base rate**, not MU-specific; (b) **n=9 →
  apply the N-conditional cap** (`rubrics/sizing-rubric.md`); (c) phase-2's bullish
  dark_pool_accumulation signal is **not backtestable** (n=0), so the only measured edge is
  bearish; (d) this is a **binary earnings event** — the directional win-rate is a weak
  prior vs the ±10.9% gap; size for the event, not the base rate.
- **Open questions:** Does macro/sector (phase-6) confirm semis are leading lower (phase-0.5)
  so the bearish edge has a tailwind, or is the −12% day already the de-risk? Do fundamentals
  (phase-7b) justify the +268% YTD re-rate or flag a valuation veto into the print?
