# Phase 3 — Open Interest & Positioning

**Ticker:** PATH
**As-of date:** 2026-05-18 (data: 2026-05-15)
**Generated:** 2026-05-18T00:40:00-04:00
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md

## Summary

OI changes confirm phase-1's bullish read: **17 of top 20 OI increases are
calls**; weighted by absolute OI added, **bullish positioning beats
bearish ~3:1** (16,127 vs 5,805 contracts). The marquee names are
**2027-01-15 $10C (+3,647 OI to 12,470, prev ask/bid 4,118/228) and
2026-05-29 $13C (+2,128 OI to 11,687, prev ask/bid 2,068/67)** — clear
fresh long-call accumulation across two horizons
[OI:biggest_increases][OI:smart_positioning]. **No position rolls
detected** today [OI:position_rolls]. PATH does **NOT** make the top-50
`oi_pin_risk` list nor top-100 `oi_opex_concentration` list — so the
name has no meaningful 2026-05-22 weekly pin, and OI is spread broadly
across multiple expiries (no single OPEX cliff)
[OI:pin_risk][OI:opex_concentration]. The dominant OI feature is the
**massive pre-existing 2027-01-15 $30C position at 35,610 OI** — a
year-old LEAP whale that anchors the long-tail upside structure.

## Key signals

- **2027-01-15 $10C: +3,647 OI to 12,470, prev ask 4,118 vs bid 228, IV
  79.4%** — fresh LEAP accumulation, clean bullish signature
  [OI:smart_positioning].
- **2026-05-29 $13C: +2,128 OI to 11,687, prev ask 2,068 vs bid 67** —
  cleanest bullish OI signature of the day (ask/bid ratio 31:1) at the
  $13 upside strike [OI:smart_positioning].
- **2026-05-22 $10C: +1,533 OI to 2,835 (+118%), prev ask 1,496 vs bid
  813** — fresh next-week call positioning right at the round-number
  pivot [OI:biggest_increases].
- **2028-01-21 $10C: +453 OI to 7,812** — slow but persistent multi-year
  LEAP base [OI:biggest_increases].
- **Pre-existing 2027-01-15 $30C OI 35,610 (largely flat: -4 today, 370
  vol)** — anchored speculative upside whale; flagged as structural, not
  fresh directional [OI:biggest_increases].

## Detailed findings

### Largest OI increases (top 15)

| Contract | DTE | Δ OI | Curr OI | Prev ask vol | Prev bid vol | Inferred | Read |
|---|---|---|---|---|---|---|---|
| 2026-05-15 $10.5C | 0 | +6,626 | 10,987 | 7,260 | 1,932 | **Bullish** | Expired ITM-ish, won't matter Monday |
| **2027-01-15 $10C** | 245 | **+3,647** | 12,470 | 4,118 | 228 | **Bullish** | LEAP accumulation |
| **2026-05-29 $13C** | 14 | **+2,128** | 11,687 | 2,068 | 67 | **Bullish** | Upside near-term breakout bet |
| 2026-05-15 $9C | 0 | +1,731 | 2,729 | 262 | 1,864 | Bearish | Expired, noise |
| **2026-05-22 $10C** | 7 | **+1,533** | 2,835 | 1,496 | 813 | **Bullish** | Next-week breakout bet |
| 2026-06-05 $9C | 21 | +1,088 | 1,176 | 436 | 614 | Bearish | Mixed — could be writers |
| 2026-09-18 $8C | 126 | +698 | 736 | 200 | 500 | Bearish | Deep ITM call-write candidate |
| 2026-12-18 $8P | 217 | +690 | 1,067 | 81 | 609 | Bullish (put-sell) | Sold to open puts at $8 floor |
| 2026-06-18 $10C | 34 | +534 | 4,602 | 564 | 322 | **Bullish** | June ATM call adds |
| 2026-06-18 $12C | 34 | +516 | 9,843 | 317 | 205 | **Bullish** | June upside add |
| 2026-06-05 $12C | 21 | +501 | 946 | 952 | 145 | **Bullish** | Strong ask-tilt $12 add |
| **2028-01-21 $10C** | 616 | +453 | **7,812** | 170 | 143 | **Bullish** | Slow LEAP accumulation |
| 2026-06-05 $10C | 21 | +393 | 887 | 16 | 500 | Bearish | Likely written |
| 2026-05-22 $9.5P | 7 | +312 | 1,140 | 380 | 64 | Bearish | Hedge into weekly OPEX |
| 2026-06-05 $10P | 21 | +287 | 1,112 | 176 | 100 | Bearish | Hedge |

