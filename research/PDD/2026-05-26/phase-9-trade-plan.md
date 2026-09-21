# Phase 9 — Trade Blueprint

**Ticker:** PDD
**As-of date:** 2026-05-26
**PM voice:** desk PM running an institutional options-overlay book
**Spot reference:** $96.58 (phase-5 `historical_trend` close 2026-05-26)
**Upstream phases cited:** phase-0.5 through phase-8b

> *For research and educational use only. Not financial advice. Sizing and structures are illustrative.*

## Thesis (≤3 sentences)

PDD enters tomorrow's (5/27) Q1 print as a **coin-flip on direction with rich, crush-prone vol**:
the 5/29 weekly is bid to **98.3% IV vs a ~42% back-month** [STRUCT:iv_term_structure] on a positive
VRP of **+0.072** [HIST:vrp], while genuine dark-pool block buying (**100% buy, $17.09M**
[DP:block_stratified]) is offset by a fundamental VETO (**EPS −13.2% TTM, China April retail +0.2%**
[FUND:epsGrowthTTMYoy, MACRO:ChinaRetail_2026-04]) and an 8b debate that **disconfirmed both
directions (0.55/0.55)** [DEBATE:bull_residual]. The only edge that survived every gate is
**selling the overpriced event move with defined risk, put-skewed** for the −$8.63M short-gamma
accelerant at strike 95 [STRUCT:gex]. **Directional exposure is watch-only** — the 7b VETO, 7c
crowded-long, and the coin-flip debate leave no directional edge to size.

## Bias + conviction + horizon

- **Directional bias:** **NEUTRAL** (plurality of phases 1–8 is NEUTRAL/RANGE with a downside skew;
  no agent is outright long, contrarian-scanner alone is SHORT-3). The edge is non-directional (vol).
- **Conviction (M-01 bin):** **0.55** (floor — slight edge, and it is a *vol* edge, not directional).
- **Time horizon:** **1-5d** (the print is the event; the vol-harvest closes the day after 5/27).
- **Why this bin:** every gate cut and the debate disconfirmed (0.55/0.55) — this sits at the bottom
  confluence band; phase-10 to confirm. No directional conviction exists to justify a higher bin.

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| Primary | ~$96.58 (pre-5/27 open) | Sell the 98.3% front-week IV into the print (vol-harvest entry) | [STRUCT:iv_term_structure] |
| Aggressive | tag $97.79 | Leg the call side in on a push to the DP pivot (sell strength) | [DP:price_levels] |
| Fade (plan B) | break <$95 post-print | Flip to the directional bear put spread IF Q1 misses + <95 breaks | [STRUCT:gex] |

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| Support | **$94.52** (then $92.00 / 52w-low $92.57) | [DP:price_levels] |
| Resistance | **$104** (positive-gamma cap, peak 110) | [STRUCT:gex] |
| Gamma flip | **none — ZGL null (FULLY_NEGATIVE)**; ~$98–99 local positive-γ pivot | [STRUCT:gex] |
| Largest pin | **none — PDD absent from pin-risk list** (free to move full implied) | [OI:pin_risk] |
| Downside accelerant | **$95** (net_gex −$8.63M — short-gamma cascade trigger) | [STRUCT:gex] |

## Invalidation

- **Price-based:** for the vol-harvest, a 5/27 gap **beyond the IC short strikes (90 / 104)** = defined
  max loss (accepted, capped). For the *directional* plan-B short, two daily closes **above $102**
  (down-drift origin / reclaim of the range) invalidates the down-skew. [DP/STRUCT]
- **Signal-based:** dark-pool **accumulation flips to distribution** (`insights_institutional_accumulation`
  buy/sell < 1.0) [INSIGHT:institutional_accumulation], **OR** GEX flips positive on an up-gap and the
  vanna bid engages >104 (the squeeze fires) [STRUCT:vanna_charm].
- **Macro-based:** a clean **Temu/margin beat or China-stimulus surprise** in the 5/27 print, or the
  6/16 FOMC delivering a dovish surprise that bids EM/China risk [MACRO:FOMC_2026-04-29] — either
  validates the bull (DP-accumulation) case and kills the down-skew.

## Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** p_raw = **null** (phase-5 `dark_pool_accumulation` backtest returned
  **total_signals 0**, win_rate_source **null** [HIST:signal_backtest]) → **fall back to the conviction
  bin 0.55**, capped at the 0.65 fallback ceiling → **p = 0.55**.
- **Kelly inputs:** b = **0.79** (iron-condor payoff: ~$2.20 credit / ~$2.80 max-loss on $5 wings),
  fraction = 0.25, cap_pct = 5.
- **Raw Kelly:** (0.55 × 0.79 − 0.45) / 0.79 = **−0.02 (≈ 0 / marginally negative)** · **Win-rate map
  ceiling:** p∈[0.50,0.70] → **half (≤2.5%)** — but raw Kelly ≈ 0 already caps the math at starter.
- **Risk gates (each can only cut):**
  - Fundamentals (phase-7b): **VETO** → **directional size = watch-only / 0%**; defined-risk carry only.
  - Sentiment/crowd (phase-7c): **CAUTION** (CROWDED_LONG, no squeeze fuel) → cut one step.
  - Correlation cluster (phase-6/8): **none fired** — no concurrent same-date blueprint; China-internet
    cluster (KWEB 0.81) is a **soft-watch** only.
  - Sector rotation (phase-6): **NEUTRAL (lean adverse)** — semis/tech lead → cut half step.
  - Debate (phase-8b): bull_residual **0.55** vs bear_residual **0.55** → **disconfirmed = true** →
    down-shift bin one (already at 0.55 floor) + cut one step.
  - **Context (phase-0.5): BUSY_NAME_NORMAL_DAY** → do not size at top of band.
