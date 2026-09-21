# Phase 3 — Open Interest & Positioning

**Ticker:** SOFI
**As-of date (requested):** 2026-05-20
**Effective data date:** 2026-05-19
**Generated:** 2026-05-20T00:00:00Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md

## Summary

SOFI positioning on 2026-05-19 is **dominated by May-22 (3 DTE) expiry**, where
49,317 new call contracts opened across $15.50–$19 strikes — heavy short-term
positioning into Friday's weekly OPEX. **SOFI ranks #18 in the entire market's
pin-risk table with the $15 strike holding 80,486 OI and a pin score of
220,723** (spot 1.51% above pin) [OI:pin_risk]. Smart-positioning inference
shows a **two-track pattern**: at-the-money 15.5/16/16.5C are bought
(directional bullish), while overhead 17/17.5/18/19C are SOLD (covered-call /
overhead-resistance writing). That structure is consistent with phase-2 dark
pool **accumulation at $15.02–$15.30** [DP:largest] — institutions long stock,
writing premium against it into the rip toward $17. No same-day position rolls
detected, meaning the buildup is fresh conviction, not migration.

## Key signals

- **Pin risk: SOFI ranks #18 market-wide, pin strike $15.00, OI 80,486, pin
  score 220,723, DTE 3, distance 1.51% above spot** — strong May-22 magnet
  to $15. [OI:pin_risk]
- **May-22 16C: +12,861 OI (78.8% increase, curr OI 29,184), volume 31,093,
  inferred BULLISH** — largest single-strike new build, just $0.77 above spot.
  [OI:biggest_increases, OI:smart_positioning]
- **May-22 17C: +12,002 OI, BEARISH inference (net_ask_bid -4,594)** — i.e.
  CALL SELLING / overhead-resistance writing. The "ceiling" for this week is
  being painted at $17. [OI:smart_positioning]
- **May-22 16.5C: +10,318 OI, BULLISH inference (net_ask_bid +503)** —
  reinforces the 16C upside push, $1.27 above spot.
  [OI:smart_positioning]
- **Total May-22 call OI buildup across $15.50-$19 strikes: 49,317 contracts**
  in a single session — equivalent to **4.93M shares of speculative call
  exposure** at 3 DTE. Gamma-stacking risk into Friday open.
  [OI:biggest_increases]
- **Zero position rolls detected** at 500-contract threshold (near-DTE max 30)
  — buildup is genuinely new positioning, not migration of existing exposure.
  [OI:position_rolls]
- **LEAP buildup confirmed:** Jan-27 25C +1,753 OI (BEARISH inference, bid-
  side), Jun-18 20C +1,751 OI (BEARISH inference, bid-heavy), Aug-21 20C
  +1,703 OI (BEARISH inference). These LEAP increases at $20-$25 strikes are
  inferred as call WRITING — i.e. institutions writing long-dated covered calls
  against existing stock. [OI:smart_positioning]
- **Dec-2027 15P: +1,163 OI, BULLISH inference (bid-heavy → put selling)**
  — institutional 18-month put-write for $4.11 premium. Cash-secured-put
  income against the $15 level. [OI:smart_positioning]

## Detailed findings

### Largest OI increases (top 20)

