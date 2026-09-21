# Phase 3 — Open Interest & Positioning

**Ticker:** NVO
**As-of date:** 2026-05-20
**Generated:** 2026-05-20T20:50:00-04:00
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md

## Summary

OI dynamics **confirm the bullish thesis from phases 1 & 2 via a different
mechanism**: today's largest OI build (1,093 contracts at the **June $42.5
put**, ~$158k premium, bid-dominant volume 816 vs 576 ask) is consistent
with an institutional **put-sale establishing a $42.5 floor**.
Long-dated puts at $35 (Jun 2027) and $40 (Jan 2027) also saw bid-side
OI builds — a layered put-write structure that monetizes premium while
defining levels. Counterweight: a 700-contract **bid-side build in the
May 29 $45 calls** is consistent with call-selling, which is mildly
bearish or income-oriented. **NVO is 30 DTE from June OPEX — no pin
risk this week**, but June expiry already carries a 32k-OI **$50C wall**
that will cap acceleration on any rally.

## Key signals

- **Top OI gainer: NVO 2026-06-18 $42.5P, OI 17 → 1,110 (+1,093)**, prev_total_premium $158k, bid_vol 816 vs ask_vol 576 — smart_positioning = **bullish** (puts being sold) [OI:biggest_increases, OI:smart_positioning]
- **NVO 2026-06-18 $50C OI = 32,113** (largest absolute OI on the chain) — dealer call wall capping upside acceleration above $50 unless absorbed [OI:biggest_increases]
- **NVO 2026-06-18 $45C OI = 23,360** + minor build (+262) — the $45 line is heavily traded both today and structurally [OI:biggest_increases]
- **Long-dated put-sale ladder:** $35P Jun 2027 OI 12,441 (+417 today, bid-dominant 447 vs 6); $40P Jan 2027 OI 18,078 (+203, ask 204 vs bid 5) — mixed but the $35P side is clearly bullish floor-writing [OI:biggest_increases, OI:smart_positioning]
- **NVO 2028-01-21 $30C OI +117** with **$524,590 premium traded, ask-side 240 vs bid 5** — long-dated deep-ITM call accumulation (delta ~0.83) consistent with phase-1 LEAP buyer [OI:smart_positioning]
- **No position rolls** detected at threshold=100 [OI:position_rolls]
- **No pin risk** — NVO not within 7-DTE OPEX window; June 19 expiry is 30 days out [OI:pin_risk]

## Detailed findings

### Largest OI increases (filtered to ≥100 contracts)

| Contract | DTE | Prev OI | New OI | ΔOI | Prev ask vol | Prev bid vol | Inferred direction |
|----------|----:|--------:|-------:|----:|-------------:|-------------:|--------------------|
| $42.5P 06/18 | 29 | 17 | 1,110 | **+1,093** | 576 | **816** | **bullish (put sale)** |
| $45C 05/29 | 9 | 930 | 1,629 | +699 | 40 | **696** | **bearish (call sale)** |
| $45P 05/29 | 9 | 188 | 830 | +642 | 13 | **663** | **bullish (put sale)** |
| $40.5P 06/18 | 29 | 17 | 491 | +474 | **201** | 58 | **bearish (put buy)** |
| $35P 06/17/27 | 393 | 12,024 | 12,441 | +417 | 6 | **447** | **bullish (LEAP put sale)** |
| $46.5C 06/18 | 29 | 4 | 357 | +353 | 38 | **275** | bearish (call sale, mild) |
| $50C 07/17 | 58 | 18,071 | 18,411 | +340 | 322 | 274 | bullish-neutral |
| $46C 05/22 | 2 | 1,445 | 1,779 | +334 | **582** | 276 | **bullish (call buy)** |
| $50C 06/18 | 29 | 31,812 | **32,113** | +301 | 410 | **754** | bearish (call sale into wall) |
| $45C 06/18 | 29 | 23,098 | 23,360 | +262 | 188 | **350** | bearish (call sale at strike) |
| $30C 01/21/28 | 611 | 2,551 | 2,668 | +117 | **240** | 5 | **bullish (LEAP call buy)** |
| $40P 01/15/27 | 240 | 17,875 | 18,078 | +203 | **204** | 5 | bearish (put buy) |
| $40P 12/18/26 | 212 | 6,219 | 6,453 | +234 | **217** | 24 | bearish (put buy) |

**Interpretation:** The largest, clearest accumulation is a **June put-write
at $42.5** (premium $158k, 1,093 contracts new OI). The structure across
expiries reads as a deliberate **floor-write strategy**: someone is willing
to be a buyer at $42.5–35 (selling June 42.5P, selling May 29 $45P, selling
June 2027 $35P), while taking moderate downside protection further out via
put buys at $40 (Dec 2026 / Jan 2027). Net bullish on the put side, with
defined hedges.

The bearish counter-pattern is **call-selling/covered-call writing into the
$45 line for May 29 expiry** (699 OI added bid-side), and continued
bid-side adds against the **$50C wall for June** — institutional desks
selling premium against existing long stock, **not initiating short calls**.

### Closing / roll activity (OI decreases with volume)

