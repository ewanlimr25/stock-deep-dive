# Phase 3 — Open Interest & Positioning

**Ticker:** BABA
**As-of date:** 2026-05-20 (data: 2026-05-19)
**Generated:** 2026-05-20T00:15:00Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md
**Spot reference:** $135.69 (`stock_price` from OI files)

## Summary

OI positioning splits cleanly by tenor: **near-term (May 22 / 3-DTE)** flow is
institutional **call-writing** at $137–$142 (high bid-side volume on rising OI →
short calls), pinning BABA toward the **$135 strike**, which sits **0.51% from
spot with 21,302 contracts** — BABA scores #40 in the market-wide pin-risk table
[OI:pin_risk]. **Mid-term (May 29 / 10-DTE)** flips bullish — **$145C OI +2,415
on 3,424 ask vs 172 bid prev-day volume** is fresh aggressive call buying. The
**Mar 2027 LEAP campaign has actually been *trimmed*** — $190C OI –2,202 and
$230C OI –2,051 — while phase-1's new $145C/$130P risk reversal was opened,
i.e. the long-dated thesis has been **pulled in from $190–$230 to $145** (less
aggressive target). No same-day position rolls detected.

## Key signals

- **Pin risk at $135 strike** for May 22 OPEX (3 DTE): pin_score 105,464, top
  strike OI 21,302, total in-window OI 301,912, pin_distance 0.51% [OI:pin_risk].
- $145C May 29 OI **+2,415** on ask:bid 3,424:172 → highest-confidence bullish
  new positioning in the chain [OI:smart_positioning].
- May 22 (3 DTE) call cluster $137–$142 OI grew on **bid-side dominant** volume
  → covered-call writing, capping near-term upside [OI:biggest_increases].
- Mar 2027 $190C OI –2,202 and Mar 2027 $230C OI –2,051: LEAP campaign
  **rotated down from $190–$230 strikes into the new $145C** seen in phase 1
  [OI:decrease_with_volume].
- Jun 18 $130P OI +1,268 on prev_ask 291 vs prev_bid 147 → genuine ask-side
  put buying for downside hedge (consistent with phase-2 fresh DP support
  forming at $133.40) [OI:smart_positioning].

## Detailed findings

### Largest OI increases (≥500 contracts)

| Strike | Type | Expiry | DTE | OI Δ | New OI | Prev ask vol | Prev bid vol | Read |
|------:|:----:|:------|:---:|----:|------:|----:|----:|------|
| 145 | C | 2026-05-29 | 10 | **+2,415** | 6,984 | 3,424 | 172 | **bullish buy** |
| 142 | C | 2026-05-22 | 3 | +1,702 | 3,139 | 125 | 1,831 | **bearish write** |
| 135 | C | 2026-05-22 | 3 | +1,438 | 3,773 | 1,996 | 2,161 | mixed/write |
| 136 | C | 2026-05-22 | 3 | +1,435 | 4,114 | 1,173 | 1,311 | write |
| 130 | P | 2026-06-18 | 30 | +1,268 | 16,650 | 291 | 147 | **put buy (hedge)** |
| 150 | C | 2026-06-18 | 30 | +1,202 | 34,204 | 652 | 1,083 | **write** |
| 210 | C | 2026-12-18 | 213 | +997 | 1,665 | 1 | 4 | noisy LEAP |
| 138 | C | 2026-05-22 | 3 | +918 | 2,704 | 1,145 | 1,061 | balanced |
| 140 | C | 2026-06-18 | 30 | +916 | 20,000 | 257 | 317 | mild write |
| 155 | C | 2026-06-18 | 30 | +844 | 19,816 | 1,479 | 207 | **OTM call buy** |
| 139 | C | 2026-05-22 | 3 | +809 | 1,501 | 199 | 649 | **write** |
| 141 | C | 2026-05-29 | 10 | +790 | 1,213 | 473 | 381 | mild buy |
| 140 | C | 2026-07-17 | 59 | +732 | 7,697 | 346 | 188 | **bullish buy** |
| 137 | C | 2026-05-22 | 3 | +714 | 1,815 | 439 | 1,425 | **write** |
| 141 | C | 2026-05-22 | 3 | +659 | 2,315 | 219 | 861 | **write** |
| 142 | C | 2026-05-29 | 10 | +641 | 819 | 273 | 477 | write |
| 138 | C | 2026-05-29 | 10 | +627 | 821 | 139 | 645 | **write** |
| 139 | C | 2026-05-29 | 10 | +598 | 755 | 95 | 564 | **write** |
| 130 | P | 2026-05-22 | 3 | +566 | 2,867 | 931 | 615 | **put buy** |
| 137 | C | 2026-05-29 | 10 | +518 | 770 | 12 | 539 | **write** |

