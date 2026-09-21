# Phase 3 — Open Interest & Positioning

**Ticker:** NVDA
**As-of date:** 2026-05-27
**Generated:** 2026-05-28T02:28:00Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md, phase-1-flow.md, phase-2-dark-pool.md
**Spot referenced in OI data:** $212.65

## Summary

Positioning **confirms phase-1's bearish read**. `uw oi smart-positioning` tags
roughly **3× more "bearish" than "bullish" OI build** in the top-12 builds, and the
single biggest OI increase — the **0DTE 215 call (+20,954 contracts to 21,959)** —
arrived on prev_bid_vol 41,141 vs prev_ask_vol 28,459, i.e. **call writing on the
bid**. The 4th-largest build is the **Jul-17 $200 PUT (+18,186, 51 DTE)** —
hedging/bearish positioning being established. The 5-day sweep persistence
(phase-1) and today's OI build are pointing the same way. No position rolls
detected. Pin candidate: $220 (3.46% above spot, top OI 81,598).

## Key signals

- **Largest single OI build = 0DTE 215 call written on the bid:**
  +20,954 contracts, prev_bid_vol 41,141 > prev_ask_vol 28,459 [OI:biggest_increases]
  → smart-positioning tags **bearish** [OI:smart_positioning].
- **Big put buildup at $200 (Jul-17):** +18,186 OI (51 DTE) — downside hedge
  layer ~6% below spot [OI:biggest_increases].
- **Top-12 smart-positioning split:** 9 bearish (Σ OI_Δ ≈ 123,571) vs 3 bullish
  (Σ OI_Δ ≈ 40,262) — bearish/bullish ratio ≈ **3.07×** [OI:smart_positioning].
- **Pin candidate at $220** (3.46% above spot, top_strike_oi 81,598, pin_score
  616,446) [OI:pin_risk].
- **No rolls detected** at threshold 500, near-DTE ≤ 30 [OI:position_rolls] —
  argues *opens/closes*, not rolling, behind the OI tape.

## Detailed findings

### Largest OI increases — [OI:biggest_increases]

| Type | Strike | DTE | OI Δ | curr_oi | Volume | prev_ask_vol | prev_bid_vol | Read |
|------|-------:|----:|-----:|--------:|-------:|-------------:|-------------:|------|
| call | 215 | 0   | +20,954 | 21,959 | 85,135 | 28,459 | 41,141 | **bid-heavy → call writing** |
| call | 200 | 16  | +19,721 | 20,855 | 20,533 |  8,663 | 10,362 | bid-heavy (ITM call writing/covered) |
| call | 215 | 2   | +19,029 | 31,820 | 79,592 | 41,030 | 29,413 | ask-heavy → call buying |
| **put** | **200** | **51** | **+18,186** | 50,463 | 23,601 | n/a | n/a | **put buildup — hedge/bearish** |
| call | 220 | 2   | +15,385 | n/a | 91,304 | n/a | n/a | (smart-positioning: bearish) |
| call | 220 | 2   | +13,440 | n/a | 56,939 | n/a | n/a | (smart-positioning: bearish) |
| call | 217.5 | 2 | +11,042 | n/a | 67,110 | n/a | n/a | (smart-positioning: bearish) |
| call | 235 | n/a | +10,713 | n/a | 22,737 | n/a | n/a | (smart-positioning: bullish) |
| call | 217.5 | n/a | +10,520 | n/a | 48,398 | n/a | n/a | (smart-positioning: bullish) |
| call | 175 | n/a | +9,615 | n/a | 10,401 | n/a | n/a | (smart-positioning: bearish) |

Largest build as % of float: 0DTE 215 call +20,954 contracts × 100 share-mult /
23.27B float = **0.0090%** [OI:oi_pct_float fz] — share-equivalent is rounding
error for a 23.27B-float megacap (advisory, not a conviction signal).

### Closing / roll activity — [OI:decrease_with_volume, position_rolls]

Top closures: K225 −6,942, K215 −4,492, K250 −2,192, K275 −2,071. Mostly upside
strikes being trimmed — consistent with reducing long-call exposure (consistent
with the bearish read).

