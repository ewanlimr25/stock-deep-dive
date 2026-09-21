# Phase 4 — Options Structure / GEX

**Ticker:** NVDA
**As-of date:** 2026-05-29
**Generated:** 2026-05-30T13:55Z
**Upstream phases cited:** phase-0.5-context.md, phase-1-flow.md, phase-3-positioning.md

## Summary

Dealers are **net LONG gamma (POSITIVE regime, total GEX +$263M)** — a
**mean-reverting / vol-dampening** structure, not an explosive one. Positive
gamma is stacked **215–230 (above spot)** and negative gamma sits **195–210
(below spot)**, with the zero-gamma transition just **~1.6% above** the structure's
212.62 anchor (≈ **215–216**). Practically: the **215–230 zone is a pinning
ceiling** — dealer hedging there *sells* rallies and *buys* dips, dampening upside;
**below ~210 dealers flip short gamma**, where moves can accelerate. This frames a
**range-bound-to-capped tape**: the 215–230 call strikes phase-1/3 highlighted are
exactly where dealer long gamma will **resist** price (and where phase-3 showed
those calls being *written*) — confirming 215–230 as a supply ceiling, not a
breakout. IV term structure is **CONTANGO** (front 37–47% rising to back) with **no
event kink** — no near-term catalyst priced (earnings Aug-26). 25Δ skew at the
1-yr tail is mildly COMPLACENT. DEX is net call-long (dealers short calls → hedge
buys dips, the source of the pin). **Vol regime: positive gamma / mean-reverting,
with a downside short-gamma trapdoor below 210. Bias: neutral-range, capped 215–230,
vulnerable <210. Conviction 3/5.**

## Key signals

- [STRUCT:gex] **Regime POSITIVE — dealers net long gamma, total_gex +$263.0M**
  ("expect mean-reversion and reduced volatility"). Anchor underlying 212.62.
- [STRUCT:gex] **Positive (pinning) gamma above spot**: K220 +$76.5M, K215
  +$56.6M, K225 +$45.5M, K217.5 +$39.3M, K230 +$38.1M — the **215–230 ceiling**.
- [STRUCT:gex] **Negative (amplifying) gamma below spot**: K210 −$28.0M, K195
  −$24.4M, K207.5 −$21.5M, K205 −$11.2M — a **short-gamma trapdoor below ~210**.
- [STRUCT:gex] **Zero-gamma transition ≈ +1.6% above 212.62 anchor (≈215–216)** —
  spot 211.14 sits *below* the flip, in the negative-gamma zone → near-term moves
  amplify until price reclaims ~215.
- [STRUCT:iv-term-structure] **CONTANGO, no kink** (6-DTE 46.7% → 19-DTE 43.2% →
  rising into back) — no binary event priced near term. [STRUCT:dex] net DEX
  +$15.6B call-long (dealers short calls → hedge buys dips).

## Detailed findings

### GEX by strike (dealer net gamma)

| zone | strikes | dealer gamma | implication |
|------|---------|--------------|-------------|
| ceiling (215–230) | 220 +$76.5M, 215 +$56.6M, 225 +$45.5M, 217.5 +$39.3M, 230 +$38.1M | **long (positive)** | rallies into 215–230 **get sold/pinned** — resistance |
| transition | ~215–216 (zero-gamma) | flip | regime boundary |
| trapdoor (195–210) | 210 −$28.0M, 207.5 −$21.5M, 205 −$11.2M, 195 −$24.4M | **short (negative)** | below 210, moves **accelerate** (downside risk) |

Total GEX is net positive (+$263M), so the *dominant* regime is mean-reverting —
but the negative-gamma pocket directly below spot (195–210) is the structural
risk: if 210 fails, dealer hedging flips from stabilizing to amplifying, opening
air toward the 195–200 negative-gamma / put-build levels (195 = −$24.4M dealer
gamma [STRUCT:gex]; 200 = the 200P 49-DTE build [OI:biggest-increases]). NOTE: max
pain was NOT computed this run (`uw options-structure` exposes no max-pain leaf);
these are gamma/OI levels, not a max-pain calculation.

