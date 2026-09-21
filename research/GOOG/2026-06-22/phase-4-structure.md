# Phase 4 — Dealer Structure & Gamma

**Ticker:** GOOG
**As-of date:** 2026-06-22
**Generated:** 2026-06-22
**Upstream phases cited:** phase-2-dark-pool.md (DP supply $362–371), phase-3-positioning.md (7/17 call-heavy cliff, $340/$330 put walls)

## Summary

GOOG sits in a **net short-gamma regime**: `regime = FULLY_NEGATIVE`, `total_gex =
−3,838,225`, `zero_gamma_level = null` (no flip anywhere in the 45-DTE window) — "strong
gamma amplification" in the tool's words. That means dealers **buy rallies and sell
dips → trend amplification, expanded realized vol** (the opposite of a pinned,
mean-reverting tape). The per-strike texture sharpens it: negative GEX is **clustered at
and below spot ($340 −5.79M, $335 −3.95M, $350 −3.69M)** — the amplification zone — while
positive GEX **caps above ($385 +3.38M, $375 +2.64M, $370 +2.53M)**. So a break of
**$340 accelerates down**, and a push up runs into a **long-gamma cap at $370–385**.
Meanwhile **max-pain pulls UP**: 6/26 $365 (+4.66%), 7/10 $365, 7/17 $360 (+3.23%) — the
OI-pin gravity is *above* the $348.31 spot, reinforcing phase-3's call-heavy 7/17 cliff
and phase-2's $362–371 DP supply. Skew is **COMPLACENT** (25Δ calls richer than puts,
ratio 0.982) and the IV term is **FLAT** — low downside-hedging demand, no event stress
in the curve (earnings 7/22 is beyond this window). Net: a **coiled, momentum-amplifying
setup with an upward OI/max-pain bias but genuine downside-acceleration risk below $340**.
Conviction 3.

## Key signals

- **Short gamma — `FULLY_NEGATIVE`, total_gex −3.84M, ZGL null** → vol-amplifying,
  trend-prone (not range-bound) `[STRUCT:gex]`
- GEX texture: **−GEX clustered $335–350** (amplification), **+GEX caps $370–385** →
  $340 = downside-accel level, $370–385 = upside cap `[STRUCT:gex]`
- **Max-pain ABOVE spot** — 6/26 $365, 7/2 $370, 7/17 $360 — upward OI-pin gravity,
  agrees with phase-3 7/17 cliff `[STRUCT:max_pain]`
- **DEX −706M: public net put-long → dealer hedge = SELL underlying** (mild supply,
  amplifies a down move) `[STRUCT:dex]`
- **Skew COMPLACENT (0.982, calls > puts)** + **IV term FLAT**; front-end IV ratio 1.17
  (mild near-term vol, not earnings) — low fear / contrarian complacency flag
  `[STRUCT:term_skew]` `[STRUCT:iv_term_structure]` `[STRUCT:front_end_iv_ratio]`

## Detailed findings

### GEX — gamma exposure `[STRUCT:gex]`

- `regime` = **FULLY_NEGATIVE**; `regime_description` = "All strikes have negative net
  GEX — strong gamma amplification"; `total_gex` = **−3,838,225**; `zero_gamma_level` =
  **null**; `underlying_price` = 348.31.
- **Per-strike cross-check** (the regime is net-negative, but the texture is
  directional):

| Strongest +GEX (long-γ cap) | Strongest −GEX (short-γ accel) |
|---|---|
| 385 → +3,375,567 | **340 → −5,792,148** |
| 375 → +2,639,699 | 335 → −3,951,131 |
| 370 → +2,532,693 | **350 → −3,692,773** |
| 400 → +2,275,144 | 345 → −2,455,711 |

Negative gamma sits **where price is now ($340–350)** → moves here amplify; positive
gamma **above ($370–400)** → that band would dampen/cap a rally. The **$340 strike
(most negative GEX) coincides with phase-3's put wall** — a break there is the
short-gamma downside-acceleration trigger.

### DEX — net dealer delta `[STRUCT:dex]`

`net_dex = −705,983,701`; spot 348.31. Tool interpretation (quoted): *"Public is net
put-long → dealers net short puts → dealer hedge is to SELL underlying."* Within ≤45
DTE the delta-weighted book is put-heavy (even though raw OI is call-heavy — the LEAP
upside calls sit outside this window). The dealer-hedge bias is a **mild standing
sell**, which in the short-gamma regime amplifies downside and means rallies must
overcome dealer supply.

### Vanna / charm `[STRUCT:vanna_charm]`

`net_vanna = +4,248`, `net_charm = +78,028`; **no squeeze_signal flagged**. Modest
positive vanna/charm — no mechanical vanna-squeeze setup (would need positive vanna +
negative dealer delta + falling IV; IV is flat, not falling). De-rate any squeeze
narrative.

### IV term structure & skew `[STRUCT:iv_term_structure]` `[STRUCT:term_skew]` `[STRUCT:front_end_iv_ratio]`

- IV term `structure` = **FLAT** — no backwardation/contango; no curve-level event
  stress (earnings 7/22 sits beyond the near window).
