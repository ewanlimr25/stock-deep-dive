# Phase 3 — Open Interest & Positioning

**Ticker:** GOOG · **As-of:** 2026-07-23 · **Spot:** $318.34
**Generated:** 2026-07-24T01:18:35Z
**Upstream:** phase-1-flow.md (net bearish, top-25 prints 100% puts; open Q: "fresh
directional shorting or writing/rolling?"), phase-2-dark-pool.md (balanced tiers,
overhead $341–351 supply, S/R 341-346 / 318 / <318)

## Summary

Open interest resolves phase-1's open question toward **not-a-clean-short**:
positioning is **genuinely two-sided and hedge-heavy**, not a one-way bearish
build. The two largest OI increases are far-dated Oct-16 calls — 365C (+11,070,
inferred *bullish*/bought) and 415C (+11,004, inferred *bearish*/written) — i.e. a
bullish accumulation and a call-write printing side by side. The broad put ladder
(295/300/305/310/330/340 across Aug–Oct) is likewise split: 295P/310P/300P infer
*bullish* (put **writing**/income), while 330P infers *bearish* (put buying).
Closing activity is concentrated in Aug-21 **upside calls** (430C −4,341, 410C
−3,408, 450C −3,354) being taken off. Net: the bearish *premium* skew from phase-1
is real, but a large share of it is put **selling**, not directional shorting — so
the OI book does **not** ratify a high-conviction short. The structural value here
is the wall map: dense put OI at 330/320/310/300, call resistance at 350–400.

## Key signals

- **Two largest builds are Oct-16 calls, opposite inferred sides:** 365C +11,070
  (bullish) vs 415C +11,004 (bearish/written). `[OI:smart_positioning]`
- **Put-ladder build is partly writing (bullish-inferred):** 295P +5,387, 310P
  +4,008, 300P +3,260 all infer bullish (bid-side put sells). `[OI:smart_positioning]`
- **Nearest-monthly upside calls being closed:** Aug-21 430C/410C/450C down
  −4.3k/−3.4k/−3.4k — upside exposure coming off. `[OI:decrease_with_volume]`
- **OPEX gravity well = Sep-18 (18.1% of total OI**, P/C 1.07); nearest monthly
  Aug-21 (13.5%, P/C 1.04, where phase-1 put sweeps sit). `[OI:term_structure]`
- **Wall map (dte≤30):** put_heavy 330 (net_oi −15,593), put_wall_support 310
  (−11,210) & 300 (−9,905); call_wall_resistance 350/360/370/380/400.
  `[OI:oi_by_strike]`

## Detailed findings

### OI walls by strike (dte ≤ 30; spot 318.34) — `[OI:oi_by_strike]`
| Strike | call_oi | put_oi | net_oi | role | dist |
|---|---|---|---|---|---|
| 300 | 861 | 10,766 | −9,905 | **put_wall_support** | −5.8% |
| 310 | 142 | 11,352 | −11,210 | **put_wall_support** | −2.6% |
| 320 | 1,191 | 10,364 | −9,173 | put_heavy | +0.5% |
| 330 | 1,335 | 16,928 | **−15,593** | put_heavy | +3.7% |
| 345 | 4,694 | 6,993 | −2,299 | put_heavy | +8.4% |
| 350 | 13,799 | 15,025 | −1,226 | put_heavy (2-sided) | +10% |
| 360 | 13,259 | 4,779 | +8,480 | call_wall_resistance | +13.1% |
| 370 | 19,062 | 1,959 | +17,103 | call_wall_resistance | +16.2% |
| 380 | 19,328 | 11,876 | +7,452 | call_wall_resistance | +19.4% |
| 400 | 24,219 | 1,698 | +22,521 | call_wall_resistance | +25.7% |

All-expiry: biggest call wall **350** (call_oi 45,361) and **400** (62,733);
biggest put concentration **330** (put_oi 54,968) and **300** (put_wall_support,
38,749). The 330 strike is the heaviest near-spot magnet.

### OI term structure (OPEX cliffs) — `[OI:term_structure]` (total OI 1,262,884)
| Expiry | DTE | call_oi | put_oi | P/C | % of total |
|---|---|---|---|---|---|
| **2026-09-18** | 57 | 110,067 | 117,844 | 1.07 | **18.1%** ← gravity well |
| 2027-01-15 | 176 | 112,484 | 92,693 | 0.82 | 16.3% (LEAP; 480P lives here) |
| **2026-08-21** | 29 | 83,551 | 86,605 | 1.04 | **13.5%** ← nearest monthly |
| 2026-07-24 | 1 | 97,164 | 66,678 | 0.69 | 13.0% (0/1DTE gamma) |
| 2026-12-18 | 148 | 65,706 | 48,439 | 0.74 | 9.0% |
| 2026-10-16 | 85 | 54,254 | 49,476 | 0.91 | 8.2% |

Sep-18 and Aug-21 are both slightly put-heavy (P/C >1) — consistent with the put
build, but not extreme.