- **Final size:** **0% — WATCH-ONLY.** Raw Kelly is **negative (−0.02)** → the Kelly ceiling is **0**,
  and upward deviation is **forbidden** because gates fired (7b VETO, 7c CAUTION, 8b disconfirm). The
  model's sized recommendation is therefore **no position**: there is no edge that clears the gates.
  The iron condor below is the structure to use **only if** a desk insists on expressing the vol-harvest
  view, at strict token risk it accepts is un-edged by this framework — it is **not** a model-sized rec.
- **Deviation reason:** none (upward deviation is not permitted — multiple gates fired).

## Option structures

### Directional (primary slot — but WATCH-ONLY / 0% per 7b VETO + 8b disconfirm)

- **Structure:** bear put debit spread (down-skew expression on the post-event tenor)
- **Strike(s) / expiry:** buy **95P / sell 88P, 2026-06-18** (95 = the −$8.63M gamma accelerant + the
  19,729-OI 6/18 95P wall [STRUCT:gex, OI:biggest_increases]; 88 below the 90-put cluster / 52w-low buffer)
- **Debit/credit:** ~$2.50 debit
- **Breakeven:** ~$92.50
- **Max loss:** $2.50 (width $7)
- **Why this structure:** 6/18 IV (49%) is far less crushed than the 5/29 weekly (98%), so it expresses
  the down-skew without buying the event-vol bleed. **DO NOT put on pre-print** — it is directional and
  VETO'd; arm it only if Q1 misses AND spot breaks/holds <95 (the cascade confirms). Watch-only, 0% size.

### Defined-risk alternative (the structure IF expressing the vol view — un-sized / watch-only per gates)

- **Structure:** put-skewed iron condor on the 5/29 weekly (harvest the 98% IV crush)
- **Strike(s) / expiry:** sell **90P / buy 85P** + sell **104C / buy 109C, 2026-05-29** (call short 104
  at the gamma cap [STRUCT:gex]; put short 90 just outside the implied low ~$91.08, wider protective
  wing on the dangerous side; 104/110 anchored to the written-call wall [OI:biggest_increases])
- **Debit/credit:** ~**$2.20 net credit**
- **Breakeven:** **$87.80 (lower) / $106.20 (upper)**
- **Max loss:** **$2.80** (width $5 − $2.20 credit)
- **Note:** profits from the IV collapse 98%→realized; **close the day after the 5/27 print** (don't hold
  to expiry). Tail = a FUTU/TIGR-style **>13% gap** blows through a wing for the defined $2.80 max loss —
  which is exactly why size is starter (0.5%). Shorts sit at ~1.2–1.35× the ±5.69% implied move (N4).

## Macro overlay (cite phase-6)

- **Tailwinds:** soft broad USD ~119 [MACRO:DTWEXBGS] (mild EM support); US-China **tariff truce
  extended to 2026-11-10** [MACRO:USChinaTariff_2025-11] (removes a near-term tail).
- **Headwinds:** **China April retail +0.2% YoY** — weakest since Dec 2022 [MACRO:ChinaRetail_2026-04];
  **Temu de-minimis removed / 25–57% tariffs + EU DSA** [MACRO:TemuTariffs_2026]; **regime TRANSITIONAL**
  (half size, defined-risk) [MACRO:MarketRegime_2026-05-26].
- **Net:** **headwind** (the China-consumption + Temu impairment dominate the second-order USD/truce tailwinds).

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|------|-------|------------------|
| **2026-05-27** | **PDD Q1 earnings** (EPS ~$2.44, rev ~$16.0B) — the event | ? |
| ~2026-06-16/17 | FOMC (likely hold 3.5–3.75%) | ? |
| ~2026-06-15 | China May activity / retail data | ? |
| 2026-06-18 | Monthly OPEX (PDD heaviest standing OI) | ? |

## Post-trade monitoring checklist

- [ ] **Close the 5/29 IC the day after the 5/27 print** once the IV crush is realized — do not hold for theta.
- [ ] Re-check `insights_institutional_accumulation` daily — a flip to **distribution (buy/sell <1.0)** kills the bull (DP) leg of the thesis.
- [ ] Watch **$95** intraday post-print — a break/hold below arms the plan-B bear put spread (short-gamma cascade) [STRUCT:gex].
- [ ] Watch **$104** — a reclaim + hold engages the vanna bid / squeeze (the bull tail); covers/threatens the call wing [STRUCT:vanna_charm].
- [ ] Re-pull phase-4 GEX/DEX on the daily refresh — a flip to POSITIVE on an up-gap = regime change.
- [ ] Treat any other China-internet position (KWEB/BABA) as the SAME book — corr 0.81 [MACRO:portfolio_correlation].

## Citations summary

1. `[STRUCT:iv_term_structure]` — 5/29 front IV **98.3%** vs back ~42% (backwardation) — phase-4 §IV term structure
2. `[DP:block_stratified]` — block tier **100% buy, $17.09M**, sell_volume 0 — phase-2 §Tier breakdown
3. `[FUND:epsGrowthTTMYoy]` — EPS growth **−13.2% TTM** (the VETO) — phase-7b §Growth profile
4. `[HIST:vrp]` — VRP **+0.0716** PREMIUM_SELLING — phase-5 §IV regime
5. `[STRUCT:gex]` — FULLY_NEGATIVE **−$12.8M**, **−$8.63M at strike 95** — phase-4 §GEX
6. `[DEBATE:bull_residual]` — debate disconfirmed **0.55/0.55** — phase-8b §Disconfirmation verdict
