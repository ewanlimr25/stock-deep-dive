# Phase 3 — Open Interest & Positioning

**Ticker:** ENVX
**As-of date:** 2026-06-26
**Generated:** 2026-06-27T14:47:39Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md

## Summary

ENVX's chain is **structurally call-owned but far-dated and slow** — net call OI is
positive at virtually every strike, and OI is concentrated in long expiries: the
**Jan-2027 LEAP holds 33.3% of all OI, July-2026 monthly OPEX 26.8%, and the Oct-2026
sweep expiry 18.4%** — all overwhelmingly calls (July P/C 0.135). The tradeable-horizon
wall map puts the next real overhead resistance at the **$7 call wall** (net +15,308 OI,
17% OTM), with the **$6 ATM strike a near-balanced battleground** (dte≤30 call 6,413 /
put 5,205, net only +1,208) rather than a clean wall. Crucially, **no fresh OI build ≥500
registered today** (`biggest-increases`, `smart-positioning`, `position-rolls` all empty)
— OI updates after the close, so phase-1's 6,738-contract $6-Oct sweep (≈0.36% of float
in share-equiv) **will land in tomorrow's OI**, roughly doubling the $6/Oct call line.
Positioning bias is **bullish-structural but unconfirmed in today's registered OI**;
the directional build is still the phase-1 sweep, not yet visible here.

## Key signals

- **$7 call wall = first real resistance**: net_oi +15,308 (all-exp), +4,476 (dte≤30),
  17.35% OTM `[OI:oi_by_strike]` — the upside target/ceiling for the $6-call thesis.
- **$6 ATM is a battleground, not a wall**: dte≤30 call 6,413 / put 5,205, net +1,208,
  0.59% from spot `[OI:oi_by_strike]` — role tag "call_wall_resistance" but net_oi is
  small; two-sided. Today's sweep will tilt it.
- **OPEX cliff = 2026-07-17** (26.77% of total OI, ~21 DTE, call-skewed P/C 0.135);
  the gravity well is **the Jan-2027 LEAP (33.31%)** `[OI:term_structure]` — much of the
  bullish OI is long-dated, slow-moving.
- **No OI build ≥500 today** — `biggest-increases`/`smart-positioning`/`position-rolls`
  all 0 rows `[OI:biggest_increases, smart_positioning, position_rolls]`. Decreases are
  trivial (0DTE $7/$7.5 put closes, $10 call trims) `[OI:decrease_with_volume]`.
- ENVX **outside** market-wide `pin-risk` and `opex-concentration` lists `[OI:pin_risk,
  opex_concentration]` — not in OPEX week (monthly was 06-19), OI not ≥40%-concentrated
  in one near expiry.

## Detailed findings

### OI walls by strike — `[OI:oi_by_strike]`

**Tradeable horizon (dte ≤ 30 — expires by ~2026-07-26):**

| Strike | call_oi | put_oi | net_oi | role | dist% |
|--------|---------|--------|--------|------|-------|
| $6 | 6,413 | 5,205 | +1,208 | call_wall_resistance* | +0.59% |
| $6.5 | 351 | 1,246 | −895 | put_heavy | +8.97% |
| $7 | 7,720 | 3,244 | +4,476 | call_wall_resistance | +17.35% |
| $7.5 | 5,165 | 869 | +4,296 | call_wall_resistance | +25.73% |
| $8 | 15,481 | 956 | +14,525 | call_wall_resistance | +34.12% |
| $9 | 10,585 | 470 | +10,115 | call_wall_resistance | +50.88% |
| $10 | 13,877 | 4 | +13,873 | call_wall_resistance | +67.64% |
| $5.5 | 181 | 562 | −381 | put_wall_support | −7.80% |

*$6 is tagged a wall but `net_oi` is only +1,208 — a **two-sided battleground**, not clean
resistance (per the role caveat). **All-expiry** adds far LEAP walls: $10 (net +45,475),
$15 (+26,728), $12 (+13,721) — structural, not near-term tradeable.

Read: overhead call OI is real but **stacked OTM** ($7→$8→$10). The first meaningful
ceiling above spot is **$7** (17% away). Below spot only a thin **$5.5 put support**.

### OI term structure (OPEX cliffs) — `[OI:term_structure]` (total_oi 219,319)

| Expiry | call_oi | put_oi | % of total OI | note |
|--------|---------|--------|---------------|------|
| **2027-01-15** | 58,673 | 14,372 | **33.31%** | LEAP gravity well (structural) |
| **2026-07-17** | 51,750 | 6,966 | **26.77%** | near-term OPEX cliff (~21 DTE), P/C 0.135 |
| 2026-10-16 | 39,690 | 713 | 18.42% | phase-1 sweep expiry (≈pure calls) |
| 2028-01-21 | 24,778 | 0 | 11.30% | far LEAP |
| 2026-06-26 | 4,400 | 2,091 | 2.96% | today 0DTE — negligible, no pin |
| (7 more) | — | — | <2.4% each | — |

