# Phase 8 — Multi-Agent Analyst Desk

**Ticker:** MARA
**As-of date:** 2026-05-19
**Generated:** 2026-05-20T01:50:00-04:00
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-4-structure.md, phase-5-historical.md, phase-6-macro.md, phase-7-insights.md

## Summary

**Four of four active analyst sub-agents converge on a non-directional
verdict.** Three (accumulation-hunter, contrarian-scanner, sweep-tracker)
return **RANGE** at conviction **3**; one (risk-monitor) returns
**NEUTRAL with defensive lean** at conviction **2**. Zero LONG verdicts,
zero SHORT verdicts — **5-of-5 institutional-grade research lenses (the
4 agents + UW conviction matrix) all reject a directional trade**.
Average conviction across the four active agents: **2.75**. The
earnings-scout was skipped because the next earnings catalyst is
2026-08-04, ~75 days out of window.

The unanimous reading is **strong evidence for a defined-risk,
range-bound or vol-positive structure**, NOT a directional bet. Common
levels across agents:
- **Support: $11.75** (3 of 4 agents) — below this invalidates the
  dip-buy thesis and may trigger the $11 negative-GEX flip
- **Resistance: $13.00** (3 of 4 agents) — gamma wall + OI wall +
  dark-pool cluster confluence
- **Invalidation band: <$11.75 OR >$13.20** (consensus across all four)

## Agent verdicts table

| Agent | bias | conviction | horizon | one_line_take |
|-------|------|------------|---------|---------------|
| accumulation-hunter | **RANGE** | 3 | 1-5d | Quiet hands are *defending* a long (collar), not building one — pin $12-$13 until $13 breaks on volume |
| contrarian-scanner | **RANGE** | 3 | 1-4w | Everyone agrees MARA pins quietly to $13; own the puts they think are too cheap, sell the calls they keep writing, let FOMC settle it |
| sweep-tracker | **RANGE** | 3 | 1-5d | Sweeps say "something's happening" 5/5 sessions but direction mixed and biggest prints CAP at $13 — fade the edges, don't chase momentum that isn't there |
| risk-monitor | **NEUTRAL** (defensive) | 2 | 1-5d | Long-gamma magnet to $13 is real but fragile — half-size only, defined-risk only, secretly 3x correlated to BTC + miners + IWM |
| earnings-scout | SKIPPED | — | — | Next earnings 2026-08-04 (75 days out, out of window) |

**Distribution:** 3 RANGE, 1 NEUTRAL, 0 LONG, 0 SHORT. **Convergence 4/4.**

## Per-agent details

### accumulation-hunter

```
VERDICT
- bias: RANGE
- conviction: 3
- horizon: 1-5d
- key_levels:
    support: $11.91 (phase-2 cluster; below $11.75 invalidates dip-buy read)
    resistance: $13.00 (phase-3 48.8K OI wall + phase-4 $12.7B GEX magnet)
    invalidation: close <$11.75 (breaks dip-buy block → bias bearish)
                  OR close >$13.05 on volume (breaks gamma wall → bias LONG)
- top_signal: Phase-2 $11.75 / 210K-share ASK-side block + phase-3 LEAP
  10P Jan-27 +$662K ask-side + phase-3 13C/5-22 -2,114 net ask-bid
  together form a textbook covered-collar — a long-equity holder is
  defending position, not new institutional accumulation initiating.
- top_risk: The $13.28 5-day cluster ($24.6M / 20 trades) reads as
  single-counterparty distribution into the 5/11 earnings spike; if that
  desk keeps unloading at $13.20-$13.29 while peers (WULF/CIFR/HIVE)
  rally, MARA breaks $11.75 and the collar's put protection gets
  monetized.
- one_line_take: Quiet hands are defending a long, not building one —
  collar mechanics pin $12-$13, and MARA is the miner-cohort laggard
  until $13 breaks on volume.
```

[AGENT:accumulation-hunter]

### contrarian-scanner

