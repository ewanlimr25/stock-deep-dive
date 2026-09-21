# Phase 8 — Multi-Agent Analyst Desk

**Ticker:** FSLY
**As-of date:** 2026-05-19  (Effective data date: 2026-05-18)
**Generated:** 2026-05-19T01:30:00Z
**Upstream phases cited:** phase-1 through phase-7

## Summary

Four specialist agents launched in parallel; one (earnings-scout)
skipped because the next earnings date (2026-08-05) is 78 days out
— well outside the 30d window required by the skill rule. Net read
is **split 2 LONG / 2 NEUTRAL with no dissent to SHORT** — the
disagreement is not about direction but about *whether to do the
trade at all*. Average conviction across non-MISSING agents = **2.5
/ 5**. Both LONG agents (`accumulation-hunter`, `sweep-tracker`)
hold conviction 3 with the **identical key_levels** ($16.48 support,
$17.50 → $18.84 resistance, $15.50 invalidation) — a notable
agreement on coordinates. Both NEUTRAL agents (`contrarian-scanner`,
`risk-monitor`) hold conviction 2 and explicitly flag the
macro/regime headwind as the reason to stand aside rather than to
short. The **plurality concrete take**: this is a wheel /
covered-call name in a hostile regime, not a directional rip
case — exactly what UW's `insights_conviction_matrix` already
labelled in phase-7 (COVERED_CALL, 24.51% confidence).

## Agent verdicts table

| Agent | bias | conviction | horizon | one_line_take |
|---|---|---|---|---|
| accumulation-hunter | **LONG** | 3 | 1-4w | Real footprints at $16.48 and stock VWAP $16.57 — someone with a balance sheet is quietly bidding the bottom of an earnings crater, but they're selling $20 calls against it, so it's accumulation, not a moonshot. |
| contrarian-scanner | **NEUTRAL** | 2 | 1-4w | No extreme to fade — sentiment is normal, signals don't aggregate, crowd is split between dip-buyers and earnings-bagholders; stand aside, this is a wheel name, not a contrarian setup. |
| sweep-tracker | **LONG** | 3 | 1-4w | Real campaign tape — five straight days of ask-side sweeps target $17.5 with urgency premium baked into 5/22 IV; play it as a defined-risk break-and-go to the $18.84 supply wall, not a moonshot. |
| earnings-scout | MISSING | n/a | n/a | (Skipped per skill rule — earnings 2026-08-05 is 78d out, outside 30d window) |
| risk-monitor | **NEUTRAL** | 2 | 1-5d | Half-size at most, defined-risk only — this is a covered-call/wheel name in a hostile tech regime, not a directional long; correlated SMH/tech exposure must be netted before adding. |

## Per-agent details

### accumulation-hunter

```
VERDICT
- bias: LONG
- conviction: 3
- horizon: 1-4w
- key_levels:
    support: $16.48 (DP cluster $3.49M, block-buy print, phase-2)
    resistance: $17.50 (gamma magnet + campaign strike, phase-4)
                then $18.84 (overhead supply $5.65M, phase-2)
    invalidation: close below $15.50 (breaks negative-gamma pocket
                  and put-write line; phase-3/phase-4)
- top_signal: Phase-2 dark-pool block-tier buy_ratio 0.847 with
  371,000 shares accumulated above-mid in 34 seconds at 15:12Z,
  paired with phase-7 institutional_accumulation signal at 2.25×
  buy/sell ratio and VWAP $16.57 — three accumulation signals
  converging within one trading day.
- top_risk: FMR's 7.77M-share position is 43% underwater from
  $29.06 (phase-6) — if Fidelity capitulates, the $18.84-$19.03
  supply wall ($22M, phase-2) becomes a relentless distribution
  zone and accumulation thesis flips to a bull trap; phase-5
  bullish_flow backtest 8.3% win rate underscores the regime risk.
- one_line_take: Real footprints at $16.48 and stock VWAP $16.57
  — someone with a balance sheet is quietly bidding the bottom of
  an earnings crater, but they're selling $20 calls against it,
  so it's accumulation, not a moonshot.
```

### contrarian-scanner

```
VERDICT
- bias: NEUTRAL
- conviction: 2
- horizon: 1-4w
- key_levels:
    support: 15.50
    resistance: 18.84
    invalidation: close >$18.84 on rising tech-sector inflow (kills
                  the fade) OR close <$15.00 on accelerating tech
                  outflow (kills any mean-revert)
- top_signal: PCR z-score −0.18 (NORMAL) [phase-5] + FSLY absent
  from BOTH bullish and bearish top-50 confluence lists [phase-7]
  + COVERED_CALL low-confidence 24.51% [phase-7] — the crowd is
  NOT one-sided, so there is no extreme to fade.
- top_risk: bullish_flow backtest 8.3% win rate [phase-5] combined
  with tech sector −$299.8M outflow [phase-6] means the campaign
  IS the crowded trade — fading the longs has merit, but a −49%
  30d move plus reverse-skew COMPLACENT [phase-4] also screams
  "too late to short."
- one_line_take: No extreme to fade — sentiment is normal, signals
  don't aggregate, crowd is split between dip-buyers and
  earnings-bagholders; stand aside, this is a wheel name, not a
  contrarian setup.
```

### sweep-tracker

