# Phase 4 — Dealer Structure & Gamma

**Ticker:** BILI
**As-of date:** 2026-05-20 (data date 2026-05-19)
**Generated:** 2026-05-20T10:00:00-04:00
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md

## Summary

BILI is in a **POSITIVE gamma regime** — dealers net long gamma $226.8M with
spot $19.55 sitting **+2.3% above the Zero Gamma Level ($19.11)**. The single
overwhelmingly dominant strike is **$20, holding +$117.6M of dealer GEX** —
the structural pin/magnet for the next OPEX. The DEX is **+$336M net call-long
public**, meaning dealers are net short calls and **mechanically buy the
underlying** on any IV expansion or rally toward call strikes. The term
structure is in clear **BACKWARDATION** (front 9-DTE IV 61.6% / far 29-DTE
55.6%, ratio 1.107) — an event-stress signature, consistent with phase-3's
near-OPEX positioning crowding. Critically, **25-delta skew is INVERTED**
(call IV 55.8% > put IV 53.9%, "COMPLACENT"), confirming the institutional
call-demand structure inferred in phase-3 — not classic tail-hedging skew.

## Key signals

- **Total GEX = +$226,786,819 (POSITIVE)** — long-gamma dealers, mean-reversion
  regime [STRUCT:gex].
- **Zero Gamma Level = $19.11**, spot $19.55 → **+2.3% above ZGL**
  [STRUCT:gex].
- **$20 GEX wall = +$117,596,555** — biggest single-strike gamma magnet by 2x
  [STRUCT:gex,today_gamma_flip].
- **Net DEX = +$336,295,121** → public call-long → dealer hedge BUYS
  underlying [STRUCT:dex].
- **25Δ skew = -0.0192 (COMPLACENT, INVERTED)** — calls pricier than puts at
  30 DTE [STRUCT:term_skew].
- **Term structure ratio 1.107 (BACKWARDATION)** — front 61.6% / far 55.6%
  [STRUCT:front_end_iv_ratio,iv_term_structure].

## Detailed findings

### GEX per-strike (DTE ≤ 45) [STRUCT:gex]

| Strike | Net GEX ($) | Role |
|---|---|---|
| 13 | -14,338 | trivial |
| 15 | -79,427 | neg, deep OTM |
| 16.5 | -105,732 | neg |
| 17 | **-2,445,689** | **negative wall** |
| **17.5** | **-5,414,431** | **biggest negative GEX (accel zone if breached)** |
| 18 | -971,409 | neg |
| 18.5 | -2,146,826 | neg |
| **19** | **-2,523,397** | **last neg before flip** |
| **19.5** | **+61,385,854** | **positive wall (secondary support)** |
| **20** | **+117,596,555** | **MAGNET — biggest positive GEX** |
| 20.5 | +4,345,354 | pos |
| **21** | **+19,421,003** | **upper support / wall** |
| 21.5 | +2,998,406 | pos |
| **22** | **+17,116,994** | **upper resistance / wall** |
| 22.5 | -24,829 | trivial neg (matches put-roll strike) |
| 23 | +1,984,559 | pos |
| 24 | +5,449,947 | pos |
| **25** | **+9,014,922** | **structural pos (Jan-27 strike echo)** |
| 28 | +410,476 | pos |
| 30 | +265,201 | pos (echo of Jul-17 short calls) |

**Reading:**
- Below **$19.11 (ZGL)** the dealer book flips to net short gamma → trend
  amplification, expanded realized vol.
- The **$20 strike alone holds 51.8% of total GEX** ($117.6M / $226.8M). For
  the next two weeks, expect mean-reversion toward $20 — classic GEX pin.
- Negative GEX cluster at $17–$17.5 forms a **gamma cliff**: if spot rejects
  the $20 magnet on a downside catalyst and breaches $19 → ZGL ($19.11) →
  acceleration toward $17.50 is mechanically supported by dealer
  short-gamma hedging.
