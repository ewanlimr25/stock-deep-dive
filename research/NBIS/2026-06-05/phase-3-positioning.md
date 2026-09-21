# Phase 3 — Open Interest & Positioning

**Ticker:** NBIS
**As-of date:** 2026-06-05
**Generated:** 2026-06-06T20:18:00-0400
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md

## Summary

OI confirms the bearish lean phase-1 found in sweeps — and shows it was built
**before** Friday's slide: the largest OI increases in the 2026-06-05 changes
file (which reflects Thursday 06-04 trading) are a stack of short-dated OTM puts
— Jun-12 205P **+6,871**, Jun-18 200P +3,555, Jun-12 202.5P +2,500, Jun-12 200P
+1,458 — with `smart-positioning` tagging the whole cluster ask-biased/bearish
(205P net_ask_bid +692; 202.5P +2,370). The ≤30-DTE wall map is **pure put
walls** (220 → 200 → 190 → 150; not one call strike makes the near-term top-10),
while the all-expiry map shows call walls only far overhead (250 / 260 / 300).
Term structure: Jun-18 monthly is the OPEX cliff (20.9% of 825,120 total OI,
P/C 1.358), and a put-heavy 0DTE book (Jun-05: 20.66% of OI, P/C 3.20) expired
at Friday's close — Monday's chain opens ~⅕ lighter. The phase-1 Jun-26 285P
write (Friday trade) cannot appear in OI until the next session's file — not
verifiable in an as-of run.

## Key signals

- **Pre-slide put build**: Jun-12 205P oi_diff_plain **+6,871** (vol 9,202),
  Jun-18 200P +3,555, Jun-12 202.5P +2,500, Jun-12 200P +1,458 — all opened
  Thursday, all bearish-inferred with ask-side bias `[OI:biggest_increases]`,
  `[OI:smart_positioning]`
- ≤30-DTE top-10 OI strikes are **all `put_wall_support`**: 200 (15,617p),
  205 (15,761p, net −15,390), 170 (15,525p), 150 (11,910p), 210 (11,051p),
  220 (8,932p, −3.4% from spot) `[OI:oi_by_strike --dte-max 30]`
- All-expiry call walls: **250** (25,916c, net +21,723, +9.8%), 260 (+14.2%),
  300 (net +27,130, +31.7%) — resistance shelf starts at the same $249–252 zone
  phase-2 flagged as trapped dark-pool supply `[OI:oi_by_strike]`
- **OPEX cliff = Jun-18** (13 DTE): 172,474 contracts = 20.9% of total OI,
  P/C 1.358 `[OI:term_structure]`; Jun-05 0DTE (P/C **3.199**, 129,886 puts)
  rolled off at Friday's close
- Jan-27 LEAPs are the **call-heavy** pole (92,209c vs 47,459p, P/C 0.515,
  16.9% of OI) — long-horizon bulls persist beneath the near-term bear stack
  `[OI:term_structure]`
- No roll signatures detected (`position-rolls` empty); closing was concentrated
  in expiring 0DTE puts (Jun-05 195P −4,352) `[OI:decrease_with_volume]`

## Detailed findings

### OI walls by strike — all expiries `[OI:oi_by_strike]` (spot ref 227.81)

| Strike | Call OI | Put OI | Net OI | Role | Dist % |
|---|---|---|---|---|---|
| 200 | 29,726 | 23,238 | +6,488 | call_heavy (battleground) | −12.2 |
| 150 | 16,644 | 19,177 | −2,533 | put_wall_support | −34.1 |
| 250 | 25,916 | 4,193 | +21,723 | call_wall_resistance | +9.8 |
| 300 | 27,797 | 667 | +27,130 | call_wall_resistance | +31.7 |
| 210 | 12,598 | 11,999 | +599 | call_heavy (battleground) | −7.8 |
| 170 | 6,040 | 18,106 | −12,066 | put_wall_support | −25.4 |
| 100 | 6,189 | 17,738 | −11,549 | put_wall_support | −56.1 |
| 260 | 19,382 | 2,473 | +16,909 | call_wall_resistance | +14.2 |
| 350 | 21,067 | 112 | +20,955 | call_wall_resistance | +53.7 |
| 220 | 10,008 | 11,143 | −1,135 | put_wall_support | −3.4 |

