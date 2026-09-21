# Phase 4 — Dealer Structure & Gamma

**Ticker:** GRAB
**As-of date:** 2026-05-21
**Generated:** 2026-05-21T20:45:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md

## Summary

Dealer regime is **POSITIVE / LONG-GAMMA** with a zero-gamma level at $2.63
(26% below spot of $3.55) [STRUCT:gex]. Total long-DTE GEX = **$1.054B**;
the $4 strike alone carries **$245M GEX** (the dominant magnet), with
secondary walls at $5 ($241M), $7.50 ($234M), and $10 ($193M) [STRUCT:gex].
This dovetails exactly with the phase-3 covered-call OI walls — the same
contracts are creating the long-gamma regime. Net DEX is +$184M (call_dex
$272M, put_dex -$89M) → dealers are net short calls and their hedge is to
BUY underlying [STRUCT:dex]. 25-delta 30DTE skew is **COMPLACENT**
(call_iv 51.1% vs put_iv 43.2%, skew -0.079) — i.e. calls are richer than
puts at the wings, a bullish-skew configuration rare for a sub-$5 single
name [STRUCT:term_skew]. The IV term curve is in **BACKWARDATION** with a
front/back ratio of **5.245** — the 8-DTE bucket (2026-05-29) prices
~381% avg IV (noise-amplified, but the genuine 28→36 DTE step from 73% to
91% suggests a real event around late June) [STRUCT:iv_term_structure],
[STRUCT:front_end_iv_ratio]. Phase-6 must confirm the calendar; possible
earnings or analyst day in the May 29 → June 26 window.

## Key signals

- **GEX regime: POSITIVE / LONG-GAMMA**, ZGL = $2.63 (26% below spot)
  [STRUCT:gex] — dealers sell rallies, buy dips → mean-reversion regime.
- **Largest gamma magnet: $4 strike, $245M GEX** (45DTE only it's $241M
  too — pulling in near-term too) — this is the most important level for
  the next 30–60 days [STRUCT:gex].
- **Net DEX +$184M, dealer hedge = BUY underlying** [STRUCT:dex] —
  structural bid baked into the tape.
- **Term skew COMPLACENT** (calls > puts in 25Δ at 30DTE) [STRUCT:term_skew]
  — bullish skew, no tail-hedging demand.
- **Front-end IV ratio 5.245 (BACKWARDATION)** [STRUCT:front_end_iv_ratio] —
  signals event stress in next 1–2 weeks; phase-6 must identify the
  catalyst (likely Q1 earnings circa May 29 or analyst day pre-June OPEX).

## Detailed findings

### GEX — 45 DTE near-term view

| Strike | Net GEX ($) | Notes |
|--------|-------------|-------|
| 0.5 | 926,049 | retail leftovers |
| 1.0 | 79,189 | |
| 1.5 | 202,303 | |
| 2.0 | 4,520 | |
| 2.5 | 13,419 | |
| 3.0 | 447,042 | |
| 3.5 | **50,254,400** | wall #2 (near spot) |
| **4.0** | **241,772,383** | **dominant gamma magnet** |
| 4.5 | 2,342,404 | |
| 5.0 | 2,317,590 | |
| 5.5 | -1,634 | tiny negative |
| 6.0 | 30,431 | |

Total 45DTE GEX = **$298,388,620** (FULLY_POSITIVE — all but a trivial
strike are net long-gamma). ZGL = null (no flip exists inside 45DTE).

### GEX — 365 DTE (LEAP-inclusive structural view)

| Strike | Net GEX ($) | Notes |
|--------|-------------|-------|
| 3.0 | **-6,508,153** | only negative-gamma strike (put-heavy) |
| 3.5 | 58,114,646 | |
| **4.0** | **245,418,226** | dominant LEAP magnet |
| 4.5 | 33,753,138 | |
| **5.0** | **241,396,880** | secondary mega-wall |
| 5.5 | 45,528,236 | |
| 6.0 | 6,674,727 | |
| 7.0 | 343,031 | |
| **7.5** | **234,299,616** | tertiary wall |
| **10.0** | **192,541,045** | far OTM wall |
| 12.0 | 479,285 | |

