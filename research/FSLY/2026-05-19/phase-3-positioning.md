# Phase 3 — Open Interest & Positioning

**Ticker:** FSLY
**As-of date:** 2026-05-19  (Effective data date: 2026-05-18)
**Stock reference price (UW field):** $16.72
**Generated:** 2026-05-19T00:30:00Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md

## Summary

OI-change tape from 2026-05-18 confirms **bullish new positioning skew on
balance** — the three largest "ask-side new" OI increases are calls at
$17.5 and $20 strikes (the same strikes phase-1 flagged as the campaign
target). Counter-position: a +300 OI new BID-side call write at the
**5/29 23C** strike (op_symbol FSLY260605C00023000) — a fresh institutional
**ceiling at $23**. There is **no near-term pin risk** (FSLY absent from
market-wide `oi_pin_risk` top-50 at DTE≤7, distance ≤10%) and **no OPEX
concentration cliff** (no expiry holds ≥30% of FSLY total OI). The biggest
standing strike mass overhead is the **9/18 $20 call at 2,890 OI** — that
is the dominant magnet/wall the trade plan must anchor on. The phase-1
$205K Jan'27 $20C bid block does **not** materially add to standing OI,
implying it was an existing-position roll/close rather than a fresh write,
which slightly de-rates the "institutional ceiling" framing from phase-1.

## Key signals

- **Sep'26 $20C is the dominant standing-OI strike: 2,890 OI** (vs 2,673
  prior day, +217 all ASK-side, inferred BULLISH) [OI:oi_biggest_increases]
  [OI:oi_smart_positioning]. Combined with Jun'18 $20C at 2,564 OI, that's
  **~5,450 contracts standing at the $20 strike** — the upside magnet.
- **Fresh bid-side call write at $23 strike (DTE 18):** 5/29 $23C OI
  118→418, +300, **100% bid-side** [OI:oi_smart_positioning] →
  institutional "won't trade above $23 by 5/29" view. Lines up with the
  phase-2 overhead supply zone at $18.84-$19.03.
- **Near-term $17.5 call accumulation:** 5/22 $17.5C OI 269→559 (+290,
  net +72 ask) and 5/29 $17.5C OI 53→333 (+280, net +107 ask)
  [OI:oi_smart_positioning] — fresh upside positioning in OPEX week and
  the next.
- **Put-selling supports $15 floor:** 5/22 $15P +61 OI bid-side, 7/17
  $12.5P +55 OI bid-side, 9/18 $15P +75 OI [OI:oi_smart_positioning].
  Confirms phase-1 put-selling read.
- **No OPEX pin / no concentration cliff for FSLY.** OI is spread across
  expiries; no single date holds ≥30% of total OI [OI:oi_opex_concentration].
- **Position-roll detector returned 0 rolls** [OI:oi_position_rolls] —
  consistent with the read that the phase-1 $205K Jan'27 $20C BID block
  was NOT an institutional roll, just a one-sided cross.

## Detailed findings

### Largest OI increases (FSLY, min |Δ| = 100)

`oi_biggest_increases`, top 5, date=2026-05-18 (only 5 contracts cleared
the 100 threshold — chain is thinly held):

| Strike | Type | Expiry | DTE | OI prev | OI curr | Δ | Prev ask vol | Prev bid vol | Inferred |
|---|---|---|---|---|---|---|---|---|---|
| 23 | C | 2026-06-05 | 18 | 118 | 418 | +300 | **0** | **300** | **bearish write** |
| 17.5 | C | 2026-05-22 | 4 | 269 | 559 | +290 | 202 | 130 | bullish |
| 17.5 | C | 2026-05-29 | 11 | 53 | 333 | +280 | 196 | 89 | bullish |
| 20 | C | 2026-09-18 | 123 | 2,673 | 2,890 | +217 | 218 | 1 | **bullish** |
| 22.5 | C | 2026-09-18 | 123 | 457 | 628 | +171 | 71 | 102 | bearish (write) |

