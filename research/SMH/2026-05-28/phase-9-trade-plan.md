# Phase 9 — Trade Blueprint

**Ticker:** SMH
**As-of date:** 2026-05-28
**PM voice:** desk PM running an institutional options-overlay book
**Spot reference:** $599.83 (phase-2 close / phase-7 `uw_screener`)
**Upstream phases cited:** phase-0.5 through phase-8b

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

SMH is pinned at the top of a parabolic move ($599.83, 96.7% of its 52-wk range,
+66.6% YTD `[HIST:52w_proximity fz]`) where dealers are **long gamma $595–650 (DEX
+$3.95bn, buy-the-dip)** `[STRUCT:dex]` and **rich IV is begging to be sold** (IV rank
84.6, VRP +0.089 PREMIUM_SELLING) `[HIST:vrp]`, while smart money quietly **rolls and
ladders protective puts into the strength** (net put OI +86,442 vs call +10,858;
530P 05-29→06-05 roll) `[OI:biggest_increases DUCKDB]` — a hedged melt-up, not a
breakout or a breakdown. The desk plurality is **RANGE/neutral with zero shorts**
(phase-8: NEUTRAL ×2, RANGE ×1, LONG ×1) `[AGENT:risk-monitor]` because the regime is
TRANSITIONAL ("iron condors in range") and shorting semis has lost all rally
(bearish_flow 55.6% vs bullish_flow 100%) `[HIST:signal_backtest]`. **Trade it as a
defined-risk premium sale inside the $585–615 dealer range, half-of-half size,
respecting $585 as the line where the short-gamma trapdoor goes live.**

## Bias + conviction + horizon

- **Directional bias:** **RANGE** (range-lean, mildly bearish skew — fade the
  extension, do not short it).