- Term skew `interpretation` = **COMPLACENT**; `skew_ratio` 0.982; put_25Δ_iv 0.3441 vs
  call_25Δ_iv 0.3505 → **calls slightly richer than puts**. Low tail-hedging demand;
  market leans to pricing upside. A **mildly bullish positioning tell but a contrarian
  complacency flag** (no fear bid for puts).
- Front-end IV ratio **1.17** (near 7-DTE 41.7% vs far 30-DTE 35.65%) — mild near-term
  vol elevation (likely the recent pullback's realized vol), **not** an earnings/event
  spike (would be sharper, and earnings is 30 days out).

### Max pain — opex gravity `[STRUCT:max_pain]`

| Expiry | DTE | max-pain | dist% from $348.31 | P/C OI |
|--------|-----|----------|--------------------|--------|
| 2026-06-26 | 4 | **365** | **+4.66** | 0.492 |
| 2026-07-02 | 10 | 370 | +6.09 | 0.768 |
| 2026-07-10 | 18 | 365 | +4.66 | 0.958 |
| **2026-07-17** | 25 | **360** | **+3.23** | 0.559 |

**All near-expiry max-pain strikes are ABOVE spot** — the OI pin pulls **up toward
$360–365**, dead-on with phase-3's call-heavy 7/17 cliff and phase-2's $362–371 DP
supply. (Caveat per tool: static-OI estimate; the nearer 6/26 magnet is firmer, the
7/17 softer as OI builds.) This upward gravity + the short-gamma regime = if a catalyst
lifts GOOG, the move can run toward $360–370 before the +GEX cap; absent a catalyst,
$348–350 is a low-conviction battleground.

### Today's gamma flip

**Skipped** — `today-gamma-flip` is 0DTE/intraday-only and this is an end-of-day as-of
run (2026-06-22 EOD). Not meaningful after the session close.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← path | Rows |
|------------------|--------------------|------|
| `uw options-structure gex --symbol GOOG --dte-max 45 --date 2026-06-22 --json` | regime=FULLY_NEGATIVE, total_gex −3.84M, ZGL null ← `.regime`/`.total_gex` | per-strike |
| `uw options-structure dex --symbol GOOG --dte-max 45 --date 2026-06-22 --json` | net_dex −705,983,701; "dealer hedge = SELL" ← `.net_dex`/`.interpretation` | 1 |
| `uw options-structure vanna-charm --symbol GOOG --dte-max 45 --date 2026-06-22 --json` | vanna +4,248, charm +78,028, no squeeze ← `.net_vanna` | 1 |
| `uw options-structure iv-term-structure --symbol GOOG --date 2026-06-22 --json` | structure=FLAT ← `.structure` | 1 |
| `uw options-structure term-skew --symbol GOOG --dte-target 30 --date 2026-06-22 --json` | COMPLACENT, skew_ratio 0.982 ← `.interpretation` | 1 |
| `uw options-structure front-end-iv-ratio --symbol GOOG --near-dte 7 --far-dte 30 --date 2026-06-22 --json` | ratio 1.17 (near 0.417/far 0.357) ← `.ratio` | 1 |
| `uw options-structure max-pain --symbol GOOG --dte-max 30 --date 2026-06-22 --json` | 6/26 pain 365 (+4.66%), 7/17 pain 360 ← `.results[].max_pain` | 4 exp |

## Tool errors

None. All seven reads round-tripped through `jq`. `today-gamma-flip` not called
(intraday-only; EOD run).

## DATA NOTE / CORRECTION

No mis-read. Note: `iv-term-structure` returned its label `structure="FLAT"` but the
`term_structure[]` per-DTE rows came back with null `dte`/`iv` — per phase-4 guidance I
quote the tool's `structure` label and did **not** re-derive the curve by hand.

## Verdict for downstream phases

- **Dealer regime:** **SHORT GAMMA (net), trend-amplifying.** `FULLY_NEGATIVE`,
  total_gex −3.84M, no ZGL in 45 DTE. Vol expands, moves trend rather than pin. DEX adds
  a mild dealer sell-bias.
- **Conviction:** **3 / 5.** The regime read is high-confidence (clean labels), but its
  directional implication is **two-sided**: max-pain + call OI bias *up* to $360–365,
  yet short gamma + the $340 −GEX/put wall means a downside break *accelerates*. The
  COMPLACENT skew is a contrarian caution on the bullish lean.
- **Three structural levels for phase-9:**
  1. **No clean ZGL (null)** — net short-gamma throughout 45 DTE. The functional
     gamma transition (per-strike GEX flips − → +) is **~$360–365**, just under the
     +GEX cap.
  2. **Upside cap $385** (largest +GEX +3.38M; band $370–385) / **downside-accel $340**
     (largest −GEX −5.79M; = phase-3 put wall) — the two amplification boundaries.
  3. **Near-expiry max-pain $365 (6/26) → $360 (7/17)** — the opex pin magnet, **above
     spot**, the upward gravity for the next month.
- **Open questions:** Does the short-gamma regime + upward max-pain need a *catalyst*
  to trigger the squeeze toward $360–370, or is the call-OI build itself the fuel
  (phase-6 macro / phase-7 insights)? Is the COMPLACENT skew a green light (no put
  demand to fight a rally) or a red flag (unhedged downside in a short-gamma tape that
  amplifies a break of $340)? Phase-8 debate should take both sides.
