# Phase 9 — Trade Blueprint

**Ticker:** NBIS (Nebius Group NV)
**As-of date:** 2026-06-17
**PM voice:** desk PM running an institutional options-overlay book
**Spot reference:** $280.91 (phase-0.5 close; GEX `underlying_price` $283.96 intraday)
**Upstream phases cited:** phase-0.5 through phase-8b

> *For research and educational use only. Not financial advice. Sizing and structures are illustrative.*

## Thesis (≤3 sentences)

NBIS is a parabolic AI-infra name where the ONLY clean bull case is mechanical — a Nasdaq-100 forced
inclusion on June 22 `[MACRO:NDX_inclusion]` riding a genuine 5-of-5-session, $722.4M bullish sweep
campaign `[FLOW:sweep_persistence]` and a dealer dip-bid (DEX +$2.88bn, dealers short calls must buy)
`[STRUCT:dex]`. But the underlying is being **distributed into that strength** — mega-tier dark pool is
93.6% sell `[DP:block_stratified]`, insiders printed MSPR −100 with a ~1.04M-share May sale
`[FUND:MSPR]`, price trades ABOVE the $255.29 analyst target `[FUND:recom fz]`, and the bullish_flow
signal class is historically edge-negative at 37.5% (n=8) `[HIST:signal_backtest]`. **Net: a tiny,
defined-risk, event-boxed long into June 22 at best; the higher-quality trade is the post-inclusion fade.**

## Bias + conviction + horizon

- **Directional bias:** LONG (tactical / event-boxed — *barely a trade*; the plurality of phases 1–8 tilts long, but the data is near-mixed)
- **Conviction (M-01 bin):** **0.55** (slight edge)
- **Time horizon:** 1-5d (flat by/at the June-22 inclusion; do not carry into the post-event fade as a long)
- **Why this bin:** phase-10 confluence ≈ **32** (base 42 − 5 debate − 5 sentiment-CAUTION) → 30–49 band → 0.55–0.65, and the phase-8b disconfirmation down-shifts to the **0.55 floor**. The dominant LONG bias is being actively fought by the data.

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| Primary | $278.84–$281 | Holds the positive-gamma dip-bid and the $278.84 52W-high breakout into Jun-22; enter defined-risk long only | [STRUCT:gex] / [HIST:52w_proximity fz] |
| Aggressive | $297.93 | Reclaim of the recent high on rising lit demand → momentum run at the $300 call wall | [INSIGHT:price_vs_flow] / [OI:oi_by_strike] |
| Fade (plan B — higher conviction) | $297.93–$300 rejection, OR post-Jun-22 close < $267.5 | Rejection at the call wall OR loss of the max-pain magnet → bearish fade toward $260 | [STRUCT:max_pain] / [DP:price_levels] |

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| Support | $267.5 (06-26 max-pain magnet, −4.7%) → $260.07 (largest 5-day DP cluster $362.8M) | [STRUCT:max_pain] / [DP:price_levels] |
| Resistance | $297.93 (30d intraday high) → $300.00 (call_wall_resistance, +6.9%) | [INSIGHT:price_vs_flow] / [OI:oi_by_strike] |
| Gamma flip (ZGL) | $34.64 — informational only (≪ spot; confirms robust long-gamma, not a tradeable level) | [STRUCT:gex] |
| Pin magnet | $267.5 (nearest-expiry max-pain, 06-26) | [STRUCT:max_pain] |

*Price-context color (advisory):* entering at the 52-week high with RSI 68.6 and price +127% above the
200-day `[HIST:rsi fz]` `[HIST:52w_proximity fz]` — chase risk is high; this is why the primary entry is
defined-risk-only and the fade is the preferred follow-on. (Color only; does not alter the Kelly `p`.)

## Invalidation

- **Price-based:** for the long — an intraday loss of the positive-gamma dip-bid with two daily closes
  below **$267.5** (the 06-26 max-pain magnet / loses the dealer dip-bid) `[STRUCT:max_pain]`. For the
  structural short/fade — two daily closes above **$300** (clears the call wall on the inclusion bid).
