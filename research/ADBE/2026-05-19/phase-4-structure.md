# Phase 4 — Dealer Structure & Gamma

**Ticker:** ADBE
**As-of date:** 2026-05-19
**Generated:** 2026-05-19T21:10:00Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-3-positioning.md

## Summary

ADBE sits **on the gamma knife's edge**: Zero Gamma Level = **$259.48**
vs underlying $258.07 in the GEX snapshot (DEX/vanna snapshots show
$260.63/$260.43) — spot is ~$1 BELOW ZGL, so the 45-DTE regime is
technically **NEGATIVE GAMMA** by ~0.5% `[STRUCT:gex]`. However, total
GEX is large-positive **$1.57B** and the per-strike GEX flips sharply
positive at **$247.5 / $255 / $260 / $265 / $270**, with **$260 = the
single largest GEX wall at +$484M** `[STRUCT:gex]`. Net DEX is **+$39.7B**
implying public is **net call-long** → dealers must **BUY underlying** to
hedge: a structural bid `[STRUCT:dex]`. Term structure is **BACKWARDATION
with a U-shape**: 5/22 IV 62.0% (highest, expiry-pin), trough at
5/29-6/05 ~47%, then a **clear earnings kink at 6/12-6/18 (57.5%/57.2%)**
`[STRUCT:iv_term_structure]`. 30-day **25Δ skew is COMPLACENT** (put/call
1.006) — no crash-hedging panic `[STRUCT:term_skew]`. Vanna is negative
($-178k net) — a vol crush would force dealer SELLING via hedge unwind
`[STRUCT:vanna_charm]`. **Net structural read: long-gamma SUPPORT at
$260, gamma FLIP at $259.48, dealer accumulation bid below via DEX,
vanna risk INTO an IV-drop event.**

## Key signals

- **Zero Gamma Level $259.48 vs spot $258.07 (Δ = -$1.41 = -0.55%)**
  `[STRUCT:gex]` — knife-edge regime. Reclaim and hold above $259.48 →
  dealer long-gamma mean-reversion kicks in.
- **GEX wall at $260 = +$484M** (single largest strike, ~7× any other
  near-spot strike) `[STRUCT:gex]` — magnet for spot, dealer support for
  any pullback below.
- **Secondary walls $265 (+$348M), $270 (+$336M), $275 (+$218M)**
  `[STRUCT:gex]` — laddered resistance/support; each acts as a dealer
  damper if breached.
- **Net DEX +$39.7B = dealer hedge demand to BUY shares**
  `[STRUCT:dex]` — structural bid that explains phase-2's mega dark-pool
  buyer paying $4.71 over mid.
- **Term-structure earnings KINK at 6/12-6/18 (57%-58% IV vs 47% trough
  at 6/05)** `[STRUCT:iv_term_structure]` — confirms an event is priced
  for the second June expiry window (Adobe Q2 fiscal historically reports
  mid-June; phase 6 will verify the date).
- **30-day skew COMPLACENT (put/call ratio 1.006, skew +0.0033)**
  `[STRUCT:term_skew]` — no fear-bid in puts despite phase-1's put-tape
  noise; corroborates phase-3's put-WRITING reframe.
- **Front-end IV ratio (7d:30d) = 0.838 = CONTANGO**
  `[STRUCT:front_end_iv_ratio]` — 30-day IV richer than 10-day, which is
  the earnings expiry premium, not stress.
- **Today (5/22) expiry-only zero-gamma = $152.73, regime POSITIVE; spot
  $260.43 sits FAR above ZGL** `[STRUCT:today_gamma_flip]` — for the
  3-DTE 5/22 expiry alone, dealers are deep LONG gamma; **$260 is a hard
  magnet for the next 3 sessions**.
- **Net vanna NEGATIVE ($-178,550)** — a post-event IV crush triggers
  dealer hedge unwind (sell underlying) `[STRUCT:vanna_charm]`.

## Detailed findings

### GEX (45-DTE, per-strike top features)

| Strike | Net GEX ($) | Role |
|-------:|------------:|------|
| 220 | **−184.5M** | DEEP put wall (negative gamma cliff) |
| 230 | **−66.6M**  | Negative GEX shelf |
| 240 | **−101.8M** | Negative GEX shelf |
| 245 | **−55.5M**  | Last negative wall before flip |
| **247.5** | **+60.2M** | **First positive-gamma strike** |
| 252.5 | −5.6M | Small dip |
| 255 | +70.8M | First major positive wall |
| 257.5 | +23.6M | |
| **260** | **+484.0M** | **MEGA gamma wall (max)** |
| 262.5 | +51.7M | |
| **265** | **+347.5M** | Secondary mega wall |
| 267.5 | +11.7M | |
| **270** | **+335.9M** | Tertiary mega wall |
| 275 | +217.7M | |
| 280 | +134.0M | |
| 285 | +21.1M | |
| 290 | +56.7M | Final material upside wall |

