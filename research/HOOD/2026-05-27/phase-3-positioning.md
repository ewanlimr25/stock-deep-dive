# Phase 3 — Open Interest & Positioning

**Ticker:** HOOD
**As-of date:** 2026-05-27
**Generated:** 2026-05-28T14:03:50Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md

## Summary

OI positioning corroborates phase-1's read: this is **range-bound, premium-selling
positioning, not directional accumulation.** The single largest OI build is the
**6/05 $80 call (+3,396, written — smart-positioning flags it bearish)**, i.e. an
overwrite/resistance cap above spot, while the **5/29 $69–72 puts are being sold**
(+2,668/+2,547/+2,461/+1,038, smart-positioning "bullish" = put writing below spot).
The dominant activity is **near-dated 5/29 OPEX (2 DTE) churn across a wide 69–82
band** — speculative/harvest, not structural (largest build = **0.045% of float**).
Pin math points to a **78 high-OI magnet** 2.4% above spot (76.18). No OPEX cliff,
no rolls. **Verdict: MIXED, range-bound; mild bullish tilt from put-selling, capped
above by written calls at 80.**

## Key signals

- Biggest build: **6/05 $80C +3,396** (curr OI 5,591, vol 4,977, avg $1.03) flagged
  **bearish** = call writing/overwrite → soft resistance ~80 [OI:biggest_increases][OI:smart_positioning].
- **Put-selling cluster 5/29:** 72P +2,668, 70P +2,547, 71P +2,461, 69P +1,038, all
  flagged **bullish** (writing puts below spot) [OI:smart_positioning] — the bullish tilt.
- **Pin magnet: strike 78**, top_strike_oi 17,288, pin_distance 2.39% above spot,
  dte_to_opex 2, total window OI 169,475 [OI:pin_risk].
- **No OPEX concentration cliff** for HOOD even at 20% threshold — OI well-distributed,
  no single-expiry gamma cliff [OI:opex_concentration].
- Largest OI build = 339,600 share-equiv = **0.045% of float** [OI:oi_pct_float fz] —
  non-structural, speculative near-dated positioning.

## Detailed findings

### Largest OI increases [OI:biggest_increases] / [OI:smart_positioning]

| Contract | Strike | Expiry | OI Δ | Vol | Curr OI | Smart-pos dir | Read |
|----------|--------|--------|------|-----|---------|---------------|------|
| HOOD…C80 | 80 | 2026-06-05 | **+3,396** | 4,977 | 5,591 | bearish | call written (cap) |
| HOOD…P72 | 72 | 2026-05-29 | +2,668 | 4,747 | — | bullish | put sold |
| HOOD…P70 | 70 | 2026-05-29 | +2,547 | 4,137 | — | bullish | put sold |
| HOOD…P71 | 71 | 2026-05-29 | +2,461 | 3,219 | — | bullish | put sold |
| HOOD…C78 | 78 | 2026-05-29 | +1,882 | 5,040 | — | bullish | call (2DTE OTM) |
| HOOD…C77 | 77 | 2026-05-29 | +1,590 | 3,705 | — | bullish | call |
| HOOD…C79 | 79 | 2026-05-29 | +1,559 | 2,809 | — | bullish | call |
| HOOD…C80 | 80 | 2026-05-29 | +1,553 | 8,374 | — | bullish | call (2DTE) |
| HOOD…C75 | 75 | 2026-06-18 | +1,491 | 2,519 | — | bullish | ATM call build |
| HOOD…P69 | 69 | 2026-05-29 | +1,038 | 1,727 | — | bullish | put sold |
| HOOD…C81/82 | 81/82 | 2026-05-29/06-05 | +1,116/+507 | — | — | bearish | upside written |
| HOOD…C90 | 90 | 2026-07-17 | +503 | 1,662 | — | bearish | far-OTM written |

Two-sided premium selling: puts written 69–72 (floor below), calls written 80–82 and
90 (ceiling above), with a band of 2DTE 75–80 calls of mixed intent. This is the
**low-IV-rank (23) range-selling signature** — dealers/funds harvesting theta expecting
HOOD to stay roughly 70–80 into Friday.

