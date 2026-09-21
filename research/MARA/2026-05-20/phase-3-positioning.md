# Phase 3 — Open Interest & Positioning

**Ticker:** MARA
**As-of date:** 2026-05-19
**Generated:** 2026-05-20T00:25:00-04:00
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md

## Summary

Today's OI delta shows **massive call-writing concentrated at the $13 and
$14 strikes** for Friday's 2026-05-22 OPEX (T+3) — the 13C now sits at
**48,851 OI** and 14C at **45,322 OI**, the two largest single-strike
positions in the MARA chain. Same-day net ask-bid is -2,114 at 13C and
-1,753 at 14C (heavy bid-side = call-writing). Layered on top, opening
flow is bullish at near-ATM 12.5C/13.5C with **net ask-bid +309 and
+1,239 respectively**, and *speculative* bullish opening at far-OTM
upside calls (17C Jun-05 +655, 20C Aug-21 +1,838, 22C Jun-18 +597).
Net positioning shape: **stock is being structurally hemmed into a
$12-$13 range for OPEX week** while a separate participant is buying
upside optionality for the Jun-Aug horizon.

Stock price at OI snapshot: **$12.46** (confirms spot anchor in phase 1).

## Key signals

- 13C / 2026-05-22 OI now **48,851** (+1,212 vs prior; net ask-bid -2,114) →
  $13 is a gamma-resistance wall for Friday OPEX [OI:oi_biggest_increases]
- 14C / 2026-05-22 OI now **45,322** (+1,115 vs prior; net ask-bid -1,753) →
  secondary wall [OI:oi_biggest_increases]
- 12.5C / 2026-05-22 OI **28,548** (+3,920, the largest absolute increase
  today); ask/bid 4,967/4,658 → near-ATM positioning, mildly bullish
  [OI:oi_biggest_increases / oi_smart_positioning]
- 20C / 2026-08-21 OI 5,765 (+2,155; net ask-bid **+1,838**) → speculative
  upside bet to $20 by Aug-21 OPEX [OI:oi_smart_positioning]
- 10P / 2027-01-15 LEAP OI 30,350 (+2,780; net ask-bid **+3,025** ASK side) →
  structural put buying at $10 strike, 8 months out, $662K prev premium —
  big tail hedge / downside speculation [OI:oi_smart_positioning]
- 10P / 2026-06-18 OI **-3,175** (closing) on 7,406 volume → existing
  near-term put hedge being unwound [OI:oi_decrease_with_volume]
- Pin risk: MARA does NOT score in market-wide top-50 (small notional vs
  index ETFs), but **local pin behavior is real** — 13C and 14C OPEX walls
  will pull spot toward the lower of the two if Friday closes <$13
  [OI:oi_pin_risk]

## Detailed findings

### Largest OI increases (top, ranked by absolute OI Δ)

| Strike | Type | Expiry | DTE | OI Δ | Curr OI | Net ask-bid | Smart-positioning |
|--------|------|--------|-----|------|---------|-------------|-------------------|
| 12.5 | call | 2026-05-22 | 3 | +3,920 | 28,548 | +309 | bullish (near-ATM) |
| 10 | put | 2027-01-15 | 241 | +2,780 | 30,350 | **+3,025** | bearish protection (LEAP put buy) |
| 12.5 | call | 2026-05-29 | 10 | +2,430 | 3,570 | +2 | bullish, balanced ask/bid |
| 13 | call | 2026-05-29 | 10 | +2,305 | 5,466 | **-1,942** | **bearish (call write)** |
| 12 | put | 2026-05-22 | 3 | +2,207 | 6,769 | -306 | bullish (put write) |
| 13.5 | call | 2026-05-22 | 3 | +2,173 | 27,251 | +1,239 | bullish (OTM call buy) |
| 20 | call | 2026-08-21 | 94 | +2,155 | 5,765 | **+1,838** | **bullish speculative** |
| 11 | put | 2026-05-22 | 3 | +2,018 | 10,910 | +302 | bearish (put buy) |
| 10.5 | put | 2026-05-22 | 3 | +1,781 | 4,730 | -817 | bullish (put write) |
| 12 | call | 2026-05-22 | 3 | +1,598 | 6,551 | -147 | bearish (mild call write) |
| 11.5 | put | 2026-05-22 | 3 | +1,494 | 8,499 | +748 | bearish (put buy) |
| 13 | call | 2026-05-22 | 3 | +1,212 | **48,851** | **-2,114** | **bearish (heavy call write)** |
| 14 | call | 2026-05-22 | 3 | +1,115 | **45,322** | **-1,753** | **bearish (heavy call write)** |
| 11.5 | put | 2026-05-29 | 10 | +968 | 7,107 | -608 | bullish (put write) |
| 14.5 | call | 2026-05-29 | 10 | +824 | 1,379 | -635 | bearish (call write) |
| 11.5 | call | 2026-05-22 | 3 | +788 | 2,146 | -330 | bearish (call write) |
| 17 | call | 2026-06-05 | 17 | +595 | 805 | +655 | bullish (OTM speculation) |
| 22 | call | 2026-06-18 | 30 | +595 | 3,523 | +597 | bullish (deep-OTM speculation) |

