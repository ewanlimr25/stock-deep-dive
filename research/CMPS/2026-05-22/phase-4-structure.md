# Phase 4 — Dealer Structure & Gamma

**Ticker:** CMPS
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T00:00:00Z
**Upstream phases cited:** phase-2-dark-pool.md, phase-3-positioning.md

## Summary

Dealers are **net long gamma (POSITIVE regime)** with spot ($11.85) sitting far above
the Zero-Gamma Level (**$9.02**), so the mechanical backdrop is **mean-reversion and
suppressed realized vol** — which justifies the cheap IV rank (12.25, phase-0.5). The
gamma map is dominated by a single enormous **$11 wall (+1,368,759 net GEX = 84% of
total)**, driven by the 10,553-contract Jun $11 call OI (phase-3); $12 is a secondary
wall (+216k). This is a **strong pin/magnet at $11 with $12 as the next shelf** — the
structural confirmation of phase-3's "willing-to-own at $11 / target $12" read and
phase-2's $11–$12 accumulation band. **DEX is positive (+10.8M)**: the public is net
call-long, dealers are short those calls, and their delta hedge is to **buy** underlying
— a structural bid that partly explains phase-2's dark-pool buying. Skew is **COMPLACENT**
(25Δ calls *richer* than puts — speculative upside demand, zero fear bid), and the term
structure is flat near-dated but bumps to **115.8% IV at Nov '26**, hinting at an
H2-2026 catalyst the front months don't price. Net: a **range-bound, dealer-pinned
$11–$12 structure** that needs a catalyst to break — no squeeze, no event stress now.

## Key signals

- **POSITIVE gamma regime**, ZGL **$9.02**, spot $11.85 (+31% above flip) → mean-reversion, vol suppression `[STRUCT:gex]`.
- **$11 gamma wall = +1,368,759 net GEX (84% of total $1.63M)** — dominant pin/magnet `[STRUCT:gex]`.
- **DEX +10,831,276** (call_dex +13.2M): dealers short calls → hedge by **buying** stock = supportive bid `[STRUCT:dex]`.
- **Skew COMPLACENT**: 25Δ call IV 80.3% > put IV 78.3% (ratio 0.975) — reverse skew, no downside fear `[STRUCT:term_skew]`.
- **Term structure FLAT** near-dated (no Jun kink) but **Nov '26 IV 115.8%** (highest) → possible H2-2026 catalyst window `[STRUCT:iv_term_structure]`.
- **No vanna squeeze**: net_vanna −986 (tiny, call-heavy book); falling IV → mild dealer-sell drift, not a squeeze `[STRUCT:vanna_charm]`.

## Detailed findings

### GEX — per strike + zero gamma `[STRUCT:gex]`

`total_gex +1,630,263 · regime POSITIVE · ZGL $9.02 · spot $11.85`

| strike | net_gex | note |
|--------|---------|------|
| **11** | **+1,368,759** | **dominant wall — 84% of total; the magnet** |
| 12 | +216,170 | secondary wall (Jul $12 call OI, phase-3 target) |
| 13 | +87,320 | minor shelf (overwrite ceiling, phase-1) |
| 15 | +50,636 | far OTM |
| 20 | +47,115 | far OTM odd-lot |
| 14 | +43,015 | — |
| 8 | +16,419 | — |
| **10** | **−193,035** | **negative pocket** — the bought Jun $10 puts (phase-3 hedge) |
| 9 | −13,056 | small negative |

Interpretation: positive gamma above ZGL means dealers **sell into rallies toward $12+
and buy dips toward $11** → the $11.85 spot is sandwiched and gravitates to the $11
wall. The −193k pocket at $10 (from the phase-3 long puts) is where dealer hedging would
*amplify* a move if spot broke below $10 toward the $9.02 ZGL — i.e. $10 is the trapdoor
edge, $9.02 is the regime flip into trend-amplifying short gamma.

### DEX — net dealer delta `[STRUCT:dex]`

`net_dex +10,831,276 · call_dex +13,229,911 · put_dex −2,398,636 · spot $11.85`

