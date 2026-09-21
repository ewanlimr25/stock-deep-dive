# Phase 4 — Dealer Structure & Gamma

**Ticker:** BABA
**As-of date:** 2026-05-20 (data: 2026-05-19)
**Generated:** 2026-05-20T00:25:00Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md
**Spot reference:** $135.70 (`underlying_price`, GEX file)

## Summary

BABA dealer regime is **POSITIVE / LONG GAMMA** with total GEX of **+$16.48B**
and the **Zero Gamma Level (ZGL) at $135.66 — exactly $0.04 below spot**.
This is the single most important fact in the deep dive: BABA is sitting on the
fulcrum. **Above $135.66:** dealers sell rallies, suppress vol, mean-revert
toward strikes (sticky). **Below $135.66:** dealers sell dips, trend amplifies.
Net DEX of **+$134.7B** (public massively call-long) creates a mechanical
dealer-bid for the underlying (dealers short calls must buy stock as
delta-hedge). The chain shows **massive long-gamma walls at $140 (+$8.5B) and
$150 (+$2.2B)**, framing $140 as a sticky ceiling. Below the ZGL the picture
inverts: **$130 strike net GEX = −$985M** is the largest negative-gamma cluster
and would amplify any breakdown. Term structure is **BACKWARDATION (ratio 1.145)**
with May 22 IV 67.5% vs Jun 18 IV 43.7% — front-end event stress (the OPEX
itself) priced in. 25Δ skew at 30 DTE is **COMPLACENT** (calls richer than
puts), confirming the chain is positioned for upside, not crash hedge.

## Key signals

- **Zero Gamma Level = $135.66**; spot $135.70 → BABA is 0.03% above ZGL,
  on the long-gamma side by a whisker [STRUCT:gex].
- **$140 strike GEX = +$8.51B** — the dominant long-gamma wall acting as
  ceiling; dealer hedge will absorb upside moves [STRUCT:gex].
- **$130 strike GEX = −$985M** — biggest negative cluster, downside
  amplifier if breached [STRUCT:gex].
- Net DEX **+$134.7B** (public call-heavy) → dealers structurally **long
  underlying** as hedge → mechanical bid for BABA shares [STRUCT:dex].
- IV term structure **BACKWARDATION**: May 22 67.5% vs May 29 50.0% vs Jun 18
  43.7%; near/far ratio **1.145** confirms event-pricing into Friday OPEX
  [STRUCT:iv_term_structure] [STRUCT:front_end_iv_ratio].
- 25Δ skew at 30 DTE **COMPLACENT** (calls 4.40 vol > puts 4.12 vol) — chain
  built for upside, no tail-hedge bid [STRUCT:term_skew].

## Detailed findings

### GEX — per-strike concentration (DTE ≤ 45)

Spot $135.70 | ZGL $135.66 | Regime **POSITIVE / LONG GAMMA**

| Strike | Net GEX ($) | Role |
|------:|------------:|------|
| 80–115 | net negative, total ≈ −$30M | distant short-gamma noise |
| **120** | **−249,012,724** | sub-major neg-gamma node |
| 125 | −121,229,071 | neg-gamma node |
| **130** | **−984,891,005** | **largest negative-gamma cluster (breakdown amplifier)** |
| 133 | +32,112,476 | first positive strike below spot |
| 134 | +41,278,858 | accumulating long gamma |
| **135** | **+519,638,761** | long-gamma support wall at spot |
| **136** | **+1,186,861,765** | dominant *support* node |
| 137 | +752,971,346 | support |
| 138 | +476,544,270 | support |
| 139 | +144,459,530 | thin |
| **140** | **+8,507,386,927** | **massive long-gamma ceiling — sticky resistance** |
| 141 | +250,919,461 | step beyond wall |
| 142 | +206,609,096 | |
| **145** | **+2,081,639,425** | secondary ceiling (matches phase-1 LEAP risk reversal target) |
| **150** | **+2,150,396,715** | tertiary ceiling (matches Jan 27 $150C LEAP cluster) |
| 155 | +549,162,266 | upper bound of significant gamma |

Interpretation: between **$135 and $138**, the chain forms a "support ribbon"
totaling **+$2.94B** of positive GEX. Above that, the wall at $140 is
**roughly 4× larger** than everything between $141–$144 combined — i.e.
upside through $140 has to consume the wall before the next gravity well at
$145. Below the ZGL, the chain becomes thin until the **$130 trapdoor**,
where dealer short gamma would mechanically *sell* into weakness. The
asymmetry favors range-trade $135–$140 with **trend-acceleration risk if
$130 breaks**. [STRUCT:gex]

