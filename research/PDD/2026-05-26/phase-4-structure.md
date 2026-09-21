# Phase 4 — Dealer Structure & Gamma

**Ticker:** PDD
**As-of date:** 2026-05-26
**Generated:** 2026-05-26T20:34:00Z
**Upstream phases cited:** phase-1-flow.md, phase-3-positioning.md, phase-0.5-context.md

## Summary

Dealers are **fully short gamma into the print — a move-amplifying regime — with a
post-earnings vanna squeeze coiled underneath.** GEX is `FULLY_NEGATIVE`: every strike
≤45 DTE carries negative net GEX, total **−$12.8M**, and there is **no zero-gamma level**
(the whole near-term book is short γ) [STRUCT:gex]. The heaviest negative-gamma strike is
**95 (−$8.63M)**, just below the $96.58 close — break below it and dealer hedging
*accelerates* the decline. DEX is **−$347M** (put-heavy public → dealers short puts →
hedge by selling underlying) [STRUCT:dex]. The term structure is steep **BACKWARDATION**
(5/29 IV **98.3%** vs back months ~42%; front/far ratio **1.344**) [STRUCT:iv_term /
front_end_iv_ratio] — severe event stress and a brutal post-print IV crush. But that same
put-heavy book is a **classic vanna-squeeze setup** (net vanna +5,795): when IV collapses
after earnings, dealers short puts must **buy back underlying** → a mechanical bid *if
spot holds or rises* [STRUCT:vanna_charm]. Net: **binary, gamma-amplified both ways,
downside more dangerous mechanically, upside favoured if it survives the print.**

## Key signals

- **Short-gamma everywhere:** GEX `FULLY_NEGATIVE`, total −$12.8M, **ZGL = null**
  [STRUCT:gex] → trend amplification, expanded realized vol on the print.
- **Downside accelerant at 95:** net_gex −$8,625,909 at strike 95 (largest), plus −$4.19M
  at 90 and −$3.73M at 100 [STRUCT:gex]. Below 95 = short-gamma cascade risk.
- **Upside gamma cap 104–110:** positive GEX flips in at 104 (+$1.04M), 105 (+$0.79M),
  peaking **110 (+$2.77M)**, 115 (+$1.20M), 120 (+$1.07M) [STRUCT:gex] — light damping on
  rallies into those strikes (the phase-3 written-call wall).
- **Dealers short puts, hedge = sell:** net_dex −$347M, put_dex −$611M [STRUCT:dex] —
  reinforces the downside-amplification mechanic.
- **Vanna squeeze armed:** net_vanna +5,795 (put-heavy); "falling IV → dealers buy
  underlying" [STRUCT:vanna_charm] — a post-crush tailwind conditional on spot not gapping
  down hard.
- **Steep earnings backwardation:** 5/29 98.3% → 6/18 49.0% → ~42% back; front/far 1.344
  [STRUCT:iv_term / front_end_iv_ratio] → confirms severe vol-crush risk on long premium.

## Detailed findings

### GEX — `[STRUCT:gex]` (underlying $96.96, dte_max 45)

- **Regime: FULLY_NEGATIVE**, total_gex **−$12,800,801**, zero_gamma_level **null**.
- Negative-gamma mass concentrated **at/below spot**: 95 (−$8.63M), 90 (−$4.19M),
  100 (−$3.73M), 94 (−$2.63M), 91 (−$0.74M), 80 (−$0.31M).
- Positive-gamma mass **above spot**: 110 (+$2.77M), 115 (+$1.20M), 120 (+$1.07M),
  104 (+$1.04M), 105 (+$0.79M), 99 (+$0.42M), 98 (+$0.31M).
- Read: spot $96.58 sits in the negative-gamma zone; the first local positive-gamma shelf
  is ~98–99, the real positive-γ cap is 104–110. **Downside is mechanically the dangerous
  tail; upside meets gamma resistance at 104–110.**

### DEX — `[STRUCT:dex]`

- net_dex **−$347,362,436** (call_dex +$264M, put_dex −$611M). Public net put-long →
  dealers net short puts → **dealer hedge sells underlying** on weakness. Consistent with
  phase-3 put accumulation and the short-gamma regime.

### Vanna + charm — `[STRUCT:vanna_charm]`

