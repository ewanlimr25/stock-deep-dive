# Phase 3 — Open Interest & Positioning

**Ticker:** MU
**As-of date:** 2026-06-25
**Generated:** 2026-06-25
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md

## Summary

The OI picture refines — and partly *counters* — phase-1's bullish premium read.
The heaviest near-money OI strike is **1200 (call_heavy, net +37,364 call OI,
−1.3% from spot)**, with a secondary call cluster at **1100**; there is **no call
wall above spot** (MU has rallied above its call concentration). But **today's new
OI build is put-dominated** — the largest builds are deep-OTM puts (7-02 550P
+11,152; 6-26 850P/800P/1000P; 7-17 1000P; 8-21 950P), most tagged *bearish*
(bought on the ask) by `smart-positioning`. On a stock that just ran +4% to ~$1,216,
this reads as **broad downside hedging / protection by longs**, not aggressive
directional shorting (nobody shorts a $1,216 stock via 550 puts for direction).
Net: institutions are **participating in upside (few, large call buys) while
layering heavy downside protection (many, smaller, deep-OTM puts)** — a "hedged
long" posture, consistent with phase-2's balanced dark pool. Two near-term OPEX
cliffs dominate: **6-26 (tomorrow, 22.55% of all OI, put-heavy)** and **7-17
(17.27%, put-heavy)**.

## Key signals

- **1200 = dominant near-money strike**, call_heavy, net +37,364 call OI, −1.3% from spot `[OI:oi_by_strike]`
- **No call_wall_resistance above spot** — overhead OI is thin; supply is structural (phase-2 $1,211-1,214), not OI `[OI:oi_by_strike]`
- **New OI build is put-heavy & deep-OTM** — 7-02 550P +11,152, 6-26/7-17/8-21 puts; `smart-positioning` mostly *bearish* (hedging) `[OI:biggest_increases / smart_positioning]`
- **OPEX cliffs:** 6-26 = **22.55%** of all OI (put-heavy 367k/209k), 7-17 = **17.27%** (put-heavy) `[OI:term_structure]`
- Deep **put_wall_support** stacked at 1000 / 900 / 800 (−18% to −34%) — far-below floor `[OI:oi_by_strike]`

## Detailed findings

### OI walls by strike (`oi-by-strike`, spot ≈ $1,216) `[OI:oi_by_strike]`

DTE ≤ 30 (tradeable horizon):

| Strike | call_oi | put_oi | net_oi | role | dist % |
|--------|---------|--------|--------|------|--------|
| **1200** | 26,421 | 3,162 | **+23,259** | call_heavy | **−1.3%** |
| 1100 | 17,889 | 7,672 | +10,217 | call_heavy | −9.5% |
| 1000 | 12,489 | 36,888 | −24,399 | put_wall_support | −17.7% |
| 900 | 7,806 | 24,744 | −16,938 | put_wall_support | −26.0% |
| 800 | 5,200 | 27,994 | −22,794 | put_wall_support | −34.2% |
| 650 | 1,139 | 36,857 | −35,718 | put_wall_support | −46.5% |
| 550 | 3,300 | 31,917 | −28,617 | put_wall_support | −54.8% |
| 50 / 55 | ~500 / 6 | 37,687 / 68,991 | ≈ −38k / −69k | put_wall_support | −96% (worthless tail) |

Read: **1200** is the at-the-money battleground — heavily call-side (net +23k) and
just below spot, so those calls are now ~ITM. The all-expiry aggregate is even
larger at 1200 (net +37,364). **No clean call wall sits above spot**, so OI imposes
little overhead resistance — the supply cap is the phase-2 dark-pool prints at
$1,211-1,214, not an OI wall. The put_wall_support strikes (1000/900/800) are deep
below (−18% to −34%) — a structural floor, but far away. The 50/55 strikes are
worthless legacy tail puts (ignore).

### OI term structure (OPEX cliffs) `[OI:term_structure]`

| Expiry | call_oi | put_oi | pct_of_total_oi | note |
|--------|---------|--------|-----------------|------|
| **2026-06-26 (1DTE)** | 208,612 | 367,233 | **22.55%** | tomorrow — biggest cliff, **put-heavy (P/C 1.76)** |
| **2026-07-17 (monthly)** | 159,450 | 281,690 | **17.27%** | July OPEX, **put-heavy (P/C 1.77)** |
| 2027-01-15 (LEAP) | 115,873 | 145,812 | 10.25% | LEAP anchor |
| 2026-09-18 | 73,493 | 108,546 | 7.13% | next earnings-quarter expiry |
| 2026-08-21 | 67,461 | 114,725 | 7.13% | — |
| 2026-07-02 | 59,602 | 118,866 | 6.99% | — |

The gravity wells are **tomorrow (6-26, 22.55%)** and **7-17 (17.27%)** — both
**put-weighted**. This much put OI at the near expiries reinforces the "heavy
protective put structure" read and hands phase-4 the key question: are dealers
long or short that put gamma (GEX)?

### Largest OI increases (new positions today) `[OI:biggest_increases]` (stock $1,215.6)

| Expiry | Type | Strike | OI Δ | Vol | dist | read |
|--------|------|--------|------|-----|------|------|
| 2026-07-02 | put | 550 | +11,152 | 15,339 | −55% | deep-OTM put build (tail/sold) |
| 2026-07-02 | put | 60 | +9,502 | 9,502 | — | worthless tail (noise) |
| 2026-06-26 | put | 850 | +6,461 | 18,209 | −30% | 1DTE deep-OTM put |
| 2026-06-26 | call | 1250 | +5,210 | 15,226 | +2.9% | 1DTE call (smart: *bearish* = write/cap) |
| 2026-06-26 | put | 800 | +4,632 | 17,527 | −34% | 1DTE deep-OTM put |
| 2026-07-17 | put | 1000 | +3,957 | 6,199 | −18% | July-OPEX hedge put |
| 2026-08-21 | put | 950 | +3,934 | 4,397 | −22% | Aug hedge put |
| 2026-06-26 | put | 1000 | +3,894 | 15,895 | −18% | 1DTE put |

