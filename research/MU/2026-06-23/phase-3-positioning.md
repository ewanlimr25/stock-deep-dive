# Phase 3 — Open Interest & Positioning

**Ticker:** MU
**As-of date:** 2026-06-23
**Generated:** 2026-06-23
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md

## Summary

Positioning is **defensive/two-sided into the print with structural bullishness
underneath** — it corroborates the phase-1 "vol event, not a direction" read. The
**2026-06-26 earnings-week expiry is the single OI gravity well (19.39% of all OI,
PCR 2.13 put-heavy)**, with the **2026-07-17 monthly second (18.66%, PCR 1.88)**;
near-dated OI is decisively put-skewed while the LEAP buckets flip call-skewed
(2027-12-17 PCR 0.32) — hedging now, structural-long later. The tradeable (≤30-DTE)
wall map is **put-wall support $1000 (−4.9%) · call-heavy ATM pivot $1050 · call-wall
resistance $1200 (+14%)**. New OI is concentrated almost entirely in 06-26 earnings
contracts on **both** sides (puts 550/600/655/1100/1200, calls 1500/1480/1400/1350) —
two-sided earnings strangle/tail building. Smart-positioning infers a **mild bearish
tilt**, but it is driven by tail-hedge put buying, not directional conviction. Largest
single OI build = 4,022 contracts = **0.036% of float** — structurally trivial for a
$1.37T name.

## Key signals

- **OPEX cliff = 2026-06-26** (dte 3, earnings week): **19.39% of total OI**, PCR **2.13** (call 144,202 / put 306,366) `[OI:term_structure]`
- Second cliff **2026-07-17** (dte 24): 18.66% of OI, PCR 1.88 `[OI:term_structure]`
- ≤30-DTE walls: **put support $1000** (net −14,145), **ATM pivot $1050** (call_heavy, net +13,986), **call resistance $1200** (+14.13%, net +14,744) `[OI:oi_by_strike]`
- New OI dominated by **06-26 earnings contracts, both sides** — top build 550p +4,022 (vol 6,352); 1500c +2,711 (vol 8,954) `[OI:biggest_increases]`
- Term-structure PCR flips with tenor: **near-term put-heavy** (06-26: 2.13, 07-10: 5.06) → **LEAP call-heavy** (2027-12-17: 0.32) — hedge-now/long-later `[OI:term_structure]`

## Detailed findings

### OI walls by strike (≤30 DTE — the tradeable map) — `[OI:oi_by_strike]`

| Strike | call_oi | put_oi | net_oi | role | dist% |
|---|---|---|---|---|---|
| **1200** | 17,988 | 3,244 | +14,744 | **call_wall_resistance** | +14.13% |
| 1100 (battle) | — | — | — | (between walls) | +4.6% |
| **1050** | 19,982 | 5,996 | +13,986 | **call_heavy (ATM pivot)** | −0.13% |
| **1000** | 10,767 | 24,912 | −14,145 | **put_wall_support** | −4.89% |
| 900 | 7,621 | 18,155 | −10,534 | put_wall_support | −14.4% |
| 800 | 5,040 | 19,773 | −14,733 | put_wall_support | −23.91% |
| 650/600/550 | — | 35k/30k/26k | strongly − | put_wall_support (tail) | −38 to −48% |

All-expiry view: strike **1000 is a 69,421-OI two-sided battleground** (call 34,711 ≈
put 34,710, net +1) — *not* a clean wall; the ≤30-DTE cut resolves it to put-support.
Deep tail strikes (50/40 with ~42k put OI) are structural crash hedges — noted, not
weighted as tradeable levels.

### OI term structure (the OPEX-cliff lens) — `[OI:term_structure]`

| Expiry | DTE | pct_of_total_oi | PCR (put/call OI) | read |
|---|---|---|---|---|
| **2026-06-26** | 3 | **19.39%** | **2.13** | earnings-week gravity well, put-heavy |
| **2026-07-17** | 24 | **18.66%** | 1.88 | monthly OPEX, put-heavy |
| 2027-01-15 | 206 | 11.06% | 0.94 | LEAP, balanced→call |
| 2026-09-18 | 87 | 8.64% | 1.32 | — |
| 2026-08-21 | 59 | 6.81% | 1.31 | — |
| 2026-12-18 | 178 | 6.60% | 1.25 | — |
| 2027-12-17 | 542 | 1.50% | **0.32** | deep LEAP, strongly call (structural long) |

The 06-26 + 07-17 cliffs together hold ~38% of OI, both put-skewed → the dealer book
is short downside near-term. Cross-check the 06-26 gravity against phase-4 max-pain.

### Largest OI increases — `[OI:biggest_increases]`

| Contract | Side/Strike/Exp | ΔOI | vol | read |
|---|---|---|---|---|
| MU260626P00550000 | 550p 06-26 | +4,022 | 6,352 | deep tail hedge |
| MU260626P00600000 | 600p 06-26 | +4,003 | 6,305 | tail hedge |
| MU260821P00980000 | 980p 08-21 | +3,829 | 4,086 | Aug hedge |
| MU260626P00655000 | 655p 06-26 | +2,906 | 3,284 | tail hedge |
| MU260731P01000000 | 1000p 07-31 | +2,732 | 3,044 | July hedge |
| MU260626C01500000 | 1500c 06-26 | +2,711 | 8,954 | earnings-week lotto call |
| MU271217C01500000 | 1500c 27-12 | +2,533 | 2,720 | LEAP (phase-1 structural call) |
| MU260626P01100000 | 1100p 06-26 | +2,331 | 7,356 | near-money put hedge |

