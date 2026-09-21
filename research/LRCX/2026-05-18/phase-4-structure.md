# Phase 4 — Dealer Structure & Gamma

**Ticker:** LRCX
**As-of date (requested):** 2026-05-18
**Effective as-of date (data):** 2026-05-15
**Spot used by tools:** $285.06–$285.28
**Generated:** 2026-05-18T00:00:00Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md

## Summary

LRCX is **deep in long-gamma regime**: total 45-DTE GEX is **+$109M**,
zero-gamma level is **$70.78** (far below the $285 spot) — dealers buy
dips, sell rallies, realized vol should stay compressed. **Net DEX +$9.3B**
(public long-call book, dealers short calls → mechanical underlying bid).
**But** the front-end is **KINKED into BACKWARDATION**: 5/22 IV is 74.5%
vs 6/18 IV 67.8% (ratio **1.099**) — a 7-point front-end premium with no
named catalyst before 5/22 OPEX, suggesting either residual post-gap vol
bid, sector-OPEX hedging spillover, or an unknown near-term event. Term
skew (30D) is **NORMAL** (call 25Δ 63.3%, put 25Δ 64.6%, ratio 1.021) — no
tail panic. Net vanna is slightly negative (-49k) → **falling IV would
mechanically force dealer selling**, a risk to monitor.

## Key signals

- **Total 45-DTE GEX +$109.3M, ZGL $70.78, regime POSITIVE** — dealers
  long gamma, mean-reversion expected [STRUCT:gex].
- **Net DEX +$9.3B** (call DEX +$22.1B vs put DEX -$12.8B) → dealers
  short-call → buy underlying on rallies [STRUCT:dex].
- **Front-end IV ratio 1.099 (BACKWARDATION)**: 5/22 (4 DTE) 74.5% vs 6/18
  (31 DTE) 67.8% → unexplained near-term event premium
  [STRUCT:front_end_iv_ratio, iv_term_structure].
- **Term skew NORMAL**, 25Δ put-call gap 1.34 vol-pts at 30 DTE → no tail
  hedging premium [STRUCT:term_skew].
- **Today gamma flip (0DTE on 5/15)**: spot $285.28 sat **right on the
  -$228.7M resistance wall at 285**, with +$151.7M support cluster at 300
  and +$115.8M at 290 → gamma walls bracketed price tightly
  [STRUCT:today_gamma_flip].

## Detailed findings

### GEX (45 DTE)

- **Total net GEX:** +$109,256,132 (POSITIVE → long gamma)
- **Zero gamma level:** $70.78 (irrelevant — too far below)
- **Underlying price:** $285.18
- **Regime description:** "Dealers net long gamma — expect mean-reversion
  and reduced volatility"

**Top positive GEX strikes (dealer support — buy here):**
- $280: **+$30.5M** (largest positive 45-DTE node, just below spot)
- $150: +$12.0M (LEAP residual)
- $135: +$6.6M
- $165: +$6.1M
- $70: +$0.3M

**Top negative GEX strikes (liquidity holes — dealers short gamma, will
amplify moves through these levels):**
- $260: **-$53.5M** (biggest hole)
- $240: -$30.1M
- $250: -$27.8M
- $220: -$26.3M
- $255: -$18.6M
- $265: -$14.5M
- $230: -$14.5M
- $270: -$13.7M
- $210: -$13.5M