200 and 210 are two-sided battlegrounds (`call_heavy` by role, near-zero net) —
not clean walls; the clean structures are the 250/260/300 call walls overhead
and the deep put floors 170/150/100.

### OI walls — ≤30 DTE (the map phase-9 sizes against) `[OI:oi_by_strike --dte-max 30]`

| Strike | Call OI | Put OI | Net OI | Role | Dist % |
|---|---|---|---|---|---|
| 200 | 8,564 | 15,617 | −7,053 | put_wall_support | −12.2 |
| 150 | 6,535 | 11,910 | −5,375 | put_wall_support | −34.1 |
| 170 | 2,147 | 15,525 | −13,378 | put_wall_support | −25.4 |
| 205 | 371 | 15,761 | −15,390 | put_wall_support | −10.0 |
| 210 | 2,439 | 11,051 | −8,612 | put_wall_support | −7.8 |
| 220 | 4,235 | 8,932 | −4,697 | put_wall_support | −3.4 |
| 190/185/175/160 | — | 8.8–10.8k each | −5.5k…−10.1k | put_wall_support | −16…−30 |

**Every row is a put wall.** The nearest is 220 (−3.4%); the heaviest block sits
200–205 (~31.4k puts). In dealer-positioning terms (if customers are net long
these puts) the zone under 220 is where short-gamma hedging pressure could
accelerate moves; the 200–205 shelf is the consensus downside target.

### OI term structure `[OI:term_structure]` (total_oi 825,120; 17 expiries)

| Expiry | DTE | Call OI | Put OI | P/C | % of total |
|---|---|---|---|---|---|
| **2026-06-18** | 13 | 73,137 | 99,337 | **1.358** | **20.90 ← OPEX cliff** |
| 2026-06-05 | 0 | 40,605 | 129,886 | 3.199 | 20.66 (expired at close) |
| 2027-01-15 | 224 | 92,209 | 47,459 | 0.515 | 16.93 |
| 2026-06-12 | 7 | 16,254 | 48,691 | 2.996 | 7.87 |
| 2026-07-17 | 42 | 34,556 | 23,532 | 0.681 | 7.04 |
| 2026-09-18 | 105 | 23,540 | 30,167 | 1.282 | 6.51 |
| 2028-01-21 | 595 | 41,769 | 2,446 | 0.059 | 5.36 |

Near-dated expiries (≤13 DTE) are put-skewed (P/C 3.0–3.2 weekly); the LEAP pole
is overwhelmingly call-skewed. Note total_oi here (825,120) is the post-0DTE
denominator context for Monday; phase-1's deep-dive block reported 1,117,357
total OI including intraday-built lines.

### Largest OI increases `[OI:biggest_increases]` (expiry/side parsed from OPRA `option_symbol`)