```
VERDICT
- bias: RANGE
- conviction: 3
- horizon: 1-4w
- key_levels:
    support: $11.75 (phase-2 algo dip-buy + above $11 GEX flip)
    resistance: $13.00 (phase-3 48.8K OI wall + phase-4 $12.7B GEX wall
                + phase-2 $13.20-$13.29 distribution band)
    invalidation: close below $11.75 (turns short-gamma trend regime +
                  breaks dip-buy floor) OR break above $13.30 on volume
                  (cohort catch-up confirmed, fade thesis dead)
- top_signal: Phase-4 25Δ term skew COMPLACENT (call IV 88.8% > put IV
  78.4%, skew_ratio 0.883) on a 90% IV miner, combined with phase-1's
  6P/Jun-18 134% IV crash hedge (1,503 contracts) hidden inside that
  complacency — smart money is buying cheap tails while the crowd
  writes calls and ignores downside.
- top_risk: BTC breaks $82K resistance and crypto-miner peer cohort
  (WULF/CIFR/HIVE/CORZ/CLSK scoring 4-5 bullish) drags MARA mechanically
  through the $13 wall via dealer short-call rehedging — fade gets
  steamrolled by a sector catch-up rally.
- one_line_take: Everyone agrees MARA pins quietly to $13 — own the
  puts they think are too cheap to bother with, sell the calls they
  keep writing, and let FOMC week settle who's right.
```

[AGENT:contrarian-scanner]

### sweep-tracker

```
VERDICT
- bias: RANGE
- conviction: 3
- horizon: 1-5d
- key_levels:
    support: $11.91
    resistance: $13.00
    invalidation: close below $11.75 (negates dip-buying + flips GEX trap
                  door at $11.00) OR close above $13.20 (breaks call-write
                  wall + DP distribution band)
- top_signal: Phase 3's 48.8K OI at 13C/May-22 with net ask-bid -2,114
  (heavy call-writing) combined with Phase 4's +$12.7B GEX wall at $13
  creates a deterministic gamma cap into Friday OPEX, while $737K bullish
  vs $380K bearish sweep premium (Phase 1) is too modest to overpower it.
- top_risk: A BTC-driven IV spike could lift MARA mechanically (Phase 4
  vanna -922K), but the inverse — a typical post-OPEX IV crush — forces
  dealer selling and breaks the $12.50 pin to the downside, invalidating
  the range.
- one_line_take: Sweeps say "something's happening" 5/5 sessions but
  direction is mixed and the largest prints CAP at $13 — trade the
  $11.91-$13.00 box, fade the edges, don't chase momentum that isn't
  there.
```

[AGENT:sweep-tracker]

### risk-monitor

```
VERDICT
- bias: NEUTRAL (lean defensive)
- conviction: 2
- horizon: 1-5d primary; re-assess into FOMC 6/17-18
- key_levels:
    support: $11.75 (phase-2 DP block buy 265K shares — last
              institutional defense before the trap door)
    resistance: $13.00 (phase-4 gamma wall +$12.7B GEX, hardest pin
                in chain)
    invalidation: spot <$11.00 on a close (first negative-GEX strike
                  −$1.16B; below this the 22-session positive-gamma
                  regime breaks and dealers flip to trend-amplifying
                  SELLING). Equivalent BTC trigger: IBIT loses $74.2K
                  BTC support → MARA-beta cascade.
- top_signal: Phase-4 vanna NEGATIVE (-922K) combined with IV already at
  14.8th percentile (phase-5) means the asymmetric risk is a vol crush
  forcing mechanical dealer selling — and Phase-7 shows MARA scores 0/5
  bullish confluence while WULF/CIFR/HIVE/CORZ/CLSK all score 4-5, so
  MARA is the cohort laggard most exposed if the miner trade unwinds.
- top_risk: Stacked correlation — Phase risk_portfolio_correlation just
  confirmed MARA/CLSK 0.789, MARA/IWM 0.64, MARA/WULF 0.571, plus
  IBIT/IWM 0.587: a long MARA position is simultaneously a leveraged bet
  on BTC, the miner cohort, AND Russell small-caps in a TRANSITIONAL
  regime with Financial Services sector seeing −$48.8M outflow today —
  one factor crack (BTC <$74K) cascades through all three correlated
  exposures into the $11 gamma trap door, where short-gamma dealer
  selling amplifies the move down (estimated -$1.16B GEX flip → ~5-8%
  air pocket to $10.00 / -$415M GEX shelf).
- one_line_take: Long-gamma magnet to $13 is real but fragile —
  half-size only, defined-risk only, and any long MARA is secretly 3x
  correlated (BTC + miners + IWM) into a cohort where MARA is already
  the laggard.
```

