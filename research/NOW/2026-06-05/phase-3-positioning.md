# Phase 3 — Open Interest & Positioning

**Ticker:** NOW
**As-of date:** 2026-06-05
**Generated:** 2026-06-06T12:18:00-04:00
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md, phase-1-flow.md, phase-2-dark-pool.md

> **OI timing caveat (applies to every number below):** OI updates after the
> close — this snapshot is start-of-day 2026-06-05 OI, i.e. it reflects
> positioning through the **2026-06-04 session**, before the −6% as-of-day
> selloff phase-1 documented. The 6/5 prints (the $20.7M 135P 7/17 bid block,
> the $7.25M 110P 8/21 ask buys — phase-1-flow.md §Sweeps) **cannot be
> confirmed or refuted in OI yet**; their OI impact lands in the next
> session's snapshot.

## Summary

Pre-selloff positioning is **two-sided premium selling under a call-heavy
ceiling**: the largest OI builds were calls at 123–135 (June) and 130–140
(July) tagged bearish (bid-side = overwriting/selling) plus near-dated puts
at 113–119 sold bullish (put-writing) [OI:smart_positioning]. The structural
map shows **call walls stacked at 120/125/130 overhead and no put-wall
support until 100/90 (−11% / −20%)** — within 30 DTE the downside is
structurally open [OI:oi_by_strike]. The 2026-06-18 monthly OPEX is the OI
gravity well (**20.9% of total 1,317,402 OI**, P/C 0.60)
[OI:term_structure]. No rolls detected; NOW absent from market-wide pin-risk
and OPEX-concentration lists.

## Key signals

- **Call wall at 120** (+6.77% from spot 112.39): 56,478 call OI vs 36,620
  put, net +19,858, `role=call_wall_resistance` (all-expiry); still the
  nearest meaningful wall at 30-DTE (net +4,675) [OI:oi_by_strike].
- **No near-term put support above 100**: 30-DTE put walls sit at 75
  (−33.3%, 20,359 put OI) and 90 (−19.9%, 13,907); the 100 strike is
  `call_heavy` two-sided (16,385c/13,438p) — dealers have little long-put
  inventory to defend the 105–110 zone [OI:oi_by_strike --dte-max 30].
- **OPEX cliff 2026-06-18 = 20.9% of all OI** (171,789 calls / 103,686 puts,
  P/C 0.60), with 130C 6/18 the single biggest near line (13,237 OI, +565 on
  the day) [OI:term_structure, OI:biggest_increases].
- **OI builds were premium SALES, not bets**: of the 19 biggest increases,
  the call builds (125C/123C 6/5, 135C/123C/130C 6/18, 130C/140C 7/17) carry
  `inferred_direction=bearish` (net bid), and the big put builds (119P 6/5,
  113P 6/12, 88P 6/12) carry `inferred_direction=bullish` (net bid = sold)
  [OI:smart_positioning] — corroborates phase-1's both-wings-net-sold read
  [FLOW:aggressor_ex0dte DUCKDB].
- **Upside-bet capitulation in the decreases**: 135C 6/26 −445, 180C 7/17
  −336, 135C 6/5 −298, 121C 6/5 −188 — far-OTM call lines unwinding after
  the ~−17% markdown week (phase-2-dark-pool.md §Price levels)
  [OI:decrease_with_volume].

## Detailed findings

### OI walls by strike — all-expiry aggregate (spot 112.39)

[OI:oi_by_strike] top-10 by total OI:

| Strike | Call OI | Put OI | Net OI | Role | Dist % |
|---|---|---|---|---|---|
| 150 | 76,105 | 2,175 | +73,930 | call_wall_resistance | +33.5 |
| 120 | 56,478 | 36,620 | +19,858 | call_wall_resistance | **+6.8** |
| 100 | 51,613 | 58,909 | −7,296 | put_wall_support | −11.0 |
| 140 | 53,438 | 7,245 | +46,193 | call_wall_resistance | +24.6 |
| 130 | 51,469 | 5,554 | +45,915 | call_wall_resistance | +15.7 |
| 90 | 15,869 | 47,250 | −31,381 | put_wall_support | −19.9 |
| 110 | 36,131 | 28,307 | +7,824 | call_heavy (two-sided) | **−2.1** |
| 125 | 35,635 | 14,679 | +20,956 | call_wall_resistance | +11.2 |
| 135 | 28,938 | 17,294 | +11,644 | call_wall_resistance | +20.1 |
| 105 | 24,164 | 19,651 | +4,513 | call_heavy (two-sided) | −6.6 |