### Zero-gamma flip

- Field `zero_gamma_level = 1.59` (≈ **+1.6% above the 212.62 anchor ≈ 215–216**;
  reported as a normalized distance, not an absolute price).
- Spot 211.14 is **below** the flip → currently in/near the negative-gamma zone.
- **Reclaiming ~215 flips dealers fully long-gamma and pins; losing 210 drops into
  the short-gamma trapdoor.** This 210↔215 band is the regime hinge.

### IV term structure & skew

- **CONTANGO** (front 37–47%, back higher), `kink_expiry: None` → **no event
  premium**, consistent with earnings being far (Aug-26). 6-DTE IV 46.7% is the
  local front-end bump (post-down-day demand), easing to 43% by Jun-18.
- **25Δ term skew (1-yr): COMPLACENT** (skew −0.053, put_25d_iv 41.7% < call_25d_iv
  47.0%, ratio 0.887) — far-dated calls bid over puts; no tail-hedging panic at
  the 1-yr tenor. (Note: near-dated downside hedging *is* visible in phase-3's
  95P/110P 7-DTE builds — the complacency is at the long tenor, not the front.)

### DEX (dealer delta)

- net_dex **+$15.6B** call-long public → dealers net **short calls** → their hedge
  is to **buy underlying on dips**. This is the mechanical source of the
  mean-reversion: it cushions selloffs *while spot stays above ~210* and the long
  gamma holds. Below the short-gamma flip the cushion inverts.

### Reconciliation with prior phases

The structure **confirms 215–230 as a ceiling, not a launchpad** — precisely where
phase-1 saw call buying and phase-3 saw those calls being *written*. Dealer long
gamma there means even if price pushes up, hedging sells into it. The bullish
near-dated call flow is fighting both the structure and the phase-2 distribution.
The clearest risk is a **break of 210** into the negative-gamma trapdoor.

## Tool calls (audit trail)

| Command | Result |
|---------|--------|
| `uw options-structure gex --symbol NVDA --date 2026-05-29 --json` | POSITIVE regime, +$263M, ceiling 215–230 |
| `uw options-structure iv-term-structure --symbol NVDA --date 2026-05-29 --json` | CONTANGO, no kink |
| `uw options-structure term-skew --symbol NVDA --date 2026-05-29 --json` | 1-yr skew COMPLACENT (−0.053) |
| `uw options-structure dex --symbol NVDA --date 2026-05-29 --json` | net DEX +$15.6B call-long |

## Tool errors

```
# `gamma-exposure` / `gex-by-strike` / `max-pain` are NOT valid options-structure
# leaves. Valid leaves: dex, front-end-iv-ratio, gex, iv-term-structure,
# term-skew, today-gamma-flip, vanna-charm. Used `gex` for the surface.
# zero_gamma_level returned as a normalized distance (1.59) rather than an absolute
# price; interpreted as ~+1.6% above the 212.62 anchor (≈215–216).
```

## Verdict for downstream phases

- **Vol regime:** POSITIVE gamma / mean-reverting (total GEX +$263M), with a
  negative-gamma trapdoor below ~210.
- **Bias from this phase:** NEUTRAL-RANGE, **capped 215–230**, **vulnerable below 210**.
- **Conviction:** 3/5 (native gex/dex/iv tools, clean read).
- **Three datapoints later phases must remember:**
  1. **215–230 is a dealer long-gamma ceiling** — rallies get sold there; aligns
     with phase-3 call-writing. Not a breakout zone.
  2. **210 is the regime hinge**: above it (to ~215) dealers cushion dips; **below
     210 = short-gamma trapdoor** → downside acceleration risk.
  3. **No event premium** (IV CONTANGO, no kink; earnings Aug-26 far) — this is a
     positioning/flow tape, not a catalyst setup.
- **Open questions:** Does history (phase-5) show NVDA's positive-gamma down days
  mean-reverting up or grinding lower? Does macro/sector (phase-6) threaten the
  210 hinge? Sentiment (7c) — is the near-dated put/tail-hedge build rising?
