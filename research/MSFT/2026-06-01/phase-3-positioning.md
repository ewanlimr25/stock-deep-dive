# Phase 3 — Open Interest & Positioning

**Ticker:** MSFT
**As-of date:** 2026-06-01
**Generated:** 2026-06-02T11:03:36Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md

## Summary

The MSFT chain is **structurally call-dominated, but today's *new* positioning is
split ~50/50 between call buying and call writing** — so the bullish call tape
(phase-1) is half speculation, half premium-selling, not clean accumulation. New
OI builds are **100% calls** (495C, 455C, 440C, 520C/800C LEAPs), yet
`smart-positioning` infers **bullish 56,078 OI vs bearish 55,182 OI** — and the
single largest build, **495C +19,995 (essentially all-new)**, is inferred **call
*writing*** (bid-side). Near-term (≤30 DTE) the wall map gives upside resistance
at **470 (+2.1%), 480 (+4.25%), 500 (+8.6%)** and **only one put-wall support, at
400 (−13%)** — the downside is structurally under-hedged. The OPEX gravity well
is **2026-06-18 (17.78% of all OI)**; the chain also carries huge call-heavy
**Dec-18 / Jan-15 LEAPs** (long-term bullish structural positioning). Largest
build is **0.027% of float** — immaterial for sizing conviction.

## Key signals

- **New OI builds are all calls but ~half are written:** smart-positioning
  bullish 56,078 vs bearish 55,182 OI; biggest build **495C +19,995 inferred
  bearish (writing)** `[OI:smart_positioning]` `[OI:biggest_increases]`.
- **Near-term call walls (≤30 DTE): 470 / 480 / 500** = upside resistance/magnets,
  matching phase-1's 470–500 call buying `[OI:oi_by_strike]`.
- **Sole put-wall support = 400 (−13%)** (net_oi −15,681 ≤30 DTE); no near-spot
  put cushion — bullish positioning, but fragile to a drop `[OI:oi_by_strike]`.
- **OPEX cliff = 2026-06-18, 17.78% of total OI** (3.66M); secondary Dec-18 LEAP
  15.82% (call/put 483k/96k, P/C 0.20 — very call-heavy) `[OI:term_structure]`.
- **480C June-OPEX closing −23,718 on 52,497 vol**, with new 495C/06-26 builds →
  **roll-up/out** signature (calls migrating higher & later) `[OI:decrease_with_volume]`.

## Detailed findings

### OI walls by strike (`oi-by-strike`) `[OI:oi_by_strike]`

**Near-term tradeable horizon (≤30 DTE)** — spot $459.77:

| Strike | call_oi | put_oi | net_oi | role | dist |
|--------|---------|--------|--------|------|------|
| 470 | 41,710 | 834 | +40,876 | **call_wall_resistance** | +2.08% |
| 480 | 59,140 | 385 | +58,755 | **call_wall_resistance** | +4.25% |
| 500 | 35,031 | 37 | +34,994 | **call_wall_resistance** | +8.60% |
| 455 | 31,000 | 1,626 | +29,374 | call_heavy | −1.18% |
| 450 | 66,169 | 8,588 | +57,581 | call_heavy | −2.26% |
| 440 | 51,759 | 6,886 | +44,873 | call_heavy | −4.44% |
| 435 | 34,402 | 4,453 | +29,949 | call_heavy | −5.52% |
| 420 | 35,543 | 20,231 | +15,312 | call_heavy | −8.78% |
| 400 | 11,112 | 26,793 | **−15,681** | **put_wall_support** | −13.12% |

All-expiry adds far walls at **575 (+24.9%)** and **625 (+35.8%)** (LEAP call
strikes). Read: the chain is net-long-call at *every* strike from 420 up; the only
strike where puts dominate is **400**. Resistance is clean (470/480/500); support
is weak (the 450/440 "call_heavy" strikes are battlegrounds, not put support).

### OI term structure (`term-structure`) `[OI:term_structure]`

total_oi 3,663,593 across 24 expiries. P/C derived from call/put OI:

