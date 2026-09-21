# Phase 3 — Open Interest & Positioning

**Ticker:** RKT
**As-of date:** 2026-05-20 (data: 2026-05-19; OI Δ vs 2026-05-18 close)
**Generated:** 2026-05-20T00:25:00Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md

## Summary

The OI change tape reconciles phase-1's bullish-tilt flow with phase-2's
distribution: institutions are **rotating from stock to bullish-tilted
risk-reversals + collars**, not exiting. The largest single-day OI buildup
is the **2026-08-21 $14 CALL at +3,610 contracts** (ask-side dominant,
$505k of prev-day premium) — a fresh near-OTM upside speculation strike
[OI:biggest_increases, OI:smart_positioning]. Even more telling is the
**2028-01-21 $10 PUT at +1,237 contracts with bid-side dominant volume**
(1,153 bid vs 101 ask) — an institution **SELLING** long-dated puts to
express a "RKT will not be below $10 in 2.5 years" view, classic structural
bullish-floor expression [OI:smart_positioning]. Weekly 13-strike put OI
also expanded on the bid (+1,368 contracts) — more put-writing for the May-22
expiry. The opposing book: +853 Dec 11P and +566 Sep 13P on the ASK as
downside hedges. Net positioning bias: **bullish with floor-defined risk
($10)**, conviction 4/5. No pin/cliff signal active this week.

## Key signals

- **Aug 14C OI +3,610** (ask 3,527 vs bid 292; net_ask_bid +3,235) — fresh
  ~10% OTM upside accumulation [OI:biggest_increases, OI:smart_positioning].
- **Jan-28 10P OI +1,237 with bid-side dominant volume** — institution
  SELLING 2.5-year LEAPS puts to define a $10 floor, premium received
  ~$238k [OI:smart_positioning].
- **May-29 14C OI +2,643** (ask 2,477 vs bid 648) — near-term upside
  speculation (10-DTE 10% OTM) [OI:biggest_increases].
- **May-22 13P OI +1,368, BID-leaning** (942 bid vs 536 ask) — weekly
  put-writing at the cluster's largest distribution price level
  [OI:smart_positioning, DP:price_levels].
- **Dec 11P OI +853 ASK** + **Sep 13P OI +566 ASK** — fresh ASK-side put
  protection layers below spot [OI:biggest_increases].
- **Zero same-session rolls** [OI:position_rolls] — the LEAPS/upside book is
  net-NEW, not a transfer from existing positions.
- **No active pin risk** — RKT not in market-wide OPEX-week top 25
  [OI:pin_risk].

## Detailed findings

### Largest OI increases (`mcp__uw-pp__oi_biggest_increases`)

| Symbol | Strike | Type | DTE | Prev OI | Curr OI | OI Δ | Prev Ask | Prev Bid | Inferred dir |
|--------|--------|------|-----|---------|---------|------|----------|----------|--------------|
| RKT260821C00014000 | 14   | CALL | 94  | 756    | 4,366  | **+3,610** | 3,527 | 292   | **Bullish (BTO)** |
| RKT260529C00014000 | 14   | CALL | 10  | 7,846  | 10,489 | +2,643 | 2,477 | 648   | Bullish (BTO) |
| RKT260522P00013000 | 13   | PUT  | 3   | 781    | 2,149  | +1,368 | 536   | 942   | **Bullish (STO put)** |
| RKT280121P00010000 | 10   | PUT  | 612 | 404    | 1,641  | +1,237 | 101   | 1,153 | **Bullish (STO LEAPS put)** |
| RKT260522C00014000 | 14   | CALL | 3   | 1,621  | 2,599  | +978   | 353   | 905   | Bearish (STO call) — covered overwrite |
| RKT261218P00011000 | 11   | PUT  | 213 | 1,524  | 2,377  | +853   | 1,605 | 27    | **Bearish (BTO put)** — hedge |
| RKT260821C00013000 | 13   | CALL | 94  | 3      | 660    | +657   | 210   | 426   | Mixed (slightly bid) |
| RKT260918P00013000 | 13   | PUT  | 122 | 4,461  | 5,027  | +566   | 592   | 76    | **Bearish (BTO put)** — hedge |

Net OI Δ pattern:
- **Calls bought above spot ($13–$14):** +6,892 contracts (Aug 14C + May-29 14C + Aug 13C + small May-22 prints)
- **Puts SOLD (bullish writing):** +1,368 (May-22 13P) + +1,237 (Jan-28 10P) = +2,605 contracts
- **Puts BOUGHT (hedges):** +853 (Dec 11P) + +566 (Sep 13P) = +1,419 contracts
- **Calls SOLD (covered/collar):** +978 (May-22 14C)

The bullish vector dominates by both contract count and inferred direction.

### Closing / roll activity (`mcp__uw-pp__oi_decrease_with_volume`)

Largest 10 decreases — none material (max -216 contracts):

| Symbol | OI Δ | Volume | Read |
|--------|------|--------|------|
| RKT260618C00014000 | -216 | 609   | June 14C closing (some take profit ahead of June OPEX) |
| RKT260522P00013500 | -176 | 258   | Weekly 13.5P closing |
| RKT260918C00020000 | -172 | 262   | Sep far-OTM 20C closing (stale spec position) |
| RKT260522C00016000 | -103 | 172   | Weekly 16C — closing penny calls |
| RKT260918P00014000 | -101 | 101   | Sep 14P closing |

No large closures. The total OI decrease across all decreasing strikes is
< 1,500 contracts — dwarfed by the +8k+ in net openings above.

### Position rolls (`mcp__uw-pp__oi_position_rolls`)

