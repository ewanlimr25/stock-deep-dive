# Phase 3 — Open Interest & Positioning

**Ticker:** FCX
**As-of date:** 2026-05-20 (effective data 2026-05-19)
**Generated:** 2026-05-20T19:55:00-04:00
**Upstream phases cited:** `phase-0-intake.md`, `phase-1-flow.md`, `phase-2-dark-pool.md`

## Summary

Phase-3 partially **contradicts** the surface read from phase-1. While phase-1
spotlighted the **$1.54M July 65C ask-side sweep** as the day's headline
bullish print, OI data shows the **July 65C OI actually FELL by 9,117
contracts** (33,172 → 24,055) on 14,478 volume [OI:decrease_with_volume].
Decomposing: ~2,681 opens / ~11,797 closes — the sweep buyer was on the
opposite side of a much larger institutional **unwind** of long July 65C
calls. The same picture holds for **July 70C (OI −5,970, vol 20,828)** and
**Jun-18 70C (OI −674, vol 14,711)**. All three highest-OI upside strikes
saw **net distribution**, not accumulation, on the day.

That said, today's **largest single new build is genuine and bullish**:
**Jun-18 59C went from 0 → 6,216 OI** on $3.23M of premium with ask-volume
5,611 vs bid 722 (88% ask) [OI:biggest_increases][OI:smart_positioning]. This
is a brand-new ATM/slightly-OTM monthly call position with the highest ask-
bid skew of the day. Combined with a 67C Jun-5 build (66 → 6,111 OI, 93%
ask) the **near-term Jun expiries are seeing fresh bullish accumulation at
59 and 67 strikes simultaneously**.

Counter to that, **bearish OI builds** include: 63P May-29 (190 → 1,979,
74% ask), 49P Aug-21 (1,881 → 3,302), 62P Jun-26 (24 → 540 all ask), 57P
Jun-18 (0 → 430 all ask), and 70C Jan-27 LEAP being SOLD (12,785 → 13,385
with 70% bid). The smart-positioning tool tags **13 of the top-20 OI changes
as bearish, 4 as bullish, 3 ambiguous** [OI:smart_positioning]. Pin-risk and
opex-concentration scans **do not flag FCX** — next OPEX (Jun-18) is 30 DTE,
outside the 7-day window [OI:pin_risk][OI:opex_concentration].

**Net positioning bias: MIXED with a bearish edge by count, but the single
biggest new bull build (59C Jun-18, $3.2M premium) is more institutionally
significant than several smaller bearish puts combined.** Conviction 3/5.
The picture is a market with active two-way debate, not a one-sided thesis.

## Key signals

- **Headline NEW bull build:** Jun-18 **59C OI 0 → 6,216 (+6,216) on 6,508
  volume**, ask_vol 5,611 vs bid 722, $3.23M premium [OI:biggest_increases].
  This is the most institutionally significant build of the day and was NOT
  visible in phase-1 (no single block ≥ $100k triggered the sweeps cutoff).
- **CRITICAL CONTRADICTION:** Jul-17 **65C OI −9,117** (33,172 → 24,055) on
  14,478 volume [OI:decrease_with_volume]. The $1.54M sweep in
  phase-1-flow.md §Sweeps was buying liquidity FROM a larger unwind, not
  pure accumulation. Estimated open/close split: 2,681 / 11,797.
- **Jul-17 70C** similarly closing: OI −5,970 (23,232 → 17,262) on 20,828
  volume — second-largest upside strike also being distributed
  [OI:decrease_with_volume].
- **Short-dated bullish lottery build:** Jun-5 67C **OI 66 → 6,111** (+6,045)
  on 91% ask-side volume [OI:smart_positioning].
- **Smart-positioning count:** 13 bearish / 4 bullish / 3 ambiguous in the
  top-20 OI changes [OI:smart_positioning]. Bearish skew is broad-based
  across DTEs.
- **No pin risk this week:** FCX absent from market-wide pin-risk top-50
  (next OPEX Jun-18 is 30 DTE) [OI:pin_risk]; absent from opex-concentration
  top-50 (OI is well-distributed across expiries) [OI:opex_concentration].
- **No same-day rolls detected** at the 300-threshold [OI:position_rolls].

## Detailed findings

### Largest OI increases [OI:biggest_increases]

(Sorted by |Δ OI|. Spot at snapshot $58.66.)

