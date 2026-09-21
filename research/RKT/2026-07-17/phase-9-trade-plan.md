# Phase 9 — Trade Blueprint

**Ticker:** RKT
**As-of date:** 2026-07-17
**PM voice:** desk PM running an institutional book
**Spot reference:** $14.54 (phase-0.5 screener close; prev $14.90, −2.4% on day)
**Upstream phases cited:** phase-1 through phase-8b

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

Institutions are quietly long RKT — continuous dark-pool large-tier `buy_ratio 0.651`
`[DP:block_stratified]` with dealers mechanically forced to buy (`DEX +$51.1M`)
`[STRUCT:dex]` — around a business that just beat EPS 4/4 quarters (+25% to +50%,
accelerating $0.04→$0.15) `[FUND:earnings_surprise]` and got a fresh Morgan Stanley
Overweight/$19 upgrade on the as-of date `[SENT:recommendation]`; the "bearish" lit
tape (net −$364,914, calls sold) is overwriting/hedging, not distribution, and price
rose +9.9% over 30 sessions *despite* 18 bearish-flow days `[HIST:trend]`. But the
edge is coiled inside a **$14.5–15.0 dealer cage** (long-gamma, ZGL $9.66)
`[STRUCT:gex]` and gated behind a back-to-back binary — **FOMC 07-29 then earnings
07-30 (~±8–10% implied)** `[MACRO:FOMC]` — with vol only fairly priced
(`VRP +0.003`) `[HIST:vrp]`, so this is a **low-conviction, constructive, defined-risk
lean**, not a sized directional bet (phase-8: 2 LONG / 2 RANGE / 1 NEUTRAL, **0
SHORT**).

## Bias + conviction + horizon

- **Directional bias:** **LONG (constructive lean)** — range-aware; the underlying
  favors up over down, near-term is cage-bound until the 07-30 event resolves it.
- **Conviction (M-01 bin):** **0.65**
- **Time horizon:** **1-4w** (through the 07-30 earnings; structures expire 08-21)
- **Why this bin:** phase-10 confluence expected in the low-to-mid 50s (mixed signals
  with a constructive tilt); 0.65 = moderate edge with real disconfirming evidence,
  matching the phase-8b bull residual 0.65 (debate **not** disconfirmed, 0.65 > 0.55).

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| Primary | **$14.30–14.55** | pullback into the dark-pool support shelf / $14.5 put-support + ATM GEX pivot | `[DP:price_levels]` / `[STRUCT:gex]` |
| Aggressive | **$13.80–14.00** | flush to the $14.0 max-pain magnet that holds (buy the dip in the long-gamma regime) | `[STRUCT:max-pain]` |
| Fade (plan B) | **$15.00–15.20** | rejection at the $15 call wall — if it caps, fade back into the range rather than chase | `[OI:oi-by-strike]` |

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| Support (primary) | **$14.30** (DP 5-day shelf, 3.19M sh) | `[DP:price_levels]` |
| Support (invalidation) | **$13.50** (put_wall_support, net_oi −12,540) | `[OI:oi-by-strike]` |
| Resistance / cap | **$15.00** (call_wall_resistance +21,514; +$13.1M positive GEX) | `[OI:oi-by-strike]` / `[STRUCT:gex]` |
| Gamma pivot (ATM) | **$14.50** (−$48.5M ATM short-gamma pocket = break-accelerant) | `[STRUCT:gex]` |
| Regime floor (ZGL) | **$9.66** (far below — confirms long-gamma) | `[STRUCT:gex]` |
| Pin magnet | **$14.0** (07-17/07-24 max-pain) → **$14.5** (07-31 post-earnings max-pain) | `[STRUCT:max-pain]` |

*Price-context color:* `fz` RSI/52w read was unavailable (reduced RKT payload), but
Finnhub places spot $14.54 in the **lower third of the $12.17–$24.36 52w range**
`[FUND:52w]` — **not extended**, which favors the primary/aggressive dip entries over
chasing.

## Invalidation

- **Price-based:** **two daily closes below $13.50** (phase-3 put_wall_support / below
  the phase-2 $14.30 shelf) → the cage has broken down; long lean is wrong.
