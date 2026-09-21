# Phase 3 — Open Interest & Positioning

**Ticker:** AAPL
**As-of date:** 2026-05-20
**Generated:** 2026-05-20T22:30:00Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md

## Summary

OI changes for 2026-05-20 are dominated by **expiration mechanics** —
9 of the top 20 OI increases are 0DTE strikes (5/20 expiry) and another
6 are this-week 5/22 weeklies, with the remainder split between 5/29
weeklies and a small handful of long-dated institutional prints. The
LEAP package from phase-1 is **not visible** in today's OI changes
because OI updates next-session: the 2028-01-21 $300C will show its OI
jump on 2026-05-21's snapshot. The most consequential new positions
visible today are: (a) bullish 5/22 call OI builds at $305 / $307.5 /
$310 — confirming dealers will be short upside gamma over the next 2
sessions; (b) a fresh **1,216-contract bid-side opening of the
2027-01-15 $255 ITM call** for $56.96 avg price (~$6.9M notional) —
reads as a covered-call write against long stock and complements the
LEAP buyer's package; and (c) **AAPL ranks #8 globally in pin risk
with spot $302.30 only 0.76% above the $300 strike** [OI:pin_risk].
Position rolls were not detected single-day [OI:position_rolls] — the
LEAP roll is a cross-session story we will see tomorrow.

## Key signals

- **Pin risk score 515,576 with spot $302.30 vs $300 strike** (0.76% pin
  distance), top strike OI 80,746 (the 6/18 300C) [OI:pin_risk]. Strong
  gamma magnet at $300 into 5/22 weekly + 6/18 monthly.
- **5/22 weekly OI builds skew bullish on the call side:**
  C00305 +1,799 (net ask-bid +1,342), C00310 +1,443 (+1,020),
  C00307.5 +1,127 (+1,291), C00302.5 +2,053 (+684) [OI:smart_positioning].
  Dealers ending the day net short ~6.4k upside call contracts at
  $302.5–$310 — will need to buy stock if AAPL rips.
- **5/22 weekly C00310 OI 24,221** — single largest near-term strike,
  caps reasonable upside through Friday's close [OI:biggest_increases].
- **2027-01-15 $255 ITM call OI +1,216 (was 21, now 1,237)** at $56.96 avg,
  inferred BEARISH (bid-side dominant, net_ask_bid −680)
  [OI:smart_positioning]. Reads as a **covered-call write** by the same
  cohort that bought the 2028 LEAP — premium-income leg of a long-dated
  diagonal.
- **0DTE call sellers visible at $297.5 / $307.5:** C00297.5 net_ask_bid
  −2,554 with +6,040 OI; C00307.5 net_ask_bid −896 with +3,823 OI
  [OI:smart_positioning]. Dealers absorbed call-write flow today —
  bearish-tape interpretation only valid intraday.
- **No same-day position rolls detected (threshold 500)**
  [OI:position_rolls]. The LEAP roll from phase-1 will surface in
  tomorrow's snapshot.

## Detailed findings

### Largest OI increases (top 10)

| Strike / Type | Expiry | DTE | OI Δ | New OI | Volume | Inferred dir |
|---------------|--------|-----|------|--------|--------|--------------|
| 305 C | 2026-05-20 | 0 | +9,583 | 15,897 | 42,124 | bullish (net ab +2,458) |
| 297.5 C | 2026-05-20 | 0 | +6,040 | 11,504 | 39,264 | bearish (net ab −2,554) |
| 307.5 C | 2026-05-20 | 0 | +3,823 | 5,977 | 13,840 | bearish (net ab −896) |
| 297.5 P | 2026-05-20 | 0 | +3,618 | 5,065 | 27,461 | bullish (put selling) |
| 295 P | 2026-05-20 | 0 | +2,685 | 5,598 | 28,374 | bullish (put selling) |
| 310 C | 2026-05-29 | 9 | +2,640 | 8,307 | 4,913 | bearish (net ab −894) |
| 302.5 C | 2026-05-20 | 0 | +2,449 | 9,171 | 52,492 | bullish (net ab +54) |
| 310 C | 2026-05-20 | 0 | +2,294 | 4,693 | 6,998 | bearish (net ab −155) |
| 300 C | 2026-05-20 | 0 | +2,134 | 9,882 | 95,378 | bullish (net ab +588) |
| 302.5 C | 2026-05-22 | 2 | +2,053 | 9,821 | 10,877 | bullish (net ab +684) |

Non-expiration standouts (DTE ≥ 2):

| Strike / Type | Expiry | DTE | OI Δ | Avg price | Note |
|---------------|--------|-----|------|-----------|------|
| 297.5 C | 2026-05-22 | 2 | +1,854 | $3.18 | net ab −2,729 → call writers |
| 305 C | 2026-05-22 | 2 | +1,799 | $1.04 | bullish (+1,342) |
| 295 P | 2026-05-22 | 2 | +1,512 | $1.74 | bullish (put sellers) |
| 310 C | 2026-05-22 | 2 | +1,443 | $0.35 | bullish (+1,020) |
| 530 C | 2026-09-18 | 121 | +1,419 | $0.04 | far-OTM lotto |
| 255 C | 2027-01-15 | 240 | **+1,216** | **$56.96** | **ITM covered call write** |
| 320 C | 2026-05-26 | 6 | +1,206 | $0.06 | far-OTM lotto |
| 307.5 C | 2026-05-22 | 2 | +1,127 | $0.51 | bullish (+1,291) |

### Closing / roll activity (top decreases)

