# Phase 4 — Dealer Structure & Gamma

**Ticker:** KWEB
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T00:00:00Z
**Upstream phases cited:** phase-2-dark-pool.md, phase-3-positioning.md

## Summary

The dealer map is **locally short-gamma at/below spot, flipping long-gamma above
28.5**, with a mechanical sell overhang and a latent bull kicker. Spot $26.88 sits
in a **negative-gamma pocket** (strikes 25–28 net negative, dominated by **strike
27 at −$41.5M GEX**), so price here is *trend-amplifying / slippery* — dealers buy
rallies and sell dips, expanding realized vol. Gamma flips **positive at ~28.5–29**
and builds a **long-gamma resistance shelf at 29–31** (+$18M/+24M/+25M), which
dampens and pins moves into that zone — reinforcing phase-3's June 30–31 call walls
and phase-2's $28 DP supply. DEX is strongly negative (**−$334M**: public put-long,
dealers short puts hedging by **selling underlying** → a structural overhang that
corroborates phase-2's distribution). Counterweight: **vanna/charm flag a
vanna-squeeze setup** — net vanna positive on a put-heavy book, so **if IV falls,
dealers cover by buying** (a latent bullish bid conditional on risk-on / vol
compression). Term structure is **calm**: contango, normal 30d skew, flat front-end
— **no event stress, no imminent binary catalyst** (KWEB is an ETF, no earnings).

## Key signals

- GEX regime **POSITIVE total (+$39.0M)** but **locally SHORT gamma at spot**:
  strike 27 = **−$41.5M**, 28 = −$14.2M, 26 = −$9.9M, 25 = −$5.8M `[STRUCT:gex]`.
- **Gamma flip ~28.5–29**: 28.5 +$6.5M, 29 +$18.3M → long-gamma above; 30 +$24.2M,
  31 +$25.1M form the resistance/pin shelf `[STRUCT:gex]`.
- DEX **net −$333.7M** (put_dex −$524M): dealers short puts → **hedge = sell
  underlying** → mechanical overhang `[STRUCT:dex]`.
- **Vanna-squeeze setup**: net_vanna +19,144, charm +554,720 → falling IV ⇒ dealer
  **buying** (bullish kicker if vol compresses) `[STRUCT:vanna_charm]`.
- Vol calm: term structure **CONTANGO**, 30d skew **NORMAL** (ratio 1.051),
  front-end **FLAT** (7d/30d 1.037) — no catalyst stress `[STRUCT:iv_term_structure]`
  `[STRUCT:term_skew]` `[STRUCT:front_end_iv_ratio]`.

## Detailed findings

### GEX (per-strike, dte≤45) `[STRUCT:gex]` — spot $26.88

| Zone | Strikes | Net GEX | Dealer behavior |
|------|---------|---------|-----------------|
| **Short-gamma pocket (spot here)** | 25 / 26 / **27** / 28 | −5.8M / −9.9M / **−41.5M** / −14.2M | buy rallies, sell dips → **trend-amplifying, slippery** |
| **Flip** | 28.5 / 29 | +6.5M / +18.3M | transition to long gamma |
| **Long-gamma resistance shelf** | 30 / 31 / 32 / 33 | +24.2M / +25.1M / +7.8M / +10.6M | sell rallies, buy dips → **pins / caps** |

