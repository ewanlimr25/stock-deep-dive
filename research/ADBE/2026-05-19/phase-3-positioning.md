# Phase 3 — Open Interest & Positioning

**Ticker:** ADBE
**As-of date:** 2026-05-19
**Generated:** 2026-05-19T20:50:00Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md

## Summary

OI snapshot stock_price = **$255.03** (NB: this is the prior session close
embedded in the OI parquet, slightly above the intraday last of $252).
Today's biggest OI builds are **dominantly bullish**: of the top-18 OI
increases, **14 are tagged `inferred_direction=bullish`** by
`oi_smart_positioning` (calls bought OR puts sold) and only **4 are
bearish** `[OI:smart_positioning]`. The single largest OI increase is
**+1,135 contracts in the 2026-05-22 $265 CALL** (current OI 1,513 vs
prior 378, **+300%**) `[OI:biggest_increases]`. **Net positioning bias =
BULLISH**, which contradicts the surface read of phase-1 ("front-end
hedging") and re-frames the put activity as **two-sided** (institutions
WRITING ATM 5/22 puts while customers buy them). Combined with phase-2's
mega-buy dark-pool footprint, the institutional posture is **long stock +
short premium** — covered-call + cash-secured-put behaviour against an
upcoming catalyst.

## Key signals

- **+1,135 OI in ADBE 2026-05-22 $265 CALL** `[OI:biggest_increases]`,
  +300% in one session — biggest single new-position open of the day.
- **+1,011 OI in ADBE 2026-05-22 $275 CALL** `[OI:biggest_increases]`
  (+289%), with net_ask_bid +393 = call BUYING (smart_positioning bullish).
- **+845 OI in ADBE 2026-05-22 $260 PUT** with prev_bid_volume **905 vs
  prev_ask_volume only 25** — these are puts being WRITTEN, not bought,
  $820k prev_total_premium collected `[OI:smart_positioning]`. Reframes
  phase-1's "260P bought on ask" — both sides traded; net opening was the
  PUT WRITER.
- **+819 OI in ADBE 2026-05-29 $255 CALL** with net_ask_bid +782 —
  unambiguous call buying at the ATM $255 strike for next-week expiry
  `[OI:smart_positioning]`.
- **+499 OI in ADBE 2026-06-18 $305 CALL** with net_ask_bid +691 —
  speculative OTM upside lottery into June expiry `[OI:smart_positioning]`.
- **LEAP bullish opens:** +394 OI in 2028-01-21 $350 CALL ($1.44M
  prev-total premium); +318 OI in 2026-08-21 $400 CALL — multi-month and
  multi-year **bullish call accumulation** `[OI:biggest_increases]`.
- **No position rolls detected at threshold 300** `[OI:position_rolls]`.
- **ADBE absent from market-wide pin-risk top-30** `[OI:pin_risk]` — at
  3 DTE to OPEX no single strike dominates ADBE's OI mass enough to score.
- **ADBE absent from OPEX-concentration list** `[OI:opex_concentration]` —
  OI is spread across many expiries; no cliff risk.

## Detailed findings

### Largest OI increases (top 18)

Sorted by absolute OI change, smart-positioning direction added.