- The $22 wall (+$17.1M) is a **breakthrough resistance**; once cleared, the
  $25 strike (+$9.0M) becomes the next magnet (matches phase-3 institutional
  bull-call-spread target).

### DEX & dealer hedge direction [STRUCT:dex]

```
Call DEX (public) : +$442,403,800
Put DEX (public)  :  -$106,108,679
NET DEX           : +$336,295,121
```

Public is **call-long by $336M of delta-weighted notional** → dealers SHORT
calls → dealer hedge **BUYS underlying**. This is a **structural bid** as
long as IV expands, gamma is positive, or spot rallies into call strikes.
Cross-references the +$117M GEX at $20 — same conclusion: dealer-hedge demand
is concentrated around $20.

### Vanna & charm [STRUCT:vanna_charm]

```
Call vanna :  -14,895
Put vanna  :   +6,391
NET vanna  :   -8,504  (slightly negative)
NET charm  :  +3,788,322
```

- **Vanna**: small net-negative. Interpretation: **rising IV is supportive**
  (dealers hedge call book by buying more underlying). Falling IV → mechanical
  selling.
- **Charm**: net positive $3.79M. Each day, time-decay erodes call delta;
  dealers (short calls) progressively cut their long-stock hedge → small
  daily selling pressure. This is **why the $20 magnet operates**: charm
  bleeds delta back into the dealer book, who then re-hedge by selling small
  amounts.

No vanna-squeeze setup detected (would require positive vanna + negative
dealer delta + declining IV; here vanna is slightly negative).

### IV term structure [STRUCT:iv_term_structure]

| Expiry | DTE | Avg IV | Contract count |
|---|---|---|---|
| **2026-05-22** | **3** | **85.7%** | **1,030** |
| 2026-05-29 | 10 | 61.6% | 164 |
| 2026-06-05 | 17 | 62.3% | 37 |
| 2026-06-12 | 24 | 62.1% | 21 |
| **2026-06-18** | **30** | **55.6%** | **185** |
| 2026-06-26 | 38 | 58.7% | 29 |
| **2026-07-17** | **59** | **56.1%** | **58** |
| 2026-08-21 | 94 | 59.1% | 17 |
| 2026-10-16 | 150 | 53.7% | 14 |
| **2027-01-15** | **241** | **60.3%** | **167** |
| 2027-12-17 | 577 | 61.8% | 45 |
| 2028-01-21 | 612 | 59.9% | 30 |

**Structure: BACKWARDATION** with a steep front-week kink. The 5/22 weekly
85.7% IV is inflated almost entirely by the **deep-ITM $22.5 put** in the
phase-1 roll (which carried 150%+ IV individually). Excluding that artifact,
the true front-month IV would be ~62% — still backwardated vs the 6/18 55.6%
trough, but less dramatically. **Real economic signal: front 9-DTE 61.6% / far
29-DTE 55.6% backwardation = mild event/catalyst stress.**

Back-end is flat at 55–62% across 30–612 DTE — no LEAP vol premium. Healthy.

### 25Δ term skew at DTE=30 [STRUCT:term_skew]

```
25Δ call IV : 55.80%
25Δ put IV  : 53.88%
Skew        : -0.0192 (call IV minus put IV / call IV)
Regime      : COMPLACENT (INVERTED skew — calls richer than puts)
```

**This is unusual and important.** Single-name equities typically have
*positive* skew (puts pricier than calls due to crash-risk premium). BILI's
inverted skew at 30 DTE means **option-market participants are paying up for
upside, not downside** — exactly the pattern you'd expect from the
institutional bull-call-spread program identified in phase-3. The
"COMPLACENT" label correctly notes no tail-hedging premium.

### Front-end IV ratio [STRUCT:front_end_iv_ratio]

```
Near 9-DTE IV : 61.6%
Far 29-DTE IV : 55.6%
Ratio         : 1.107
Regime        : BACKWARDATION (event stress, ratio > 1.05)
```

