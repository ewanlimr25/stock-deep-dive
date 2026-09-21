# Phase 3 — Open Interest & Positioning

**Ticker:** BBAI
**As-of date:** 2026-05-29
**Generated:** 2026-05-31 (re-verified against validated JSON)
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md

> **## DATA NOTE.** Figures from JSON-validated `uw oi` output. An earlier draft
> over-stated the $5 wall (271k) and mis-named the OPEX cliff (6/18); the correct
> numbers (near-term $5 = 82.8k call OI; dominant OI = Jan-2027 LEAP at 36%) are below.

## Summary

BBAI's option structure is **call-heavy and concentrated at the $5 strike, but the
bulk of the open interest is a long-dated LEAP.** The single largest OI block is
the **2027-01-15 expiry — 36.01% of all 871,994 OI** (call 236,525 / put 77,494),
i.e. structural/speculative LEAP calls that hedge slowly. The largest **near-term**
(DTE ≤ 30) strike is **$5: call_oi 82,832 vs put_oi 7,422 (net +75,410), role
`call_heavy`, −1.38% from spot ($5.07)** — a two-sided battleground at spot, not a
one-sided wall. Above it sit call walls at **$5.5 (+8.5%)** and **$6 (+18%)**; put
support is **thin and far** ($4.5 at −11% is `call_heavy`; real put walls only at
$3.5/$3). The near-term OPEX cliff is **6/18 (19.74% of OI)**, and **pin-risk flags
$5** (pin_score 101,019, 1.38% away). Fresh builds are all calls, but the $5 strike
also saw heavy **closing** (−5,071) — churn, not clean accumulation.

## Key signals

- **Dominant OI = 2027-01-15 LEAP: 36.01% of total** (call 236,525 / put 77,494,
  P/C 0.328) — long-dated, slow-hedging [OI:term-structure]
- **Near-term $5 strike** (DTE≤30): call 82,832 / put 7,422 (net +75,410),
  `call_heavy`, **−1.38% from spot** — the pin/battleground [OI:oi-by-strike]
- Near-term call walls above: **$5.5 (net +33,913, +8.5%)**, **$6 (+32,679, +18%)**,
  **$7 (+21,981, +38%)** [OI:oi-by-strike]
- **Pin-risk FLAGGED at $5**: pin_score 101,019, pin_distance 1.38%, spot $5.07,
  dte_to_opex 0 [OI:pin-risk]
- Fresh builds **all calls** ($5.5 +13,795, $7 +10,114, $5 +5,079) **but $5 also
  closed −5,071 and $4.5 −3,459** → churn at the money [OI:biggest-increases][OI:decrease-with-volume]
- Near-term OPEX cliff **6/18 (19.74% of OI)**, call-heavy (P/C 0.251) [OI:term-structure]

## Detailed findings

### OI walls by strike — near-term (`uw oi oi-by-strike --dte-max 30`)

| strike | call_oi | put_oi | net_oi | role | dist% |
|--------|---------|--------|--------|------|-------|
| **5** | **82,832** | 7,422 | **+75,410** | call_heavy | −1.38 |
| 6 | 37,617 | 4,938 | +32,679 | call_wall_resistance | +18.34 |
| 5.5 | 34,129 | 216 | +33,913 | call_wall_resistance | +8.48 |
| 4.5 | 30,997 | 8,797 | +22,200 | call_heavy | −11.24 |
| 4 | 30,896 | 28,574 | +2,322 | call_heavy | −21.10 |
| 7 | 21,990 | 9 | +21,981 | call_wall_resistance | +38.07 |
| 3.5 | 1,278 | 8,826 | −7,548 | put_wall_support | −30.97 |
| 3 | 3,104 | 4,369 | −1,265 | put_wall_support | −40.83 |

→ Near-term structure is call-dominated; **$5 is the pin (call_heavy at spot)**,
real put support only ~−31% away. Downside has little OI cushion under $4.5.
(All-expiry view scales $5 to call 163,363 / put 38,109 — the extra is LEAP OI.)

### OI term structure (`uw oi term-structure`, total_oi 871,994)