```
VERDICT
- bias: LONG
- conviction: 3
- horizon: 1-4w
- key_levels:
    support: $16.48 (DP at-spot cluster $3.49M, phase-2; aligns
             with 5/22 long-gamma $17.5 magnet floor in phase-4)
    resistance: $17.50 → $18.84 (5/22 long-gamma magnet phase-4;
                then $22M DP supply wall $18.41-$19.03 phase-2)
    invalidation: close below $15.50 (drops spot into deepening
                  neg-gamma pocket per phase-4 GEX; also breaks
                  phase-3 put-sell floor)
- top_signal: 5-of-5 sweep persistence with consistency_score 1.0
  and $642,945 5d premium [phase-1
  hot_chains_sweep_persistence], anchored by the 19:22:44Z
  ask-side cluster of ~5 prints on Sep'26 $17.5C totaling ~$190K
  of the $255,633 aggregated sweep — a multi-day campaign, not a
  single-day blip.
- top_risk: The $205K bid-side Jan'27 $20C is a write (no OI bump
  per phase-3) and phase-6's −$299.8M tech sector outflow +
  phase-5's 8.3% bullish_flow backtest win-rate mean the campaign
  is fighting a hostile complex.
- one_line_take: Real campaign tape — five straight days of
  ask-side sweeps target $17.5 with urgency premium baked into
  5/22 IV; play it as a defined-risk break-and-go to the $18.84
  supply wall, not a moonshot.
```

### earnings-scout (MISSING)

```
MISSING: earnings-scout (skipped per skill rule — next earnings
2026-08-05 is 78 days out, outside the 30-day pre-earnings
positioning window for which this agent is designed).
```

### risk-monitor

```
VERDICT
- bias: NEUTRAL
- conviction: 2
- horizon: 1-5d
- key_levels:
    support: $16.48 (DP at-spot accumulation cluster, phase-2)
    resistance: $17.50 (5/22 dealer-gamma magnet wall + 45-DTE
                neg-gamma acceleration strike, phase-4)
    invalidation: close below $15.50 (drops into deepening
                  negative-gamma pocket; phase-4 GEX at $15 =
                  −$8.2M) OR a close above $18.84 (clears the
                  $22M overhead supply shelf, phase-2)
- top_signal: Tech sector premium outflow −$299.8M on 5/18 (30×
  the next-worst sector) combined with bullish_flow backtest 8.3%
  win rate over last 5 sessions [phase-6 + phase-5] — single-stock
  conviction does not override regime headwind.
- top_risk: FSLY's realized vol 166% (30d) and IV 117.7% on 5/22
  [phase-5/4] mean any correlated tech drawdown (SMH bearish
  5-confluence per phase-7) gets amplified as a beta-to-tech tail;
  small position can deliver outsized portfolio P&L impact from a
  single-day air-pocket.
- one_line_take: Half-size at most, defined-risk only — this is a
  covered-call/wheel name in a hostile tech regime, not a
  directional long; correlated SMH/tech exposure must be netted
  before adding.
```

## Disagreements

There is **no agent with a SHORT bias.** The split is LONG vs
NEUTRAL, with neutrals describing the trade as "wheel, half-size,
defined-risk" — *which is a long-stock posture sized down for
regime*. So directionally, all 4 returned agents lean ≥ neutral.

The substantive disagreement:

| LONG side (acc-hunter, sweep-tracker) | NEUTRAL side (contrarian, risk-monitor) |
|---|---|
| Signal stack is real (5/5 sweep persistence, DP buy_ratio 0.847, COVERED_CALL setup) → put it on, defined-risk, 1-4w | Signal stack is real BUT regime headwind (8.3% backtest, tech sector −$299.8M, COMPLACENT skew suggests "too late to short and too late to chase long") → half size or stand aside |

**Read:** the disagreement is about *sizing* and *regime tolerance*,
not direction. Phase 9 should reconcile by sizing DOWN (NEUTRAL
caution) but keeping a LONG-biased structure (LONG agents'
coordinates).

## Tool errors

- `MISSING: earnings-scout` (intentional, per skill rule).
- All four returned agents reported nominal tool use (8 tool calls
  each, average ~24 seconds runtime). No agent reported a UW MCP
  error in their phase-8 work.

## Verdict for downstream

- **Plurality bias:** 2 LONG / 2 NEUTRAL / 0 SHORT (of 4 returned).
  No SHORT advocate ⇒ **net constructive but constrained.**
- **Average conviction (non-MISSING):** (3 + 2 + 3 + 2) / 4 =
  **2.5 / 5**.
- **Three highest-quality signals across agents:**
  1. *acc-hunter:* "DP block-tier buy_ratio 0.847 + 371,000
     shares above-mid in 34 seconds at 15:12Z" [DP:dark_pool_largest,
     dark_pool_block_stratified] [AGENT:accumulation-hunter].
  2. *sweep-tracker:* "5-of-5 sweep persistence consistency 1.0,
     $642,945 5d premium; 19:22:44Z cluster of ~5 ask-side prints
     on Sep'26 17.5C ~$190K" [FLOW:hot_chains_sweep_persistence,
     options_flow_top_premium_trades] [AGENT:sweep-tracker].
  3. *risk-monitor:* "Tech sector premium outflow −$299.8M on 5/18,
     30× next-worst sector; bullish_flow 5d backtest 8.3% win
     rate" [MACRO:MarketRegime_2026-05-18 UW, HIST:historical_signal_backtest]
     [AGENT:risk-monitor] — *the binding constraint on size.*
- **Open questions surfaced by agents:**
  - Is the FMR LLC ($226M position now ~43% underwater) capitulation
    a near-term risk? Phase 9 should plan for this as a tail.
  - Should phase-9 net out beta-to-SMH exposure if the desk
    already holds correlated tech? risk-monitor flagged
    explicitly.
  - Where does FSLY's idiosyncratic edge-AI narrative break the
    correlation to broader tech, if anywhere? No agent surfaced a
    confident answer; treat as open.
