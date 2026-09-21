# Phase 4 — Dealer Structure & Gamma

**Ticker:** NBIS
**As-of date:** 2026-06-05
**Generated:** 2026-06-06T20:30:00-0400
**Upstream phases cited:** phase-1-flow.md, phase-3-positioning.md

## Summary

Dealers are **short gamma at every strike**: `regime = "FULLY_NEGATIVE"` ("All
strikes have negative net GEX — strong gamma amplification"), total_gex
**−$12,546,295**, zero_gamma_level **null** (no flip — the book never goes
positive within 45 DTE). The largest negative-GEX node sits **right at spot**
(227.5: −$2.93M; spot 227.19), with secondary nodes at 205 / 220 / 225 — moves
through these get amplified, not absorbed. The front of the vol surface is
stressed: near/far IV ratio **1.187 = BACKWARDATION** (6-DTE 132.1% vs 34-DTE
111.3%) with a **hump at Jun-18 (143.6%)** — the market is paying up for
something inside OPEX week. Skew is **inverted/"COMPLACENT"**: 25Δ calls
(114.9%) trade *over* 25Δ puts (111.5%, skew_ratio 0.97) — upside-grab premium
on a 22%-short-float name, matching phase-1's call-side LEAP demand. Max-pain
magnets: Jun-12 **235** (+3.2% above spot), Jun-26 **230** (+1.0%); the Jun-18
figure (175, −23%) is a put-OI-distorted soft magnet (static-OI caveat).

## Key signals

- GEX `regime: FULLY_NEGATIVE`, total_gex −$12.55M, ZGL null; node at 227.5
  −$2.93M (at spot) `[STRUCT:gex]`
- DEX: call_dex +$1.963bn vs put_dex −$1.359bn → net_dex **+$604.0M**;
  tool interpretation verbatim: "Public is net call-long → dealers net short
  calls → dealer hedge is to BUY underlying." `[STRUCT:dex]`
- Vanna: net −1,729 (call-driven; "Falling IV → call delta drops → dealers cut
  long-underlying hedge → SELLING pressure. Rising IV reverses."); net charm
  −61,059 — decay-driven hedge selling into expiry `[STRUCT:vanna_charm]`
- Front-end stress: near_iv (6 DTE) **1.3214** vs far_iv (34 DTE) 1.1133 →
  ratio **1.187, regime BACKWARDATION** `[STRUCT:front_end_iv_ratio]`; surface
  hump at Jun-18: **143.6%** avg IV `[STRUCT:iv_term_structure]`
- Skew: 25Δ call 1.1491 > 25Δ put 1.1148, skew −0.0343, skew_ratio 0.97,
  `interpretation: "COMPLACENT"` — calls richer than puts `[STRUCT:term_skew]`
- Max pain: Jun-12 **235** (dist +3.19%, P/C OI 2.996), Jun-26 **230** (+1.0%),
  Jun-18 175 (−23.2%, soft — see findings) `[STRUCT:max_pain]`

## Detailed findings

### GEX `[STRUCT:gex]` (dte_max 45, underlying 227.19)

- `regime`: **FULLY_NEGATIVE** — `regime_description`: "All strikes have
  negative net GEX — strong gamma amplification"
- `total_gex`: **−12,546,295** · `zero_gamma_level`: **null** (no positive
  territory to flip into)
- Top per-strike nodes (|net_gex|):

| Strike | net_gex | Note |
|---|---|---|
| 227.5 | −2,932,765 | at spot — max amplification at current price |
| 205 | −2,449,788 | phase-3's fresh put shelf |
| 220 | −1,668,326 | phase-3 nearest put wall / phase-2 AH low |
| 225 | −1,374,281 | |
| 232.5 / 210 / 202.5 / 222.5 | −0.88M…−0.76M | |
| 200 | −680,759 | |

(One negligible positive row exists at strike 165: +15,454 — ~0.1% of the
largest node; does not alter the regime label.)

Interpretation per heuristics: spot below any positive-gamma territory →
**dealers sell dips / buy rallies is OFF; they chase** — realized vol expands,
trends extend. Friday's 240→217→228 violence (phase-1/phase-2) is consistent
with this regime, not an anomaly.

### DEX `[STRUCT:dex]` (dte_max 45, spot 227.19)

call_dex +1,963,141,401 · put_dex −1,359,163,472 · **net_dex +603,977,929**.
Tool note: sign reflects *public* positioning; dealer hedge is the inverse —
dealers are net short ~$604M delta-equivalent and hold long-stock hedges
against short calls. Mechanical consequence (with vanna below): **an IV crush
or call-OI decay forces dealers to SELL their hedge** — the book's mechanical
flows currently point down on vol-normalization, up only on rising IV.

### Vanna + charm `[STRUCT:vanna_charm]` (dte_max 45, spot 226.96)

- call_vanna −3,432, put_vanna +1,703 → **net_vanna −1,729**
- `vanna_interpretation` (verbatim): "Public net vanna negative (call-heavy
  book). Falling IV → call delta drops → dealers (short calls) cut
  long-underlying hedge → SELLING pressure. Rising IV reverses."
- net_charm −61,059: time decay alone bleeds call deltas → daily dealer hedge
  selling into Jun-18 OPEX, all else equal.
- **No vanna-squeeze setup**: the squeeze recipe (positive vanna + negative
  dealer delta + declining IV) is not present — the signs run the other way.

### IV term structure `[STRUCT:iv_term_structure]`

`structure: "CONTANGO"` (tool label, quoted verbatim — but see Tool errors/DATA
NOTE: the label is distorted by the expired 0DTE row at 14.9%).

| Expiry | DTE | avg IV |
|---|---|---|
| 2026-06-05 | 0 (expired) | 14.9% (artifact) |
| 2026-06-12 | 6 | 132.1% |
| **2026-06-18** | 12 | **143.6% ← hump** |
| 2026-06-26 | 20 | 116.3% |
| 2026-07-02 | 26 | 113.5% |
| 2026-07-10 → 07-24 | 34–48 | 111.2–113.8% |

The tradeable front (ex-0DTE) is **downward-sloping from Jun-18 out** — an
event/stress kink concentrated on OPEX week, not a calm contango.

### Term skew `[STRUCT:term_skew]` (dte_target 30 → actual 34)

25Δ call IV 1.1491 vs 25Δ put IV 1.1148 → skew −0.0343, skew_ratio 0.97,
`interpretation: "COMPLACENT"`. After a −9% intraday flush, puts trading
*under* calls is striking: no tail-hedge panic; the chain prices
upside-chase (squeeze) risk over downside continuation. Cross-ref phase-7c
short-float gate (22.43%, phase-0).

### Front-end IV ratio `[STRUCT:front_end_iv_ratio]`

near (6-DTE actual) 1.3214 / far (34-DTE actual) 1.1133 = **1.187 →
"BACKWARDATION"** — event stress inside the next two weeks. No earnings until
2026-08-06 (phase-0.5), so the stress is news-flow-driven (phase-6 must name
the catalyst).

### Today's gamma flip

Skipped — `today-gamma-flip` is 0DTE-intraday only and this is a post-close
as-of run (phase-0). Noted per phase guidance.

### Max pain `[STRUCT:max_pain]` (dte_max 30, spot 227.73; static-OI caveat quoted)

| Expiry | DTE | Max-pain strike | dist% | P/C OI | Total OI |
|---|---|---|---|---|---|
| 2026-06-05 | 0 | 265 | +16.4% | 3.199 | 170,491 (expired; settled FAR below pain — put holders paid) |
| **2026-06-12** | 7 | **235** | **+3.19%** | 2.996 | 64,945 |
| 2026-06-18 | 13 | 175 | −23.2% | 1.358 | 172,474 |
| 2026-06-26 | 21 | 230 | +1.0% | 1.437 | 17,058 |
| 2026-07-02 | 27 | 250 | +9.8% | 3.345 | 7,565 |

Tool caveat (verbatim): "Max pain assumes settlement at each candidate strike
with current open interest unchanged to expiry." The tradeable magnets are
**Jun-12 @ 235** and **Jun-26 @ 230** — both *above* spot, a mild mean-reversion
pull upward into next week. The Jun-18 175 print is mathematically real but
soft: 13 DTE out on the chain's biggest expiry (20.9% of OI, phase-3), heavily
distorted by deep-OTM put strata (170/150 walls); treat as indicative of
downside-tail gravity only if 200–205 breaks. Cross-check vs phase-3: Jun-12
max-pain 235 sits between the 220 put wall and 250 call wall — coherent.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw options-structure gex --symbol NBIS --dte-max 45 --date 2026-06-05 --json` | regime FULLY_NEGATIVE; total_gex −12,546,295; ZGL null ← `.regime/.total_gex/.zero_gamma_level`; nodes ← `.per_strike \| sort_by(-(.net_gex\|fabs))` | full surface |
| `uw options-structure dex --symbol NBIS --dte-max 45 --date 2026-06-05 --json` | net_dex 603,977,929 ← `.net_dex`; interpretation verbatim | aggregate |
| `uw options-structure vanna-charm --symbol NBIS --dte-max 45 --date 2026-06-05 --json` | net_vanna −1,729; net_charm −61,059 ← `.net_vanna/.net_charm` | aggregate |
| `uw options-structure iv-term-structure --symbol NBIS --date 2026-06-05 --json` | structure "CONTANGO"; Jun-18 1.4359 ← `.structure/.term_structure[].avg_iv` | 8 expiries read |
| `uw options-structure term-skew --symbol NBIS --dte-target 30 --date 2026-06-05 --json` | skew_ratio 0.97 "COMPLACENT" ← `.skew_ratio/.interpretation` | 1 |
| `uw options-structure front-end-iv-ratio --symbol NBIS --near-dte 7 --far-dte 30 --date 2026-06-05 --json` | ratio 1.187 "BACKWARDATION" ← `.ratio/.regime` | 1 |
| `uw options-structure max-pain --symbol NBIS --dte-max 30 --date 2026-06-05 --json` | Jun-12 235 (+3.19%); Jun-26 230 ← `.results[].{max_pain_strike,distance_pct}` | 5 expiries |

## Tool errors

- First GEX jq pass (`sort_by(-(.gex|fabs))`) → `jq: error … null (null) number
  required`: wrong field name (`gex` vs actual `net_gex`) plus a null row.
  Schema inspected, re-ran with `.net_gex`-based null-safe filter. No values
  transcribed from the failed parse.

## DATA NOTE / CORRECTION

- `iv-term-structure` labels the surface **CONTANGO** while
  `front-end-iv-ratio` reports **BACKWARDATION** (1.187). The contango label is
  polluted by the expired Jun-05 row (avg_iv 14.9%, dte −1 — an EOD artifact).
  Both labels are quoted verbatim per guidance; the row-level data (132% → 143.6%
  → 111–116%) supports the backwardation/event-stress read. Downstream phases
  should use BACKWARDATION.

## Verdict for downstream phases

- **Dealer regime:** **short gamma, fully negative** — trend amplification both
  directions; no ZGL to mean-revert around.
- **Conviction:** 4/5 (regime is unambiguous; directional implication is
  conditional, not directional per se)
- **Three structural levels for phase-9 (+ opex magnet):**
  1. **227.5** — the largest negative-GEX node, at spot: expect violent travel
     away from here, either direction.
  2. **220 → 205/202.5 → 200** — descending negative-GEX nodes aligned with
     phase-3 put walls: breakdown path accelerates through these.
  3. **232.5** then phase-3's 250 call wall — upside amplification nodes; a
     squeeze through 232.5 runs into thin GEX until 250.
  4. **Max-pain magnet: Jun-12 @ 235 (+3.2%), Jun-26 @ 230 (+1.0%)** — static-OI
     pull mildly *up* into next week's expiries.
- **Open questions:** What event is the Jun-18 143.6% IV hump pricing (phase-6)?
  Does historical behavior show this name trending or mean-reverting after
  short-gamma flush days (phase-5)? With calls richer than puts, is a
  short-squeeze the asymmetric tail (phase-7c short-interest gate)?
