# Phase 3 — Open Interest & Positioning

**Ticker:** CRM
**As-of date:** 2026-06-05
**Generated:** 2026-06-06T16:12:00-04:00
**Upstream:** phase-1-flow.md (open question: "are the Jan-2028 call sales
overwrites or naked vol supply?"), phase-2-dark-pool.md (overhead supply shelves
~189/201/210; spot 185.66), phase-0-intake.md (`Shs Float` 792.65M `fz`)

## Summary

Positioning is a **call-supply ceiling over a put-floor at spot**. Every OI
build ≥500 contracts on the date is an OTM **call** (195 through 220), and
smart-positioning infers 5 of 6 of those builds were **sold** (net ask-bid
negative) — the street is writing calls into the post-earnings fade, stacking
supply on top of the dark-pool shelves phase-2 mapped at 189/201/210. Below
spot, 185 and 180 are put-support walls. The OPEX cliff is the 2026-06-18
monthly (25.13% of all OI, 13 days out) with its heaviest near-DTE walls at
200 and an outsized 220 (net +37.3k ≤30DTE — stranded from the 6/01 spike at
209.60, now 18% OTM). No pin-risk or opex-concentration flag for CRM
market-wide. Net read: dealers/overwriters are SHORT upside calls 190–220;
positioning agrees with phase-2's "trapped supply overhead" — rallies into
190–200 should meet mechanical selling, while 180–185 puts give near support.

## Key signals

- **All 6 OI builds ≥500 are calls above spot, 5/6 inferred SOLD:** 0DTE-expiry
  195C +2,327 / 200C +1,572 (both expired worthless at 185.66 close), Jun-18
  220C +1,114, Jun-18 210C +693, Jul-17 220C +604 (this one inferred *bullish*),
  Jun-18 190C +544. `[OI:biggest_increases]` `[OI:smart_positioning]`
- **OPEX cliff = 2026-06-18 monthly: 25.13% of total OI** (141,275C / 69,787P,
  derived P/C 0.49) — the chain's gravity well, 13 days from as-of.
  `[OI:term_structure .term_structure[]]`
- **Near-term wall map (≤30DTE):** put_wall_support **185** (16,456P, net
  −9,580, −0.41% from spot) and **180** (net −933); two-sided **190** (10,552C /
  10,885P, net −333 — battleground, not a wall); call_wall_resistance **195**
  (net +8,928), **200** (net +21,976), **220** (net +37,305). `[OI:oi_by_strike]`
- **220 is the stranded-supply tell:** 66,125 calls all-expiry (net +61,624) —
  18.44% OTM after a −11% four-day fade; built when spot was 200–210 (6/01–02),
  now far out of the money into 6/18 OPEX. `[OI:oi_by_strike]`
- **No roll activity (n=0) and decreases are expiry cleanup** (6/05 strikes:
  182.5P −1,296, 220C −1,095) plus far-OTM call closes (Aug 240C −198, Jul 260C
  −121) — spike-chasers liquidating, not repositioning. `[OI:position_rolls]`
  `[OI:decrease_with_volume]`

## Detailed findings

### OI walls by strike — all-expiry aggregate `[OI:oi_by_strike]`

| Strike | Call OI | Put OI | Net OI | Role | Dist % |
|---|---|---|---|---|---|
| 220 | 66,125 | 4,501 | +61,624 | call_wall_resistance | +18.44 |
| 200 | 63,328 | 19,968 | +43,360 | call_wall_resistance | +7.67 |
| 210 | 36,369 | 7,672 | +28,697 | call_wall_resistance | +13.05 |
| 250 | 33,726 | 4,003 | +29,723 | call_wall_resistance | +34.59 |
| 230 | 29,227 | 4,921 | +24,306 | call_wall_resistance | +23.82 |
| 195 | 25,478 | 12,484 | +12,994 | call_wall_resistance | +4.98 |
| 190 | 25,746 | 34,026 | −8,280 | put_heavy (two-sided) | +2.29 |
| 185 | 18,260 | 25,833 | −7,573 | put_wall_support | −0.41 |
| 180 | 17,867 | 24,388 | −6,521 | put_wall_support | −3.10 |
| 170 | 9,661 | 29,493 | −19,832 | put_wall_support | −8.48 |

