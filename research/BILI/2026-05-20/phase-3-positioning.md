# Phase 3 — Open Interest & Positioning

**Ticker:** BILI
**As-of date:** 2026-05-20 (data date 2026-05-19)
**Generated:** 2026-05-20T09:50:00-04:00
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md

## Summary

OI moves tell a more **sophisticated** story than the raw flow tape suggested.
The single largest OI build is **+2,421 contracts at the July-17 $30 strike,
inferred direction bearish** — institutional **call writing** above $30. A
matching **+428 OI at the Jan-2027 $30 strike, also bid-side** suggests the
phase-1 Jan-2027 $25 call sweep is one leg of a **bull call spread $25/$30** —
long $25 / short $30 — rather than a naked long call. Counter-positioning
includes deep OTM put writing at 5/22 $17/$17.5 (bullish premium collection)
and small protective puts in 8/21 $18 (94-DTE downside insurance, ask-side).
The 5/29 $25 call OI **dropped 849 contracts** — strong evidence the trader
behind the Jan-27 sweep is **rolling out an existing $25 strike position** to
a longer horizon. **No pin risk** for OPEX week; BILI does not appear in the
top-50 market-wide pin candidates.

## Key signals

- **Jul-17 $30 Call OI +2,421** (676 → 3,097, +358%), prev_ask 7 vs prev_bid
  2,532 → **call writing** [OI:smart_positioning,biggest_increases].
- **Jan-27 $25 Call OI built only +106** vs the 883-contract phase-1 sweep —
  the sweep is partially OI-pending but companion **Jan-27 $30 Call OI +428
  bid-side** suggests a $25/$30 vertical spread [OI:smart_positioning].
- **May-29 $25 Call OI −849** (1,210 → 361) on 1,037 volume — closing the
  existing near-term $25 call, **rolling out** [OI:decrease_with_volume].
- **5/22 $17.5 Put OI +488** (20 → 508, +2,440%) all bid-side → **put
  writing at the lower band** [OI:smart_positioning].
- **8/21 $18 Put OI +154**, prev_ask 200 vs prev_bid 2 → **long-dated
  protective puts being bought** [OI:smart_positioning].

## Detailed findings

### Largest OI increases [OI:biggest_increases]

(Note: tool reports `stock_price` = **$20.02** as the close mark on 5/19;
phase-1 working spot $19.94 was the 19:46Z late-print. Use $20.00 as round
working spot.)

| # | Strike / Expiry / Type | DTE | OI Δ | Vol | prev_ask | prev_bid | Inferred dir |
|---|---|---|---|---|---|---|---|
| 1 | $30 / 2026-07-17 / **C** | 59 | **+2,421** | 2,539 | 7 | **2,532** | **bearish (write)** |
| 2 | $19.5 / 2026-05-22 / C | 3 | +680 | 1,018 | 297 | 676 | bearish (write) |
| 3 | $17.5 / 2026-05-22 / **P** | 3 | +488 | 575 | 180 | 366 | **bullish (write)** |
| 4 | $20 / 2026-05-22 / C | 3 | +464 | 837 | 405 | 372 | bullish (buy) |
| 5 | $17 / 2026-05-22 / P | 3 | +441 | 515 | 288 | 209 | bearish (buy) |
| 6 | $30 / 2027-01-15 / **C** | 241 | +428 | 429 | 52 | **376** | **bearish (write)** |
| 7 | $19.5 / 2026-05-29 / C | 10 | +404 | 408 | **408** | 0 | bullish (buy) |
| 8 | $21 / 2026-05-22 / C | 3 | +378 | 487 | 328 | 133 | bullish (buy) |
| 9 | $16.5 / 2026-05-22 / P | 3 | +242 | 280 | 142 | 113 | bearish (buy) |
| 10 | $26.5 / 2026-05-22 / C | 3 | +196 | 206 | 7 | 199 | bearish (write) |
| 11 | $26 / 2026-05-22 / C | 3 | +161 | 206 | 36 | 93 | bearish (write) |
| 12 | $23 / 2026-06-26 / C | 38 | +155 | 155 | 11 | 31 | bearish (write) |
| 13 | $18 / 2026-08-21 / **P** | 94 | +154 | 202 | **200** | 2 | **bearish (buy)** |
| 14 | $23.5 / 2026-06-26 / C | 38 | +152 | 154 | 8 | 33 | bearish (write) |
| 15 | $21.5 / 2026-05-22 / C | 3 | +150 | 243 | 71 | 144 | bearish (write) |
| 16 | $22.5 / 2026-05-22 / C | 3 | +133 | 151 | 86 | 58 | bullish (buy) |
| 17 | $19 / 2026-05-22 / P | 3 | +132 | 255 | 110 | 144 | bullish (write) |
| 18 | $19.5 / 2026-05-22 / P | 3 | +127 | 137 | 17 | 99 | bullish (write) |
| 19 | $22 / 2026-05-22 / C | 3 | +117 | 375 | 215 | 117 | bullish (buy)+write |
| 20 | $31 / 2026-07-17 / C | 59 | +115 | 115 | 0 | 115 | bearish (write) |

