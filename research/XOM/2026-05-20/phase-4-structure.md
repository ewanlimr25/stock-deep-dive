# Phase 4 — Dealer Structure & Gamma

**Ticker:** XOM
**As-of date (user request):** 2026-05-20
**Effective data date:** 2026-05-18 (close, spot $160.09 per GEX tool / $160.41 per OI snapshot)
**Generated:** 2026-05-19T00:00:00Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md

## Summary

XOM dealer book is **deeply long-gamma in a positive GEX regime** ($23.2B
aggregate net GEX, dte≤45), with spot $160 sitting **$105 above the
aggregate ZGL of $55.03**. The dominant gamma mass is **+$9.75B at the $165
strike** (Jun'26 165C OI 18,186 from phase-3) and **+$6.66B at $160**. Net DEX
is **+$315.0B (call-heavy public, dealer net short calls, dealer hedge =
LONG underlying)** — this confirms phase-3's bullish positioning read and
explains the institutional accumulation in phase-2 at $150–152. IV term
structure is in **backwardation** (May 22 40.8% → Jun 18 33.5%) with a
**COMPLACENT** 30-DTE skew (call IV 32.86% > put IV 31.49% — calls richer
than puts is the **inverse of normal** and a tell that upside demand is
pricing-dominant). Critical level: **OPEX-week ZGL = $153.09** — below
this strike dealer flips to short-gamma and downside accelerates.

## Key signals

- **Dealer regime: STRONGLY POSITIVE GAMMA / long-gamma.** Total net GEX
  $23,230,980,610 (DTE≤45). ZGL $55.03 vs spot $160.09 ⇒ spot is in
  long-gamma territory by a wide margin. Expect mean-reversion in
  $152.5–$170 corridor; reduced realized vol. [STRUCT:gex]
- **The $165 strike is the single largest gamma magnet at $9.75B net GEX**,
  followed by **$160 at $6.66B** and **$180 at $1.63B**, **$170 at $1.39B**.
  Dealers are long stock to hedge their short calls → as spot approaches $165,
  dealers SELL underlying to maintain delta-neutral hedge → **$165 acts as
  sticky resistance / pin magnet, NOT a breakout level**. [STRUCT:gex]
- **Net DEX +$315.0B** (call DEX +$335.0B, put DEX -$20.0B). Public is
  10× more call-long than put-long in delta dollars. Dealer hedge = long
  underlying. Continued call buying mechanically forces dealer to keep
  buying stock — supportive but constrained by the long-gamma sell-on-rally
  mechanic. [STRUCT:dex]
- **30-DTE term skew COMPLACENT (call IV > put IV, skew_ratio 0.958)** —
  call 25Δ IV 32.86% vs put 25Δ IV 31.49%. **Inverted from normal index
  skew.** Upside demand is dominating put-hedge demand in vol pricing. Often
  precedes either continuation of the up-move OR a sharp mean-revert if
  complacency unwinds. [STRUCT:term_skew]
- **OPEX-week (May 22) ZGL = $153.09**. Below this level, dealer flips to
  short-gamma and downside accelerates. Above it (current spot $159.86),
  dealer continues long-gamma mean-reversion behavior with $160 as the
  strongest support wall ($4.10B today_GEX). [STRUCT:today_gamma_flip]

## Detailed findings

### GEX (DTE ≤ 45)

**Total net GEX:** +$23,230,980,610
**Zero Gamma Level (ZGL):** $55.03
**Underlying price (per tool):** $160.09
**Regime:** POSITIVE — "Dealers net long gamma — expect mean-reversion and
reduced volatility"

Top-10 positive-GEX strikes (long-gamma anchors):

| Rank | Strike | Net GEX | Distance from spot | Notes |
|------|--------|---------|--------------------|-------|
| 1 | **$165** | +$9,749,363,698 | +3.1% | Largest gamma magnet, matches Jun'26 165C OI 18,186 |
| 2 | **$160** | +$6,661,131,731 | 0% | Current spot, primary anchor |
| 3 | $180 | +$1,629,727,236 | +12.4% | Far-OTM gamma (LEAP overflow) |
| 4 | $170 | +$1,388,389,711 | +6.2% | Upside continuation |
| 5 | $162.5 | +$1,200,522,153 | +1.5% | Inter-strike |
| 6 | $157.5 | +$930,674,515 | -1.6% | Lower support |
| 7 | $155 | +$901,769,345 | -3.2% | Support |
| 8 | $185 | +$608,487,979 | +15.6% | Far-OTM (lotto) |
| 9 | $175 | +$293,522,191 | +9.3% | |
| 10 | $167.5 | +$133,087,550 | +4.6% | |

Top negative-GEX strikes (short-gamma zones, downside accelerators):

| Strike | Net GEX | Distance from spot |
|--------|---------|--------------------|
| $140 | -$126,825,764 | -12.6% |
| $145 | -$73,292,027 | -9.4% |
| $135 | -$50,025,579 | -15.7% |
| $150 | -$24,349,439 | -6.3% |
| $125 | -$22,701,958 | -22.0% |
| $130 | -$8,315,628 | -18.8% |

**Read:** A break below ~$152.5 (ATM flip) sends the dealer book into the
$140-145-150 short-gamma cluster, which would amplify any decline. But to
get *to* $150, spot has to break $155 first, which is itself a $902M positive
GEX support level. The gamma topology produces a step-down ladder of
defense: $157.5 → $155 → $152.5 → THEN short-gamma cliff.

### DEX (dealer delta hedge)

- **Net DEX:** +$315,020,687,821
- **Call DEX:** +$334,993,499,758
- **Put DEX:** -$19,972,811,937
- **Spot:** $160

Tool interpretation (verbatim): "Public is net call-long → dealers net short
calls → dealer hedge is to BUY underlying."

Implication: dealers have been mechanically bidding XOM as the public
levered into calls. Phase-2's 5-day institutional accumulation cluster at
$150-152 was likely **partially dealer hedging buys** layered on top of
strategic accumulation. Phase-3's +8,150 OI Δ on Jun'26 165C alone added an
estimated $9.75B in dealer short-call exposure that needs **continuous
delta hedging** as spot moves.

If the public starts UNWINDING call positions (closing trades), dealer DEX
falls → dealer SELLS stock to unwind hedge → mechanical selling pressure.
This is the asymmetric risk in the current setup: the call buildup that
mechanically supports XOM today can mechanically pressure it tomorrow if
positioning unwinds.

### Vanna + charm

- **Net vanna:** -5,009,217 (call vanna -5,332,967, put vanna +323,750)
- **Net charm:** +104,396,975
- **Spot:** $160

Tool interpretation: "Public net vanna negative (call-heavy book). Falling IV
→ call delta drops → dealers (short calls) cut long-underlying hedge →
**SELLING pressure**. Rising IV reverses."

Given:
- IV term structure is in backwardation with May 22 IV at 40.8% (elevated)
- After May 22 OPEX, near-term IV will mechanically collapse as the front-end
  contract rolls off
- That IV decline → call delta drops → dealer unwinds long-underlying hedge
  → **mechanical selling into Friday's post-OPEX session**

This is the **vanna-bleed risk** for the bull case. Phase-9 must account for
**timing the entry around May 22 OPEX** — entering before OPEX exposes the
trade to potential post-OPEX vanna unwind.

### IV term structure

| Expiry | DTE | Avg IV | Avg IV % | Contract count |
|--------|-----|--------|----------|----------------|
| 2026-05-22 | 4 | 0.4083 | **40.8%** | 6,673 |
| 2026-05-29 | 11 | 0.3458 | 34.6% | 1,679 |
| 2026-06-05 | 18 | 0.3431 | 34.3% | 656 |
| 2026-06-12 | 25 | 0.3398 | 34.0% | 290 |
| 2026-06-18 | 31 | 0.3351 | 33.5% | 4,702 |
| 2026-06-26 | 39 | 0.3268 | 32.7% | 207 |
| 2026-07-17 | 60 | 0.3327 | 33.3% | 1,599 |
| 2026-08-21 | 95 | 0.3293 | 32.9% | 536 |
| 2026-09-18 | 123 | 0.3234 | 32.3% | 1,020 |
| 2026-10-16 | 151 | 0.3141 | 31.4% | 516 |
| 2026-11-20 | 186 | 0.3216 | 32.2% | 274 |
| 2026-12-18 | 214 | 0.3228 | 32.3% | 133 |
| 2027-01-15 | 242 | 0.3188 | 31.9% | 404 |
| 2027-03-19 | 305 | 0.3171 | 31.7% | 157 |
| 2027-06-17 | 395 | 0.3144 | 31.4% | 169 |
| 2027-12-17 | 578 | 0.3061 | 30.6% | 27 |
| 2028-01-21 | 613 | 0.3037 | 30.4% | 106 |
| 2028-12-15 | 941 | 0.3192 | 31.9% | 66 |

**Structure: BACKWARDATION** (front > back). No kink expiry detected.

The 4-DTE 40.8% vs 31-DTE 33.5% step is **7.3 IV points** — meaningful but
not earnings-level (earnings would typically show 10–15 points). XOM Q1 2026
earnings already reported (typical early May). The May 22 IV pop is most
likely:
1. OPEX-week mechanical IV from short-dated demand (the 6,673 contracts
   stamping the May 22 expiry — that's an outsized count vs neighbors)
2. Potential reaction to OPEC+ meeting / oil headlines / DoE data prints

Beyond the May-22 spike, the curve is well-behaved with mild backwardation
through Jun 26 then small contango back-end (LEAPs at 30.4–31.9%). Long-end
LEAP IV is the lowest at 2028-01-21 (30.37%) — the same expiry as the phase-1
2028 120P tail-hedge purchase. LEAPs trade at the cheap end of the curve.

### Term skew (30 DTE)

- **Put 25Δ IV:** 31.49%
- **Call 25Δ IV:** **32.86%**
- **Skew (call-put):** **-0.0137**
- **Skew ratio:** 0.958
- **Regime:** **COMPLACENT**

Calls trade at a 1.37-point IV premium to puts at 30 DTE. This is **inverted
skew** relative to the historical norm for energy single-names (which
typically trade put-skewed for tail-hedge demand). When skew inverts to call-
heavy:
- Bullish: confirms upside demand is mechanically pricing the curve
- Risk: a single negative catalyst can re-skew to puts FAST, with explosive
  put IV repricing
- **Often coincides with late-stage bull moves** (consider this a yellow flag,
  not a buy/sell signal)

### Front-end IV ratio

- **Near IV (10 DTE):** 34.58%
- **Far IV (30 DTE):** 33.51%
- **Ratio:** 1.032
- **Regime:** **FLAT** (just below the 1.05 backwardation threshold)

By the 7-day window, IV pop has already mostly normalized — the 40.8% spike
at the May 22 expiry is concentrated in the 4-DTE bucket and the smoother
near-IV measure (10 DTE) at 34.6% is barely above 30-DTE. **No persistent
event stress** in the 7-30 DTE window.

### Today's gamma flip (May 22 OPEX expiry slice)

- **ATM flip strike:** $152.5
- **OPEX ZGL:** $153.09
- **Spot (per tool):** $159.86
- **Today expiry total GEX:** +$9,198,075,939
- **Regime:** POSITIVE

Key walls (all support, all positive GEX):

| Strike | GEX | Distance from spot |
|--------|-----|--------------------|
| $160 | $4,099,261,006 | 0% |
| $165 | $2,488,025,711 | +3.2% |
| $162.5 | $1,061,438,241 | +1.7% |
| $157.5 | $911,422,514 | -1.5% |
| $155 | $507,281,772 | -3.0% |

Reading: into May 22 OPEX, the $160 strike acts as the dominant pin
(+$4.1B GEX vs second-place $2.5B at $165). Expect XOM to gravitate toward
$160 by Friday close. **$160 is the OPEX magnet.** Any move toward $157.5 or
$155 attracts dealer-bid; any move toward $162.5 or $165 attracts dealer-sell.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__options_structure_gex` | symbol=XOM, dte-max=45, date=2026-05-18 | Total GEX +$23.2B; ZGL $55.03; top strike $165 +$9.75B |
| `mcp__uw-pp__options_structure_dex` | symbol=XOM, dte-max=45, date=2026-05-18 | Net DEX +$315B (call-heavy public, dealer long underlying) |
| `mcp__uw-pp__options_structure_vanna_charm` | symbol=XOM, dte-max=45, date=2026-05-18 | Net vanna -5,009,217 (post-OPEX IV decline → mechanical sell) |
| `mcp__uw-pp__options_structure_iv_term_structure` | symbol=XOM, date=2026-05-18 | BACKWARDATION; May 22 40.8% → Jun 18 33.5%; 18 expiries |
| `mcp__uw-pp__options_structure_term_skew` | symbol=XOM, dte-target=30, date=2026-05-18 | COMPLACENT; call 32.86% > put 31.49%; skew_ratio 0.958 |
| `mcp__uw-pp__options_structure_front_end_iv_ratio` | symbol=XOM, near-dte=7, far-dte=30, date=2026-05-18 | FLAT; near 34.58% / far 33.51%; ratio 1.032 |
| `mcp__uw-pp__options_structure_today_gamma_flip` | symbol=XOM, date=2026-05-18 | ATM flip $152.5; OPEX ZGL $153.09; $160 = $4.1B support wall |

## Tool errors

None.

## Verdict for downstream phases

- **Dealer regime:** **STRONGLY POSITIVE GAMMA (long-gamma)** with massive
  call-heavy DEX. Mean-reversion environment in $152.5–$170 corridor.
  Reduced realized vol expected. **$165 is sticky resistance, not a breakout
  level**, because dealer hedging mechanics SELL into rallies toward strikes
  where they're long gamma.
- **Conviction:** **5/5.** The dealer mechanics are textbook clear and
  internally consistent with phase-3 OI flows. The Jun'26 165C +8,150 OI
  build (phase-3) maps directly to the +$9.75B GEX at $165 (phase-4) — same
  signal, different angle.
- **Three structural levels for phase-9:**
  1. **$153.09 (OPEX ZGL) / $152.5 (ATM flip)** — **the most important
     defensive level.** A break and HOLD below $152.5 flips dealer to
     short-gamma and unleashes the negative GEX zone at $150/$145/$140.
     Hard stop for any long trade.
  2. **$160 (current spot, $6.66B GEX)** — primary dealer support / OPEX
     magnet ($4.10B today_GEX). XOM should pin here into Friday May 22 OPEX.
  3. **$165 (largest single-strike GEX, $9.75B)** — sticky upside resistance.
     A move above $165 requires *sustained spot demand* to overcome dealer
     sell-hedge — phase-9 needs to size targets at $165 *with awareness* this
     is the mechanical ceiling, not a breakout level. Through $165, the next
     gamma cluster is $170 (+$1.39B) which is a much thinner wall — air
     pocket between $165 and $170 if the wall breaks.
- **Open questions:**
  - **Post-OPEX vanna unwind risk:** The May 22 40.8% IV collapse on
    Monday May 25 will lower call deltas and force dealer to sell ~$X of
    underlying. Phase-7 / phase-9 must model this — is the post-OPEX dip a
    BUY into the dealer support zone, or the start of a bigger unwind?
  - **Complacent call-skewed term structure:** What's the historical
    distribution of XOM call-skewed terminal periods? Phase 5 should pull
    historical IV percentile / VRP to determine whether 32.86% call-25Δ IV
    is a normal range or an extreme.
  - **The phase-1 LEAP 2028 120P buy is at the long-end IV minimum
    (30.4%) — the cheapest tail-hedge vol available on the curve.** This is
    a sophisticated buy: timing the lowest-IV expiry to lock in a long-dated
    tail. Likely an institutional structural hedge, not directional.
