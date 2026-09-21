# Phase 9 — Trade Blueprint

**Ticker:** PATH (UiPath Inc.)
**As-of date:** 2026-05-22
**PM voice:** desk PM running an institutional options-overlay book
**Spot reference:** $10.93 close / ~$10.99 spot (phase-2 DP avg $10.95; phase-1 print underlying)
**Upstream phases cited:** phase-0.5 through phase-8b

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

PATH is a beaten-down, profitable software name (PE 20, 83% gross margin, **2/2 recent EPS
beats** [FUND:earnings_surprise]) being quietly accumulated in the dark pool (**block
buy_ratio 1.0, $13.95M** [DP:block_stratified]) against a **~28–31% short float**
[SENT:short_interest] — a squeeze-fueled, mild-long setup into the 2026-05-28 earnings. But
the *edge is structural, not directional*: **VRP +43.7 vol points** [HIST:vrp] and a **140%
5/29 IV bubble** [STRUCT:iv_term_structure] make the overpriced premium the real prize, and
the bull/bear debate **disconfirmed the directional long** (bear 0.65 ≥ bull 0.55
[DEBATE:bear_residual]). So express it defined-risk and small — harvest the rich IV with a
neutral-to-mildly-long structure, cap the downside below the **$10.50 negative-GEX gate**
[STRUCT:gex], and let the **$11 gamma pin** [STRUCT:gex] do the work into the print.

## Bias + conviction + horizon

- **Directional bias:** **NEUTRAL** (mild long tilt; range/vol-harvest expression). Plurality
  of phases 1–8 = 2 LONG + 3 NEUTRAL, **0 SHORT** — no one defends a short into ~30% short
  interest.
- **Conviction (M-01 bin):** **0.55**
- **Time horizon:** **1-4w** (initiate now to capture peak IV; the 05-28 print + 05-29 IV
  crush is decisive; structures expire 06-18).
- **Why this bin:** phase-10 confluence ≈ **57** (band 50–64 → 0.65), then the **phase-8b
  debate disconfirmation down-shifts one bin to 0.55** (`rubrics/sizing-rubric.md` §Risk gates).
  This is a genuinely two-sided, BUSY_NAME, binary-event setup — a slight edge, not a
  conviction trade.

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| Primary | ~$10.93–$11.00 (now) | Initiate the neutral structure **pre-event** to sell peak IV with spot at the $11 gamma pin | [STRUCT:gex] |
| Aggressive | $10.50–$10.65 | Leg the put side on a tag of the DP support shelf / neg-GEX gate (richer put credit, support defended) | [DP:price_levels] |
| Fade | $12.00 | Rejection at the positive-GEX call cap → take profit / counter any directional long | [STRUCT:gex] |

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| Support | **$10.50–$10.65** (DP shelf + neg-GEX gate); deeper $10.00 put wall | [DP:price_levels] · [STRUCT:gex] · [OI:biggest_increases] |
| Resistance | **$11.00** ($20.5M gamma wall / pin); then $12.00 cap | [STRUCT:gex] · [OI:biggest_increases] |
| Gamma flip (ZGL) | $7.26 (far below — only relevant on a catastrophic miss) | [STRUCT:gex] |
| Largest pin | **$11.00** (gamma wall; PATH not in market-wide oi_pin_risk) | [STRUCT:gex] |

## Invalidation

- **Price-based:** **two daily closes below $10.50** (the DP support shelf + neg-GEX gate).
  Below it dealers flip short-gamma and the move accelerates toward the $8.5–$9 air pocket
  [STRUCT:gex] — voids the long-lean and threatens the put wing.
- **Signal-based:** dark-pool **ACCUMULATION flips to DISTRIBUTION** [INSIGHT:institutional_accumulation],
  OR `conviction_matrix` flips DIRECTIONAL_LONG → HEDGED_LONG [INSIGHT:conviction_matrix],
  OR cumulative premium flow turns net-bearish 3 consecutive sessions [HIST:cumulative_premium_flow].
