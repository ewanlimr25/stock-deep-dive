# Phase 3 — Open Interest & Positioning

**Ticker:** NBIS (Nebius Group NV)
**As-of date:** 2026-06-17
**Generated:** 2026-06-18T00:35:43Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md, phase-1-flow.md, phase-2-dark-pool.md

## Summary

Positioning is **bullish-leaning, barbelled**, and it RE-CONFIRMS phase-1's directional read once you
read the put builds correctly. The structural book is unambiguously bullish: long-dated call OI
dominates (**2027-01 P/C 0.69 holding 20.1% of all OI; 2028-01 P/C 0.06; 2028-12 P/C 0.07** — the
$410/$350/$180 LEAP calls from phase-1). Today's *incremental* OI is also **net bullish ~1.6:1**
(bullish Δoi 23,148 vs bearish 14,351): although the biggest builds are PUTS, the largest by far —
**$200 July-2 put, +13,047 OI, vol 17,524 — is inferred put SELLING (bullish income at 28% OTM in
113% IV)**, not put buying. A smaller, genuine tail-hedge layer is being bought ($172.5/$190/$225/$180
puts ≈ 11k contracts). Wall map: nearest resistance is the **$300 call wall (+6.9%)** then **$350
(+24.7%)**, with little near-term call resistance between spot and $300; support is diffuse (the heavy
put strikes $200/$220 are deep tail levels, not near-spot). No clean pin (NBIS absent from the
market-wide pin-risk top-25). This bullish-lean **partially offsets** phase-2's mega-tier distribution.

## Key signals

- **Structural bull book:** 2027-01 call OI 102,007 (P/C 0.69, 20.1% of total); 2028-01 call OI 43,582
  (P/C 0.06). Long-dated positioning is heavily call-side. [OI:term_structure]
- **Net new OI is 1.6:1 bullish** (Δoi bull 23,148 vs bear 14,351 across top-20). [OI:smart_positioning]
- **Largest single build = $200 Jul-2 PUT +13,047, inferred BULLISH (sold)** — premium underwriting,
  not a hedge. [OI:biggest_increases + smart_positioning]
- **Nearest call wall $300 (+6.9%), then $350 (+24.7%)**; clear-ish runway from spot to $300. [OI:oi_by_strike]
- **OPEX cliff 2026-06-18 (dte 1) = 26.7% of OI, P/C 1.40**, but no pin (high-OI strikes are deep puts far from spot). [OI:term_structure / pin_risk]

## Detailed findings

### OI walls by strike (spot $280.71) [OI:oi_by_strike]

**All-expiry aggregate:**

| Strike | call_oi | put_oi | net_oi | role | dist |
|--------|---------|--------|--------|------|------|
| $350 | 35,418 | 942 | +34,476 | call_wall_resistance | +24.7% |
| $300 | 28,924 | 662 | +28,262 | **call_wall_resistance (nearest above)** | +6.9% |
| $250 | 26,305 | 9,203 | +17,102 | call_heavy | −10.9% |
| $240 | 18,257 | 7,574 | +10,683 | call_heavy | −14.5% |
| $200 | 33,770 | 41,461 | −7,691 | put_wall_support | −28.8% |
| $180 | 10,924 | 21,679 | −10,755 | put_wall_support | −35.9% |

**Near-term (DTE ≤ 30):** dominated by put_wall_support strikes far below spot ($200 net −22,600, $180
−14,252, $175 −11,432, $190 −9,472); the only call wall is $350 (+24.7%). **There is no near-term call
wall between spot $280 and $350** — overhead is light near-term; the $300 wall is a farther-dated level.

### OI term structure — OPEX cliffs (total OI 858,500, 16 expiries) [OI:term_structure]