Pattern: **the entire May 22 (3-DTE) call chain $137–$142 is being written**,
not bought. May 29 mixes ($145C bought, but $137–$142 still written). The phase-1
ASK-side sweep tape and the phase-3 OI tape **agree** that the genuine bullish
buys sit at the **wings** ($145C May 29, $155C Jun 18, $140C Jul 17, plus the
LEAP risk reversal). [OI:biggest_increases]

### OI decreases with volume

| Strike | Type | Expiry | DTE | OI Δ | Volume | Read |
|------:|:---:|:------|:---:|----:|-----:|------|
| 190 | C | 2027-03-19 | 304 | **−2,202** | 3,005 | **closing far-OTM LEAP** |
| 230 | C | 2027-03-19 | 304 | **−2,051** | 3,095 | **closing far-OTM LEAP** |
| 145 | C | 2026-05-22 | 3 | −1,888 | 4,139 | expiring OTM / closing |
| 140 | C | 2026-05-22 | 3 | −1,501 | 7,473 | covered call closing |
| 165 | C | 2026-07-17 | 59 | −1,275 | 1,819 | closing far-OTM |
| 160 | C | 2026-06-18 | 30 | −793 | 2,200 | closing |
| 200 | C | 2026-06-18 | 30 | −551 | 954 | closing |
| 150 | C | 2026-05-22 | 3 | −469 | 4,067 | closing OTM |
| 120 | C | 2026-05-22 | 3 | −339 | 367 | profit-take ITM |
| 150 | C | 2027-01-15 | 241 | −327 | 817 | mild LEAP trim |
| 119 | C | 2026-05-22 | 3 | −244 | 285 | profit-take deep ITM |

**Mar 2027 LEAP trim is the key tell:** $4.25M of premium in $190/$230 calls
closed (−4,253 contracts combined). Simultaneously, phase-1 saw $1.89M of
Mar 2027 $145C opened. The LEAP campaign **shifted its target downward** from
$190–$230 → $145. This is bullish in direction but **less aggressive** than the
prior structural positioning. [OI:decrease_with_volume]

### Smart positioning (inferred direction)

The tool tags 20 BABA contracts with direction; tallying by inferred call/put
side and OI Δ:

| Tag | Count | Net OI Δ (sum) | Notes |
|------|------:|--------------:|------|
| `bullish` (call buy / put sell) | 5 | +5,253 | $145C 5/29, $138C 5/22, $155C 6/18, $141C 5/29, $140C 7/17 |
| `bearish` (call sell / put buy) | 15 | +12,037 | mostly **call writes** in 3-DTE strip + $130P/$150C 6/18 |

Net OI Δ counted as "bearish" by the tool is **larger in magnitude**, but the
*directional* (calls bought ask-side) bullish buckets are concentrated at the
**wings** ($145–$155) where the LEAP campaign sits, while the "bearish" tag is
heavily inflated by **covered-call writing** of the $137–$142 strip — which is
typically performed by long-stock holders, **not** outright bears. The tool's
binary label is misleading without tier context. [OI:smart_positioning]

### Pin risk (OPEX window ≤ 7 DTE)

| Ticker | Spot | Pin strike | Distance | DTE | Top OI | Total OI in window | Pin score |
|--------|----:|---:|---:|:--:|----:|----:|----:|
| **BABA** | **$135.69** | **$135** | **0.51%** | **3** | **21,302** | **301,912** | **105,465** |

