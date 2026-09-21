# Phase 4 — Dealer Structure & Gamma

**Ticker:** PATH
**As-of date:** 2026-07-13
**Generated:** 2026-07-13T20:28:00-04:00
**Upstream phases cited:** phase-2-dark-pool.md, phase-3-positioning.md

## Summary

Dealers are **net long gamma** (`regime = POSITIVE`, ZGL $5.70 sits far below spot
$11.88) — the mechanical regime is **mean-reversion and suppressed realized vol**, so
absent a catalyst PATH behaves range-bound. The delta book is constructive: **net DEX
+34.4M with dealers net short calls → they must BUY the underlying to hedge**, a
mechanical bid that reinforces the phase-2 $11.80 accumulation shelf. But the same
book boxes price in: **max-pain is $11 into Jul-17 OPEX** (−7.3%) and the **largest
gamma wall is $13** (net GEX +5.6M), so near-term price is pinned in an **$11–$13
box**. Skew is **COMPLACENT** (0.985, no downside fear priced); IV term is **backwardated**
(front-end ratio 1.20) but that is technical near-OPEX richness, not event stress —
earnings are 2026-09-03. Vanna flags the risk: the dealer bid **unwinds to selling if
IV falls**. Conviction 3/5 — constructive floor, capped ceiling, no squeeze.

## Key signals

- **GEX regime POSITIVE** — "Dealers net long gamma — expect mean-reversion and reduced volatility"; ZGL **$5.70** ≪ spot $11.88 `[STRUCT:gex]`.
- **Net DEX +34.4M**, "dealers net short calls → dealer hedge is to BUY underlying" `[STRUCT:dex]` — bullish-mechanical bid under spot.
- **Largest gamma wall $13** (net GEX +5,595,439), secondary $12 (+3,437,988) `[STRUCT:gex per_strike]` — the $13 mean-reversion ceiling.
- **Max-pain $11 into Jul-17 OPEX** (dist −7.3%), migrating to $12 by Jul-31 `[STRUCT:max_pain]` — mild downward pin near-term.
- **Skew COMPLACENT** (skew_ratio 0.985; 25Δ put IV ≈ call IV) `[STRUCT:term_skew]` — no tail-hedging fear despite the beaten-down price.
- **Vanna warning:** net_vanna −2,930 (call-heavy) — "falling IV → dealers cut long-underlying hedge → SELLING pressure" `[STRUCT:vanna_charm]`.

## Detailed findings

### GEX `[STRUCT:gex]`
- regime **POSITIVE** / long-gamma; regime_desc: mean-reversion, reduced vol.
- total_gex **+15,612,557**; zero_gamma_level **$5.70**; spot $11.88 → spot ~2× above ZGL, firmly long-gamma.
- Top net-GEX strikes: **$13 (+5.60M)**, $12 (+3.44M), $14 (+1.98M), $11 (+1.52M), $15 (+1.35M), $12.5 (+1.14M); only $9 negative (−0.65M). Gamma concentrated $12–$14 → that band is the mean-reversion box.

### DEX `[STRUCT:dex]`
- net_dex **+34,371,545**. Interpretation: "Public is net call-long → dealers net short calls → dealer hedge is to BUY underlying." Constructive mechanical demand — the structural counterpart to the phase-2 accumulation.

### Vanna + charm `[STRUCT:vanna_charm]`
- net_vanna **−2,930** (call-heavy book), net_charm **+210,451**. No squeeze signal. Two-sided: the DEX bid depends on IV holding — a **falling-IV tape flips dealer hedging from buying to selling**. Watch IV rank (currently ~40).

### IV term structure & front-end `[STRUCT:iv_term_structure / front_end_iv_ratio]`
- structure **BACKWARDATION**, kink_expiry null. front_end ratio **1.202** (near_iv 1.036 vs far_iv 0.862). Front-month richer by 20%, but **no earnings until 2026-09-03** — this is near-OPEX/lotto-driven front richness (phase-1 saw 100–298% IV on Jul-17 micro-calls), not event stress. Do not trade it as a catalyst.

### Term skew `[STRUCT:term_skew]`
- interpretation **COMPLACENT**; skew_ratio **0.985**; put_25d ≈ call_25d IV. No downside insurance bid — the market is not pricing fear here, consistent with the phase-2 accumulation read (nobody rushing to hedge downside).

### Max pain `[STRUCT:max_pain]` (spot $11.87)

| Expiry | Max pain | Dist | P/C OI |
|--------|----------|------|--------|
| 2026-07-17 (4 DTE) | **$11** | −7.3% | 0.336 |
| 2026-07-24 | $11 | −7.3% | 0.298 |
| 2026-07-31 | $12 | +1.1% | 0.246 |
| 2026-08-07 | $12 | +1.1% | 0.191 |

Near-OPEX magnet $11 (mild downward pull), then $12. Agrees with phase-3: $11 is the two-sided call_heavy strike, $12 the nearest call wall. Static-OI caveat applies — soft magnet.

## Tool calls (audit trail)

| Command | Key value(s) ← `jq` path | 
|---------|--------------------------|
| `options-structure gex --dte-max 45` | POSITIVE, ZGL 5.70, $13 wall +5.60M ← `.regime`, `.zero_gamma_level`, `.per_strike` |
| `options-structure dex --dte-max 45` | +34.4M, hedge = BUY ← `.net_dex`, `.interpretation` |
| `options-structure vanna-charm` | net_vanna −2930 ← `.net_vanna`, `.vanna_interpretation` |
| `options-structure iv-term-structure` | BACKWARDATION ← `.structure` |
| `options-structure term-skew --dte-target 30` | COMPLACENT 0.985 ← `.interpretation`, `.skew_ratio` |
| `options-structure front-end-iv-ratio` | 1.202 backwardation ← `.ratio`, `.regime` |
| `options-structure max-pain --dte-max 30` | Jul-17 $11 ← `.results[].max_pain` |

## Tool errors

- None. (`today-gamma-flip` skipped — 0DTE intraday tool, run is after-hours/as-of.)

## DATA NOTE / CORRECTION

- GEX per-strike gamma field is `net_gex`, not `gex`; first sort used the wrong key.
  Re-read `.per_strike[].net_gex` → $13 wall values above.

## Verdict for downstream

- **Dealer regime:** **LONG GAMMA (positive)** — mean-reversion, vol suppression; range-bound until a catalyst overwhelms dealer damping. DEX adds a **bullish mechanical bid** (dealers buy to hedge short calls).
- **Conviction:** 3/5.
- **Structural levels for phase-9:**
  1. **$13 — gamma wall / near-term ceiling** (largest net GEX; also phase-3 call wall + covered-call strike). Triple-confirmed resistance.
  2. **$11 — near-OPEX max-pain magnet** (mild downward pin; also phase-3 two-sided strike). Sits just above the $11.80 darkpool shelf.
  3. **$12 — secondary gamma pin / max-pain by Jul-31** (nearest overhead, +1.1%).
  - ZGL $5.70 is a long-gamma *confirmation*, not a near-term level (would need a ~50% crash to flip to short-gamma).
- **Open questions:** If IV falls (skew already complacent), does the vanna-driven dealer unwind pressure the $11.80 shelf? Does phase-6 surface a catalyst strong enough to break the $11–$13 long-gamma box? Is the constructive DEX the mechanical echo of the same accumulator's LEAP-call footprint (phase-3 $18 Jan-27)?