| Strike | Type | Expiry | DTE | Prev OI | Curr OI | Δ OI | Vol | Prev ask vol | Prev bid vol | Read |
|--------|------|--------|-----|---------|---------|------|-----|--------------|--------------|------|
| 59 | call | 2026-06-18 | 30 | 0 | **6,216** | **+6,216** | 6,508 | 5,611 (86%) | 722 | **Brand-new ATM bull build — top signal** |
| 67 | call | 2026-06-05 | 17 | 66 | 6,111 | +6,045 | 6,148 | 5,616 (91%) | 425 | Bullish short-dated lottery |
| 63 | put | 2026-05-29 | 10 | 190 | 1,979 | +1,789 | 1,882 | 1,351 (74%) | 472 | ITM put build — protection or short |
| 49 | put | 2026-08-21 | 94 | 1,881 | 3,302 | +1,421 | 1,521 | 18 | 3 | Long-dated OTM put build (tiny ask/bid sample → low confidence on direction) |
| 66 | call | 2026-05-22 | 3 | 2,457 | 3,455 | +998 | 1,341 | 166 | 1,097 (82%) | **0DTE-style bid-side adds — calls SOLD, weekly mean-revert bet** |
| 40 | put | 2027-01-15 | 241 | 6,355 | 7,055 | +700 | 700 | 0 | 700 (100%) | Pure put-write — bullish LEAP signature |
| 70 | call | 2027-01-15 | 241 | 12,785 | 13,385 | +600 | 1,083 | 276 | 649 (60%) | LEAP calls SOLD (covered-call / call-writing) |
| 55 | put | 2026-05-29 | 10 | 203 | 748 | +545 | 549 | 512 (93%) | 37 | OTM put bought |
| 62 | put | 2026-06-26 | 38 | 24 | 540 | +516 | 516 | 516 (100%) | 0 | Pure put-buy build — protective |
| 57 | put | 2026-06-18 | 30 | 0 | 430 | +430 | 451 | 414 (92%) | 35 | NEW OTM put protection at Jun-18 |
| 63 | call | 2026-05-29 | 10 | 229 | 648 | +419 | 539 | 57 | 455 (84%) | Calls SOLD (bid-side) — short call or cover |
| 70 | call | 2026-06-05 | 17 | 733 | 1,143 | +410 | 581 | 57 | 470 (81%) | Calls SOLD (bid-side) |
| 57 | put | 2026-05-22 | 3 | 410 | 786 | +376 | 453 | 270 (61%) | 175 | Weekly OTM put |
| 65 | call | 2026-09-18 | 122 | 2,971 | 3,333 | +362 | 603 | 49 | 530 (88%) | Calls SOLD (bid) — meaningful for Sep |
| 58 | put | 2026-05-22 | 3 | 471 | 804 | +333 | 461 | 347 (75%) | 75 | ATM weekly put bought |

### Largest OI decreases [OI:decrease_with_volume]

| Strike | Type | Expiry | DTE | Prev OI | Curr OI | Δ OI | Vol | Open/close split (est) | Read |
|--------|------|--------|-----|---------|---------|------|-----|------------------------|------|
| **65** | **call** | **2026-07-17** | **59** | **33,172** | **24,055** | **−9,117** | **14,478** | 2,681 / 11,797 | **MASSIVE long-call unwind. Counters phase-1 65C sweep narrative.** |
| **70** | **call** | **2026-07-17** | **59** | 23,232 | 17,262 | **−5,970** | 20,828 | 7,429 / 13,399 | Long-call distribution |
| 70 | call | 2026-06-18 | 30 | 29,333 | 28,659 | −674 | 14,711 | 7,019 / 7,693 | Heavy churn, slight unwind |
| 50 | put | 2026-06-18 | 30 | 19,701 | 19,482 | −219 | 560 | 171 / 390 | Minor put close |
| 55 | call | 2026-07-17 | 59 | 1,656 | 1,458 | −198 | 325 | 64 / 261 | Slight ITM call close |
| 75 | call | 2026-06-18 | 30 | 14,100 | 13,903 | −197 | 831 | 317 / 514 | OTM call slight close |
| 50 | call | 2026-07-17 | 59 | 811 | 665 | −146 | 525 | 190 / 335 | ITM call closing |

**Open/close estimation:** if `vol = opens + closes` and `Δ OI = opens −
closes`, then `opens = (vol + Δ_OI)/2` and `closes = (vol − Δ_OI)/2`. For
the 65C Jul: opens ≈ (14,478 − 9,117)/2 = 2,681; closes ≈ 11,797. The
$1.54M sweep buyer (6,158 contracts on ask) was therefore **either rolling
their own position or buying from a larger profit-taking seller**.

### Smart positioning — inferred direction summary [OI:smart_positioning]

| Direction | Count in top-20 | Notable contracts |
|-----------|----------------|-------------------|
| **Bullish** | **4** | 59C Jun-18 (huge), 67C Jun-5 (huge), 40P Jan-27 (put-write), 65C May-22 weekly |
| **Bearish** | **13** | 63P May-29, 49P Aug-21, 66C May-22 (call-write), 70C Jan-27 (LEAP call-sell), 55P May-29, 62P Jun-26, 57P Jun-18, 63C May-29 (call-sell), 70C Jun-5 (call-sell), 65C Sep-18 (call-sell), 57P May-22, 58P May-22, 65C Jun-18 (call-sell) |
| Ambiguous | 3 | 59P May-22, 53C May-29, 52C May-29 |