| expiry | dte | call_oi | put_oi | P/C | % of total |
|--------|-----|---------|--------|-----|------------|
| **2027-01-15** | 231 | 236,525 | 77,494 | 0.328 | **36.01** |
| **2026-06-18** | 20 | 137,593 | 34,543 | 0.251 | **19.74** |
| 2028-01-21 | 602 | 72,224 | 15,444 | 0.214 | 10.05 |
| 2026-05-29 (0DTE) | 0 | 65,276 | 13,358 | 0.205 | 9.02 |
| 2026-07-17 | 49 | 45,834 | 13,857 | 0.302 | 6.85 |
| 2026-06-05 | 7 | 48,193 | 8,399 | 0.174 | 6.49 |
| 2026-09-18 | 112 | 43,258 | 10,061 | 0.233 | 6.11 |

→ **Tradeable cliff = 6/18** (largest near-term, 20 DTE); the 36% Jan-2027 LEAP is
the structural anchor but hedges slowly (treat as background, not a near-term lever).

### Builds, closes, smart positioning

- `biggest-increases` (all calls): $5.5C +13,795 (vol 25,405), $7C +10,114, $5C
  +5,079 (vol 32,291), $5C +4,689, $6C +3,650.
- `decrease-with-volume`: **$5 −5,071 (vol 29,431)**, **$4.5 −3,459 (19,055)**, $7
  −1,405 → meaningful same-day **closing at $5/$4.5** = churn, not one-way building.
- `smart-positioning` (`inferred_direction`): $5.5/$7/$5/$6 mostly **bullish**
  call-opening, with **bearish** tags at $5/$4.5/$6 → mixed, net bullish-opening.

### Pin / OPEX concentration

- `pin-risk`: **BBAI flagged** — nearest_high_oi_strike $5, pin_distance 1.38%,
  pin_score 101,019, spot $5.07, total_oi_in_window 201,472. $5 is a near-term magnet.
- `opex-concentration` (≥40%): **none** — the 36% Jan-2027 concentration is below
  the threshold (and is a LEAP, not a tradeable cliff).

## Tool calls (audit trail)

| Command | Result |
|---------|--------|
| `uw oi oi-by-strike --symbol BBAI --top-n 12 --dte-max 30 --date 2026-05-29` | $5 call 82,832/put 7,422 (call_heavy, −1.38%) |
| `uw oi term-structure --symbol BBAI --date 2026-05-29` | Jan-2027 LEAP 36%; 6/18 19.7%; total_oi 871,994 |
| `uw oi biggest-increases / decrease-with-volume --symbol BBAI` | all-call builds; but $5 −5,071 / $4.5 −3,459 closing |
| `uw oi smart-positioning --symbol BBAI` | net bullish call-opening, mixed |
| `uw oi pin-risk --dte-max 7` / `opex-concentration` | pin $5 flagged; no opex-conc flag |

## Tool errors

- An earlier draft used non-existent leaves (`oi net/by-strike/changes`) and a
  wrong $5 OI figure; corrected to validated `oi-by-strike`/`term-structure`/etc.

## Verdict for downstream phases

- **Positioning bias:** **call-heavy but churny** — fresh call opening offset by
  $5/$4.5 closing; structure dominated by a slow Jan-2027 LEAP.
- **Conviction:** 3/5 — the call-heavy chain and $5 pin are clear; directional
  read is conditional on the gamma sign (phase-4).
- **Largest OI build as % of float:** `$5.5C +13,795` ≈ 1.38M share-equiv =
  **0.29% of float** (advisory) — near-term/retail-scale, not structural.
- **Three pin/cliff strikes for phase-9:** **$5.00** (pin + spot + call_heavy + DP
  shelf — the pivot/invalidation anchor), **$5.50** (call wall, +8.5%, upside
  magnet), **$4.50** (thin first support, −11%); **6/18** is the near OPEX cliff.
- **Open questions:** Are dealers long or short gamma at $5 (phase-4 GEX is
  decisive)? Does the churn at $5 (open+close) mean the squeeze is stalling at the
  call wall? Is the thin sub-$4.5 put structure an air-pocket if $5 fails?