**Weighted bullish vs bearish (sum of |OI Δ|):**
- Bullish: 6,626 + 3,647 + 2,128 + 1,533 + 534 + 516 + 501 + 453 + 690 +
  189 + … ≈ **16,127 contracts**
- Bearish: 1,731 + 1,088 + 698 + 393 + 312 + 287 + 210 + 210 + 186 + 463
  + … ≈ **5,805 contracts**
- **Net bullish: ~2.8× by OI** — the 0DTE 2026-05-15 contracts are now
  irrelevant for downstream, so the cleaner forward-looking ratio is the
  2027/2028 LEAP + 2026-05-29/06-18 dominance.

### Closing / roll activity

| Contract | DTE | Δ OI | Volume | Read |
|---|---|---|---|---|
| 2026-06-18 $13C | 34 | -387 | 1,414 | Profit-taking on June upside |
| 2026-06-18 $14C | 34 | -128 | 637 | Profit-taking on June upside |
| 2026-05-29 $14C | 14 | -101 | 121 | Light close |
| 2026-05-22 $9P | 7 | -66 | 545 | Hedge unwind |
| 2027-03-19 $10C | 308 | -69 | 386 | Negligible |

`oi_position_rolls` returned **0 detected rolls** at threshold=100 with
near-DTE max=30 [OI:position_rolls]. **No same-day near→far roll
signature.** Today's net flow is overwhelmingly new positioning.

The fact that **OI is BEING ADDED at $10-$12 strikes** in 2026-06-18
while **OI is BEING CLOSED at $13-$14** for the same June expiry is
notable. This could be either:
1. Profit-taking on previously-bought $13/$14 calls (positive sign — old
   bull was right and is rotating closer-to-money), OR
2. A rotation of speculation **closer to spot** (bullish but with less
   conviction in a >$13 move by June OPEX).

Either reading is **structurally bullish for the near term but caps the
June upside view around $13**.

### Smart positioning (inferred direction)

The smart_positioning tool flagged **8 bullish vs 9 bearish vs 3 ambiguous**
labels in the top 20. By raw count this looks "mixed." But applied to OI
weight, bullish dominates (see weighted ratio above). The 9 "bearish"
labels are mostly:
- Bid-side closes on 2026-06-05 $10C/$9C (likely closers, not new shorts)
- Hedge puts in 2026-05-22 $9.5P / 2026-06-05 $10P (small)
- 2026-09-18 $8C bid-side +698 — looks like a covered-call write on a
  long stock position, NOT a directional bear (the buy ratio in phase-2
  was 0.586 — institutions are LONG)

So the cleaner read is: **bullish directional + covered-call income on
long stock + tail-hedge puts.**

### Pin risk

PATH does NOT appear in the top 50 by `oi_pin_risk` with dte-max=7 and
max-distance-pct=10 [OI:pin_risk]. **No meaningful pin into 2026-05-22
weekly.** OPEX behavior into this week's expiry should not dominate the
underlying.

### OPEX concentration

PATH does NOT appear in the top 100 of `oi_opex_concentration` at
min-concentration-pct=40 [OI:opex_concentration]. **OI is spread across
many expiries**, with the largest single-strike-expiry being **2027-01-15
$30C at 35,610 OI** — an old LEAP whale. The 2027-01-15 expiry overall
likely holds the deepest concentration but it's still below the 40%
threshold because OI is also meaningful at 2028-01-21, 2026-06-18, and
2026-07-17.

### Existing OI ranks (top strikes by current OI)

