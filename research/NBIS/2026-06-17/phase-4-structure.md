# Phase 4 — Dealer Structure & Gamma

**Ticker:** NBIS (Nebius Group NV)
**As-of date:** 2026-06-17
**Generated:** 2026-06-18T00:38:31Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-0.5-context.md

## Summary

Dealer structure is **supportive-but-capping near-term, with a vol-crush trap underneath.** GEX regime
is **POSITIVE (dealers net long gamma)** with ZGL $34.64 far below spot $283.96 — robustly long-gamma,
so dealers sell rallies and buy dips → **mean-reversion and suppressed realized vol** (consistent with
today's intraday fade from $285 to the $280.91 close after a parabolic run). DEX is bullish-mechanical:
**net_dex +$2.88bn, public net call-long → dealers short calls → dealer hedge is to BUY underlying**
(a bid on dips). **The catch is negative vanna**: with **IV rank 91 (absolute IV 110–126%)**, a vol
decline would force dealers to *cut* that long-underlying hedge → mechanical SELLING. So the same rich
IV that underpins the dip-bid is the downside fuse. Max-pain gravity is mildly **downward** (near magnet
**$267.5 for 06-26, −4.7%**, sloping to $250/$235/$220 further out). Term skew is NORMAL (mild put
richness 1.05), front-end FLAT (no event stress; no earnings until 08-06). Net: **range-to-mild-pullback
bias, not continuation** — structure tempers the bullish flow/positioning.

## Key signals

- **POSITIVE gamma regime**, ZGL $34.64 ≪ spot $283.96 → long-gamma, mean-reversion, vol suppression. [STRUCT:gex]
- **DEX +$2.88bn, dealers short calls → buy underlying to hedge** = supportive dip-bid. [STRUCT:dex]
- **Negative net vanna (−1,795)**: falling IV → dealer selling. IV rank 91 ⇒ high vol-crush/downside risk. [STRUCT:vanna_charm]
- **Near max-pain magnet $267.5 (06-26, −4.7%)**; max-pain slopes down across expiries → mild downward OI pull. [STRUCT:max_pain]
- **Term skew NORMAL (put 116.7% / call 110.8%, ratio 1.05); front-end FLAT (0.98)** — no panic, no event cliff. [STRUCT:term_skew / front_end_iv_ratio]

## Detailed findings

### GEX [STRUCT:gex]

| Field | Value |
|-------|-------|
| regime | **POSITIVE** — "Dealers net long gamma — expect mean-reversion and reduced volatility" |
| zero_gamma_level | $34.64 (≪ spot → no realistic flip; solidly long-gamma) |
| total_gex | 9,835,601 |
| underlying_price | $283.96 |
| note (verbatim) | "GEX most meaningful for index products … and large-cap single stocks with deep OI" → treat magnitude as coarse |

Per-strike gamma magnitude concentrates in the **$200–230 put zone** (e.g. $225 net_gex −215,658, $220
−198,709, $230 +202,186) — i.e. below spot, around the heavy put OI. Near spot ($280–300) gamma is
lighter. The regime label (POSITIVE) is the read; per-strike used only to confirm.

### DEX [STRUCT:dex]

net_dex **+$2,879,876,655** (call_dex +$3.41bn, put_dex −$0.53bn). Tool interpretation (verbatim):
"Public is net call-long → dealers net short calls → dealer hedge is to BUY underlying." → mechanical
**dip-bid** supports spot while the call book is live. Bullish-supportive, reinforces phase-3's call-heavy book.

### Vanna + charm [STRUCT:vanna_charm]

net_vanna **−1,795** (call-heavy book), net_charm +206,630. Interpretation (verbatim): "Falling IV →
call delta drops → dealers (short calls) cut long-underlying hedge → SELLING pressure. Rising IV
reverses." **This is the single most important structural risk:** IV rank 91 means IV is far likelier
to fall than rise (post-OPEX crush, or as the parabolic move's realized vol cools) → vanna turns to a
selling headwind. The bullish DEX bid and the bearish vanna risk share the same root (elevated IV).

### IV term structure [STRUCT:iv_term_structure]

`structure` = **BACKWARDATION** (driven by the 06-18 1DTE front spike). But the cleaner front read
(below) is flat — backwardation here is the 0/1DTE artifact, not a deep event-stress curve.

### Term skew (25Δ, dte 30) [STRUCT:term_skew]

put_25d_iv **116.66%**, call_25d_iv **110.84%**, skew 0.0582, skew_ratio **1.053**, interpretation
**NORMAL**. Mild, ordinary put richness — NOT a tail-hedge panic despite the put OI builds (consistent
with phase-3's read that much of the put flow is *written*, not panic-bought).

### Front-end IV ratio (9d vs 30d) [STRUCT:front_end_iv_ratio]

near_iv (9d) **123.65%** vs far_iv (30d) **126.15%**, ratio **0.98**, regime **FLAT**. No acute event
stress at the front — consistent with no earnings until 2026-08-06. Just uniformly high IV.

### Today's gamma flip

**Skipped** — `today-gamma-flip` is 0DTE-only and intraday-meaningful; this is an after-hours/as-of run.

### Max pain (opex gravity, dte ≤ 30) [STRUCT:max_pain]

| Expiry | DTE | max_pain | dist | P/C OI |
|--------|-----|----------|------|--------|
| 2026-06-18 | 1 | $200 | −28.8% | 1.40 (degenerate — deep-put artifact, ignore as magnet) |
| **2026-06-26** | 9 | **$267.5** | **−4.7%** | 1.55 (nearest realistic magnet) |
| 2026-07-02 | 15 | $250 | −10.9% | 5.6 |
| 2026-07-10 | 23 | $235 | −16.3% | 1.6 |
| 2026-07-17 | 30 | $220 | −21.6% | 1.31 |

Max-pain is below spot at every expiry and slopes lower with tenor → a **mild downward OI gravity**.
Cross-check: agrees with phase-3 (put-heavy below spot, no near-spot pin) and phase-2 (mega blocks sold
into $283–285). The static-OI caveat applies — the $267.5 (06-26) is the usable near magnet; further
strikes are soft and migrate.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← path | Rows |
|------------------|--------------------|------|
| `uw options-structure gex --symbol NBIS --dte-max 45 --date 2026-06-17` | regime POSITIVE, ZGL $34.64, total_gex 9.84M ← `.regime/.zero_gamma_level` | surface |
| `uw options-structure dex --symbol NBIS --dte-max 45 …` | net_dex +$2.88bn, dealers buy underlying ← `.net_dex/.interpretation` | — |
| `uw options-structure vanna-charm --symbol NBIS --dte-max 45 …` | net_vanna −1,795 (falling IV → selling) ← `.net_vanna/.vanna_interpretation` | — |
| `uw options-structure iv-term-structure --symbol NBIS …` | BACKWARDATION (front 1DTE artifact) ← `.structure` | 16 |
| `uw options-structure term-skew --symbol NBIS --dte-target 30 …` | put 116.7%/call 110.8%, ratio 1.053, NORMAL ← `.interpretation/.skew_ratio` | — |
| `uw options-structure front-end-iv-ratio --symbol NBIS --near-dte 7 --far-dte 30 …` | 9d 123.7% / 30d 126.2%, FLAT ← `.ratio/.regime` | — |
| `uw options-structure max-pain --symbol NBIS --dte-max 30 …` | near magnet $267.5 (06-26, −4.7%) ← `.results[].max_pain_strike` | 5 |

## Tool errors

None. (`iv-term-structure` per-row IV rendered 0% under my jq field guess — the `structure` label
BACKWARDATION is the authoritative field and was read directly; per-row IV not transcribed.)

## DATA NOTE / CORRECTION

The 06-18 max_pain of $200 (−28.8%) is a degenerate static-OI artifact (the deep $200 put OI dominates
the 1-DTE weighting) — explicitly NOT used as a real pin magnet. The usable near magnet is $267.5
(06-26). iv-term-structure's BACKWARDATION label conflicts mildly with the FLAT 9d-vs-30d front-end
ratio; reconciled as: backwardation is the 0/1DTE front spike, the tradeable front (9d→30d) is flat.

## Verdict for downstream phases

- **Dealer regime:** **LONG GAMMA (positive), bullish-supportive DEX (dip-bid), but negative-vanna /
  vol-crush downside risk.** Net structural posture: **range-to-mild-pullback, not continuation.**
- **Conviction:** **3/5.** Regime signals are clear and internally consistent (long gamma + max-pain
  pull down + DEX bid = consolidation with a soft floor), but GEX magnitude is coarse for a non-mega-cap
  (per tool note) and the vanna risk is conditional on IV falling.
- **Three structural levels for phase-9 (+ near max-pain magnet):**
  1. **Near max-pain $267.5 (06-26, −4.7%)** — opex pin magnet / first downside gravity target.
  2. **GEX concentration $220–230** (below spot) — where dealer gamma is densest; a deeper magnet only on a break.
  3. **ZGL $34.64** — informational (confirms long-gamma; not a tradeable level). For overhead, defer
     to phase-3's $300 call wall (+6.9%).
- **Open questions:** Does the negative-vanna vol-crush risk materialize after 06-18 OPEX (cross-ref
  phase-5 VRP/IV-percentile)? Does the long-gamma dip-bid hold spot above the $267.5 magnet, or does
  phase-2's distribution + downward max-pain win? Is the elevated IV justified by historical realized
  vol or is it a sell (phase-5 VRP)?
