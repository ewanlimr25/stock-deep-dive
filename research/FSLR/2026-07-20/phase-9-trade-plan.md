# Phase 9 — Trade Blueprint

**Ticker:** FSLR
**As-of date:** 2026-07-20
**PM voice:** desk PM running an institutional options-overlay book
**Spot reference:** ~$206 (phase-4 structure feed $206.61; intraday tape $210.56 [phase-1]; OI feed prior-close $205.23 [phase-3])
**Upstream phases cited:** phase-0.5 through phase-8b

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

FSLR is in a mechanically bearish tactical setup — a **5-session persistent bearish
sweep campaign (consistency 1.0, $16.3M) [FLOW:sweep_persistence]** riding a
**FULLY_NEGATIVE short-gamma book with DEX −$226M [STRUCT:gex][STRUCT:dex]** into
the tail of a **−26.4% downtrend now pinned at its period low $203.77
[HIST:trend][INSIGHT:price_vs_flow]** — but it is a *low-conviction, two-sided
earnings coin-flip*, not a conviction short. The bearish edge is real (Tech is the
#1 outflow sector, persistence 0.8 [MACRO:sector_rotation]; the desk was 0-LONG
[AGENT:phase-8]) yet it fights a cheap, fast-growing, unlevered compounder
(**fwd P/E 12.3, +27% revenue growth [FUND:valuation]**) with a solar-policy
tailwind and a live post-earnings **vanna-squeeze bid if $200 holds
[STRUCT:vanna_charm]** — so the debate came back **disconfirmed (bull 0.65 / bear
0.65) [DEBATE]**. Trade it small and defined-risk only.

## Bias + conviction + horizon

- **Directional bias:** SHORT (mild; the plurality of phases 1–8 leans bearish, 0 LONG)
- **Conviction (M-01 bin):** **0.55** (slight edge — coin-flip plus a sliver)
- **Time horizon:** 1-4w (event-anchored to the 2026-07-30 earnings)
- **Why this bin:** MIXED composite (FSLR absent both confluence top-40, conf 7.5%
  [INSIGHT:signal_confluence]), avg agent conviction 2.4 [AGENT:phase-8], and a
  debate that came back **disconfirmed** [DEBATE] → the confluence band is low; the
  debate down-shift lands it at 0.55 (see Sizing).

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| Primary | ~$205 | Daily close **below $205.31** (loses the DP shelf; $200 is the short-gamma acceleration strike) | [DP:price_levels] / [STRUCT:gex] |
| Aggressive | ~$210–212 | **Rejection at the $211.99 DP pivot** — fade strength into the pre-earnings bounce | [DP:price_levels] |
| Fade (plan B) | ~$220 | Daily close **above $220** = vanna squeeze confirmed → **flip long**, target $230 | [STRUCT:vanna_charm] |

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| Support | **$205.31** (DP shelf, 25 trades + $5.0M post-mkt) → **$200** (put wall + gamma trigger) | [DP:price_levels] / [OI:oi_by_strike] |
| Resistance | **$211.99** (DP pivot) → **$220** (vanna cap) → **$240** (near-term call wall) | [DP:price_levels] / [OI:oi_by_strike] |
| Gamma flip | **ZGL = null** — pure short gamma; **$200** is the acceleration strike (2nd-heaviest neg-GEX) | [STRUCT:gex] |
| Largest pin | **$220** max-pain (07-24/07-31) — **weak** (thin OI, short-gamma overrides) | [STRUCT:max_pain] |

## Invalidation

- **Price-based:** Daily close **>$212** (pivot reclaim) = **partial** invalidation →
  cut the directional leg in half. Daily close **>$220** = **full** invalidation
  (vanna squeeze confirmed) → exit shorts, consider the fade (long) plan.
