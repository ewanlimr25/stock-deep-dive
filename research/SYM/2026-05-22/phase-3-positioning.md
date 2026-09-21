# Phase 3 — Open Interest & Positioning

**Ticker:** SYM
**As-of date (effective):** 2026-05-21
**Generated:** 2026-05-22T15:09Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md

## Summary

SYM's options chain shows a **thin, concentrated positioning profile**.
Only three contracts cleared the OI-change ≥100 threshold for 2026-05-21
[OI:biggest_increases]. The single biggest OI build is a 0DTE call-lottery
ticket — `SYM260522C00053000` went from 48 → **452 OI** with prev_ask_volume
420 vs prev_bid_volume 4 (ask/bid ratio ~105x) [OI:smart_positioning, marked
bullish]. The Jan-27 $50 call had a +110 OI increase with prev_bid_volume
67 > prev_ask_volume 42 → **bearish inferred** by the smart_positioning
heuristic [OI:smart_positioning], which corroborates the phase-1 finding
that the $66K single trade on the same contract was bid-side. **SYM does
not appear in `oi_pin_risk` (next OPEX is 2026-06-18, ~28 days out) or
`oi_opex_concentration` (≥30% threshold)** — no near-term pin to defend.

## Key signals

- **Bullish 0DTE call lottery**: `SYM260522C00053000` OI 48 → 452
  (+404, +841%), volume 431, ask/bid 420:4 [OI:biggest_increases,
  OI:smart_positioning]. Speculative open on a same-day 5%-OTM call.
- **Bearish-inferred LEAP build**: `SYM270115C00050000` OI 500 → 610
  (+110), but ask 42 / bid 67 → smart_positioning flags **bearish**
  [OI:smart_positioning]. Matches the $66K bid-side print from
  phase-1-flow.md — institution writing/closing LEAP calls.
- **Modest bullish add at 0DTE $52**: `SYM260522C00052000` OI 152 → 265
  (+113), ask/bid 63:46 [OI:biggest_increases] — small, near-money
  speculative open.
- **No position rolls detected** (`oi_position_rolls`, threshold=100,
  near_dte_max=30) — zero same-day roll candidates. Phase-1 "rolling LEAP
  calls" thesis is *not confirmed* by intraday OI rolling, but the
  single-day filter misses cross-session rolls.
- **No pin risk**: SYM is not in the OPEX-week pin list (next OPEX is
  2026-06-18, dte=28 from 2026-05-21) [OI:pin_risk].
- **No OPEX concentration ≥30%**: SYM's OI is spread across multiple
  expiries (LEAP, Jun, Jul, Aug, Jan-27, Jan-28) — no cliff strike to
  defend [OI:opex_concentration].

## Detailed findings

### Largest OI increases

Spot at snapshot: $50.44.

| Option | DTE | Strike | OI prev | OI curr | Δ OI | Vol | Ask vol | Bid vol | Inferred |
|--------|-----|--------|---------|---------|------|-----|---------|---------|----------|
| `SYM260522C00053000` | 1 | 53 (+5.1% OTM) | 48  | 452 | +404 | 431 | 420 | 4  | **bullish** |
| `SYM260522C00052000` | 1 | 52 (+3.1% OTM) | 152 | 265 | +113 | 120 | 63  | 46 | bullish (mild) |
| `SYM270115C00050000` | 239 | 50 (ATM)    | 500 | 610 | +110 | 114 | 42  | 67 | **bearish** |

Read: short-dated ask-side call opens (lottery tickets for a same-day
breakout above $52–53) overlay a longer-dated bid-side call write at the
ATM Jan-27 50 strike. Two different participants, two different timeframes.

### Closing / roll activity (decreases with volume)

Only 0DTE contracts saw meaningful closing on 2026-05-21:

| Option | Strike | DTE | OI prev | OI curr | Δ OI | Vol | Read |
|--------|--------|-----|---------|---------|------|-----|------|
| `SYM260522P00046000` | 46  | 1 | 102 | 70 | −32 | 53 | put closing (downside hedge unwind) |
| `SYM260522C00047000` | 47  | 1 | 117 | 93 | −24 | 53 | call closing |
| `SYM260522P00044500` | 44.5 | 1 | 79  | 68 | −11 | 52 | put closing |
| `SYM260618C00060000` | 60  | 28 | 214 | 211 | −3 | 84 | negligible |

The two put closures (P46, P44.5) are mildly bullish at the margin —
near-term downside hedges being unwound rather than added to. The C47
close is just position cleanup.

### Position rolls

