# Phase 4 — Dealer Structure & Gamma

**Ticker:** USAR
**As-of date:** 2026-05-20 (effective UW data date: 2026-05-19)
**Generated:** 2026-05-20T10:30:00-04:00
**Upstream phases cited:** phase-0, phase-1, phase-2, phase-3

## Summary

USAR is in a **SHORT-GAMMA regime**, with spot $20.02 sitting $4.96
(-19.8%) **below** the **Zero Gamma Level of $24.98**. The dealer book is
short gamma from $14 to $21 (per-strike GEX deeply negative across this
entire range) and long gamma from $22 upward, with a **dominant
+$383.5M GEX line at the $25 strike** — by far the chain's largest gamma
node. This **lines up exactly with the $24.98 ZGL, the dark-pool $25.42
supply cluster (phase 2), and the 5/22 call walls being written at $21+
(phase 3)** — triple confluence at $25 as a structural ceiling and pin
magnet from above. Term structure is in **BACKWARDATION** (5/22 IV 145%
vs 30d IV 105%, ratio 1.389), confirming a near-term binary catalyst.
Skew is **COMPLACENT** (25Δ call IV slightly > put IV at 30d) — the market
is NOT pricing tail-downside premium, which is unusual for an equity that
just dropped 20%, and tilts the read **upside-resolution-biased** despite
the short-gamma trend-amplification risk.

## Key signals

- **Regime: NEGATIVE GEX / short-gamma below $25**, total GEX +$221M is
  dominated by the single $25 strike. ZGL $24.98 = strong upside ceiling.
  [STRUCT:options_structure_gex]
- **$25 strike GEX: +$383,535,631** — the chain's single biggest gamma
  node. Spot must reclaim $25 to flip into long-gamma regime.
  [STRUCT:options_structure_gex]
- **Today's (5/22) gamma flip resistance walls**: $20 (-$45.7M),
  $20.5 (-$23.7M), $19 (-$18.8M); support walls: $21 (+$11.8M),
  $25 (+$10.5M). Today ZGL: $13.65. [STRUCT:today_gamma_flip]
- **DEX = +$411.6M**: public net call-long → dealers net short calls →
  dealer hedge is to BUY underlying. **Dealers are systematic buyers
  of stock** at current levels. [STRUCT:dex]
- **Front-end IV ratio = 1.389** (BACKWARDATION; threshold 1.05) — strong
  event premium in 5/22 expiry. [STRUCT:front_end_iv_ratio]
- **Term skew = COMPLACENT** (25Δ call IV 102% vs put IV 100% at 29 DTE) —
  unusual absence of put protection bid post-20% drop.
  [STRUCT:options_structure_term_skew]
- **Net vanna: -12,798 (small but negative)**; **net charm: +$4.46M
  (positive)** — vol crush after 5/22 → selling pressure; positive charm
  = slow long-the-stock tailwind from time decay alone.
  [STRUCT:vanna_charm]

## Detailed findings

### GEX (≤45 DTE)

**Total GEX:** +$221,082,179 (the aggregate is positive only because of
the single $25 line; everything between $14–$21 is deeply negative).
**Regime:** NEGATIVE (spot below ZGL).
**Zero Gamma Level:** $24.98.

Top 10 strikes by absolute GEX:

| Strike | Net GEX | Sign | Role |
|--------|---------|------|------|
| **25** | **+$383,535,631** | + | **Mega gamma magnet / pin from above** |
| 20 | -$175,761,744 | − | Short-gamma accelerator at spot |
| 30 | +$135,902,898 | + | Upper magnet (12,424 OI 6/18 $30C) |
| 18 | -$73,361,223 | − | Short-gamma accelerator (put wall) |
| 17 | -$36,994,533 | − | Short-gamma accelerator (put wall) |
| 21 | -$34,612,543 | − | Short-gamma accelerator (the 16,949 OI 6/18 $21P) |
| 27 | +$27,451,489 | + | Long-gamma above magnet |
| 19 | -$24,676,469 | − | Short-gamma at spot region |
| 20.5 | -$23,928,251 | − | Short-gamma at spot region |
| 24 | +$21,680,908 | + | Long-gamma above magnet |

**Reading**: USAR is structurally **upside-magnetized to $25** but
**volatility-amplified at current $20 spot**. Any directional break in
either direction through the $19–$21 short-gamma corridor will accelerate
(dealers chase), but the natural mechanical magnet is $25 from above.