### OI walls — 30-DTE tradeable horizon (what phase-9 sizes against)

[OI:oi_by_strike --dte-max 30]:

| Strike | Call OI | Put OI | Net OI | Role | Dist % |
|---|---|---|---|---|---|
| 140 | 27,131 | 251 | +26,880 | call_wall_resistance | +24.6 |
| 150 | 25,347 | 96 | +25,251 | call_wall_resistance | +33.5 |
| 130 | 23,827 | 3,011 | +20,816 | call_wall_resistance | +15.7 |
| 120 | 21,157 | 16,482 | +4,675 | call_wall_resistance | +6.8 |
| 125 | 17,421 | 6,681 | +10,740 | call_wall_resistance | +11.2 |
| 100 | 16,385 | 13,438 | +2,947 | call_heavy (two-sided) | −11.0 |
| 110 | 14,226 | 7,657 | +6,569 | call_heavy (two-sided) | −2.1 |
| 115 | 9,089 | 9,061 | **+28** | tagged call_wall, really a **battleground** | +2.3 |
| 75 | 0 | 20,359 | −20,359 | put_wall_support | −33.3 |
| 90 | 3,021 | 13,907 | −10,886 | put_wall_support | −19.9 |

Read: resistance ladder every 5 points from 115/120 up; genuine near-term
put support only at 90/75. The 115 strike (net +28) is dead-even two-sided —
expect chop there, not a wall.

### OI term structure

[OI:term_structure] `total_oi` 1,317,402 across 17 expiries. Cliff = 6/18:

| Expiry | DTE | Call OI | Put OI | P/C | % of total |
|---|---|---|---|---|---|
| **2026-06-18** | 13 | 171,789 | 103,686 | 0.60 | **20.9** |
| 2027-01-15 | 224 | 112,106 | 65,702 | 0.59 | 13.5 |
| 2026-07-17 | 42 | 80,396 | 60,859 | 0.76 | 10.7 |
| 2026-08-21 | 77 | 64,411 | 64,091 | **1.00** | 9.8 |
| 2026-06-05 (0DTE, rolls off) | 0 | 80,768 | 47,392 | 0.59 | 9.7 |
| 2028-01-21 | 595 | 63,006 | 15,873 | 0.25 | 6.0 |
| 2026-09-18 | 105 | 50,334 | 27,724 | 0.55 | 5.9 |
| 2026-11-20 | 168 | 15,959 | 23,899 | 1.50 | 3.0 |

June OPEX is call-heavy (P/C 0.60) — overhead OI, not downside hedges.
**Aug-21 is the put-balanced expiry (P/C 1.00)** — and it is where phase-1's
fresh $7.25M ask-side 110P buying went; Nov-20 (P/C 1.50) is the only
put-dominated tenor. LEAP Jan-28 P/C 0.25 echoes phase-1's call-heavy LEAP
tape [FLOW:dte_bucket DUCKDB].

### Largest OI increases (built during 6/4 session)

[OI:biggest_increases] 19 rows ≥500. Parsed from `option_symbol` (OPRA):

| Contract | OI Δ | curr OI | ratio | Vol |
|---|---|---|---|---|
| 125C 06/05 (0DTE) | +1,853 | 6,745 | 0.38 | 13,935 |
| 119P 06/05 (0DTE) | +1,372 | 2,880 | 0.91 | 2,260 |
| 135C 06/18 | +1,248 | 5,425 | 0.30 | 2,815 |
| 175C 06/12 | +1,157 | 1,226 | **16.77×** | 1,204 |
| 123C 06/05 | +1,128 | 1,758 | 1.79 | 5,378 |
| 117P 06/12 | +1,016 | 1,130 | 8.91× | 1,055 |
| 113P 06/12 | +1,007 | 1,097 | 11.19× | 1,046 |
| 123C 06/18 | +950 | 950 | new line | 1,128 |
| 130C 07/17 | +911 | 7,666 | 0.13 | 2,640 |
| 125P 01/15/27 | +830 | 2,985 | 0.39 | 1,379 |
| 140C 07/17 | +737 | 4,743 | 0.18 | 1,780 |
| 88P 06/12 | +676 | 816 | 4.83× | 695 |
| 110P 09/18 | +504 | 2,133 | 0.31 | 508 |

The 175C 6/12 (+1,157, 16.8× ratio, ~56% OTM after the selloff) is a
lottery/structure artifact positioned pre-collapse — flag, don't trade off
it.

