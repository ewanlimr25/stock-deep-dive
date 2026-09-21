# Phase 3 — Open Interest & Positioning

**Ticker:** PATH
**As-of date:** 2026-07-13
**Generated:** 2026-07-13T20:24:00-04:00
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md

## Summary

PATH's option chain is **overwhelmingly call-skewed** — total OI 542,012 contracts,
43% of it concentrated in **January-2027 LEAP calls** (162,929 call vs 72,189 put
OI, P/C 0.44) — a structural *recovery/upside* positioning lean typical of a
beaten-down name. Near spot (~$11.87) the nearest resistance is a **$12 call wall
(+1.1%)** then **$12.5 / $13 (+9.5%)**; put support sits far below at **$10 (−15.7%)
and $9 (−24.2%)**. The most telling near-term build is **+2,548 OI at the $13 Jul-17
call printed on the *bid* (smart-positioning tags it bearish)** — consistent with
**covered-call writing against the stock accumulated in phase-2**, which caps
near-term upside around $13 while confirming holders intend to keep the shares.
Conviction 3/5: constructive structural lean, near-term upside overwritten.

## Key signals

- **Jan-2027 LEAP = 43.4% of all OI**, call-heavy (call 162,929 / put 72,189) `[OI:term_structure]` — the chain's gravity well is far-dated upside.
- **$12 call wall at +1.1%** (net_oi +11,954, dte≤60), first overhead resistance `[OI:oi_by_strike]`.
- **$13 Jul-17 call OI +2,548 on the bid** (net_ask_bid −547, smart-positioning "bearish") `[OI:smart_positioning]` — covered-call overwrite against accumulated stock.
- **$18 Jan-2027 call OI +3,742 on the ask** (smart-positioning "bullish", net_ask_bid +630) `[OI:biggest_increases]` — the one genuine new *bullish* structural build.
- **Put support far below spot** — $10 (−15.7%) and $9 (−24.2%) put walls `[OI:oi_by_strike]`; almost no downside OI cushion near current price.
- PATH **absent** from market-wide pin-risk (dte≤7) and opex-concentration (≥40%) lists `[OI:pin_risk / opex_concentration]` — no dealer-pin catalyst.

## Detailed findings

### OI walls by strike (dte ≤ 60, tradeable horizon) `[OI:oi_by_strike]`

| Strike | call_oi | put_oi | net_oi | role | dist_pct |
|--------|---------|--------|--------|------|----------|
| $13 | 23,596 | 954 | +22,642 | call_wall_resistance | +9.5% |
| $18 | 18,306 | 1 | +18,305 | call_wall_resistance | +51.6% |
| $14 | 17,697 | 0 | +17,697 | call_wall_resistance | +17.9% |
| $12 | 16,784 | 4,830 | +11,954 | call_wall_resistance | **+1.1%** |
| $11 | 13,008 | 6,446 | +6,562 | call_heavy (2-sided) | −7.3% |
| $12.5 | 3,519 | 424 | +3,095 | call_wall_resistance | +5.3% |
| $10 | 4,161 | 9,230 | −5,069 | put_wall_support | −15.7% |
| $9 | 593 | 12,119 | −11,526 | put_wall_support | −24.2% |

Nearest overhead: **$12 → $12.5 → $13**. Nearest real support from OI is distant ($10).
$11 is a two-sided battleground (call_heavy but 6,446 puts), not clean support.

### OI term structure (OPEX cliffs) `[OI:term_structure]`

| Expiry | DTE | call_oi | put_oi | P/C | % of total OI |
|--------|-----|---------|--------|-----|---------------|
| **2027-01-15** | 186 | 162,929 | 72,189 | 0.44 | **43.4%** |
| 2026-08-21 | 39 | 72,625 | 20,202 | 0.28 | 17.1% |
| 2026-07-17 | 4 | 46,380 | 15,603 | 0.34 | 11.4% |
| 2028-01-21 | 557 | 46,112 | 12,879 | 0.28 | 10.9% |
| 2026-09-18 | 67 | 33,178 | 11,524 | 0.35 | 8.3% |