Total GEX is +$39.0M (the big 29–33 positive walls dominate the sum), but the
**actionable local read is short gamma around spot**. The tool's `zero_gamma_level
= 15` is a coarse/degenerate artifact for this ETF (note: "GEX most meaningful for
index products… deep OI") — the *effective* flip from the per-strike profile is
**~28.5**. Treat ZGL as a ±2% band around 28–28.5.

### DEX (net dealer delta) `[STRUCT:dex]`

net_dex **−$333.7M** (call_dex +$190M, put_dex −$524M). Public is **net put-long**;
dealers are short those puts and hedge by **selling underlying** — a standing
mechanical sell pressure that aligns with phase-2's mega/block distribution. As the
deep-ITM 34P/35P close (phase-3) and puts decay, this overhang should ease.

### Vanna + charm `[STRUCT:vanna_charm]`

net_vanna **+19,144** (put_vanna +27,628), net_charm **+554,720**. On this put-heavy
book, **falling IV shrinks |put delta| → dealers (short puts) buy underlying to
re-hedge** = a **vanna-squeeze bid**. With IV rank at 38.9 (down from a mid-May 88.8
peak, per phase-0.5), this is a live, asymmetric **bullish kicker if China risk-off
abates and IV keeps compressing**. Positive charm is mildly supportive into June OPEX.

### IV term structure / skew / front-end

- **Term structure: CONTANGO** — 05-29 34.9% → 06-18 36.0% → back ~35–40%; no kink
  (`kink_expiry: null`). Normal upward slope, no binary event priced `[STRUCT:iv_term_structure]`.
- **30d skew: NORMAL** — put_25Δ 35.0% vs call_25Δ 33.3%, ratio 1.051. Slight put
  premium, not tail-hedging, not complacent `[STRUCT:term_skew]`.
- **Front-end (7d/30d): FLAT** — 35.9% / 34.6%, ratio 1.037 (< 1.05 backwardation
  cutoff). No event stress `[STRUCT:front_end_iv_ratio]`.

### Today's gamma flip (0DTE intraday)

**Skipped by design** — `today_gamma_flip` is a 0DTE intraday hedge map; this is an
**EOD/after-hours as-of read (2026-05-22)**, so an intraday 0DTE flip is not
actionable. The dte≤45 GEX above supplies the structural levels instead.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `options_structure_gex` | KWEB, dte45 | +39M total; short γ at spot (27=−41.5M); flip ~28.5 |
| `options_structure_dex` | KWEB, dte45 | net −334M; dealers sell to hedge short puts |
| `options_structure_vanna_charm` | KWEB, dte45 | vanna-squeeze setup if IV falls |
| `options_structure_iv_term_structure` | KWEB | CONTANGO, no kink |
| `options_structure_term_skew` | KWEB, dte30 | NORMAL, ratio 1.051 |
| `options_structure_front_end_iv_ratio` | KWEB, 7/30 | FLAT, ratio 1.037 |
| `options_structure_today_gamma_flip` | — | skipped (EOD, not intraday) |

## Tool errors

(none)

## Verdict for downstream phases

- **Dealer regime:** **SHORT gamma at/below spot (trend-amplifying), flipping LONG
  gamma above ~28.5 (pinning/capping into 29–31)**; mechanical sell overhang via
  negative DEX; latent vanna-squeeze bid if IV compresses. Vol regime calm (no event).
- **Conviction:** **3.5/5** — per-strike GEX/DEX/vanna are coherent and corroborate
  phases 2–3; de-rated modestly for the ETF GEX caveat and the coarse ZGL.
- **Three structural levels for phase-9:**
  1. **~28.5–29 gamma flip** — the pivot from short-γ (volatile, trend) to long-γ
     (pinned). Bull case *needs* this reclaim; it coincides with phase-2 $28 supply
     and phase-3 call walls → a stacked resistance band **$28–29**.
  2. **$27 — max short-gamma node (−$41.5M)** — spot sits just below; price is
     slippery here, prone to sharp moves both ways; breaks extend.
  3. **$29–31 long-gamma shelf** — sticky upside resistance/cap (with the June
     30–31 call walls); the bull target zone but mechanically dampened.
- **Open questions:**
  1. Which force wins near-term: the **negative-DEX sell overhang** (heavy) vs the
     **vanna-squeeze bid** (needs IV to fall)? Resolution hinges on China risk
     sentiment → **phase-6/7c**.
  2. With spot in a short-gamma pocket and **no near-term pin** (phase-3), is the
     path more likely a **trend down to 25–26** or a **vol-compression squeeze to
     28–29**? The historical base rates (phase-5) and macro (phase-6) decide.