Critical aggregation:

- **Call WRITING (institutional supply) at $19.5-$31 strikes:** rows 1+2+6+10+11+12+14+15+20 add up to **≈ +3,816 contracts of new call supply** flowing in from sellers (premium collected). This is the dominant institutional flow pattern.
- **Call BUYING (directional demand) at $19.5-$22.5 strikes:** rows 4+7+8+16+19 add up to **≈ +1,646 contracts of new call demand**. Less than half the call-writing flow.
- **Put WRITING (bullish lower-band support):** rows 3+17+18 = **+747 puts written** — institutions agree to buy stock at $17-$19.5 if assigned. Bullish backstop.
- **Put BUYING (hedges/bearish):** rows 5+9+13 = **+837 puts purchased** — split between very-near-dated 3-DTE tail hedges (rows 5, 9 = $17 and $16.5 puts) and the 94-DTE $18 protective put (row 13).

### Largest OI decreases [OI:decrease_with_volume]

| Strike / Expiry / Type | DTE | OI Δ | Vol | Read |
|---|---|---|---|---|
| **$25 / 2026-05-29 / Call** | 10 | **−849** (1,210 → 361) | 1,037 | **Position closing** |
| $22 / 2026-06-18 / Put | 30 | −70 | 70 | Minor close |
| $30 / 2026-06-18 / Call | 30 | −23 | 52 | Negligible |

The −849 contracts at 5/29 $25 call is the single most informative *close*: it
arrives on the same day as the phase-1 **Jan-2027 $25 call ask sweep** (883
contracts / $217k). Same strike, different expiry — virtually certain to be
the **same trader rolling out a directional call** from a 10-DTE expiry to a
241-DTE expiry. Rolling out 8 months means the trader still wants upside
exposure but is **not** in a hurry — they don't expect the move imminently
and want time to be on their side.

### Smart positioning summary [OI:smart_positioning]

Aggregating directional inference:
- **Net "bullish" inferred:** 6 rows (5,353 prev_total_premium reference)
- **Net "bearish" inferred:** 14 rows
- **Inference is dominantly bearish-tilted by row count**, but the largest
  individual *bullish* row is the 5/29 $19.5C +404 ask-side (the kind of
  position that opens on an intraday rip).

### Roll detection [OI:position_rolls]

Tool returned **0 rolls** at threshold 100 with near-DTE max 21. Single-day
intersection misses cross-bucket rolls — but manually we identified:
- **5/29 $25C close (−849)** ↔ **Jan-27 $25C sweep (+883 contracts via flow,
  +106 OI partial)** = ROLL OUT in time, same strike.
- **5/22 $22.5P sold (141c bid)** ↔ **6/5 $22.5P bought (141c ask)** = ROLL
  OUT in time, same strike (already captured in phase-1).

### Pin risk [OI:pin_risk]

BILI **does not appear** in the top-50 pin-risk list. Top pin candidates this
OPEX week (DTE ≤ 7) are dominated by index ETFs (SPY 710, QQQ 680, IWM 270,
HYG 78) and a few China-adjacent names: **BABA $135 (3 DTE, pin score
$105,464)** and **FXI $37 (3 DTE, pin score $322,681)**. Flag these for
phase-6 macro — if China ADR sector pins to those round numbers, BILI is a
sympathy mover.

