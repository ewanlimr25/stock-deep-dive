# Phase 4 — Dealer Structure & Gamma

**Ticker:** PATH · **As-of:** 2026-07-17 · **Version:** v1
Cites: phase-3-positioning.md (open question: are $12.5/$13 call walls dealer-short
squeeze-fuel or dealer-long cap?); phase-2-dark-pool.md ($11.88–$12.01 support
shelf); phase-0.5-context.md (`implied_move_pct 1.13`).

## Summary

Dealers are **net LONG gamma** — the regime is mean-reversion / vol-suppression,
which **answers phase-3's central question: the $12.5/$13 call walls are a genuine
CAP, not squeeze fuel.** `gex` returns `regime=POSITIVE` ("Dealers net long
gamma — expect mean-reversion and reduced volatility") with **Zero Gamma Level
$6.78**, far below spot $12.13, and a huge positive-gamma shelf spanning $11–$15
that **peaks at $13 (+6.03M GEX)** and $12 (+5.93M). Practically: rallies into
$12.5–$13 get sold by dealers, dips toward $11–$11.5 get bought — a $11.5–$13
range with $12–$12.5 as the fulcrum. Two things soften the bullish accumulation
thesis from phases 1–3: **near-expiry max-pain sits BELOW spot at $11–$11.5** (a
mild downward opex gravity), and **skew is COMPLACENT** (25Δ put IV 0.668 <
call IV 0.682, ratio 0.979 — no downside fear bid). The one genuine tailwind is
**DEX +43.9M: dealers are net short calls → their hedge is to BUY the underlying**,
a supportive bid consistent with the phase-2 dark-pool floor. Net structural read:
**range-bound with a supportive dealer bid and a hard $13 cap** — a patient-long /
buy-the-dip regime, NOT a breakout or squeeze.

## Key signals

- **POSITIVE gamma regime, ZGL $6.78** — dealers long gamma, spot $12.13 well
  above ZGL → mean-reversion, suppressed vol `[STRUCT:gex]`.
- **Peak positive GEX at $13 (+6.03M) and $12 (+5.93M)** — dealer long-gamma wall
  thickest exactly at the phase-3 call walls → those strikes are hard caps/pins,
  not squeeze fuel `[STRUCT:gex]`.
- **DEX +43.9M: dealers net short calls → BUY underlying to hedge** — a supportive
  structural bid under spot `[STRUCT:dex]`. The one clean bullish structural tell.
- **Near-expiry max-pain $11–$11.5** (Jul 24 $11 / Jul 31 $11.5 / Aug 7 $12) —
  opex gravity pulls *down*, 5–9% below spot `[STRUCT:max_pain]`.
- **Skew COMPLACENT (0.979), no vanna squeeze** — puts not bid, `net_vanna −3,088`,
  squeeze_signal null `[STRUCT:term_skew, vanna_charm]`. No fear, no mechanical
  squeeze setup.

## Detailed findings

### GEX `[STRUCT:gex]`
- `regime=POSITIVE`, `regime_description`: "Dealers net long gamma — expect
  mean-reversion and reduced volatility"; `total_gex` +23.3M; `zero_gamma_level`
  $6.78; spot $12.13.
- Per-strike (near spot): **$13 +6,034,671** · $12 +5,926,613 · $12.5 +4,235,840 ·
  $14 +2,812,296 · $15 +1,511,415 · $11 +1,306,112. Negative below: $10 −63,981,
  $10.5 −29,463, $8 −155,294 (the big put-OI strike). The positive shelf $11–$15
  is the mean-reversion cage; the fulcrum is $12–$13.

### DEX `[STRUCT:dex]`
`net_dex +43,911,621`; interpretation verbatim: *"Public is net call-long →
dealers net short calls → dealer hedge is to BUY underlying."* Supportive delta
bid — reconciles with long gamma as: dealers own convexity (sell rips/buy dips)
**and** currently carry short-call delta they must cover by buying. Floor-friendly.

### Vanna + charm `[STRUCT:vanna_charm]`
`net_vanna −3,088` (small negative), `net_charm +68,844`, **squeeze_signal null**.
No vanna squeeze regime (would need positive vanna + negative dealer delta + IV
declining). Charm flow is ordinary time-decay hedging. Nothing mechanical to trade.

### IV term structure `[STRUCT:iv_term_structure]`
`structure = BACKWARDATION` (front IV > back). Read with care: ATM-IV rows
returned null and **today is 0DTE July OPEX**, so the label is dominated by the
mechanically-elevated expiring front. Not corroborated as event stress by the
front-end ratio below — earnings are 7 weeks out (Sep 3), so treat the
backwardation as OPEX-artifact, not a catalyst tell.

### Term skew `[STRUCT:term_skew]`
`interpretation = COMPLACENT`, `skew_ratio 0.979`, 25Δ put IV **0.6677** vs call
IV **0.6824** — **calls slightly richer than puts**. No tail-hedging bid; call
demand consistent with the call-owned chain (phase-3). Yellow flag: complacency
means little downside protection is priced, so a shock would be un-cushioned.

### Front-end IV ratio `[STRUCT:front_end_iv_ratio]`
`ratio 0.731` (7d/30d) — near-dated IV is **73% of** 30-day, i.e. the front is
*cheaper* than the 30-day, not stressed. No acute near-term event premium (Sep 3
earnings sit outside the 30-day window). Confirms the backwardation label is a
0DTE artifact, not front-end event stress.

### Today's gamma flip
**Skipped** — 0DTE/intraday tool; this is an after-hours as-of run (rule: note
and skip). The `gex` ZGL ($6.78) + max-pain below cover the same ground statically.

### Max pain (opex gravity) `[STRUCT:max_pain]`
| Expiry | Max-pain strike | dist% from spot | P/C OI |
|---|---|---|---|
| 2026-07-17 (0DTE) | $11 | −9.39 | 0.264 |
| 2026-07-24 | $11 | −9.39 | 0.26 |
| 2026-07-31 | $11.5 | −5.27 | 0.21 |
| 2026-08-07 | $12 | −1.15 | 0.541 |
| 2026-08-14 | $11 | −9.39 | 2.956 |
Near-expiry pins cluster **$11–$11.5, below spot $12.13** — a mild downward gravity
(static-OI caveat: soft, migrates as OI builds). Note it *disagrees* with the
positive-GEX pin at $12–$13: gamma cages price at $12–$13 now, max-pain tugs toward
$11–$11.5 into each expiry. The honest synthesis is a **$11–$13 range biased to the
$11.5–$12.5 middle**, not a directional pin either way. Cross-checks phase-3: the
$11–$11.5 max-pain sits right at the phase-3 thin $11.5 put wall and just above the
phase-2 $11.88–$12.01 DP demand shelf — the levels agree.

## Tool calls
| Tool | Args | Result |
|---|---|---|
| options-structure gex | --symbol PATH --dte-max 45 --date 2026-07-17 | POSITIVE, ZGL 6.78, peak $13 |
| options-structure dex | --symbol PATH --dte-max 45 --date 2026-07-17 | +43.9M, dealers buy underlying |
| options-structure vanna-charm | --symbol PATH --dte-max 45 --date 2026-07-17 | no squeeze |
| options-structure iv-term-structure | --symbol PATH --date 2026-07-17 | BACKWARDATION (0DTE artifact) |
| options-structure term-skew | --symbol PATH --dte-target 30 --date 2026-07-17 | COMPLACENT 0.979 |
| options-structure front-end-iv-ratio | --symbol PATH --near-dte 7 --far-dte 30 --date 2026-07-17 | 0.731 (no front stress) |
| options-structure max-pain | --symbol PATH --dte-max 30 --date 2026-07-17 | pins $11–$11.5 |
| options-structure today-gamma-flip | — | skipped (after-hours) |

## Tool errors
- None.

## Verdict for downstream

- **Dealer regime: LONG gamma (POSITIVE), mean-reversion / range.** Spot $12.13 far
  above ZGL $6.78; long-gamma shelf $11–$15. This is a vol-suppression, buy-dip /
  sell-rip regime — the phase-1/2/3 bullish accumulation can grind but is **capped
  at the $13 gamma wall** and gets no squeeze help. DEX gives a supportive bid;
  max-pain gives a mild downdraft. Net: constructive-but-caged.
- **Conviction: 4 / 5** — GEX/DEX/max-pain are internally consistent and cross-check
  phase-2/3 levels; data clean. High confidence the near-term is range-bound.
- **Three structural levels for phase-9 (+ max-pain pin):**
  1. **ZGL $6.78** — regime floor; long-gamma holds as long as spot >> this (it is).
  2. **Peak-GEX $13 (+6.03M)** — the mean-reversion ceiling / call-wall cap; the
     level a bullish thesis must *catalyst* through (a close >$13 flips the cap to a
     launchpad). Secondary fulcrum $12 (+5.93M).
  3. **Near-expiry max-pain $11–$11.5** — opex-gravity magnet and downside pin;
     coincides with phase-2 DP shelf ($11.88–$12.01) and phase-3 $11.5 put wall.
  - **Vanna pivot: none** (no squeeze; net vanna ≈ 0).
- **Open questions:** The bullish accumulation needs a *catalyst* to break the $13
  long-gamma cap — the only scheduled one is **Sep-3 earnings** (7 weeks out).
  Until then, is this just range-trading noise around $12? Does the COMPLACENT
  skew + backwardation mean cheap downside protection for a long (phase-9 sizing),
  and is the max-pain $11–$11.5 pull strong enough to threaten the phase-2 $11.88
  shelf before then?