Public net call-long → dealers net **short** calls → dealer hedge = **BUY underlying**.
This is a standing mechanical bid beneath the stock and is consistent with phase-2's
DP `buy_ratio 0.839` (some of that buying is dealer delta hedging, not just directional
accumulation — de-rate phase-2's "conviction accumulation" slightly accordingly). The
bid strengthens as spot rises (call deltas grow) and fades on dips — pro-cyclical but
supportive at current levels.

### Vanna + charm `[STRUCT:vanna_charm]`

`net_vanna −986 · call_vanna −1,219 · put_vanna +233 · net_charm +7,889`

Negative net vanna (call-heavy book). Per the model: **falling IV → call deltas drop →
dealers trim their long hedge → mild SELLING pressure**; rising IV reverses. With IV
already at rank 12 (cheap) the vanna drift is a slight headwind, but the magnitude is
tiny — **this is not a vanna squeeze** (would need positive vanna + negative dealer delta
+ declining IV). No mechanical squeeze either direction.

### IV term structure `[STRUCT:iv_term_structure]`

`structure FLAT · kink_expiry null`

| expiry | avg IV | contracts |
|--------|--------|-----------|
| 2026-06-18 | 95.3% | 201 |
| 2026-07-17 | 103.6% | 359 |
| 2026-08-21 | 108.1% | 104 |
| **2026-11-20** | **115.8%** | 16 |
| 2027-01-15 | 93.0% | 58 |
| 2028-01-21 | 99.1% | 19 |

Mild **contango** Jun→Nov with the peak at **Nov '26 (115.8%)**, then dropping to 93%
by Jan '27. No kink/backwardation in the front → **no imminent (June) binary event is
vol-priced.** The Nov bump (on thin OI, 16 contracts — so soft) is the only hint of a
forward catalyst window; phase-6/7c should hunt an H2-2026 clinical/regulatory date. The
**low June IV (95%) means the phase-3 $10 put hedge is NOT priced as an imminent-event
hedge** — it reads as generic gain-protection after the +26% run.

### Term skew `[STRUCT:term_skew]`

`25Δ call IV 80.3% vs put IV 78.3% · skew −0.0203 · ratio 0.975 · COMPLACENT (23 DTE)`

**Reverse (call) skew** — calls richer than puts, the opposite of typical equity fear
skew. The market is paying up for *upside* lottery tickets and is **complacent on
downside**. Read two ways: (a) confirms no feared near-term catalyst; (b) complacency +
no protection bid means a downside surprise would be unhedged and could gap. The phase-3
$10 put buyer is hedging *against* this complacent crowd — mildly informative (a
sophisticated holder protecting the run while others chase calls).

### Front-end IV ratio `[STRUCT:front_end_iv_ratio]`

`ratio 1.0 · FLAT` (tool resolved both near/far to the 23-DTE Jun expiry given sparse
chains — low information; consistent with "no event stress").

### Today's gamma flip

**N/A** — `today_gamma_flip` is 0DTE intraday-only; this is an as-of historical run
(2026-05-22), after-hours. Skipped per phase guidance.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__options_structure_gex` | symbol=CMPS, dte_max=45 | POSITIVE, ZGL $9.02, $11 wall +1.37M (84%) |
| `mcp__uw-pp__options_structure_dex` | symbol=CMPS, dte_max=45 | net_dex +10.8M, dealers buy to hedge short calls |
| `mcp__uw-pp__options_structure_vanna_charm` | symbol=CMPS, dte_max=45 | net_vanna −986, no squeeze |
| `mcp__uw-pp__options_structure_iv_term_structure` | symbol=CMPS | FLAT, no kink; Nov '26 bump 115.8% |
| `mcp__uw-pp__options_structure_term_skew` | symbol=CMPS, dte_target=30 | COMPLACENT, calls richer (ratio 0.975) |
| `mcp__uw-pp__options_structure_front_end_iv_ratio` | symbol=CMPS, near=7, far=30 | FLAT, ratio 1.0 |

## Tool errors

_None._ (`today_gamma_flip` intentionally skipped — N/A after-hours.)

## Verdict for downstream phases

- **Dealer regime:** **POSITIVE / LONG GAMMA — strongly pinned**, spot $11.85 well above
  ZGL $9.02. Expect mean-reversion and suppressed realized vol; a directional breakout
  requires a catalyst to overpower the $11 gamma wall. Net mechanical lean is
  **range-bound $11–$12 with a mild upward DEX bid**, downside trapdoor only below $10→$9.02.
- **Conviction:** **4/5.** GEX/DEX signals are clean and the $11 wall is so dominant
  (84% of GEX) that the pin is high-confidence despite the standard low-liquidity caveat.
  De-rated from 5 only because part of the supportive bid is mechanical dealer hedging
  (not pure conviction accumulation) and the Nov-catalyst hint rests on thin OI.
- **Three structural levels for phase-9:**
  1. **$11 — dominant gamma magnet/pin** (+1.37M GEX). Strongest mean-reversion center;
     aligns with phase-3 "willing-to-own" line. Best long-entry zone on dips.
  2. **$12 — secondary gamma wall + supply** (+216k GEX, phase-2 $12.0–12.2 DP supply,
     phase-3 Jul $12 target). The realistic upside cap absent a catalyst.
  3. **ZGL $9.02 — regime-flip floor / hard invalidation.** $10 (−193k GEX pocket, phase-3
     put-hedge strike) is the trapdoor edge; a break of $10 toward $9.02 flips dealers
     short-gamma and turns mean-reversion into trend-amplification (downside accelerant).
- **Open questions for phases 5–7c:**
  - Does **historical** behavior (phase-5) confirm CMPS mean-reverts in positive-gamma
    regimes, or does it gap through walls on biotech headlines (which would neuter the pin)?
  - What **H2-2026 catalyst** lifts Nov IV to 115.8%? (phase-6 calendar / phase-7c news) —
    decisive for whether the range breaks up (data win) or the $10 hedge pays (data miss).
  - Is the COMPLACENT skew a contrarian warning (unhedged downside) given a binary-event
    name? Phase-7b cash-runway + phase-7c short-interest/sentiment should stress-test it.
