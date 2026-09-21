# Phase 4 — Dealer Structure & Gamma

**Ticker:** PATH (UiPath Inc.)
**As-of date:** 2026-06-01
**Generated:** 2026-06-01T20:24:00-04:00
**Upstream phases cited:** phase-1-flow.md, phase-3-positioning.md

## Summary

Dealers are **net long gamma** (GEX +18.1M, regime POSITIVE; spot $13.11 ≫ zero-gamma
$8.10) with peak positive gamma pinned at **$13** — a mean-reversion, vol-suppressed
regime that mechanically reinforces phase-3's range read. The $12–15 band is dealer-
pinned; the $13 ATM strike is the gamma magnet. Two softer counter-currents sit
underneath: every near-expiry **max-pain prints at $11** (−16%, a downward OPEX gravity
that agrees exactly with phase-3's $11 put wall), and the call-heavy book carries
**negative vanna** so a normalization of the elevated front IV (term structure is in
BACKWARDATION, Jun-5 102% vs back 78%, *despite no earnings until Sep*) would generate
mild dealer **selling** pressure. Skew is **COMPLACENT** — calls are richer than puts,
i.e. all the vol demand is upside/squeeze, no downside hedging priced. Net: a
vol-suppressed $12–15 chop with a $13 pin, a soft $11 monthly magnet below, and a
$14–15 call-wall cap above. Not a trending configuration.

## Key signals

- **GEX POSITIVE +18.1M, ZGL $8.10, spot $13.11** → long-gamma / mean-reversion
  [STRUCT:gex]
- Peak positive gamma at **$13 (+5.86M)**, then $12 (+3.32M), **$15 (+3.20M)**; only
  near-strike negative gamma is **$11 (−1.39M)** [STRUCT:gex]
- **Max-pain = $11 for Jun-5/12/18** (−16%), $10.5 for Jun-26 — downward OPEX gravity,
  matches phase-3 $11 put wall [STRUCT:max_pain]
- **DEX +76.8M**, dealers short calls → hedge = **buy underlying** (standing bid)
  [STRUCT:dex]
- **Skew COMPLACENT** (25Δ call IV 81.7% > put 71.5%, ratio 0.875) — upside demand, no
  downside hedge priced [STRUCT:term_skew]
- **IV BACKWARDATION** (front 102% vs far 78%, ratio 1.307) with **no Sep-earnings yet**
  → short-dated speculative vol [STRUCT:iv_term_structure][STRUCT:front_end_iv_ratio]

## Detailed findings

### GEX `[STRUCT:gex]`

- `regime` = **POSITIVE** — "Dealers net long gamma — expect mean-reversion and reduced
  volatility." `zero_gamma_level` = **$8.10**, `underlying_price` = $13.11,
  `total_gex` = **+18,115,064**.
- Top net-GEX strikes: **$13 +5.86M** (magnet), $12 +3.32M, **$15 +3.20M**, $13.5 +2.02M,
  $14 +1.95M, **$11 −1.39M**, $12.5 +1.20M, $18 +0.62M, $16 +0.46M.
- Read: positive gamma concentrated $12–15 → dealers mean-revert within the band; $13 is
  the strongest pin. $11 flips slightly negative (gamma support thins below). The crash-
  flip (short gamma / vol expansion) is only at ZGL $8.10, far from spot.

### DEX `[STRUCT:dex]`

- `net_dex` **+76.78M** (call_dex +83.5M, put_dex −6.75M). Tool: "Public is net call-long
  → dealers net short calls → dealer hedge is to BUY underlying." A standing mechanical
  hedge **bid** under spot, but in long-gamma it also means dealers sell into rallies →
  caps upside thrust.

### Vanna + charm `[STRUCT:vanna_charm]`

- `net_vanna` **−3,376** (call-heavy book), `net_charm` +206,499. Tool: "Falling IV →
  call delta drops → dealers (short calls) cut long-underlying hedge → **SELLING
  pressure**. Rising IV reverses." Given front IV is elevated (backwardation) with no
  scheduled catalyst, the path of least resistance is IV *down* → a mild structural
  selling headwind on the call-heavy book.

### IV term structure `[STRUCT:iv_term_structure]`

- `structure` = **BACKWARDATION**, 14 expiries. Front Jun-5 (4 DTE) avg IV **102.1%**
  (8,174 contracts), Jun-12 90.8%, Jun-18 85.0%, Jul ~78%, back ~79–80%. Front-end vol
  richly bid. **No earnings until 2026-09-03** (phase-0.5) → this is short-dated
  speculative/weekly vol, not a scheduled-event term-structure. Don't trade it as an
  earnings backwardation.

### Term skew `[STRUCT:term_skew]`

- `interpretation` = **COMPLACENT**. call_25d_iv **0.8168** > put_25d_iv **0.7146**;
  `skew` −0.1022, `skew_ratio` 0.875. Calls richer than puts = inverted (call) skew →
  demand is for upside, downside is *unhedged/cheap*. Constructive for the squeeze tilt
  but a contrarian yellow flag: a downside surprise would hit an unhedged book.

### Front-end IV ratio `[STRUCT:front_end_iv_ratio]`

- `ratio` **1.307** (near 4-DTE 102% / far 31-DTE 78%), `regime` BACKWARDATION. Confirms
  front-end stress is real but, absent a calendar catalyst, mean-reverts (feeds the
  vanna selling-pressure read above).

### Today's gamma flip (after-hours — informational) `[STRUCT:today_gamma_flip]`

- Market closed at run time; 0DTE/intraday read is end-of-session. `regime` POSITIVE,
  `atm_flip_strike` $8.5 (≈ ZGL). `key_walls` tags **$13/$13.5/$14/$12/$12.5 as
  support_walls** (positive gamma below price = support). Consistent with the GEX read;
  not used as a live intraday signal.

### Max pain `[STRUCT:max_pain]`

| Expiry | DTE | max_pain | dist% | P/C OI | total OI |
|--------|-----|----------|-------|--------|----------|
| 2026-06-05 | 4 | **$11** | −16.2 | 0.41 | 50,269 |
| 2026-06-12 | 11 | **$11** | −16.2 | 1.08 | 16,775 |
| **2026-06-18** | 17 | **$11** | −16.2 | 0.48 | **109,970** |
| 2026-06-26 | 25 | $10.5 | −20.0 | 0.48 | 6,531 |

Every near expiry pins to **$11** under the static-OI assumption (caveat: migrates as OI
builds). With spot $13.12 and the heaviest near OI at Jun-18 (110k) pinning $11, there is
a soft downward monthly gravity — but the $13 positive-gamma wall resists it intraday.
The two magnets bracket the likely path: chop between the $13 gamma pin and the $11
max-pain/put-wall floor.

## Cross-tool agreement (structure skeleton)

| Level | GEX | max-pain | phase-3 walls | Reading |
|-------|-----|----------|---------------|---------|
| **$11** | slight −γ | **pin (all near exp)** | put_wall_support | downside magnet / support floor |
| **$13** | **peak +γ (magnet)** | — | call_heavy ATM | mean-reversion pin ≈ spot |
| **$15** | +γ peak | — | call_wall_resistance | upside cap |

Three independent tools agree on $11 / $13 / $15 — a robust structural frame for phase-9.

## Tool calls (audit trail)

| Command | Key value(s) ← `jq` path | Rows |
|---------|--------------------------|------|
| `options-structure gex --dte-max 45` | regime POSITIVE, ZGL 8.10, peak $13 +5.86M ← `.regime`,`.zero_gamma_level`,`.per_strike[].net_gex` | per-strike |
| `options-structure dex` | net_dex +76.8M ← `.net_dex`; hedge=buy ← `.interpretation` | — |
| `options-structure vanna-charm` | net_vanna −3,376 ← `.net_vanna`; falling-IV→sell ← `.vanna_interpretation` | — |
| `options-structure iv-term-structure` | BACKWARDATION ← `.structure` | 14 exp |
| `options-structure term-skew --dte-target 30` | COMPLACENT, call 81.7%>put 71.5% ← `.interpretation`,`.call_25d_iv` | — |
| `options-structure front-end-iv-ratio` | ratio 1.307 ← `.ratio` | — |
| `options-structure max-pain --dte-max 30` | $11 all near exp ← `.results[].max_pain_strike` | 4 exp |

## Tool errors

First batch: `gex` jq used the wrong per-strike field (`.gex` vs actual `.net_gex`),
which errored and the fail-fast harness **cancelled the 3 sibling calls** (dex,
vanna-charm, iv-term, term-skew, front-end, max-pain, today-gamma-flip). Per Orchestration
rule 0, treated as "nothing ran"; all calls re-issued with hardened jq (forced exit 0).
No fabricated values — every number above is from the clean re-run.

## DATA NOTE / CORRECTION

`gex` per-strike field is **`net_gex`**, not `gex` (the path map lists `per_strike[]`
without the leaf name). Corrected before any value was transcribed.

## Verdict for downstream phases

- **Dealer regime:** **LONG GAMMA (positive)** — mean-reversion, vol-suppressed; spot
  far above ZGL. Reinforces the phase-3 range/collar thesis mechanically.
- **Conviction:** **3/5** — regime read is unambiguous, but the magnets pull both ways
  ($13 gamma pin vs $11 max-pain), so it's a *range* conviction, not a directional one.
- **Three structural levels for phase-9 (+ max-pain pin):**
  1. **$13 — peak positive-gamma pin** (mean-reversion anchor ≈ spot)
  2. **$15 — upside cap** (GEX +3.2M + call wall) ; $14 first resistance
  3. **$11 — near-expiry max-pain magnet + put wall** (downside gravity/support floor);
     **ZGL $8.10** = the only regime-flip (short-gamma/vol-expansion) level, crash-only
- **Open questions:**
  1. The vanna selling-pressure + max-pain-$11 + COMPLACENT-skew trio is a quiet bearish
     undercurrent beneath the bullish flow — does phase-5 history show PATH's
     positive-gamma days actually mean-revert, or do its squeezes override the pin?
  2. With no earnings until Sep, what *is* driving the front-end backwardation — a known
     June catalyst (conference/product), or pure short-dated speculation? Phase-6 to check.
