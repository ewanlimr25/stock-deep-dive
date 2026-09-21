# Phase 3 — Open Interest & Positioning

**Ticker:** GRAB
**As-of date:** 2026-05-21
**Generated:** 2026-05-21T20:40:00Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md

## Summary

GRAB's OI flow today resolves the phase-1 / phase-2 contradiction: it shows
the unmistakable signature of **covered-call writing on top of dark-pool
accumulation**. The 5 largest "bearish smart_positioning" rows are all
LEAP calls being added on the BID side (institutions WRITING calls, not
buying puts), with sizable existing OI walls at $5, $7, $7.50, and $10
strikes that are characteristic of an institutional covered-call program
[OI:smart_positioning]. The only opened put position (2026-10-16 $4P, +159
OI on ask) reinforces the hedged-long read [OI:biggest_increases]. GRAB is
NOT in pin-risk or OPEX-concentration tables [OI:pin_risk],
[OI:opex_concentration] — no near-term OPEX gravity. **Net read: institutional
overlay program (long stock + short LEAP calls + small put protection)** —
i.e. carry/yield trade, mildly constructive but capped on the upside.

## Key signals

- **2028-01-21 $3C: +792 OI, 782 of 807 prev-day vol on BID side** ($105K
  premium) — call writing in size on a deep-ITM LEAP [OI:smart_positioning].
- **2028-12-15 $2C: +538 OI, 503 of 532 on ASK** ($109K premium) — deep-ITM
  LEAP call BUYER (institutional long via call) [OI:smart_positioning,
  biggest_increases].
- **2027-01-15 $5.50C: +209 OI but 1,125 of 1,226 vol on BID** — heavy call
  writing at $5.50 strike [OI:smart_positioning].
- **2026-10-16 $4P: +159 OI, 156 of 159 on ASK** — single new put buyer at
  the $4 strike (mild downside protection) [OI:smart_positioning].
- **No pin risk for 2026-05-22 weekly OPEX** — GRAB not in top 48 pin
  candidates [OI:pin_risk]. No OPEX concentration cliff [OI:opex_concentration].
- **Roll signal: -858 near-DTE puts / +378 far-DTE puts** (balance_ratio
  0.441) — small protective put position rolled further out [OI:position_rolls].

## Detailed findings

### Largest OI increases (today)

| Contract | DTE | Type | Strike | OI Δ | Vol | Prev ask vol | Prev bid vol | Inferred dir | Premium |
|----------|-----|------|--------|------|-----|--------------|--------------|--------------|---------|
| GRAB260626C00004500 | 36 | call | $4.5 | **+1,555** | 1,555 | 1,555 | 0 | **bullish** | $4,665 |
| GRAB280121C00003000 | 610 | call | $3 | +792 | 824 | 25 | 782 | **bearish (write)** | $105,222 |
| GRAB281215C00002000 | 939 | call | $2 | +538 | 541 | 503 | 29 | **bullish** | $109,173 |
| GRAB270617C00007000 | 392 | call | $7 | +521 | 521 | 5 | 513 | bearish (write) | $10,920 |
| GRAB270617C00010000 | 392 | call | $10 | +419 | 428 | 6 | 412 | bearish (write) | $4,697 |
| GRAB281215C00003000 | 939 | call | $3 | +280 | 459 | 107 | 351 | bearish (write) | $69,443 |
| GRAB270115C00005500 | 239 | call | $5.5 | +209 | 1,295 | 101 | 1,125 | bearish (write) | $21,036 |
| GRAB280121C00005000 | 610 | call | $5 | +196 | 296 | 37 | 57 | bearish (mixed) | $19,381 |
| GRAB280121C00004000 | 610 | call | $4 | +163 | 269 | 33 | 148 | bearish (write) | $23,465 |
| GRAB280121C00010000 | 610 | call | $10 | +161 | 200 | 152 | 22 | bullish | $4,108 |
| GRAB261016P00004000 | 148 | **put** | $4 | +159 | 159 | 156 | 3 | bearish (put buy) | $11,917 |
| GRAB260618C00003500 | 28 | call | $3.5 | +151 | 176 | 98 | 71 | bullish | $3,096 |
| GRAB261016C00007000 | 148 | call | $7 | +151 | 151 | 57 | 93 | bearish (write) | $755 |
| GRAB270115C00007500 | 239 | call | $7.5 | +142 | 358 | 155 | 47 | bullish | $2,919 |
| GRAB270115C00005000 | 239 | call | $5 | +136 | 586 | 266 | 284 | bearish (mixed) | $13,183 |