### Closing / roll activity

| Strike | Type | Expiry | DTE | OI Δ | Curr OI | Volume | Read |
|--------|------|--------|-----|------|---------|--------|------|
| 10 | put | 2026-06-18 | 30 | **-3,175** | 23,020 | 7,406 | Closing existing put hedge → bullish |
| 15 | call | 2026-06-18 | 30 | -696 | 35,342 | 2,037 | Closing OTM long calls → mild bearish |
| 10 | put | 2026-09-18 | 122 | -376 | 33,343 | 2,151 | Closing put hedge → bullish |
| 15 | call | 2028-01-21 | 612 | -363 | 4,036 | 1,039 | Closing LEAP calls → mild bearish |

Note: phase 1 logged a $368K bid-side sweep at **10P 2026-09-18** —
"put-writing" interpretation. The OI for 10P Sep-18 only decreased -376
contracts vs 2,151 volume; that's ratio ~17% close-to-volume → mostly NEW
positions opening (with some closing). Consistent with the bullish read.

**`oi_position_rolls`** returned **zero** detected rolls today (threshold
500, near_dte_max 30). No near-to-far OPEX rolling activity observable
intraday — fits the picture that this is *new* position buildup, not
maintenance.

### Smart positioning — net bias by horizon

**Near-term (DTE ≤ 10, May-22 / May-29 OPEX):** dominant signature is
**call-writing at 13-14** offset by **put-writing at 10.5-12** → range trade.
Implied corridor by OPEX:
- Hard ceiling: **$13** (call walls 13/14, $94K combined OI at 13/14, plus
  $13 call writers want stock <$13)
- Soft floor: **$11** (put writers @ 10.5-12, $20K combined OI being shorted)
- Most-likely pin: somewhere **$12.20-$12.80** for Friday close

**Mid-term (DTE 30-94, Jun/Aug OPEX):** bullish speculation appears at
**20C Aug-21 (+1,838 ask)** and **22C Jun-18 (+597 ask)** — these are
+60-75% OTM bets. Tiny premium ($149K, $3K) but the *direction* is
unambiguous: somebody is positioned for a major upside move into late
summer.

**Long-term (DTE 241):** **$662K of premium across the 10P Jan-27 LEAP
bought on the ask** is the largest single-name conviction print in
absolute dollar terms. Two readings:
1. *Bearish tail bet:* somebody thinks MARA could be at or below $10 by
   Jan 2027 (down 20%+).
2. *Portfolio hedge:* a holder of MARA equity is buying long-dated
   protection while collecting put-write premium near-term — classic
   covered-collar structure.

Read #2 is more consistent with the rest of the tape (put-writing
near-term, call-writing near-term, dark pool dip-buying) — looks like a
**long-equity holder running a structured collar position**.

### Pin risk

MARA does not appear in the market-wide `oi_pin_risk` top-50. Closest peer
small-cap names that DID make the list with similar geometry:
- AAL ($12.06 spot, $12 pin, pin_score 293K, 0.5% distance)
- F ($13.06, $13 pin, pin_score 124K, 0.46%)
- SOFI ($15.23, $15 pin, pin_score 221K)