**Of the top builds, puts outnumber calls ~5:1.** Most carry `smart-positioning`
*bearish* tags (bought on the ask). At strikes 18–55% below a $1,216 spot, these
are **downside hedges / tail insurance / put writes**, not directional shorts. The
one call build (1250, 6-26) is flagged bearish = **covered-call writing / upside
cap** just above spot.

### Closing / roll activity `[OI:decrease_with_volume / position_rolls]`

- Decreases are 1DTE expiry management: 6-26 **1050 call −9,864** (vol 26,985), 6-26
  550 put −5,291, 6-26 1240 call −2,245 — ITM/near calls being closed/exercised
  ahead of tomorrow's expiry. Normal churn, not directional.
- `position-rolls`: **0 detected** (single-day detection only; cross-session rolls
  not captured — caveat noted).

### Smart positioning (inferred) `[OI:smart_positioning]`

Of the top-8 inferred reads: **6 bearish, 2 bullish.** The bearish tags are the
deep-OTM put buys (550/1000/950) + the 1250 call write; the "bullish" tags (850P,
800P) are inferred put *selling*. Net inferred lean: **mildly bearish/hedging on
the day's OI build** — a genuine counter to phase-1's bullish premium.

### Pin / OPEX concentration

- `pin-risk` (dte-max 7, max-distance 5%): **MU outside the market-wide top-25** —
  recorded, no pin commentary forced. (The 1200 strike is within 5% but MU's
  concentration didn't rank top-25.)
- `opex-concentration` (min 40%): **MU outside top-20** — its largest single-expiry
  concentration is 22.55% (6-26), below the 40% bar. No single expiry dominates.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows |
|------------------|--------------------------|------|
| `oi oi-by-strike --symbol MU --dte-max 30` | 1200 net +23,259 call_heavy −1.3% ← `.results[]` | top-10 |
| `oi oi-by-strike --symbol MU` (all-expiry) | 1200 net +37,364 ← `.results[]` | top-10 |
| `oi term-structure --symbol MU` | 6-26 22.55%, 7-17 17.27% ← `.term_structure[].pct_of_total_oi` | all exp |
| `oi biggest-increases --symbol MU --min-oi-change 500` | 7-02 550P +11,152 ← `.results[].{option_symbol,oi_diff_plain}` | top-20 |
| `oi smart-positioning --symbol MU --min-oi-change 500` | 6 bearish / 2 bullish ← `.results[].inferred_direction` | top-20 |
| `oi decrease-with-volume --symbol MU` | 6-26 1050C −9,864 ← `.results[]` | top-15 |
| `oi position-rolls --symbol MU --near-dte-max 30` | rolls_detected 0 ← `.rolls_detected` | — |
| `oi pin-risk --dte-max 7 --max-distance-pct 5` | MU outside top-25 | top-25 |
| `oi opex-concentration --min-concentration-pct 40` | MU outside top-20 | top-20 |

## Tool errors

None. (`term-structure` payload is under `.term_structure[]`, not `.results[]` —
parsed correctly after schema check.)

## DATA NOTE / CORRECTION

`biggest-increases` rows carry no side/expiry column — both parsed from
`option_symbol` (OPRA): e.g. `MU260702P00550000` → 2026-07-02 / Put / 550. All
strikes/types cross-checked against the explicit `strike`/`underlying_symbol`
fields in the row. `term-structure` initial jq failed on `.results[]` (wrong key);
re-parsed against `.term_structure[]` — no number transcribed from the failed read.

## Verdict for downstream phases

- **Positioning bias:** **MIXED / HEDGED-LONG** — heaviest near-money OI is call-side
  (1200, net +37k) and overhead OI resistance is absent (bullish for upside path),
  BUT today's *new* OI build is put-dominated (~5:1) and inferred mostly bearish =
  broad downside hedging on an extended name. Institutions are long upside *and*
  insured against downside.
- **Conviction:** **3 / 5** — the call-heavy 1200 strike + no overhead wall is
  constructive, but the put-heavy build + put-weighted 6-26/7-17 cliffs are a real
  caution. This corroborates phase-2's "two-way into strength," not a clean bull.
- **Largest OI build as % of float:** 11,152 contracts ≈ 1.12M share-equiv /
  1.12B float = **0.10%** — *not* structural for a 1.12B-float mega-cap; the OI
  builds are tradeable/tactical, not a balance-sheet-scale bet. `[OI:oi_pct_float fz]`
- **Three pin/cliff strikes for phase-9:**
  1. **1200** — `call_heavy`, net +37,364 call OI, −1.3% from spot: the at-the-money
     magnet / first support-or-resistance pivot.
  2. **6-26 expiry (22.55% of OI, put-heavy)** — tomorrow's gravity well; the 7-17
     OPEX (17.27%, put-heavy) is the next.
  3. **1000** — `put_wall_support`, net −24,399, −17.7%: the structural downside
     floor (deep, but the cleanest OI support level).
- **Open questions:** Are dealers **long or short** the heavy 6-26/7-17 put gamma
  (phase-4 GEX) — i.e. will pinning *dampen* or *amplify* moves? Is the 1200
  call_heavy cluster covered-write supply (phase-2 institutions writing against
  stock) or speculative length? Is the put build a hedge against a visible long
  (phase-2 balanced) or a real bearish tell?