- **Signal-based:** DEX flips from +$2.88bn toward negative on the phase-4 daily refresh `[STRUCT:dex]`,
  OR institutional-accumulation flips from NEUTRAL to clear distribution `[INSIGHT:institutional_accumulation]`,
  OR the negative-vanna vol-crush fires post-OPEX (IV30d falls hard off the 95.7%ile) `[STRUCT:vanna]`.
- **Macro-based:** any incremental hawkish surprise (June CPI ~07-15 hotter than the +4.17% YoY trend, or
  Fed speak reinforcing the hike-biased dots) `[MACRO:FOMC_2026-06-17]` — directly compresses a
  normalized-P/E-808 long-duration name.
- **Exit on invalidation:** **hard stop** (debit structures) — close 100% on the price/signal trigger;
  for the iron condor, roll or close the tested wing.

## Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** p_raw = **0.375** (n=**8**, source=**backtest**, bullish_flow, market-wide)
  → N-cap (n<10 → 0.75) → capped **p = 0.375** `[HIST:signal_backtest]`. **p < 0.50 ⇒ the signal is
  edge-NEGATIVE → win-rate map forces STARTER / SKIP regardless of Kelly (SHORT-side floor).**
- **Kelly inputs:** b = **1.73** (entry $281 / target $300 / stop $270), fraction = 0.25, cap_pct = 5.
- **Raw Kelly:** (0.375×1.73 − 0.625)/1.73 = **0.014 → suggested 0.34%** · **Win-rate map ceiling: STARTER** (p<0.50).
- **Risk gates:**
  - Fundamentals (phase-7b): **CAUTION** (insider selling) → cut one size step.
  - Sentiment/crowd (phase-7c): **CAUTION**, crowd_state **CROWDED_LONG** (borderline VETO; held off only by the Jun-22 forced bid) → cut one size step.
  - Correlation cluster (phase-6/8): **none** (NBIS is the sole blueprint for the date) → no-op.
  - Sector rotation (phase-6): **aligned/neutral** (Tech 5d INFLOW persistence 0.8) → no cut.
  - Debate (phase-8b): bull_residual **0.55** vs bear_residual **0.65** → **disconfirmed=true** → down-shift bin (already 0.55 floor) + cut one size step.
  - Context (phase-0.5): **GENUINELY_UNUSUAL** → no-op (edge already in p), but directional conviction was flagged capped (two-sided net +$18M / $640M gross).
- **Final size:** **≈0.3% of book risk (token/starter)** — the raw Kelly 0.34% is already starter-tier;
  the three firing gates + the p<0.50 floor confirm starter-or-skip. **Honest desk call: this rounds to
  "stand aside / token defined-risk lottery into Jun-22," not a real position.**
- **Deviation reason:** none (no upward deviation — forbidden here, three gates fired).

## Option structures

### Directional (primary) — tiny event-box on the inclusion bid

- **Structure:** call debit spread (defined-risk; do NOT express via long premium at IV rank 91 / 113% IV).
- **Strike(s) / expiry:** **+$290 / −$300 call spread, expiry 2026-06-26** (captures Jun-22 inclusion; short strike sits at the $300 call wall).
- **Debit/credit:** ≈ **$3.50 debit** (illustrative at ~113% IV, 9 DTE).
- **Breakeven:** ≈ **$293.50**.
- **Max loss:** the $3.50 debit (= the entire position risk; size so debit ≤ ~0.3% of book risk).
- **Why this structure:** at IV rank 91 / IV30d 113% `[HIST:iv_percentile]` long premium is too expensive
  — the spread caps the vega bleed and the vanna risk. The $290/$300 width sits inside ~1× the ±4.86%
  expected move `[CTX:implied_move]` and targets the $297.93 high / $300 call wall; flat by/at Jun-22.

### Defined-risk alternative — range/IV harvest (positive-gamma regime)