| Expiry | DTE | call_oi | put_oi | P/C | % of total OI |
|--------|-----|---------|--------|-----|---------------|
| **2026-06-18** | 1 | 95,478 | 133,555 | 1.40 | **26.7%** (near gravity, put-heavy) |
| **2027-01-15** | 212 | 102,007 | 70,265 | 0.69 | **20.1%** (LEAP bull cliff) |
| 2026-07-17 | 30 | 39,050 | 50,974 | 1.31 | 10.5% (July monthly, put-heavy) |
| 2026-06-26 | 9 | 28,666 | 44,276 | 1.55 | 8.5% (put-heavy) |
| 2026-09-18 | 93 | 31,143 | 26,364 | 0.85 | 6.7% (call-lean) |
| 2028-01-21 | 583 | 43,582 | 2,732 | **0.06** | 5.4% (almost all calls — $410 LEAPs) |
| 2026-07-02 | 15 | 5,375 | 30,088 | **5.6** | 4.1% (extreme put-heavy — tail cluster) |

**The barbell is explicit:** near-dated expiries are put-heavy (06-18 1.40, 06-26 1.55, 07-02 5.6,
07-17 1.31) while long-dated are call-heavy (2027-01 0.69, 2028-01 0.06, 2028-12 0.07). Matches
phase-1: LEAP-call bull bets + near-term put activity (mostly written, partly hedges).

### Largest OI increases TODAY (OPRA-parsed) [OI:biggest_increases]

| Contract | Type/Strike/Exp | Δoi | vol | inferred dir |
|----------|------------------|-----|-----|--------------|
| NBIS260702P00200000 | $200 P 07-02 | **+13,047** | 17,524 | **bullish (sold)** |
| NBIS260618P00172500 | $172.5 P 06-18 | +3,500 | 3,603 | bearish (bought, tail) |
| NBIS260626P00190000 | $190 P 06-26 | +2,251 | 2,725 | bearish (bought) |
| NBIS260710P00200000 | $200 P 07-10 | +1,866 | 2,513 | bullish (sold) |
| NBIS260626P00225000 | $225 P 06-26 | +1,536 | 2,332 | bearish (bought) |
| NBIS260918P00250000 | $250 P 09-18 | +1,301 | 1,374 | bullish (sold) |
| NBIS260717C00380000 | $380 **C** 07-17 | +987 | 1,041 | (lone OTM call build, +35%) |

Net across top-20: **bullish Δoi 23,148 vs bearish Δoi 14,351 (≈1.6:1 bullish)**. The headline
"puts being built" is misleading — the dominant build is put *writing* (bullish income), with a
smaller genuine tail-hedge layer ($172.5/$190/$225 puts bought).

### Closing / roll activity [OI:decrease_with_volume / position_rolls]

Decreases are concentrated in **06-18 expiry** contracts being closed ahead of tomorrow's expiry
(natural): $225C −1,789, $175P −1,342, $210P −953, $280C −654, $195P −633, $280P −628. Nothing
structural. **position-rolls: 0 detected** (single-day window; cross-session rolls not captured).

### Smart positioning (inferred direction) [OI:smart_positioning]

Inference is from prior ask/bid volume (heuristic). Across the put builds, SELLING (bullish) ≈ 19.8k
contracts vs BUYING (bearish) ≈ 10.9k — net bullish via underwriting. Treat as directional color,
not certainty (OPRA-symbol-parsed; spot-checked $200P 07-02 = deep-OTM put, plausible income write).

### Pin risk & OPEX concentration [OI:pin_risk / opex_concentration]