The 9/18 $20C delta is the cleanest single signal — net new positioning is
**99.5% ask-side** (218 vs 1) and lifts the standing OI to 2,890. This is
the **bullish anchor** in the chain.

### Closing / roll activity

`oi_decrease_with_volume`, top results: only −21 on 6/18 $20C, −17 on
6/18 $25C, −2 on 6/18 $17.5C. **All trivial.** No meaningful position
exits. `oi_position_rolls` returned 0 rolls. Combined read: **no
distribution of existing positions**, all the action is opening.

### Smart positioning — inferred direction (full chain ≥ 50 OI Δ)

`oi_smart_positioning`, top 18 by |OI Δ|, date=2026-05-18:

Bullish-inferred new positions (calls bought / puts sold):

| Expiry | Strike | Type | OI Δ | Net ask−bid vol | DTE |
|---|---|---|---|---|---|
| 2026-05-22 | 17.5 | C | +290 | +72 | 4 |
| 2026-05-29 | 17.5 | C | +280 | +107 | 11 |
| **2026-09-18** | **20** | **C** | **+217** | **+217** | **123** |
| 2026-09-18 | 15 | P | +75 | −1 | 123 |
| 2028-01-21 | 25 | P | +74 | −36 | 613 |
| 2026-05-22 | 19.5 | C | +67 | +67 | 4 |
| 2026-05-22 | 18 | P | +66 | −41 | 4 |
| 2026-05-22 | 15 | P | +61 | −43 | 4 |
| 2026-05-29 | 20 | C | +60 | +58 | 11 |
| 2026-07-17 | 30 | C | +59 | +40 | 60 |
| 2026-07-17 | 12.5 | P | +55 | −52 | 60 |
| 2026-05-22 | 16.5 | P | +50 | −7 | 4 |

Bearish-inferred new positions (calls sold / puts bought):

| Expiry | Strike | Type | OI Δ | Net ask−bid vol | DTE |
|---|---|---|---|---|---|
| **2026-06-05** | **23** | **C** | **+300** | **−300** | **18** |
| 2026-09-18 | 22.5 | C | +171 | −31 | 123 |
| 2026-06-18 | 22.5 | C | +77 | −39 | 31 |
| 2026-06-05 | 19 | P | +63 | +64 | 18 |
| 2026-05-22 | 16 | P | +57 | +22 | 4 |

**Net read.** Bullish OI Δ on calls/puts combined ≈ +1,154 contracts;
bearish OI Δ ≈ +668 contracts. **~63% bullish skew on new positioning**
— consistent with phase-1 sweep verdict but a meaningfully less lopsided
ratio than the premium-side read would suggest.

The 6/5 $23C bear-write (+300 OI, 100% bid-side) is the single highest-
conviction bearish print of the day; it draws a hard ceiling at $23 for
the next 18 days. The 6/5 $19P fresh ASK-side buy (+63 OI, all ask)
suggests at least one trader is also positioned for downside through
early June.

### Pin risk (OPEX-week within 7 DTE, ≤10% distance)

`oi_pin_risk`, top 50: **FSLY does not appear**. The top contracts FSLY
holds in the 5/22 OPEX week (4 DTE) are 5/22 17C (94 OI), 5/22 17.5C
(559 OI), 5/22 18P (66 OI), 5/22 15P (61 OI) — none individually >1,000
OI, which is the floor for global pin-risk inclusion. **No pin pressure
into Friday's OPEX.**

### OPEX concentration (cliff strikes)

`oi_opex_concentration`, top 50, min 30%: **FSLY does not appear**. OI is
distributed across at least three monthlies (6/18, 7/17, 9/18) and
weeklies — no single expiry holds a dominant share.

### Reconciliation with phase-1 $205K Jan'27 $20C bid block