### DEX — net dealer hedge direction

| Bucket | Value |
|------|------|
| `call_dex` | $190,619,383,121 |
| `put_dex` | −$55,925,824,669 |
| **`net_dex`** | **+$134,693,558,452** |
| `interpretation` | "Public is net call-long → dealers net short calls → dealer hedge is to BUY underlying" |

This is a **structurally bullish** condition for share price: dealers must
buy stock to hedge their short-call exposure. If realized vol expands, the
delta on those short calls rises and the buying pressure increases (positive
feedback). If realized vol collapses, the opposite — but with BABA already
sitting on ZGL the hedge baseline is set by the current OI, not by vol
direction alone. [STRUCT:dex]

### Vanna and charm

| Field | Value |
|------|------|
| `call_vanna` | −1,910,390 |
| `put_vanna` | +954,337 |
| **`net_vanna`** | **−956,053** |
| `net_charm` | +191,724,696 |
| `vanna_interpretation` | "Public net vanna negative (call-heavy book). Falling IV → call delta drops → dealers cut long-underlying hedge → **SELLING** pressure. Rising IV reverses." |

So the post-OPEX scenario matters: when May 22 expires and the 67.5% IV
collapses toward the 50% May 29 level, dealers will reduce their long-stock
hedge → **mild mechanical selling pressure into the IV crush**, even if no
news hits. Position sizing in phase 9 must account for this. Charm is large
and positive — dealer call-side delta bleeds toward zero as expiry approaches,
also implying a *reduction* of long hedge as the call OI bleeds. Combined
vanna + charm = **negative mechanical drift post-OPEX** for the underlying.
[STRUCT:vanna_charm]

### IV term structure

| Expiry | DTE | Avg IV |
|--------|---:|------:|
| 2026-05-22 | 3 | **67.5%** |
| 2026-05-29 | 10 | 50.0% |
| 2026-06-05 | 17 | 45.2% |
| 2026-06-12 | 24 | 43.8% |
| 2026-06-18 | 30 | 43.7% |
| 2026-06-26 | 38 | 41.8% |
| 2026-07-17 | 59 | 42.2% |
| 2026-08-21 | 94 | 44.5% |
| 2026-09-18 | 122 | 43.6% |
| 2026-10-16 | 150 | 45.2% |
| 2026-11-20 | 185 | 44.2% |
| 2026-12-18 | 213 | 45.4% |
| 2027-01-15 | 241 | 46.3% |
| 2027-03-19 | 304 | 46.3% |
| 2027-06-17 | 394 | 47.3% |
| 2027-12-17 | 577 | 47.0% |
| 2028-01-21 | 612 | 46.6% |
| 2028-06-16 | 759 | 47.7% |
| 2028-12-15 | 941 | 47.8% |

Structure tag: **BACKWARDATION**. Shape: very steep drop in the first two
weeks (67.5% → 50% → 45%), then flat-to-mild-contango out to LEAPs (~46–48%).
No kink — the front-month IV pop is an **OPEX/event pricing**, not a
forward-dated binary. After May 22 expires, the chain returns to a normal
upward-sloping vol curve. [STRUCT:iv_term_structure]

### 25Δ term skew (30 DTE target)

| Field | Value |
|------|------|
| `put_25d_iv` | 0.4118 |
| `call_25d_iv` | 0.4396 |
| `skew` (call − put) | **+0.0279** in calls (negative if put-rich) |
| `skew_ratio` (put/call) | 0.937 |
| `interpretation` | **COMPLACENT** |

Calls are **richer than puts** by 2.8 vol points — the opposite of a normal
equity skew. This typically reflects **upside speculation demand** (chain
participants bidding up calls), not tail hedging. Consistent with phase-1's
$2.43M ASK-side sweep on Jan 27 $150C and phase-3's $145C May 29 +2,415 OI
buy. Risk: complacency on the put side means a downside surprise has
**less hedging cushion priced in** and could move the skew violently.
[STRUCT:term_skew]

### Front-end IV ratio (near 7 → far 30 DTE)

| Field | Value |
|------|------|
| `near_iv` (9 DTE actual) | 0.4997 |
| `far_iv` (29 DTE actual) | 0.4365 |
| `ratio` | **1.145** |
| `regime` | **BACKWARDATION** (>1.05) |

