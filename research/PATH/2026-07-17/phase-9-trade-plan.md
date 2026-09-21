# Phase 9 — Trade Blueprint

**Ticker:** PATH (UiPath)
**As-of date:** 2026-07-17
**PM voice:** desk PM running a $5–50M options-overlay book
**Spot reference:** $12.13 (phase-4 GEX spot; phase-2 DP VWAP $12.14; close $12.11)
**Upstream phases cited:** phase-0.5 through phase-8b

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

PATH is a genuinely-accumulated but **dealer-caged range**: institutions bought
$267M dark-pool with the large tier **65.7% buy** and absorbed an intraday fade
`[DP:block_stratified]`, and OI has built **11 consecutive sessions (+337k)**
`[HIST:oi_trend]` — yet the upside is triple-capped at **$13** (19,681-contract call
wall + **+6.03M peak GEX** dealer-sell + analyst PT cluster) `[OI:oi_by_strike][STRUCT:gex][MACRO:PATH_analysts]`
with no catalyst until Sep-3 earnings. The desk is non-directional (phase-8: 1 LONG /
2 NEUTRAL / 1 RANGE `[AGENT:*]`), the empirical bullish_flow edge is negative
(**14.3% win, n=7** `[HIST:signal_backtest]`), and the debate disconfirmed the long
(bull 0.55 / bear 0.65 `[DEBATE:]`) — so the tradeable edge here is **harvesting the
rich-IV $11.88–$13 range** (VRP +0.289 `[HIST:vrp]`), not chasing direction.

## Bias + conviction + horizon

- **Directional bias:** LONG (slight, accumulation-backed) — but so weak the
  *recommended expression is range-neutral*; no phase is bearish, none breakout-bullish.
- **Conviction (M-01 bin):** **0.55** (slight edge)
- **Time horizon:** 1-4w (range harvest pre-earnings); the directional flyer is 1-3m (Sep-3 catalyst)
- **Why this bin:** base narrative ~0.65 (real accumulation, clean levels) **down-shifted
  one bin to 0.55 by the phase-8b disconfirmation** (bear residual 0.65 ≥ bull 0.55);
  phase-10 confluence expected in the low band (QUIET tape, absent from signal-confluence,
  26.1% conviction matrix).

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| Primary | $11.90–$12.05 | tag of the $11.88–$12.01 DP demand shelf that holds (sell the condor / put spread here) | `[DP:price_levels]` |
| Aggressive | ~$12.13 (now) | initiate the range condor at spot with $11–$13 defined | `[STRUCT:gex]` |
| Fade (plan B) | close >$13.05 on rising volume | the cap breaks → cover the short call, flip to the $12.5/$14 call-debit breakout | `[OI:oi_by_strike]` |

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| Support | **$11.88** (5-day DP demand shelf; heaviest $11.99/$12.00) | `[DP:price_levels]` |
| Resistance | **$13.00** (call_wall_resistance, 19,681 near-term call OI; peak GEX) | `[OI:oi_by_strike]` / `[STRUCT:gex]` |
| Gamma flip (ZGL) | **$6.78** (far below spot — long-gamma holds until price collapses here) | `[STRUCT:gex]` |
| Pin magnet (max-pain) | **$11–$11.5** (near-expiry max-pain; downward opex gravity) | `[STRUCT:max_pain]` |

Price-context color: `fz` RSI/SMA/52W read was **unavailable this run** (truncated
payload) — no independent overbought/52W-proximity cross-check; the +4.1% 30d grind
`[HIST:trend]` is orderly (not parabolic), so no acute chase flag, but the read is
un-corroborated.

## Invalidation

- **Price-based:** two daily closes **below $11.85** (loses the $11.88 DP shelf →
  downside un-cushioned to $11/$10) **OR** two daily closes **above $13.10** (breaks
  the call-wall cap → the RANGE/short-call thesis is wrong; flip to the breakout flyer).
- **Signal-based:** **GEX flips negative** on daily refresh (the durable 30d
  long-gamma regime `[HIST:gex_time_series]` breaking = the pin fails) **OR** dark-pool
  accumulation reverses to distribution `[INSIGHT:institutional_accumulation]` **OR**
  cumulative premium flow turns net-bearish 3 consecutive sessions `[HIST:cumulative_premium_flow]`.