### DEX (net dealer delta hedge)

```
call_dex   = +$3,774,763,629
put_dex    = -$3,363,151,911
NET DEX    = +$411,611,718  (≈ $20.5M shares-equivalent at $20)
```

The interpretation field reports: *"Public is net call-long → dealers net
short calls → dealer hedge is to BUY underlying."*

That is a **mildly bullish structural tailwind**: dealers hedging short
calls are systematic underlying buyers. This is consistent with the
phase-2 dark-pool large-tier buy_ratio of 0.623 — institutional dealer
hedging may be a meaningful contributor to that bid pressure.

### Vanna + charm

```
call_vanna = -162,532
put_vanna  = +149,734
NET VANNA  = -12,798     (slightly negative, call-heavy book)
NET CHARM  = +4,464,901  (positive — meaningful)
```

**Vanna interpretation** (from tool): *"Falling IV → call delta drops →
dealers (short calls) cut long-underlying hedge → SELLING pressure.
Rising IV reverses."*

→ **Post-event vol crush after 5/22 = mechanical selling pressure**.
Holders into the catalyst should expect a "sell the news" hedge unwind
even if the news itself is bullish.

**Charm interpretation**: Positive net charm of $4.46M means dealer
delta becomes more positive as time elapses → dealers must buy more
stock just from time decay (assuming spot stable). Modest tailwind in
the days approaching expiry, **until** vol crush overrides.

### IV term structure

| Expiry | DTE | Avg IV | Contracts |
|--------|-----|--------|-----------|
| 2026-05-22 | 3   | **145.2%** | 2,031 |
| 2026-05-29 | 10  | 113.0% | 771 |
| 2026-06-05 | 17  | 119.1% | 403 |
| 2026-06-12 | 24  | 103.8% | 179 |
| 2026-06-18 | 30  | 104.5% | 1,629 |
| 2026-06-26 | 38  | 102.7% | 131 |
| 2026-07-17 | 59  | 98.8% | 331 |
| 2026-09-18 | 122 | 101.4% | 344 |
| 2026-12-18 | 213 | 100.8% | 173 |
| 2027-01-15 | 241 | 99.5% | 441 |
| 2028-01-21 | 612 | 97.3% | 228 |

**Structure: BACKWARDATION**. The 5/22 → 5/29 drop is **32 vol points**
in 7 days — overwhelming evidence of a 5/22-window catalyst. The
secondary **5/29 → 6/5 bump (113% → 119%)** is notable but driven by a
small contract count (403); could be either a secondary catalyst or
sample noise. **Phase 7 earnings_play must check both windows.**

Floor IV across the back-end ~ 97–101% — that is USAR's "structural" vol
level. Even the 2028 LEAP IV at 97% is high; this is a name with chronic
vol regardless of catalyst.

### Term skew (25Δ, ~30 DTE)

```
call_25d_iv  = 101.77%
put_25d_iv   = 100.14%
SKEW         = -0.0163  (calls richer than puts)
RATIO        = 0.984
INTERPRETATION: COMPLACENT
```

**This is structurally anomalous.** After a -20% drawdown (phase 2 shows
spot dropped from $25.42 → $20 area in the last 5 sessions), normal
equity skew would have **puts substantially richer** as portfolio
managers chase protection. Instead, calls are slightly more expensive
than puts. Reads two ways:

1. **Bullish bias**: the option-buying flow is on the upside (consistent
   with the call lottery tickets in phase 1 + the $25 GEX magnet); few
   buyers see a need to pay up for downside.
2. **Already-hedged bias**: institutions that wanted protection already
   bought it earlier in the slide; the marginal incremental demand has
   shifted to upside calls.

Either way, **the market is NOT pricing further downside as the dominant
scenario from here**. This tilts the structural read **upside-biased**
beneath the short-gamma volatility regime.

### Front-end IV ratio

```
near_dte  = 2  (5/22 expiry approx)
near_iv   = 145.2%
far_dte   = 29 (6/18 expiry approx)
far_iv    = 104.5%
RATIO     = 1.389
REGIME    = BACKWARDATION
```

A 1.389 ratio is **deep backwardation** — well above the 1.05 threshold.
This is event-stress: the market is paying massively for 3-day vol.

### Today's gamma flip (5/22 expiry, 0DTE-ish)