- **Conviction (M-01 bin):** **0.65**
- **Time horizon:** **1-4w** (through June OPEX 06-19)
- **Why this bin** (phase-10 confluence): structurally well-supported range
  (phase-4 pin + phase-6 "iron condors in range") but materially fought by a MIXED
  conviction matrix, a price/flow divergence, extreme extension, and a CAUTION
  sentiment gate → confluence lands ~58–62, the 0.65 ("moderate edge with real
  disconfirming evidence") band.

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| Primary | $598–602 | Sell the condor while spot pins the $600 long-gamma strike (IV rich, pre-NFP) | `[STRUCT:gex]` |
| Aggressive | $605–612 | Leg into the call wing on a push toward the 52-wk-high/long-gamma cap (rallies sold by dealers) | `[STRUCT:gex]` |
| Fade | $586–590 | If spot probes the gamma flip: tighten/close the put wing — do NOT add the credit there | `[STRUCT:gex]` |

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| Support (major) | **$567.88** | `[DP:price_levels]` 5-day institutional shelf ($198.7M) |
| Support (secondary) | $576–577 | `[DP:price_levels]` |
| **Gamma flip** | **$585** | `[STRUCT:gex]` long→short gamma boundary (the thesis line) |
| Short-gamma well | $550 | `[STRUCT:gex]` −$16M accelerant (trapdoor target) |
| Long-gamma pin | $600 | `[STRUCT:gex]` +$7.4M (no OPEX pin this week — `[OI:pin_risk]` empty) |
| Resistance / cap | $612.30 / $620 | `[HIST:52w_proximity fz]` 52-wk high · `[STRUCT:gex]` long-gamma cap |

**Price-context color (advisory):** entering at RSI 71.4 and −2.0% from the 52-wk
high `[HIST:rsi fz]` — chase risk is high; this is why the plan **sells premium /
fades the extension** rather than chasing a breakout long.

## Invalidation

- **Price-based:** **Two daily closes below $585** (the phase-4 gamma flip /
  `[STRUCT:gex]`) → the short-gamma trapdoor is live; close the put wing, the range
  thesis is broken. (Symmetric upside: two daily closes above **$620** on volume →
  the cap broke, close the call wing.)
- **Signal-based:** **DEX flips negative** (dealers stop buying dips) on the phase-4
  daily refresh, OR the phase-7 conviction-matrix flips MIXED→DIRECTIONAL_SHORT
  `[INSIGHT:conviction_matrix]` — the pin is failing.
- **Macro-based:** **June-5 NFP downside surprise** (or hawkish FOMC 06-16/17) that
  gaps SMH through $585 `[MACRO:calendar_2026-06 WebSearch:bls.gov]`; OR UW market
  regime flips TRANSITIONAL→RISK-OFF `[MACRO:MarketRegime_2026-05-28 UW]`.

## Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** p_raw = **0.556** (n=**9**, source=**backtest**, bearish_flow)
  → N-cap (n<10 → 0.75) → capped **p = 0.556** `[HIST:signal_backtest]`.
- **Kelly inputs:** b = **2.56** (directional reference: entry $599.83, target
  $567.88 `[DP:price_levels]`, stop $612.30 — `|599.83−567.88|/|612.30−599.83|`),
  fraction = 0.25, cap_pct = 5.
- **Raw Kelly:** (0.556×2.56 − 0.444)/2.56 = **0.382** → ×0.25×100 = 9.55% → capped at
  cap_pct **5%**. **Win-rate map ceiling:** p 0.556 ∈ [0.50,0.70] → **HALF (≤2.5%)**.
  Take the smaller → **2.5%**.
- **Risk gates:**
  - Fundamentals (7b): **NA** (ETF) → no-op.
  - **Sentiment/crowd (7c): CAUTION** (euphoric media + persistent bullish sector
    inflow are adverse to the bearish-skewed lean) → **cut one step: half → starter**.
  - Correlation cluster (6/8): **none** — SMH is the only 2026-05-28 blueprint → no-op.
  - Sector rotation (6): **neutral for a range thesis** (Tech persistence 1.0 is
    adverse only to a directional short, which this isn't) → no-op.
  - Debate (8b): bull_residual **0.65** vs bear_residual **0.60** → **not
    disconfirmed** → no-op (but thin margin — keep defined-risk).
  - **Context (0.5): BUSY_NAME_NORMAL_DAY** → do NOT size at top of band (reinforces
    the starter level).
- **Final size:** **1.25%** of book risk (starter). Each structure's max-loss is
  sized to fit ≤1.25%.
- **Deviation reason:** none (no upward deviation — forbidden here anyway, a gate fired).

## Option structures

> **The two structures express the central tension.** The condor (PREFERRED) bets the
> pin holds; the put debit spread bets the trapdoor fires. **Default to the condor;
> switch to the put debit spread only if $585 starts breaking.** Both are defined-risk
> and sized so a single NFP/FOMC gap stays within max loss (N4). Front-expiry implied
> move **±1.71% / ~$10.2** `[CTX:implied_move_pct]`; the 8-DTE 84% IV implies a larger
> move, which is exactly why a defined-risk (capped) wrapper is mandatory through 06-05.

### Directional (the minority lean — bearish fade, press only on a $585 break)

- **Structure:** put debit spread (bearish)
- **Strike(s) / expiry:** **Long 590P / Short 565P, 2026-06-19** (strikes at the
  gamma flip zone → DP shelf `[STRUCT:gex]`/`[DP:price_levels]`)
- **Debit/credit:** ~$4.50 debit
- **Breakeven:** ~$585.50
- **Max loss:** $4.50 (the debit) — defined
- **Why this structure:** Aligns with the bearish_flow signal, the price/flow
  divergence `[INSIGHT:price_vs_flow]`, and the smart-money hedge; convex if the
  June-5 NFP flushes the short-gamma trapdoor toward $567. **Caveat:** it BUYS rich IV
  (fights the VRP `[HIST:vrp]`) so it is the lower-EV leg — starter size, tail bet only.

### Defined-risk alternative (PREFERRED — the recommended trade)

- **Structure:** iron condor (range / premium sale)
- **Strike(s) / expiry:** **Sell 585P / Buy 567P  +  Sell 615C / Buy 627C, 2026-06-19**
  (put wing at the gamma flip → DP shelf; call wing above the 52-wk high / long-gamma
  cap `[STRUCT:gex]`/`[DP:price_levels]`/`[HIST:52w_proximity fz]`)
- **Debit/credit:** ~$5.00 credit
- **Breakeven:** ~$580.50 (down) / ~$620.00 (up)
- **Max loss:** ~$13.00 (wider put wing 18 − credit 5) — defined
- **Why this structure:** Sells the over-bid IV (rank 84.6, VRP +0.089) on **both**
  sides of the $585–615 dealer-pinned range; profits in 3 of the debate's 4 paths
  (grind-up, pin, contained dip). **The put wing (585/567) is the higher-confidence
  side** (sells the hedge premium institutions are over-paying for, above the $567.88
  shelf); the call wing fades the long-gamma cap. This is the regime's own
  prescription `[MACRO:MarketRegime_2026-05-28 UW]` ("iron condors in range").

## Macro overlay (cite phase-6)

- **Tailwinds:** Technology #1 sector inflow, persistence 1.0 `[MACRO:sector_flow_persistence_2026-05-28 UW]`;
  benign rates + calm VIX 16.3, 2s10s +0.46 normal `[MACRO:VIXCLS_2026-05-27 FRED]`;
  core semis growth-supported (PEG 0.93) `[FUND:peer_pe fz]`.
- **Headwinds:** regime TRANSITIONAL, breadth 40.6% `[MACRO:MarketRegime_2026-05-28 UW]`;
  SOX +65% YTD with BTIG 25–30% "1999" correction warning `[MACRO:semis_top_call_2026-05 WebSearch]`;
  sticky inflation (CPI 3.95%, Core PCE 3.29%) `[MACRO:CPIAUCSL_2026-04 FRED]`.
- **Net:** **mixed** — risk-on backdrop supports the pin; euphoria + binary catalysts
  threaten the trapdoor. A premium-selling range trade is the correct expression of
  "mixed."

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|------|-------|------------------|
| 2026-06-05 | May NFP jobs report (the 84%-IV front-end event; 06-05 weekly expiry) | ? |
| ~2026-06-11 | May CPI (approx) | ? |
| ~2026-06-16/17 | FOMC (rate decision + SEP/dot plot) | ? |
| 2026-06-19 | June monthly OPEX (structure expiry) | ? |

## Post-trade monitoring checklist

- [ ] **Daily: is $585 holding?** Two closes below = invalidation; close the put wing
      and (if pressing the tail) flip to the put debit spread `[STRUCT:gex]`.
- [ ] **Phase-4 daily refresh:** DEX still positive (dealers buying dips) and GEX flip
      still ~$585? A DEX flip negative is a signal-invalidation `[STRUCT:dex]`.
- [ ] **Dark pool:** does the $567.88 shelf hold on any dip, or does it break (→ $550)?
      Re-check `uw dark-pool price-levels` daily `[DP:price_levels]`.
- [ ] **June-5 NFP:** be defined-risk into it; do not be naked short premium.
- [ ] **Sector rotation:** Tech persistence staying >0.8 post-NFP? A drop confirms
      rotation adverse to extended SMH `[MACRO:sector_flow_persistence_2026-05-28 UW]`.
- [ ] **IV/VRP:** if IV rank collapses <50 (VRP gone), the premium-selling edge is
      spent — take profit `[HIST:vrp]`.

## Citations summary

1. `[STRUCT:dex]` — DEX +$3.95bn, dealers net short calls → buy dips — phase-4-structure.md §DEX.
2. `[HIST:vrp]` — VRP +0.089, PREMIUM_SELLING (IV 46.2% > RV 37.3%) — phase-5-historical.md §IV regime.
3. `[HIST:signal_backtest]` — bearish_flow win-rate 0.556 (n=9) vs bullish_flow 100% (n=6) — phase-5-historical.md §Signal backtest.
4. `[OI:biggest_increases DUCKDB]` — net put OI +86,442 vs call +10,858 (~8:1); 530P 05-29→06-05 roll — phase-3-positioning.md.
5. `[STRUCT:gex]` — long-gamma cushion $595–650, short-gamma well $550 (−$16M), flip ~$585 — phase-4-structure.md §GEX.
6. `[MACRO:MarketRegime_2026-05-28 UW]` — regime TRANSITIONAL, "iron condors in range," breadth 40.6% — phase-6-macro.md.
