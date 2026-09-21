# Phase 3 — Open Interest & Positioning

**Ticker:** PATH (UiPath Inc.)
**As-of date:** 2026-06-01
**Generated:** 2026-06-01T20:18:00-04:00
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md

## Summary

The standing OI chain leans **structurally bullish/long-biased** — a dominant $15 call
wall (93,768 OI, net +66k calls) with call-heavy strikes laddered $13→$20 and the bulk
of OI (37%) parked in long-dated Jan-2027 LEAP calls. But *today's* new positioning is
genuinely **two-sided** and, read with phases 1–2, resolves into a coherent
**collar-shaped institutional long**: accumulate stock (phase-2 +4.6M sh), buy the $13
Sep put as protection (phase-1 $2.31M), **write upside calls at $14** (Jul/Aug, tagged
bearish by smart-positioning = covered-call writing), and **sell downside puts at $9–10**
(tagged bullish = willing to own lower). Net posture is mildly constructive but
**range-capped, not a breakout bet** — every individual build is <0.1% of float, so
there is no single high-conviction directional structure. Upside is gated by the $14→$15
call walls; downside is cushioned by the $11 put wall and the dark-pool $12.86–12.91
shelf.

## Key signals

- **Major call wall $15** — 80,093 call vs 13,675 put OI, net +66,418, role
  `call_wall_resistance`, +14.3% above spot [OI:oi_by_strike]
- **ATM $13 is call-heavy** — 34,084 call vs 1,980 put, net +32,104, −0.9% from spot
  (near-term 20,136 call OI) — battleground/magnet at the money [OI:oi_by_strike]
- **OPEX gravity:** Jan-2027 LEAP = **37.2% of all OI** (call-skewed P/C 0.54); near-term
  cliff = **Jun-18, 15.7%** (P/C 0.48) [OI:term_structure]
- **Two-sided new builds:** covered-call writing $14 Jul/Aug (bearish), put-selling
  $9–10 (bullish), OTM call buys $13/$20, downside put buying $8–9 [OI:smart_positioning]
- Largest build $13.5 Jun-5 call **+4,036 = 0.098% float** — not structural
  [OI:biggest_increases][OI:oi_pct_float fz]
- pin-risk & opex-concentration: **PATH absent** from both → no near-term pin/cliff
  concentration [OI:pin_risk][OI:opex_concentration]

## Detailed findings

### OI walls by strike — all-expiry aggregate (spot $13.12) `[OI:oi_by_strike]`

| Strike | call_oi | put_oi | net_oi | total_oi | role | dist% |
|--------|---------|--------|--------|----------|------|-------|
| **15** | 80,093 | 13,675 | +66,418 | 93,768 | **call_wall_resistance** | +14.3 |
| 10 | 34,715 | 48,111 | −13,396 | 82,826 | put_wall_support | −23.8 |
| 12 | 51,501 | 25,462 | +26,039 | 76,963 | call_heavy | −8.5 |
| 20 | 55,817 | 1,100 | +54,717 | 56,917 | call_wall_resistance | +52.4 (LEAP) |
| 8 | 7,010 | 44,308 | −37,298 | 51,318 | put_wall_support | −39.0 |
| 11 | 23,146 | 26,454 | −3,308 | 49,600 | put_wall_support | −16.2 |
| **13** | 34,084 | 1,980 | +32,104 | 36,064 | call_heavy | −0.9 (ATM) |
| 17 | 27,850 | 4,032 | +23,818 | 31,882 | call_wall_resistance | +29.6 |
| 18 | 28,813 | 59 | +28,754 | 28,872 | call_wall_resistance | +37.2 |

### OI walls — near-term, DTE≤30 (the horizon phase-9 sizes against) `[OI:oi_by_strike]`

| Strike | call_oi | put_oi | net_oi | role | dist% |
|--------|---------|--------|--------|------|-------|
| 11 | 7,664 | 19,614 | −11,950 | **put_wall_support** | −16.2 |
| 13 | 20,136 | 782 | +19,354 | call_heavy (ATM) | −0.9 |
| 12 | 18,375 | 2,656 | +15,719 | call_heavy | −8.5 |
| 15 | 18,213 | 88 | +18,125 | **call_wall_resistance** | +14.3 |
| 14 | 7,306 | 228 | +7,078 | **call_wall_resistance** | +6.7 |
| 13.5 | 5,860 | 94 | +5,766 | call_wall_resistance | +2.9 |
| 9 | 1,313 | 10,259 | −8,946 | put_wall_support | −31.4 |

Near-term resistance ladder: **$13.5 → $14 → $15** (call walls). Near-term support:
**$11** (put wall) then $10/$9. ATM $13 heavily call-skewed.

### OI term structure — OPEX cliffs (total OI 700,166; 14 expiries) `[OI:term_structure]`

| Expiry | DTE | call_oi | put_oi | P/C | % of total OI |
|--------|-----|---------|--------|-----|---------------|
| **2027-01-15** | 228 | 169,330 | 91,150 | 0.54 | **37.2%** (LEAP gravity) |
| **2026-06-18** | 17 | 74,313 | 35,657 | 0.48 | **15.7%** (near-term cliff) |
| 2026-08-21 | 81 | 61,114 | 20,276 | 0.33 | 11.6% |
| 2028-01-21 | 599 | 66,209 | 10,159 | 0.15 | 10.9% (LEAP) |
| 2026-06-05 | 4 | 35,672 | 14,597 | 0.41 | 7.2% (weekly) |
| 2026-09-18 | 109 | 21,019 | 10,852 | 0.52 | 4.6% ← the $13 Sep put lives here |