Confirms the term-structure read. The 14.5% front-end vol premium implies the
chain expects more realized vol in the next ~9 days than the next ~29 days —
i.e. the May 22 OPEX and any associated catalyst (earnings adjacency, China
PMI, headline) is being priced. Phase 6 (macro) must check whether BABA has
a near-term earnings date — Alibaba's typical FQ4 earnings is mid-May, so
this could be **post-earnings** vol still bleeding off. [STRUCT:front_end_iv_ratio]

### Today's gamma flip (May 22 expiry — earliest in chain)

| Field | Value |
|------|------|
| `today_expiry` | 2026-05-22 (3 DTE) |
| `today_total_gex` | +$11,929,283,687 |
| `today_zero_gamma` | **$134.43** |
| `atm_flip_strike` | 105 (far below — not meaningful) |
| `regime` | POSITIVE |

Key support walls inside the May 22 chain:

| Strike | GEX | Role |
|------:|----:|------|
| 140 | +$7,576,482,333 | dominant ceiling wall |
| 136 | +$1,135,139,555 | near-spot wall |
| 135 | +$953,542,776 | near-spot wall |
| 137 | +$699,128,512 | near-spot wall |
| 138 | +$458,913,936 | near-spot wall |

May 22 GEX alone explains 72% of the total dealer long-gamma — i.e. the
positive-gamma regime largely **dissolves after Friday's OPEX**. Phase 9 must
treat the long-gamma protective bid as a **time-bound regime that resets next
week**. The today_zero_gamma at $134.43 is lower than the overall ZGL at
$135.66 — within the May 22 chain alone, BABA has a small additional cushion
toward $134.43 before regime-flips. [STRUCT:today_gamma_flip]

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `options_structure_gex` | symbol=BABA, dte_max=45 | Total GEX +$16.5B, ZGL $135.66, $140 wall +$8.5B, $130 trapdoor −$985M |
| `options_structure_dex` | symbol=BABA, dte_max=45 | net_dex +$134.7B → dealer mechanical bid |
| `options_structure_vanna_charm` | symbol=BABA, dte_max=45 | net_vanna −956K, net_charm +191.7M → post-OPEX selling pressure |
| `options_structure_iv_term_structure` | symbol=BABA | BACKWARDATION, May22 67.5% → Jun18 43.7%, no kink |
| `options_structure_term_skew` | symbol=BABA, dte_target=30 | COMPLACENT, calls > puts by 2.8 vol pts |
| `options_structure_front_end_iv_ratio` | symbol=BABA, near=7, far=30 | ratio 1.145, BACKWARDATION |
| `options_structure_today_gamma_flip` | symbol=BABA | May 22 ZGL $134.43, $140 wall +$7.58B intra-chain |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** **range-bound long-gamma into Friday OPEX; mild
  mechanical bid from dealer DEX hedge; structural sticky resistance at $140
  and trapdoor risk through $130.**
- **Conviction:** **4 / 5** — GEX, DEX, vanna/charm, term structure, and
  skew all corroborate the same structural picture; rare to get this
  alignment.
- **Three structural levels for phase-9:**
  1. **ZGL $135.66 / today_ZGL $134.43** — the line. Above = long gamma
     (dealers sell rallies, vol suppressed); below = short gamma (trend
     amplifies). A daily close below $134.43 = regime flip and primary
     stop-loss trigger.
  2. **$140 wall (+$8.5B GEX)** — sticky resistance. Upside thesis works
     *through* this with a catalyst; without catalyst, expect rejection
     and dealer mean-reversion sell flow.
  3. **$130 trapdoor (−$985M GEX)** — downside acceleration risk. A break
     of $130 mechanically opens $125 ($121M neg) and $120 ($249M neg)
     amplifier zones.
- **Open questions:**
  - Did BABA report earnings on/around May 15, and is the May 22 IV
    backwardation a post-earnings residual? (→ phase 6 catalyst calendar
    + phase 5 historical IV).
  - How does BABA's current 30-DTE IV (43.7%) compare to its 1Y range?
    Is the skew complacency cheap (room to spike) or expensive
    (mean-revert)? (→ phase 5 historical IV percentile / Z-score).
  - Does the vanna-implied post-OPEX selling drift conflict with the
    LEAP risk-reversal long thesis? (resolved in phase 9 — different
    horizons; near-term drift can co-exist with long-term thesis if
    sized correctly).
