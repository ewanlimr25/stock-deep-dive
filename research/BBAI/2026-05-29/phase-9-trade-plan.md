# Phase 9 — Trade Blueprint (PM synthesis)

*For research and educational use only. Not financial advice. Sizing and
structures are illustrative.*

**Ticker:** BBAI **As-of:** 2026-05-29 **Spot:** ~$5.04 **Generated:** 2026-05-31
**Horizon:** 1–4w (into the 2026-06-18 OPEX cliff)

## Thesis (≤3 sentences)

BBAI ran **+30.9%** into a **long-gamma $5 dealer pin** (+$82.0M GEX, ZGL $2.64
[STRUCT:gex]) while whole-tape **net call premium turned negative (−$999,867
[FLOW:insights_deep_dive])** — a textbook **price-vs-flow DIVERGENCE
[INSIGHT:price-vs-flow]**, i.e. a capped, complacent bounce, not a confirmed
trend. With IV rich vs realized (**VRP +0.28, PREMIUM_SELLING [HIST:vrp]**), no
catalyst until 8/10, and a **TRANSITIONAL "reduce-size" regime [MACRO:MarketRegime]**,
the edge is to **sell premium around the $5 pin, not chase**. Size is starter-only:
a **26.37% short float [SENT:short_float fz]** is a live squeeze tail and the desk
came back **0-of-5 long**.

## Bias + conviction

- **Bias: RANGE** (fade-the-extension / premium-sell, pinned to $5). Plurality of
  phases 1–8: 0 LONG · 1 defined-risk SHORT · 4 NEUTRAL/range/sell-vol.
- **Conviction: 0.55** (slight edge — the lowest bin). Conflicting signals
  (bearish premium + long-gamma pin vs 26% squeeze tail + dark-pool buy-lean), no
  historical edge (backtest 50% on n≈8), and two downside-only CAUTION gates keep
  this at the floor. Matches phase-10's low confluence band (see phase-10).

## Entry zones

- **Primary:** initiate with spot holding the **$5.00–$5.10 GEX pin** and rejecting
  the $5.50 call wall; trigger = a failed push at $5.40–$5.50 [STRUCT:gex].
- **Aggressive:** leg the call-credit side on an intraday tag of **$5.45–$5.55**
  (the $5.5 call wall / next +GEX strike) [OI:oi-by-strike].
- **Fade (plan B if thesis partially invalidates):** if price **closes above $5.50**
  (gamma-flip-through / squeeze), **stop the short call side** and stand down — do
  not fight a confirmed break; re-assess long only above $5.50 on positive net call
  premium [STRUCT:gex].

## Levels to watch

- **Support $5.00** — +$82.0M GEX pin / DP shelf [DP:price-levels] / call_heavy strike [OI:oi-by-strike].
- **Resistance $5.50** — largest +GEX strike & call wall (ZGL-of-upside) [STRUCT:gex][OI:oi-by-strike].
- **Gamma flip (ZGL) $2.64** — far below; long gamma is secure unless price collapses [STRUCT:gex].
- **Pin magnet $5.00** (dealer gamma) with **max-pain $4.00 (−21%)** the lower
  static-OI magnet into 6/18 [STRUCT:max-pain].
- **Price-context color (advisory):** the bounce is **−46% from the 52-wk high
  $9.39 and below the 200-day** [HIST:52w_proximity fz] — a relief bounce into
  overhead supply (~$5.30 falling 200-DMA), not a breakout. Prefer the fade entry.

## Invalidation (falsifiable)

- **Price:** a **daily close > $5.50** (squeeze through the call wall) **or < $4.50**
  (air-pocket through thin put support) breaks the $5-pin range thesis.
- **Signal:** `net_call_premium` flips **strongly positive** with **ask-side
  near-dated call buying** (squeeze confirmed) [FLOW], or the GEX regime turns
  negative.
- **Macro:** a hot June CPI / hawkish FOMC risk-off in small-caps, **or** a fresh
  defense-contract headline that re-ignites the momentum bid [MACRO:Fed].

## Sizing (% of book risk) — Kelly + gates

- **p:** phase-5 backtest is **50% on n≈8 (below the usable-N floor)** →
  `win_rate_source = fallback_bin` → **p = 0.55** (conviction bin, ≤0.65 cap).
  `p_raw` = 0.50.
- **b (payoff):** primary iron condor ≈ credit $0.35 / max-loss $0.15 per side ⇒
  **b ≈ 2.33**.
- **raw_kelly** = (0.55·2.33 − 0.45)/2.33 = **0.357**.
- **suggested** = min(0.357 × 0.25 × 100, 5) = min(8.9, 5) = **5.0%**; **win-rate map**
  (p 0.50–0.70 → half ≤ 2.5%) ⇒ take the smaller = **2.5% ceiling**.