Long-dated call OI dominates (Jan-2027 + Aug + Jan-2028 all call-skewed) = structural
bullish LEAP base. Near-term tradeable gravity is **Jun-18** (cross-check phase-4
max-pain).

### Largest OI increases (new positions today) `[OI:biggest_increases]`

| Strike | Expiry | Side | OI Δ | Vol | % float |
|--------|--------|------|------|-----|---------|
| 13.5 | 2026-06-05 | Call | +4,036 | 6,654 | 0.098% |
| 20 | 2026-06-18 | Call | +3,239 | 5,038 | 0.079% |
| 9 | 2026-06-18 | Put | +3,238 | 4,021 | 0.079% |
| 13 | 2026-06-05 | Call | +2,916 | 8,466 | 0.071% |
| 10 | 2026-06-05 | Put | +2,252 | 3,758 | 0.055% |
| 14 | 2026-07-17 | Call | +2,177 | 2,984 | 0.053% |
| 14 | 2026-08-21 | Call | +1,973 | 5,179 | 0.048% |

Builds straddle both sides — short-dated OTM calls ($13/$13.5/$14/$20) and downside
puts ($8/$9/$9.5/$10). All <0.1% of float → no single structural directional bet.

### Smart positioning (inferred direction) `[OI:smart_positioning]`

| Strike | Exp | DTE | inferred dir | reading |
|--------|-----|-----|--------------|---------|
| 13.5 | Jun-5 | 4 | bearish | short-dated **call writing** (capping) |
| 14 | Jul-17 | 46 | bearish | **covered-call writing** vs accumulated stock |
| 14 | Aug-21 | 81 | bearish | covered-call writing |
| 9 | Jun-18 | 17 | bullish | **put selling** (willing to own lower) |
| 10 | Jun-5 | 4 | bullish | put selling |
| 8 | Jun-18 | 17 | bullish | put selling |
| 20 / 13 / 12 | — | — | bullish | OTM/ATM call buying |
| 9 | Jun-12 | 11 | bearish | put buying (downside) |

The mix = a **collar/covered-call income structure**, exactly the phase-2-accumulation
+ phase-1-protective-put complement: long stock, capped at $14, floored ~$9–10.

### Closing / rolls `[OI:decrease_with_volume][OI:position_rolls]`

Decreases concentrated in calls: $12 Jun-18 (−1,286), $15 '27 (−845), $12 '28 (−795),
$30 '27 (−716), $20 '27 (−543) — some LEAP call profit-taking/closing. `position-rolls`
returned **n=0** (no near→far rolls at threshold 500).

### Pin / OPEX concentration

- `pin-risk` (dte≤7, ≤5% distance): **PATH absent** from market-wide top-25 → no strong
  Jun-5 weekly pin.
- `opex-concentration` (≥40%): **PATH absent** → OI spread across 14 expiries, no single
  near-expiry cliff ≥40%.

## Tool calls (audit trail)

| Command | Key value(s) ← `jq` path | Rows |
|---------|--------------------------|------|
| `oi oi-by-strike --symbol PATH` (+`--dte-max 30`) | $15 wall net +66,418 ← `.results[].net_oi`,`role` | top-10 ×2 |
| `oi term-structure --symbol PATH` | Jan-27 37.2% ← `.term_structure[].pct_of_total_oi` | 14 exp |
| `oi biggest-increases --min-oi-change 500` | $13.5 C +4,036 ← `.results[].oi_diff_plain`; side ← OPRA `option_symbol` | top-20 |
| `oi smart-positioning` | $14 calls "bearish" (writing) ← `.results[].direction` | top-20 |
| `oi decrease-with-volume`, `position-rolls` | rolls n=0 ← `.results|length` | — |
| `oi pin-risk`, `oi opex-concentration` | PATH absent ← `.results[]|select(.ticker=="PATH")` | market-wide |

## Tool errors

<none — all reads parsed clean through `jq`>

## Verdict for downstream phases

- **Positioning bias:** **mildly bullish but range-capped** — structurally call-skewed
  OI (long LEAP-call base, $15 wall), but today's builds form a **collar/covered-call**
  structure (cap $14, floor $9–10) around the phase-2 accumulated long. Not a breakout
  configuration; an income/protection configuration.
- **Conviction:** **2/5** (directionally) — two-sided builds, none structural; the
  bullish tilt is in the *standing* LEAP base, not in fresh conviction.
- **Largest OI build as % of float:** **0.098%** ($13.5 Jun-5 call +4,036, share-equiv)
  — immaterial vs the 412.34M float; no structural directional bet today.
  [OI:oi_pct_float fz]
- **Three pin/cliff strikes for phase-9:**
  1. **$15 call_wall_resistance** (93,768 OI, +66k net call) — primary upside magnet/cap
  2. **$14 call_wall_resistance** (near-term) — first resistance above spot (+6.7%)
  3. **$11 put_wall_support** (19,614 near-term put OI) — downside structural support;
     near-term OPEX gravity = **Jun-18** expiry
- **Open questions:**
  1. Does phase-4 GEX/max-pain confirm $13–15 as the dealer-pinned range, and where is
     zero-gamma relative to spot?
  2. Is the $14 call writing truly covered (vs the accumulated stock = capped-but-long)
     or naked (a genuine ceiling call)? Phase-4/8 to weigh.