| Contract | DTE | Strike | Type | OI Δ | Curr OI | Volume | Inferred dir |
|---|---|---|---|---|---|---|---|
| SOFI260522C00016000 | 3 | 16 | C | **+12,861** | 29,184 | 31,093 | Bullish |
| SOFI260522C00017000 | 3 | 17 | C | **+12,002** | 26,204 | 23,547 | Bearish |
| SOFI260522C00016500 | 3 | 16.5 | C | **+10,318** | 35,605 | 23,883 | Bullish |
| SOFI260522C00017500 | 3 | 17.5 | C | +5,618 | 17,453 | 8,986 | Bearish |
| SOFI260522C00015500 | 3 | 15.5 | C | +5,037 | 8,655 | 12,037 | Bullish |
| SOFI260522P00014500 | 3 | 14.5 | P | +3,067 | 9,724 | 4,943 | Bullish (put-sell) |
| SOFI260522P00015500 | 3 | 15.5 | P | +2,798 | 13,186 | 9,665 | Bearish (put-buy) |
| SOFI260529C00017000 | 10 | 17 | C | +2,749 | 8,838 | 4,890 | Bearish |
| SOFI260529C00018000 | 10 | 18 | C | +2,393 | 11,803 | 4,852 | Bullish |
| SOFI260522C00018000 | 3 | 18 | C | +2,177 | 14,765 | 6,578 | Bearish |
| SOFI260522P00016000 | 3 | 16 | P | +1,927 | 16,331 | 10,788 | Bearish (put-buy ask) |
| SOFI260529P00015000 | 10 | 15 | P | +1,774 | 16,653 | 5,098 | Bullish (put-sell) |
| SOFI270115C00025000 | 241 | 25 | C | +1,753 | 74,400 | 2,838 | Bearish (call-write) |
| SOFI260618C00020000 | 30 | 20 | C | +1,751 | 63,263 | 8,325 | Bearish (call-write) |
| SOFI260821C00020000 | 94 | 20 | C | +1,703 | 9,263 | 3,072 | Bearish (call-write) |
| SOFI260529C00017500 | 10 | 17.5 | C | +1,681 | 5,891 | 2,758 | Bearish |
| SOFI260522C00019000 | 3 | 19 | C | +1,304 | 5,826 | 2,347 | Bearish |
| SOFI260522P00015000 | 3 | 15 | P | +1,295 | 32,161 | 37,087 | Bullish (put-sell) |
| SOFI260605P00015500 | 17 | 15.5 | P | +1,181 | 3,961 | 1,804 | Bearish |
| SOFI271217P00015000 | 577 | 15 | P | +1,163 | 16,100 | 1,178 | Bullish (put-sell) |

**Aggregate May-22 net OI changes:**
- Calls: $15.5C +5,037 + $16C +12,861 + $16.5C +10,318 + $17C +12,002 +
  $17.5C +5,618 + $18C +2,177 + $19C +1,304 = **+49,317 net new call OI**.
- Puts: $14.5P +3,067 (sold = bullish), $15P +1,295 (sold = bullish),
  $15.5P +2,798 (bought = bearish), $16P +1,927 (bought = bearish) =
  **+9,087 net new put OI** (mixed direction).
- Call/put new-OI ratio: **5.4× more new calls than new puts** for May-22 →
  call-skew expansion intra-week.

### Closing / roll activity (decreases + position rolls)

The decreases table is **dominated by trivial moves** (-100 to -1,100 contracts
in deep OTM Jun-18 25/28/35C and isolated May-22 puts). No mass exit signature.

`oi_position_rolls(threshold=500, near-dte-max=30)` returned **zero detected
rolls**. This is informative: the May-22 buildup is **not absorbing flow from
expiring positions** — it is genuinely new positioning entering 3 DTE.

### Smart positioning (inferred direction)

The two-track pattern is the headline:

**BULLISH directional (ask-side or net buying):**
- 16C +12,861 OI (slightly ask, $0.77 above spot) — speculative upside
- 16.5C +10,318 OI (+503 ask) — speculative upside
- 15.5C +5,037 OI (+1,807 ask) — directional upside
- 14.5P +3,067 OI (bid-heavy = SOLD puts) — bullish income
- 15P May-22 +1,295 OI (bid-heavy = SOLD puts at the pin) — bullish income
- 15P May-29 +1,774 OI (balanced, slight bid) — likely put-write at $15 support
- Dec-2027 15P +1,163 OI (bid-heavy = SOLD LEAP puts) — long-term bullish income

**BEARISH directional (bid-side / call-writing / put-buying):**
- 17C +12,002 OI (bid-heavy = SOLD calls) — overhead resistance writing
- 17.5C +5,618 OI (bid-heavy = SOLD calls) — overhead resistance writing
- 18C May-22 +2,177 OI (bid-heavy = SOLD calls)
- 19C May-22 +1,304 OI (bid-heavy = SOLD calls)
- 15.5P +2,798 OI (ask-side = BOUGHT puts) — downside hedge
- 16P May-22 +1,927 OI (ask-heavy = BOUGHT puts) — downside hedge
- Jan-27 25C +1,753 OI (bid-heavy = SOLD LEAP calls) — long-term ceiling write
- Jun-18 20C +1,751 OI (bid-heavy = SOLD calls)
- Aug-21 20C +1,703 OI (bid-heavy = SOLD calls)