### Closing / roll activity

[OI:decrease_with_volume] top decreases: 135C 6/26 −445, 150C 6/5 −388,
180C 7/17 −336, 135C 6/5 −298, **100P 9/18 −262**, 135P 6/5 −223, 125P 6/5
−218, 80P 9/18 −188, 121C 6/5 −188, 120P 6/5 −179, 135C 8/21 −173. Pattern:
far-OTM call hopes unwinding + some deep Sep put profit-taking. No
roll signature: `uw oi position-rolls` → `rolls_detected` empty (n=0)
[OI:position_rolls].

### Pin risk / OPEX concentration

NOW absent from market-wide `pin-risk` top-25 (dte_max 7) and
`opex-concentration` top-20 (min 40%) [OI:pin_risk, OI:opex_concentration] —
no single-expiry pin setup; OI is distributed (largest expiry only 20.9%).

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw oi biggest-increases --symbol NOW --top-n 20 --min-oi-change 500 --date 2026-06-05 --json` | +1,853 125C 6/5 ← `.results[0].oi_diff_plain/.option_symbol` | 19 rows |
| `uw oi decrease-with-volume --symbol NOW --top-n 15 --min-volume 100 --date 2026-06-05 --json` | 135C 6/26 −445 ← `.results[0].oi_diff_plain` | 15 rows |
| `uw oi smart-positioning --symbol NOW --top-n 20 --min-oi-change 500 --date 2026-06-05 --json` | bearish call-builds / bullish put-builds ← `.results[].inferred_direction` | 19 rows |
| `uw oi position-rolls --symbol NOW --threshold 500 --near-dte-max 30 --date 2026-06-05 --json` | no rolls ← `.results` = [] | 0 rows |
| `uw oi pin-risk --top-n 25 --dte-max 7 --max-distance-pct 5 --date 2026-06-05 --json` | NOW absent ← ticker filter → [] | top-25 |
| `uw oi opex-concentration --top-n 20 --min-concentration-pct 40 --date 2026-06-05 --json` | NOW absent ← ticker filter → [] | top-20 |
| `uw oi oi-by-strike --symbol NOW --top-n 10 --date 2026-06-05 --json` | spot 112.39; 120 net +19,858 role call_wall ← `.spot, .results[]` | top-10 strikes |
| `uw oi oi-by-strike --symbol NOW --top-n 10 --dte-max 30 --date 2026-06-05 --json` | 115 net +28; put walls 75/90 ← `.results[]` | top-10 strikes |
| `uw oi term-structure --symbol NOW --date 2026-06-05 --json` | 6/18 pct 20.9 / P/C 0.60; total 1,317,402 ← `.term_structure[], .total_oi` | 17 expiries |

## Tool errors

(none)

## DATA NOTE / CORRECTION

(none — all values round-tripped `jq` on first read)

## Verdict for downstream phases

- **Positioning bias:** **premium-selling, structurally capped** — call OI
  being written overhead (123–140), near puts written below; not a
  directional accumulation. Downside structurally open to 100/90 on the
  wall map; upside capped at 120 then every 5 points.
- **Conviction:** 3 / 5 (the wall map and term structure are structural
  facts, not probabilistic classifications)
- **Largest OI build as % of float:** +1,853 contracts ≈ 185,300 share-equiv
  ≈ **0.018% of the 1.02B float** [OI:oi_pct_float fz] — nothing here is a
  structural position for this name; advisory only.
- **Three pin/cliff strikes for phase-9:**
  1. **120** — `call_wall_resistance` +6.8% (all-expiry net +19,858; 30-DTE
     net +4,675): first upside cap / short-entry reference.
  2. **2026-06-18 OPEX** — the 20.9%-of-OI cliff (P/C 0.60), 130C its
     biggest line (13,237): gravity + theta decay zone into 6/18; phase-4
     must cross-check max-pain for this expiry.
  3. **100 then 90** — first real downside OI shelves (−11% / −19.9%);
     between spot and 100 there is no put wall (115 is a dead-even
     battleground, net +28).
- **Open questions:** Did 6/5's 135P 7/17 $20.7M bid block CLOSE existing OI
  (the 7/17 put line held 60,859 as of this snapshot) or OPEN a put-write?
  → unresolvable until the next OI snapshot; phase-9 must carry this as an
  explicit unknown. Is the 6/18 call-heavy OI (P/C 0.60) overhead supply
  that pins any bounce below 120 into OPEX?
