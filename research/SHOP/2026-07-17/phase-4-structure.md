# Phase 4 — Dealer Structure & Gamma

**Ticker:** SHOP
**As-of date:** 2026-07-17
**Generated:** 2026-07-19 (run) · as-of 2026-07-17
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md

## Summary

Dealers are **net SHORT gamma** (`regime NEGATIVE`, ZGL **134.98** vs spot
**123.52**) — spot sits ~9% below the flip, so the **entire tradeable range is
trend-amplifying** (dealers sell dips / buy rallies). The destabilizing strike is
**123 with −$12.8M GEX** (right at spot): a break below 123 accelerates downside,
while positive gamma at **125–135 caps rallies**. This is reinforced by **near-term
max pain sitting below spot** (7/17 → 117, 7/24 → 121, 7/31 → 120) — an opex pull
toward the 117–121 zone that phases 1–3 already flagged. **Counterweights:** term
skew is **NORMAL** (25Δ put/call 1.034 — no fear/tail-hedging) and static **DEX is
a dealer buy** (+$187.7M, dealers short calls → hedge is to buy underlying). Net: the
cleanest near-term **downside** confluence in the run so far (short-γ + max-pain-below
+ flow lean), but tempered — this is a **grind/drift risk, not a crash setup**.

## Key signals

- **Short-gamma regime**, ZGL 134.98, spot 123.52 → trend amplification below 135. `[STRUCT:gex]`
- **123 = −$12.8M GEX** (largest, at spot) = the accelerant pivot; 125 = +$4.87M
  (dealers sell rallies). `[STRUCT:gex]`
- **Near-term max pain below spot:** 7/17 → 117 (−5.3%), 7/24 → 121 (−2.0%, P/C OI
  1.17), 7/31 → 120 (−2.9%). `[STRUCT:max_pain]`
- **IV term structure BACKWARDATION** (event stress into Aug-5 earnings) but **mild**
  (front/far ratio 1.026). `[STRUCT:iv_term_structure]`
- **Skew NORMAL (1.034)** — puts barely richer than calls; put flow is measured
  hedging, **not panic**. `[STRUCT:term_skew]`

## Detailed findings

### GEX `[STRUCT:gex]`

- **Regime: NEGATIVE** — "Dealers net short gamma — expect trend acceleration and
  increased volatility." `zero_gamma_level = 134.98`, `underlying_price = 123.52`,
  `total_gex = 2,256,674`.
- Per-strike net_gex (top by magnitude): **123 → −12,771,622** (dominant, at spot),
  125 → +4,866,717, 128 → +2,046,949, 126 → +1,805,004, 135 → +1,624,928, 130 →
  +1,396,487. **Negative pocket at/below spot, positive shelf 125–135.** A move
  below 123 is amplified; rallies into 125–135 are damped by dealer selling.

### DEX `[STRUCT:dex]`

`net_dex = +187,668,083` — "Public is net call-long → dealers net short calls →
dealer hedge is to BUY underlying." A **static supportive bid**, but note: in a
short-gamma regime the *dynamic* gamma hedge (sell weakness) dominates on a
directional break, so this cushions drift, not a breakdown.

### Vanna + charm `[STRUCT:vanna_charm]`

net_vanna −522, net_charm +8,233 — small magnitudes, **no squeeze signal**. Neutral.

### IV term structure `[STRUCT:iv_term_structure]`

`structure = BACKWARDATION` — front-month IV > back = event stress (Aug-5 earnings,
~19 days out) and iv_rank 85.6 elevated. But **front-end-iv-ratio = 1.026** (near-7
/ far-30) → the backwardation is **mild**, not a violent event kink.

### Term skew `[STRUCT:term_skew]`

`interpretation = NORMAL`, `skew_ratio = 1.034` (25Δ put IV ≈ call IV). **No
tail-hedging steepening** despite the phase-1 put-buying → confirms the puts are
measured protection/positioning, not risk-off panic. This is the main brake on the
bearish thesis.

### Front-end IV ratio `[STRUCT:front_end_iv_ratio]`