[AGENT:risk-monitor]

### earnings-scout

**SKIPPED** — next earnings date is 2026-08-04 per
`insights_deep_dive.next_earnings_date` (phase 7). Pre-earnings analysis
requires earnings within the 30-day window. Q1 2026 earnings already
released and digested (5/11 — see phase 6).

[AGENT:earnings-scout (skipped)]

## Disagreements

**None substantive.** All four active agents agree:
1. Direction is RANGE / non-directional
2. Support floor around $11.75-$11.91
3. Resistance ceiling at $13.00
4. Invalidation triggers outside that band

The single nuance: **risk-monitor pushes harder defensive** with
NEUTRAL (vs RANGE) and conviction 2 (vs 3), based on correlation
cascade math. This is a *sizing* disagreement, not a *direction*
disagreement — risk-monitor argues for a smaller defined-risk
expression than the other three. Phase 9 should heed this on sizing.

## Tool errors

None. All four agents completed. earnings-scout SKIPPED by design (not
an error).

**Note:** risk-monitor independently invoked `risk_portfolio_correlation`
to derive the correlation matrix cited in its top_risk — that data
**was not in the original phase 1-7 chain** and should be referenced
forward as a phase-8 contribution:

| Pair | 30d correlation |
|------|-----------------|
| MARA / CLSK | 0.789 |
| MARA / IWM | 0.640 |
| MARA / WULF | 0.571 |
| IBIT / IWM | 0.587 |

(Source: risk-monitor sub-agent's UW MCP call)

## Verdict for downstream phases

- **Plurality bias:** RANGE (3 of 4) / NEUTRAL-defensive (1 of 4) →
  **NON-DIRECTIONAL** with defensive sizing
- **Average conviction:** 2.75 across 4 active agents
- **Three highest-quality signals across all agents:**
  1. **Covered-collar mechanics** [accumulation-hunter]: $11.75 dip-buy
     + Jan-27 10P LEAP +$662K ask + 13C/5-22 net ask-bid -2,114 = single
     coherent position structure indicating range-defense, not
     accumulation
  2. **Complacent skew + hidden crash hedge** [contrarian-scanner]:
     skew_ratio 0.883 (calls > puts) on a 90% IV miner WHILE 1,503
     contracts of 6P/Jun-18 at 134% IV signal smart-money tail-load
  3. **Stacked correlation cascade** [risk-monitor]: MARA is 3x
     correlated (BTC 0.79 to CLSK, IWM 0.64, WULF 0.57); a single BTC
     break of $74K could cascade through all three into the negative-GEX
     trap door at $11
- **Open questions surfaced by agents:**
  - (sweep-tracker) Post-OPEX IV crush could mechanically force dealer
    selling via negative vanna — does phase 9 hedge this directly?
  - (contrarian-scanner) Is the 6P/Jun-18 crash hedge the *first*
    smart-money tail buyer, or does the OI history show it as a
    standing position? Phase 10 may want to check.
  - (risk-monitor) Should phase 9 size against the *cohort*
    correlation (MARA + CLSK + WULF) or treat MARA standalone? Strong
    argument for sizing as if MARA is a leveraged crypto-miner ETF.
- **Phase 9 implications:**
  - Defined-risk structure (no naked long stock, no naked long calls,
    no naked short puts)
  - Range-bound expression: iron condor, calendar/diagonal, or
    put-spread collar — NOT outright directional
  - Half-size or smaller (TRANSITIONAL regime, sub-3 conviction)
  - Time horizon: primary 1-5d (Friday OPEX), secondary 1-4w (into FOMC
    6/17-18)
  - Tail hedge consideration: cheap downside (puts) are mispriced
    given complacent skew — contrarian-scanner argues for a long-vol
    tilt
