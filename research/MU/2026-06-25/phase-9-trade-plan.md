# Phase 9 — Trade Blueprint

**Ticker:** MU
**As-of date:** 2026-06-25
**PM voice:** desk PM running an institutional options-overlay book
**Spot reference:** $1,213.56 (phase-5 close / phase-2 closing print)
**Upstream phases cited:** phase-0.5 through phase-8b

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

MU is a fundamentally cheap-on-forward (fwd P/E 8.4, 4/4 beats `[FUND:fwd_pe]`)
leader of a confirmed memory supercycle, and today it is the #1 single-name
net-bullish premium in the universe (+$279M, calls 2.79× `[FLOW:insights_deep_dive]`)
with price-and-flow aligned (no divergence `[INSIGHT:price_vs_flow]`) — the right
side of the cycle. **But the entry is wrong:** spot sits at the 1,211-1,213
double-top after a +15.8% earnings gap on a +325%-YTD parabola, the dark pool is
balanced/distributive (mega buy_ratio 0.47 `[DP:block_stratified]`), dealer structure
is long-gamma with vanna selling and max-pain pulling to 1,040 `[STRUCT:max_pain]`,
and the desk is non-directional (2 NEUTRAL / 1 RANGE / 1 caveated-LONG `[AGENT:desk]`).
**Net: structural long, but only on a pullback to the $1,134 absorbed shelf — do not
chase the ATH; token size here.**

## Bias + conviction + horizon

- **Directional bias:** LONG (structural) — *near-term actionable = wait/fade-the-rip*
- **Conviction (M-01 bin):** **0.55** (slight edge — floored)
- **Time horizon:** 1-3m (the cycle); the actionable long is a pullback entry
- **Why this bin:** every downside gate fired (7b CAUTION, 7c CAUTION, 8b
  disconfirmed) and the desk is non-directional — a slight edge at best; the debate
  wanted to down-shift further but 0.55 is the floor. (Phase-10 confluence band to
  confirm; deviation note below if it disagrees.)

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| **Primary** | **~$1,134** | Pullback to the heaviest 5-session dark-pool shelf; go long on first hold/reclaim | `[DP:price_levels]` |
| Aggressive | **>$1,255** | Decisive daily close above the intraday high on rising IV (vanna flips seller→bid, no short base to slow it) | `[INSIGHT:price_vs_flow]` / `[SENT:short_float fz]` |
| Fade (plan-B) | **$1,211-$1,255** | Rejection at the double-top / intraday high → tactical put-debit fade (counter-trade) | `[HIST:trend]` / `[STRUCT:gex]` |

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| Support (primary) | **$1,134** (5-session DP shelf, $5.14B/4.53M sh) | `[DP:price_levels]` |
| Support (deep / pivot) | **$1,052** (6-23 pivot low); then $1,000 put-wall | `[HIST:trend]` / `[OI:oi_by_strike]` |
| Resistance | **$1,211-$1,213** (6-22 high = 6-25 close double-top); $1,255 intraday | `[HIST:trend]` / `[INSIGHT:price_vs_flow]` |
| Gamma regime | **POSITIVE / long-gamma** (mean-reverting; ZGL 41.47 is an artifact, no flip near spot) | `[STRUCT:gex]` |
| Pin magnet (max-pain) | **$1,040** (6-26); 7-17 max-pain $800 (soft/static) | `[STRUCT:max_pain]` |

**Price-context color (advisory):** entering at the **52-week high (1,213.56, 0.00%
off) with RSI 64.5 `[HIST:52w_proximity fz]` `[HIST:rsi fz]`** and +325% YTD — clear
chase risk; this is *why* the primary entry is the $1,134 pullback, not spot. (Color
only — does not alter the Kelly `p` or final size.)

## Invalidation

- **Price-based:** Two daily closes **below $1,052** (the 6-23 pivot low / shelf
  failure) confirm the parabola round-trip → exit/abandon the long thesis. (For the
  fade plan-B: a decisive close **above $1,255** invalidates the fade.)