| Contract | OI Δ | Vol | Read |
|---|---|---|---|
| Jun-12 205P | **+6,871** | 9,202 | fresh bearish line (ask-biased +692) |
| Jun-18 200P | +3,555 | 4,390 | bearish, ask 521 vs bid 104 |
| Jun-12 202.5P | +2,500 | 2,546 | bearish, ask 2,458 vs bid 88 — near-pure buy |
| Jun-12 200P | +1,458 | 2,116 | bearish |
| Jun-12 125P | +1,152 | 1,218 | tail hedge (phase-1's lottery-put cohort) |
| Sep-18 350C | +1,037 | 1,158 | bullish far-OTM, ask-biased +617 |
| Jul-17 280C / 400C | +710/+622 | 859/908 | bid-biased — call *writing* |
| Jan-27 210C | +549 | 2,051 | bid-biased −555 (prev prem $21.95M — the deep-ITM complex) |

### Closing / roll activity

- `decrease-with-volume`: dominated by the expiring Jun-05 strip (195P −4,352
  on 8,983 vol; 230P −656; 127P −539) — 0DTE close-outs, not thesis changes
  `[OI:decrease_with_volume]`
- `position-rolls` (threshold 500, near-DTE ≤30): **empty** — the Thursday tape
  had no detectable roll pairs; Friday's 285P calendar (phase-1) is a same-day
  structure invisible to this OI diff `[OI:position_rolls]`

### Pin risk / OPEX concentration

- `pin-risk` top-25 (≤7 DTE, ≤5% from strike): **no NBIS rows** `[OI:pin_risk]`
- `opex-concentration` top-20 (≥40%): **no NBIS rows** — 20.9% Jun-18
  concentration is meaningful but below screen threshold `[OI:opex_concentration]`

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw oi biggest-increases --symbol NBIS --top-n 20 --min-oi-change 500 --date 2026-06-05 --json` | 205P +6,871 ← `.results[0].oi_diff_plain` | 17 rows |
| `uw oi decrease-with-volume --symbol NBIS --top-n 15 --min-volume 100 --date 2026-06-05 --json` | Jun-05 195P −4,352 ← `.results[0].oi_diff_plain` | top-15 |
| `uw oi smart-positioning --symbol NBIS --top-n 20 --min-oi-change 500 --date 2026-06-05 --json` | 205P bearish net_ask_bid +692; stock_price 227.73 ← `.results[].{inferred_direction,net_ask_bid}` | 17 rows |
| `uw oi position-rolls --symbol NBIS --threshold 500 --near-dte-max 30 --date 2026-06-05 --json` | `[]` | 0 |
| `uw oi oi-by-strike --symbol NBIS --top-n 10 --date 2026-06-05 --json` | tables above ← `.results[].{strike,call_oi,put_oi,net_oi,role,distance_pct}` | top-10 |
| `uw oi oi-by-strike --symbol NBIS --top-n 10 --dte-max 30 --date 2026-06-05 --json` | all-put-wall table ← same paths | top-10 |
| `uw oi term-structure --symbol NBIS --date 2026-06-05 --json` | Jun-18 20.9%, P/C 1.358 ← `.term_structure[] \| {expiry,pct_of_total_oi,put_call_oi_ratio}`; total_oi 825,120 ← `.total_oi` | 17 expiries |
| `uw oi pin-risk --top-n 25 --dte-max 7 --max-distance-pct 5 --date 2026-06-05 --json` | no NBIS ← ticker filter | top-25 |
| `uw oi opex-concentration --top-n 20 --min-concentration-pct 40 --date 2026-06-05 --json` | no NBIS ← ticker filter | top-20 |

## Tool errors

- `uw oi term-structure … | jq '.results'` → `jq: error … Cannot iterate over
  null` — this command returns `.term_structure`, not `.results`. Schema
  inspected (`keys`), re-ran with the correct path; no values were transcribed
  from the failed parse.

## DATA NOTE / CORRECTION

- OI updates overnight: the 2026-06-05 changes file reflects **Thursday 06-04**
  position changes. Friday's headline trades (Jun-26 285P write, 285P calendar)
  will only hit OI in the 06-08 file — outside this as-of window. Phase 9 must
  treat the 285P-write read as *flow-inferred, OI-unconfirmed*.

## Verdict for downstream phases

- **Positioning bias:** **puts being built** — short-dated OTM puts (200–205,
  Jun-12/Jun-18) opened aggressively pre-slide and now in profit; near-term
  chain put-dominated at every top strike; partially offset by a persistent
  call-heavy LEAP pole (Jan-27 P/C 0.515).
- **Conviction:** 3/5
- **Largest OI build as % of float:** Jun-12 205P +6,871 contracts ≈ 687,100
  share-equiv ≈ **0.34% of float** (201.04M, phase-0) `[OI:oi_pct_float fz]` —
  individually modest; the aggregate fresh 200–205 put stack (~14.4k contracts
  ≈ 0.72% of float) is structurally meaningful for a 22%-short-float name.
- **Three pin/cliff strikes for phase-9:**
  1. **220 put wall** (nearest support, −3.4%, 8,932 puts ≤30 DTE) — first line;
     also phase-2's AH low zone $220.7.
  2. **200–205 put shelf** (31,378 puts ≤30 DTE, −10…−12%) — the bears' target
     and the heaviest near-term gravity below.
  3. **250 call wall** (+9.8%, net +21,723) — coincides with phase-2's $249.5–251.7
     trapped-supply cluster; cap on any bounce. OPEX cliff: **Jun-18** (20.9% of
     OI) — positioning resets in 13 days.
- **Open questions:** Is the 200–205 put stack outright bearish or protective
  against long stock (22% short float cuts both ways — phase-7c)? Does Friday's
  285P write survive in Monday OI (unverifiable as-of)? Where does max-pain sit
  for Jun-18 (phase-4)?
