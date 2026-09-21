# Phase 3 — Open Interest & Positioning

**Ticker:** PATH
**As-of date:** 2026-08-12
**Generated:** 2026-08-13T01:55:00Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md

## Summary

PATH's structural OI book is heavily **call-skewed** — every near/mid-term
expiry in the term structure carries a put/call OI ratio well under 1.0, and
the tradeable-horizon (`--dte-max 30`) strike map shows a dense ladder of
call-wall resistance stacking up just above spot ($16/$16.50/$17/$18) with
essentially no near-term put support. But **today's actual OI change is a
broad call unwind**: 11 of the 15 largest OI decreases are calls
(−4,048 contracts total) against only 4 put decreases (−982 contracts),
coinciding with today's −2.93% price drop after the run-up phase-2 documented.
Read together: a structurally bullish/covered-call-heavy book is being
partially unwound on today's pullback, not fresh bearish conviction being
built — the 4 "biggest increases" rows are small and directionally mixed (2
bullish/2 bearish per the tool's own `inferred_direction`). Conviction stays
low; this phase doesn't add directional edge.

## Key signals

- Term structure: **2027-01-15 expiry holds 38.44% of total OI** (239,592 of
  623,255 contracts) — the OPEX gravity well, P/C=0.603 [OI:term_structure]
- Near-term (≤30 DTE) resistance ladder: $16 (+5.06%), $16.50 (+8.34%), $17
  (+11.62%), $18 (+18.19%) — all `call_wall_resistance` [OI:oi_by_strike]
- Today's OI change: **calls −4,048 contracts (11 rows) vs. puts −982 (4
  rows)** — broad call unwind on the down day [OI:decrease_with_volume]
- `biggest-increases` top 4 are small and mixed: 2 `inferred_direction=bullish`
  (net oi_diff 1,276) vs 2 `bearish` (net oi_diff 1,379) [OI:smart_positioning]
- PATH absent from market-wide `pin-risk` (top-25, ≤7 DTE) and
  `opex-concentration` (top-20, ≥40%) — not a pin/gamma-risk name this week
  [OI:pin_risk, OI:opex_concentration]

## Detailed findings

### OI walls by strike (`--dte-max 30`, spot $15.23)

| Strike | Call OI | Put OI | Net OI | Role | Distance from spot |
|---|---|---|---|---|---|
| $9 | 282 | 7,145 | −6,863 | put_wall_support | −40.91% |
| $11 | 6,171 | 5,157 | +1,014 | call_heavy (thin net) | −27.77% |
| $12 | 9,337 | 4,431 | +4,906 | call_heavy | −21.21% |
| $13 | 7,809 | 639 | +7,170 | call_heavy | −14.64% |
| $14 | 11,806 | 5,594 | +6,212 | call_heavy | −8.08% |
| **$15 (ATM)** | 19,404 | 1,727 | +17,677 | call_heavy | −1.51% |
| $16 | 4,791 | 699 | +4,092 | **call_wall_resistance** | +5.06% |
| $16.50 | 8,263 | 5 | +8,258 | **call_wall_resistance** | +8.34% |
| $17 | 5,291 | 193 | +5,098 | **call_wall_resistance** | +11.62% |
| $18 | 22,592 | 0 | +22,592 | **call_wall_resistance** (largest in window) | +18.19% |

Reading `net_oi` alongside `role` per this phase's own pitfall note: the $11
strike is technically tagged `call_heavy` but its net_oi (+1,014) is thin
relative to its ~11,300 total OI — a genuine two-sided battleground, not a
clean wall. The only real put-side structure is $9, a deep 41%-OTM insurance
level, not a near-term support. **There is no meaningful put wall between spot
and $9** — downside in the tradeable window is unsupported by OI structure.

### OI term structure (OPEX cliff)

`uw oi term-structure` (`total_oi=623,255` across 15 expiries):

| Expiry | DTE | % of total OI | Call OI | Put OI | P/C ratio |
|---|---|---|---|---|---|
| **2027-01-15** | 156 | **38.44%** | 149,454 | 90,138 | 0.603 |
| 2026-08-21 | 9 | 15.87% | 78,951 | 19,966 | 0.253 |
| 2026-09-18 | 37 | 12.44% | 59,164 | 18,382 | 0.311 |
| 2028-01-21 | 527 | 11.28% | 60,131 | 10,152 | 0.169 |
| 2026-12-18 | 128 | 6.04% | 34,818 | 2,805 | 0.081 |
| 2026-11-20 | 100 | 3.58% | 18,608 | 3,683 | 0.198 |
| 2026-08-14 | 2 | 4.51% | 19,495 | 8,641 | 0.443 |
| 2028-12-15 | 856 | 0.62% | 907 | 2,965 | **3.269** |

The **2027-01-15 January-standard expiry is the clear OPEX gravity well**
(38.44% of all OI, call-heavy) — but at 156 DTE it's a structural/LEAP-adjacent
holding, not a near-term pin candidate. Every expiry inside 6 months is
call-skewed (P/C 0.08–0.60) **except** the far-dated 2028-12-15 chain
(P/C=3.269, put-heavy) — this is the same chain phase-1 flagged as the
dominant (and two-sided) recent sweep activity, but it holds only **0.62% of
total OI** ($3,872 contracts) — the flow there is fresh/small relative to the
whole book, consistent with position-building or churn rather than a large
existing structural bet.

### Largest OI increases

`uw oi biggest-increases --min-oi-change 500` (only 4 rows clear the
threshold):

