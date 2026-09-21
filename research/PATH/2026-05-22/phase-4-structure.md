# Phase 4 — Dealer Structure & Gamma

**Ticker:** PATH (UiPath Inc.)
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T00:00:00Z
**Upstream phases cited:** phase-2-dark-pool.md, phase-3-positioning.md, phase-0.5-context.md

## Summary

Dealers are **net LONG gamma** (total_gex **+$29.5M**, spot $10.91 far above ZGL **$7.26**),
with a dominant **+$20.5M gamma wall at $11** that pins/mean-reverts spot into the 05-28
event and suppresses realized vol *pre-print*. **DEX is positive** (public net call-long →
dealers short calls → hedge = BUY underlying), supplying a mechanical bid that **partly
explains the phase-2 dark-pool buying** (i.e. not all DP accumulation is conviction; some
is dealer delta-hedging). The asymmetry that matters for an event trade: **strikes
$8.5–$10.5 are all NEGATIVE GEX** — a break below ~$10.5 flips dealers short-gamma and turns
the downside into a vol-expanding air pocket toward the $8.5–$9 put wall, while the upside
is pinned/capped at $11–$13. Term structure carries the **5/29 earnings vol bubble (140%
IV, front-end ratio 1.33 backwardation)**, and 30-DTE skew is **call-skewed / COMPLACENT**
(upside-tilted, low downside fear) — coherent with the phase-3 buy-write/collar read.

## Key signals

- **Long-gamma regime:** total_gex +$29,452,339 POSITIVE; ZGL **$7.26** vs spot $10.91 [STRUCT:gex]
- **$11 gamma wall +$20.5M** dominates the chain (next: $11.5 +$4.69M, $12 +$3.55M, $13 +$2.03M) — pin/resistance [STRUCT:gex]
- **Negative-GEX pocket $8.5–$10.5:** $9 −$1.17M, $10.5 −$1.07M, $9.5 −$0.75M, $8.5 −$0.73M, $10 −$0.59M → downside air pocket below $10.5 [STRUCT:gex]
- **DEX +$28.2M** (call_dex +$47.4M / put_dex −$19.2M): dealers BUY underlying to hedge → mechanical bid [STRUCT:dex]
- **Earnings vol bubble:** 5/29 expiry IV **140.2%** vs 6/18 100.7% vs LEAPs ~81%; front-end ratio **1.326 BACKWARDATION** [STRUCT:iv_term_structure / front_end_iv_ratio]
- **Skew COMPLACENT:** 25Δ call IV 93.3% > put IV 86.2% (skew −0.071, ratio 0.924) — calls richer than puts, low downside fear [STRUCT:term_skew]

## Detailed findings

### GEX (per-strike, ZGL)

`regime = POSITIVE` — "dealers net long gamma → mean-reversion and reduced volatility."
ZGL **$7.26** sits ~33% below spot, so PATH is deep in long-gamma territory pre-earnings.

| Strike | net_gex | Role |
|--------|---------|------|
| **$11** | **+20,511,306** | Dominant gamma wall — pin/magnet & resistance |
| $11.5 | +4,688,650 | Positive shelf (upside cap) |
| $12 | +3,547,863 | Upside cap (= phase-3 call-write strike) |
| $13 | +2,025,778 | Upside cap |
| $15 | +1,209,509 | Far cap (= 2027 LEAP OI 33,865, phase-3) |
| $10.5 | −1,073,683 | **Neg-GEX pocket top** |
| $9 | −1,171,356 | Deepest negative GEX |
| $9.5 | −748,550 | Negative |
| $8.5 | −730,363 | Negative (= put-write wall, phase-3) |
| $10 | −593,490 | Negative (= put wall / DP-support edge) |

Caveat (tool note): GEX is coarse on small-caps; treat ZGL as a **±2% band ($7.1–$7.4)**
and the $11 wall as the high-confidence structural feature. **Interpretation:** above
$10.5, dealers dampen moves and lean spot toward the $11 wall; **below $10.5, dealers flip
short-gamma and amplify the move** — the downside is structurally more dangerous than the
upside into a binary event.

### DEX (dealer hedge direction)

net_dex **+$28.2M** (call_dex +$47.4M, put_dex −$19.2M). Public is net call-long → dealers
are net short calls → their hedge is to **buy** underlying. This is a standing mechanical
bid that **overlaps the phase-2 DP accumulation** — an important caveat to phase-2's
"institutional conviction" read: a chunk of the off-exchange buying is plausibly dealer
delta-hedging of the call-heavy retail/public book, not a thesis. (Flag for phase-10.)

### Vanna + charm (post-event mechanics)