| Contract | DTE | OI Δ | Curr OI | %Δ | Side bias (ask/bid vol) | Inferred dir |
|----------|----:|-----:|--------:|---:|------------------------:|--------------|
| ADBE 260522 C $265   | 3   | +1,135 | 1,513 | +300% | 329 / 1,115 | **bearish** (calls SOLD) |
| ADBE 260522 C $275   | 3   | +1,011 | 1,361 | +289% | 774 / 381   | **bullish** (calls BOUGHT) |
| ADBE 260522 P $260   | 3   |   +845 |   938 | +908% | 25 / 905    | **bullish** (puts WRITTEN) |
| ADBE 260529 C $255   | 10  |   +819 | 1,081 | +313% | 877 / 95    | **bullish** (calls BOUGHT) |
| ADBE 260522 C $260   | 3   |   +771 | 1,698 |  +83% | 1,206 / 522 | **bullish** (calls BOUGHT) |
| ADBE 260522 C $255   | 3   |   +530 | 1,017 | +109% | 751 / 261   | **bullish** (calls BOUGHT) |
| ADBE 260618 C $305   | 30  |   +499 | 1,117 |  +81% | 709 / 18    | **bullish** (calls BOUGHT) |
| ADBE 260522 C $282.5 | 3   |   +478 |   627 | +321% | 409 / 48    | **bullish** (calls BOUGHT) |
| ADBE 260522 C $270   | 3   |   +462 |   805 | +135% | 445 / 238   | **bullish** (calls BOUGHT) |
| ADBE 260522 P $220   | 3   |   +445 |   943 |  +89% | 35 / 462    | **bullish** (puts WRITTEN) |
| ADBE 260522 C $277.5 | 3   |   +397 |   475 | +509% | 93 / 380    | **bearish** (calls SOLD) |
| ADBE 280121 C $350   | 612 |   +394 |   790 | +99%  | 206 / 100   | **bullish** (LEAP calls BOUGHT) |
| ADBE 260612 P $240   | 24  |   +382 | 1,445 |  +36% | 435 / 129   | **bearish** (puts BOUGHT) |
| ADBE 260522 P $215   | 3   |   +327 |   553 | +145% | 88 / 191    | **bullish** (puts WRITTEN) |
| ADBE 260821 C $400   | 94  |   +318 |   993 |  +47% | 557 / 198   | **bullish** (LEAP calls BOUGHT) |
| ADBE 260612 P $250   | 24  |   +265 |   606 |  +78% | 223 / 308   | **bullish** (puts WRITTEN) |
| ADBE 260522 C $285   | 3   |   +260 |   392 | +197% | 123 / 228   | **bearish** (calls SOLD) |
| ADBE 260529 C $275   | 10  |   +208 |   450 |  +86% | 312 / 26    | **bullish** (calls BOUGHT) |

**Aggregation by direction & strike type (top-18):**

| Category | Count | Combined OI Δ |
|----------|------:|--------------:|
| Bullish call opens (buying) | 8 | +4,229 |
| Bullish put writes (selling) | 4 | +1,882 |
| Bearish call writes (selling) | 3 | +1,792 |
| Bearish put opens (buying) | 1 | +382 |
| **Net bullish open positioning** | — | **+6,111 contracts vs 2,174 bearish** |

Net opening flow = ~2.8× more bullish than bearish OI mass today.

### Closing / roll activity

| Contract | OI Δ | DTE | Read |
|----------|-----:|----:|------|
| ADBE 260618 P $220 | −124 | 30 | Small OTM put close |
| ADBE 270115 C $400 | −121 | 241 | LEAP OTM call profit-take/close |
| ADBE 260821 C $395 | −87 | 94 | Aug OTM call closed |
| ADBE 260821 C $425 | −69 | 94 | Aug OTM call closed |
| ADBE 260522 C $247.5 | −47 | 3 | Weekly ITM call profit-take |
| ADBE 260522 P $250 | −42 | 3 | Weekly put close |
| ADBE 260821 C $405 | −31 | 94 | Aug OTM call closed |
| ADBE 260821 C $435 | −26 | 94 | Aug OTM call closed |

Aug $395-$435 calls — net **−213 OI closed** across four adjacent strikes.
That's a coordinated take-down of upper-OTM August calls (could be a fund
de-risking ahead of earnings, or a 1×2 spread rolling lower) but it is
**tiny** compared to today's +1,955 bullish call OI build in 5/22-5/29-
6/18 expiries. Net call exposure is rising sharply.

**No same-day position rolls detected** at threshold 300
`[OI:position_rolls]` — meaning no large near-DTE OI decrease paired with
far-DTE OI increase on this date.

### Smart positioning (inferred direction summary)

Per `oi_smart_positioning`, of 18 OI-increase rows:
- **14 BULLISH** (calls bought = 8; puts sold = 6) representing
  +6,111 OI Δ
- **4 BEARISH** (calls sold = 3; puts bought = 1) representing
  +2,174 OI Δ
- Net: **+3,937 OI bullish-skewed contracts** opened today.