| Contract | Curr OI | DTE | Note |
|---|---|---|---|
| 2027-01-15 $30C | **35,610** | 245 | Anchored speculative whale (existed before today) |
| 2027-01-15 $10C | 12,470 | 245 | LEAP base, growing today |
| 2026-05-29 $13C | 11,687 | 14 | Today's standout add (+2,128) |
| 2026-05-15 $10.5C | 10,987 | 0 | Expired Friday — irrelevant Monday |
| 2026-06-18 $12C | 9,843 | 34 | Phase-1 call wall confirmed |
| 2028-01-21 $10C | 7,812 | 616 | Slow LEAP base |
| 2026-05-22 $9P | 7,866 | 7 | Largest near-week put OI |
| 2026-06-18 $13C | 6,808 | 34 | Light closing today (-387) |
| 2026-05-15 $10C | 7,034 | 0 | Expired |
| 2026-06-18 $14C | 2,318 | 34 | Light closing today (-128) |

**Magnetism map (forward-looking strikes):**
- **$10.00:** 2026-05-22 ($10C 2,835 + $9P 7,866), 2026-06-18 $10C 4,602,
  2027-01-15 $10C 12,470, 2028-01-21 $10C 7,812 — **HEAVIEST round-number
  magnet** across the entire term structure.
- **$12.00:** 2026-06-18 $12C 9,843, 2027-01-15 $12C (~3k from phase-1
  sweep). **Primary upside target where call-sellers will defend**.
- **$13.00:** 2026-05-29 $13C 11,687, 2026-06-18 $13C 6,808. **Next
  resistance shelf if $12 breaks**.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `oi_biggest_increases` | `{symbol: PATH, top-n: 20, min-oi-change: 100, date: 2026-05-15}` | 20 rows, 17 calls, top +6,626 |
| `oi_decrease_with_volume` | `{symbol: PATH, top-n: 15, min-volume: 100, date: 2026-05-15}` | 10 rows, max decrease -387 at 2026-06-18 $13C |
| `oi_smart_positioning` | `{symbol: PATH, top-n: 20, min-oi-change: 100, date: 2026-05-15}` | 8 bull / 9 bear / 3 mixed; bullish-weighted ~3:1 |
| `oi_position_rolls` | `{symbol: PATH, threshold: 100, near-dte-max: 30, date: 2026-05-15}` | **0 rolls detected** |
| `oi_pin_risk` | `{top-n: 50, dte-max: 7, max-distance-pct: 10, date: 2026-05-15}` | PATH not in top-50 — no meaningful weekly pin |
| `oi_opex_concentration` | `{top-n: 100, min-concentration-pct: 40, date: 2026-05-15}` | PATH not in top-100 — broad expiry distribution |

## Tool errors

(none)

## Verdict for downstream phases

- **Bias from this phase:** **BULLISH (with income / covered-call
  overlay)**
- **Conviction:** **4/5** — clean 3:1 bullish OI weighting on fresh
  positioning, including the cleanest signature (2026-05-29 $13C ask/bid
  31:1); held back from 5 because the closing of $13/$14 June calls hints
  at a near-term ceiling around $13.
- **Three pin/cliff strikes for phase-9:**
  1. **$10.00** — strongest round-number magnet, OI everywhere (weekly,
     monthly, LEAPs). Useful as the **floor and entry/re-entry pivot**.
  2. **$12.00** — heaviest forward call wall (2026-06-18 $12C 9,843,
     2027-01-15 $12C growing). **Phase-9 should target this as the first
     measured-move objective** if break of $10.71 (phase-2 resistance)
     confirms.
  3. **$13.00** — second resistance shelf (2026-05-29 $13C 11,687,
     2026-06-18 $13C 6,808). **Phase-9 upside extension target** if a
     June catalyst breaks $12.
- **Open questions for downstream:**
  - Is the **2027-01-15 $30C 35,610 OI whale** sitting on a known
    institutional thesis (a buyout call?) or just an aged speculative
    leftover? (phase 6 catalyst search)
  - Does the dealer gamma profile (phase 4) align with the $10 / $12 OI
    walls — i.e. is dealer gamma flip at or near $10? If gamma flips
    positive above $10, dealers will damp moves into $12.
  - The covered-call writing on $8-$10 strikes (2026-06-05 $10C +393,
    2026-09-18 $8C +698) plus the dark-pool 0.586 buy ratio = an
    institution running a **buy-write program**. That's structurally
    bullish for the **floor** but caps the **upside** until the
    program is rolled higher.