Build is overwhelmingly **2026-06-26** and two-sided; new put strikes (550/600/655/
1100/1200) modestly outnumber new call strikes (1500/1480) → mild defensive tilt.

### Closing / roll activity — `[OI:decrease_with_volume]` / `[OI:position_rolls]`

- Biggest decrease: **MU260702P01000000 (1000p 07-02) −4,091** (vol 6,603) — a 1000-put
  position being closed just after the print; also 1150c 06-26 −923, 1100c 07-17 −633.
- `position-rolls` returned **0 rows** (no near→far rolls above threshold) — positioning
  is fresh earnings build, not rolling existing exposure.

### Smart positioning (inferred direction) — `[OI:smart_positioning]`

Mixed, ~8 bearish / ~6 bullish of the top-14. Bearish tags are the tail-hedge puts
(550/600/655/1100p bought) and a 1480c/1400c sold; bullish tags are the 1500c bought,
980p/1200p/1000p sold. **Net: mild bearish tilt, but it is hedging (put buying), not a
directional short** — consistent with phase-1's call-overwriting + put-hedge read.

### Pin risk & OPEX concentration — `[OI:pin_risk]` / `[OI:opex_concentration]`

- **MU not in the pin-risk top-25**: that tool keys on monthly-OPEX `dte_to_opex=0`
  (today's list is SPY etc. at their OPEX); today (06-23) is not within 7d of a *monthly*
  OPEX, and MU's catalyst is the 06-26 *weekly*. The near-term gravity is the 06-26
  cliff (term-structure) + phase-4 max-pain, not a monthly pin.
- **MU not in opex-concentration (≥40%)**: its top expiry (06-26) is 19.4% — OI is
  spread across many expiries, no single-expiry cliff ≥40%.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows |
|---|---|---|
| `oi term-structure --symbol MU` | 06-26 19.39% PCR 2.13 ← `.term_structure[]\|.pct_of_total_oi,.put_call_oi_ratio` | 19 expiries |
| `oi oi-by-strike --symbol MU --dte-max 30` | 1200 call_wall +14,744; 1000 put_wall −14,145 ← `.results[]\|.strike,.net_oi,.role` | top-10 |
| `oi oi-by-strike --symbol MU` (all-exp) | 1000 battleground net +1 ← `.results[0]` | top-10 |
| `oi biggest-increases --symbol MU --min-oi-change 500` | 550p +4,022 ← `.results[0].oi_diff_plain`; strike/dte clean cols | top-20 |
| `oi decrease-with-volume --symbol MU` | 1000p 07-02 −4,091 ← `.results[0]` | top-15 |
| `oi smart-positioning --symbol MU` | mixed; tail-hedge puts bearish ← `.results[].inferred_direction` | top-20 |
| `oi position-rolls --symbol MU --near-dte-max 30` | 0 rows | — |
| `oi pin-risk --dte-max 7` | MU absent (no monthly OPEX this week) | market-wide |
| `oi opex-concentration --min-concentration-pct 40` | MU absent (top exp 19.4%) | market-wide |

## Tool errors

(none — all reads parsed; term-structure required `.term_structure[]` not `.results[]`,
a shape lookup, not an error.)

## DATA NOTE / CORRECTION

First term-structure `jq` used `.results[]/.expiries[]` (wrong path → indexing error,
surfaced by the JSON-validity gate); re-read against the actual `.term_structure[]`
array. No value was transcribed from the failed read.

## Verdict for downstream phases

- **Positioning bias:** **MIXED / DEFENSIVE-HEDGED** — near-term put-heavy (06-26 PCR
  2.13, tail-hedge put building) over a structural-bullish LEAP base (call-heavy LEAPs).
  Reads as hedging into a binary, not a directional position. Corroborates phase-1
  (mixed) and is consistent with phase-2 accumulation underneath.
- **Conviction:** **2/5** on direction (genuinely two-sided); 4/5 that the 06-26 cliff
  is the structural gravity for the post-print move.
- **Largest OI build as % of float (share-equiv):** **0.036%** (4,022 × 100 / 1.12B) —
  trivial for a mega-cap; the build is informational (earnings positioning), not a
  structural directional bet. `[OI:oi_pct_float fz]`
- **Three pin/cliff strikes for phase-9:**
  1. **Put-wall support $1000** (≤30-DTE role put_wall_support, net −14,145; the 06-26
     PCR-2.13 cliff sits here) → primary downside level / stop reference.
  2. **Call-wall resistance $1200** (role call_wall_resistance, +14.13%, net +14,744) →
     upside target/cap if the print is well-received (note: 06-26 1500c lottos above).
  3. **ATM pivot $1050 + the 06-26 gravity well** (call_heavy at spot) → the post-print
     pin reference; defer exact pin to phase-4 max-pain.
- **Open questions:** Where does max-pain (phase-4) place the 06-26 gravity strike, and
  what does dealer GEX/charm imply for whether the post-print move pins to $1050 or runs
  to a wall? Is the near-term put skew pure hedging or the start of distribution
  (resolve against phase-2's mega-buy accumulation)?
