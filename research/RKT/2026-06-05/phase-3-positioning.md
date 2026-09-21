# Phase 3 — Open Interest & Positioning

**Ticker:** RKT
**As-of date:** 2026-06-05
**Generated:** 2026-06-06T17:12:00-04:00
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md

## Summary

RKT's chain is **call-dominated at every tenor and capped by a staircase of call
walls directly overhead** ($13.5 → $14 → $14.5 → $15 → $16), while the only
fresh builds are bullish: +2,971 Sep-18 $13C (ask-skewed) and +1,170 Jun-12 $14C.
The OI gravity well is **Sep-18 2026 (27.91% of all OI, P/C 0.127)** with Jun-18
the near-term cliff (23.77%). Below spot ($12.64) there is **no put wall in the
top-10 strikes** — the downside is structurally unsupported, echoing phase-2's
missing DP shelf below $12.65. One standout anomaly: Dec-18 2026 carries P/C
**10.24** (13,307 puts vs 1,299 calls) — a lone long-dated put pocket. The
Jan-2027 $9.2 line shows a paired signature: calls bought (phase-1) while
**9.2P OI fell −407** — synthetic-long/collar-unwind flavor, bullish.

## Key signals

- Largest build: `RKT260918C00013000` (Sep-18 $13C) OI 1,298 → 4,269
  (`oi_diff_plain` **+2,971**), prev ask_volume 2,258 vs bid 1,155 (ask-skewed),
  prev premium $722,649 — inferred **bullish** [OI:biggest_increases +
  smart_positioning]
- Jun-12 $14C +1,170 (473→1,643), ask 811/bid 461 — short-dated upside spec
  [OI:biggest_increases]
- **OPEX cliff = Sep-18 2026**: total_oi 133,355, `pct_of_total_oi` 27.91,
  put_call_oi_ratio 0.127; Jun-18 second at 23.77% (113,579) [OI:term_structure]
- 30D wall map: $16 call wall 32,962C (+26.6%), $15 20,146C (+18.7%), $14.5
  20,045C (+14.7%); $13 put-heavy 13,445P net −11,021 (+2.85%); $14 put-heavy
  14,650P net −6,447 (+10.8%) [OI:oi_by_strike]
- `RKT270115P00009200` OI **−407** on 500 vol @ $0.68 — Jan-27 $9.2 puts closed
  the same line phase-1's $257,910 ask-side call sweep hit (synthetic-long /
  collar-unwind read) [OI:decrease_with_volume; phase-1-flow.md §Sweeps]
- Dec-18 2026: P/C **10.244** (13,307P / 1,299C, 3.06% of OI) — isolated
  long-dated put position [OI:term_structure]
- Jul-10 expiry total OI just **52** — phase-1's 3,460-lot Jul-10 $14.5C sale is
  new; tomorrow's OI print should confirm ~+3,400 [OI:term_structure;
  phase-1-flow.md §Sweeps]

## Detailed findings

### OI walls by strike (`oi-by-strike`, spot $12.64)

**≤30 DTE (the tradeable map phase-9 sizes against):**

| Strike | call_oi | put_oi | net_oi | role | distance_pct |
|---|---|---|---|---|---|
| 16 | 32,962 | 5,580 | +27,382 | call_wall_resistance | +26.58 |
| 15 | 20,146 | 3,890 | +16,256 | call_wall_resistance | +18.67 |
| 14 | 8,203 | 14,650 | **−6,447** | put_heavy (two-sided battleground) | +10.76 |
| 14.5 | 20,045 | 1,752 | +18,293 | call_wall_resistance | +14.72 |
| 17 | 17,932 | 2,072 | +15,860 | call_wall_resistance | +34.49 |
| 13 | 2,424 | 13,445 | **−11,021** | put_heavy | +2.85 |
| 20 | 14,378 | 0 | +14,378 | call_wall_resistance | +58.23 |
| 13.5 | 6,669 | 5,135 | +1,534 | call_wall_resistance (battleground — near-equal two-sided) | +6.80 |
| 18 | 6,912 | 4 | +6,908 | call_wall_resistance | +42.41 |
| 15.5 | 4,803 | 66 | +4,737 | call_wall_resistance | +22.63 |

