# Phase 4 — Dealer Structure & Gamma

**Ticker:** BABA
**As-of date:** 2026-05-27
**Generated:** 2026-05-28T03:25:00Z
**Upstream phases cited:** phase-0.5-context.md, phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md

## Summary

Dealer positioning is **net long-gamma and vol-suppressing** — spot $127.74 sits
far **above** the Zero Gamma Level **$91.35** with total GEX **+$3.85M**
`[STRUCT:gex]`. That regime (dealers sell rallies, buy dips) explains phase-0.5's
orderly ~12% grind down and the IV-rank collapse (83→21) — this has been a
*controlled* distribution, not a panic. Two structural cautions sit underneath:
(1) a **negative-GEX pocket at $100–113 (largest −949k at C110)** — a break below
~$113 flips local dealer gamma negative and would **accelerate** the move
`[STRUCT:gex]`; and (2) the 25Δ skew is **COMPLACENT** (puts *cheaper* than calls,
ratio 0.977) — the market is **not** paying for downside protection
`[STRUCT:term_skew]`. DEX is negative (public net put-long → dealers sell
underlying) `[STRUCT:dex]`, but positive vanna + crushed IV sets up a latent
**vanna-squeeze BUY** if IV falls further `[STRUCT:vanna_charm]`. IV term is in
mild **BACKWARDATION** (ratio 1.1) despite earnings being far out (2026-09-04) —
modest near-term stress for phase-6 to source `[STRUCT:front_end_iv_ratio]`.

## Key signals

- **Long-gamma regime:** spot $127.74 ≫ ZGL $91.35, total GEX +$3.85M → vol
  suppression / mean-reversion `[STRUCT:gex]`.
- **Negative-GEX acceleration pocket $100–113** (C110 −949k, C100 −219k) — break
  <$113 = short-gamma, vol expands `[STRUCT:gex]`.
- **DEX −$669M** (public put-long, dealers net short puts → hedge = sell
  underlying) `[STRUCT:dex]`.
- **Vanna-squeeze BUY latent:** net vanna +7,748, falling IV → short-put dealers
  cover by **buying** underlying `[STRUCT:vanna_charm]`.
- **Skew COMPLACENT** (25Δ put IV 0.398 < call IV 0.408, ratio 0.977) + IV term
  **BACKWARDATION** (near 9DTE 0.452 > far 30DTE 0.411) `[STRUCT:term_skew]`
  `[STRUCT:iv_term_structure]`.

## Detailed findings

### GEX `[STRUCT:gex]`

- **Total GEX +$3,853,871; ZGL $91.35; spot $127.74.** Spot ~40% above ZGL →
  firmly long-gamma. Dealers dampen moves both ways near spot.
- **Per-strike:** large **negative** net_gex below spot — C110 **−949,041**,
  C100 −218,949, C95 −56,387, C105 −30,675 — i.e. a short-gamma shelf at
  $100–113. Above spot net_gex turns positive (long gamma), reinforcing the
  $129–131 supply node (phase-2) as a sticky cap (dealers long the overwritten
  C130–135, sell into strength). Caveat: tool notes GEX is "most meaningful for
  index products"; treat single-name ZGL as a ±2% band.

### DEX `[STRUCT:dex]`

- **net_dex −$668,938,213** (call_dex +$571M). Interpretation (tool): "Public is
  net put-long → dealers net short puts → dealer hedge is to SELL underlying."
  Structural mild downward hedge pressure, but muted while long-gamma holds.
  Reconciles with phase-1 (OI book put-long even though *today's* put flow was
  net-sold = closing some longs).

### Vanna + charm `[STRUCT:vanna_charm]`

- net_vanna **+7,748** (put-heavy book), net_charm +259,676. Tool: "Falling IV →
  |put delta| drops → dealers (short puts) cover by BUYING underlying. Classic
  vanna-squeeze setup if VIX collapses." With IV rank already at 21 and falling,
  this is a **latent mechanical bid** — a mild bullish counterweight to the
  bearish flow.

### IV term structure & front-end ratio `[STRUCT:iv_term_structure]` `[STRUCT:front_end_iv_ratio]`

- **BACKWARDATION.** Near (9DTE) IV 0.4524 > far (30DTE) IV 0.4114, ratio **1.1**.
  Backwardation usually signals an event; BABA earnings are **2026-09-04** (far),
  so the near-term stress is likely macro (China / tariff / early-June data) or
  residual downtrend realized vol — **phase-6 must source it**. (Row-level
  `term_structure` returned null dte/iv; regime field is authoritative.)

### Term skew `[STRUCT:term_skew]`

- **COMPLACENT.** 25Δ put IV **0.3982** < 25Δ call IV **0.4077**, skew −0.0096,
  ratio **0.977**. Puts trade *below* calls — unusual for equity and notable
  *into a downtrend*. Read: no downside fear is priced; the flow (LEAP/upside call
  bids + put selling, phase-1) created a call-rich vol surface. **Cheap puts** =
  attractive cost for bearish/protective structures; also a **yellow flag** —
  an unhedged, complacent market gaps harder on a negative shock.

### Today's gamma flip

- **Skipped** — `today-gamma-flip` is 0DTE/intraday and the run is EOD as-of
  (2026-05-27). Not meaningful after the close.

## Tool calls (audit trail)

| Command | Result summary |
|---------|----------------|
| `uw options-structure gex --symbol BABA --dte-max 45` | +$3.85M, ZGL $91.35, neg pocket $100–113 |
| `uw options-structure dex --symbol BABA --dte-max 45` | −$669M, public put-long |
| `uw options-structure vanna-charm --symbol BABA --dte-max 45` | +vanna, latent squeeze-buy |
| `uw options-structure iv-term-structure --symbol BABA` | BACKWARDATION |
| `uw options-structure term-skew --symbol BABA --dte-target 30` | COMPLACENT, ratio 0.977 |
| `uw options-structure front-end-iv-ratio --symbol BABA` | ratio 1.1, backwardation |
| `uw options-structure today-gamma-flip` | skipped (EOD / 0DTE-only) |

## Tool errors

- `iv-term-structure` `term_structure[]` rows returned null `dte`/`iv`; the
  `structure` regime field (BACKWARDATION) is used and corroborated by
  `front-end-iv-ratio` (ratio 1.1). `gex` `per_strike` truncated in capture but
  the negative cluster $95–113 and total/ZGL are confirmed.

## Verdict for downstream

- **Dealer regime:** **LONG GAMMA** (spot ≫ ZGL) — vol-suppressing,
  mean-reverting, dip-buying. This is the dominant structural fact and it argues
  for a **contained range** absent a catalyst. Mildly **supportive** via the
  latent vanna-squeeze bid.
- **Conviction:** **3 / 5.** The long-gamma / skew / backwardation reads are
  clean and consistent even though the name had a light flow day.
- **Three structural levels for phase-9:**
  1. **ZGL $91.35** — long-gamma anchor (far below; regime intact unless price
     collapses).
  2. **$110–113 negative-GEX pocket** — the **acceleration trapdoor**: a break
     below flips local dealer gamma short and expands downside vol (aligns with
     P110 Mar-2027 hedge, phase-3).
  3. **$129–131 long-gamma + supply node** — sticky **cap** (dealers long the
     overwritten C130–135; sell strength) — reclaim level for any long.
- **Open questions:** What near-term catalyst is the **backwardation** pricing
  (no earnings until Sept)? — phase-6. Is the **complacent skew** an
  opportunity (cheap puts for a trend-continuation short) or a contrarian buy
  signal (no fear = bottoming)? — phase-5/8 to weigh.