**NBIS is NOT in the market-wide pin-risk top-25** (dominated by SPY/QQQ/NVDA/AAPL/TSLA/PLTR/NU). The
06-18 expiry holds 26.7% of OI but its high-OI strikes are deep puts ($200) far from spot $280, so
there is no pin gravity near the money. **NBIS absent from opex-concentration top-20** (no single
strike ≥40%). → No pin commentary for phase-9; spot can move freely into 06-18 expiry.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← path | Rows |
|------------------|--------------------|------|
| `uw oi oi-by-strike --symbol NBIS --top-n 10 --date 2026-06-17` | $300 call wall +6.9%, $350 +24.7%, $200 put wall −28.8% ← `.results[].role/net_oi` | 10 |
| `uw oi oi-by-strike --symbol NBIS --dte-max 30 …` | near-term: all put walls below; only $350 call wall ← `.results` | 10 |
| `uw oi term-structure --symbol NBIS --date 2026-06-17` | 06-18 26.7% P/C1.40; 2027-01 20.1% P/C0.69; 2028-01 P/C0.06 ← `.term_structure[]` | 16 |
| `uw oi biggest-increases --symbol NBIS --top-n 20 --min-oi-change 500` | $200P 07-02 +13,047 vol 17,524 ← `.results[].oi_diff_plain` | 20 |
| `uw oi smart-positioning --symbol NBIS --top-n 20 --min-oi-change 500` | net bull Δoi 23,148 vs bear 14,351 ← `.inferred_direction`+`.oi_diff_plain` | 20 |
| `uw oi decrease-with-volume --symbol NBIS --top-n 15 --min-volume 100` | 06-18 closes (natural pre-expiry) ← `.results` | 15 |
| `uw oi position-rolls --symbol NBIS --threshold 500 --near-dte-max 30` | rolls_detected 0 ← `.rolls_detected` | 0 |
| `uw oi pin-risk --top-n 25 --dte-max 7 --max-distance-pct 5` | NBIS absent ← `.results[]\|select NBIS` | 25 |
| `uw oi opex-concentration --top-n 20 --min-concentration-pct 40` | NBIS absent ← `.results[]` | 20 |
| `fz` float (phase-0) | largest build 0.65% float; total OI 42.5% float ← computed | — |

## Tool errors

None.

## DATA NOTE / CORRECTION

Initial naive read ("today's OI builds are overwhelmingly puts → defensive/hedging") was CORRECTED by
the `smart-positioning` directional inference: the largest put build ($200 Jul-2, +13,047) and most of
the put OI added is put *selling* (inferred bullish income), not buying. Net incremental OI is 1.6:1
bullish. No transcribed number changed; the directional interpretation was revised against the
`inferred_direction` field. Reliability caveat: inference is ask/bid-volume heuristic, flagged as color.

## Verdict for downstream phases

- **Positioning bias:** **bullish-leaning** — structural LEAP-call book (2027/2028) + net-bullish
  incremental OI (1.6:1) driven by put underwriting; smaller genuine tail-hedge layer underneath.
- **Conviction:** **3/5.** Confirms phase-1 direction, but the bullishness is income/structural
  (put-writing in rich IV + slow LEAP calls), not aggressive fresh call buying — and IV rank 91 means
  put-writing is partly just premium harvesting. Tempered by phase-2 distribution.
- **Largest OI build as % of float (advisory):** $200P 07-02 build of 13,047 contracts ≈ **0.65% of the
  202M float** (share-equivalent) — a moderate, structural-ish position, not float-dominating. Total OI
  ≈ 42.5% of float (options-heavy name). [OI:oi_pct_float fz]
- **Three pin/cliff strikes for phase-9 (sourced from roles + term-structure):**
  1. **$300 call_wall_resistance (+6.9%)** — nearest overhead magnet/target; little call resistance below it.
  2. **$350 call_wall_resistance (+24.7%)** — the big upside cap (where 2028 LEAP calls + call OI sit).
  3. **$200 put_wall_support / $250 call_heavy (−28.8% / −10.9%)** — downside reference; the $200 put
     wall is where the big written-put OI sits (a soft floor as writers defend), $250/$240 are prior-OI shelves.
- **Open questions:** Is the bullish LEAP-call book a leveraged bet or stock→call rotation paired with
  phase-2's mega-tier stock selling? Does dealer gamma pin or accelerate around spot (phase-4 GEX/max-pain)?
  Will the rich IV (rank 91) being harvested via put-writing collapse post-OPEX (phase-4 term-skew/VRP)?
