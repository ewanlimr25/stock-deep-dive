# Phase 9 — Trade Blueprint

**Ticker:** BE
**As-of date:** 2026-07-21
**PM voice:** desk PM running an institutional options-overlay book
**Spot reference:** 226.26 (phase-2 DP close / phase-0.5)
**Upstream phases cited:** phase-0.5 through phase-8b

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

BE's record net-bullish flow is manufactured out of **$25.7M of net put-SELLING at
197.5–230** `[FLOW:sweeps]` into a **VRP of +0.49 in a PREMIUM_SELLING regime (IV
percentile 100)** `[HIST:vrp]` — the smart money is harvesting the richest event
vol of the year, not chasing direction, and the desk agrees to a man (phase-8: 3
RANGE / 2 NEUTRAL, 0 directional) `[AGENT:earnings-scout]`. The tradeable edge is
therefore to **sell the vol with defined risk between the triple-confirmed 197.5
floor and the 250 call wall**, siding with the put-writers rather than the price.
But this is a *small, contested* trade: the 8b debate disconfirmed
(bull 0.65 / bear 0.65) `[DEBATE:]`, fundamentals flagged CAUTION on insider
selling into extreme valuation `[FUND:MSPR]`, and a short-gamma trapdoor sits at
197.5 `[STRUCT:gex]` — so the size is starter and the lower wing is bought.

## Bias + conviction + horizon

- **Directional bias:** **RANGE** (premium-selling, bullish-lean) — the phase-8
  plurality; the 7b veto and 8b debate cut size, not bias.
- **Conviction (M-01 bin):** **0.55** (slight edge)
- **Time horizon:** **1-4w** (through the 8/21 post-earnings OPEX; the LEAP
  directional leg is 1-3m+)
- **Why this bin:** avg agent conviction 2.4/5 with 0 directional votes
  `[AGENT:*]`, and 8b `disconfirmed = true` down-shifted the base 0.65 by one bin
  `[DEBATE:]` — a genuine but contested premium-selling edge, not a conviction long.
  (Phase-10 to confirm the confluence band.)

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| Primary | **215** | Tag of the 7/24 max-pain magnet holding; sell the put credit spread into the pin (better credit, defined risk) | `[STRUCT:max_pain]` |
| Aggressive | **205–210** | Deeper dip into the 210 put wall / DP support — richer credit, breakeven still on the 197.5 floor | `[OI:oi_by_strike]` |
| Fade | **243–250** | If it rips to the call wall pre-earnings, sell the rip (call credit spread / trim longs) — the phase-8 "squeeze outran its pin" fade | `[DP:price_levels]` / `[OI:oi_by_strike]` |

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| Support | **197.5** (put wall net −31,125 OI) / 197.06 (DP $214.9M cluster / 7/20 low) | `[OI:oi_by_strike]` / `[DP:price_levels]` |
| Resistance | **250** (call wall +4,671 OI) / 243 (DP $51.1M) | `[OI:oi_by_strike]` / `[DP:price_levels]` |
| Gamma flip | **none — FULLY_NEGATIVE, no ZGL** (whole zone is short-gamma/amplifying) | `[STRUCT:gex]` |
| Largest pin | **215** (7/24 max-pain, pre-earnings magnet); post-ER flips to 240 (7/31) | `[STRUCT:max_pain]` |

*Price-context color:* `fz` RSI/52-week reads were unavailable (degraded quote,
phase-5) — no independent overbought/52w-proximity overlay. Note the stock sits
mid-range of a violent $24→$351→$226 year `[HIST:trend]`; treat any rip into 250
as fade-able, not breakout-confirmed, until the print.

## Invalidation

- **Price-based:** **daily close below 197.5** — the put wall + GEX trapdoor
  breaks, short-gamma mechanically accelerates toward 165 `[STRUCT:gex]`. This is
  the credit-spread's danger line; the bought 185 wing caps the loss below it.