**Aggregating call writes vs call buys (by premium):**
- **Call write premium (LEAP, ≥180d)**: $105K + $109K* (–this is buy, not write) + $69K + $21K + $19K + $23K = roughly $237K of premium SOLD (institutional collection).

  *Note*: $109K on 2028-12-15 $2C is a BUYER, not a writer. So **net write
  premium (excluding the 2028-12 $2C buy):** ~$237K SELL vs $109K BUY = ~$128K net call premium SOLD by institutions on the LEAP curve.

This is the dollar-weighted center of the day's OI action and it's net SHORT
volatility / covered-call writing — exactly what you'd expect if the dark pool
buyer in phase-2 is the same desk.

### Existing OI walls (largest open positions)

| Contract | OI | Strike | Expiry | DTE | Type | Notes |
|----------|-----|--------|--------|-----|------|-------|
| GRAB270115C00010000 | 208,228 | $10 | 2027-01 | 239 | call | dominant LEAP wall (capped upside) |
| GRAB270115C00007500 | 167,753 | $7.5 | 2027-01 | 239 | call | secondary wall |
| GRAB271217C00007000 | 115,895 | $7 | 2027-12 | 575 | call | 2027 wall |
| GRAB270115C00005000 | 105,422 | $5 | 2027-01 | 239 | call | major wall (~40% above spot) |
| GRAB270115C00005500 | 48,778  | $5.5 | 2027-01 | 239 | call | |
| GRAB280121C00010000 | 47,449  | $10 | 2028-01 | 610 | call | |
| GRAB271217C00010000 | 39,839  | $10 | 2027-12 | 575 | call | |
| GRAB280121C00005000 | 31,353  | $5 | 2028-01 | 610 | call | |
| GRAB270115C00004000 | 25,887  | $4 | 2027-01 | 239 | call | nearest LEAP $4 wall |
| GRAB280121C00004000 | 19,410  | $4 | 2028-01 | 610 | call | |
| GRAB260618C00004000 | 15,511  | $4 | 2026-06 | 28 | call | near-term $4 wall |
| GRAB280121C00003000 | 10,796  | $3 | 2028-01 | 610 | call | |

Reading: the call OI is heavily skewed to $5–$10 strikes (LEAP), totaling
nearly **800K LEAP calls outstanding above $5**. If even half of these are
written by institutions (covered overlays), the implied capped upside zone
is **$5 → $10 over the 2027–2028 horizon** — institutions are collecting
yield while expressing constructive-but-capped GRAB.

### Closing / roll activity

| Contract | DTE | Vol | OI Δ | Notes |
|----------|-----|-----|------|-------|
| GRAB270115C00010000 | 239 | 775 | -550 | 2027-01 $10C trimming (closing some writes) |
| GRAB260717P00005000 | 57  | 171 | -96 | $5P being closed (modest) |
| GRAB260522C00001000 | 1   | 94 | -58 | 0DTE clean-up |

Position rolls (single tool result):
- **Type: PUT roll** — near-DTE OI -858, far-DTE OI +378. balance_ratio 0.441
  (more closed than added) [OI:position_rolls]. Net put protection
  REDUCED slightly while extending out the duration of remaining puts.

### Smart positioning (synthesis)

By aggregate inferred direction across rows ≥100 OI Δ:
- **Bullish-inferred:** 5 rows totaling +2,605 OI (driven by the 2026-06-26
  $4.5C +1,555 — a single retail-sized aggressive bullish opening, plus deep-
  ITM 2028-12 $2C buy)
- **Bearish-inferred (call writes & put buys):** 14 rows totaling +1,728 OI,
  but premium-weighted is the larger story (~$237K written vs ~$110K bought).

The smart-positioning tool flags this as net bearish by COUNT but it's
specifically **call-writing dominated**, which when paired with the phase-2
dark-pool block buy of 817K shares = **covered-call overlay** rather than
directional bearish positioning.