The near-term cliff is **2026-07-17** — cross-check vs phase-4 max-pain and phase-6
catalysts (earnings ~2026-07-30 per phase-0.5, *after* this OPEX). The $6-Oct sweep adds
to the 18.42% Oct bucket.

### Largest OI increases / closing / rolls — `[OI:biggest_increases, decrease_with_volume, position_rolls]`

**No increases ≥500 contracts and no rolls today.** Decreases are minor and mostly
0DTE put unwinds: $7.5P −338 (vol 894), $7P −261 (vol 895), plus small $10C trims
(Jan-27 −47, Oct-16 −44) and $11P Jul-17 −25. Nothing structural closing.

### Smart positioning / Pin risk / OPEX concentration

- `smart-positioning` ≥500: **0 rows** — no inferred directional build registered today.
- `pin-risk` (dte≤7, ≤5% from spot): **ENVX absent** — not OPEX week; 0DTE OI only 2.96%.
- `opex-concentration` (≥40%): **ENVX absent** — max single-expiry share is 33% (LEAP).

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|------------------|--------------------------|-----------|
| `uw oi oi-by-strike --symbol ENVX --top-n 10 --dte-max 30 --date 2026-06-26` | $7 wall net +4,476; $6 net +1,208 ← `.results[].net_oi,.role,.distance_pct` | 10 |
| `uw oi oi-by-strike --symbol ENVX --top-n 10 --date 2026-06-26` | $10 LEAP wall net +45,475 ← `.results[]` | 10 |
| `uw oi term-structure --symbol ENVX --date 2026-06-26` | Jul-17 26.77%, Jan-27 33.31% ← `.term_structure[].pct_of_total_oi`; total_oi 219,319 | 11 exp |
| `uw oi biggest-increases --symbol ENVX --top-n 20 --min-oi-change 500 --date 2026-06-26` | 0 rows ← `.results\|length` | 0 |
| `uw oi smart-positioning --symbol ENVX --top-n 20 --min-oi-change 500 --date 2026-06-26` | 0 rows | 0 |
| `uw oi position-rolls --symbol ENVX --threshold 500 --near-dte-max 30 --date 2026-06-26` | 0 rows | 0 |
| `uw oi decrease-with-volume --symbol ENVX --top-n 15 --min-volume 100 --date 2026-06-26` | $7.5P −338 ← `.results[].oi_diff_plain` | 6 |
| `uw oi pin-risk --top-n 25 --dte-max 7 --max-distance-pct 5 --date 2026-06-26` | ENVX absent ← `select(.ticker=="ENVX")` | 0 (of 25) |
| `uw oi opex-concentration --top-n 20 --min-concentration-pct 40 --date 2026-06-26` | ENVX absent | 0 (of 20) |

## Tool errors

<none — all reads round-tripped through jq>

## DATA NOTE / CORRECTION

- `uw oi term-structure` returns an object (`.term_structure[]`), not a top-level array;
  first `jq` on `.results` mis-typed it. Re-read against `.term_structure` (schema
  confirmed) — values above are from the corrected path. No number transcribed from a
  failed read.

## Verdict for downstream phases

- **Positioning bias:** **bullish-structural but far-dated and unconfirmed today.** The
  chain is call-owned everywhere, but the weight is in the Jan-27 LEAP (33%) and July OPEX
  (27%); the fresh directional build (phase-1 $6-Oct sweep) **has not yet hit OI** — it
  registers tomorrow. **Conviction 3/5.**
- **Largest OI build as % of float:** today's registered build is **n/a (<500 ct, 0 rows)**;
  the *pending* build is the phase-1 $6-Oct sweep ≈ **0.357% of float** (673,800 sh-equiv),
  which nearly doubles the $6/Oct call line — structural for this 188.93M float. `[OI:oi_pct_float fz]`
- **Three pin/cliff strikes for phase-9:**
  1. **$6 (ATM, +0.59%)** — battleground/decision line; sweep building here; net_oi +1,208 (two-sided).
  2. **$7 (call wall, +17.35%, net +15,308)** — first real overhead resistance AND the upside
     target zone for the $6-call thesis; phase-2's $6.28–6.33 DP supply sits just under it.
  3. **2026-07-17 OPEX cliff** (26.77% of OI) as the near-term gravity well; **$5.5 put_wall_support
     (−7.80%)** as the only structural downside level.
- **Open questions:** Is the call OI speculative or covered/short-hedged? (26% short float — some
  OTM calls may be short-sellers' upside hedges, not bulls — phase-7c/8b). Will tomorrow's OI
  confirm the $6-Oct build, or was today's sweep a single actor? Does max-pain (phase-4) align
  the July cliff with a pin near $6?