- **Signal-based:** post-print **IV percentile fails to compress** (the crush that
  funds the credit doesn't happen) `[HIST:iv_percentile_zscore]`, OR UW
  institutional-accumulation stays **DISTRIBUTION** while net_flow flips negative
  `[INSIGHT:institutional_accumulation]`.
- **Macro-based:** **hawkish FOMC surprise 7/29** (hike / hawkish-hold shock)
  `[MACRO:FOMC_2026-07-29]`, OR a renewed **AI-sector rout** ("China AI shock 2.0")
  dragging BE regardless of its own print `[SENT:news]`.

## Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** p_raw = **0.857** (n=**7**, source=**backtest**) →
  N-conditional cap (n<10 → 0.75) → **capped p = 0.75** `[HIST:signal_backtest]`
- **Kelly inputs:** b = **0.481** (credit $6.50 / max-loss $13.50 on the primary
  put credit spread), fraction = 0.25, cap_pct = 5
- **Raw Kelly:** (0.75×0.481 − 0.25)/0.481 = **0.230** → ×0.25×100 = 5.76% →
  **capped 5.0%** · **Win-rate map ceiling** (p=0.75 ≥ 0.70): **full (5%)** → take
  the smaller = **5.0% pre-gate**
- **Risk gates:**
  - Fundamentals (7b): **CAUTION** → **cut one step (full → half = 2.5%)** — insider MSPR selling into 26× sales `[FUND:MSPR]`
  - Sentiment/crowd (7c): **CONFIRM / BALANCED** → no-op (crowd was short, now covering) `[SENT:short_interest]`
  - Correlation cluster (phase-6/8): **none** (BE sole blueprint 2026-07-21) → no-op
  - Sector rotation (phase-6): **neutral** (Industrials outflow offset by AI/Tech alignment) → no-op
  - Debate (8b): bull_residual **0.65** vs bear_residual **0.65** → **disconfirmed → down-shift bin one (0.65→0.55) + cut one step (half → starter = 1.25%)** `[DEBATE:]`
  - Context (0.5): **GENUINELY_UNUSUAL** → no-op (edge already in p)
- **Final size:** **1.25% of book risk** (starter; max-loss of the primary
  spread ≤ 1.25% of book)
- **Deviation reason:** none (no upward deviation; forbidden — gates fired)

## Option structures

### Directional (primary bullish expression — mirrors the smart-money LEAP ladder)

- **Structure:** **call debit spread (LEAP)** — buy Jan-2027 300 call / sell Jan-2027 350 call
- **Strike(s) / expiry:** **300 / 350, 2027-01-15** — anchored to the 300 call wall
  (net +19,769 OI) and the 350-strike LEAP block ($17.2M) the institutions bought `[OI:oi_by_strike]` `[FLOW:top_premium_trades]`
- **Debit/credit:** ~**$15.00 debit** (300C ~$50 / 350C ~$35, avg LEAP IV ~130%)
- **Breakeven:** **$315**
- **Max loss:** **$15.00** (the debit)
- **Why this structure:** rides the institutional LEAP conviction (310/430/510
  ladder) without touching the front-month **IV-crush** — the 300/350 spread is
  **vega-reduced** (long one leg, short the other), so it survives the post-earnings
  vol collapse the risk-monitor flagged `[STRUCT:vanna_charm]`; targets the far bull
  case (BE reclaiming its old $300+ zone) on a 1-3m+ horizon. **Sized inside the
  1.25% book-risk cap** — a fraction of the starter allocation, not additive to it.

### Defined-risk alternative (primary earnings-window trade)

- **Structure:** **put credit spread (bull put)** — sell 205 put / buy 185 put
- **Strike(s) / expiry:** **205 / 185, 2026-08-21** (post-earnings OPEX; short 205
  just below the 210 put wall, long 185 **below the 197.5 GEX trapdoor** per the 8b
  bear's unrefuted point) `[OI:oi_by_strike]` `[STRUCT:gex]`
- **Debit/credit:** ~**$6.50 credit** (rich IV-rank-98.8 premium)
- **Breakeven:** **$198.50** (sits on the triple-confirmed 197.5 floor)
- **Max loss:** **$13.50** (width 20 − credit 6.50) — this is what the 1.25% sizes to
- **Expected-move check (N4):** front-expiry implied move **±10.6% / ±$23.89**
  `[CTX:implied_move_pct]`. A single-catalyst −10.6% gap to ~$202 stays **above** the
  $198.50 breakeven → the priced move does **not** breach the trade; only a
  >12.5% miss (≤ ~$198) turns it losing, and max loss is capped at ≤$185. The
  structure is sized to the priced move, not beyond it. ✓

## Macro overlay (cite phase-6)

- **Tailwinds:**
  - AI-datacenter power demand — rev guide **+106.5% YoY** `[MACRO:BE_earnings_2026-07-28]`
  - Technology sector inflow **+$2.46B today** (BE trades as the AI-power proxy) `[MACRO:sector_flow_2026-07-21]`
- **Headwinds:**
  - Regime **TRANSITIONAL — "half position sizes, defined-risk"** `[MACRO:MarketRegime_2026-07-21]`
  - **10y at 4.60% + core PCE 3.41%** — cost-of-capital drag on a capex-heavy name `[MACRO:DGS10_2026-07-20]` `[MACRO:PCEPILFE_2026-05]`
- **Net:** **mixed** — a real secular tailwind under a size-down regime and a rates headwind.

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|------|-------|------------------|
| **2026-07-28 (AMC)** | **BE Q2 earnings** (EPS $0.41e, rev +106.5%e) | ? (binary, the ±10.6% move) |
| **2026-07-29 (2pm)** | **FOMC** (hold 3.50–3.75% expected) | ? (macro vol the next morning) |
| ~2026-08-01 | July NFP | − / neutral |
| ongoing | Oracle/AEP project timing | − if delayed (guidance risk) |

## Post-trade monitoring checklist

- [ ] **Daily: hold of 197.5** — a daily close below it opens the GEX trapdoor; roll/close the put spread's short leg or take the defined loss.
- [ ] **Into 7/28: IV percentile** — if IV keeps ramping, add credit on the fade entry; the trade *wants* the crush post-print `[HIST:iv_percentile_zscore]`.
- [ ] **Post-7/28: did IV compress and did net_flow stay ≥ 0?** — if IV holds and DP stays DISTRIBUTION, the premium-sell thesis failed `[INSIGHT:institutional_accumulation]`.
- [ ] **7/29 FOMC + AI-sector tape** — a hawkish surprise or renewed AI rout invalidates independent of BE's print `[MACRO:FOMC_2026-07-29]`.
- [ ] **Re-run the deep dive after the print** — the trailing UW reads (IV z, VRP, GEX regime) all shift once the 7/28 session lands (phase-5 latest-anchor caveat).

## Citations summary (M-04 — phase-10 spot-checks these)

1. `[FLOW:sweeps]` — puts net **SOLD $25.7M** (bid $44.0M vs ask $18.3M) — phase-1-flow.md §Sweeps
2. `[HIST:vrp]` — VRP **+0.4935**, regime **PREMIUM_SELLING** (IV 1.77 vs RV 1.28) — phase-5-historical.md §IV regime
3. `[STRUCT:gex]` — GEX **FULLY_NEGATIVE**, worst strike **197.5 (−4.84M)** — phase-4-structure.md §GEX
4. `[HIST:signal_backtest]` — bullish_flow win-rate **0.857 (n=7)** → capped p 0.75 — phase-5-historical.md §Verdict
5. `[DEBATE:]` — bull 0.65 / bear 0.65, **disconfirmed=true** — phase-8b-debate.md