- **Signal-based:** (a) the **bearish sweep persistence breaks** — consistency
  drops <0.6 or the tape flips to ask-side call *buying* [FLOW:sweep_persistence];
  (b) **GEX flips POSITIVE** (long gamma returns, ZGL prints below spot) [STRUCT:gex];
  (c) the **$205 DP buy-shelf vanishes / turns to distribution** [DP:block_stratified].
- **Macro-based:** a **strong 07-30 earnings/guidance beat** or a favorable
  **solar-policy catalyst** (FEOC/45X ruling, tariff escalation) [MACRO:SolarPolicy];
  or **broad risk-on** (breadth >50% bullish, SPY reclaims its 50-SMA)
  [MACRO:MarketRegime].

## Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** p_raw = **0.90** (bearish_flow backtest, n=**10**,
  source=backtest) → N-cap (10 ≤ n < 20 → 0.85) → **capped p = 0.85**
  `[HIST:signal_backtest]`. *Caveat: this is a **market-wide base rate**, not
  FSLR-specific, on a small N — the gates below, not p, govern the final size.*
- **Kelly inputs:** b = **2.14** (short $205 → target $190, stop $212 = 15/7),
  fraction = 0.25, cap_pct = 5.
- **Raw Kelly:** (0.85·2.14 − 0.15)/2.14 = **0.78** → ×0.25×100 = 19.5% → capped
  **5.0%**. **Win-rate map ceiling:** p 0.85 ≥ 0.70 → **full (≤5%)**. **Pre-gate = 5.0%.**
- **Risk gates (each cuts; none add):**
  - **Fundamentals (phase-7b): CAUTION** → cut one step (full → **half → 2.5%**).
    Cheap/strong quality contradicts the short on the growth/margins axis.
  - **Sentiment/crowd (phase-7c): CAUTION** (crowd_state BALANCED) → cut one step
    (half → **starter → ~1.25%**). Bullish Street/news vs the bearish thesis.
  - **Correlation cluster (phase-6/8): none** — FSLR is the only 07-20 blueprint → no-op.
  - **Sector rotation (phase-6): aligned** (Tech outflow is *with* the short) → no-op.
  - **Debate (phase-8b): bull 0.65 vs bear 0.65 → DISCONFIRMED** → down-shift the
    bin (0.65 → **0.55**) **and** cut one step (starter → **below-starter ~0.6%**).
- **Context modifier (phase-0.5):** `BUSY_NAME_NORMAL_DAY` → do **not** size top of
  band (already at the floor).
- **Final size:** **~0.6% of book risk** (three gate-cuts from the 5% Kelly ceiling
  → minimal, defined-risk-only). **Deviation reason:** none (upward deviation
  forbidden — three gates fired + BUSY_NAME context).

## Option structures

### Directional (primary)

- **Structure:** Put **debit** spread (bearish, defined-risk)
- **Strike(s) / expiry:** Buy **$205P / sell $190P, Aug-21 2026** (post-earnings OI
  cliff, 15.1% of OI [OI:term_structure]; $190 = the neg-gamma trough [STRUCT:gex])
- **Debit/credit:** ~**$5.50 debit** (est., IV rank 99)
- **Breakeven:** ~**$199.50**
- **Max loss:** **$5.50** (the debit) — sized so debit ≤ ~0.6% book risk
- **Why this structure:** IV rank is **98.5th-pctile / VRP +0.19 (PREMIUM_SELLING)
  [HIST:iv_percentile_zscore][HIST:vrp]**, so a naked long put overpays for vega and
  gets crushed post-earnings; the short $190 leg offsets most of that vega and caps
  cost. It targets the $200-break→$190 short-gamma path over a 1–4w horizon that
  spans the 07-30 print. A single-catalyst ±$10.9 gap (±5.31% [CTX:implied_move])
  cannot exceed the max loss (the debit is the whole risk) → earnings-safe.

### Defined-risk alternative

- **Structure:** Call **credit** spread (bearish-to-neutral; sells the rich upside vol)
- **Strike(s) / expiry:** Sell **$220C / buy $230C, Aug-21 2026** ($220 = vanna cap /
  below the $240 call wall [STRUCT:vanna_charm][OI:oi_by_strike]; above the
  expected-move top ~$217)
