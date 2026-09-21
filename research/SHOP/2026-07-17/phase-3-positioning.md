# Phase 3 — Open Interest & Positioning

**Ticker:** SHOP
**As-of date:** 2026-07-17
**Generated:** 2026-07-19 (run) · as-of 2026-07-17
**Upstream phases cited:** phase-0.5-context.md, phase-1-flow.md, phase-2-dark-pool.md

## Summary

Near-term OI structure **brackets spot (123.56) cleanly**: put-wall support at
**117 (net −5,461) and the 120 battleground (net −610)**, call-wall resistance at
**125 (net +4,687, +1.2%) and 130 (net +7,377, +5.3%)**. This corroborates phase-1's
116–121 battle zone and phase-2's 124.7–125.8 overhead supply. The dominant OI mass
is the **Sep-18 OPEX = 52.9% of all 520,744 contracts, heavily call-heavy** (247k
call vs 29k put) — but that call OI is spread across deep-OTM 130–175 LEAP-style
strikes, **not a near-term directional signal**. New OI builds are **modest** (max
988 contracts = ~0.008% of float — immaterial) with a slight put-build tilt,
although the two largest builds are ambiguously tagged bullish by smart-positioning.
Today (7/17) is July monthly OPEX but SHOP is **neither a pin candidate nor
opex-concentrated**. Net: mixed positioning, mild near-term hedging tilt.

## Key signals

- **Near-term put wall 117** (net_oi −5,461, −5.3%) = first structural support. `[OI:oi_by_strike]`
- **Near-term call walls 125 (+4,687, +1.2%) and 130 (+7,377, +5.3%)** = resistance
  band capping upside. `[OI:oi_by_strike]`
- **Sep-18 OPEX = 52.9% of total OI**, call-heavy 247k/29k — the gravity well, but
  deep-OTM. `[OI:term_structure]`
- **Next-week 7/24 is slightly put-heavy** (7,593 call / 8,914 put OI). `[OI:term_structure]`
- **Largest OI build only 988 contracts** (Jul-31 $150 call) — no structural
  mega-position; ~0.008% of float. `[OI:biggest_increases]`

## Detailed findings

### OI walls by strike (≤30 DTE tradeable horizon) `[OI:oi_by_strike]`

| Strike | call_oi | put_oi | net_oi | role | dist% | Read |
|---|---|---|---|---|---|---|
| 150 | 9,743 | 121 | +9,622 | call_wall_resistance | +21.4% | Far OTM cap |
| 140 | 6,184 | 1 | +6,183 | call_wall_resistance | +13.3% | Upper cap |
| **130** | 7,888 | 511 | **+7,377** | call_wall_resistance | **+5.3%** | **First strong resistance** |
| 135 | 5,908 | 125 | +5,783 | call_wall_resistance | +9.3% | Resistance |
| **125** | (all-exp 10,694) | 6,007 | **+4,687** | call_wall_resistance | **+1.2%** | **Nearest overhead** (agrees w/ phase-2 125.06) |
| **120** | 3,684 | 4,294 | **−610** | put_wall_support | **−2.9%** | **Battleground** (near-balanced) |
| **117** | 331 | 5,792 | **−5,461** | put_wall_support | **−5.3%** | **Strongest near support** |
| 115 | 3,750 | 3,970 | −220 | put_wall_support | −6.9% | Two-sided (phase-1 wrote puts here) |
| 110 | 2,126 | 4,865 | −2,739 | put_wall_support | −11% | Deeper support |
| 100 | 822 | 7,697 | −6,875 | put_wall_support | −19% | Tail support |

Spot 123.56 sits in a **120–125 no-man's-land**, put-wall support 117/120 below,
call-wall resistance 125/130 above. Clean range to size against.

### OI term structure (OPEX cliffs) `[OI:term_structure]`

| Expiry | call_oi | put_oi | P/C(oi) | % of total OI |
|---|---|---|---|---|
| **2026-09-18** | 246,819 | 28,856 | 0.12 | **52.9%** ← gravity well (call-heavy, deep-OTM) |
| 2026-07-17 (today, exp) | 54,851 | 34,938 | 0.64 | 17.2% |
| 2027-01-15 (LEAP) | 24,400 | 24,513 | 1.00 | 9.4% |
| 2026-08-21 | 17,907 | 13,339 | 0.74 | 6.0% |
| **2026-07-24 (next wk)** | 7,593 | 8,914 | **1.17** | 3.2% ← **put-heavy near-term** |