### Closing / roll activity [OI:decrease_with_volume] / [OI:position_rolls]

Decreases are small and scattered (95C −588, 85C −436, 75C −220, 100C −211) — ordinary
closing, no large unwind. `position-rolls` (threshold 500, near-dte ≤30) returned
**no rolls** — no systematic near→far migration. Nothing structural rotating.

### Smart positioning (inferred direction) [OI:smart_positioning]

Net inference: **bullish on the put side (writing 69–72)**, **bearish on the upper
call wall (writing 80–82, 90)**. The 2DTE 75–80 call builds are tagged bullish but
sit against the written 80 cap — net a **pin/range** stance, not a breakout bet.

### Pin risk (OPEX week — 5/29 is 2 DTE) [OI:pin_risk]

HOOD pin candidate: nearest_high_oi_strike **78**, spot 76.18, pin_distance 2.39%,
top_strike_oi 17,288, total_oi_in_window 169,475, pin_score 74,628. The 78 strike is
the upside OI magnet; combined with the written 80 cap and put-selling floor 69–72,
Friday's gravity zone is roughly **76–78**. (Spot must clear 78 with conviction to
escape the pin; the 80 written wall is the next cap.)

### OPEX concentration [OI:opex_concentration]

HOOD absent even at min-concentration 20% — OI spread across strikes/expiries, **no
single-expiry cliff**. No forced-hedging cliff risk into 5/29.

## Tool calls (audit trail)

| Command | Result summary |
|---------|----------------|
| `uw oi biggest-increases --symbol HOOD --top-n 20 --min-oi-change 500 --date 2026-05-27` | top 80C 6/05 +3,396; 70-72P 5/29 sold |
| `uw oi decrease-with-volume --symbol HOOD --top-n 15 --min-volume 100 --date 2026-05-27` | small scattered closes, no unwind |
| `uw oi smart-positioning --symbol HOOD --top-n 20 --min-oi-change 500 --date 2026-05-27` | puts 69-72 bullish (sold); 80-82/90 calls bearish (written) |
| `uw oi position-rolls --symbol HOOD --threshold 500 --near-dte-max 30 --date 2026-05-27` | none |
| `uw oi pin-risk --top-n 200 --dte-max 7 --max-distance-pct 5 --date 2026-05-27` | HOOD pin @78, 2.39% above spot, dte 2 |
| `uw oi opex-concentration --top-n 300 --min-concentration-pct 20 --date 2026-05-27` | HOOD absent (no cliff) |

## Tool errors

None (jq cuts initially showed null type/expiry; `option_symbol` carries both —
re-parsed cleanly).

## Verdict for downstream

- **Positioning bias:** **MIXED / range-bound** — mild bullish tilt from put-selling
  (69–72), capped by written calls (80–82, 90). Premium-selling on both wings.
- **Conviction:** **2/5** (low; near-dated harvest, not structural).
- **Largest OI build as % of float:** **0.045%** (3,396 contracts ≈ 339.6k shares vs
  761.05M float) — *not structural for this name*; advisory only [OI:oi_pct_float fz].
- **Three pin/cliff strikes for phase-9:**
  1. **78** — pin/high-OI magnet 2.4% above spot; first upside friction into 5/29.
  2. **80** — written call wall (biggest OI build, overwrite cap) → resistance.
  3. **70–72** — put-selling floor (sellers willing to own here) → support shelf,
     dovetails with phase-2's 73.64 lower DP shelf.
- **Open questions:**
  - Does dealer GEX (phase-4) sit positive (price pinned 76–78) or flip negative below
    a strike (squeeze risk)? The pin@78 + written-80 wall suggests **positive gamma /
    pinning** near spot — phase-4 to confirm.
  - Is the 75C 6/18 build (+1,491) the continuation of phase-1's Dec/Jun call buying,
    or more writing? (only mid-conviction directional build in the chain).
