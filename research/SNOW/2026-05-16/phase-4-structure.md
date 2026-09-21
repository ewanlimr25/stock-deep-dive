# Phase 4 — Dealer Structure & Gamma

**Ticker:** SNOW
**As-of date:** 2026-05-16 (data date: 2026-05-15)
**Generated:** 2026-05-17T00:00:00Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md

## Summary

Dealer structure on SNOW is **strongly POSITIVE GEX** (total GEX = $4.83 billion, all DTE ≤ 45) with **Zero Gamma Level at $154.56**, just $3 below spot ($157.60). Spot is **above ZGL**, so dealers are net long gamma → mean-reverting tape, suppressed realized vol, support on dips and sell-the-rip on rallies. The dominant strike gravity well is **$160** ($2.3B net GEX) — the dealer wall. Net DEX is **+$113.8B (public call-long)**, so dealers are short calls and must buy underlying on rallies (delta hedging). Vanna is negative — **falling IV cuts the dealer hedge bid**. Term structure is in **CONTANGO** (front 7d IV 71.2% < far 30d IV 84.9%) on the front-end ratio of 0.839, but the full term curve technically prints "BACKWARDATION" only because of the 0DTE 5/15 expiry's 196% IV pin artifact. **Earnings or event premium is NOT priced** in the next 1-4 weeks — 25Δ skew at 30 DTE is +0.015 with skew_ratio 0.982 = **COMPLACENT** regime.

## Key signals

- **Total GEX +$4.83B** [STRUCT:gex] — **POSITIVE regime**, dealers long gamma, expect mean-reversion intraday. ZGL = $154.56, spot $157.60 → **3 points above flip**, comfortable long-gamma bandwidth.
- **$160 strike is the dominant gamma wall** [STRUCT:gex]: net_gex = **$2,311,523,013** at strike 160 — single largest absorbing strike in the chain. Spot will magnetize toward $160 on dips/rallies through this level.
- **DEX = +$113.8B (call-heavy public)** [STRUCT:dex] — dealers must BUY underlying as spot rises (chasing delta). This is the mechanical bid that has been lifting SNOW intraday.
- **Vanna NEGATIVE (-$678,799)** [STRUCT:vanna_charm] — falling IV → dealers (short calls) cut long-stock hedges → **IV crush is bearish for SNOW**. Conversely, an IV spike here would mechanically force more dealer buying.
- **30 DTE 25Δ skew = COMPLACENT** [STRUCT:term_skew]: put_25d_iv 82.9% vs call_25d_iv 84.4%, skew_ratio 0.982 — **calls richer than puts**, no tail-hedging demand. This is bullish in the short term but a complacent regime that can snap.

## Detailed findings

### GEX (dealer gamma exposure)

[STRUCT:gex] for DTE ≤ 45:

```
regime: POSITIVE
total_gex: +$4,833,651,697
zero_gamma_level: $154.56
underlying_price: $157.60
spot - ZGL: +$3.04 (+1.93%)
```

**Top 10 positive-GEX strikes (dealer absorbing walls above spot):**

| Strike | net_gex ($) | vs spot |
|---|---|---|
| **160** | **+2,311,523,013** | +$2.40 (+1.5%) |
| 170 | +855,232,491 | +$12.40 (+7.9%) |
| 155 | +192,991,889 | -$2.60 (-1.6%) |
| 165 | +166,844,501 | +$7.40 (+4.7%) |
| 167.5 | +101,665,080 | +$9.90 (+6.3%) |
| 162.5 | +73,017,473 | +$4.90 (+3.1%) |
| 157.5 | +7,667,519 | -$0.10 |
| 172.5 | +4,051,744 | +$14.90 |
| (below 155 = all negative) | | |

**Negative-GEX strikes (short-gamma support zone, dealers buy on dips):**

| Strike | net_gex ($) | vs spot |
|---|---|---|
| 152.5 | -37,225,308 | -$5.10 (-3.2%) |
| 150 | -4,774,681 | -$7.60 (-4.8%) |
| 145 | -24,292,046 | -$12.60 (-8.0%) |
| 140 | -33,125,743 | -$17.60 (-11.2%) |
| 135 | -9,246,269 | -$22.60 |
| 130 | -14,888,573 | -$27.60 |
| 125 | -9,343,363 | -$32.60 |
| 120 | -6,851,027 | -$37.60 |

The structure is asymmetric: **positive GEX is concentrated at $155-$170 (call walls)** while **negative GEX is distributed across $140-$152.50 (put walls below)**. Above ZGL ($154.56), dealers are long gamma → they sell rallies and buy dips → **suppressed realized vol with a magnet toward $160**. Below ZGL, dealers flip short gamma → they sell dips → **realized vol expands** if SNOW breaks $154.56 to the downside.

