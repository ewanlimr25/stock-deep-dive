# Phase 8 — Multi-Agent Analyst Desk

**Ticker:** FSLR
**As-of date:** 2026-05-18 (data anchor: 2026-05-15)
**Generated:** 2026-05-18T01:35:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-4-structure.md, phase-5-historical.md, phase-6-macro.md, phase-7-insights.md

## Summary

Four specialist sub-agents (accumulation-hunter, contrarian-scanner,
sweep-tracker, risk-monitor) ran in parallel against the same packed
phase-1-through-7 context. **Plurality verdict: LONG (2/4)**, with one
RANGE (contrarian-scanner) and one NEUTRAL (risk-monitor); the two LONG
votes are both conviction 3, the RANGE and NEUTRAL votes are both
conviction 2. **Average conviction across all 4 agents = 2.50/5.**
**earnings-scout was skipped** (FSLR Q2 earnings 2026-07-30, 73 days
out — beyond the 30-day window per skill rule). Remarkable level
convergence: **every agent put support at $231.62, resistance at $250,
and invalidation at a sustained close below $230** — a direct echo of
phase-2 dark-pool clusters and phase-4 dealer-structure walls. The
strategic spread is in *positioning approach*, not levels: the two LONGs
(accumulation-hunter, sweep-tracker) advocate defined-risk call spreads
toward $240/$250; the contrarian flags the +19% trailing rally as a
crowded chase but refuses to press a short into a binary tariff catalyst;
the risk-monitor recommends harvesting the May-22 IV bump via short
220/215 put credit spreads. **All four agents recommend defined-risk
structures; none recommend naked exposure.**

## Agent verdicts table

| Agent | bias | conviction | horizon | support | resistance | invalidation | one_line_take |
|-------|------|-----------|---------|---------|------------|--------------|---------------|
| accumulation-hunter | **LONG** | **3** | 1-4w | 231.62 | 250.00 | close < 230 | Quiet stacked accumulation behind a binary tariff catalyst — size small until $237 breaks or $231 holds the retest. |
| contrarian-scanner | **RANGE** | 2 | 1-5d | 231.62 | 250.00 | < 230 OR > 240 on heavy vol | Crowd is long +19%, calls richer than puts, 30B/5H stack, 9:1 DEX call-heavy into binary tariff — classic complacency, fade the chase, do not press the short. |
| sweep-tracker | **LONG** | **3** | 1-4w | 231.62 | 250.00 | close < 230 | Follow the sweep into $240/$250 magnet but size half — defined-risk call-spread campaign, not naked chase. |
| risk-monitor | **NEUTRAL** | 2 | 1-4w | 231.62 | 250.00 | close < 230 | TRANSITIONAL regime + binary tariff + failing bull-flow backtest = half-size defined-risk; sell May-22 IV bump via short-dated 220/215 put credit spreads, not naked longs. |
| earnings-scout | **MISSING: skipped** | n/a | n/a | n/a | n/a | n/a | Earnings 2026-07-30 (>30d) — per skill rule. |

Distribution: **LONG 2 / RANGE 1 / NEUTRAL 1 / SHORT 0.** No short bias
from any agent — even the contrarian explicitly declined to press a short
into the binary asymmetry.

## Per-agent details

### Agent 1 — accumulation-hunter

```
VERDICT
- bias: LONG
- conviction: 3
- horizon: 1-4w
- key_levels:
    support: 231.62
    resistance: 250.00
    invalidation: sustained close below 230 (loses long-gamma cushion;
      phase-4 −$46.5M GEX wall breaks)
- top_signal: Phase-7 reveals a two-tenor $280C build (Dec-2026 280C
  +434 OI / $24.72 avg + phase-1 Mar-2027 280C +480 vol/OI=10× at $34.75
  ask) layered behind a 5-of-5-session sweep persistence streak ($35.4M,
  consistency=1.0) — institutions are quietly stacking the same
  directional target across expiries while phase-2 large-tier DP
  buy_ratio of 0.535 on $61M / 377 trades absorbed a +5.8% intraday
  rally.
- top_risk: Phase-5 bullish_flow signal backtest is a 26.3% win rate /
  −1.26% avg 20d move in the current market-wide regime, and phase-6 UW
  regime is TRANSITIONAL with Tech sector −$151M outflows —
  accumulation thesis can be right but mis-timed if Section 232
  polysilicon decision slips or disappoints.
- one_line_take: Quiet stacked accumulation behind a binary tariff
  catalyst — dealers long gamma, DP absorbing the lift, $280 strike
  getting layered; size small until $237 breaks or $231 holds the
  retest.
```

### Agent 2 — contrarian-scanner

```
VERDICT
- bias: RANGE
- conviction: 2
- horizon: 1-5d
- key_levels:
    support: 231.62
    resistance: 250
    invalidation: close below 230 (loss of long-gamma cushion) OR close
      above 240 on heavy volume (gamma-magnet pull to 250 invalidates
      fade)
- top_signal: phase-5 bullish_flow signal backtest fires 26.3% win rate
  / −1.26% avg 20d move across 19 recent firings — the consensus +19%
  rally chase is statistically a fade, and phase-4's COMPLACENT skew
  (0.954, calls richer than puts) plus FLAT 1.044 front-end ratio shows
  zero crash premium priced into a binary Section 232 print, which is
  textbook "buy-the-rumor" complacency.
- top_risk: a bullish Section 232 polysilicon tariff decision lands
  inside the window and triggers an IV-expansion vanna squeeze that
  mechanically forces dealer buying through the $240/+$142M and
  $250/+$228M gamma magnets — the asymmetric idiosyncratic catalyst
  overpowers the crowded-trade fade.
- one_line_take: Crowd is long +19%, calls richer than puts, 30B/5H
  analyst stack, 9:1 DEX call-heavy into a binary tariff — classic
  complacency, but the catalyst is too asymmetric to short; fade the
  chase, do not press the short.
```