### OI walls — tradeable horizon (≤30 DTE) `[OI:oi_by_strike --dte-max 30]`

| Strike | Call OI | Put OI | Net OI | Role | Dist % |
|---|---|---|---|---|---|
| 220 | 40,785 | 3,480 | +37,305 | call_wall_resistance | +18.44 |
| 200 | 27,132 | 5,156 | +21,976 | call_wall_resistance | +7.67 |
| 240 | 17,056 | 0 | +17,056 | call_wall_resistance | +29.20 |
| 210 | 14,916 | 743 | +14,173 | call_wall_resistance | +13.05 |
| 195 | 13,468 | 4,540 | +8,928 | call_wall_resistance | +4.98 |
| 230 | 13,653 | 2 | +13,651 | call_wall_resistance | +23.82 |
| 190 | 10,552 | 10,885 | −333 | put_heavy → battleground | +2.29 |
| 185 | 6,876 | 16,456 | −9,580 | put_wall_support | −0.41 |
| 180 | 7,408 | 8,341 | −933 | put_wall_support | −3.10 |
| 170 | 1,626 | 11,297 | −9,671 | put_wall_support | −8.48 |

190 is NOT a clean wall near-term (net −333, two-sided battleground); the real
near resistance steps are 195 then 200. Support: 185 (strong, at spot) then a
soft 180 and a hard 170.

### OI term structure `[OI:term_structure]`