- **Debit/credit:** ~**$3.00 credit**
- **Breakeven:** ~**$223**
- **Max loss:** **$7.00** (width $10 − credit $3.00), NOT margin
- **Why:** monetizes the IV crush + overhead call wall + vanna cap; profits if FSLR
  simply stays < $220 (spot $206, downtrend) — the "sell rich vol in range"
  expression the regime prescribes ("iron condors in range" [MACRO:MarketRegime]).
  *(Neutral variant: combine both legs into a bearish-skewed iron condor if you want
  the IV-crush theta without a directional tilt.)*

## Macro overlay (cite phase-6)

- **Tailwinds (for the short):**
  - [MACRO:sector_rotation] Technology is the **#1 outflow sector, −$133.9M,
    persistence 0.8** — durable rotation out.
  - [MACRO:MarketRegime] **TRANSITIONAL/CHOPPY, 34% bullish breadth, "half position
    sizes"** — risk-off tape.
- **Headwinds (against the short):**
  - [MACRO:SolarPolicy] **>100% China tariff wall + OBBBA FEOC/CdTe 45X advantage** —
    structural tailwind that could turn 07-30 into a guidance beat.
  - [MACRO:DGS10] Rates **stable** (fed funds 3.63% on hold, 10y 4.55%) — no fresh
    tightening to press solar lower.
- **Net:** **mixed, tilting mildly bearish tactically.**

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|------|-------|------------------|
| **2026-07-30 (AMC)** | **FSLR Q2 earnings** (cons EPS $2.85, −10% YoY; guide 3.4–4.0 GW, EBITDA $400–500M) | **? (dominant binary; ±5.31% implied)** |
| ~2026-08-13 | CPI (Jul) release | ? (index-level, inside ±5%) |
| ongoing | Solar-policy headlines (FEOC/45X, tariff reviews) | ? (idiosyncratic) |

## Post-trade monitoring checklist

- [ ] **Daily: bearish sweep persistence** — does the campaign extend (consistency
  holds ≥0.8) or break? A flip to ask-side call buying kills the thesis
  [FLOW:sweep_persistence].
- [ ] **Daily: GEX regime** — a flip to POSITIVE (ZGL prints) removes the
  short-gamma amplification and the vanna asymmetry [STRUCT:gex].
- [ ] **Daily: the $205.31 DP shelf** — does institutional buying persist (short
  failing) or vanish/turn to distribution (short confirming) [DP:block_stratified]?
- [ ] **Into 07-30: IV rank + skew** — if skew steepens (puts get bid) the
  complacency window closed; if it stays complacent, downside stays cheap
  [STRUCT:term_skew].
- [ ] **On 07-30 earnings:** measure the gap vs ±5.31% implied; **if $200 holds,
  expect the vanna bid → exit the put spread**, watch for the $220 fade-long trigger.

## Citations summary

1. [FLOW:sweep_persistence] 5-session persistent **bearish** sweep campaign,
   consistency **1.0**, $16.3M — phase-1-flow.md §Key signals.
2. [STRUCT:gex]/[STRUCT:dex] **FULLY_NEGATIVE** short gamma (GEX −2.04M, ZGL null) +
   **DEX −$226M** dealers-sell-underlying — phase-4-structure.md §GEX/§DEX.
3. [HIST:trend] **−26.4%** 30-session downtrend + [HIST:signal_backtest]
   bearish_flow win-rate **0.90 (n=10)** — phase-5-historical.md §Verdict.
4. [DEBATE] **disconfirmed**, bull_residual 0.65 / bear_residual 0.65 —
   phase-8b-debate.md §Disconfirmation verdict.
5. [FUND:valuation] fwd P/E **12.3**, +27% revenue growth (short-thesis risk) —
   phase-7b-fundamentals.md §Valuation.