```
today_expiry     = 2026-05-22
spot             = $20.10
today_total_gex  = -$66,600,796   (deeply negative)
today_zero_gamma = $13.65          (only ~$5/sh below — distant)
atm_flip_strike  = $13.50
regime           = NEGATIVE
```

**Key walls**:

| Strike | GEX | Role |
|--------|------|------|
| 20.0 | -$45.7M | **Resistance wall** (negative gamma accelerator) |
| 20.5 | -$23.7M | Resistance wall |
| 19.0 | -$18.8M | Resistance wall |
| 21.0 | +$11.8M | Support wall (positive gamma) |
| 25.0 | +$10.5M | Upper support / magnet |

In 5/22 single-expiry alone, **$21 flips to positive GEX** (only 687 OI
of 5/22 $21P vs 388 OI of 5/22 $21C — the 16,949 OI 6/18 $21P dominates
the 45-DTE bucket but doesn't show in 5/22-only). So **for the 5/22
binary event specifically**, breaking through $21 unleashes positive
gamma (pin-style) toward $25, while breaking below $19 unleashes negative
gamma (acceleration) toward $13.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `options_structure_gex` | symbol=USAR, dte-max=45, date=2026-05-19 | Total +$221M; **ZGL $24.98**; $25 strike +$383.5M dominant |
| `options_structure_dex` | symbol=USAR, dte-max=45, date=2026-05-19 | Net DEX +$411.6M; dealers BUY underlying |
| `options_structure_vanna_charm` | symbol=USAR, dte-max=45, date=2026-05-19 | Vanna -12.8k; charm +$4.46M; vol crush → selling pressure |
| `options_structure_iv_term_structure` | symbol=USAR, date=2026-05-19 | BACKWARDATION; 5/22 IV 145% → 5/29 IV 113% (-32 vol pts) |
| `options_structure_term_skew` | symbol=USAR, dte=30, date=2026-05-19 | **COMPLACENT** (calls richer than puts) |
| `options_structure_front_end_iv_ratio` | symbol=USAR, near=3, far=30, date=2026-05-19 | Ratio 1.389 — deep backwardation |
| `options_structure_today_gamma_flip` | symbol=USAR, date=2026-05-19 | 5/22 expiry, today GEX -$66.6M; walls $19/$20/$20.5 resistance, $21/$25 support |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** **STRUCTURALLY UPSIDE-BIASED beneath a
  short-gamma vol regime**. Dealers are long the stock (DEX +$411M),
  skew is complacent (no downside premium being bid), the dominant
  gamma magnet is at $25 (overhead), and term structure flags a 5/22
  binary catalyst. But the short-gamma corridor $14–$21 means any move
  out of the current zone amplifies before it resolves.
- **Conviction:** **4/5** — structurally the dealer book is unambiguous
  and the $25 confluence (ZGL + GEX magnet + DP supply) is the highest-
  conviction level in this entire deep dive.
- **Three structural levels for phase-9:**
  1. **$24.98 ZGL / $25 GEX magnet / $24.18–$25.95 DP supply band** —
     **PRIMARY OVERHEAD CEILING + UPSIDE TARGET**. If spot reaches $25,
     mean-reversion suppression kicks in and the structural tailwind
     pauses. Reasonable take-profit zone.
  2. **$21 resistance flip → support flip**. Below $21 (today), spot is
     in negative-gamma chase territory. **Reclaiming $21 on a closing
     basis flips 5/22 to positive gamma** and opens the $25 magnet. This
     is the **most important breakout trigger** in the chart.
  3. **$13.65 today's ZGL / $13.50 ATM flip**. If 5/22 catalyst goes
     bearish and spot breaks $18 (phase-3 put-wall floor), the short
     gamma below opens a path to $13.50 — but the chain has no
     meaningful support there per phase 2 dark-pool data, so floors
     would be set by realized panic, not by structure. Worst-case
     invalidation target.
- **Open questions:**
  - Why is skew complacent after a -20% drawdown? Is there positive
    fundamental news priced in? (Phase 6 macro + phase 8 fundamental
    sub-agent.)
  - The 5/22 → 5/29 → 6/5 IV bump (-32 vp then +6 vp): single catalyst
    on 5/22 or two events? (Phase 7 earnings_play.)
  - Does the 2028 $40P put-sale (phase 3) plus DEX +$411M imply the
    smart-money structural bias is **long-stock-via-LEAP-put-write**?
    That would explain the call-skew complacency.