- **Macro-based:** **the 05-28 earnings guide misses** (the dominant binary) — a guide-down
  gaps PATH through $10.50 toward $8.5–$9 [STRUCT:gex] · [FUND:forward_consensus]; OR a
  TRANSITIONAL → RISK-OFF regime flip [MACRO:MarketRegime_2026-05-22].

## Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** `p_raw = null` — phase-5 `dark_pool_accumulation` backtest returned
  **0 signals** (`win_rate_source = null`) [HIST:signal_backtest], so **fall back to the
  conviction bin** (capped at 0.65). Operative bin after the debate down-shift = **0.55** →
  **p = 0.55**. (Cautionary cross-ref: `bearish_flow` backtested 28.6% (n=7) — argues against
  any bearish framing, not used as `p`.)
- **Kelly inputs:** b = **1.7** (directional call spread: max gain $0.95 / max loss $0.55),
  fraction = 0.25, cap_pct = 5.
- **Raw Kelly:** (0.55×1.7 − 0.45)/1.7 = **0.285** → 0.285 × 0.25 × 100 = 7.1% → cap 5%.
  **Win-rate map ceiling:** p in 0.50–0.70 → **half (≤ 2.5%)** → take the smaller = **2.5%**.
- **Risk gates:**
  - Fundamentals (phase-7b): **CONFIRM** → no-op.
  - Sentiment/crowd (phase-7c): **CONFIRM**, crowd_state CROWDED_SHORT (supports the long-lean,
    vetoes a short) → no-op.
  - Correlation cluster (phase-6/8): coefficients **unusable** (sectors "Unknown"); no confirmed
    ≥0.70 cluster — **soft-watch only** (PATH/SYM automation theme; **NTAP same-day 5/28
    earnings**) → surface, no cut.
  - Sector rotation (phase-6): **aligned** (Tech persistent inflow, score 1.0) → no cut.
  - Debate (phase-8b): **bull_residual 0.55 vs bear_residual 0.65 → disconfirmed = true** →
    **down-shift bin (done: 0.65→0.55) AND cut one size step (half → starter)**.
  - Context modifier (phase-0.5): **BUSY_NAME_NORMAL_DAY** → do not size top of band (already
    starter). TRANSITIONAL macro half-size reinforces.
- **Final size:** **1.25% of book risk** (starter). Max-loss of the chosen structure must be
  ≤ 1.25% of book.
- **Deviation reason:** none (size was only cut, never raised — compliant with every gate).

## Option structures

Both are defined-risk and sized to the **±11.8% implied move (~±$1.30 → $9.70–$12.30)**
[CTX:implied_move_pct]. A single-catalyst gap of the implied-move magnitude does **not**
exceed max loss on either (both are fully width-capped) — so holding through 05-28 is safe.

### Directional (mild-long / squeeze lean) — 06-18 call debit spread

- **Structure:** buy 2026-06-18 **$11 call** / sell 2026-06-18 **$12.50 call** (debit spread).
- **Strikes / expiry:** $11 (= gamma wall/pin) / $12.50 (above the $12 call cap, into the
  squeeze target); expiry 06-18 (post-earnings, IV ~100% vs 140% on 5/29 — less crush-exposed).
- **Debit/credit:** ~**$0.55 debit** (illustrative at current IV).
- **Breakeven:** ~$11.55.
- **Max loss:** **$0.55** (the debit).
- **Max gain:** $0.95 (width $1.50 − debit).
- **Why this structure:** spread (not long call) blunts the post-earnings IV crush; it leans
  into a beat-driven squeeze of the 30% short float through the $12 cap, with risk capped
  below the implied move. Use only if you want the directional tilt.

### Defined-risk alternative (the desk's primary recommendation) — 06-18 iron condor

- **Structure:** sell **$9.50 put** / buy **$8.50 put** + sell **$12.50 call** / buy **$13.50 call**.
- **Strikes / expiry:** short strikes $9.50 / $12.50 bracket the ±11.8% implied move; long
  wings $8.50 (caps the air-pocket floor) and $13.50; expiry 06-18.