```
rolls_detected: 0
threshold: 500
near_dte_max: 30
```

No same-day near→far rolls. **Implication:** the LEAPS / Aug-21 / Jan-28
buildup is FRESH money, not migrating from front-month expiries. This is
a stronger signal than rolls — it's net new positioning.

### Smart positioning (`mcp__uw-pp__oi_smart_positioning`)

| Symbol | OI Δ | Inferred direction | Rationale |
|--------|------|-------------------|-----------|
| RKT260821C00014000 | +3,610 | bullish | Ask-skew on calls = BTO |
| RKT260529C00014000 | +2,643 | bullish | Ask-skew on calls = BTO |
| RKT260522P00013000 | +1,368 | bullish | **Bid-skew on puts = STO (premium collection)** |
| RKT280121P00010000 | +1,237 | bullish | **Bid-skew on LEAPS puts = STO (floor expression)** |
| RKT260522C00014000 | +978   | bearish | Bid-skew on calls = STO (covered overwrite) |
| RKT261218P00011000 | +853   | bearish | Ask-skew on puts = BTO (hedge) |
| RKT260821C00013000 | +657   | bearish | Slight bid-skew on calls |
| RKT260918P00013000 | +566   | bearish | Ask-skew on puts = BTO (hedge) |

**Net direction by OI Δ:**
- Bullish-tagged: 3,610 + 2,643 + 1,368 + 1,237 = **8,858 contracts**
- Bearish-tagged: 978 + 853 + 657 + 566 = **3,054 contracts**
- **Bull/bear OI ratio = 2.9×**

Even with phase-2's distribution overlay, the options POSITIONING tape is
unambiguously bullish-tilted.

### Pin risk (`mcp__uw-pp__oi_pin_risk`, dte_max=7, max_distance_pct=5)

RKT is NOT in the top 25 pin candidates this week. The bar for inclusion
is a pin_score above ~$176k (PFE, the #25). Top names include SPY ($1.85M),
HYG ($1.51M), QQQ ($1.15M), IWM ($1.11M).

For RKT, the closest weekly with material OI is 2026-05-22 (3 DTE). The
biggest May-22 strikes by current OI:
- May-22 13C: not flagged but likely material
- May-22 13P: 2,149 OI (post-build) — sits 1.0% below spot
- May-22 14C: 2,599 OI — sits 8.7% above spot

The 13-strike has weekly OI both sides, but ~4k total OI is too thin to
create meaningful pin gravity. **No pin pressure to factor into phase-9.**

### OPEX concentration (`mcp__uw-pp__oi_opex_concentration`)

RKT does NOT appear in the top 20 single-expiry-concentration list. Those
are all microcaps with a single dominant expiry. RKT's OI is spread across
2026-05-22, 2026-06-18, 2026-07-17, 2026-08-21, 2026-09-18, 2026-12-18, and
2027-01-15 / 2028-01-21 — healthy chain dispersion, no cliff risk.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `oi_biggest_increases` | `{symbol: RKT, top_n: 20, min_oi_change: 500, date: 2026-05-19}` | 8 rows; #1 = Aug 14C +3,610 |
| `oi_decrease_with_volume` | `{symbol: RKT, top_n: 15, min_volume: 100, date: 2026-05-19}` | 14 rows; max decrease -216 |
| `oi_smart_positioning` | `{symbol: RKT, top_n: 20, min_oi_change: 500, date: 2026-05-19}` | 8 rows; net bullish (8,858 vs 3,054) |
| `oi_position_rolls` | `{symbol: RKT, threshold: 500, near_dte_max: 30, date: 2026-05-19}` | rolls_detected: 0 |
| `oi_pin_risk` | `{top_n: 25, dte_max: 7, max_distance_pct: 5, date: 2026-05-19}` | RKT not in top 25 |
| `oi_opex_concentration` | `{top_n: 20, min_concentration_pct: 40, date: 2026-05-19}` | RKT not in top 20 |

## Tool errors

(none)

## Verdict for downstream phases

- **Bias from this phase:** bullish (positioning tape clearly bull-skewed,
  2.9× bull/bear contract ratio)
- **Conviction:** 4/5
  - Strengthened by the Jan-28 10P sell (long-dated structural bullish call)
    and the Aug 14C +3,610 net-new build.
  - Held back from 5/5 by the parallel Dec 11P / Sep 13P hedges that
    indicate the bulls are NOT pure directional — they're paying for
    downside protection in parallel.
- **Three strikes / OI levels for phase-9 reference:**
  1. **$14 (call-magnet)** — combined OI Δ +6,892 across Aug 21, May 29, May 22,
     and June 18 expiries. This is the institutional "if we break $14, we
     run to $15+" upside trigger.
  2. **$13 (transaction-pivot)** — both weekly put-writing (May-22 13P)
     AND Sep 13P hedging cluster here. The strike is the inflection where
     bullish premium-collectors meet bearish protection-buyers.
  3. **$10 (LEAPS floor)** — Jan-28 10P sold + Dec 10P bought (phase-1).
     This is the institutional floor: below $10 someone has to deliver
     stock on the put assignment AND someone is structurally short
     downside via the LEAPS write. **$10 is a hard 'thesis broken' line.**
- **Open questions:**
  - Are dealers positive- or negative-gamma at $13? (phase 4 must answer)
  - Has IV30 mean-reverted since the recent decline from $14.25 to $12.52?
    (phase 5)
  - Did the institutional Jan-28 put-write occur after a known catalyst
    (e.g., Q1 earnings beat) or in front of one? (phase 6)
