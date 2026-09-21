# Phase 3 — Open Interest & Positioning

**Ticker:** PATH
**As-of date:** 2026-06-05
**Generated:** 2026-06-06T10:35:00-04:00
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md, phase-1-flow.md, phase-2-dark-pool.md

## Summary

The chain is being **overwritten, not chased**: the three largest fresh OI
builds are all *bid-dominant call selling above spot* (Aug-21 $12C +3,379 with
net_ask_bid −1,557; Jan-27 $20C +1,603 with −890; Jun-12 $13.5C +601 with
−697), while the single biggest position change is a **−9,049 close of the
Jun-18 $11P** with only ~11.6% rolled out — post-earnings downside hedges
lifted. Net structure: a put-supported floor at $10–$11, a call-wall ceiling
at $12–$13, and the chain's gravity well in the Jan-2027 LEAPs (32.93% of all
OI). This corroborates phase-2's overhead-supply map and tempers phase-1's
mildly-bullish read: holders are renting out upside, not paying for it.

## Key signals

- **Aug-21 $12C OI +3,379 (+72.8%)** on 5,430 vol, but prev-day flow was
  bid-dominant (ask 1,446 vs bid 3,003, net −1,557) → `inferred_direction:
  bearish` = **call writing** [OI:biggest_increases][OI:smart_positioning]
- **Jun-18 $11P OI −9,049** on just 226 vol; position-rolls: near_oi_change
  −8,801, far_oi_change +1,018, balance_ratio 0.116 → **hedge taken OFF, not
  rolled** [OI:decrease_with_volume][OI:position_rolls]
- ≤30DTE walls: **put_wall_support $11 (net_oi −12,197, −2.1% from spot)**;
  call walls $12 (+13,105, +6.8%) and $13 (+23,495, +15.7%)
  [OI:oi_by_strike]
- **OPEX cliffs:** Jan-2027 holds **32.93%** of total OI (165,837C/72,934P,
  P/C 0.44); near-term cliff = **Jun-18 at 15.9%** (85,022C/30,277P, P/C
  0.356, 13 DTE) [OI:term_structure]
- Jan-27 $20C +1,603 and Jan-28 $37C −427 — LEAP-tier overwriting being
  built/recycled, structural not directional [OI:biggest_increases]

## Detailed findings

### OI walls by strike (`oi-by-strike`, all-expiry aggregate)

| strike | call_oi | put_oi | net_oi | role | dist % |
|---|---|---|---|---|---|
| 15 | 87,398 | 9,184 | +78,214 | call_wall_resistance | +33.5 |
| 20 | 58,975 | 2 | +58,973 | call_wall_resistance | +78.0 |
| 12 | 54,982 | 9,945 | +45,037 | call_wall_resistance | +6.8 |
| 13 | 41,526 | 16,298 | +25,228 | call_wall_resistance | +15.7 |
| 10 | 33,406 | 50,022 | −16,616 | put_wall_support | −11.0 |
| 11 | 21,059 | 25,374 | −4,315 | put_wall_support | −2.1 |
| 8 | 6,977 | 38,727 | −31,750 | put_wall_support | −28.8 |

Caveat: strike 11 is a **two-sided battleground** (21.1k calls vs 25.4k puts,
net only −4,315), not a clean wall; $10 is the cleaner support (net −16,616).

### Tradeable-horizon walls (≤30DTE)

| strike | call_oi | put_oi | net_oi | role | dist % |
|---|---|---|---|---|---|
| 13 | 24,509 | 1,014 | +23,495 | call_wall_resistance | +15.7 |
| 15 | 23,448 | 4 | +23,444 | call_wall_resistance | +33.5 |
| 12 | 17,546 | 4,441 | +13,105 | call_wall_resistance | +6.8 |
| 11 | 5,715 | 17,912 | **−12,197** | put_wall_support | −2.1 |
| 10 | 5,809 | 14,566 | −8,757 | put_wall_support | −11.0 |

Near-term implied range: **$11 floor / $12–$13 ceiling** (spot 11.235 per
`smart-positioning .stock_price`).

### OI term structure (cliff lens)

Total OI 724,984 across 15 expiries [OI:term_structure]:

| expiry | dte | call_oi | put_oi | P/C | % of total OI |
|---|---|---|---|---|---|
| **2027-01-15** | 224 | 165,837 | 72,934 | 0.44 | **32.93** |
| **2026-06-18** | 13 | 85,022 | 30,277 | 0.356 | **15.90** |
| 2026-08-21 | 77 | 66,761 | 15,827 | 0.237 | 11.39 |
| 2026-06-05 (expired today) | 0 | 52,931 | 19,309 | 0.365 | 9.96 |
| 2028-01-21 | 595 | 58,264 | 4,128 | 0.071 | 8.61 |