- **Signal-based:** Dark-pool tiers flip to outright **distribution** (mega buy_ratio
  ≤ 0.45 with clusters below spot) on the phase-2 daily refresh, OR cumulative
  premium flow turns net-bearish **3 consecutive sessions** `[HIST:cumulative_premium_flow]`,
  OR conviction-matrix flips MIXED → bearish `[INSIGHT:conviction_matrix]`.
- **Macro-based:** A **DRAM/HBM contract-price rollover** or hyperscaler capex cut
  `[MACRO:memory_cycle_2026]` (the one fundamental that re-rates the fwd-8.4 multiple),
  or a hawkish FOMC surprise (~July 28-29) flipping the UW regime hard risk-off
  `[MACRO:MarketRegime_2026-06-25]`.

## Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** p_raw = **0.60** (n=5, source=backtest) → N-cap (n<10) =
  0.75 → **capped p = 0.60** `[HIST:signal_backtest]` *(market-wide bullish_flow base
  rate, not MU-specific; small N).*
- **Kelly inputs:** b = **1.5** (target $1,255 / stop $1,052 from a $1,134 entry =
  121/82), fraction = 0.25, cap_pct = 5.
- **Raw Kelly:** (0.60·1.5 − 0.40)/1.5 = **0.333** → ×0.25 = 8.3% → cap_pct 5%.
  **Win-rate map ceiling (p=0.60 → 0.50-0.70 band):** **half ≤ 2.5%** → take the
  smaller = **2.5% pre-gate.**
- **Risk gates (each cuts, none adds):**
  - Fundamentals (7b): **CAUTION** (insiders net-selling the parabola) → **cut one
    step** (half → starter): 2.5% → ~1.25%.
  - Sentiment/crowd (7c): **CAUTION / CROWDED_LONG** (analysts maxed, shorts
    capitulated 3.71%, retail chasing) → **cut one step:** ~1.25% → ~0.6%.
  - Correlation cluster (phase-6): **none** (MU is the only 2026-06-25 blueprint) →
    no-op. *(Soft-watch: MU↔SNDK co-move as the memory pair.)*
  - Sector rotation (phase-6): **ALIGNED** (tech net inflow, persistence 1.0) →
    no-op (aligned does not cut; flagged narrow/MU-concentrated).
  - Debate (8b): **disconfirmed = TRUE** (bear_residual 0.65 ≥ bull_residual 0.60) →
    **down-shift bin (floored at 0.55) + cut one step:** ~0.6% → **~0.3%.**
- **Context modifier (0.5):** unusual_verdict = **GENUINELY_UNUSUAL** → no-op (edge
  in `p`).
- **Final size:** **~0.3% of book risk (token / starter).** Three gates fired — the
  chain says *barely participate at spot; the real size is reserved for the $1,134
  pullback.*
- **Deviation reason:** none (no upward deviation; forbidden here — gates fired).

## Option structures

### Directional (primary) — LONG, debit, on the $1,134 pullback

- **Structure:** Call debit (vertical) spread — defined-risk, debit (VRP =
  PREMIUM_BUYING, RV 122% > IV 91% `[HIST:vrp]` favors *owning* premium, not selling).