- net_vanna **+5,795** (put_vanna +8,701, call_vanna −2,906), net_charm +44,606.
- **Vanna-squeeze setup:** put-heavy book + dealers short puts + imminent post-earnings IV
  collapse → |put delta| shrinks → dealers buy back underlying = **mechanical bid after the
  print, conditional on spot holding/rising.** The single most constructive forward signal
  in the workup — but it does *not* protect against a hard gap-down (where gamma
  amplification dominates first).

### IV term structure — `[STRUCT:iv_term_structure]`

**BACKWARDATION** (16 expiries):

| Expiry | avg IV | Note |
|--------|--------|------|
| 2026-05-29 | **98.3%** | post-earnings weekly — the event vol |
| 2026-06-05 | 61.1% | |
| 2026-06-18 | 49.0% | monthly |
| 2026-07-17 | 42.3% | baseline |
| 2027-01-15 | 40.6% | LEAP floor |

The 5/29 front is **~2.3× the back-month baseline**. Post-print, that 98% collapses toward
~45% → any long 5/29 premium suffers a ~50-vol-point crush regardless of direction.

### Term skew (30 DTE) — `[STRUCT:term_skew]`

- **COMPLACENT.** put_25d_iv 0.4304 **<** call_25d_iv 0.4449, skew −0.0144, ratio 0.968.
- At the monthly tenor, **calls are richer than puts** (call-demand skew) — structurally
  positioned for upside beyond the event, *and* nobody is paying up for monthly downside
  protection (a contrarian yellow flag if it gaps down). Reconciles with phase-3: front-end
  event puts are hedges; term demand is for calls.

### Today's gamma flip — `[STRUCT:today_gamma_flip]`

**Skipped.** 0DTE-only intraday tool; PDD has no 0DTE listings (nearest expiry 5/29) and
this is an as-of/post-session read — not meaningful per the phase guidance.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `options_structure_gex` | symbol=PDD, dte45 | FULLY_NEGATIVE, −$12.8M, ZGL null; −8.63M@95 |
| `options_structure_dex` | symbol=PDD, dte45 | net_dex −$347M, dealers short puts, hedge sells |
| `options_structure_vanna_charm` | symbol=PDD, dte45 | net_vanna +5,795 → post-crush squeeze setup |
| `options_structure_iv_term_structure` | symbol=PDD | BACKWARDATION, 5/29 98.3% → back 42% |
| `options_structure_term_skew` | symbol=PDD, dte30 | COMPLACENT, calls richer (ratio 0.968) |
| `options_structure_front_end_iv_ratio` | symbol=PDD, 7/30 | ratio 1.344 BACKWARDATION |
| `options_structure_today_gamma_flip` | — | skipped (no 0DTE; post-session) |

## Tool errors

None.

## Verdict for downstream phases

- **Dealer regime:** **SHORT GAMMA (fully negative, no ZGL).** Move amplification into the
  print; downside mechanically the more dangerous tail (−$8.63M gamma at 95). Bias from
  structure is **neutral on direction but high on volatility**, with a **post-crush vanna
  bid favouring upside if spot survives**.
- **Conviction:** **4/5** on the regime read (PDD has deep OI >1M, GEX/DEX are meaningful
  here, not coarse).
- **Three structural levels for phase-9:**
  1. **95 — short-gamma trigger / downside accelerant** (net_gex −$8.63M). A post-earnings
     break below 95 invites a dealer-driven cascade; coincides with phase-2 $94.52 support
     and phase-3 put wall. The line that matters on the downside.
  2. **104–110 — positive-gamma cap** (110 = +$2.77M peak). Upside meets dealer gamma
     resistance + phase-3 written-call supply here; first real overhead on a squeeze.
  3. **No ZGL / ~98–99 local pivot** — reclaiming 98–99 (first positive-γ shelf) post-print
     is the line between "still in the danger zone" and "vanna bid engages."
- **Open questions:** Will the 5/27 print push spot above 98–99 (vanna bid engages, upside)
  or below 95 (gamma cascade, downside)? The structure says the move will be *large* either
  way (confirms 5.69% implied). Direction is the earnings outcome — phase-5 (historical
  earnings reaction) and phase-7b (fundamentals) must inform the directional lean since flow
  itself is two-sided.