MARA's geometry (spot $12.46, 13C OI 48.8K, 12.5C OI 28.5K) is comparable.
The pin_score threshold is gamma-weighted across notional, which works
against a $12 stock. **Local pin reality**: with 48.8K OI at 13C and 45.3K
OI at 14C entering OPEX week, dealers are *short calls* above $13 and will
sell stock if MARA rallies above $13 to hedge gamma. **Expect $13 to act
as resistance through Friday close**.

### OPEX concentration

MARA does not appear in the market-wide `oi_opex_concentration` top-50
(min 99.7% concentration). MARA's chain is well-distributed across May-22,
May-29, Jun-05, Jun-18, Jul-17, Aug-21, Sep-18, and LEAPs (Jan-27, Jun-27,
Jan-28). The Jun-18 expiry has the heaviest dollar OI but not the
overwhelming majority. **No single-expiry cliff.**

### Total OI snapshot (5/19 close)

Approximate OI by major strike (May-22 OPEX, T+3):

```
Strike      Calls    Puts
$10         3,183       (LEAP put has 30K, near-term smaller)
$10.5         420    4,730
$11         2,253   10,910
$11.5       2,146    8,499
$12         6,551    6,769
$12.5      28,548    (sparse puts)
$13        48,851      945
$13.5      27,251       0
$14        45,322       —
$14.5       1,379       —
```

Total call OI 11-14 strikes: ~134K contracts. Total put OI 10-12 strikes:
~31K contracts. **Call-skew positioning ~4:1** at OPEX. Combined with
the call-writing signature, the structure reads as **dealers/holders
short upside / long downside through Friday**.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__oi_biggest_increases` | `{symbol: MARA, date: 2026-05-19, min_oi_change: 500, top_n: 25}` | 18 rows, biggest 12.5C +3,920 |
| `mcp__uw-pp__oi_decrease_with_volume` | `{symbol: MARA, date: 2026-05-19, min_volume: 100, top_n: 15}` | 15 rows, top closer 10P Jun-18 -3,175 |
| `mcp__uw-pp__oi_smart_positioning` | `{symbol: MARA, date: 2026-05-19, min_oi_change: 500, top_n: 20}` | 18 rows, mix bullish/bearish |
| `mcp__uw-pp__oi_position_rolls` | `{symbol: MARA, date: 2026-05-19, threshold: 500, near_dte_max: 30}` | **0 rolls detected** |
| `mcp__uw-pp__oi_pin_risk` | `{date: 2026-05-19, dte_max: 7, max_distance_pct: 5, top_n: 50}` | MARA absent from top-50 |
| `mcp__uw-pp__oi_opex_concentration` | `{date: 2026-05-19, min_concentration_pct: 40, top_n: 50}` | MARA absent (well-distributed) |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** mixed-bullish; near-term *capped*, mid-term *bullish*
- **Conviction:** 4/5 — the OI walls at 13/14 are concrete (gamma-mechanical)
  and the LEAP put + far-OTM upside calls together define a coherent
  positioning story (covered-collar with upside speculation overlay)
- **Three pin/cliff strikes for phase-9 reference:**
  1. **$13.00** — 48,851 OI on 13C/May-22 (T+3). Gamma resistance.
  2. **$14.00** — 45,322 OI on 14C/May-22. Hard upside wall this week.
  3. **$12.50** — 28,548 OI on 12.5C/May-22 + bullish ATM positioning. Pin pivot.
- **Open questions:**
  - Is the 10P Jan-27 LEAP buyer the same desk as the dark-pool $13.28
    cluster seller? (Possible covered-collar at peak distribution.) Phase 7
    accumulation/distribution insights should help.
  - Where exactly is the dealer gamma flip (phase 4)? Hypothesis: flip
    near **$12.50-$12.80**, putting spot $12.46 just below — meaning
    dealers are short gamma below and long gamma above, which amplifies
    moves toward the gamma flip. Test in phase 4.
  - Does the 20C Aug-21 speculation align with any known catalyst (BTC
    halving cycle, MARA earnings)? Phase 6 macro should flag the calendar.