`ratio = 1.026` — front barely over back; no acute event stress beyond normal
pre-earnings drift.

### Today's gamma flip

Not run as a live intraday read (as-of is a historical date, after-hours) — the
`gex` ZGL 134.98 is the standing flip level. Skipped per phase guidance.

### Max pain (opex-gravity magnet) `[STRUCT:max_pain]`

| Expiry | Max-pain strike | dist% | P/C OI |
|---|---|---|---|
| 2026-07-17 (today) | **117** | −5.3% | 0.64 |
| 2026-07-24 (next wk) | **121** | −2.0% | 1.17 |
| 2026-07-31 | **120** | −2.9% | 0.80 |
| 2026-08-07 | 127 | +2.8% | 1.87 |
| 2026-08-14 | 127 | +2.8% | 3.23 |

**Near-term gravity is below spot (117–121)**, flipping above (127) only from Aug-7.
Agrees tightly with phase-3 (put wall 117, 7/24 max-pain 121 = the $121-put strike
phase-1 saw bought). Caveat: static-OI estimate; near strikes are the firm magnets.

## Tool calls (audit trail)

| Command | Key value ← `jq` path | Rows |
|---|---|---|
| `uw options-structure gex --symbol SHOP --dte-max 45` | regime NEGATIVE, ZGL 134.98 ← `.regime,.zero_gamma_level`; 123 −12.77M ← `.per_strike[].net_gex` | 45d |
| `uw options-structure dex --symbol SHOP --dte-max 45` | +187.7M, dealer buy ← `.net_dex,.interpretation` | 45d |
| `uw options-structure max-pain --symbol SHOP --dte-max 30` | 7/24 → 121 ← `.results[].max_pain_strike` | 5 exp |
| `uw options-structure iv-term-structure --symbol SHOP` | BACKWARDATION ← `.structure` | — |
| `uw options-structure term-skew --symbol SHOP --dte-target 30` | NORMAL 1.034 ← `.interpretation,.skew_ratio` | — |
| `uw options-structure front-end-iv-ratio --symbol SHOP --near-dte 7 --far-dte 30` | 1.026 ← `.ratio` | — |
| `uw options-structure vanna-charm --symbol SHOP --dte-max 45` | vanna −522 / charm +8,233 ← `.net_vanna,.net_charm` | 45d |

## Tool errors

<none — all seven structure commands returned valid JSON>

## DATA NOTE / CORRECTION

First `jq` on GEX per-strike used field `gex` (null); correct field is `net_gex`
(`.per_strike[].net_gex`) — re-read; 123 = −$12.77M confirmed. Phase-0.5 flagged the
0.49% `implied_move_perc` as suspect — **resolved**: with backwardation + iv_rank
85.6 the realized-vol regime is elevated; treat the deep-dive `implied_move_perc`
field as unreliable and use the term-structure/skew reads instead for expected move.

## Verdict for downstream phases

- **Dealer regime:** SHORT GAMMA (trend-amplifying below ZGL 134.98). Directionally
  this favours **downside continuation** given max-pain-below + flow lean, but skew
  NORMAL + DEX-buy make it a **drift/grind, not a crash**.
- **Conviction:** 3/5 (cleanest directional confluence so far; braked by normal skew).
- **Three structural levels for phase-9 (+ max-pain magnet):**
  1. **ZGL 134.98** — regime flip; above it dealers mean-revert (hard ceiling of the
     amplification zone). Coincides with the 135 call wall.
  2. **123 (−$12.8M GEX)** — the accelerant pivot; below 123 short-γ hedging speeds
     the move toward 121→117.
  3. **125 (+$4.87M GEX)** — dealer-sell-the-rally resistance (agrees w/ phase-2/3
     125 call wall).
  4. **Max-pain magnet: 117 (this week) → 121 (7/24)** — the opex pull for phase-9's
     downside target.
- **Open questions:** Does the historical base-rate (phase-5) confirm that
  short-gamma + max-pain-below + mild-distribution setups on SHOP resolve downward?
  Does macro/sector (phase-6) support or fight a SHOP fade while Tech leads?