- **Signal-based:** **dark-pool large-tier `buy_ratio` rolls below 0.50** (accumulation
  → distribution) on the phase-2/phase-7 daily refresh, **OR `DEX` flips negative**
  `[STRUCT:dex]` while spot holds — the mechanical bid that underpins the thesis is gone.
- **Macro-based:** **hawkish FOMC surprise 07-29** (a hike, or a hawkish hold that
  gaps the 30y mortgage rate decisively above 6.55%) `[MACRO:FOMC / MORTGAGE30US]`, or
  a regime deepening from TRANSITIONAL to outright RISK-OFF — either breaks the cage
  *before* earnings can resolve it constructively.
- **Exit style:** **hard stop** on the debit structure (defined max loss); the credit
  structure is defined-risk carry — roll or close on a $13.50 breach.

## Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** `signal_backtest_win_rate` for the *firing* thesis
  (dark-pool accumulation / constructive) is **null** — `dark_pool_accumulation`
  backtest returned no results `[HIST:signal_backtest]`. The `bearish_flow` backtest
  (**1.00, n=10, market-wide**) is **rejected as inapplicable**: this is a constructive
  trade, not a short, and RKT's own 30-session tape *contradicts* bearish_flow (price
  +9.9% under it). → **fall back to the conviction bin.** p_raw = **0.65** (fallback,
  capped at 0.65 — a proxy is never quoted ≥0.70). **p = 0.65.**
- **Kelly inputs:** b = **1.40** (price thesis: entry $14.54, target $16.0, stop
  $13.50 → 1.46/1.04), fraction = 0.25, cap_pct = 5.0
- **Raw Kelly:** (0.65×1.40 − 0.35)/1.40 = **0.40** → 0.40×0.25×100 = 10.0% → capped at
  cap_pct = **5.0%**. **Win-rate map ceiling:** p 0.65 ∈ [0.50,0.70) → **half → 2.5%**.
  Take the smaller → **2.5% pre-context ceiling.**
- **Risk gates:**
  - Fundamentals (phase-7b): **CONFIRM** for a long — `fundamental_signal BULLISH`; the
    7b `tier_adjustment=VETO` is a veto of a *short* (not traded), moot here → **no cut**.
  - Sentiment/crowd (phase-7c): **CONFIRM**, `crowd_state BALANCED` → **no cut**.
  - Correlation cluster (phase-6/8): **none** — RKT uncorrelated with OKLO/PATH/SHOP
    (only PATH/SHOP 0.707) → **no cut**.
  - Sector rotation (phase-6): **neutral** (Financials persistent inflow but bearish
    aggressor) → **no cut**.
  - Debate (phase-8b): bull_residual **0.65** vs bear_residual **0.55** → **not
    disconfirmed → no cut**.
- **Context modifier (phase-0.5):** `unusual_verdict = BUSY_NAME_NORMAL_DAY` → **do not
  size at the top of the band** (today's magnitude is normal-to-quiet for RKT,
  self-pctile 16–20). Combined with the whole desk's "small / defined-risk / don't
  play the binary big" (risk-monitor, 8b), size **below** the 2.5% ceiling.
- **Final size:** **1.5% of book risk** (defined-risk max-loss), below the 2.5%
  half-band ceiling.
- **Deviation reason:** none (deviated *downward*, always permitted).

## Option structures

### Directional (primary) — constructive, defined-risk

- **Structure:** **Call debit spread** (bull call spread)
- **Strike(s) / expiry:** **buy $15C / sell $17C, expiry 2026-08-21** (post-earnings;
  single expiry covering FOMC 07-29 + earnings 07-30)
- **Debit/credit:** ~**$0.65 debit** (illustrative; $15C ~$1.05 − $17C ~$0.40 at iv~0.70)
- **Breakeven:** ~**$15.65**
- **Max loss:** **$0.65** (the debit — this is the 1.5%-of-book risk unit)
- **Why this structure:** IV is rich by percentile (89.6) but FAIRLY priced (VRP ~0)
  into backwardation `[HIST:vrp]`, so a *naked* long call overpays for event vol and
  eats the post-earnings crush; the **debit spread's short $17 leg finances the vega**
  and caps cost. Strikes anchor to the $15 call wall/positive-gamma pin (the cap the
  move must clear) and the $17 call-heavy strike (≈ Barclays target) `[OI:oi-by-strike]`.
  A ±8–10% earnings gap up (~$1.3–1.5) carries spot toward/through $15.65 breakeven;
  max loss is capped regardless of a gap **down** (N4 satisfied).