**Key gamma walls for trading:**
- **$160 = primary magnet** ($2.3B net GEX). Dealer hedging will pin spot toward $160 on most paths.
- **$170 = secondary upside cap** ($855M net GEX). Even if SNOW breaks $160, the next resistance is $170 from dealer selling.
- **$154.56 = ZGL** — the demarcation. Below this, regime flips negative-gamma and the tape gets messy.
- **$152.50 = first significant negative-GEX strike** ($-37M). A break below this would push dealers into actively SELLING into the move down, opening the trapdoor to $140-$145.

### DEX (net dealer delta)

[STRUCT:dex]:

```
call_dex: +$120,401,489,763
put_dex:  -$6,605,429,597
net_dex:  +$113,796,060,166
interpretation: public net call-long → dealers net short calls → dealer hedge BUYS underlying on rallies
```

This is enormous. Public is overwhelmingly call-long on SNOW; dealers are short calls and must accumulate stock as spot rises (delta-hedging). This is the **mechanical bid** that explains how SNOW rallied $5+ intraday on 5/15 despite phase-2's BLOCK-tier dark-pool selling. As spot pushed from $153 to $159, dealer call deltas rose, dealers bought stock to hedge. The institutional sellers in dark pool provided the supply, dealers were the buyers. **This is the structural bullish kicker for SNOW** — as long as call-OI remains call-heavy and dealers stay short calls, every move higher requires more dealer buying.

The downside risk: if SNOW reverses, dealer hedging is symmetric — dealers SELL underlying to cut delta, mechanically reinforcing the downside until enough OI burns off.

### Vanna + charm

[STRUCT:vanna_charm]:

```
call_vanna: -$722,394
put_vanna:  +$43,594
net_vanna:  -$678,799     (NEGATIVE)
net_charm:  +$48,987,797  (positive — theta decay favors short-options dealer book in time)
```

The book is **net negative vanna**. Interpretation:
- **Vanna ↓ as IV ↓**: Public is call-heavy. If IV falls, call deltas drop. Dealers (short calls) need less long-stock hedge → SELL underlying.
- **Vanna ↑ as IV ↑**: If IV spikes (e.g., on a fast move), call deltas rise, dealers BUY underlying.

In a **stable-or-falling IV environment** (which is the base case in a positive-GEX regime), vanna provides a slow drip of SELLING pressure as time and IV decay. This is a **secondary headwind** to keep in mind once the dealer-buying-on-rally pulse exhausts.

The positive net_charm is mechanical — dealers earn theta on their short options book. Not a directional signal, just a structural fact.

### IV term structure

[STRUCT:iv_term_structure]:

| Expiry | DTE | avg IV | contracts |
|---|---|---|---|
| 2026-05-15 | 0 | **196.1%** | 11,579 (artifact) |
| 2026-05-22 | 7 | 71.2% | 7,475 |
| 2026-05-29 | 14 | 107.6% | 2,894 |
| 2026-06-05 | 21 | 96.5% | 713 |
| 2026-06-12 | 28 | 88.9% | 240 |
| 2026-06-18 | 34 | 84.9% | 3,194 |
| 2026-06-26 | 42 | 81.3% | 148 |
| 2026-07-17 | 63 | 74.5% | 972 |
| 2026-08-21 | 98 | 71.1% | 383 |
| 2026-09-18 | 126 | 71.9% | 338 |
| 2026-10-16 | 154 | 68.8% | 103 |
| ... LEAPs trending to 62-67% ... | | | |

Server tag: `BACKWARDATION` — but this is driven by the 5/15 0DTE 196% IV which is a pin-day artifact, not informational. Removing the 0DTE, **the term curve is in healthy contango from 5/22 outward EXCEPT for a kink at 5/29 (107.6%) and 6/5 (96.5%)** that is **substantially above 5/22 (71.2%)** and **above 6/18 (84.9%)**.

**This kink is the signature of a binary event priced into the 5/29 expiry.** Probable cause: SNOW Q1 FY27 earnings (Snowflake typically reports late May / early June). The kink magnitude (107.6% on 5/29 vs 71.2% on 5/22 vs 84.9% on 6/18) implies a binary move expected between 5/22 (post-OPEX) and 5/29. Phase 6 should confirm SNOW's earnings date.

### Term skew (25Δ put vs call IV at 30 DTE)

[STRUCT:term_skew]:

```
dte_actual: 32
call_25d_iv: 84.41%
put_25d_iv:  82.91%
skew:        -0.015  (calls richer than puts)
skew_ratio:  0.982
interpretation: COMPLACENT
```

**Calls are slightly richer than puts** at 30 DTE — the opposite of the typical equity skew (where puts are richer because of crash hedging demand). This is consistent with:
- Speculative call buying (phase-1 confirmed)
- Lack of put-protection demand
- Low realized vol regime (positive-GEX dealer regime, phase-4 confirmed)

