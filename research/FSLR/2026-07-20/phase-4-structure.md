# Phase 4 — Dealer Structure & Gamma

**Ticker:** FSLR · **As-of:** 2026-07-20 · **Underlying (struct feed):** $206.61 · **Version:** v1
**Generated:** 2026-07-20
**Cites:** phase-3-positioning.md ($250–310 call wall, $200/$205 put walls, 07-31
put-heavy P/C 2.15); phase-1-flow.md (IV rank 99, OTM call selling, earnings 07-30);
phase-2-dark-pool.md (support $205.31).

## Summary

Dealers are in a **fully short-gamma, net-short-put regime — a trend-amplifying,
mechanically bearish setup with a post-earnings vanna safety valve.** GEX is
**FULLY_NEGATIVE** (total −2.04M, *every* strike negative, **no zero-gamma level**
in range) → dealers sell dips and buy rallies inverted, i.e. **moves get amplified,
realized vol expands.** DEX is **−$226M**: the public is net put-long, dealers are
net short puts, and their hedge is to **SELL underlying** — adding mechanical
downside pressure that dovetails with the bearish flow (phase-1) and bearish new
OI (phase-3). The offset is **vanna**: because dealers are short a put-heavy book,
a **post-earnings IV collapse** (front IV 91% vs back 77%, IV rank 99) shrinks put
deltas and forces dealers to **buy back underlying** — a classic vanna-squeeze bid
*if* the stock holds its put wall. So the structure is bearish-into-weakness but
carries a built-in mechanical bid on any post-earnings vol crush that doesn't break
$200. Skew is **COMPLACENT** (puts *cheaper* than calls) — no downside fear priced
despite the bearish tape.

## Key signals

- **[STRUCT:gex]** Regime **FULLY_NEGATIVE** ("strong gamma amplification"), total
  GEX −2.04M, ZGL **null** — pure short-gamma, no long-gamma pin above; a break
  trends rather than mean-reverts.
- **[STRUCT:dex]** Net DEX **−$226M**: dealers net short puts → hedge = **sell
  underlying**. Mechanical bearish pressure aligned with flow/OI.
- **[STRUCT:vanna_charm]** net_vanna +1,120: "*falling IV → dealers (short puts)
  cover by BUYING underlying — classic vanna-squeeze setup if VIX collapses*" →
  **post-earnings IV-crush bid** if $200 holds.
- **[STRUCT:iv_term_structure]** **BACKWARDATION** (front-end IV ratio **1.182**,
  near-IV 91.4% @4DTE vs far-IV 77.3% @32DTE) = event stress into 07-30 earnings.
- **[STRUCT:term_skew]** **COMPLACENT** (skew_ratio 0.981; put-25Δ IV 76.8% <
  call-25Δ IV 78.3%) — puts *not* bid; cheap downside protection, no fear premium.

## Detailed findings

### GEX `[STRUCT:gex]`
Regime **FULLY_NEGATIVE** — "All strikes have negative net GEX — strong gamma
amplification." Total GEX **−2,043,806**, **zero_gamma_level = null** (spot is
below any flip; the entire near-term surface amplifies). Most-negative strikes
(strongest amplification) cluster at spot:
| Strike | Net GEX |
|--------|---------|
| 190 | −589,265 |
| 200 | −466,786 |
| 210 | −462,353 |
| 230 | −329,954 |
| 250 | −293,387 |
Implication: a break of **$200** sits on the second-heaviest negative-gamma
strike → downside accelerates through it; the $190 strike is the amplification
trough (max pain of a short-gamma cascade).

### DEX `[STRUCT:dex]`
Net DEX **−$226,004,046**. Tool read verbatim: *"Public is net put-long → dealers
net short puts → dealer hedge is to SELL underlying."* Reinforces the bearish
mechanical bias below spot.

### Vanna + charm `[STRUCT:vanna_charm]`
net_vanna **+1,120**, net_charm **+6,464**. Tool read: *"Public net vanna positive
(put-heavy book). Falling IV → |put delta| drops → dealers (short puts) cover by
BUYING underlying. Classic vanna-squeeze setup if VIX collapses."* → the
**post-earnings IV-crush mechanical bid**. No active squeeze *today* (needs the IV
collapse to fire); flagged as the key post-event dynamic.

### IV term structure `[STRUCT:iv_term_structure]`
Structure **BACKWARDATION** (kink_expiry null — smooth front-loaded). Front-loaded
IV = earnings event stress; expect normalization/crush after 07-30.