Sep-18 (phase-1's buy tenor) holds only 6.52% (24,333C/22,970P — P/C 0.944,
the chain's most *balanced* expiry). The near-term gravity well is **Jun-18**
— cross-check phase-4 max-pain against it. ~10% of chain OI expired today.

### Largest OI increases (Δ = `oi_diff_plain`; side/expiry parsed from OPRA symbol)

| contract | OI Δ | Δ ratio | vol | smart-positioning read |
|---|---|---|---|---|
| Aug-21 2026 $12 C | +3,379 | +72.8% | 5,430 | net_ask_bid −1,557 → **sold/write** |
| Jan-15 2027 $20 C | +1,603 | +5.4% | 2,383 | net_ask_bid −890 → sold/write |
| Jun-05 2026 $12 C | +886 | +24.5% | 3,979 | net_ask_bid +637 → bought (0DTE, expired worthless — spot 11.235) |
| Jun-12 2026 $13.5 C | +601 | +67.8% | 892 | net_ask_bid −697 → sold/write |

**OI lag caveat:** these builds convert *prior-session (06-04)* volume
(`prev_total_premium` Aug $12C = $847,872 refers to 06-04 flow). Phase-1's
Sep $10C/$15C buys (06-05) cannot appear in OI until the next session's file
— phase-1's conversion question stays open.

### Closing / roll activity

Decreases led by **Jun-18 $11P −9,049** (vol 226). Position-rolls confirms a
put roll: near −8,801 / far +1,018, `balance_ratio 0.116`, roll_size 1,018 —
i.e. **~89% of the near-dated $11 put position was simply closed**, only ~1k
re-established farther out. Post-earnings protection unwound. Minor closes:
Jan-28 $37C −427, Aug $20C −166, Jun-18 $15C −65.

### Pin risk / OPEX concentration

No PATH rows in market-wide `pin-risk` top-25 (dte≤7, ≤5% from spot) or
`opex-concentration` top-20 (min 40% — PATH's max single-expiry share is
32.93%, below threshold; consistent). No pin commentary warranted.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw oi biggest-increases --symbol PATH --top-n 20 --min-oi-change 500 --date 2026-06-05 --json` | Aug $12C +3,379 ← `.results[].oi_diff_plain` | 4 |
| `uw oi decrease-with-volume --symbol PATH --top-n 15 --min-volume 100 --date 2026-06-05 --json` | Jun-18 $11P −9,049 ← `.results[0].oi_diff_plain` | 15 |
| `uw oi smart-positioning --symbol PATH --top-n 20 --min-oi-change 500 --date 2026-06-05 --json` | net_ask_bid −1,557 / inferred bearish ← `.results[]{net_ask_bid,inferred_direction}` | 4 |
| `uw oi position-rolls --symbol PATH --threshold 500 --near-dte-max 30 --date 2026-06-05 --json` | put roll balance_ratio 0.116 ← `.results[0]` | 1 |
| `uw oi pin-risk --top-n 25 --dte-max 7 --max-distance-pct 5 --date 2026-06-05 --json` | no PATH ← ticker filter | top-25 |
| `uw oi opex-concentration --top-n 20 --min-concentration-pct 40 --date 2026-06-05 --json` | no PATH ← ticker filter | top-20 |
| `uw oi oi-by-strike --symbol PATH --top-n 10 [--dte-max 30] --date 2026-06-05 --json` | $11 net −12,197 ≤30DTE ← `.results[]{net_oi,role}` | 10 ×2 |
| `uw oi term-structure --symbol PATH --date 2026-06-05 --json` | Jan-27 32.93% ← `.term_structure[] \| sort_by(-.pct_of_total_oi)` | 15 expiries |

## Tool errors

None fatal. First `term-structure` jq used `.results[]` (null — tool returns
`.term_structure[]`); no values were transcribed from the failed parse; re-ran
with the correct path (see DATA NOTE).

## DATA NOTE / CORRECTION

- `term-structure` shape: rows live under `.term_structure[]` with metadata
  keys `{expiry_count, source, symbol, total_oi}` — corrected before any value
  was read. All quoted cliff numbers re-verified against
  `.term_structure[] | sort_by(-.pct_of_total_oi)`.

## Verdict for downstream phases

- **Positioning bias:** **calls being written / hedges lifted** — income
  positioning inside an expected $11–$13 range; not directional accumulation
  (tempers phase-1's mild bullish read)
- **Conviction:** 3/5 (clean, mutually consistent OI signals)
- **Largest OI build as % of float:** Aug $12C +3,379 ≈ 337,900 share-equiv =
  **0.082% of float** (412.34M, phase-0) — not structural for this name
  [OI:oi_pct_float fz]
- **Three pin/cliff strikes for phase-9:**
  1. **$11** — ≤30DTE put_wall_support (net_oi −12,197, −2.1% from spot); $10
     the cleaner deep support (all-expiry net −16,616)
  2. **$12** — first call_wall_resistance (≤30DTE net +13,105, +6.8%); $13
     behind it (+23,495)
  3. **Jun-18 OPEX** — near-term cliff (15.9% of chain OI) → phase-4 max-pain
     cross-check; Jan-2027 the structural well (32.93%)
- **Open questions:** Did 06-05's Sep $10C/$15C buys convert to OI (next
  session's file)? Is the Aug $12C writing covered (against the phase-2 DP
  buys) or naked overwriting — phase-4 GEX/skew may hint?
