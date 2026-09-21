# Phase 4 — Dealer Structure & Gamma

**Ticker:** AAPL
**As-of date:** 2026-05-27
**Generated:** 2026-05-28T03:08:00Z
**Upstream phases cited:** phase-2-dark-pool.md, phase-3-positioning.md

## Summary

Dealers are **net long gamma** (total GEX +$382M, regime POSITIVE) with the
**dominant gamma wall sitting exactly at 310 (+$109M net_gex) = spot** — a strong
mean-reversion/pin configuration that **suppresses realized vol and argues against
a clean directional move**. The usable zero-gamma level is **≈297** (0DTE
`today_zero_gamma 297.21`; the 45-DTE call's `zero_gamma_level 5.07` is a
degenerate artifact, discarded). Term structure is **contango** and skew is
**COMPLACENT** (25Δ put/call ratio 1.019 — almost flat, no downside fear priced),
confirming a calm, no-event regime (next earnings 7/30). DEX is +$13.9B (dealers
buy underlying to hedge a call-long public — mild supportive bid), but **net vanna
is negative**: if IV drifts lower from already-low levels, dealers cut that hedge =
mechanical selling. **Net: NEUTRAL / range-bound, pinned to ~310; long gamma is
the dominant fact and it caps directional conviction.**

## Key signals

- **GEX regime POSITIVE / long gamma**, total +$382M; dominant wall at **310
  (+$109M)** = spot → mean-reversion, vol suppression `[STRUCT:gex]`
- Usable **ZGL ≈ 297** (0DTE `today_zero_gamma 297.21`); below it dealers flip
  short-gamma (downside accelerant) `[STRUCT:today_gamma_flip]`
- **DEX +$13.9B** — public call-long, dealers BUY underlying to hedge → mild
  mechanical bid `[STRUCT:dex]`
- **Net vanna negative (−70,509)** — falling IV → dealers cut long hedge →
  selling pressure (headwind if IV keeps dropping) `[STRUCT:vanna_charm]`
- **Skew COMPLACENT** (put 25Δ 23.3% vs call 22.9%, ratio 1.019) + **contango**
  (front-end IV ratio 0.89) → no event stress, no tail-hedge demand `[STRUCT:term_skew]` `[STRUCT:front_end_iv_ratio]`

## Detailed findings

### GEX (gamma exposure)

- **Regime: POSITIVE** — "Dealers net long gamma → expect mean-reversion and
  reduced volatility." total_gex **+382,476,597**, underlying $310.77.
- Largest |net_gex| walls (DTE ≤ 45), 290–345 band:

| Strike | net_gex | Role |
|--------|---------|------|
| **310** | **+109.5M** | dominant wall = **spot pin/magnet** |
| 315 | +61.3M | upside wall (resistance) |
| 312.5 | +49.9M | upside wall |
| 320 | +48.4M | upside wall (= phase-3 pin strike) |
| 300 | +30.6M | downside wall (= phase-3 unwind / above DP support) |

Spot pinned on the biggest positive-gamma strike (310) → dealers sell rallies
above and buy dips below 310 within the wall band. **Expect oscillation 305–315
with vol suppressed** absent a regime-breaking catalyst.

- **ZGL:** the 45-DTE GEX returned `zero_gamma_level 5.07` — **implausible as a
  price, discarded as a degenerate artifact** (per pitfall: ZGL coarse/unreliable).
  The 0DTE `today_gamma_flip` returns **`today_zero_gamma 297.21`** with spot
  $310.68 → spot well above ZGL, long-gamma confirmed. **~297 is the flip level**:
  a break below ~297 turns dealers short-gamma and would amplify a selloff.

### DEX (dealer delta)

- net_dex **+$13.9B** (call_dex +$15.2B, put_dex −$1.24B). Interpretation:
  "Public is net call-long → dealers net short calls → dealer hedge is to BUY
  underlying." A **mild standing bid** that supports spot — consistent with the
  long-gamma dip-buying behavior.