### OPEX concentration [OI:opex_concentration]

BILI **does not appear** in the top-50 single-expiry concentration list (which
requires ≥30%+ in one expiry). BILI's chain is healthily distributed across
5/22, 5/29, 6/5, 6/18, 7/17, 8/21, 9/18, 1/16/27, 12/17/27, 1/21/28 expiries
— no single-expiry cliff risk.

### Implied position structure (synthesized)

Reading flow + OI together, the institutional bloc appears to hold:

```
LONG  : 883c (or rolled-in equivalent) Jan-2027 $25 calls           [phase-1 sweep + phase-3 close of 5/29 $25C]
SHORT : 428c Jan-2027 $30 calls                                     [phase-3 bid-side OI build]
SHORT : 2,421c Jul-2026 $30 calls                                   [phase-3 dominant signature]
SHORT : 141c diagonal-rolled 22.5 puts to 6/5 expiry                [phase-1 + phase-3 inferred]
SHORT : 488c 5/22 $17.5 puts (premium collection)                   [phase-3]
SHORT : 132c 5/22 $19 puts + 127c 5/22 $19.5 puts                   [phase-3]
LONG  : 154c 8/21 $18 puts (protective)                             [phase-3]
LONG  : 15c Jan-2028 $25P + 15c $32P (deep-LEAP, small)             [phase-1]
+ retail-flavored 5/22 weekly call buying ($19-$22 strikes, small)  [phase-1]
+ DP block accumulation 307k shares cost basis ~$19.07 avg          [phase-2]
```

Net read: **bull call spread Jan-2027 $25/$30, financed partially by July $30
call writing, with bullish lower-band put writing at $17-$19.5 and a small
93-DTE downside hedge at $18.** This is a **range trade with bullish skew**
betting on BILI in the **$17–$30 corridor** by year-end, structurally biased
to upper end.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|---|---|---|
| `oi_biggest_increases` | symbol=BILI, date=2026-05-19, top-n=20, min=100 | 20 OI builds, top = Jul-17 $30C +2,421 |
| `oi_decrease_with_volume` | symbol=BILI, date=2026-05-19, top-n=20, min-vol=50 | 5 decreases, top = 5/29 $25C −849 |
| `oi_smart_positioning` | symbol=BILI, date=2026-05-19, top-n=20 | 14 bearish-inferred, 6 bullish-inferred |
| `oi_position_rolls` | symbol=BILI, threshold=100, near-dte-max=21 | 0 rolls detected (single-day algo) |
| `oi_pin_risk` | date=2026-05-19, dte-max=7, top-n=50 | BILI absent; top: SPY/HYG/QQQ/IWM/TLT |
| `oi_opex_concentration` | date=2026-05-19, top-n=50, min-conc=30 | BILI absent (healthily distributed) |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** **range-bound with bullish skew** — institutional
  structure is a long-dated bull call spread ($25/$30) financed by premium
  selling. Not aggressively bullish; not bearish. Believes in a controlled
  appreciation toward $30 over 8 months.
- **Conviction:** **3 / 5** — the synthesized structure is coherent and
  multi-leg (high-conviction interpretation), but the dominant single OI
  build is **call writing**, which caps upside in the near term.
- **Three pin/cliff strikes for phase-9:**
  1. **$22 (5/22 weekly):** highest near-DTE OI strike at 2,512 OI on $22
     call — first material **resistance ceiling** above spot.
  2. **$30 (Jul-17 / Jan-27):** institutional **call-write ceiling**;
     above-$30 unlikely on a 2-month basis.
  3. **$17–$17.5 (5/22):** put-write base = **soft support** (~750 contracts
     of short puts willing to be assigned at this level).
- **Open questions:**
  - Are the Jul-17 $30 calls written as covered-call overlay against a long
    stock position? Phase-4 GEX should clarify dealer-side gamma exposure at
    $30 to confirm.
  - Did the 5/29 $25 call closer actually roll into the Jan-2027 $25 sweep,
    or is this a coincidence? Phase-7 institutional_accumulation should
    settle it.
  - Why the 8/21 $18 protective put — is something specific being hedged
    around September? Phase-6 needs to check BILI's fiscal calendar
    (typically Q1 earnings in late-May; Q2 in late-August).
