# Phase 3 — Open Interest & Positioning

**Ticker:** USAR
**As-of date:** 2026-05-20 (effective UW data date: 2026-05-19)
**Generated:** 2026-05-20T10:15:00-04:00
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md

## Summary

USAR's OI chain reveals **three coexisting institutional behaviors** that
finally explain phase 1's "crossed signals":

1. **The 6/18 $21 PUT wall** sits at **16,949 OI** — the largest single
   contract in the chain — and is barely changing (-80 today). This is a
   pre-existing **structural hedge** that anchors the dealer short-gamma
   profile at $21. Phase 4 GEX should confirm.
2. **5/22 expiry (3 DTE) is being SOLD as a strangle around $20–$21**:
   call OI builds at $21, $21.5, $22, $27 are bid-side dominant (sellers
   writing premium), while put OI builds at $17.5, $19, $20, $20.5 are
   ask-side dominant (BUYERS paying premium). Net: someone is short the
   $17–$22 strangle, someone else is long $17–$20 puts and $24+ calls.
3. **6/18 $16P (+277 OI, bid>ask)** and **2028 $40P (+283 OI, all bid)** are
   being **SOLD** — i.e., the same large players hedging at $21P are also
   harvesting premium far below spot ($16) and on the deep-ITM LEAP wing —
   a **bullish-tilt premium harvester** layered on top of the bear hedge.

Net positioning: **range-bound expectation $16–$22 over the next month**,
with the **5/22 binary event window** creating peripheral wing buyers paying
240% IV for tail upside or downside.

## Key signals

- **6/18 $21 PUT: 16,949 OI** (the chain gorilla; -80 today; $90,468 prev
  premium) — major dealer short-gamma anchor [OI:oi_decrease_with_volume]
- **5/22 $17.5 PUT: +1,300 OI (27.7x change)**, prev_ask_vol 1,202 vs
  bid 45 → **directional bear** open at deep OTM put for 3DTE
  [OI:oi_biggest_increases / oi_smart_positioning]
- **5/22 $20.5 PUT: +1,296 OI (12.7x)**, ask_vol 1,436 vs bid 56 → ATM
  put buying for 3DTE [OI:oi_smart_positioning]
- **5/22 $21.5 PUT: +930 OI**, **bid_vol 800 vs ask 293 → put SELLING**
  (bullish; harvest premium) [OI:oi_smart_positioning]
- **5/22 $21 / $21.5 / $22 / $27 CALLS: bid-dominant OI growth** — all
  inferred as **call SELLING** = covered-call write / call-wall build
  [OI:oi_smart_positioning]
- **6/18 $16 PUT: +277 OI, bid 544 vs ask 126** → **put SELLING** below
  any support level [OI:oi_smart_positioning]
- **2028-01-21 $40 PUT: +283 OI from 124 → 407, ALL bid (ask=0)**, premium
  $682k — single biggest LEAP institutional print is a **PUT WRITER**
  (bullish synthetic) [OI:oi_smart_positioning]
- **`oi_position_rolls`: 0 rolls detected** (single-day window only;
  cross-session rolls invisible) [OI:oi_position_rolls]
- **USAR absent from market-wide pin_risk top-25** (top-25 dominated by
  SPY/QQQ/IWM/HYG/AAPL/NVDA/TSLA for 5/22) and **absent from
  opex_concentration top-30** (USAR's OI is spread across many strikes &
  expiries — no single concentrated cliff) [OI:oi_pin_risk + opex_concentration]

## Detailed findings

### Largest OI increases

Sorted by OI Δ (top 20):