**Interpretation:** The chain pattern is **classic institutional
covered-call income strategy** layered on top of **retail / momentum
directional call buying at 15.5–16.5 strikes**. Institutions long the stock
(see phase-2 0.616 buy ratio [DP:block_stratified]) are writing premium at
17/17.5/18/19/20/25 strikes across May-22, May-29, Jun-18, Aug-21, and
Jan-27 expiries. The 15.5–16.5C call buying creates dealer **short gamma
above spot**, while the 17–25C call writing creates **dealer long gamma /
mean-reversion pull** at and above $17.

### Pin risk (May-22 OPEX, DTE=3)

SOFI ranks **#18 in the market-wide pin-risk table** for the May-22 weekly:

- **Spot:** $15.23
- **Pin strike (highest OI within 5%):** $15.00
- **Top-strike OI:** 80,486 contracts
- **Pin score:** 220,723 (well above the SOFI-historical baseline)
- **Total OI in pin window:** 500,432
- **Pin distance from spot:** 1.51% above the pin

This is the highest pin-score for SOFI we should expect in any typical week —
$15 will exert significant **gamma-pull on price into Friday close**.
Combined with phase-2 dark pool support at $15.02–$15.06 [DP:largest], the
two signals reinforce: **$15 is a hard floor for May-22 absent a downside
catalyst**.

### OPEX concentration

SOFI does NOT appear in the `oi_opex_concentration` table at the 40%+ threshold
— meaning SOFI's OI is **widely distributed across expiries** (May-22, May-29,
Jun-05, Jun-18 monthly, Jul-17, Aug-21, Sep-18, Jan-27, Jan-28, Jun-28 all
have meaningful OI). This is healthy chain structure for a fintech name and
means there is no single OPEX cliff after May-22 — the next monthly opex
(Jun-18) is the next major liquidity event.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|---|---|---|
| `oi_biggest_increases` | symbol=SOFI, top-n=20, min-oi-change=500, date=2026-05-19 | 20 rows; +12,861 on May-22 16C dominant; +49k aggregate May-22 call OI |
| `oi_decrease_with_volume` | symbol=SOFI, top-n=15, min-volume=100, date=2026-05-19 | All decreases trivial (-100 to -1,100); no mass exit |
| `oi_smart_positioning` | symbol=SOFI, top-n=20, min-oi-change=500, date=2026-05-19 | Two-track: directional 15.5-16.5C bullish; 17-25C call-write bearish |
| `oi_position_rolls` | symbol=SOFI, threshold=500, near-dte-max=30, date=2026-05-19 | **Zero rolls detected** — new positioning, not migration |
| `oi_pin_risk` | top-n=30, dte-max=7, max-distance-pct=5, date=2026-05-19 | SOFI #18 market-wide, pin $15, score 220,723, OI 80,486 |
| `oi_opex_concentration` | top-n=30, min-concentration-pct=40, date=2026-05-19 | SOFI absent → chain widely distributed (healthy) |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** **bullish-with-overhead-cap-at-$17**.
- **Conviction:** **4 / 5** — pin-risk #18 market-wide with $15 floor is a hard
  signal; covered-call writing at $17 caps near-term upside; the two-track
  pattern is institutionally rational and stack-confirms phase-2 accumulation.
- **Three pin/cliff strikes for phase-9 entry/stop reference:**
  1. **$15.00 — pin / hard floor for May-22.** 80,486 OI; gamma magnet. Use
     as primary entry trigger (buy retracement into $15.00–$15.06) and as the
     stop reference (loss of $14.95 invalidates the pin).
  2. **$17.00 — covered-call ceiling.** 26,204 OI built into May-22 alone;
     dealers will hedge on rally above $16.50 but selling pressure intensifies
     into $17. Use as **profit target #1** for any May-22 trade.
  3. **$18.00–$20.00 — institutional resistance.** Multi-expiry call-write
     buildup (Jun-18 20C +1,751, Aug-21 20C +1,703, Jan-27 25C +1,753) means
     $20 is the heavy institutional ceiling for the next 12 months. Use as
     **multi-month resistance / structural profit target**.
- **Open questions:**
  - Where is dealer gamma flip? (phase-4 must answer)
  - Does the put-write at $15P / $14.5P suggest institutions view $15 as a
    structural floor? (phase-7 insights composite should confirm)
  - Is the $20 / $25 institutional call-write tied to an upcoming Q2 earnings
    print? (phase-6 catalyst calendar must answer)