### Pin risk (2026-05-22 weekly OPEX, dte_max=7)

GRAB **not present** in the top 48 ranked tickers by pin_score. Spot $3.555,
nearest weekly OPEX 2026-05-22 = 1 DTE. No actionable pin gravity for
tomorrow's expiry. The two near-spot weekly strikes ($3.50, $3.50, $3.50 OI
across calls and puts) carry trivial OI relative to peers.

### OPEX concentration

GRAB **not present** in the 100%-concentration list (dominated by illiquid
single-expiry tickers). GRAB's OI is healthily distributed across:
- 2026-05-22 weekly: tiny
- 2026-05-29 weekly: small
- 2026-06-18 monthly: ~10–20K OI per major strike
- 2026-07-17 monthly: moderate
- 2026-10-16, 2026-12-18: small
- **2027-01-15 LEAP: largest concentration (~590K OI across calls $3–$10)** —
  this is the dominant institutional anchor
- 2027-12-17, 2028-01-21, 2028-12-15 LEAPS: substantial

No 50%+ single-expiry cliff. No tail-risk OPEX gravity to game.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__oi_biggest_increases` | symbol=GRAB, date=2026-05-21, top_n=25, min_oi_change=100 | 19 rows; biggest = +1,555 @ Jun-26 $4.5C; LEAPS dominate by premium |
| `mcp__uw-pp__oi_decrease_with_volume` | symbol=GRAB, top_n=15, min_vol=50 | 11 rows; biggest decrease = -550 @ 2027-01 $10C |
| `mcp__uw-pp__oi_smart_positioning` | symbol=GRAB, top_n=25, min_oi_change=100 | 19 rows; 14 bearish-inferred (mostly call writes) |
| `mcp__uw-pp__oi_position_rolls` | symbol=GRAB, threshold=100, near_dte_max=30 | 1 roll: PUT, near -858 / far +378 |
| `mcp__uw-pp__oi_pin_risk` | date=2026-05-21, top_n=50, dte_max=7, max_dist=5%, min_total_oi=500 | GRAB not in list |
| `mcp__uw-pp__oi_opex_concentration` | date=2026-05-21, top_n=50, min_concentration_pct=30 | GRAB not in list |

## Tool errors

(none)

## Verdict for downstream phases

- **Bias from this phase:** **HEDGED-LONG / COVERED-CALL OVERLAY** —
  consistent with phase-2 dark-pool accumulation. Net premium-weighted OI is
  call writing (income), small new put protection, no net short-the-stock
  signal.
- **Conviction:** 3/5 (clear pattern but premiums are small in absolute terms
  per the phase-0 thin-options caveat).
- **Three pin/cliff strikes for phase-9 entry/stop reference:**
  1. **$4 strike** — primary near-term institutional wall. June 2026 $4C OI
     15,511; 2027-01 $4C OI 25,887; 2028-01 $4C OI 19,410 (combined ~60K
     calls); $4 is also the dominant put strike being added today (2026-10
     $4P +159). Acts as both magnet and likely reaction level.
  2. **$5 strike** — major LEAP call wall (2027-01 $5C OI 105,422 + 2028-01
     $5C OI 31,353 + 2027-01 $5.5C OI 48,778) → **gamma cap** on rallies.
     If spot breaks ABOVE $5, dealer hedging will accelerate the move once
     dealers buy back their short calls.
  3. **$3 strike** — institutional base. 2027-01 $3C OI 5,448 + 2028-01 $3C
     OI 10,796; today's $3C activity is mixed but slightly net positive.
     Important downside reference; break below $3 invalidates the
     covered-call regime (deep ITM call sellers under water).
- **Open questions:**
  - Phase-4 GEX should confirm whether the $5 strike is the dealer gamma
    pivot. If so, phase-9 should size a "magnet to $5" trade structure.
  - Phase-5 cumulative_premium_flow should confirm the covered-call regime
    by showing persistent net call SELLING over weeks.
  - Phase-7 institutional_accumulation should agree (ACCUMULATION) and
    conviction_matrix should label HEDGED_LONG or COVERED_CALL.