**All-expiry aggregate** (far-dated LEAP piles dominate): $17 (46,492C),
$18 (43,786C), $15 (36,176C), $16 (34,975C), $20 (38,558C), $13 put-heavy
(29,086P vs 9,656C, net −19,430), $14 battleground (19,100C / 18,682P, net +418),
$23 / $24.2 LEAP call piles (14,048 / 13,222).

**Read:** every top-10 strike sits **above** spot. The nearest structure is the
$13 ITM-put pocket (+2.85%); first true call wall at $13.5–$14, heaviest at
$14.5–$16. **No put-wall support below $12.64 anywhere in the top-10** — if the
stock breaks down, dealer OI offers no shelf.

### OI term structure (`term-structure`, 15 expiries)

| Expiry | DTE | call_oi | put_oi | P/C | % of total OI |
|---|---|---|---|---|---|
| 2026-06-05 | 0 | 38,493 | 8,611 | 0.224 | 9.86 (rolls off today) |
| 2026-06-12 | 7 | 11,400 | 9,316 | 0.817 | 4.34 |
| **2026-06-18** | 13 | 83,242 | 30,337 | 0.364 | **23.77** (near cliff) |
| 2026-06-26 | 21 | 2,561 | 2,162 | 0.844 | 0.99 |
| 2026-07-10 | 35 | 19 | 33 | 1.737 | **0.01** (pre-sale) |
| 2026-07-17 | 42 | 15,191 | 6,938 | 0.457 | 4.63 |
| 2026-08-21 | 77 | 8,923 | 6,969 | 0.781 | 3.33 |
| **2026-09-18** | 105 | 118,348 | 15,007 | **0.127** | **27.91** (gravity well) |
| **2026-12-18** | 196 | 1,299 | 13,307 | **10.244** | 3.06 (lone put pocket) |
| 2027-01-15 | 224 | 69,316 | 8,972 | 0.129 | 16.39 |
| 2028-01-21 | 595 | 16,842 | 0 | 0.000 | 3.53 |

Call OI concentration at Sep-18/Jan-27/Jun-18 (68% of all OI, P/C ≤ 0.36) is a
structural long-call complex; the Dec-18 put pocket is the only downside-skewed
tenor. Cross-check Sep-18 against phase-4 max-pain and phase-6 catalysts
(earnings 2026-07-30 lands before the Sep cliff).

### Largest OI increases (all 3 rows ≥ min-oi-change 500; side/expiry parsed from `option_symbol`)

| option_symbol | Expiry | Type | Strike | OI Δ (`oi_diff_plain`) | curr_oi | prev ask/bid vol | Read |
|---|---|---|---|---|---|---|---|
| RKT260918C00013000 | 2026-09-18 | C | 13 | **+2,971** | 4,269 | 2,258 / 1,155 | bought, bullish, 105 DTE |
| RKT260612C00014000 | 2026-06-12 | C | 14 | +1,170 | 1,643 | 811 / 461 | bought, 7 DTE spec |
| RKT260605C00014000 | 2026-06-05 | C | 14 | +586 | 1,561 | 444 / 341 | 0DTE, expired worthless (close $12.65) — noise |

### Closing / roll activity

`position-rolls`: **0 rows** (no near→far roll ≥500 detected).
`decrease-with-volume` highlights (ex-0DTE-expiry noise):

| Chain | OI Δ | vol | Note |
|---|---|---|---|
| RKT270115P00009200 (Jan-27 $9.2P) | **−407** | 500 | closed @ avg $0.68 — pairs with phase-1's 9.2C ask-sweep → synthetic-long/collar-unwind |
| RKT260618C00013500 | −162 | 806 | trimming at the 13.5 wall |
| RKT260612P00013000 | −130 | 189 | |
| RKT260618C00014000 | −98 | 309 | |
| RKT260821P00013000 | −84 | 110 | |
| RKT260618P00014000 | −18 | 367 | OI 10,247 — big ITM put line barely moved |

0DTE expiry-day churn (Jun-5 14P −423, 17.5P −400, 12.5C −246) ignored.

### Smart positioning

All 3 qualifying rows inferred **bullish** (calls, positive `net_ask_bid`:
+1,103 Sep $13C, +350 Jun-12 $14C, +103 0DTE $14C). One-sided but small sample
(n=3); OPRA parsing spot-checked against `option_symbol` — strikes/expiries
consistent.