- **Strike(s) / expiry:** **buy 1150 call / sell 1350 call, expiry 2026-09-18**
  (strikes set at a ~$1,134 entry; 1150 anchors near the call_heavy zone, 1350 is the
  next-leg cap; **expires 4 days before the 9-22 earnings** → captures the cycle +
  pre-earnings IV ramp, avoids the print's binary/crush).
- **Debit/credit:** ~$60 debit (illustrative, ~90% IV) · **Breakeven:** ~$1,210 ·
  **Max loss:** $60 (the debit) · **Max gain:** ~$140 (width 200 − debit).
- **Why this structure:** debit spread caps cost into very high absolute IV while
  staying long the cycle; entered on weakness ($1,134) not strength, so you are not
  chasing the +15.8% gap. Sized to the ±3.93% front-expiry move — a 200-wide spread
  is ~4× the priced move, appropriate for a 1-3m cycle horizon.

### Defined-risk alternative — bullish-leaning income, sells the support shelf

- **Structure:** Put credit spread (defined-risk; "get paid to be a buyer at
  support"). *Caveat: RV (122%) > IV — keep this small; it is the lower-conviction
  income leg, and the $1,134 shelf must hold.*
- **Strike(s) / expiry:** **sell 1100 put / buy 1000 put, expiry 2026-07-17** (short
  strike 1100 is −9.4% from spot ≈ 2.4× the front expected move, below the $1,134
  shelf; long 1000 sits on the OI `put_wall_support` `[OI:oi_by_strike]`).
- **Debit/credit:** ~$22 credit · **Breakeven:** ~$1,078 · **Max loss:** ~$78 (width
  100 − credit). Profits if MU holds above $1,100 into 7-17 OPEX.
- **Why:** monetizes the "1,134 absorbed shelf holds" thesis with a hard-defined max
  loss and the 1,000 OI wall as backstop; its risk (a break <1,100) **is** the
  primary thesis's invalidation, so the two legs are coherent.

## Macro overlay (cite phase-6)

- **Tailwinds:** AI memory supercycle — DRAM +90% QoQ, HBM sold out 2026, capex +40%
  `[MACRO:memory_cycle_2026]`; easing Fed (funds 3.63%) + falling 10y (4.41%)
  `[MACRO:DFF_2026-06-24]`; tech sector net inflow +$3.68B, persistence 1.0
  `[MACRO:sector_flow_2026-06-25]`.
- **Headwinds:** UW regime **TRANSITIONAL, "reduce size,"** breadth 35.4%
  `[MACRO:MarketRegime_2026-06-25]`; narrow leadership (the inflow *is* MU; SNDK
  +883% froth); SPY below 20-SMA `[MACRO:MarketRegime_2026-06-25]`.
- **Net:** mixed — strong structural tailwind, cautious tactical tape (the size cap).

## Catalyst calendar (next 30d)

Front-expiry implied move **±3.93% / ±$47.4** `[CTX:implied_move]`.

| Date | Event | Impact direction |
|------|-------|------------------|
| ~2026-07-14/15 | June CPI release | ? (macro, rates) |
| 2026-07-17 | July monthly OPEX (17.27% of OI, put-heavy) | ? (pin/positioning) |
| ~2026-07-28/29 | FOMC + rate decision | ? (easing-cycle cut watch) |
| ongoing | DRAM/HBM contract pricing + hyperscaler capex prints | + if firm / − if rollover |
| 2026-09-22 | MU next earnings (beyond 30d) | + / − (next binary) |

## Post-trade monitoring checklist

- [ ] Re-check phase-2 dark-pool tiers daily — a mega buy_ratio ≤ 0.45 with
  below-spot clusters = distribution confirmed → abandon the long.
- [ ] Watch the **$1,134 shelf** and **$1,052 pivot** — primary entry vs invalidation.
- [ ] Re-run phase-4 GEX/vanna — if IV re-firms and GEX magnitudes flip, the vanna
  seller becomes a bid (supports the aggressive >1,255 entry).
- [ ] Track DRAM/HBM contract-price headlines — the single fundamental that re-rates
  the fwd-8.4 multiple.
- [ ] Re-check cumulative premium flow — 3 consecutive net-bearish sessions = exit signal.
- [ ] Watch SNDK (memory pair) — a parabolic-froth unwind there leads MU.

## Citations summary (≥3 distinct, for phase-10 spot-check)

1. `[FLOW:insights_deep_dive]` — net_flow +$279M, call premium 2.79× put (phase-1-flow.md §Whole-tape aggregate)
2. `[DP:block_stratified]` — dark-pool tiers balanced, mega buy_ratio 0.47 (phase-2-dark-pool.md §Tier breakdown)
3. `[STRUCT:max_pain]` — near-expiry max-pain 1,040 (−14.5%), 7-17 → 800 (phase-4-structure.md §Max pain)
4. `[FUND:fwd_pe]` — forward P/E 8.4, PEG 0.05, 4/4 beats (phase-7b-fundamentals.md §Valuation)
5. `[HIST:signal_backtest]` — bullish_flow win-rate 0.60, n=5 (phase-5-historical.md §Sizing handoff)
6. `[AGENT:desk]` — 2 NEUTRAL / 1 RANGE / 1 LONG, avg conviction 2.25 (phase-8-agent-views.md)
7. `[DEBATE]` — disconfirmed, bull 0.60 / bear 0.65 (phase-8b-debate.md)