### Term skew `[STRUCT:term_skew]` (30-DTE target, 32-DTE actual)
**COMPLACENT** — put-25Δ IV **76.8%** vs call-25Δ IV **78.3%**, skew **−0.0146**,
ratio 0.981. Puts slightly *cheaper* than calls: no tail-hedging bid despite the
bearish flow → downside puts are relatively **cheap to own** (relevant to phase-9
structure selection), and the crowd is not braced for a drop.

### Front-end IV ratio `[STRUCT:front_end_iv_ratio]`
Ratio **1.182** (near-IV 91.4% @4DTE / far-IV 77.3% @32DTE), regime
**BACKWARDATION** — event-stress confirmation.

### Today's gamma flip (0DTE)
**Skipped** — as-of / after-hours run; 0DTE intraday ZGL is not meaningful outside
a live session. The DTE≤45 GEX above already establishes the short-gamma regime.

### Max pain `[STRUCT:max_pain]` (DTE≤30)
| Expiry | DTE | Max-pain | Dist | P/C OI | Total OI |
|--------|-----|----------|------|--------|----------|
| 2026-07-24 | 4 | **$220** | +7.2% | 0.39 | 8,366 |
| 2026-07-31 | 11 | **$220** | +7.2% | 2.15 | 4,448 |
| 2026-08-07 | 18 | $225 | +9.6% | 5.27 | 1,424 |
| 2026-08-14 | 25 | $215 | +4.8% | 4.65 | 384 |

Near-term static max-pain sits **above spot ($220, +7.2%)** — a mild *upward*
OI-magnet. **But** the total OI is thin (8k/4k) and the short-gamma regime means
price is **not pinned** — the magnet is weak and easily overridden by a trending
move. Treat $220 as indicative only; it does *not* contradict the bearish tactical
read so much as mark where a mean-revert bounce could stall. The heavy 08-21
expiry (15% of OI, phase-3) is just outside DTE≤30 and not scored here.

## Tool calls
| Tool | Args | Result |
|------|------|--------|
| options-structure gex | FSLR, dte-max 45 | FULLY_NEGATIVE, total −2.04M, ZGL null |
| options-structure dex | FSLR, dte-max 45 | net −$226M, dealers sell underlying |
| options-structure vanna-charm | FSLR, dte-max 45 | vanna +1,120, IV-crush buy-back setup |
| options-structure iv-term-structure | FSLR | BACKWARDATION |
| options-structure term-skew | FSLR, dte-target 30 | COMPLACENT, ratio 0.981 |
| options-structure front-end-iv-ratio | FSLR, 7/30 | 1.182, BACKWARDATION |
| options-structure max-pain | FSLR, dte-max 30 | $220 (07-24/07-31), thin OI |
| options-structure today-gamma-flip | — | skipped (after-hours) |

## Tool errors
None. All regime labels quoted verbatim from the tools' own `regime` /
`structure` / `interpretation` fields (not re-derived). All reads parsed via `jq`.

## Verdict for downstream

- **Dealer regime:** **SHORT GAMMA (FULLY_NEGATIVE), net short puts, hedging by
  selling underlying** — mechanically bearish and **trend-amplifying**. Overlaid
  with a **post-earnings vanna-squeeze bid** (IV crush → dealers buy back) that
  fires *only if $200 holds through earnings*.
- **Conviction: 4/5** — the clearest, most corroborated structural read in the
  chain (GEX regime label + DEX sign + backwardation all agree). This is the phase
  that most sharpens the thesis: **weakness accelerates; a hold triggers a bid.**
- **Three structural levels for phase-9:**
  1. **ZGL = null / spot in pure short gamma** — no long-gamma cushion; treat the
     whole $190–210 zone as amplification. **$200** = the second-heaviest negative-
     gamma strike → the acceleration trigger (aligns with phase-3 put wall &
     phase-2 $205.31 shelf).
  2. **$190** — negative-gamma trough (−589k) = downside cascade magnet / short
     target on a break of $200.
  3. **Near max-pain $220** = weak static upward magnet / mean-revert cap; the
     $240 call wall (phase-3) is the firmer ceiling.
- **Open questions:**
  - Does earnings (07-30) break $200 (short-gamma cascade toward $190) or hold it
    (vanna IV-crush bid back toward $215–220)? This binary defines the trade.
  - Complacent skew + bearish flow: is cheap put IV an opportunity to own downside
    into earnings, or a sign the smart-money bearishness is vol-selling not
    conviction-shorting? Phase-8b to adjudicate.
  - Post-earnings, does the vanna bid overwhelm the bearish DEX pressure? Depends
    on realized move vs the ±5.3% implied.