### Agent 3 — sweep-tracker

```
VERDICT
- bias: LONG
- conviction: 3
- horizon: 1-4w
- key_levels:
    support: 231.62
    resistance: 250
    invalidation: daily close below 230 (loses −$46.5M GEX cushion +
      dark-pool floor)
- top_signal: Phase-1 Mar-2027 280C $1.39M ask-side single print (Δ0.48,
  vol/OI 10×, IV 57.5%) layered with Phase-7's Dec-2026 280C +434 OI
  build — two-tenor $280 strike campaign confirms $280 is the
  institutional directional target, with Phase-4's +$228M GEX magnet at
  $250 as the mechanical first stop.
- top_risk: Section 232 tariff binary in the May-22 IV bump (58.2%) plus
  phase-1's $1.27M May 220-230 put hedge layer — a no-tariff ruling
  unwinds the upside thesis fast through $230 into the $224-228 air gap.
- one_line_take: Follow the sweep into $240/$250 magnet but size half —
  two-sided 250C tape and Sec 232 binary make this a defined-risk
  call-spread campaign, not a naked chase.
```

### Agent 4 — risk-monitor

```
VERDICT
- bias: NEUTRAL
- conviction: 2
- horizon: 1-4w
- key_levels:
    support: 231.62
    resistance: 250.00
    invalidation: close below 230 (loses long-gamma cushion; aligns with
      −$46.5M GEX wall and 220–230 put-hedge layer activation)
- top_signal: Phase-4 dealer regime is structurally long-gamma (+$452M
  GEX, ZGL $121, DEX +$18.3B, $250 magnet at +$228M) — built-in dealer
  bid on dips toward $230 and dealer sell into $250.
- top_risk: Correlation cluster — FSLR is tagged Technology (sector
  −$151M outflows, breadth 35.9%) AND a solar-policy beta (SEDG
  bearish-confluence 4, peer ENPH bullish 5) AND carries an unresolved
  Section 232 binary; a single tariff "no" headline would simultaneously
  hit Tech beta, solar sentiment, and the May-22 IV bid, while phase-5
  bullish_flow backtest is firing 26.3% / −1.26% in this exact regime.
- one_line_take: TRANSITIONAL regime plus binary tariff plus failing
  bull-flow backtest equals half-size defined-risk only — sell the
  May-22 IV bump via short-dated put credit spreads at 220/215, not
  naked longs.
```

### Agent 5 — earnings-scout (skipped)

`MISSING: earnings-scout` — per skill rule, only invoked when earnings
within 30 days. FSLR next earnings is **2026-07-30** (~73 days from
as-of 2026-05-18). Deferred — should be re-invoked closer to the report
date.

## Disagreements

There is no agent that takes the opposite (SHORT) bias. The notable
within-LONG-vs-not split:

- **contrarian-scanner (RANGE)** disagrees with the two LONG votes on
  the *crowdedness* of the trade — quoted top_signal:
  > "phase-5 bullish_flow signal backtest fires 26.3% win rate / −1.26%
  > avg 20d move across 19 recent firings — the consensus +19% rally
  > chase is statistically a fade … textbook 'buy-the-rumor' complacency."

- **risk-monitor (NEUTRAL)** disagrees with directional sizing — quoted
  top_signal:
  > "Phase-4 dealer regime is structurally long-gamma … built-in dealer
  > bid on dips toward $230 and dealer sell into $250."

Both dissents are valuable: they identify why the LONG thesis cannot be
sized at full conviction. Their top_risks are also useful for phase-9
invalidation language.

## Tool errors

- `earnings-scout` not invoked (intentional per skill rule). Recorded
  here for the audit trail.
- No agent reported execution errors.

## Verdict for downstream phases

- **Plurality bias:** **LONG (2 of 4 non-skipped agents)**, with
  **0 SHORT** votes — the directional skew is unambiguous, but the
  conviction is moderate.
- **Average conviction across non-MISSING agents:** **2.50/5.**
  Weighted: LONG cluster averages 3.0, dissent cluster averages 2.0.
- **Universal level convergence:**
  - Support **$231.62**
  - Resistance **$250.00**
  - Invalidation **close < $230**
- **Three highest-quality signals across all agents:**
  1. **Two-tenor $280C institutional build** (Dec-2026 280C +434 OI +
     Mar-2027 280C +480 vol/OI=10×) [accumulation-hunter, sweep-tracker
     — citing phase-1 + phase-7]
  2. **Bullish_flow signal backtest 26.3% win rate / −1.26% avg 20d in
     the current TRANSITIONAL regime** [contrarian-scanner, risk-monitor
     — citing phase-5]
  3. **Long-gamma dealer regime with $250 magnet (+$228M GEX) and $230
     friction wall (−$46.5M GEX)** [all four agents — citing phase-4]
- **Open questions surfaced:**
  - Does the Section 232 decision land in the May-22 IV-bump window
    or slip into June, and how is the position structured for a slip?
  - If FSLR breaks $237 cleanly, is that an early signal the catalyst
    has leaked, or just a gamma-magnet pull to $240?
  - Should the trade be sized for *catalyst optionality* (long
    call-spread) or *premium harvest* (short put-spread) — given that
    both LONG agents and the NEUTRAL agent endorsed different
    structures?
  - When should the trade be partially de-risked — at $240, $245, $250,
    or only after the Section 232 print?
- **Phase-9 guidance:** treat phase-8 as confirming **LONG bias with
  defined-risk discipline and half-size**, with the call-spread
  structure as primary and a complementary put-credit-spread as a
  premium-harvest secondary leg if portfolio capacity exists.