Phase 1 flagged a single $205K bid-side block at 13:33:09Z, 500 contracts
on Jan'27 $20C. If this were an institutional NEW WRITE we should see a
~+500 OI bump on FSLY270115C00020000 in today's OI change file. The OI
biggest-increases tool returned 5 contracts ≥100 OI change and **none
were Jan'27 $20C**. Two implications:

1. The print likely represented an **existing long closing** (selling to
   the market maker) — the buyer was a hedger, OI nets to ~zero. The
   "institutional ceiling at $20" framing from phase-1 is therefore
   **weaker** than the standing OI at 9/18 $20C suggests.
2. Even so, the standing 9/18 $20C OI of **2,890** is now the
   highest-OI standing strike visible on the chain and remains the
   primary upside magnet/wall structurally.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|---|---|---|
| `mcp__uw-pp__oi_biggest_increases` | symbol=FSLY, top_n=20, min_oi_change=100, date=2026-05-18 | 5 rows; 9/18 20C and 5/29 23C are the standouts |
| `mcp__uw-pp__oi_decrease_with_volume` | symbol=FSLY, top_n=15, min_volume=50, date=2026-05-18 | Trivial −21 max; no real closing activity |
| `mcp__uw-pp__oi_smart_positioning` | symbol=FSLY, top_n=20, min_oi_change=50, date=2026-05-18 | 18 rows; ~63% bullish skew on new positioning |
| `mcp__uw-pp__oi_position_rolls` | symbol=FSLY, threshold=100, near_dte_max=30, date=2026-05-18 | 0 rolls detected |
| `mcp__uw-pp__oi_pin_risk` | top_n=50, dte_max=7, max_distance_pct=10, date=2026-05-18 | FSLY absent (below 1,000-OI floor) |
| `mcp__uw-pp__oi_opex_concentration` | top_n=50, min_concentration_pct=30, date=2026-05-18 | FSLY absent (OI distributed across expiries) |

## Tool errors

(none)

## Verdict for downstream phases

- **Bias from this phase:** bullish-skew but with two-sided positioning
  (~63% bullish / ~37% bearish in new OI). Less unambiguous than
  phase-1 flow read.
- **Conviction:** 3 / 5 — magnitudes are small in absolute terms; the
  campaign signal is real but FSLY's standing OI base is thin enough
  that a single Wednesday block could shift the picture.
- **Three pin/cliff strikes for phase-9 entry/stop reference:**
  1. **$17.50** — near-term upside magnet. 5/22 17.5C (559 OI) + 5/29
     17.5C (333 OI) + 6/18 17.5C (937 OI) + 9/18 17.5C (campaign
     target, 783 day-vol on 229 prior OI). First breakout level.
  2. **$20.00 — primary upside magnet & ceiling.** 9/18 20C (2,890 OI,
     largest standing in chain) + 6/18 20C (2,564 OI). This is the
     "if FSLY rallies, gamma is here" strike. Also the strike of the
     phase-1 $205K bid block.
  3. **$23.00** — hard institutional ceiling for next 18 days. 6/5
     23C +300 OI new bid-side write. Any move toward $23 by early
     June will encounter dealer-supplied supply.
  4. (Bonus floor) **$15.00** — fresh put-selling across 5/22 / 7/17
     / 9/18 expiries. Bullish "willing to own here" line in the sand.
- **Open questions:**
  - Does the standing 5,454 OI at $20 strike (Jun+Sep) align with the
    dealer gamma flip / max-pain coordinates from phase-4 structure?
    → phase-4 will resolve.
  - Is the 5/29 $23 call write coordinated with FSLY's earnings or
    other catalyst, or just a generic premium-collection trade?
    → phase-5 historical earnings calendar + phase-6 catalyst search.
  - Why is the 7/17 OPEX seeing both ATM call and ATM put OI building
    in tandem? Long straddle, short straddle, or two different desks?
    → phase-4 vanna/charm + phase-5 IV percentile.