**Important nuance:** the "bearish" classifications include a lot of
**short-call writing** (bid-side calls at 66/63/70/65/53/52 strikes). These
are often *covered* calls written by institutions ALREADY long the stock —
their bias isn't "I think FCX falls", it's "I want premium income and would
sell if assigned at strike X". The dark-pool data (phase-2, +$11M net
accumulation) suggests this is exactly what's happening: institutions are
**accumulating equity + writing premium against it** (a *covered-call yield
play*), not directionally shorting.

That nuance does NOT extend to the OTM put builds (62P Jun-26, 57P Jun-18,
63P May-29) — those are genuine bearish/protection bets.

### Position rolls

[OI:position_rolls] — **0 rolls detected** at threshold=300 within the 30-
DTE near bucket. Means no clear single-day institutional roll from a near-
DTE strike to a far-DTE strike. The 65C July unwind does NOT have a
matching far-dated build elsewhere visible in OI deltas, suggesting profit-
taking rather than rolling out.

### Pin risk

[OI:pin_risk] — **FCX absent from the OPEX-week pin-risk top-50** (top
tickers SPY pin 710, HYG 78, QQQ 680, etc., all DTE ≤ 7). FCX's nearest OPEX
is Jun-18 at 30 DTE. **No current pin pressure** — phase-9 cannot anchor
entries to a pin level this week.

### OPEX concentration

[OI:opex_concentration] — **FCX absent from the top-50 single-OPEX-
concentration list** (top names are small-caps with ≥99% OI in one expiry).
FCX's OI is **spread across multiple expiries** (Jun-18, Jul-17, Aug-21,
Nov-20, Jan-27, Jan-28) — characteristic of liquid mid-cap chains. No
single OPEX cliff to fade or trade.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `oi_biggest_increases` | symbol=FCX, top_n=20, min_oi_change=200, date=2026-05-19 | 20 builds; #1 = 59C Jun-18 +6,216 |
| `oi_decrease_with_volume` | symbol=FCX, top_n=15, min_volume=100, date=2026-05-19 | 15 closes; #1 = **65C Jul-17 −9,117** |
| `oi_smart_positioning` | symbol=FCX, top_n=20, min_oi_change=200, date=2026-05-19 | 13 bear / 4 bull / 3 ambig |
| `oi_position_rolls` | symbol=FCX, near_dte_max=30, threshold=300, date=2026-05-19 | **0 rolls detected** |
| `oi_pin_risk` | dte_max=7, top_n=50, date=2026-05-19 | FCX not in list (30 DTE to nearest OPEX) |
| `oi_opex_concentration` | min_conc=30%, top_n=50, date=2026-05-19 | FCX not in list (multi-expiry spread) |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** **mixed, with bearish edge by count BUT
  largest single-position dollar weight is bullish (59C Jun-18 $3.2M).** The
  surface tape (phase-1) overstated the bull case; OI mechanics reveal
  significant call distribution at $65/$70 strikes.
- **Conviction:** **3/5**. Strong evidence in both directions — needs
  phase-4 (dealer GEX) to tip the scale on which side dealers are squeezed.
- **Three pin/cliff strikes for phase-9 reference:**
  1. **$59 — the new 59C Jun-18 build (6,216 OI).** This is the magnet for
     the next 30 days. Dealer gamma will compress around this strike.
  2. **$65 — the dying-but-still-large 65C Jul-17 (24,055 OI after
     unwind).** Acts as upside friction, but de-loading dealer short-gamma
     here.
  3. **$70 — the 70C Jul-17 (17,262 OI) + 70C Jun-18 (28,659 OI).** Still
     the upside ceiling; if spot rallies into this, dealer gamma resists.
- **Open questions:**
  - Did the 65C Jul-17 long position close because the position holder
     gave up on the move, or because they are rolling externally (not
     captured by single-day rolls)? Phase 5 historical OI trend may help.
  - Is the 59C Jun-18 build a SPECULATIVE bet (someone betting on a Jun-18
     monthly move above $59) or part of a structured trade (e.g., 59C / 65C
     bull call spread)? The 65C Jun-18 was net-sold (308 net bid-side) —
     **consistent with a 59C/65C bull call spread structure**.
  - Net dealer gamma exposure — does the 59C build force dealers short
     gamma into a squeeze if spot ticks above $59? (phase 4 `gex` /
     `today_gamma_flip` is decisive)