### Defined-risk alternative — constructive-neutral income (the RANGE case)

- **Structure:** **Put credit spread** (bull put spread)
- **Strike(s) / expiry:** **sell $13.5P / buy $12.5P, expiry 2026-08-21**
- **Debit/credit:** ~**$0.30 credit** (illustrative)
- **Breakeven:** ~**$13.20**
- **Max loss:** **$0.70** (width $1.00 − credit $0.30) — the defined-risk unit
- **Why:** sells the **$13.50 put-wall / invalidation shelf** the market is *already*
  selling (phase-3 put-selling footprint), profits if RKT simply holds the cage, and
  **benefits from the post-earnings IV crush**. A ±10% gap down to ~$13.09 breaches the
  short strike but loss is capped at $0.70 (N4 satisfied). Use this instead of the debit
  spread if you want the range/income expression rather than the upside-lean.

## Macro overlay (cite phase-6)

- **Tailwinds:**
  - Fed funds 3.63%, mid-easing cycle; contained CPI (332.6, flat) supports eventual
    cuts `[MACRO:DFF]` `[MACRO:CPIAUCSL]`.
  - Mr. Cooper **servicing book hedges rising rates** (MSR marks up as prepays slow) —
    why RKT beat *through* the rate rise `[MACRO:sector-overlay]`.
- **Headwinds:**
  - **30y mortgage rate rising 6.55%** (+12bps/2wk) — origination headwind `[MACRO:MORTGAGE30US]`.
  - **Market regime TRANSITIONAL, breadth 38.4%** — "reduce size" `[MACRO:MarketRegime]`.
  - **FOMC 07-29 hawkish tail** (9–8 hike split) `[MACRO:FOMC]`.
- **Net:** **mixed, tilting headwind** — the reason this is defined-risk and small.

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|------|-------|------------------|
| **2026-07-29** | FOMC decision (2pm ET) | ? — hold expected, **hawkish tail** = − for RKT |
| **2026-07-30** | **RKT Q2 2026 earnings** | ? — ~±8–10% implied; beat habit (4/4) skews +, guidance/rate-mix the swing |

Front-expiry implied move: Jul-24 ATM straddle ≈ **$0.96 (~6.6%)** `[CTX:implied_move]`;
earnings-tenor ≈ **±8–10%** — structures sized to this, not the 0.63% 1-day figure.

## Post-trade monitoring checklist

- [ ] **Daily:** dark-pool large-tier `buy_ratio` (invalidate if it rolls < 0.50) and
      any new mega prints vs the $14.54 cluster `[DP:block_stratified]`.
- [ ] **Daily:** `DEX` sign and `GEX` regime on the phase-4 refresh — a flip to
      negative DEX or spot losing $14.5 with the ATM short-gamma pocket = trend risk.
- [ ] **07-29 15:00 ET:** FOMC outcome vs consensus; 30y mortgage / 10y reaction —
      hawkish surprise = invalidation trigger before earnings.
- [ ] **07-30 (earnings):** actual vs the Q2 $2.7–2.9B adj-rev guide + integration/
      synergy commentary; watch for the 10.8% short-float squeeze on a 5th beat.
- [ ] **Weekly:** analyst-revision trend (currently improving, 0 sells) and any move
      of the $15.5–$19 target cluster `[SENT:recommendation]`.

## Citations summary

1. `[DP:block_stratified]` — dark-pool large-tier **buy_ratio 0.651** (1,426 trades,
   $191.2M) — phase-2 §Tier breakdown.
2. `[FUND:earnings_surprise]` — **4/4 EPS beats, +25% to +50%, EPS $0.04→$0.15** —
   phase-7b §Earnings-surprise history.
3. `[HIST:trend]` — price **+9.9% over 30 sessions despite 18/30 bearish-flow days** —
   phase-5 §Multi-day trend.
4. `[STRUCT:gex]` — **POSITIVE/long-gamma, ZGL $9.66**, −$48.5M ATM pocket at $14.5,
   $15 positive-gamma wall — phase-4 §GEX.
5. `[MACRO:MORTGAGE30US]` — **30y mortgage 6.55% rising** — phase-6 §Rates.