**Interpretation:** the positive gamma is concentrated at $280 — that's
the dealer-sided support that will catch a pullback. **Below $280, the
gamma terrain is hostile**: stacked negative gex from $260 down to $210
means a break of $280 will **accelerate**, not cushion. The largest hole
is at $260 (-$53.5M), which is also where 5/22 sees 6,653 OI in puts and
where one of the largest sweep prints (Jan'27 260P bid-side $1.03M) was
placed — that level will be a **gamma magnet to the downside if $280
breaks**.

Above spot the 45-DTE GEX table truncates at $287.5 — the 5/22 OPEX has
limited far-OTM call OI; most of the dealer-positive overhead is in 6/18
and beyond.

### DEX (45 DTE)

| Metric | Value | Interpretation |
|--------|-------|----------------|
| Call DEX | **+$22.1B** | Public is heavily long calls |
| Put DEX | **-$12.8B** | Public has put protection |
| **Net DEX** | **+$9.3B** | Public is net delta-long → dealers net short delta → **dealer hedge: buy underlying** |

The interpretation field from the tool: *"Public is net call-long →
dealers net short calls → dealer hedge is to BUY underlying."* This is a
mechanical bid — but is the SAME signal as phase-1's institutional call
**writing**: institutions sell calls → dealers buy them (or facilitate the
flow) → dealers go long calls / short stock at the open → as stock moves,
dealers re-hedge. The net effect is **modest support at current levels**
unless flow flips materially.

### Vanna + Charm (45 DTE)

| Metric | Value |
|--------|-------|
| Call vanna | -108,355 |
| Put vanna | +59,245 |
| **Net vanna** | **-49,110** |
| **Net charm** | **+809,707** |

Net vanna is **slightly negative**. Tool interpretation: *"Falling IV →
call delta drops → dealers (short calls) cut long-underlying hedge →
SELLING pressure. Rising IV reverses."*

Given LRCX IV (67-75%) is meaningfully above its 1Y baseline (assume
~50-55% in normal regimes, to be verified phase 5), an **IV mean-reversion
lower** would be the natural next move — and that would **mechanically
remove the dealer bid**. This is a real downside risk multiplier even
with the supportive GEX backdrop.

Charm is positive — time decay slowly rolls call deltas down, dealer
unwind is gradual, no immediate dislocation.

### IV term structure

```
Expiry      DTE   Avg IV
2026-05-15    0   14.0%   ← intraday-only ATM (already settled)
2026-05-22    4   74.5%   ← FRONT-END SPIKE
2026-05-29   11   67.7%
2026-06-05   18   67.3%
2026-06-12   25   66.0%
2026-06-18   31   67.8%
2026-06-26   39   64.9%
2026-07-17   60   64.7%
2026-08-21   95   66.0%   ← mild earnings bump (LRCX reports late July)
2026-09-18  123   64.8%
2026-10-16  151   64.3%
2026-11-20  186   64.8%
2026-12-18  214   65.8%
2027-01-15  242   63.5%
2027-03-19  305   63.0%
2027-06-17  395   65.9%
2028-01-21  613   65.6%
```

**Structure:** flagged "CONTANGO" overall but the body of the curve is
nearly **flat at 63–68%** between 5/29 and 1/15. The 5/22 spike to 74.5%
is the anomaly. The 8/21 modest tick to 66.0% is the earnings embed
(consistent with phase-3's read that the 8/21 expiry is the post-earnings
positioning vehicle).

### Term skew (30 DTE)

| Metric | Value |
|--------|-------|
| Call 25Δ IV | 63.28% |
| Put 25Δ IV | 64.62% |
| **Skew (put - call)** | **+1.34 vol pts** |
| Skew ratio | 1.021 |
| **Regime** | **NORMAL** |

Skew is **NORMAL** — not steep puts, not complacent. No tail-hedge
premium. The market is pricing modest natural put richness and not
expecting a tail-event.

### Front-end IV ratio (7d vs 30d)

| Metric | Value |
|--------|-------|
| Near IV (4 DTE) | 74.51% |
| Far IV (31 DTE) | 67.80% |
| Ratio | **1.099** |
| **Regime** | **BACKWARDATION** |

The front-end is **bid by 10%** relative to the 30D. Standard threshold
for backwardation is >1.05; LRCX is at 1.10. This is real event premium
into 5/22 OPEX week.

### Today's gamma flip (5/15 expiry only)

| Strike | GEX | Role |
|-------:|----:|------|
| **285** | **-$228.7M** | **resistance_wall** (where spot sat) |
| **300** | **+$151.7M** | **support_wall** |
| **290** | +$115.8M | support_wall |
| **287.5** | +$97.0M | support_wall |
| **280** | +$77.1M | support_wall |

Intraday 5/15: spot was pinned at the $285 negative-gamma node with
positive support walls at $287.5/$290/$300 above. The day printed exactly
in that band ($282–$287). 0DTE pin worked. Today_zero_gamma was $218.27;
ATM-flip-strike $120 (a deep-OTM artifact from intraday call wall
positioning).

## Tool calls (audit trail)

| Tool | Args | Result |
|------|------|--------|
| `mcp__uw-pp__options_structure_gex` | symbol=LRCX, dte-max=45, date=2026-05-15 | Total +$109M, ZGL $70.78 |
| `mcp__uw-pp__options_structure_dex` | symbol=LRCX, dte-max=45, date=2026-05-15 | Net +$9.3B |
| `mcp__uw-pp__options_structure_vanna_charm` | symbol=LRCX, dte-max=45, date=2026-05-15 | Vanna -49k, Charm +810k |
| `mcp__uw-pp__options_structure_iv_term_structure` | symbol=LRCX, date=2026-05-15 | 17 expiries, kinked |
| `mcp__uw-pp__options_structure_term_skew` | symbol=LRCX, dte-target=30, date=2026-05-15 | NORMAL, 1.021 |
| `mcp__uw-pp__options_structure_front_end_iv_ratio` | symbol=LRCX, near-dte=7, far-dte=30, date=2026-05-15 | BACKWARDATION 1.099 |
| `mcp__uw-pp__options_structure_today_gamma_flip` | symbol=LRCX, date=2026-05-15 | resistance_wall 285 |

## Tool errors

(none)

## Verdict for downstream phases

- **Bias from this phase:** **LONG-GAMMA STABILITY with NEAR-TERM EVENT
  PREMIUM**. The dealer hedging map is constructive: positive 45-DTE GEX,
  positive DEX (dealers short calls → buy stock), positive support at
  $280–$300 cluster. But the kinked front-end (5/22 IV 74.5%) means
  someone is pricing in a near-term event into next week. Combined with
  vanna negativity (a vol crush would un-hedge dealer longs and add
  selling), the structure is **mildly bullish-but-fragile**.
- **Conviction: 4/5**. GEX, DEX, term structure, and skew are all
  internally consistent. The single open mystery is the front-end IV
  spike with no named catalyst.
- **Three structural levels for phase-9:**
  1. **Gamma support: $280** (+$30.5M 45-DTE GEX node). Buy zone.
     Aligns with phase-2 S1 $283–$284 and phase-3 stop-out zone.
  2. **Gamma break: $260** (-$53.5M, the biggest negative-gex hole below
     spot). If $280 breaks, the path of least resistance is $260 — also
     where the Jan'27 260P was bid for $1.03M (phase-1) and 5/22 260P has
     6,653 OI (phase-3).
  3. **Upside dealer band: $290–$300** (today 5/15 had +$97/116/152M
     positive walls). Dealers will sell into this band; combined with
     dark-pool resistance at $295.44 (phase-2) and 8/21 310C/400C
     overwriting (phase-3), this is a **stacked institutional ceiling**.
- **Open questions:**
  - **Why is 5/22 IV at 74.5%?** No earnings is scheduled before then.
    Candidates: (a) FOMC / macro data print, (b) semis sector OPEX
    hedging spillover (recall SMH 5/22 500P had $48.8M premium from
    phase-1), (c) China export-controls headline risk, (d) idiosyncratic
    company news leak. **Phase 6 macro must scan for this.**
  - **Will IV mean-revert lower into next week, triggering vanna
    selling?** If yes, $280 support is in play. If 5/22 IV stays bid,
    dealer gamma keeps stabilizing.
  - **Does the 8/21 IV bump (+1.3 pts above the 7/17 baseline) imply
    earnings ARE inside the 8/21 expiry?** Phase 5 historical earnings
    pattern will confirm.
