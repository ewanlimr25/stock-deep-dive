# Phase 4 — Dealer Structure & Gamma

**Ticker:** GOOG · **As-of:** 2026-07-23 · **Spot:** $318.59 (structure feed)
**Generated:** 2026-07-24T01:18:35Z · after-hours run (0DTE gamma-flip skipped)
**Upstream:** phase-1 (bearish premium, deep-ITM puts), phase-2 (overhead $341–351
supply, balanced DP), phase-3 (MIXED/hedge-heavy positioning, put walls 330/310/300,
call wall 350, put OI substantially *written*; open Q: "dealers long puts →
supportive gamma below spot?")

## Summary

Dealer structure is a **material counterweight to the bearish flow**: it leans
**mean-reverting / mildly supportive**, not bearish-continuation. Dealers are in a
**long-gamma (POSITIVE) regime** with the zero-gamma level at 187.5 — far below
spot 318.59 — so they dampen moves and fade extremes (vol suppression). **Max pain
sits ABOVE spot** (350 for all expiries through Aug-14, 365 for Aug-21), a
theoretical upward pull. Vanna is a **squeeze-up setup**: dealers short a put-heavy
book, and with IV rank only 38 a further IV decline mechanically forces dealer
*buying*. The bearish structural pieces are (a) the standing DEX hedge — dealers
net short puts, net_dex −$3.0B, so the static hedge is to *sell* underlying — and
(b) **backwardation** (near IV 41% > far 35%, ratio 1.16) flagging near-term stress
from the ~8–9% breakdown. But the 30-day skew is **COMPLACENT** (put/call IV 1.002)
— the option market is *not* pricing further downside tail. Net: this phase caps
the short thesis and tilts the synthesis toward range/mean-reversion off the
300–310 put-wall support toward the 350 max-pain/call-wall cap.

## Key signals

- **Long-gamma regime (POSITIVE)**, ZGL 187.5 ≪ spot 318.59 → dealers fade moves,
  suppress realized vol. `[STRUCT:gex]`
- **Max pain above spot:** 350 (07-24→08-14, +9.96%), 365 (08-21, +14.67%) —
  upward OI pull; overlaps phase-3 call wall 350 & phase-2 DP supply. `[STRUCT:max_pain]`
- **Vanna-squeeze-up setup:** net_vanna +10,504, dealers short put-heavy book;
  falling IV → dealers BUY underlying. IV rank 38 leaves room. `[STRUCT:vanna_charm]`
- **Backwardation:** near IV 0.412 (8DTE) vs far 0.354 (29DTE), ratio 1.16 →
  near-term stress (the breakdown), not an earnings event (earnings 2026-11-04).
  `[STRUCT:front_end_iv_ratio]` `[STRUCT:iv_term_structure]`
- **Complacent skew (1.002)** — no downside tail premium bid despite the drop;
  contrarian-neutral. `[STRUCT:term_skew]`

## Detailed findings

### GEX — `[STRUCT:gex]`
- regime **POSITIVE** — "Dealers net long gamma — expect mean-reversion and reduced
  volatility." zero_gamma_level **187.5** (deep below spot → firmly long-gamma).
- `total_gex` field returns −48,436,742, which conflicts in sign with the POSITIVE
  regime label; per skill guidance I quote the tool's **regime label** (POSITIVE)
  and flag the total_gex sign as a build quirk, not a re-derivation. Long-gamma is
  corroborated by ZGL ≪ spot.

### DEX — `[STRUCT:dex]`
- net_dex **−2.99B** (call_dex +0.52B, put_dex −3.51B). Interpretation: "Public net
  put-long → dealers net short puts → dealer hedge is to SELL underlying." A
  standing bearish *delta* pressure (a level of supply), distinct from trend.

### Vanna + charm — `[STRUCT:vanna_charm]`
- net_vanna **+10,504**, net_charm **−353,845**. "Public net vanna positive
  (put-heavy book). Falling IV → |put delta| drops → dealers (short puts) cover by
  BUYING underlying. Classic vanna-squeeze setup if VIX collapses." Supportive/
  upside-mechanical if IV eases.

### IV term structure / front-end — `[STRUCT:iv_term_structure]` `[STRUCT:front_end_iv_ratio]`
- structure **BACKWARDATION**; front-end ratio 1.162 (near 8DTE IV 0.412 vs far
  29DTE 0.354). Near-term realized-vol stress from the breakdown; will normalize if
  the tape stabilizes (no earnings catalyst in the window).

### Term skew — `[STRUCT:term_skew]`
- skew_ratio **1.002**, interpretation **COMPLACENT** — 25Δ put IV ≈ 25Δ call IV.
  Despite the put buying and the drop, no rich downside tail is priced. Either
  genuine complacency (gap risk) or the put-writing (phase-3) offsetting put demand.

### Max pain (per expiry, dte≤30) — `[STRUCT:max_pain]`
| Expiry | Max pain | Dist | P/C OI |
|---|---|---|---|
| 2026-07-24 | 350 | +9.96% | 0.686 |
| 2026-07-31 | 350 | +9.96% | 0.555 |
| 2026-08-07 | 350 | +9.96% | 0.915 |
| 2026-08-14 | 350 | +9.96% | 0.489 |
| 2026-08-21 | 365 | +14.67% | 1.037 |
Static-OI estimate (soft magnet, per tool caveat) — pin sits ~10–15% *above* spot.
Cross-checks phase-3: agrees with the 350 call wall and Aug-21 OI cliff.

### Today's gamma flip
Skipped — after-hours run (0DTE intraday tool not meaningful post-close).

## Tool calls
| Tool | Args | jq path |
|---|---|---|
| options-structure gex | --symbol GOOG --dte-max 45 | `.{regime,zero_gamma_level,total_gex,underlying_price}` |
| options-structure dex | --symbol GOOG --dte-max 45 | `.{net_dex,call_dex,put_dex,interpretation}` |
| options-structure vanna-charm | --symbol GOOG --dte-max 45 | `.{net_vanna,net_charm,vanna_interpretation}` |
| options-structure iv-term-structure | --symbol GOOG | `.structure` |
| options-structure term-skew | --symbol GOOG --dte-target 30 | `.{skew_ratio,interpretation}` |
| options-structure front-end-iv-ratio | --symbol GOOG --near-dte 7 --far-dte 30 | `.{ratio,near_iv,far_iv,regime}` |
| options-structure max-pain | --symbol GOOG --dte-max 30 | `.results[].{expiry,max_pain,distance_pct,put_call_oi_ratio}` |

## Tool errors
- `iv-term-structure` per-row `term_structure[]` returned null dte/iv in the jq
  cut, but the top-level `structure=BACKWARDATION` label parsed clean and is
  corroborated by `front-end-iv-ratio` (ratio 1.162, regime BACKWARDATION). Regime
  label used; per-strike rows not relied upon.

## Verdict for downstream

- **Dealer regime: LONG GAMMA (mean-reverting), mildly SUPPORTIVE.** Spot ≫ ZGL,
  max pain above spot, vanna-squeeze-up potential. The only bearish structural
  input is the static DEX short-put hedge (sell-underlying level) and near-term
  backwardation — neither is a trend engine in a long-gamma regime.
- **Conviction: 3 / 5.** Coherent mean-reversion signal. This phase **caps the
  short thesis further** (after phase-3): dealers actively dampen downside momentum
  and the mechanical pulls lean up.
- **Structural levels for phase-9:**
  1. **Max-pain 350** (near-expiry pin/upward magnet; = phase-3 call wall 350 =
     phase-2 DP supply 341–351) → the upside cap / mean-reversion target.
  2. **ZGL 187.5** — far below; confirms long-gamma, not a tradeable level. Dips
     toward the 310/300 put walls should be *dealer-bought* (supportive).
  3. **Vanna pivot ≈ spot/300–310 put-wall zone** — falling IV mechanically bids
     the underlying here; 300–310 (phase-3 put_wall_support) is the structural floor.
  - Near-expiry max-pain magnet: **350** (soft, static-OI).
- **Open questions:**
  - Does the complacent skew mean stabilization ahead, or unpriced gap risk if the
    breakdown catalyst (phase-6) is fundamental? → phase-6, phase-7b.
  - Will near-term backwardation normalize (bounce) or is front IV signalling a
    known near-term event? → phase-6 catalyst calendar.