- **Debit/credit:** ~**$0.55 net credit** (illustrative; harvests the rich 100–140% IV).
- **Breakevens:** ~$8.95 and ~$13.05.
- **Max loss:** ~**$0.45** per side (width $1.00 − credit $0.55).
- **Why this structure:** this is the truest expression of the dive — sell the structurally
  overpriced IV (VRP +43.7, 5/29 bubble 140%) [HIST:vrp] · [STRUCT:iv_term_structure] with the
  $11 long-gamma pin centered in the profit zone, defined risk on both wings, and the put wing
  pulled to $9.50 (below DP support, above the $8.5 air-pocket floor). Profits if realized move
  < implied — the premium-selling edge. **Tail risk:** a beat-driven squeeze > $12.50 or a
  miss-driven gap < $9.50; both are width-capped at ~$0.45.

## Macro overlay (cite phase-6)

- **Tailwinds:** [MACRO:sector_flow_persistence_2026-05-22] Technology = #1 persistent inflow
  sector (score 1.0, accelerating); [MACRO:DFF_2026-05-21] fed funds easing to 3.62% supports
  rate-sensitive software.
- **Headwinds:** [MACRO:MarketRegime_2026-05-22] regime TRANSITIONAL, breadth 38% bullish →
  half-size/defined-risk; [MACRO:CPIAUCSL_2026-04] April CPI MoM +0.64% (firm) → easing-path risk.
- **Net:** **mixed/neutral** — macro neither makes nor breaks the trade; the 05-28 event dominates.

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|------|-------|------------------|
| **2026-05-28** | **PATH Q1 FY27 earnings** (±11.8% implied) | ? (the trade) |
| ~2026-06-11 | May CPI release | ? (rate-sensitivity, post-event) |
| ~2026-06-17 | FOMC + SEP | ? (post-event) |

## Post-trade monitoring checklist

- [ ] Re-check phase-2 dark-pool daily: does ACCUMULATION (buy/sell 6.11×) **persist or flip
      to distribution**? A flip is a signal-based invalidation.
- [ ] Watch the **$10.50 gate**: two daily closes below it → exit/roll the put wing (air pocket).
- [ ] Re-run phase-4 GEX daily: confirm spot stays above ZGL and the $11 wall holds; a DEX flip
      negative pre-event is a warning.
- [ ] **05-28 earnings**: the binary — be flat or fully defined-risk into the print; close/roll
      the day after on the IV crush (vanna/charm = mechanical dealer selling post-crush).
- [ ] Track **short interest / borrow**: a sharp SI drop = the squeeze firing (manage the call
      wing); a borrow spike = stress.
- [ ] Watch **NTAP (same-day 5/28 earnings)** and the broad tech tape as a read-through/cluster.

## Citations summary (M-04 — ≥3 distinct, spot-checked by phase-10)

1. [DP:block_stratified] dark-pool block buy_ratio **1.0**, $13.95M, 0 sells — phase-2-dark-pool.md §Tier breakdown.
2. [SENT:short_interest] **~28–31% of float short**, ~5.2 days-to-cover — phase-7c-sentiment.md §Short interest.
3. [HIST:vrp] **VRP +0.4367** (IV30d 98.7% vs realized 55%), PREMIUM_SELLING — phase-5-historical.md §IV regime.
4. [STRUCT:gex] $11 gamma wall **+$20.5M**, negative-GEX pocket $8.5–$10.5, ZGL $7.26 — phase-4-structure.md §GEX.
5. [DEBATE:bear_residual] bear 0.65 ≥ bull 0.55 → disconfirmed — phase-8b-debate.md §Disconfirmation verdict.
6. [FUND:earnings_surprise] 2/2 recent beats (+15.5%, +7.4%) — phase-7b-fundamentals.md §Earnings-surprise.