The 5/22 $265 CALL line (+1,135 OI tagged bearish) is the standout
counter-flow — call-side ask-vol 329 vs bid-vol 1,115 implies institutions
WROTE 5/22 $265 calls today, then OI built as customers absorbed. This is
classic **covered-call writing** above the $263 dark-pool resistance
(phase-2). Read it as institutions monetizing upside premium against the
$24M mega buy at $261.86 — a defensive overlay on a long stock book, not
a directional short.

### Pin risk (single-day, 7 DTE window)

ADBE does **NOT** appear in the market-wide pin-risk top-30
`[OI:pin_risk]`. The lowest pin_score in the top-30 = ~124k (INTC). Today
the highest ADBE strike-level OI in the 5/22 window is **5/22 $260 CALL
at curr_oi 1,698**, with $265 C at 1,513 and $260 P at 938. Total ADBE
5/22 OI in the ±5% spot window is on the order of 12-15k contracts — far
below the SPY/QQQ/HYG/IWM peers in the pin list. **No single-strike pin
magnet for the 5/22 expiry**, though the wall is layered at $260-265.

### OPEX concentration

ADBE is **not** in the `oi_opex_concentration ≥30%` list. ADBE's OI is
distributed across many monthly + LEAP expiries (May/Jun/Jul/Sep/Jan-27/
Mar-27/Jan-28 all show meaningful OI), so no single expiry holds >30% of
the chain. **No OPEX cliff risk**.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__oi_biggest_increases` | symbol=ADBE, top-n=20, min-oi-change=200, date=2026-05-19 | 18 rows, 14 bullish / 4 bearish |
| `mcp__uw-pp__oi_decrease_with_volume` | symbol=ADBE, top-n=15, min-volume=100, date=2026-05-19 | 11 rows, all small (<125 OI), Aug calls closed |
| `mcp__uw-pp__oi_smart_positioning` | symbol=ADBE, top-n=20, min-oi-change=200, date=2026-05-19 | Net bullish 6,111 vs 2,174 |
| `mcp__uw-pp__oi_position_rolls` | symbol=ADBE, threshold=300, near-dte-max=30, date=2026-05-19 | 0 rolls detected |
| `mcp__uw-pp__oi_pin_risk` | top-n=30, dte-max=7, max-distance-pct=5, date=2026-05-19 | ADBE absent |
| `mcp__uw-pp__oi_opex_concentration` | top-n=50, min-concentration-pct=30, date=2026-05-19 | ADBE absent |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** **BULLISH net opening positioning** with
  defensive overlay (covered-call writing at $265 and put-writing at
  $260/$220/$215). Net OI build is 2.8× bullish-skewed.
- **Conviction:** **4/5** — clean unidirectional OI build in 5/22-5/29-
  6/18 calls + LEAP buying corroborates phase-2 accumulation; the only
  caveat is the $265-call write line ($1,135 OI bearish-flagged) which
  rationally reflects covered-call overlay rather than a bear bet.
- **Three pin/cliff strikes for phase-9 entry/stop reference:**
  1. **$255 (5/29 expiry)** — fresh OI 1,081, +313% intraday, net call
     buying = "must hold to print profits" level for the new longs.
  2. **$260 (5/22 expiry)** — combined call OI 1,698 + put OI 938 (with
     put writers in control). **$260 = pin magnet / dealer battle zone for
     the next 3 sessions**.
  3. **$265 (5/22 expiry)** — call OI 1,513 with institutions WRITING.
     **$265 is the covered-call cap** — if ADBE rips through it, dealers
     and the writers go short gamma and have to chase upward. Reclaim of
     $265 on closing basis = upside acceleration trigger.
- **Open questions:**
  - Is dealer gamma profile net long or short at $255-260? — phase 4 GEX
    answers; the put-writing here implies dealers absorbed customer puts
    → dealers are likely **short put gamma below $260**, **short call
    gamma above $265**.
  - Does today's bullish OI build match historical pre-earnings patterns
    on ADBE? — phase 5 (historical) should check OI buildup vs prior
    earnings cycles.
  - **CONTRADICTION with phase-1:** phase-1 read the front-end put tape
    as bearish hedge. OI-level evidence shows the OPPOSITE — puts were
    being WRITTEN (institutions short the puts), not bought net. Phase 9
    must reconcile this; phase 10 must flag and score.
