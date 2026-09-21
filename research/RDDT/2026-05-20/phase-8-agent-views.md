# Phase 8 — Multi-Agent Analyst Desk

**Ticker:** RDDT
**As-of date:** 2026-05-20 (data anchor 2026-05-18)
**Generated:** 2026-05-19T02:10:00-04:00
**Upstream phases cited:** phase-1-flow.md through phase-7-insights.md
**Agents launched:** accumulation-hunter, contrarian-scanner,
sweep-tracker, risk-monitor (4 of 5; earnings-scout skipped per phase
spec — RDDT Q2 earnings 2026-07-30 = 73 days out, outside the 30-day
window for the agent's mandate).

## Summary

The 4-agent desk returns a **MIXED** verdict that mirrors phase-7's
"high score / low confidence" tension. **2 NEUTRAL, 1 LONG, 1 SHORT**.
Average conviction across agents is **2.75 / 5**. No agent disputes
that institutional accumulation is real (all four cite phase-2's
block-tier 0.79 buy ratio); they disagree on whether the hostile
short-term tape (phase-5 bullish_flow 0% win rate, phase-6
TRANSITIONAL regime) overwhelms the multi-week constructive setup.
All four agents converge on the **same level structure**: support
$154.12, resistance $160, invalidation around $154 close OR GEX
regime flip below ZGL. The desk's consensus is therefore best
expressed as **HALF-SIZE, DEFINED-RISK LONG WITH HARD STOP** —
which lines up exactly with phase-6's TRANSITIONAL trading-guidance
card.

## Agent verdicts table

| Agent | bias | conv | horizon | support | resistance | one_line_take |
|-------|------|------|---------|---------|------------|---------------|
| accumulation-hunter | **LONG** | 3 | 1-4w | 154.12 | 160.00 | "Real accumulation footprint at $154–$160 with LEAP-grade fingerprints, but a thin shelf into faded-flow regime — accumulate on dips to $154, do not chase $160." |
| contrarian-scanner  | **SHORT** | 4 | 1-5d | 154.12 | 160.50 | "Textbook crowded long: 5/6 confluence, complacent skew, persistent sweeps, 22% confidence, sector bleeding, and the gamma pin already broke — fade the consensus." |
| sweep-tracker       | NEUTRAL | 2 | 1-5d | 154.12 | 160.00 | "Sweep momentum got knifed at the gate — wait for $160.50 reclaim on volume or a $154 retest with DP defense before chasing; otherwise stand down." |
| risk-monitor        | NEUTRAL | 2 | 1-5d | 154.12 | 160.00 | "Half size max (25-33% of normal), defined-risk only; cut on any close below 154 — the regime, not the company, is the trade-killer here." |
| earnings-scout      | n/a | n/a | n/a | n/a | n/a | SKIPPED — RDDT Q2 earnings 2026-07-30 (73 days out) is outside the 30-day mandate window. |

Plurality: NEUTRAL (2). Bullish agents (1) vs bearish agents (1) tie.
Average conviction across 4 non-skipped agents: **(3+4+2+2)/4 = 2.75**.

## Per-agent details

### accumulation-hunter

```
VERDICT
- bias: LONG
- conviction: 3
- horizon: 1-4w
- key_levels:
    support: 154.12
    resistance: 160.00
    invalidation: sustained close below 151.00 (loses 5-day DP shelf
                  and unlocks 150 short-gamma air pocket)
- top_signal: Phase-2 block-tier dark pool buy_ratio 0.793 on $26.26M
  premium plus a post-close 6,468-share print at $159.11 vs NBBO mid
  $157.75 (+$1.36) is corroborated by phase-7
  institutional_accumulation buy/sell 1.80 and signal_confluence 5/6
  — multiple independent UW tools converge on the same ACCUMULATION
  fingerprint.
- top_risk: Phase-5 bullish_flow 5d backtest shows 0% win rate (avg
  -3.05%) and the next-session 5/19 already printed -2.64% with GEX
  flipping POS→NEG, while phase-6 Comm Services -$20.5M sector
  outflow and TRANSITIONAL regime cap upside follow-through.
- one_line_take: Real accumulation footprint at $154–$160 with
  LEAP-grade fingerprints, but a thin shelf into faded-flow regime
  — accumulate on dips to $154, do not chase $160.
```

### contrarian-scanner

```
VERDICT
- bias: SHORT
- conviction: 4
- horizon: 1-5d
- key_levels:
    support: 154.12
    resistance: 160.50
    invalidation: sustained close above 160.50 on >1.5x avg volume
                  with positive GEX regime confirmed
- top_signal: Phase-5 historical_signal_backtest shows bullish_flow
  5d win rate 0% / avg -3.05% across 7 recent signals, and RDDT's
  own 5/19 close at $154.91 (-2.64%) already validates the fade
  while phase-4 GEX flipped POS→NEG.
- top_risk: Phase-2 block-tier 0.793 buy ratio plus the after-hours
  $1.36-over-mid lift represents real institutional accumulation
  that could absorb selling and squeeze through the 160 wall on any
  macro relief.
- one_line_take: Textbook crowded long: 5/6 confluence, complacent
  skew, persistent sweeps, 22% confidence, sector bleeding, and the
  gamma pin already broke — fade the consensus.
```

### sweep-tracker

```
VERDICT
- bias: NEUTRAL
- conviction: 2
- horizon: 1-5d
- key_levels:
    support: 154.12
    resistance: 160.00
    invalidation: sustained close below 154 (DP shelf fails) or
                  break above 160.50 with volume (squeeze ignites)
- top_signal: Phase-1 sweep persistence 5/5 sessions, $24.91M
  bullish premium, consistency 1.0, with front-end 160C ladder
  $850k+ ask-side stacked into phase-4's $622.7M GEX wall at $160.
- top_risk: Phase-5 bullish_flow 5d backtest win rate 0% / avg
  -3.05% plus 5/19 -2.64% drop already flipping GEX regime POS->NEG
  (ZGL 158.21) — the long-gamma pin lasted exactly one session and
  phase-6 Comm Services -$20.5M sector outflow is bleeding the tape.
- one_line_take: Sweep momentum got knifed at the gate — wait for
  $160.50 reclaim on volume or a $154 retest with DP defense before
  chasing; otherwise stand down.
```

### risk-monitor

```
VERDICT
- bias: NEUTRAL
- conviction: 2
- horizon: 1-5d
- key_levels:
    support: 154.12
    resistance: 160.00
    invalidation: close below 154 OR sustained spot below 158.39 ZGL
                  with GEX flip to NEGATIVE
- top_signal: Phase-6 TRANSITIONAL regime + Comm Services -$20.5M /
  Tech -$299.8M sector outflow combined with phase-5's bullish_flow
  backtest at 0% win rate (avg -3.05% over 5d, n=7) means the
  upstream bullish setup is firing into a tape that is actively
  fading it.
- top_risk: Phase-4 spot is only $0.50 above ZGL on a regime that
  has flipped 10x in 28 sessions (phase-5) — already flipped POS→NEG
  on 5/19 with -2.64% next-day move — so the long-gamma pin
  protecting the bullish thesis is structurally unstable and a
  single risk-off session opens the $150 short-gamma air pocket
  (-5.7%).
- one_line_take: Half size max (25-33% of normal), defined-risk
  only; cut on any close below 154 — the regime, not the company,
  is the trade-killer here.
```

### earnings-scout

**MISSING (skipped by spec):** RDDT Q2 2026 earnings = 2026-07-30
per phase-7 deep_dive; days-until-earnings = 73 > 30. The
earnings-scout agent's mandate is pre-earnings positioning within
30 days, so the agent is correctly skipped per `phases/phase-8-
agent-views.md` instructions. The 7/30 date should still be carried
into phase-9 as the **next major idiosyncratic catalyst** and the
explanation for the 8/21 IV hump in phase-4.

## Disagreements

The desk split LONG vs SHORT on the same data:

| Side | Agent | Conviction | Core argument |
|------|-------|-----------|---------------|
| LONG | accumulation-hunter | 3 | Real institutional accumulation (block tier 0.79, after-hours +$1.36 over mid, LEAP fingerprints) — wait for $154 retest |
| SHORT | contrarian-scanner | 4 | Crowded consensus with 22% model confidence, complacent skew, 0% recent flow win rate, regime fading bullish flow |

The two NEUTRAL agents effectively bridge these: sweep-tracker says
"momentum knifed, wait for level break" and risk-monitor says "half
size, defined risk, cut at 154". Both express the same trade as
"don't be a hero here".

**Pattern:** the LONG view is the **multi-week** (1-4w horizon) read;
the SHORT view is the **1-5d** read. They are not necessarily
contradictory — they are arguing about timeframe. A defensible
synthesis is: SHORT-bias or NEUTRAL near-term (next 1-5 sessions),
LONG-bias on a $154-ish bounce setup over 1-4 weeks.

## Tool errors

- earnings-scout: SKIPPED per spec (earnings > 30d).
- No other tool errors.

## Verdict for downstream phases

- **Plurality bias:** **NEUTRAL** (2 of 4).
- **Average conviction:** **2.75 / 5** across non-skipped agents.
- **Effective bias for phase-9:** **NEUTRAL-LONG with defined-risk
  buy-the-dip-only mandate** — the only agent willing to be
  size-on-now is the SHORT contrarian, and even the LONG agent says
  "do not chase $160". This is the textbook setup for: (a) NO
  market-order entry at spot; (b) buy a defined-risk structure on
  a $154-$155 retest only; (c) hard stop on a confirmed close below
  $154.
- **Three highest-quality signals across agents:**
  1. *(LONG corroborator)* — Phase-2 block-tier DP buy ratio **0.793**
     on $26.26M premium + post-close 6,468-share print at $159.11 vs
     NBBO mid $157.75 (+$1.36) → real institutional accumulation
     [DP:block_stratified, DP:dark_pool_extended_hours, AGENT:accumulation-hunter].
  2. *(SHORT corroborator)* — Phase-5 `bullish_flow` 5d win rate
     **0% / avg -3.05%** + RDDT's own 5/19 -2.64% next-day move →
     regime is fading bullish flow signals
     [HIST:signal_backtest, AGENT:contrarian-scanner].
  3. *(Sizing constraint)* — Phase-6 TRANSITIONAL regime + Comm
     Services -$20.5M sector outflow → half-size, defined-risk
     mandatory [MACRO:MarketRegime_2026-05-18, AGENT:risk-monitor].
- **Open questions surfaced by agents:**
  - Will a $154 retest hold (accumulation-hunter wants to see DP
    defense at the level before sizing) or will it break (sweep-
    tracker + risk-monitor invalidation)?
  - Does the next-session GEX print on 2026-05-20+ stay in NEGATIVE
    regime (confirming bearish tape) or re-flip POSITIVE
    (re-arming the magnet)?
  - Is the 1-5d weakness consumable inside a 1-4w long if expressed
    as a calendar/diagonal (long back-month, short front-week) to
    monetize the 5/22 79% / 7/17 63% IV term backwardation?