Top expiries by `pct_of_total_oi` (total chain OI ≈ 1.082M, phase-1 deep-dive):
**2026-06-18 = 25.13%** (141,275C/69,787P, derived P/C 0.49) ← **OPEX cliff**;
2026-07-17 = 12.33% (63,532/40,013); 2026-09-18 = 11.64%; 2027-01-15 = 11.57%
(64,048/33,138 — where phase-1's risk reversal lives); 2026-06-05 = 10.36%
(expired on as-of date, 65,054C/21,955P — that call mass is now OFF the board,
mechanically reducing upside OI overhead next session); 2026-08-21 = 8.94%.
Note `put_call_ratio` returned null per-expiry — P/C derived as put_oi/call_oi.

### Largest OI increases `[OI:biggest_increases]` (strike/expiry/side parsed from OPRA `option_symbol`)

| Contract | OI Δ | Volume | Smart-positioning inference |
|---|---|---|---|
| 2026-06-05 195C | +2,327 | 3,805 | bearish (sold) — expired worthless same day |
| 2026-06-05 200C | +1,572 | 5,030 | bearish (sold) — expired worthless |
| 2026-06-18 220C | +1,114 | 2,039 | bearish (sold) |
| 2026-06-18 210C | +693 | 1,359 | bearish (sold) |
| 2026-07-17 220C | +604 | 1,122 | **bullish (bought)** — lone spec bet |
| 2026-06-18 190C | +544 | 2,176 | bearish (sold) |

n=6 at the ≥500 threshold; **zero put builds** ≥500 — the put walls are legacy
OI, not fresh hedging. `[OI:smart_positioning .inferred_direction]`

### Closing / roll activity

Decreases `[OI:decrease_with_volume]` (n=15): dominated by 6/05-expiry
mechanical cleanup (182.5P −1,296 on 4,813 vol; 220C −1,095 on 1,271; 210P
−313; 205P −255; 210C −242) plus far-OTM call abandonment (8/21 240C −198,
7/17 260C −121, 6/12 215C −125). Position rolls (threshold 500, near-DTE ≤30):
**n=0** `[OI:position_rolls]` — nobody is rolling the stranded 210–220 June
calls out; they're being left to decay or closed outright.

### Pin risk / OPEX concentration

Market-wide `uw oi pin-risk --dte-max 7` top-25: **CRM absent** (no notable pin
into the 6/12 weekly). Market-wide `opex-concentration --min-concentration-pct
40` top-20: **CRM absent** (the 25.13% 6/18 cliff is large for the name but
below the 40% market-wide flag bar). `[OI:pin_risk]` `[OI:opex_concentration]`

## Tool calls

| Command | jq path | Status |
|---|---|---|
| `uw oi oi-by-strike --symbol CRM --top-n 10 [--dte-max 30] --date 2026-06-05 --json` ×2 | `.results[] {strike,call_oi,put_oi,net_oi,role,distance_pct}` | ok n=10+10 |
| `uw oi term-structure --symbol CRM --date 2026-06-05 --json` | `.term_structure[]` (first attempt `.results` → jq null-iterate error; rows live under `.term_structure`) | ok n=19 expiries |
| `uw oi biggest-increases --symbol CRM --top-n 20 --min-oi-change 500 --date 2026-06-05 --json` | `.results[] {option_symbol,oi_diff_plain,volume}` | ok n=6 |
| `uw oi decrease-with-volume --symbol CRM --top-n 15 --min-volume 100 --date 2026-06-05 --json` | `.results[] {option_symbol,oi_diff_plain,volume}` | ok n=15 |
| `uw oi smart-positioning --symbol CRM --top-n 20 --min-oi-change 500 --date 2026-06-05 --json` | `.results[] {option_symbol,inferred_direction,oi_diff_plain}` | ok n=6 |
| `uw oi position-rolls --symbol CRM --threshold 500 --near-dte-max 30 --date 2026-06-05 --json` | `.results` | ok n=0 |
| `uw oi pin-risk --top-n 25 --dte-max 7 --max-distance-pct 5 --date 2026-06-05 --json` | filter ticker==CRM | ok — absent |
| `uw oi opex-concentration --top-n 20 --min-concentration-pct 40 --date 2026-06-05 --json` | filter ticker==CRM | ok — absent |

## Tool errors

- First `term-structure` extraction used jq path `.results[]` → `jq: error (at
  <stdin>:198): Cannot iterate over null (null)`. Not a CLI failure — the
  payload roots at `.term_structure[]` (keys: expiry_count, source, symbol,
  term_structure, total_oi). Re-extracted with the correct path; values above
  round-tripped through jq on the second pass.

## Verdict for downstream

- **Positioning bias: CALL SUPPLY OVERHEAD / mild put floor.** Fresh OI is
  call-writing into the fade (5/6 builds sold); put walls at 185/180 are legacy,
  with zero fresh put builds ≥500 — no panic hedging, no aggressive bullish
  accumulation. Answers phase-1's open question: the call sales pattern
  (190–220 strikes, sold, no rolls) is consistent with **overwriting/supply,
  not naked-vol panic** — but it is supply either way.
- **Conviction: 3/5** (wall map is unambiguous; inference layer is heuristic).
- **Largest OI build as % of float:** +2,327 contracts ≈ 232,700 share-equiv ≈
  **0.029%** of 792.65M float `[OI:oi_pct_float fz]` — nothing here is
  structural for a name this size; the signal is the *pattern* (all-call,
  all-sold), not the size.
- **Three pin/cliff strikes for phase-9:**
  1. **185 put_wall_support** (net −9,580 ≤30DTE, −0.41% from spot) — first
     defense; lines up with phase-2's thin-air zone below 186.
  2. **195→200 call walls** (net +8,928 / +21,976 ≤30DTE) — the resistance
     stack; 200 also carries the all-expiry +43,360 wall and phase-2's $415M
     DP shelf at 201.
  3. **2026-06-18 OPEX cliff (25.13% of chain OI)** — 141k calls, most 190–220,
     largely underwater; their decay/unwind into 6/18 is the next two weeks'
     mechanical flow driver.
- **Open questions:** Where does dealer gamma flip — is 185–190 long-gamma
  pinning or short-gamma acceleration territory (phase 4 GEX + max-pain)? Does
  the 6/18 max-pain sit below spot (phase 4), adding OPEX gravity to the
  bear case?