Mild backwardation. Not a hard binary-event print (would expect ratio > 1.3
for earnings stress); more consistent with **chained-OPEX positioning** —
flow-and-OI participants crowded into the 5/22 weekly. Should ease into 6/18
monthly.

### Today's 0DTE gamma map [STRUCT:today_gamma_flip]

(Today's expiry = 2026-05-22 weekly, 3 DTE — closest tradeable expiry.)

```
Today (5/22) total GEX  : +$206,338,671 (POSITIVE)
Today's ZGL             : $15.01 (well below spot $19.51)
ATM flip strike         : $15.50
```

Walls keyed for 5/22 expiry:

| Strike | GEX | Role |
|---|---|---|
| **20** | **+$121,907,945** | **today's primary support / pin** |
| 19.5 | +$59,289,092 | secondary support |
| 22 | +$16,405,760 | resistance (call OI wall — phase-3: 2,512 OI here) |
| 21 | +$13,769,442 | mid resistance |
| **17.5** | **-$5,387,570** | **resistance wall (negative GEX accel zone if breached)** |

The 5/22 walls reinforce the multi-expiry GEX read: **$20 is the magnet
through Friday**, $22 is the cap, $17.5 is the downside acceleration trigger.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|---|---|---|
| `options_structure_gex` | symbol=BILI, dte-max=45 | Total GEX +$226.8M, ZGL $19.11, $20 dominant wall |
| `options_structure_dex` | symbol=BILI, dte-max=45 | Net DEX +$336.3M (call-long public) |
| `options_structure_vanna_charm` | symbol=BILI, dte-max=45 | Net vanna -8.5k (slight neg), charm +$3.79M |
| `options_structure_iv_term_structure` | symbol=BILI | BACKWARDATION; 12 expiries; 5/22 weekly 85.7% (inflated) |
| `options_structure_term_skew` | symbol=BILI, dte=30 | COMPLACENT inverted skew -0.0192 |
| `options_structure_front_end_iv_ratio` | symbol=BILI, near=7, far=30 | Ratio 1.107 BACKWARDATION |
| `options_structure_today_gamma_flip` | symbol=BILI | 5/22 ZGL $15.01, ATM flip $15.5, $20 wall +$121.9M |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** **structurally constructive / range-bound at
  $19–$22** with a strong $20 magnet. Above-ZGL long-gamma regime suppresses
  volatility; positive DEX delivers a mechanical dealer bid; inverted skew
  confirms call demand is real.
- **Conviction:** **4 / 5** — total GEX magnitude is small in absolute terms
  ($227M; small-cap single name) but the per-strike concentration at $20 is
  unambiguous and the regime classification is unanimous across GEX / DEX /
  skew / term structure.
- **Three structural levels for phase-9:**
  1. **Magnet / pin: $20.00** — primary gamma magnet (+$117M; today's wall
     +$122M). Expect price to gravitate here through 5/22 OPEX.
  2. **ZGL / regime-change line: $19.11** — break below = transition to
     short-gamma → vol expansion → mechanical accel toward $17.50.
  3. **Breakthrough resistance: $22.00** — +$17M GEX cap; coincides with
     phase-2 5-day DP overhead at $22.30 and phase-3 call OI wall (2,512
     OI). A daily close above $22 unlocks $25 (next +$9M GEX magnet).
- **Open questions:**
  - Is the front-end IV backwardation (1.107) being driven by an upcoming
    catalyst (earnings? China policy?) or just flow crowding? → phase-5
    historical IV percentile + phase-6 macro should resolve.
  - Is BILI structurally rich/cheap on realized vol vs implied (VRP)? →
    phase-5 historical VRP series.
  - With charm bleed and a strong $20 magnet, what's the realistic 1-σ
    range for next 5 days? Phase-9 needs this for entry/stop sizing.