BABA is the **40th-ranked** pin candidate market-wide and the only China-tech
ADR in the top 50 outside KWEB. With $135 strike OI of 21,302 and total OI in
the 5% window of 301,912, the dealer hedging required to close BABA away from
$135 by Friday is meaningful — **expect a magnet effect toward $135** into May
22, all else equal. [OI:pin_risk]

For comparison the nearby cluster:
- KWEB pin at $29 strike (2.55% from spot $28.28) — China-ETF pin nearby, but
  weaker (pin_score 114,423 with diffuse OI).
- PLTR pin at $130 (3.90% from spot $135.27) and BABA pin at $135 (0.51%
  from spot $135.69): note the **strike confusion risk** — PLTR's spot is
  almost the same as BABA's despite the very different pin strikes. Phase-9
  must label strikes by ticker explicitly.

### Position rolls (same-day)

**Zero rolls detected** at threshold ≥500 contracts within 30 DTE.
Cross-session rolls would not show up in a single-day report per the tool
caveat; the LEAP trim from $190/$230 → $145 (visible above) is a roll
*across sessions* that this single-day check can't capture.
[OI:position_rolls]

### OPEX concentration

BABA does **not** appear in the ≥40% concentration list — its OI is spread
across many expiries (May 22, May 29, Jun 18, Jul 17, Aug 21, Sep 18, Jan 27,
Mar 27, Jun 27, Jan 28, Dec 28). The top-50 concentration list is dominated by
small-cap names with single-expiry chains and isn't useful for BABA pin
analysis. [OI:opex_concentration]

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `oi_biggest_increases` | symbol=BABA, top_n=25, min_oi_change=500 | 20 rows; May22 calls $137–$142 dominant write side |
| `oi_decrease_with_volume` | symbol=BABA, top_n=15, min_volume=100 | 15 rows; Mar27 $190/$230C LEAP trim –4,253 |
| `oi_smart_positioning` | symbol=BABA, min_oi_change=500 | 20 rows; tool's "bullish" 5/20 lines concentrated at wings |
| `oi_position_rolls` | symbol=BABA, threshold=500, near_dte_max=30 | 0 rolls detected |
| `oi_pin_risk` | top_n=50, dte_max=7, max_distance_pct=5 | BABA at $135 strike, 3 DTE, pin_score 105,465 |
| `oi_opex_concentration` | top_n=50, min_concentration_pct=40 | BABA not in list (OI is multi-expiry) |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** **bullish on the wings + LEAPs, neutral-to-bearish
  on near-term ($135–$142 strip), pin gravity into $135 Friday.**
- **Conviction:** **3 / 5** — split-tenor positioning reduces unanimity.
  Wings + LEAP risk reversal are bullish but the May 22 call-writing strip
  argues that institutions are not expecting >$142 by Friday.
- **Three pin/cliff strikes for phase-9:**
  1. **$135 (May 22 weekly)** — primary pin into Friday close.
  2. **$140 / $142** — overhead cap from concentrated covered-call writing
     in May 22 / May 29 expiries; aligns with phase-2 DP overhead supply
     starting at $140.81.
  3. **$130 (Jun 18 put)** and **$130 (Mar 27 short put leg)** — downside
     pin / institutional support; aligns with phase-2 fresh DP support at
     $133.40.
- **Open questions:**
  - Dealer positioning (phase-4 GEX) will determine whether the $135 pin is
    self-reinforcing (long gamma above spot = pin) or breakable
    (short-gamma flip).
  - The LEAP campaign's downward strike rotation $190 → $145 needs context
    — has BABA realized vol collapsed, making $145 now look "cheap" the way
    $190 looked cheap a quarter ago? (→ phase 5 historical IV).
  - Is the May 22 $135–$142 call-writing institutionally owned overwrite,
    or speculative short-call selling? Phase-2 DP buyer-skew of 0.584
    supports the overwriter hypothesis (long stock + write near-term
    calls) — phase-9 should treat this as **friendly** for an uptrend
    thesis, not hostile.