`oi_position_rolls(threshold=100, near_dte_max=30)` returned **0 rolls
detected**. Notable caveat from the tool itself: *"Single-day detection
only — cross-session rolls are not captured."* So phase-1's "LEAP roll"
hypothesis would only show up as a single-day signal if the near-leg
unwind happened on 2026-05-21; it didn't appear at the 100-contract
threshold.

### Pin risk

SYM is **not** in `oi_pin_risk` (dte_max=7, max_distance_pct=5) — the
next OPEX is 2026-06-18, which is ~28 calendar days out, so SYM is
correctly excluded. Tickers that do appear in the pin list at dte=0 or 1
include SPY (spot 742.69, pin 710), HYG (spot 79.9, pin 79), TLT (spot
84.24, pin 86), QQQ (spot 714.43, pin 680), NVDA (spot 219.42, pin 220),
XLF (spot 51.74, pin 51) — relevant for phase-6 market regime context.

**Implication for SYM**: no immediate gamma-pinning effect on the
underlying. Movement is unconstrained by 0DTE positioning at the index/
broad-market level (those names will pin); SYM itself trades freely.

### OPEX concentration

SYM does **not** appear in the ≥30% concentration list. By construction,
SYM has options across at least 6 expiries (2026-05-22, 2026-06-05,
2026-06-18, 2026-07-17, 2026-08-21, 2027-01-15, 2028-01-21 visible in
phases 1 + 3), so no single expiry holds more than 30% of OI. No OPEX
cliff to defend.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__oi_biggest_increases` | symbol=SYM, top-n=25, min-oi-change=100, date=2026-05-21 | 3 rows: 0DTE C53 (+404), 0DTE C52 (+113), Jan-27 C50 (+110) |
| `mcp__uw-pp__oi_decrease_with_volume` | symbol=SYM, top-n=20, min-volume=50, date=2026-05-21 | 4 rows, mostly 0DTE closures |
| `mcp__uw-pp__oi_smart_positioning` | symbol=SYM, top-n=20, min-oi-change=100, date=2026-05-21 | 3 rows: 2 bullish + 1 bearish (LEAP 50C) |
| `mcp__uw-pp__oi_position_rolls` | symbol=SYM, threshold=100, near-dte-max=30, date=2026-05-21 | 0 rolls detected |
| `mcp__uw-pp__oi_pin_risk` | top-n=100, dte-max=7, max-distance-pct=5, date=2026-05-21 | SYM not in list |
| `mcp__uw-pp__oi_opex_concentration` | top-n=100, min-concentration-pct=30, date=2026-05-21 | SYM not in list |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** **mixed-bullish**. Speculative ask-side
  short-dated call opens (0DTE C52 + C53) and put-hedge unwind on the
  near tape lean bullish; the LEAP 50C bid-side build is bearish/yield-
  grab and matches the phase-1 institutional roll. Net is mild bullish
  at the retail/short-dated end of the chain and mild bearish at the
  institutional/LEAP end — two distinct flow profiles.
- **Conviction:** 2/5. Total OI build across all three flagged contracts
  is only +627 contracts (~$60K aggregate notional from the new opens).
  The 0DTE C53 was a same-day lottery (already expired by the time this
  research is written) and provides limited forward signal.
- **Three pin/cliff strikes for phase-9:**
  1. **$53 (0DTE C53 magnet, +404 OI today)** — for retrospective
     reference only; expiry was 2026-05-22 (today). If the underlying
     printed close to $53 at close, expect mean-reversion as call
     unwind finishes.
  2. **$50 strike (Jan-27 C50, 610 OI)** — the largest single LEAP OI
     concentration and the contract being written/closed by the
     institution. Acts as a vol-seller anchor at the ATM. Phase-4 GEX
     should show whether this builds a positive-gamma shelf right at
     spot.
  3. **No near-term pin** — June 18 chain has highest OI at C60
     (211 contracts), which is +18.9% OTM and too far/too small to
     gamma-pin. Underlying is free to trend within the LEAP-strike grid
     (45, 50, 52.5, 55).
- **Open questions:**
  - Phase-4 (GEX/dealer): does the Jan-27 C50 being written by
    institutions translate to positive dealer gamma at $50 (calls
    shorted by customers = dealers long the calls = long gamma)?
  - Phase-5 (historical OI trend): is the 610 OI on Jan-27 C50 a fresh
     build or a multi-month accumulation? The same-day Δ of +110 is
     too small to tell on its own.
  - The two participant profiles (retail short-dated lottery + LEAP
     writer) co-existing is normal; no contradiction with phase-2
     accumulation. Phase-10 audit needs to check that.