Total OI 520,744 across 18 expiries. The Sep-18 call mass is structural/LEAP, not a
short-term directional tell; cross-check vs phase-4 max-pain. Near-term (7/24)
put-heaviness aligns with the phase-1 $121-put buying.

### Largest OI increases (min 100) `[OI:biggest_increases]`

Modest builds — 5 of the top 8 are **puts**:
Jul-31 $150C +988 · Jul-24 $110P +948 · Jan-27 $95P +484 · Oct $110P +363 · Nov
$155P +234 · Sep $125P +228 · Sep $100P +198 · Jul-24 $125C +153. Slight
put-building tilt (hedging/downside), but nothing structural.

### Closing / roll activity `[OI:decrease_with_volume]`

Decreases are the **expiring 7/17 contracts** (July OPEX): $130C −640 (vol 3,557),
$120C −182, $125C −138, $105P −170. Normal OPEX-day roll-off, no directional roll
signature.

### Smart positioning `[OI:smart_positioning]`

Only 2 contracts cleared the ≥500 OI-change filter; smart-positioning tags **both
bullish**: Jul-31 $150C +988 (call buy) and Jul-24 $110P +948 (inferred put-write).
Low sample, crude inference — a **mild bullish counter** to phase-2 distribution,
but weak.

### Pin risk / OPEX concentration `[OI:pin_risk] [OI:opex_concentration]`

SHOP is **absent** from both the pin-risk (≤7 DTE, ≤5% distance) and
opex-concentration (≥40%) market-wide lists, **despite today being July monthly
OPEX**. No pin gravity into today's close; no single-expiry cliff within range.

## Tool calls (audit trail)

| Command | Key value ← `jq` path | Rows |
|---|---|---|
| `uw oi oi-by-strike --symbol SHOP --dte-max 30 --top-n 12` | put wall 117 net −5,461 ← `.results[]{net_oi,role}` | 10 |
| `uw oi term-structure --symbol SHOP` | Sep-18 52.9% ← `.term_structure[]{pct_of_total_oi}` | 18 exp |
| `uw oi biggest-increases --symbol SHOP --min-oi-change 100` | Jul-31 150C +988 ← `.results[].oi_diff_plain` | 14 |
| `uw oi decrease-with-volume --symbol SHOP --min-volume 100` | 7/17 130C −640 ← `.results[].oi_diff_plain` | 15 |
| `uw oi smart-positioning --symbol SHOP --min-oi-change 500` | both bullish ← `.results[].direction` | 2 |
| `uw oi pin-risk --dte-max 7 --max-distance-pct 5` | SHOP absent ← `select(.ticker=="SHOP")`=∅ | 40 |
| `uw oi opex-concentration --min-concentration-pct 40` | SHOP absent | 40 |

## Tool errors

- `uw oi term-structure` output is under `.term_structure` (not `.results`) — first
  `jq` on `.results[]` hit nulls; re-read against `.term_structure[]`. Values valid.
- `uw oi biggest-increases --min-oi-change 500` returned only 2 rows; re-ran at
  `--min-oi-change 100` for the build map. Both surfaced.

## DATA NOTE / CORRECTION

`term-structure` path corrected (`.term_structure` not `.results`). `fz Shs Float`
n/a → float ≈1.30B derived for the %-of-float line. Largest build 988 ct ×100 =
98,800 sh = **0.0076% of float** — immaterial.

## Verdict for downstream phases

- **Positioning bias:** MIXED — near-term put-build/hedging tilt (5 of top-8 builds
  puts; 7/24 put-heavy) offset by a weak smart-positioning bullish tag on the two
  biggest builds. No structural directional bet.
- **Conviction:** 2/5.
- **Largest OI build as % of float:** ~0.008% (988 ct) — **not structural for a
  1.30B-float name**; positioning is tactical, not a whale.
- **Three pin/cliff strikes for phase-9:**
  1. **Resistance: 125 → 130** (call walls; 125 net +4,687 at +1.2%, 130 net +7,377
     at +5.3%) — upside is capped into this band.
  2. **Support: 117** (put wall, net −5,461, −5.3%); **120** the immediate
     battleground (net −610).
  3. **OPEX cliff: Sep-18** (52.9% of OI, call-heavy) — the far gravity well; the
     tradeable near-term structure is the 117–130 range.
- **Open questions:** Does phase-4 max-pain sit inside 120–125 (reinforcing the
  range)? Is dealer gamma positive (pinning 120–125) or negative below 117 (which
  would let phase-2's mild distribution accelerate on a break)?