Total 365DTE GEX = **$1,053,800,004** — POSITIVE regime, ZGL = **$2.63**.
At spot $3.55, the dealer book is comfortably in long-gamma territory with
a 26% buffer before regime flip.

**Cross-reference with phase-3 OI walls:** the strikes carrying the most
LEAP GEX ($4, $5, $7.50, $10) are exactly the strikes with the largest
existing covered-call OI (phase-3 table). The structural signature is one
big institutional overlay program, not retail.

### DEX — net dealer delta

| Field | Value |
|-------|-------|
| call_dex | +$272,498,988 |
| put_dex | -$88,879,513 |
| **net_dex** | **+$183,619,475** |
| Interpretation | Public net call-long → dealers net short calls → hedge = BUY underlying |

The dealer-bid bias is consistent with the dark-pool block buyer in phase-2
(if the same institution is short the calls AND long the stock = textbook
covered-call program).

### Vanna + charm

| Field | Value | Read |
|-------|-------|------|
| call_vanna | -53,402 | |
| put_vanna | +21,149 | |
| net_vanna | -32,253 (slightly negative) | mild bearish if IV falls |
| net_charm | +5,093,119 | large positive — supports long-stock hedge into expiry |

Karsan-style vanna squeeze setup requires positive vanna + negative dealer
delta + falling IV. Here vanna is mildly negative, so a classical vanna
squeeze is NOT in play. However, charm is decidedly positive and large,
which means dealer long-stock hedges accrete as DTE drops → mild upside
support from charm decay across the next 30 days.

### IV term structure

| Expiry | DTE | Contracts | Avg IV |
|--------|-----|-----------|--------|
| 2026-05-22 | 1 | 523 | 777% (0DTE-class, noise) |
| 2026-05-29 | 8 | 302 | 382% (likely noise from low-extrinsic strikes) |
| 2026-06-05 | 15 | 61 | 121% |
| 2026-06-12 | 22 | 52 | 91% |
| 2026-06-18 | 28 | 191 | 73% |
| **2026-06-26** | **36** | 45 | **91%** ← kink upward; event candidate |
| 2026-07-02 | 42 | 7 | 63% |
| 2026-07-17 | 57 | 153 | 64% |
| 2026-10-16 | 148 | 132 | 59% |
| 2027-01-15 | 239 | 199 | 60% |
| 2027-06-17 | 392 | 64 | 60% |
| 2027-12-17 | 575 | 36 | 60% |
| 2028-01-21 | 610 | 116 | 62% |
| 2028-12-15 | 939 | 63 | 63% |

Structure: **BACKWARDATION** confirmed. The clean signal (ignoring 1/8 DTE
noise) is the **2026-06-26 vs 2026-06-18 kink up from 73% → 91% IV** —
characteristic of a binary catalyst on or before 2026-06-26 (most likely Q1
2026 earnings, since Grab reports late May / early June typically). Phase-6
must verify.

LEAP IV floor sits at **~60%** — a structurally elevated but stable backend
for an EM consumer-tech name.

### Term skew (25Δ, 30 DTE)

| Metric | Value |
|--------|-------|
| call_25d_iv | 0.511 (51.1%) |
| put_25d_iv | 0.432 (43.2%) |
| skew | -0.079 |
| skew_ratio | 0.845 |
| **interpretation** | **COMPLACENT** |

Calls richer than puts → bullish skew → market not paying for downside
protection at 30DTE. This is INCONSISTENT with the phase-1 "5/5 bearish
sweep persistence" read and CONSISTENT with the phase-2 / phase-3 hedged-
long / covered-call regime. The complacent skew is the structural fingerprint
of net-long bias being expressed via calls.