| Strike / Type | Expiry | DTE | OI Δ | Avg price | Note |
|---------------|--------|-----|------|-----------|------|
| 300 C | 2026-06-18 | 29 | −2,850 | $7.42 | June monthly ITM call closing — possible partial leg of the LEAP roll |
| 305 C | 2026-07-17 | 58 | −2,215 | $9.03 | July OTM call closing |
| 270 P | 2026-05-29 | 9 | −961 | $0.20 | small short-dated put close |
| 265 P | 2026-06-05 | 16 | −455 | $0.38 | weekly put close |
| 310 C | 2026-06-18 | 29 | −435 | $3.68 | June OTM call close |

`oi_position_rolls` returned **0 detected rolls** at threshold 500
[OI:position_rolls]. **Caveat:** single-day detection only — the LEAP
package (phase-1: $24.7M 190C 6/18 bid + $29.5M 200C 12/18 bid + $54.1M
300C 2028 ask) is a cross-session roll that will appear in tomorrow's
snapshot when 2028 OI prints.

### Smart positioning (top inferences)

The full `oi_smart_positioning` table flagged 13 bullish and 7 bearish
positions in the top 20. **Bullish premium** is concentrated in:
0DTE 305C (lotto + call buyers into close), 5/22 305C/307.5C/310C
(upside builds), put-selling at 295/297.5 (high-confidence rotation
into income from put writers, supports the floor), and the 9/18
530C far-OTM lotto.

**Bearish premium** concentrates in 0DTE 297.5C/307.5C (call writers
collecting decay) and the 5/29 310C +2,640 OI bearish (call writers
capping the next-week upside) — these are decay-harvesting trades, not
directional shorts.

### Pin risk

AAPL ranks **#8 globally** in pin risk score (515,576) within the 7-day
OPEX window [OI:pin_risk]:

| Field | Value |
|-------|-------|
| Spot | $302.30 |
| Nearest high-OI strike | $300 |
| Pin distance | 0.76% |
| Top strike OI (6/18 300C) | 80,746 |
| Total OI in 7-DTE window | 1,168,091 |
| DTE to opex (next weekly) | 0 (5/20) → 2 (5/22) |

**Interpretation.** AAPL has the structural pin force of an
options-heavy mega-cap into a weekly OPEX, with $300 as the magnet
strike. Combined with phase-2's $302.25 DP clearing print, the most
likely path for Thursday–Friday is **chop in the $299–$303 band**
with mean reversion to $300–$301 by Friday's close.

### OPEX concentration

`oi_opex_concentration` returned only small-cap penny stocks
(APYX, BWMN, etc.) at 100% concentration. AAPL did not surface — its
OI is **well-distributed** across multiple expiries (5/22 weekly,
6/18 monthly, 7/17 monthly, Jan-27 / Jan-28 LEAPs), which is healthy
and means there's **no single-expiry OPEX cliff risk** for AAPL in
the next 90 days.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__oi_biggest_increases` | `{symbol: AAPL, top-n: 20, min-oi-change: 500, date: 2026-05-20}` | 20 rows; 9 are 0DTE, 6 are 5/22, 5 longer-dated |
| `mcp__uw-pp__oi_decrease_with_volume` | `{symbol: AAPL, top-n: 15, min-volume: 100, date: 2026-05-20}` | 6/18 300C −2,850 largest; 7/17 305C −2,215 |
| `mcp__uw-pp__oi_smart_positioning` | `{symbol: AAPL, top-n: 20, min-oi-change: 500, date: 2026-05-20}` | 13 bullish / 7 bearish; mostly expiration mechanics |
| `mcp__uw-pp__oi_position_rolls` | `{symbol: AAPL, threshold: 500, near-dte-max: 30, date: 2026-05-20}` | 0 rolls detected single-day |
| `mcp__uw-pp__oi_pin_risk` | `{top-n: 25, dte-max: 7, max-distance-pct: 5, date: 2026-05-20}` | AAPL #8, pin score 515k, $300 strike 0.76% from spot |
| `mcp__uw-pp__oi_opex_concentration` | `{top-n: 20, min-concentration-pct: 40, date: 2026-05-20}` | AAPL not present — diversified expiry profile |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** **mildly bullish for 2–5 day window** (5/22
  weekly C-side builds 30:5 bullish:bearish in net ask-bid terms); **pin
  to $300** for the very near term.
- **Conviction:** 3 / 5. Most of today's OI moves are expiration noise.
  The long-dated 2027 255C bid-side opening is genuinely institutional
  but small ($6.9M) relative to phase-2's $1B+ DP signal.
- **Three pin/cliff strikes for phase-9 reference:**
  1. **$300** — primary pin (5/22 + 6/18 OI mass, DP $300.23 cluster).
  2. **$302.25 / $302.50** — today's DP clearing price + 5/22 C00302.50
     OI 9,821 — battleground level.
  3. **$310** — 5/22 C00310 OI 24,221 (biggest near-term strike) =
     upside resistance / dealer short-gamma cliff if pierced.
- **Open questions:**
  - Tomorrow's snapshot will show the 2028 LEAP OI build — phase-9 should
    plan to re-pull `oi_biggest_increases` next session and verify.
  - The 5-day bearish sweep persistence (phase-1) is **not visible** in
    today's OI — it was likely intraday roll-and-close activity that
    doesn't accumulate. Phase 5 historical_cumulative_premium_flow
    should resolve whether the bearish-direction tag was net-new
    short-side premium or just sweep mechanics.