**Total GEX = +$1.565B** (45-DTE)
**Zero Gamma Level = $259.48**
**Regime classification = NEGATIVE** (spot $258.07 < ZGL $259.48)

Reading: the regime tag is technically "NEGATIVE" because spot is a
sliver below ZGL, but the TOTAL gamma is positive AND the four strikes
just above current spot ($260/265/270/275) hold over **$1.38B of net
positive GEX**. This means:
- Any drift up to $260+ flips dealers to long gamma → **rallies get sold,
  dips get bought, vol compresses**.
- Any breakdown below $245 enters a **−$408M negative-GEX corridor
  ($245/$240/$235/$230/$220)** where dealers SELL into weakness → trend
  acceleration risk.
- The setup is asymmetric: $260 is a SOFT MAGNET (positive gamma
  attraction) while $220-245 is a HARD CLIFF.

### DEX (45-DTE)

| Metric | Value |
|--------|------:|
| Call DEX | +$64.5B |
| Put DEX | −$24.8B |
| **Net DEX** | **+$39.7B** |
| Spot used | $260.63 |

Interpretation: public is **net call-long** by $39.7B notional → dealers
are net **short calls** → dealer hedge is to **BUY underlying** as spot
or delta rises. This creates a structural **bid** that grows with rallies.
Corroborates phase-2's mega DP buyer (likely a dealer-related hedge or a
fund that recognized the dealer-hedge tailwind).

### Vanna + Charm

| Metric | Value |
|--------|------:|
| Net vanna | **−178,550** |
| Call vanna | −322,340 |
| Put vanna | +143,789 |
| Net charm | +17,238,501 |

Vanna **negative** because the book is call-heavy. Mechanics:
- IF IV DROPS (e.g., clean earnings → vol crush): call delta drops →
  dealers (short calls) reduce long-underlying hedge → **SELLING PRESSURE**.
- IF IV RISES (e.g., bad headline): call delta rises → dealers ADD long
  hedge → **BUYING PRESSURE**.

Net charm +17.2M is moderately positive — over time, the call book bleeds
delta into expiry, which forces dealers to slowly REDUCE their long hedge
→ small downward drift from time decay alone. Not a vanna squeeze setup;
**reverse vanna risk into the next earnings**.

### IV Term Structure

| Expiry | DTE | Avg IV |
|--------|----:|-------:|
| 2026-05-22 | 3   | **62.0%** ← front weekly pin |
| 2026-05-29 | 10  | 47.9% |
| 2026-06-05 | 17  | **47.0% (trough)** |
| 2026-06-12 | 24  | **57.5%** ← **EARNINGS KINK** |
| 2026-06-18 | 30  | **57.2%** ← **EARNINGS KINK** |
| 2026-06-26 | 38  | 52.0% |
| 2026-07-17 | 59  | 49.6% |
| 2026-08-21 | 94  | 49.8% |
| 2026-09-18 | 122 | 50.3% |
| 2026-10-16 | 150 | 47.5% |
| 2026-11-20 | 185 | 45.9% |
| 2026-12-18 | 213 | 48.8% |
| 2027-01-15 | 241 | 48.6% |
| 2027-02-19 | 276 | 43.4% |
| 2027-03-19 | 304 | 48.2% |
| 2027-06-17 | 394 | 46.6% |
| 2027-12-17 | 577 | 47.0% |
| 2028-01-21 | 612 | 48.2% |

**Structure tag: BACKWARDATION**; `kink_expiry: null` (the tool didn't
flag the 6/12-6/18 bump as a kink, but the data clearly shows a 10-vol-
point bump vs the 6/05 trough). Read it as **U-shaped term structure**
with an event premium isolated to the 6/12 and 6/18 expiries — exactly
the shape produced by a dated earnings catalyst in that window.

**Implied move (rough, ATM straddle proxy):** at IV 57.2% over 30 days,
expected 1σ move ≈ $258 × 0.572 × √(30/365) ≈ **$42 / ±16%** over the
full 30-day window. But the kink is centred on the 6/12-6/18 expiries,
so the **incremental event move** (vs the 6/05 ATM straddle baseline) ≈
$258 × √(0.572² - 0.47²) × √(30/365) ≈ **±$23 / ±9% expected earnings
move** — at the high end of ADBE's historical 5-8% earnings reactions.

### Term skew

| Metric | Value |
|--------|------:|
| 30-day 25Δ put IV  | 0.5472 |
| 30-day 25Δ call IV | 0.5438 |
| Skew (put − call) | +0.0033 |
| Skew ratio (P/C) | **1.006** |
| Tag | **COMPLACENT** |