| Strike/Type | Expiry | DTE | OI Δ | Curr OI | Avg Px | Inferred dir | Read |
|-------------|--------|-----|------|---------|--------|--------------|------|
| 17.5 P | 2026-05-22 | 3 | **+1,300** | 1,347 | $0.09 | **bearish** | buying deep-OTM puts |
| 20.5 P | 2026-05-22 | 3 | **+1,296** | 1,398 | $0.51 | bearish | buying ATM puts |
| 21.5 P | 2026-05-22 | 3 | +930 | 1,466 | $0.99 | **bullish** | SELLING ITM puts |
| 20.0 P | 2026-05-22 | 3 | +663 | 1,415 | $0.43 | bearish | buying near-ATM puts |
| 26.0 C | 2026-05-22 | 3 | +501 | 1,418 | $0.29 | bullish | buying lottery calls |
| 24.0 C | 2026-06-05 | 17 | +456 | 538 | $1.04 | bearish | SELLING $24 calls |
| 24.0 P | 2026-07-17 | 59 | +429 | 429 | $4.91 | bullish | SELLING ITM puts |
| 24.0 C | 2026-05-22 | 3 | +364 | 973 | $0.60 | bullish | buying OTM calls |
| 19.0 P | 2026-05-22 | 3 | +331 | 600 | $0.21 | bearish | buying puts |
| 21.0 P | 2026-05-22 | 3 | +325 | 687 | $0.80 | bearish | buying ITM puts |
| 21.0 C | 2026-05-22 | 3 | +311 | 388 | $1.19 | **bearish** | SELLING calls |
| 27.0 C | 2026-05-22 | 3 | +307 | 1,487 | $0.11 | bearish | SELLING calls |
| **40 P 2028** | 2028-01-21 | 612 | **+283** | 407 | $24.10 | **bullish** | SELLING LEAP puts ($682k prem) |
| 16.0 P | 2026-06-18 | 30 | +277 | 2,627 | $0.49 | bullish | SELLING wing puts |
| 22.0 C | 2026-05-22 | 3 | +245 | 550 | $0.94 | bearish | SELLING calls |
| 23.5 C | 2026-05-22 | 3 | +239 | 279 | $0.56 | bullish | buying calls |
| 18.0 P | 2026-05-29 | 10 | +233 | 383 | $0.19 | bearish | buying puts |
| 21.0 C | 2026-06-18 | 30 | +230 | 4,563 | $2.60 | bearish | SELLING calls |
| 21.5 C | 2026-06-18 | 30 | +219 | 219 | $2.60 | bearish | SELLING calls heavily |
| 23.5 C | 2026-05-29 | 10 | +204 | 211 | $0.70 | bullish | buying calls |

### Closing / roll activity

Largest OI decreases:

| Strike/Type | Expiry | DTE | OI Δ | Volume | Note |
|-------------|--------|-----|------|--------|------|
| 30 C | 2026-06-18 | 30 | -751 | 3,007 | Way-OTM 6/18 call exit |
| 20 C 2028 | 2028-01-21 | 612 | -317 | 833 | LEAP call closed/rolled |
| 15 C 2028 | 2028-01-21 | 612 | -280 | 520 | Deep-ITM LEAP call closed (synth unwind) |
| 28 C | 2026-05-22 | 3 | -223 | 923 | 5/22 OTM call wind-down |
| 25 C | 2026-05-22 | 3 | -218 | 1,612 | 5/22 mid-OTM call exit |
| 24 P | 2026-05-22 | 3 | -210 | 773 | 5/22 ITM put close |
| 23.5 P | 2026-05-22 | 3 | -207 | 283 | 5/22 put close |
| 35 C | 2026-09-18 | 122 | -158 | 229 | 9/18 OTM call exit |
| 21 P | 2026-06-18 | 30 | **-80** | 424 | **The $21P wall: marginal trim** |

**`oi_position_rolls`: zero rolls detected** at the 200-contract threshold
on a single-day window. We cannot conclude there's no rolling — only that
nothing fires the same-day signature. Multi-session roll detection would
need to compare today's 6/18 OI increases against last-week's 5/22 OI
decreases, which is outside this tool's scope.

### Smart positioning summary

Counted by inferred direction (top 20 by OI Δ):

- **Bearish**: 11 contracts (puts bought, calls sold, or directional bear
  opens). Total OI Δ: ~5,015 contracts.
- **Bullish**: 8 contracts (puts sold or calls bought). Total OI Δ:
  ~2,890 contracts.
- **Neutral / mixed**: 1.

**Raw count** tilts bearish, but **dollar weight** is more balanced:

- Top bearish premium build: 5/22 $20.5P ask buying ($81k prev premium)
- Top bullish premium build: **2028 $40P all-bid SELL ($682k premium)**
- Top bullish: 6/18 $16P SELL ($38k)
- Top bearish: 5/22 $17.5P BUY (small premium each, large contract count)

When weighted by dollars, the **single biggest institutional commitment of
the day is bullish** (the 2028 $40P sale = synthetic long stock at $40),
which corroborates the phase-2 large-tier `buy_ratio` of 0.623 in the dark
pool. The 5/22 stack is volume-heavy but small-premium-per-contract due to
near-zero theta.

### Pin risk / OPEX concentration

USAR is **not in the top-25 pin_risk** (within 10% of spot, ≤7 DTE) and
**not in the top-30 opex_concentration**. Translation:
- Pin risk is **diffuse** — many strikes have moderate OI; no single strike
  is the dominant magnet.