- **Macro-based:** **hawkish FOMC surprise 2026-07-29** (a hike, or a hold that prices
  the Sept hike harder → growth-multiple headwind `[MACRO:FOMC]`) **OR** VIX closes
  **>20** with `risk_market_regime` flipping RISK-OFF `[MACRO:VIX]`.
- **Exit style:** condor/put-spread = **roll or close** at the tested short strike;
  call-debit flyer = **hard stop** at the debit (defined max loss).

## Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** `p_raw = 0.143` (bullish_flow, **n=7**, source=backtest)
  `[HIST:signal_backtest]`; N-cap (n<10) = 0.75 → **capped p = min(0.143, 0.75) = 0.143**.
  (No fallback — win_rate_source is `backtest`, not null.)
- **Kelly inputs:** b = |13.00 − 11.90| / |11.90 − 11.50| = **2.75**; fraction 0.25; cap_pct 5.
- **Raw Kelly:** (0.143×2.75 − 0.857)/2.75 = **−0.169 (NEGATIVE)** → **Win-rate map
  ceiling: STARTER / SKIP** (p 0.143 < 0.50 → SHORT-side floor forces starter/skip;
  a negative-edge signal is not a directional position).
- **Risk gates:**
  - Fundamentals (7b): **NA** (no Finnhub key) → no-op; qualitative read non-contradicting (contradiction_count 0).
  - Sentiment/crowd (7c): **CONFIRM**, crowd_state **CROWDED_SHORT** → no-op (short base is squeeze *optionality*, not sized on; hazard for any short).
  - Correlation cluster (6/8): OKLO **below 0.70** → soft-watch, **no cut** (two speculative high-beta longs share risk-sentiment beta — note, don't cut).
  - Sector rotation (6): Technology **INFLOW, persistence 0.8** → **aligned, no cut**.
  - Debate (8b): bull_residual **0.55** vs bear_residual **0.65** → **DISCONFIRMED** →
    down-shift bin one (0.65→0.55) **and cut one size step**. **FIRES.**
- **Context modifier (0.5):** `unusual_verdict = QUIET` → **caps directional size at
  STARTER regardless of Kelly.**
- **Final directional size: 0% (watch-only / carry the defined-risk range only).**
  Negative raw Kelly (−0.169) with a directional bias mandates 0 directional size
  (sizing rubric: "if raw_kelly < 0 the directional action MUST be NEUTRAL or the
  opposite side") — reinforced by the QUIET starter-cap and the debate cut. **Only
  the defined-risk structures are carried**, each ≤0.5% of book risk (range condor
  the primary; the $12.5/$14 flyer ≤0.25% as an optional pre-earnings lottery).
  **No upward deviation (forbidden — a gate fired, context is QUIET, and Kelly is
  negative).**

## Option structures

### Directional (primary) — small breakout flyer on the accumulation
- **Structure:** call debit spread (bull)
- **Strike(s) / expiry:** **$12.5 / $14 call spread, 2026-09-18**
- **Debit/credit:** ~**$0.55 debit** (illustrative; IV ~67%)
- **Breakeven:** ~**$13.05**
- **Max loss:** $0.55 (the debit); max gain ~$0.95
- **Why this structure:** the *only* way the $13 cap breaks is the **Sep-3 earnings**
  catalyst (the debate's unrefuted "no catalyst till Sep-3"); a **spread, not a naked
  call**, because VRP +0.289 makes IV rich and both legs crush together through
  earnings `[HIST:vrp]`. **Earnings-exposed by design** — strikes anchored to the
  $12.5 wall and above the $13 cap. Starter size only (negative empirical edge).

### Defined-risk alternative (the RECOMMENDED expression) — rich-IV range harvest
- **Structure:** iron condor (slight bull skew: put spread further OTM)
- **Strike(s) / expiry:** **sell $11P / buy $10.5P + sell $13C / buy $13.5C, 2026-08-21**
- **Debit/credit:** ~**$0.25 net credit** (illustrative)
- **Breakeven:** ~**$10.75** and ~**$13.25**
- **Max loss:** ~$0.25 (width $0.50 − credit $0.25), one side
- **Why this structure:** this is the regime-matched trade — long-gamma **mean-reversion
  pin at $12–$13** `[STRUCT:gex]`, **rich IV to sell** (VRP +0.289 `[HIST:vrp]`),
  max-pain pulling to $11–$11.5, and the macro guidance literally says *"iron condors
  in range"* `[MACRO:MarketRegime]`. Short strikes ($11/$13) map to the DP shelf and
  the call wall. **Pre-earnings (Aug 21 < Sep 3)** — closes before the binary, no
  earnings gap risk.
- **Expected-move (N4) check:** front-expiry implied move **±1.13% / $0.14**
  `[CTX:implied_move]`; over the 35-day Aug-21 tenor IV implies ~**±21% (±$2.5)** and
  realized (RV30 0.386) ~**±12% (±$1.45)**. The short strikes sit **±$1.1 (inside both)**
  — the trade is *explicitly* the VRP + long-gamma-pin bet (realized < implied), which
  is precisely why it is **sized starter/small**: a single 1-SD move tags a short strike.
  If uncomfortable, widen shorts to $10.5P/$13.5C for more room at less premium.

## Macro overlay (cite phase-6)

- **Tailwinds:** Technology **#1 sector options inflow +$1.17B, persistence 0.8**
  `[MACRO:sector_flow_persistence]`; cooling CPI **3.5% YoY** `[MACRO:CPI]`; ~28% short
  base = squeeze optionality on a $13 break `[SENT:short_float]`.
- **Headwinds:** regime **TRANSITIONAL "half position sizes"** `[MACRO:MarketRegime]`;
  Fed **hawkish, ~63% Sept-hike odds** `[MACRO:FOMC]`; **VIX 18.77 +12% d/d** rising
  `[MACRO:VIX]`; PATH a **laggard within tech** `[CTX:]`; growth decelerating (Hold-rated).
- **Net:** **mixed, headwind-leaning** — the sector inflow is the one real tailwind,
  swamped for *sizing* by the half-size regime + rising VIX.

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|------|-------|------------------|
| 2026-07-29 | FOMC (non-SEP, hold expected) | ? (hawkish-hold risk; hike surprise = − for growth) |
| ~2026-08-12 | July CPI | ? (further cooling = +; sticky core = − via Sept-hike fuel) |
| 2026-09-03 | **PATH Q2 earnings** (outside 30d) | ? — the ONLY catalyst that can break the $13 cap |

## Post-trade monitoring checklist

- [ ] **Daily: GEX regime + ZGL** — a flip to NEGATIVE breaks the pin thesis; exit the condor `[STRUCT:gex]`.
- [ ] **Daily: dark-pool buy-ratio** — if it drops <0.50 (accumulation → distribution), the floor is failing `[DP:block_stratified]`.
- [ ] **Daily: $11.88 shelf and $13 wall closes** — two closes beyond either = invalidation.
- [ ] **Each session: cumulative premium flow sign** — 3 net-bearish sessions = signal invalidation `[HIST:cumulative_premium_flow]`.
- [ ] **VIX through 20 / FOMC Jul-29** — macro invalidation triggers; cut on a RISK-OFF regime flip `[MACRO:VIX]`.
- [ ] **Into Sep-3 earnings:** decide the $12.5/$14 flyer BEFORE the print (hold for the catalyst = intended; the condor must already be closed pre-earnings).

## Citations summary

1. `[DP:block_stratified]` — dark-pool large tier **65.7% buy** (buy 13.95M / sell 7.30M sh), $258M — phase-2-dark-pool.md §Tier breakdown.
2. `[HIST:oi_trend]` — OI **BUILDING 11 consecutive days, +337,036 net** — phase-5-historical.md §OI trend.
3. `[STRUCT:gex]` — GEX POSITIVE, **peak +6.03M at $13**, ZGL $6.78 (dealer-cap, mean-reversion) — phase-4-structure.md §GEX.
4. `[HIST:signal_backtest]` — bullish_flow win-rate **14.3% (n=7)** → negative Kelly — phase-5-historical.md §Sizing handoff.
5. `[DEBATE:]` — disconfirmed, bull 0.55 / bear 0.65 — phase-8b-debate.md §Disconfirmation verdict.