### Largest OI increases (OPRA-parsed) — `[OI:biggest_increases]`
| Contract | Exp | Side | Strike | OI Δ | Vol |
|---|---|---|---|---|---|
| GOOG261016C00365000 | Oct-16 | Call | 365 | +11,070 | 11,475 |
| GOOG261016C00415000 | Oct-16 | Call | 415 | +11,004 | 11,362 |
| GOOG261016P00295000 | Oct-16 | Put | 295 | +5,387 | 5,604 |
| GOOG260807P00310000 | Aug-07 | Put | 310 | +4,008 | 5,000 |
| GOOG260724C00370000 | Jul-24 | Call | 370 | +3,572 | 7,456 |
| GOOG260821P00330000 | Aug-21 | Put | 330 | +3,512 | 6,456 |
| GOOG260918P00380000 | Sep-18 | Put | 380 | +2,539 | 3,006 |

### Closing / roll activity — `[OI:decrease_with_volume]` `[OI:position_rolls]`
Aug-21 upside calls closing: 430C −4,341, 410C −3,408, 450C −3,354, 415C −435,
400C −428. Some Aug-21 puts closing too: 300P −2,277, 335P −1,765, 310P −1,589.
`position-rolls` returned **0 rows** (no clean near→far roll signature at the
threshold). Read: upside call exposure is being *reduced* into the drop.

### Smart positioning (inferred direction) — `[OI:smart_positioning]`
Direction inference is **split** across the 20 rows — bullish tags on 365C, 295P,
310P, 300P, 380P, 400C; bearish tags on 415C, 370C, 330P, 360C, 330P. No dominant
side. The put OI building is materially put-*writing*, not clean shorting.

### Pin risk / OPEX concentration
GOOG **absent** from both market-wide screens (spot is 29 DTE from the nearest
monthly Aug-21 OPEX, > the 7-DTE pin window). No pin commentary this session.

## Tool calls
| Tool | Args | Rows | jq path |
|---|---|---|---|
| oi oi-by-strike | --symbol GOOG --top-n 12 --dte-max 30 | 12 | `.results[].{strike,call_oi,put_oi,net_oi,role,distance_pct}` |
| oi oi-by-strike | --symbol GOOG --top-n 12 (all-exp) | 12 | same |
| oi term-structure | --symbol GOOG | 18 exp | `.term_structure[].{expiry,call_oi,put_oi,put_call_oi_ratio,pct_of_total_oi}` |
| oi biggest-increases | --symbol GOOG --top-n 20 --min-oi-change 500 | 20 | `.results[].{option_symbol,oi_diff_plain,volume}` |
| oi decrease-with-volume | --symbol GOOG --top-n 15 --min-volume 100 | 15 | `.results[].{option_symbol,oi_diff_plain,volume}` |
| oi smart-positioning | --symbol GOOG --top-n 20 --min-oi-change 500 | 20 | `.results[].{option_symbol,inferred_direction,oi_diff_plain,net_ask_bid}` |
| oi position-rolls | --symbol GOOG --threshold 500 --near-dte-max 30 | 0 | — |
| oi pin-risk | --top-n 40 --dte-max 7 --max-distance-pct 5 | GOOG absent | market-wide |
| oi opex-concentration | --top-n 40 --min-concentration-pct 40 | GOOG absent | market-wide |

## Tool errors
- `oi term-structure` payload is `.term_structure[]`, not `.results[]` (nulls in a
  naive `.results` index). Read the correct key; no data lost.

## Verdict for downstream

- **Positioning bias: MIXED / hedge-heavy** — two-sided builds (bullish 365C
  accumulation *and* 415C call-writing), a put ladder that is substantially
  *written* (income) not bought, and upside Aug-21 calls being closed. The
  phase-1 bearish *premium* is not corroborated by a one-way short OI build.
- **Conviction: 2 / 5.** This phase **caps** the bearish thesis: flow dollars lean
  short, but the book is hedge/writing-heavy and directionally muddled.
- **Largest OI build as % of float:** 11,070 contracts ≈ 1.1M share-equiv ≈ 0.02%
  of GOOG's ~5.8B float — **not structural for this name** (advisory; no fz float,
  `[OI:oi_pct_float]` n/a).
- **Three pin/cliff strikes for phase-9** (sourced from roles + term-structure):
  1. **330 (put_heavy, heaviest near-spot put OI 54,968 all-exp)** — the dominant
     magnet just above spot; overlaps the phase-2 breakdown zone. Pivot/resistance.
  2. **300 (put_wall_support, −5.8%)** — LEAP-put strike, structural downside
     support/target; a break of 310 (also put_wall_support) opens toward it.
  3. **350 (call_wall_resistance, all-exp biggest call wall 45,361)** — overhead
     cap, aligns with phase-2 DP supply at 341–351.
  - OPEX gravity: **Sep-18 (18.1%)** dominant; **Aug-21 (13.5%)** nearest tradeable.
- **Open questions:**
  - Is the 365C-vs-415C Oct pairing a call spread / risk-reversal, or two players?
    → phase-4 structure / dealer positioning.
  - With put OI substantially *written*, are dealers long puts (supportive gamma
    below spot at 300/310)? → phase-4 GEX / max-pain.