net_vanna **−1,026** (call-heavy book), net_charm **+99,543**. No squeeze setup. The
forward read is a **post-earnings headwind**: once the 05-28 print collapses IV, falling IV
→ call deltas drop → dealers (short calls) **cut their long-underlying hedge → mechanical
SELLING**, reinforced by charm decay into the 5/29 expiry. So the mechanical DEX bid that
supports spot now **reverses into selling after the IV crush**. The dealer support is
*conditional on high IV* and evaporates post-print.

### IV term structure + front-end ratio

15 expiries. The tool labels the overall shape `CONTANGO` (artifact of including the
near-dead 5/22 0DTE expiry at 43.7%), but the **economically meaningful shape is an
earnings KINK/backwardation at 5/29**: 5/22 43.7% → **5/29 140.2%** → 6/05 119.6% → 6/18
100.7% → LEAPs ~81%. `front_end_iv_ratio` (10DTE vs 31DTE) = **1.326 = BACKWARDATION** =
classic single-name event stress. **The 5/29 140% IV is the bubble that crushes after
05-28** — this is the single most reliable post-event expectation (IV mean-reverts toward
the ~85–100% back-month level).

### Term skew (30 DTE)

`interpretation = COMPLACENT`: call_25Δ_iv **93.3%** > put_25Δ_iv **86.2%** (skew −0.071).
**Calls are richer than puts** — unusual, and the opposite of tail-hedging. On a
beaten-down small-cap into earnings this is a **speculative-upside / recovery / squeeze**
tell, consistent with the positive DEX (call-long public) and the phase-2 accumulation.
It directly contrasts the short-term bearish sweeps (phase-1) — the 1-month structural
positioning leans **upside**, the short-dated flow leans defensive.

### Today's gamma flip (0DTE)

**Skipped** — `today_gamma_flip` is an intraday 0DTE map; the as-of is an EOD/after-hours
historical snapshot, so the 5/22 0DTE flip level is stale and non-actionable per phase
guidance. The 45-DTE GEX above is the actionable structural read.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__options_structure_gex` | `{symbol: PATH, dte_max: 45}` | +$29.5M POSITIVE, ZGL $7.26, $11 wall +$20.5M, neg pocket $8.5–$10.5 |
| `mcp__uw-pp__options_structure_dex` | `{symbol: PATH, dte_max: 45}` | net_dex +$28.2M, dealers BUY underlying (bid) |
| `mcp__uw-pp__options_structure_vanna_charm` | `{symbol: PATH, dte_max: 45}` | vanna −1,026, charm +99,543 → post-IV-crush selling |
| `mcp__uw-pp__options_structure_iv_term_structure` | `{symbol: PATH}` | 5/29 140% earnings bubble; labeled CONTANGO (0DTE artifact) |
| `mcp__uw-pp__options_structure_term_skew` | `{symbol: PATH, dte_target: 30}` | COMPLACENT, call-skewed (call 93.3% > put 86.2%) |
| `mcp__uw-pp__options_structure_front_end_iv_ratio` | `{symbol: PATH, near_dte: 7, far_dte: 30}` | ratio 1.326 BACKWARDATION (event stress) |
| `mcp__uw-pp__options_structure_today_gamma_flip` | — | Skipped (EOD as-of; 0DTE map stale) |

## Tool errors

None.

## Verdict for downstream

- **Dealer regime:** **LONG GAMMA pre-earnings** (mean-reversion, $11 pin) flipping to a
  **post-event selling headwind** (vanna/charm unwind on IV crush). Conditional, not
  static.
- **Conviction:** **4/5** — GEX/DEX/term-structure are clear and mutually consistent; the
  small-cap GEX coarseness and the 0DTE-skip are the only caveats.
- **Three structural levels for phase-9:**
  1. **$11 gamma wall (+$20.5M)** — pin/resistance & mean-reversion anchor into the event;
     spot will lean here pre-print. Aligns with DP $11 ceiling + OI battleground.
  2. **$10.5 = negative-GEX gate** — below it ($8.5–$10.5 all neg GEX), dealers flip
     short-gamma and the move **accelerates** toward the $8.5–$9 put wall. The key
     downside risk line for a bad print.
  3. **$12–$13 positive-GEX cap** — long-gamma dealers sell rallies here; matches phase-3
     call-overwriting cap. Upside is structurally throttled short of $13.
- **Open questions:**
  - How much of phase-2's DP buying is **dealer delta-hedging** (DEX +$28M) vs genuine
    accumulation? Material for the conviction weighting. → phase-7 insights/accumulation.
  - The skew says upside-tilted, the sweeps say bearish — which dominates *through* the
    event? → phase-5 historical earnings-reaction + phase-7b/7c.
  - Does the 140% 5/29 IV imply a move large enough to clear the $11 pin and the $12–13
    cap (or break the $10.5 gate)? → phase-9 expected-move math (implied move ~11.8%).