| Expiry | call_oi | put_oi | P/C | % of total OI |
|--------|---------|--------|-----|---------------|
| **2026-06-18** (June OPEX) | 421,043 | 230,377 | 0.55 | **17.78%** ← cliff |
| 2026-12-18 (LEAP) | 483,122 | 96,348 | 0.20 | 15.82% |
| 2027-01-15 (LEAP) | 313,360 | 126,085 | 0.40 | 11.99% |
| 2026-07-17 | 263,869 | 109,822 | 0.42 | 10.20% |
| 2026-09-18 | 152,399 | 108,913 | 0.71 | 7.13% |
| 2026-08-21 | 151,722 | 84,872 | 0.56 | 6.46% |
| 2026-06-05 (weekly) | 112,895 | 39,921 | 0.35 | 4.17% |

The **2026-06-18 monthly is the gravity well** (cross-check phase-4 max-pain &
phase-6 calendar). The Dec/Jan LEAPs are enormous and extremely call-heavy (P/C
0.20–0.40) — structural long-term bullish positioning sitting under the tape.

### Largest OI increases (all calls) `[OI:biggest_increases]`

| Strike | Expiry (dte) | Type | OI Δ | curr_oi | vol | % float |
|--------|--------------|------|------|---------|-----|---------|
| 495 | 06-26 (25) | C | +19,995 | 20,100 | 20,846 | 0.027% |
| 455 | 06-26 (25) | C | +11,643 | 12,762 | 18,988 | 0.016% |
| 520 | ~12-18 (200) | C | +10,137 | 13,158 | 11,275 | 0.014% |
| 440 | 06-26 (25) | C | +10,043 | 23,655 | 13,852 | 0.014% |
| 800 | ~09-18 (109) | C | +9,098 | 10,889 | 11,402 | 0.012% |
| 470 | 06-05 (4) | C | +7,781 | 14,257 | 31,041 | 0.011% |
| 480 | ~06-12 (11) | C | +7,619 | 8,264 | 19,645 | 0.010% |

100% calls, spanning weeklies (06-05/06-12/06-26) and LEAPs (520 Dec, **800 Sep —
a far-OTM tail bet**). All builds tiny as % of float (≤0.027%).

### Smart positioning — inferred direction `[OI:smart_positioning]`

| Inferred | positions | Σ OI Δ |
|----------|-----------|--------|
| bullish | 12 | 56,078 |
| bearish | 8 | 55,182 |

Near-dead-even. Top builds by direction: **495C/06-26 → bearish (writing)**,
455C/06-26 → bullish, 520C-LEAP → bearish (writing), 440C → bullish, 800C → bullish,
470C/06-05 → bearish. The biggest single build is **call writing**, confirming
phase-1's $208M bid-side call selling — the "bullish" chain is heavily overwritten.

### Closing / roll activity `[OI:decrease_with_volume]` `[OI:position_rolls]`

Top decreases: **480C 06-18 −23,718 (vol 52,497)**, 480C ~08-21 −4,089, 470C 06-18
−3,856, 450C ~08-21 −2,149, 450C ~07-17 −2,126. The 480C-June-OPEX unwind + new
495C/06-26 builds = **roll up-and-out**. `position-rolls` algorithm:
`rolls_detected: 0` (its near→far pairing threshold not met), but the manual read
shows roll-like migration. Note its `caveat` field; treat as "no clean
algorithmic roll, but discretionary roll-up visible."

### Pin risk & OPEX concentration `[OI:pin_risk]` `[OI:opex_concentration]`

- **pin-risk (dte-max 7):** only surfaces the **0DTE (dte_to_opex 0, now expired on
  the as-of date)** — nearest_high_oi_strike 475 at pin_distance 3.17%, weak pin
  (heavy OI sits *above* spot, not on it). The tradeable June-OPEX (06-18) is 18
  days out, outside the 7-day window → **no actionable near-term pin**.
- **opex-concentration (≥40%):** MSFT **absent** — OI is diversified across 24
  expiries (max 17.78% at 06-18), so MSFT is not a concentration/cliff name.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|------------------|--------------------------|-----------|