- **Structure:** iron condor (sells the rich IV into the long-gamma mean-reversion regime).
- **Strike(s) / expiry:** **−$265 put / +$255 put** and **−$300 call / +$310 call, expiry 2026-06-26.**
- **Debit/credit:** ≈ **$3.30 credit** (illustrative).
- **Breakeven:** ≈ **$261.70** and **$303.30**.
- **Max loss:** **$10 − $3.30 = $6.70** per condor (size so max-loss ≤ ~0.3% of book risk).
- **Why:** dealer regime is POSITIVE gamma (mean-reversion) `[STRUCT:gex]`, max-pain sits at $267.5 with
  no near-spot pin, and IV is rich `[HIST:iv_percentile]`; the condor brackets the ±4.86% expected move
  ($267–295) and is *helped* by the negative-vanna vol-crush. **Tail risk: a Jun-22 inclusion gap through
  $300 tests the call wing — defined-risk, but watch it.** (For the post-Jun-22 *fade*, the cleaner
  follow-on is a +$280/−$260 put debit spread, 07-17, targeting the $267.5/$260 magnets — not initiated now.)

## Macro overlay (cite phase-6)

- **Tailwinds:** Nasdaq-100 forced inclusion Jun-22 (valuation-agnostic mechanical bid) `[MACRO:NDX_inclusion_2026-06-22]`; Technology 5-day net INFLOW, persistence 0.8 `[MACRO:sector_flow_persistence]`; secular AI-capex story ($22.5bn 2026 capex, $2.6bn stake) `[MACRO:catalyst]`.
- **Headwinds:** hawkish June-17 FOMC, hike-biased 3.8% dots `[MACRO:FOMC_2026-06-17]`; CPI +4.17% YoY / Core PCE +3.29% `[MACRO:CPIAUCSL_2026-05]`; rising yields (10y 4.43%, 2y 4.05%) `[MACRO:DGS10_2026-06-16]`; TRANSITIONAL regime, 38.1% bullish breadth, "half-size" guidance `[MACRO:MarketRegime_2026-06-17]`.
- **Net:** **HEADWIND** — temporarily overridden by the idiosyncratic Jun-22 inclusion bid; the headwind re-asserts post-event.

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|------|-------|------------------|
| 2026-06-18 | June OPEX / 26.7%-of-OI expiry; positive-gamma pin + vanna unwind | ? |
| 2026-06-22 | **Nasdaq-100 inclusion effective** (forced index buying; sell-the-news risk after) | + (then −) |
| ~2026-07-15 | June CPI release | − if hot |
| 2026-08-06 | NBIS next earnings (beyond horizon) | ? |

## Post-trade monitoring checklist

- [ ] Re-run `uw options-structure dex/gex/vanna-charm` daily — flag any DEX→negative or GEX regime flip (the dip-bid turning to a vanna sell).
- [ ] Re-check `uw dark-pool block-stratified` mega-tier buy_ratio daily — a flip toward accumulation (>0.55) would be the first real bull confirmation; continued <0.10 sell confirms distribution.
- [ ] Watch the $297.93 / $300 call wall and the $267.5 max-pain magnet — define the box; exit the long on a close < $267.5.
- [ ] **Be flat the directional long by/at the June-22 open** — the inclusion is the last forced bid; pivot to the fade plan (put debit spread) only on a post-event rejection at $297.93–$300.
- [ ] Re-pull `fz quote` insider/short data and Finnhub MSPR after Jun-22 — escalating insider selling or SI build into the inclusion sharpens the fade.

## Citations summary

1. `[FLOW:sweep_persistence]` — NBIS top sweeps **5/5 sessions, consistency 1, $722.4M** — phase-1-flow.md §Sweeps.
2. `[DP:block_stratified]` — mega-tier dark pool **buy_ratio 0.064 (93.6% sell), $158.5M** — phase-2-dark-pool.md §Tier breakdown.
3. `[HIST:signal_backtest]` — bullish_flow **win_rate 37.5%, n=8, avg move −0.58%** — phase-5-historical.md §Signal backtest.
4. `[FUND:MSPR]` — insider **MSPR −100/−100/−34/−100, ~1.04M-share May sale** — phase-7b-fundamentals.md §Insider signal.
5. `[MACRO:NDX_inclusion_2026-06-22]` — Nasdaq-100 forced inclusion June 22 — phase-6-macro.md §Catalyst calendar.
6. `[STRUCT:dex]` / `[STRUCT:vanna]` — DEX +$2.88bn dip-bid; net vanna −1,795 vol-crush fuse — phase-4-structure.md.