The COMPLACENT tag is a **mild contrarian flag**: when skew flips this way, downside surprises are unhedged and can produce outsized drawdowns. But absent a catalyst, this regime can persist for weeks.

### Front-end IV ratio

[STRUCT:front_end_iv_ratio] (near=7 DTE, far=30 DTE):

```
near_iv: 71.23%
far_iv:  84.91%
ratio:   0.839
regime:  CONTANGO
```

Front IV is sharply lower than far IV → **CONTANGO regime, no near-term event stress**. The earnings kink at 5/29 (not the 7DTE bucket) is consistent with this — the event is far enough out that 7d IV is "off the curve". The 30 DTE IV (84.9%) is elevated relative to LEAP IV (62-67%), which captures the earnings premium.

**IV-trade implication:** the earnings vol crush trade is alive — selling 5/29 straddles or strangles (or 5/29 vs 5/22 calendars) would capture the elevated 5/29 IV that should mean-revert post-event.

### Today's gamma flip (intraday 0DTE)

[STRUCT:today_gamma_flip]:

```
regime: POSITIVE
today_total_gex: $39,456,010,312 (0DTE only)
today_zero_gamma: $98.81
atm_flip_strike: $95
spot: $157.50
```

**Key 0DTE walls:**

| Strike | Role | net_gex |
|---|---|---|
| 155 | support wall | +$17,339,106,139 |
| 160 | support wall | +$13,663,133,958 |
| 157.5 | support wall | +$6,229,390,229 |
| 162.5 | support wall | +$901,448,090 |
| 150 | support wall | +$553,427,786 |

All key 0DTE walls are tagged "support_wall" (positive GEX). 0DTE ZGL was $98.81 — far below spot — so 5/15 was strongly long-gamma all day, which explains the orderly grind higher into close after the morning sell-down. **The mean-reversion regime is well-established intraday and structural for SNOW currently.**

But note: this is 5/15 (now expired). The 5/16 0DTE structure begins fresh on Monday 5/18.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__options_structure_gex` | symbol=SNOW, dte_max=45 | total_gex +$4.83B, ZGL $154.56, $160 wall $2.3B |
| `mcp__uw-pp__options_structure_dex` | symbol=SNOW, dte_max=45 | net_dex +$113.8B, public call-heavy, dealers buy rallies |
| `mcp__uw-pp__options_structure_vanna_charm` | symbol=SNOW, dte_max=45 | net_vanna -$679k, net_charm +$49M |
| `mcp__uw-pp__options_structure_iv_term_structure` | symbol=SNOW | Tagged BACKWARDATION (0DTE artifact); kink at 5/29 = earnings |
| `mcp__uw-pp__options_structure_term_skew` | symbol=SNOW, dte_target=30 | skew_ratio 0.982, COMPLACENT |
| `mcp__uw-pp__options_structure_front_end_iv_ratio` | symbol=SNOW, near_dte=7, far_dte=30 | ratio 0.839, CONTANGO |
| `mcp__uw-pp__options_structure_today_gamma_flip` | symbol=SNOW | 0DTE positive, walls $150/$155/$157.5/$160/$162.5 |

## Tool errors

None.

## Verdict for downstream phases

- **Dealer regime:** **Long-gamma / POSITIVE GEX** while spot > $154.56. Mean-reverting tape, suppressed realized vol, magnetic pull toward $160. Dealers BUY underlying on rallies (call-heavy DEX).
- **Conviction:** 4/5. The GEX, DEX, and 0DTE gamma flip tools all align. The vanna negative is a slow drag, not a regime threat.
- **Three structural levels for phase-9:**
  1. **$160 = primary gamma magnet** ($2.31B net GEX). High-probability mean-revert target for any pullback OR rally extension. Use as **profit-take #1** on long entries.
  2. **$154.56 = ZGL (regime flip)**. **Hard invalidation line for any long thesis** — below this, dealers flip short-gamma and the tape gets violent.
  3. **$170 = secondary upside cap** ($855M net GEX). The next dealer wall above. Use as **profit-take #2** or stretch target. Above $170 the gamma structure thins, so a break above $170 is structurally significant.
- **Open questions:**
  - The 5/29 IV kink (107.6% vs 71.2% / 84.9% neighbors) = **earnings event in that window**. Phase-6 macro must confirm the SNOW Q1 FY27 report date.
  - If dealers are long $2.3B GEX at $160, **what was the institutional flow that built it?** Cross-check phase-3: 5/29 200C bid-side build (+821 OI) and 6/18 180C bid-side build (+929 OI) — institutions writing premium that landed in dealer hands. Confirmed.
  - Is the $145 strike from phase-1's directional buy structurally significant? At -$24M GEX (negative), it's a **short-gamma support level** below ZGL — if SNOW gets to $145, dealers are forced sellers, amplifying downside. The phase-1 145C buyer is betting against this dynamic — they want SNOW to STAY above $145.