### Pin risk

`pin-risk --dte-max 7 --max-distance-pct 5` top-25: **no RKT** (board is
SPY/HYG/TLT/IWM/QQQ…). Weekly Jun-12 is 7 DTE but RKT doesn't rank; monthly OPEX
Jun-18 is 13 days out — outside the pin window. No pin commentary warranted.

### OPEX concentration

`opex-concentration --min-concentration-pct 40` top-20: **no RKT** (board is
micro-cap names). RKT's 27.91% Sep concentration is below the 40% screen — noted,
not an OI cliff by this tool's bar.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw oi biggest-increases --symbol RKT --top-n 20 --min-oi-change 500 --date 2026-06-05 --json` | +2,971 ← `.results[0].oi_diff_plain` | 3 |
| `uw oi decrease-with-volume --symbol RKT --top-n 15 --min-volume 100 --date 2026-06-05 --json` | −407 9.2P ← `.results[1]` | 15 |
| `uw oi smart-positioning --symbol RKT --top-n 20 --min-oi-change 500 --date 2026-06-05 --json` | 3× bullish ← `.results[].inferred_direction` | 3 |
| `uw oi position-rolls --symbol RKT --threshold 500 --near-dte-max 30 --date 2026-06-05 --json` | 0 rows ← `.results\|length` | 0 |
| `uw oi pin-risk --top-n 25 --dte-max 7 --max-distance-pct 5 --date 2026-06-05 --json` | no RKT ← ticker filter | 0 |
| `uw oi opex-concentration --top-n 20 --min-concentration-pct 40 --date 2026-06-05 --json` | no RKT ← ticker filter | 0 |
| `uw oi oi-by-strike --symbol RKT --top-n 10 [--dte-max 30] --date 2026-06-05 --json` | walls ← `.results[]` | 10 + 10 |
| `uw oi term-structure --symbol RKT --date 2026-06-05 --json` | cliff ← `.term_structure[]` (NOT `.results` — see DATA NOTE) | 15 |

## Tool errors

None fatal. First `jq` pass on `term-structure` assumed a `.results` envelope and
errored (`jq: error … Cannot iterate over null`); raw output inspection showed the
payload key is **`.term_structure`** (with `expiry_count`, `source`, `symbol`
siblings). Re-ran with the correct path; no value was transcribed from the failed
parse.

## DATA NOTE / CORRECTION

`term-structure` envelope: values quoted from the corrected
`.term_structure[]` read (validated JSON round-trip). Nothing else re-read.

## Verdict for downstream phases

- **Positioning bias:** calls being built (all 3 qualifying builds bullish
  call-side; Jan-27 9.2 synthetic-long signature), but inside a chain whose
  existing structure is a **call-wall staircase overhead** and **no put support
  below spot** — net read: positioning is bullish-leaning medium-term, with
  upside mechanically resistant and downside unprotected.
- **Conviction:** 3/5 (builds are clean and one-directional but small;
  +2,971 contracts = the day's only structural print)
- **Largest OI build as % of float:** Sep-18 $13C +2,971 contracts ≈ 297,100
  share-equivalent = **0.031% of 960.91M float** [OI:oi_pct_float fz] — not
  structural for this name; a tactical institutional bet, not a stake.
- **Three pin/cliff strikes for phase 9** (from `oi-by-strike` roles +
  `term-structure` cliff):
  1. **$13.0** — nearest structure, put_heavy net −11,021 (30D), +2.85% from
     spot; ITM-put pocket = friction zone, not support.
  2. **$14.5** — call_wall_resistance net +18,293 (30D) and phase-1's fresh
     3,460-lot short-call line: the defined upside cap.
  3. **$16.0** — heaviest 30D call wall (net +27,382); Sep-18 (27.91% of OI,
     P/C 0.127) is the term cliff that anchors the medium-term magnet zone.
- **Open questions:** Is the Sep-18 call complex speculative or covered
  (covered-call writing against phase-2 stock holdings would flip its meaning)?
  Who owns the Dec-18 put pocket and does it map to a catalyst (phase-6)?
  Does GEX/max-pain (phase-4) put the dealer magnet at/below $13?
