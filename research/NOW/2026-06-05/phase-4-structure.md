# Phase 4 — Dealer Structure & Gamma

**Ticker:** NOW
**As-of date:** 2026-06-05
**Generated:** 2026-06-06T12:26:00-04:00
**Upstream phases cited:** phase-0.5-context.md, phase-1-flow.md, phase-3-positioning.md

## Summary

Dealers are **net long gamma (regime POSITIVE, total_gex +$6,878,457) with
spot 112.53 only ~2.5% above the zero-gamma level 109.7** — a thin cushion:
below ~110 the book flips short-gamma exactly where phase-3 found no put
wall until 100/90. Skew is **inverted/COMPLACENT** (25Δ put 63.9% vs call
71.4%) — no panic put bid despite the −17% week — while the front end is in
**BACKWARDATION** (7d/26d ratio 1.104). OPEX gravity is split: 6/12 max
pain at 120 (above), but the 6/18 cliff expiry (20.9% of OI,
phase-3-positioning.md) pins at **108, −3.9% below spot**.

## Key signals

- **ZGL 109.7 vs spot 112.53** — `regime=POSITIVE`, "Dealers net long gamma —
  expect mean-reversion and reduced volatility" (verbatim), but the
  flip level is just −2.5% away [STRUCT:gex].
- **At-spot negative gamma pocket**: strike 112 carries the largest
  per-strike GEX at **−$5,325,467** (113/117/119 also negative); positive
  shelves at 110 (+$3.51M), 125 (+$2.41M), 130 (+$4.23M) [STRUCT:gex
  per_strike] — locally unstable at spot inside a globally long-gamma book.
- **DEX: public net call-long** — call_dex +$1,345,153,943 vs put_dex
  −$1,044,401,979, net +$300,751,964; tool verbatim: "Public is net
  call-long → dealers net short calls → dealer hedge is to BUY underlying"
  [STRUCT:dex].
- **Vanna is IV-directional**: net_vanna −2,297 (call-heavy book) — verbatim:
  "Falling IV → call delta drops → dealers (short calls) cut long-underlying
  hedge → SELLING pressure. Rising IV reverses." net_charm +183,791
  [STRUCT:vanna_charm]. With iv_rank 79 (phase-0.5), **vol compression would
  mechanically sell the stock** — unusual and worth phase-9's attention.
- **Skew COMPLACENT / inverted**: 25Δ put IV 0.6393 < 25Δ call IV 0.7142
  (skew −0.0748, ratio 0.895, dte_actual 26) [STRUCT:term_skew] — calls
  richer than puts after a −6% day; bounce-chasing, not tail-hedging.
- **Front-end BACKWARDATION**: near (6 DTE) IV 0.7482 vs far (26 DTE) 0.6775,
  ratio 1.104 [STRUCT:front_end_iv_ratio] — near-term stress priced without
  an imminent earnings event (next earnings 2026-07-22, phase-0.5).

## Detailed findings

### GEX

[STRUCT:gex --dte-max 45] `total_gex` +6,878,457; `zero_gamma_level` 109.7;
`underlying_price` 112.53; `regime` POSITIVE. Top strikes by |net_gex|:

| Strike | net_gex | Sign |
|---|---|---|
| 112 | −5,325,466 | short-γ at spot |
| 130 | +4,225,472 | long-γ shelf |
| 110 | +3,506,502 | long-γ shelf |
| 125 | +2,407,413 | long-γ |
| 100 | +1,144,933 | long-γ |
| 120 | +1,136,358 | long-γ |
| 113 | −1,083,780 | short-γ |
| 106 | +956,109 | long-γ |
| 119 | −882,872 | short-γ |
| 117 | −828,581 | short-γ |

Aggregate below spot (<112): −$2.97M; at/above spot (≥112): +$9.54M. The
negative pocket spans 112–119 (the week's markdown path, phase-2's overhead
supply zone) — rallies into 117–120 meet short-gamma chop then the 120/125/130
long-γ + call-wall cap (phase-3-positioning.md §Walls).

### DEX

[STRUCT:dex --dte-max 45] call_dex +$1.345B, put_dex −$1.044B, **net_dex
+$300.75M** (spot 112.53). Tool interpretation verbatim: dealers net short
calls → their hedge is long stock. Charm decay of that call book into 6/18
OPEX bleeds the hedge off (dealer selling pressure as OTM call deltas decay)
— consistent with the max-pain-below-spot pull.

### Vanna + charm

[STRUCT:vanna_charm --dte-max 45] net_vanna −2,297 (call_vanna −10,269 /
put_vanna +7,972), net_charm +183,791. Verbatim interpretation quoted in Key
signals. **No vanna-squeeze setup**: the classic squeeze needs positive
vanna + falling IV; here falling IV produces dealer *selling*. The
mechanical bid only appears if IV *rises* while the call book persists.

### IV term structure

[STRUCT:iv_term_structure] `structure=CONTANGO` (label verbatim; kink_expiry
null, 17 expiries). Row cross-check (avg_iv_pct): 6/12 **74.8%**, 6/18
**75.6%**, 6/26 71.2%, 7/2 67.7%, 7/10 **66.5%** (trough), 7/17 68.2%, 7/24
70.6%, 8/21 **72.0%**, 9/18 71.2%, 11/20 67.8%. Shape: front hump
(stress) → ~35-DTE trough → post-earnings (7/22) bump in 7/24+/8/21. The
CONTANGO label averages away the front hump that `front_end_iv_ratio`
correctly flags as BACKWARDATION — both quoted; the actionable read is the
hump+trough+earnings-bump shape.