The gravity well is the Jan-2027 LEAP (43%, call-skewed). Near-term Jul-17 OPEX (4 DTE) holds 11.4% — a minor cliff, no market-level pin. Every expiry is call-dominant (P/C ≤ 0.44).

### Largest OI increases (OPRA-parsed) & smart positioning

| Contract | Expiry | Type | Strike | OI Δ | Side (net_ask_bid) | Inferred |
|----------|--------|------|--------|------|--------------------|----------|
| PATH270115C00018000 | 2027-01-15 | Call | $18 | +3,742 | ask (+630) | **bullish** LEAP upside bet |
| PATH260717C00013000 | 2026-07-17 | Call | $13 | +2,548 | **bid (−547)** | **bearish → covered-call write** |

### Closing / roll activity

- **Position rolls: none** (0 rows at threshold 500 / near-dte 30).
- Decreases are trivial: −204 at $20 Jan-28 C, −132 at $11 Jul-17 C, etc. No structural unwind.

### Pin risk / OPEX concentration

- PATH not in market-wide pin-risk (dte≤7, ±5%) top-25 nor opex-concentration (≥40%) top-20. Small name — no dealer-pin catalyst into Jul-17 OPEX. Skip pin commentary.

## Tool calls (audit trail)

| Command | Key value(s) ← `jq` path | Rows |
|---------|--------------------------|------|
| `oi oi-by-strike --dte-max 60` | $12 wall +1.1% net +11,954 ← `.results[]|select(.strike==12)` | 10 |
| `oi term-structure` | Jan-27 43.4% OI ← `.term_structure|sort_by(-.pct_of_total_oi)[0]` | 15 exp |
| `oi biggest-increases --min-oi-change 500` | $18 Jan-27 C +3,742 ← `.results[].oi_diff_plain` (OPRA-parsed) | 2 |
| `oi smart-positioning` | $13 Jul-17 C bid, bearish ← `.results[].{net_ask_bid,inferred_direction}` | 2 |
| `oi position-rolls --threshold 500` | none ← len 0 | 0 |
| `oi decrease-with-volume` | trivial closes ← `.results[].oi_diff_plain` | 6 |
| `oi pin-risk` / `oi opex-concentration` | PATH absent ← `select(.ticker=="PATH")` | 0/0 |

## Tool errors

- `term-structure` output is `{term_structure:[…], total_oi, …}`, not a bare array — first jq indexed the wrong path and errored; re-read `.term_structure[]`. All term values above trace to the corrected path.

## DATA NOTE / CORRECTION

- None beyond the term-structure path fix noted above.

## Verdict for downstream

- **Positioning bias:** **structurally bullish / recovery-skewed** (43% of OI in call-heavy Jan-27 LEAPs; $18 LEAP call the only sizeable new ask-side build), but **near-term upside is overwritten** — $13 Jul-17 calls sold on the bid = covered-call writing against the phase-2 accumulated stock. Net: constructive but capped.
- **Conviction:** 3/5.
- **Largest OI build as % of float:** $18 Jan-27 call +3,742 contracts ≈ 374,200 share-equivalents ≈ **~0.1% of float** `[OI:oi_pct_float fz-fallback]` — negligible; the OI build is structural but tiny next to the phase-2 darkpool (~14% of float). Positioning is *not* the size story here.
- **Three pin/cliff strikes for phase-9:**
  1. **$12** — nearest call wall / resistance (+1.1%); overwrite + wall may act as a near-term ceiling/magnet.
  2. **$13** — call wall (+9.5%) + covered-call strike; the near-term upside cap.
  3. **$10** — put wall support (−15.7%); the first structural OI floor below the $11.80 darkpool shelf.
- **Open questions:** Is the $13 call writing dealer/MM or the accumulator overwriting its own new long (income while it waits)? Does phase-4 max-pain sit near $12, reinforcing the wall? Are the Jan-27 LEAP calls the same actor as the phase-2 buyer expressing convex upside?