| Contract | DTE | OI Δ | Curr OI | Avg price | Inferred direction |
|---|---|---|---|---|---|
| PATH260814C00017000 ($17C, 8/14) | 2 | +785 | 1,810 | $0.072 | bearish (call-selling on bid) |
| PATH260918P00016000 ($16P, 9/18) | 37 | +759 | 974 | $1.753 | bullish (put-selling on bid) |
| PATH280121C00037000 ($37C, 1/21/28) | 527 | +594 | 5,530 | $1.825 | bearish (call-selling on bid) |
| PATH261120P00015000 ($15P, 11/20) | 100 | +517 | 724 | $1.902 | bullish (put-selling on bid) |

All four rows show `net_ask_bid` negative (prior-session bid volume
dominated) — `smart-positioning` classifies bid-side call activity as bearish
and bid-side put activity as bullish, so this splits 2-and-2, net contracts
+1,379 "bearish" vs. +1,276 "bullish" — a wash. None of these are large; the
$37 LEAP call add is a small (594-contract) top-up on an already-large 4,936
base, not a fresh structural bet.

### Closing / roll activity

`uw oi decrease-with-volume` (15 rows, sorted by `oi_diff_plain`): dominated by
**call closes across nearly every near/mid strike and expiry** — Jan 2027 $20C
(−1,348), Jan 2027 $15C (−649), Sep 2026 $13C (−425), Sep 2026 $15C (−418),
Jan 2027 $12C (−295), and six smaller call rows down to −101. Put closes are
minor by comparison: Aug21 $15P (−544), Dec2028 $12P (−224), Jan2027 $12P
(−111), Sep18 $13P (−103). **Aggregate: calls −4,048 vs puts −982.** This
lines up with today's −2.93% price move — holders of calls across the curve
(not one specific strike/expiry) reduced exposure into weakness. No `position-
rolls` were detected (`uw oi position-rolls --threshold 500 --near-dte-max 30`
returned 0 rows) — this reads as outright closing, not a roll to a new strike
or expiry.

### Smart positioning

Covered above with `biggest-increases` — net wash (2 bullish/2 bearish by
contract count), no dominant inferred direction today.

### Pin risk / OPEX concentration

`uw oi pin-risk --dte-max 7 --max-distance-pct 5` (market-wide top-25, 2 days
to Friday 8/14 OPEX): **PATH absent.** `uw oi opex-concentration
--min-concentration-pct 40` (market-wide top-20): **PATH absent.** PATH is not
a gamma-pin risk name this week — consistent with phase-0.5's
`BUSY_NAME_NORMAL_DAY` read and the modest total OI relative to true
pin-risk names (e.g. SPY, top of the pin-risk list, `pin_score=2.13M` vs.
PATH's total book of 623K contracts).

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw oi biggest-increases --symbol PATH --top-n 20 --min-oi-change 500 --date 2026-08-12 --json` | 4 rows ← `.results[]` | 4 |
| `uw oi decrease-with-volume --symbol PATH --top-n 15 --min-volume 100 --date 2026-08-12 --json` | 15 rows; calls_total=−4048 ← `[.results[]\|select(.option_symbol\|test("C[0-9]"))\|.oi_diff_plain]\|add` | 15 |
| `uw oi smart-positioning --symbol PATH --top-n 20 --min-oi-change 500 --date 2026-08-12 --json` | 4 rows ← `.results[]` | 4 |
| `uw oi position-rolls --symbol PATH --threshold 500 --near-dte-max 30 --date 2026-08-12 --json` | 0 rows | 0 |
| `uw oi pin-risk --top-n 25 --dte-max 7 --max-distance-pct 5 --date 2026-08-12 --json` | PATH absent ← `.results[]\|select(.ticker=="PATH")` | 25 |
| `uw oi opex-concentration --top-n 20 --min-concentration-pct 40 --date 2026-08-12 --json` | PATH absent (same filter) | 20 |
| `uw oi oi-by-strike --symbol PATH --top-n 10 --dte-max 30 --date 2026-08-12 --json` | 10 rows ← `.results[]` | 10 |
| `uw oi term-structure --symbol PATH --date 2026-08-12 --json` | `total_oi=623255`, 15-expiry table ← `.term_structure[]` | 15 |

## Tool errors

<none>

## DATA NOTE / CORRECTION

<none — first read stood>

## Verdict for downstream phases

- **Positioning bias:** Structurally call-heavy/bullish-skewed book being
  **partially unwound today** on the pullback — net read is **mixed, leaning
  risk-reduction**, not fresh directional conviction either way.
- **Conviction:** 2/5 (structural call skew is real but old/pre-existing;
  today's actual flow — the only thing that's "new" — is a wash per
  smart-positioning and a call-unwind per decrease-with-volume; capped by
  phase-0.5)
- **Largest OI build as % of float:** 785 contracts (78,500 share-equivalent)
  / 390.80M float = **0.02%** — negligible, non-structural [OI:oi_pct_float fz]
- **Three pin/cliff strikes for phase-9:**
  1. **$16.00** — nearest true call-wall resistance (+5.06% from spot,
     `call_wall_resistance`)
  2. **$18.00** — largest near-term call-wall (+18.19%, 22,592 OI, the
     dominant strike in the ≤30-DTE window)
  3. **2027-01-15 (156 DTE)** — the OPEX gravity well (38.44% of total OI) —
     not a near-term pin, but the level to watch if the position ever gets
     managed/rolled into that date
- **Open questions:** Is today's broad call unwind profit-taking after the
  run-up (benign) or the start of a larger de-risking (bearish continuation)?
  Phase-5's historical/technical read and phase-6's macro/sector context
  should help distinguish. Also: does the $9 put wall (−40.91%, the only real
  put structure) correspond to any prior support level from phase-2's price
  levels, or is it pure tail-hedge positioning unrelated to near-term price
  action?