- **Risk gates (downside-only):**
  1. **Fundamentals (7b) = CAUTION** → cut one step (half → starter). *Fired.*
  2. **Sentiment/crowd (7c) = CAUTION** (CROWDED, 26% SI) → cut one step. *Fired.*
  3. **Correlation = none** (no concurrent 2026-05-29 blueprint). *No-op.*
  4. **Sector rotation = neutral** (Tech inflow, BBAI peripheral). *No-op.*
  5. **Debate (8b) = not disconfirmed** (fade defender residual 0.65 ≥ squeeze
     attacker 0.55). *No-op* (but the squeeze tail is carried as a key risk).
- **Context modifier:** phase-0.5 `BUSY_NAME_NORMAL_DAY` → do not size at the top
  of the band.
- **Final size = ~1.0% of book risk (starter)** — two CAUTION gates drive the 2.5%
  half-ceiling down to starter; no upward deviation. Express as **defined-risk max
  loss ≤ 1.0% of book**.

## Option structures

Both expiries are **2026-06-18** (the OPEX cliff; **no earnings until 8/10**, so no
earnings IV-crush risk). Front-expiry **implied move ≈ ±6.79% (±$0.34)** — short
strikes sit just outside 1σ.

- **Defined-risk (PRIMARY) — Iron condor, 2026-06-18:**
  short **$4.50 put** / long **$4.00 put** + short **$5.50 call** / long **$6.00 call**.
  Net credit ≈ **$0.35**; max loss ≈ **$0.15 per side** (width $0.50 − credit);
  breakevens ≈ **$4.15 / $5.85**. Sells the rich, complacent IV around the $5 pin;
  short strikes ($4.50/$5.50) are outside the ±6.8% expected move. **Wings are
  load-bearing** (squeeze defense). **Close/roll before the 6/18 un-pin.** Max loss
  ≤ 1.0% of book.
- **Directional (starter, fade-side) — Bear put debit spread, 2026-06-18:**
  long **$5.00 put** / short **$4.00 put**. Debit ≈ **$0.25**; max loss = debit
  $0.25; breakeven ≈ **$4.75**; target **$4.00** (max-pain), max profit ≈ $0.75
  (~3:1). **Starter only** — `p<0.50` bearish backtest + squeeze risk; defined-risk.
  Max loss ≤ 0.5% of book.

## Macro overlay

- **Tailwinds:** Technology sector net inflow **+$533M** [MACRO:sector_rotation];
  BBAI defense backlog **$281.9M (+14% QoQ)** [MACRO:BBAI_news].
- **Headwinds:** regime **TRANSITIONAL — "reduce size," breadth 36.3%**
  [MACRO:MarketRegime]; **no 2026 rate cuts + sticky CPI +3.7%** [MACRO:Fed].
- **Net: mixed, leaning headwind** for a speculative high-beta long.

## Catalyst calendar (next 30d)

| Date | Event | Impact |
|------|-------|--------|
| 2026-06-05 | Weekly OPEX | ? (gamma/pin mechanics) |
| ~2026-06-10/12 | May CPI | − (risk-off if hot) |
| ~2026-06-17 | FOMC | − (hawkish-hold risk) |
| 2026-06-18 | Monthly OPEX (OI cliff) | ? (the $5-pin un-pin) |

(Next earnings 2026-08-10 — outside the window.)

## Post-trade monitoring checklist

1. **Daily net_call_premium** — a flip to strongly positive on ask-side near-dated
   calls = squeeze starting; cover the short-call wing.
2. **$5.50 close** — a daily close above flips the gamma cap into squeeze fuel
   (invalidation); $4.50 close = downside air-pocket.
3. **Short-interest / borrow** — next semi-monthly SI print; a borrow-fee spike or
   rising DTC raises squeeze odds.
4. **Defense-contract headlines** — a fresh award re-ignites momentum vs the fade.
5. **Roll/close the condor before 6/18 OPEX** — the +$82M $5 gamma rolls off (un-pin).

## Citations summary (phase-10 spot-checks these)

1. `[FLOW:insights_deep_dive]` net_call_premium **−$999,867** (vs price +30.9%).
2. `[STRUCT:gex]` long-gamma **$5 pin +$82.0M GEX, ZGL $2.64** (regime POSITIVE).
3. `[HIST:vrp]` **VRP +0.28, PREMIUM_SELLING** (IV 102.7% vs realized 74.6%).
4. `[SENT:short_float fz]` **26.37% short float** (~3 DTC) — squeeze tail.
5. `[INSIGHT:price-vs-flow]` explicit **DIVERGENCE** (price +30.9% / flow bearish).