### Term skew

[STRUCT:term_skew --dte-target 30] `interpretation=COMPLACENT` (verbatim);
put_25d_iv 0.6393, call_25d_iv 0.7142, skew −0.0748, skew_ratio 0.895,
dte_actual 26. Inverted skew post-selloff = the put side is supplied
(phase-1's put-writing campaign [FLOW:aggressor_ex0dte DUCKDB]) while calls
are bid for bounce — crowd leaning long the rebound.

### Front-end IV ratio

[STRUCT:front_end_iv_ratio --near-dte 7 --far-dte 30] near_iv 0.7482 (6
DTE), far_iv 0.6775 (26 DTE), ratio 1.104, `regime=BACKWARDATION`. No
earnings inside the window (7/22 is 47 days out) — the stress is the
selloff itself, not an event premium.

### Today's gamma flip

Skipped — `today-gamma-flip` is 0DTE/intraday-only and this is an as-of
(T+1, after-hours) run; noted per phase instructions, no call made.

### Max pain

[STRUCT:max_pain --dte-max 30] spot 112.39. Caveat verbatim: "Single-day OI
snapshot. Max pain assumes settlement at each candidate strike…" (static-OI
estimate — softer the further out):

| Expiry | DTE | Max pain | Dist % | P/C OI | Total OI |
|---|---|---|---|---|---|
| 2026-06-05 | 0 | 120 | +6.77 | 0.587 | 128,160 |
| 2026-06-12 | 7 | **120** | **+6.77** | 0.541 | 60,366 |
| **2026-06-18** | 13 | **108** | **−3.91** | 0.604 | 275,475 |
| 2026-06-26 | 21 | 110 | −2.13 | 1.200 | 34,147 |
| 2026-07-02 | 27 | 117 | +4.10 | 1.233 | 11,623 |

Cross-check vs phase-3: 6/18 = the 20.9% term-structure cliff; its 108
magnet sits between the 110 two-sided strike and the 100 shelf — chain
gravity into monthly OPEX is **down −3.9%**, while the small 6/12 weekly
pulls up toward 120. Near-expiry (6/12) magnet: 120; tradeable-gravity
conflict resolves 6/12→6/18.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw options-structure gex --symbol NOW --dte-max 45 --date 2026-06-05 --json` | ZGL 109.7 / +6,878,457 / POSITIVE ← `.zero_gamma_level, .total_gex, .regime`; strikes ← `.per_strike[].net_gex` | 50 strikes |
| `uw options-structure dex --symbol NOW --dte-max 45 --date 2026-06-05 --json` | net_dex +300,751,964 ← `.net_dex` | aggregate |
| `uw options-structure vanna-charm --symbol NOW --dte-max 45 --date 2026-06-05 --json` | net_vanna −2,297 / net_charm +183,791 ← `.net_vanna, .net_charm` | aggregate |
| `uw options-structure iv-term-structure --symbol NOW --date 2026-06-05 --json` | CONTANGO ← `.structure`; curve ← `.term_structure[].avg_iv_pct` | 17 expiries |
| `uw options-structure term-skew --symbol NOW --dte-target 30 --date 2026-06-05 --json` | COMPLACENT / 0.895 ← `.interpretation, .skew_ratio` | 1 |
| `uw options-structure front-end-iv-ratio --symbol NOW --near-dte 7 --far-dte 30 --date 2026-06-05 --json` | BACKWARDATION / 1.104 ← `.regime, .ratio` | 1 |
| `uw options-structure max-pain --symbol NOW --dte-max 30 --date 2026-06-05 --json` | 6/18 → 108 (−3.91%) ← `.results[].max_pain_strike, .distance_pct` | 5 expiries |

## Tool errors

(none — `today-gamma-flip` intentionally skipped as intraday-only)

## DATA NOTE / CORRECTION

First GEX/IV-term extractions assumed field names `.gex` and `.atm_iv`; the
actual fields are `.net_gex` and `.avg_iv`/`.avg_iv_pct` (jq errored on
nulls — caught by the JSON-validity gate, no value transcribed). Re-extracted
from the saved JSON with correct paths; tables above reflect the verified
reads. The 0DTE row's 11.1% avg_iv is an expiry-day artifact, excluded from
the curve read.

## Verdict for downstream phases

- **Dealer regime:** **long-gamma but transitional** — POSITIVE total GEX
  with ZGL only 2.5% below spot, a −$5.3M short-γ pocket at the spot strike,
  and the heaviest OPEX expiry pulling toward 108.
- **Conviction:** 3 / 5
- **Structural levels for phase-9:**
  1. **ZGL 109.7** (treat as ±2% band ≈ 107.5–112) — below it dealers flip
     short-gamma into the phase-3 no-put-wall air pocket toward 100.
  2. **Largest GEX strikes: 112 (−$5.3M) at spot; 130 (+$4.2M) / 110
     (+$3.5M)** — 110 is the long-γ shelf that should slow the first test;
     120–130 caps rallies (with phase-3's call walls).
  3. **Max-pain magnets: 6/12 → 120 (+6.8%), 6/18 cliff → 108 (−3.9%)** —
     gravity rotates downward after the 6/12 weekly rolls off.
- **Open questions:** Does realized vol justify 75% front IV (phase-5 VRP)?
  If IV compresses from rank 79, vanna says dealers sell — does that cap any
  relief bounce? Is the COMPLACENT skew a contrarian red flag given the
  macro tape (phase 6)?