| Contract | DTE | ΔOI | Volume | Read |
|----------|----:|----:|-------:|------|
| $35P 07/17 | 58 | −503 | 654 | small put closing |
| $55C 06/18 | 29 | −203 | 691 | far-OTM call unwind |
| $50C 01/15/27 | 240 | −178 | 285 | minor unwind |
| $65C 01/15/27 | 240 | −137 | 159 | far-OTM unwind |
| $70P 01/21/28 | 611 | −113 | 145 | deep-ITM 2028 put close |
| $45C 12/17/27 | 576 | −103 | 109 | trivial unwind |
| $50C 01/15/27 | 240 | −178 | 285 | minor unwind |

`oi_position_rolls(threshold=100, near_dte_max=30)` returned **0 rolls
detected** today. Closing activity is light and uncoordinated — no large
position is being unwound that would mark a peak/distribution.

### Smart positioning summary

Aggregated by direction (top 25 OI gainers, weighted by ΔOI):

| Direction | ΔOI sum | Contracts involved |
|-----------|--------:|-------------------:|
| **Bullish (puts sold or calls bought)** | ~2,490 | 8 contracts incl. $42.5P, $45P 05/29, $35P 06/27, $30C 01/28 LEAP, $46C 05/22, $45.5P 06/05, $49.5C 06/18, $46.5C 05/22 |
| **Bearish (puts bought or calls sold)** | ~2,232 | 15 contracts incl. $45C 05/29, $40.5P 06/18, $50C 06/18, $46.5C 06/18, $40P 12/26, $40P 01/27, $44.5C 06/18, $50C 05/22, $47.5C 06/18, $46C 06/18, $50C 08/21, $44.5P 05/22 |

**Bullish narrowly wins on ΔOI (~52% vs 48%)** but the bullish bucket is
**bigger per ticket** (top single position is bullish $42.5P at 1,093 OI vs
bearish top of $40.5P at 474). The structural read: institutional players
are **net-writing the downside** while retail-adjacent flow is **selling
the upside** — a classic accumulation profile where pros gather long-stock
synthetics from below while income-seekers cap the upside.

### Pin risk (OPEX week)

`oi_pin_risk(dte_max=7, max_distance_pct=5)` returned **0 NVO rows**. NVO's
nearest OPEX is **2026-06-19, 30 calendar days out**. No pin commentary this
week. Top pin candidates today are SPY/HYG/TLT/QQQ/IWM — index-driven.

### OPEX concentration

`oi_opex_concentration(min_concentration_pct=40)` returned only micro-cap
single-expiry tickers (VEL, TRVG, PDSB...). NVO is **not** in the top 30 —
its OI is well-distributed across May 22, May 29, Jun 5, Jun 18, Jul 17,
Aug 21, Sep 18, Dec 18, Jan 27, Mar 27, Jun 27, Dec 27, Jan 28 expiries.
**No structural OPEX cliff risk.**

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `oi_biggest_increases` | `{symbol: NVO, date: 2026-05-20, min_oi_change: 100, top_n: 25}` | 25 rows; top is $42.5P 06/18 +1,093 |
| `oi_decrease_with_volume` | `{symbol: NVO, date: 2026-05-20, min_volume: 100, top_n: 20}` | 18 rows; light unwinds, no concentration |
| `oi_smart_positioning` | `{symbol: NVO, date: 2026-05-20, min_oi_change: 100, top_n: 25}` | Net ~52/48 bullish ΔOI by direction inference |
| `oi_position_rolls` | `{symbol: NVO, date: 2026-05-20, threshold: 100, near_dte_max: 30}` | 0 rolls detected |
| `oi_pin_risk` | `{date: 2026-05-20, dte_max: 7, max_distance_pct: 5}` | NVO not in OPEX window |
| `oi_opex_concentration` | `{date: 2026-05-20, min_concentration_pct: 40, top_n: 30}` | NVO not in concentrated list |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** **bullish floor-write structure** with capped upside via call-wall at $50 (June expiry). Net = constructive but rangebound until $50 absorbs.
- **Conviction:** **3.5/5** — the $42.5P put-sale is a clear single-actor positioning signal but represents only $158k traded premium (small notional). The 32k-OI $50C wall is the bigger structural fact.
- **Three pin/cliff strikes for phase-9 entry/stop reference:**
  1. **$42.5 — June put-sale floor.** Sized accumulation here is the "I will buy this" line. Stops below $42 are sound; below $40 is conservative.
  2. **$45 — most-traded line on the chain** (heavy OI both calls and puts; phase-2 DP cluster; phase-1 LEAP synthetic). Pivot for short-term plays.
  3. **$50 — call wall.** First hard resistance from gamma; phase-4 GEX must confirm if dealers are short here. Take-profit zone for trades initiated near $45.
- **Open questions:**
  - Does the $42.5P put-sale show up in larger size on Monday's tape (i.e. is it a recurring program)? Phase 5 historical OI trend will answer.
  - Are the bid-side $50C OI adds covered (against long stock) or naked (limiting upside via gamma)? Phase 4 GEX is the diagnostic.
  - The $40P 12/26 and $40P 01/27 ask-side put **buying** is downside protection ~11% below spot — what catalyst is being hedged out 7–8 months? Phase 6 macro/catalyst must surface (likely U.S. Medicare drug-price negotiation cycle and tirzepatide / compounding-rule expirations).