`uw oi position-rolls` (threshold 500, near-DTE ≤ 30): **0 rolls detected**. The
OI activity is *opens/closes*, not rolls — a Δ-OI bearish read in this regime is
"real" positioning, not duration management.

### Smart positioning — [OI:smart_positioning]

| Rank | Strike | Direction | OI Δ |
|-----:|-------:|-----------|-----:|
| 1  | 215  | bearish | 20,954 |
| 2  | 200  | bearish | 19,721 |
| 3  | 215  | bullish | 19,029 |
| 4  | 200  | bearish | 18,186 |
| 5  | 220  | bearish | 15,385 |
| 6  | 220  | bearish | 13,440 |
| 7  | 217.5| bearish | 11,042 |
| 8  | 235  | bullish | 10,713 |
| 9  | 217.5| bullish | 10,520 |
| 10 | 175  | bearish |  9,615 |
| 11 | 220  | bearish |  8,901 |
| 12 | 50   | bearish |  8,327 |

Sum bearish builds (top-12): ~123,571 contracts; sum bullish builds: ~40,262.
Ratio ≈ **3.07× bearish-heavy**. Note one revealing internal disagreement: the
*same* $215 strike is bearish on 0DTE (+20,954, ITM-pin call writing) and bullish
on May-29 2DTE (+19,029, ask-buying) — a calendar-like split, not a clean
single-direction position.

### Pin risk — [OI:pin_risk] (weekly OPEX week, 2026-05-29 Fri)

NVDA appears in pin-risk with:
- `nearest_high_oi_strike`: **$220** (3.46% above spot $212.65)
- `top_strike_oi`: **81,598 contracts**
- `total_oi_in_window`: 1,686,467
- `pin_score`: 616,446

$220 is the magnetic upside strike for weekly OPEX. The 0DTE $215 call writing
(largest build) sits *below* the pin — sellers betting it expires worthless if
spot drifts toward $215 or below.

### OPEX concentration

`uw oi opex-concentration` returned no NVDA rows at ≥40% threshold — OI is
spread across many strikes, not concentrated in a single OPEX cliff.

## Tool calls (audit trail)

| Command | Result summary |
|---------|----------------|
| `uw oi biggest-increases --symbol NVDA` | 0DTE C215 +20,954 (bid-heavy); P200 Jul-17 +18,186 |
| `uw oi decrease-with-volume --symbol NVDA` | top closes at upside strikes 225/215/250/275 |
| `uw oi smart-positioning --symbol NVDA` | 9 bearish / 3 bullish in top-12 (~3.07×) |
| `uw oi position-rolls --symbol NVDA --threshold 500 --near-dte-max 30` | 0 rolls |
| `uw oi pin-risk` (market-wide → NVDA filter) | pin K220, OI 81,598, distance 3.46% |
| `uw oi opex-concentration` (market-wide → NVDA filter) | no NVDA rows ≥40% |

## Tool errors

(none)

## Verdict for downstream

- **Positioning bias:** **BEARISH** — call writing dominates new OI; put hedges
  layering at $200; closings concentrated at upside strikes ($225/$215/$250/$275).
- **Conviction:** **3/5** (3:1 bearish/bullish ratio is real, but %-of-float is
  immaterial for a megacap; the cross-tenor disagreement at $215 trims the
  cleanliness).
- **Largest OI build as % of float:** 0.0090% [OI:oi_pct_float fz] — advisory:
  not a structural %-of-float move on a 23.27B-float name.
- **Three pin/cliff strikes for phase-9:**
  1. **$220** — weekly OPEX pin candidate (OI 81,598; 3.46% above spot).
  2. **$215** — heaviest writes/builds at this strike (0DTE 21,959 + May-29
     31,820); a clean ceiling for the next 2 sessions.
  3. **$200** — put-buildup floor (Jul-17 P200 OI 50,463); below this, hedges
     start *paying off* and dealer flow shifts.
- **Open questions:**
  - Are the $215 0DTE call writes naked (bearish) or covered (mechanical income)?
    Phase-4 GEX/dealer positioning is the only way to resolve.
  - Is the Jul-17 $200 put buildup discretionary hedging or systematic protection
    re-up? Phase-7c (sentiment / put-skew) should weigh in.