| `uw oi oi-by-strike --symbol MSFT --top-n 10 --dte-max 30 --date 2026-06-01 --json` | walls 470/480/500 res, 400 sup ← `.results[].role,.net_oi` | 10 |
| `uw oi oi-by-strike --symbol MSFT --top-n 10 --date 2026-06-01 --json` | all-expiry adds 575/625 LEAP walls ← same | 10 |
| `uw oi term-structure --symbol MSFT --date 2026-06-01 --json` | 06-18 = 17.78% cliff ← `.term_structure\|max_by(.pct_of_total_oi)` | 24 expiries |
| `uw oi biggest-increases --symbol MSFT --top-n 20 --min-oi-change 500 --date 2026-06-01 --json` | 495C +19,995 (0.027% float) ← `.results\|sort_by(.oi_diff_plain)`, type from `option_symbol` capture | top-20 |
| `uw oi smart-positioning --symbol MSFT --top-n 20 --min-oi-change 500 --date 2026-06-01 --json` | bull 56,078 / bear 55,182 OI ← `group_by(.inferred_direction)` | 20 |
| `uw oi decrease-with-volume --symbol MSFT --top-n 15 --min-volume 100 --date 2026-06-01 --json` | 480C 06-18 −23,718 ← `.results\|sort_by(.oi_diff_plain)` | 15 |
| `uw oi position-rolls --symbol MSFT --threshold 500 --near-dte-max 30 --date 2026-06-01 --json` | rolls_detected 0 ← `.rolls_detected` | 0 |
| `uw oi pin-risk --top-n 25 --dte-max 7 --max-distance-pct 5 --date 2026-06-01 --json` | MSFT only 0DTE, weak pin 475 ← `map(select(.ticker=="MSFT"))` | 25 |
| `uw oi opex-concentration --top-n 20 --min-concentration-pct 40 --date 2026-06-01 --json` | MSFT absent ← same filter = [] | 20 |

## Tool errors

None — all nine commands returned valid JSON that round-tripped through `jq`.

## DATA NOTE / CORRECTION

None. (Call/put type for `biggest-increases` parsed from `option_symbol` via
`capture("[0-9]{6}(?<cp>[CP])")` per the field-path map, since the rows carry no
`side`/type column; `smart-positioning` supplied a native `option_type_inferred`.)

## Verdict for downstream phases

- **Positioning bias: structurally call-heavy, but new positioning is balanced
  (≈50/50 buy/write).** The long-standing chain is overwhelmingly long-call
  (P/C 0.20–0.55 across expiries, big LEAP call books), but *today's* builds are
  half written → **not clean directional accumulation.** Corroborates phase-1
  (bullish tilt + heavy writing) and phase-2 (mixed/rebalance).
- **Conviction: 3/5** — clean wall structure and persistent call-lean, but the
  bullish signal is diluted by inferred writing and tiny float impact.
- **Largest OI build as % of float: 0.027%** (495C +19,995 ≈ 2.0M sh / 7.31B) —
  immaterial; do not let contract counts inflate conviction.
- **Three pin/cliff strikes for phase-9** (sourced from roles + term-structure):
  1. **2026-06-18 OPEX cliff** (17.78% of OI) — the near-term gravity well; pair
     with phase-4 max-pain.
  2. **470 / 480 call walls** (+2.1% / +4.25%) — first upside resistance/magnet;
     **500 call wall** (+8.6%) the larger ceiling (the 500C Aug flow target).
  3. **400 put wall** (−13%) — sole structural downside support; near-spot the
     **450 call_heavy strike** (confluent with phase-2's $450 DP shelf) is the
     pivot, not true support.
- **Open questions:** Is the call writing dealer-driven (phase-4 GEX: are dealers
  long gamma from all these written calls, pinning price)? Does max-pain (phase-4)
  sit near the 06-18 cliff and the 470/480 walls? Is the 800C/520C LEAP build a
  recurring institutional tail position or new this session?