Read: **no tail-hedging bid**. Put-call skew is essentially flat — which
contradicts phase-1's "put-buying as hedge" narrative and supports
phase-3's "puts being WRITTEN" interpretation. If institutions were
panic-hedging into earnings, the put wing would be 5-10 vol points
richer; here it's a third of a vol point above calls.

### Front-end IV ratio

| Metric | Value |
|--------|------:|
| Near (10 DTE) | 0.4787 |
| Far (30 DTE)  | 0.5716 |
| Ratio (near/far) | **0.838** |
| Regime | **CONTANGO** |

The "contango" ratio is a SURFACE artifact — back-month IV is the
earnings expiry. The 5/22 front-weekly IV (62%) is BACKWARDATED vs both,
but the 7-vs-30 calc skips the 3-DTE pin-vol. **Net read: market is
pricing the 6/12-6/18 event premium plus the 5/22 expiry-week noise**.

### Today's gamma flip (5/22 expiry only, intraday snapshot)

| Metric | Value |
|--------|------:|
| Spot at snapshot | $260.43 |
| 5/22-only ZGL | **$152.73** |
| 5/22-only Total GEX | +$1.213B |
| Regime | **POSITIVE** (heavily long gamma) |
| ATM flip strike (5/22) | 155 |
| Key support walls (5/22 only) | $260 +$313M; $265 +$305M; $275 +$186M; $270 +$177M; $255 +$67M |

**Read: for the 5/22 expiry alone, dealers are deep long gamma. $260 is
a hard magnet pinning spot through Friday.** The 0DTE expiry-only ZGL of
$152.73 is meaningless as a level (spot won't approach it); the real
3-session ranges are bounded by the $255-$275 GEX cluster.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__options_structure_gex` | symbol=ADBE, dte-max=45, include-zero-gamma=true, date=2026-05-19 | ZGL $259.48; total GEX +$1.565B; $260 wall +$484M |
| `mcp__uw-pp__options_structure_dex` | symbol=ADBE, dte-max=45, date=2026-05-19 | Net DEX +$39.7B (dealer hedge BUY) |
| `mcp__uw-pp__options_structure_vanna_charm` | symbol=ADBE, dte-max=45, date=2026-05-19 | Net vanna −178,550 (call-heavy) |
| `mcp__uw-pp__options_structure_iv_term_structure` | symbol=ADBE, date=2026-05-19 | BACKWARDATION; 6/12-6/18 earnings kink |
| `mcp__uw-pp__options_structure_term_skew` | symbol=ADBE, dte-target=30, date=2026-05-19 | COMPLACENT, skew ratio 1.006 |
| `mcp__uw-pp__options_structure_front_end_iv_ratio` | symbol=ADBE, near-dte=7, far-dte=30, date=2026-05-19 | CONTANGO 0.838 |
| `mcp__uw-pp__options_structure_today_gamma_flip` | symbol=ADBE, date=2026-05-19 | 5/22-only POSITIVE; $260 wall +$313M |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** **STRUCTURALLY BULLISH-WITH-VOLATILITY** —
  dealer hedge bid (DEX +$39.7B) + $260 mega gamma magnet supports spot;
  COMPLACENT skew rules out panic; the only embedded headwind is
  negative vanna (post-event IV crush → dealer sell).
- **Conviction:** **4/5** — clean, internally consistent structural read
  with multiple corroborating tools. The 1-point deduction reflects spot
  being a hair below ZGL (regime label NEGATIVE) — a genuine knife's
  edge, so a downside catalyst could flip the regime adversely fast.
- **Three structural levels for phase-9:**
  1. **ZGL $259.48** — gamma regime flip. **Hold above = long-gamma
     mean-revert; lose = short-gamma cascade**. Primary trigger / hold-
     above level for any tactical long entry.
  2. **$260 gamma wall (+$484M)** — magnet through 5/22 expiry.
     Profit-take T1 / pin target. $265/$270 are the next walls if it
     melts through.
  3. **$245 negative-GEX cliff** (−$55M, with −$102M at $240 below it).
     **Hard stop / invalidation** — close below $245 enters the
     $220-245 short-gamma corridor where trend amplifies.
- **Open questions:**
  - When exactly does Adobe report Q2 fiscal 2026 earnings? (Phase 6 to
    confirm — kink suggests 6/15-6/18 window.)
  - Did the implied move expand or contract over the last 5 sessions?
    (Phase 5 IV percentile / VRP answers.)
  - Is the ADBE IV percentile elevated vs its own 1-year band, or just
    elevated vs its non-event baseline? (Phase 5.)
  - **CONTEXT for prior contradictions:** phase-4 COMPLACENT skew +
    long-gamma walls at $260+ structurally favour the phase-3 "puts being
    written" reframe over the phase-1 "puts being bought as hedge" read.
    Phase 10 audit should give phase-3+phase-4 more weight on the put
    interpretation.