### Front-end IV ratio

| Metric | Value |
|--------|-------|
| near_dte (8) IV | 3.817 (artifactually high; many low-extrinsic strikes) |
| far_dte (28) IV | 0.728 |
| ratio | 5.245 |
| **regime** | **BACKWARDATION** |

Even discounting the 8DTE inflation, the regime label is correct: there is
event stress priced into the next 2 weeks. The most plausible catalyst is
the kink-up at 2026-06-26 in the term curve.

### Today's gamma flip (2026-05-22 0DTE, intraday view)

| Field | Value |
|-------|-------|
| atm_flip_strike | $4.50 |
| spot | $3.49 (close-of-day pre 0DTE) |
| today_total_gex | $57.76M |
| today_zero_gamma | null (regime fully positive) |
| regime | POSITIVE |

Key walls (intraday support):
- $3.50: $39.6M GEX support wall
- $4.00: $16.7M GEX support wall
- $4.50: $0.74M GEX support wall

**Reading:** for tomorrow's 0DTE session, $3.50 is the gravity floor and
$4.00 is the magnet ceiling. Dealers will buy dips below $3.50 and sell
rallies toward $4.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__options_structure_gex` | symbol=GRAB, dte_max=45 | FULLY_POSITIVE; $4 = $241.8M GEX; ZGL null |
| `mcp__uw-pp__options_structure_gex` | symbol=GRAB, dte_max=365 | POSITIVE; $4 = $245.4M; ZGL = $2.63 |
| `mcp__uw-pp__options_structure_dex` | symbol=GRAB, dte_max=45 | net_dex +$184M, dealer hedge buys underlying |
| `mcp__uw-pp__options_structure_vanna_charm` | symbol=GRAB, dte_max=45 | vanna -32K (mild bear if IV drops), charm +5.1M (large +) |
| `mcp__uw-pp__options_structure_iv_term_structure` | symbol=GRAB | BACKWARDATION; clean kink at 2026-06-26 |
| `mcp__uw-pp__options_structure_term_skew` | symbol=GRAB, dte_target=30 | COMPLACENT, skew -0.079, ratio 0.845 |
| `mcp__uw-pp__options_structure_front_end_iv_ratio` | symbol=GRAB, near=7 far=30 | ratio 5.245, BACKWARDATION |
| `mcp__uw-pp__options_structure_today_gamma_flip` | symbol=GRAB | POSITIVE; ATM flip $4.50; walls $3.50/$4/$4.50 |

## Tool errors

(none)

## Verdict for downstream phases

- **Bias from this phase:** **LONG-GAMMA / MEAN-REVERTING with BULLISH
  SKEW** — dealers buying dips, $4 = dominant magnet, calls richer than
  puts.
- **Conviction:** 4/5 (GEX magnitudes, ZGL position, and DEX sign all
  reinforce each other; only weak vanna footprint dilutes).
- **Three structural levels for phase-9:**
  1. **Gamma magnet $4.00** — $245M LEAP GEX, dominant magnet. Spot should
     drift toward this level absent a catalyst.
  2. **Zero Gamma Level $2.63** — regime-flip floor. Two daily closes below
     $2.63 = regime flip to short-gamma → invalidation of the long-gamma
     trade construction.
  3. **0DTE support shelf $3.50** — phase-9 intraday entry trigger; dealer
     dip-buying mechanically expected on retests.
- **Open questions:**
  - Phase-6 must identify the catalyst implied by the 2026-06-26 IV kink
    (Q1 earnings? analyst day? regulatory?).
  - Phase-5 historical_gex_time_series should confirm regime stability
    (long-gamma for 30d = high-confidence structural read).
  - Phase-7 conviction_matrix label is the tiebreaker between
    DIRECTIONAL_LONG and HEDGED_LONG/COVERED_CALL interpretation.