- The 6/18 $21P (16,949 OI) is the closest thing to a pin anchor, but it's
  30 DTE (out of 5/22 window) and is a PUT (so the pinning dynamic is
  different from the symmetric calls-puts case).
- The 5/22 strangle build implies dealers are **NET SHORT volatility** in
  the 3DTE window — they want spot to land between $19–$21 to harvest
  decay.

### Standing OI snapshot (positions that didn't change today but matter)

| Strike/Type | Expiry | OI | Today's Δ | Significance |
|-------------|--------|----|-----------|----|
| 21 P | 2026-06-18 | **16,949** | -80 | Chain gorilla; dealer short-gamma anchor at $21 |
| 30 C | 2026-06-18 | 12,424 | -751 | Way-OTM speculative call OI (decaying) |
| 15 P | 2026-09-18 | 7,249 | -70 | Tail-hedge holdings, 122 DTE |
| 21 C | 2026-06-18 | 4,563 | +230 | Call-wall being built at $21 |
| 25 P | 2026-09-18 | 3,048 | -79 | ITM long-dated put inventory |
| 17 P | 2026-06-18 | 3,404 | +172 | Lower-end put inventory growing |
| 16 P | 2026-06-18 | 2,627 | +277 | Bull put-write zone |
| 25 P | 2026-05-22 | 1,513 | -45 | 5/22 ITM put inventory |
| 27 C | 2026-05-22 | 1,487 | +307 | 5/22 call-write zone |
| 21.5 P | 2026-05-22 | 1,466 | +930 | Today's biggest put-write build |

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `oi_biggest_increases` | symbol=USAR, top-n=25, min-oi-change=100, date=2026-05-19 | 25 contracts, top OI Δ 5/22 $17.5P +1,300 |
| `oi_decrease_with_volume` | symbol=USAR, top-n=20, min-vol=50, date=2026-05-19 | 20 contracts; top dec 6/18 $30C -751 |
| `oi_smart_positioning` | symbol=USAR, top-n=20, min-oi-change=100, date=2026-05-19 | 11 bearish vs 8 bullish; 2028 $40P bullish stands out at $682k |
| `oi_position_rolls` | symbol=USAR, threshold=200, near-dte-max=30, date=2026-05-19 | **0 rolls** (same-day only) |
| `oi_pin_risk` | top-n=25, dte-max=7, max-distance-pct=10, date=2026-05-19 | USAR absent; top = SPY/HYG/QQQ/IWM/TLT/XLF/NVDA |
| `oi_opex_concentration` | top-n=30, min-concentration-pct=30, date=2026-05-19 | USAR absent; top = micro/single-strike tickers |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** **range-bound / mean-reverting** $16–$22 over
  ~30 days with a **wing-buyer overlay** on 5/22 that could break either
  way for the binary. The single largest dollar commitment is **bullish**
  (2028 $40P sale), tilting medium-term institutional tilt slightly bullish.
- **Conviction:** **3.5/5** — the OI structure is informative and
  internally consistent, but the 5/22 binary creates two-way risk that
  caps directional conviction. Phase 4 GEX will sharpen this.
- **Three pin/cliff strikes for phase-9:**
  1. **$21 = hard ceiling** (16,949 6/18 $21P + growing 6/18 $21C/$21.5C
     call wall + dark pool $21.27 pivot from phase 2). Confluence of three
     independent signals at this strike.
  2. **$20 = magnet for 5/22** — combined put OI at $20 (1,415 OI) + put
     OI at $20.5 (1,398 OI) makes this the strangle-short midpoint. Spot
     is $19.91; the gravity is upward toward $20.
  3. **$17–$17.5 = put-wall floor**. The +1,300 OI build at 5/22 $17.5P
     plus 6/18 $16P/$17P inventory (5,031 combined OI) marks where
     dealers will get long delta from short-put inventory — a buy zone
     below $18.
- **Open questions:**
  - What is the 5/22 binary catalyst? (Phase 7 `insights_earnings_play`
    must determine — most likely earnings date.)
  - Is the **2028 $40P all-bid sale ($682k premium)** a single trader's
    synthetic-long-stock position, or several traders harvesting deep-ITM
    premium? Either way it's the day's biggest bullish dollar commitment.
  - Why is 6/18 $21P at 16,949 OI? When was it built, and what was the
    fill price? (Cannot recover from single-day data; phase 5 historical
    OI trend may help.)