### Vanna + charm

- net_vanna **−70,509** (call-heavy book), net_charm +1,111,804.
- Interpretation: "Falling IV → call delta drops → dealers (short calls) cut
  long-underlying hedge → **SELLING pressure**. Rising IV reverses." With IV rank
  only 32 and contango/complacency, **the path of least resistance for IV is
  flat-to-down → vanna is a mild headwind**, not a squeeze. **Not** a vanna-squeeze
  setup (that needs positive vanna + negative dealer delta + falling IV).

### IV term structure

- **CONTANGO** (normal upward slope): 2DTE 28.1% → 7DTE 22.4% → 30DTE ~25% out the
  curve (0DTE 2.9% is an expiry-day degenerate, ignore). No backwardation = **no
  event stress**. Next earnings 2026-07-30 sits well out the curve.

### Term skew (25Δ put vs call)

- **COMPLACENT** — put_25d_iv 23.33% vs call_25d_iv 22.88%, **skew_ratio 1.019**
  (puts barely richer than calls). Unusually flat skew for a mega-cap = minimal
  downside fear priced. Mild contrarian yellow flag: protection is cheap precisely
  because no one wants it — fine while calm, but no cushion if a shock hits.

### Front-end IV ratio (event stress)

- ratio **0.89** (near 7DTE 22.4% < far 30DTE 25.2%) = **CONTANGO**, no front-end
  stress. Confirms calm regime.

### Today's gamma flip (0DTE)

- regime POSITIVE, today_total_gex +$60.2M, **today_zero_gamma 297.21**,
  atm_flip_strike 270, spot $310.68. (Run is EOD/as-of, not live-intraday — used
  here only for its ZGL read, which corrects the broken 45-DTE ZGL.)

## Tool calls (audit trail)

| Command | Result summary |
|---------|----------------|
| `uw options-structure gex --dte-max 45` | POSITIVE/long-γ, total +$382M, wall at 310; ZGL field degenerate (5.07) |
| `uw options-structure dex --dte-max 45` | net +$13.9B, dealers buy underlying (mild bid) |
| `uw options-structure vanna-charm --dte-max 45` | net vanna −70,509 (falling-IV = dealer selling) |
| `uw options-structure iv-term-structure` | CONTANGO, no event stress |
| `uw options-structure term-skew --dte-target 30` | COMPLACENT, skew_ratio 1.019 |
| `uw options-structure front-end-iv-ratio --near 7 --far 30` | 0.89, CONTANGO |
| `uw options-structure today-gamma-flip` | ZGL 297.21 (usable), long-γ confirmed |

## Tool errors

None (the 45-DTE `zero_gamma_level 5.07` is a degenerate value, not a tool error —
noted and superseded by the 0DTE ZGL 297.21).

## Verdict for downstream

- **Dealer regime:** **LONG GAMMA / range-bound**, pinned to ~310. This is the
  single most decision-relevant structural fact — it suppresses directional moves
  and means any phase-1/2 bullish lean has to fight dealer mean-reversion.
- **Conviction:** **3/5** (high confidence in the *range-bound/neutral* read; this
  is a confident neutral, not a directional call).
- **Three structural levels for phase-9:**
  1. **310** — dominant gamma wall = spot pin/magnet (expect gravitation here).
  2. **315 → 320** — stacked upside gamma walls = resistance (dealers sell into).
  3. **~297** — zero-gamma flip; below it long→short gamma, downside accelerates.
     (300 wall + DP $302–305 support sit just above this as the first line.)
- **Open questions:**
  - What breaks the long-gamma pin? → phase-5 (historical vol regime) + phase-6
    (macro catalyst) + phase-7c (positioning).
  - Does the complacent skew + negative vanna mean a small IV pop would be a
    bigger up-move than down (or vice-versa)? Resolve in phase-9 structure choice.
