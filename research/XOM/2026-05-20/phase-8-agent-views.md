# Phase 8 — Multi-Agent Analyst Desk

**Ticker:** XOM
**As-of date (user request):** 2026-05-20
**Effective data date:** 2026-05-18
**Generated:** 2026-05-19T00:00:00Z
**Upstream phases cited:** phase-0 through phase-7 (all)

## Summary

Four specialist agents ran in parallel. **The desk is overwhelmingly RANGE /
NEUTRAL with one cautious LONG** — all four converge at **conviction 2/5**
and a **1-5 day horizon**. The unanimous structural read is that XOM is
**pinned between $152.5 / $153.09 (OPEX ZGL — hard invalidation) and $165
(sticky dealer wall, not breakout)**, the macro tailwind is real but
positioning is already crowded with institutions trimming into the rally,
and the right action is **defined-risk bullish-biased structures with
fade-the-extreme tactical overlays** rather than naked directional bets.
**No agent voted SHORT.** `earnings-scout` was skipped per phase rubric
(next XOM earnings 2026-08-07 is 80 days out).

## Agent verdicts table

| Agent | Bias | Conviction | Horizon | One-line take |
|---|---|---|---|---|
| accumulation-hunter | **NEUTRAL** | 2/5 | 1-5d | "Not accumulation — hedged profit-taking into strength dressed up as a call build; one contract is doing all the work and the tape underneath it is selling." |
| contrarian-scanner | **NEUTRAL (lean fade)** | 2/5 | 1-5d | "Crowd is right on macro, wrong on entry — calls are euphoric and dealers will sell every approach to $165; fade rips, don't short the trend." |
| sweep-tracker | **RANGE** | 2/5 | 1-5d | "No momentum edge — institutional rolling and hedging inside a $157-$165 dealer-pinned range; fade extremes, don't chase directional sweeps." |
| risk-monitor | **LONG** | 2/5 | 1-5d | "Setup is structurally bullish but upside is capped at $165 dealer wall while downside is uncapped on a single Hormuz headline — size half, define risk, don't chase." |
| earnings-scout | **MISSING** | n/a | n/a | (Skipped — next earnings 2026-08-07 outside 30-day window per phase rubric.) |

**Vote tally:**
- LONG: 1 (risk-monitor)
- NEUTRAL: 2 (accumulation-hunter, contrarian-scanner)
- RANGE: 1 (sweep-tracker)
- SHORT: 0
- **Plurality:** NEUTRAL/RANGE (3 of 4 active agents)

**Average conviction across non-MISSING agents:** **2.0 / 5.0**

## Per-agent details

### accumulation-hunter

```
VERDICT
- bias: NEUTRAL
- conviction: 2
- horizon: 1-5d
- key_levels:
    support: 152.50
    resistance: 165.00
    invalidation: Close below $150 (breaches the $1.34B 5-day DP accumulation
                  shelf AND the $152.5 ATM gamma flip) OR XOM appearing in
                  `insights_institutional_accumulation` as ACCUMULATION on
                  a follow-up day
- top_signal: Phase-2/Phase-7 show $206.6M of mega-tier dark-pool premium at
  buy_ratio 0.049 (95% sell-classified, 5 of 6 mega prints below NBBO mid)
  with `insights_institutional_accumulation` independently flagging
  DISTRIBUTION (1.06M buy vs 2.03M sell shares), and aggregate call flow is
  bid-side dominant (call_bid 36,074 vs call_ask 29,426) — the call-OI bull
  thesis is carried by a single Jun'26 165C contract (+8,150 OI), not
  broad-based accumulation.
- top_risk: If the Jun'26 165C +8,150 OI build is genuine new long-call
  exposure by a strategic actor (not dealer hedging artifact), the dealer's
  $9.75B short-gamma-at-$165 obligation forces mechanical buying on
  continuation, and the macro supply-shock tape (Hormuz, Energy +$9.1M /
  Tech -$299.8M rotation) overrides the distribution read.
- one_line_take: Not accumulation — this is hedged profit-taking into
  strength dressed up as a call build; one contract is doing all the work
  and the tape underneath it is selling.
```

### contrarian-scanner

```
VERDICT
- bias: NEUTRAL (lean SHORT/fade on tactical 1-5d horizon)
- conviction: 2
- horizon: 1-5d
- key_levels:
    support: 157.50 (first dealer wall) / 152.50 (ATM gamma flip — hard
             invalidation)
    resistance: 165.00 (Jun'26 165C +$9.75B GEX sticky ceiling)
    invalidation: Sustained close above $165 on rising IV (kills fade
                  thesis — vanna unwinds the wrong way for shorts) OR
                  Strait of Hormuz reopening headline (kills macro tailwind
                  for longs)
- top_signal: Phase-7 `insights_conviction_matrix` = DISTRIBUTION (15.78%
  conf) with mega-tier dark pool buy_ratio 0.049 (Phase-2) + aggregate
  call_bid 36,074 > call_ask 29,426 — the crowd's call buying is being SOLD
  to them by institutions distributing stock while writing premium.
- top_risk: Macro supply shock (Strait of Hormuz / 10.5 mmb/d shut-in,
  Phase-6) is a real fundamental tailwind that can override positioning
  mechanics — fading a geopolitical bid is how careers end; +$315B net DEX
  means dealers are forced buyers on any continued call demand.
- one_line_take: Crowd is right on macro, wrong on entry — calls are
  euphoric and dealers will sell every approach to $165; fade rips, don't
  short the trend.
```

**Notable bonus signal-count:** the agent enumerated **seven** independent
contrarian signals (COMPLACENT skew, DP DISTRIBUTION, 0% bullish_flow
backtest, absent from confluence top-50, call bid > ask aggregate, GEX 6×
fragility, $165 as sticky resistance), but capped conviction at 2/5
because (a) macro tailwind is fundamentally real not just sentiment, (b)
sector rotation reframes the backtest universe, (c) market regime is
TRANSITIONAL not range-bound (fade rule only applies in range markets).

### sweep-tracker

```
VERDICT
- bias: RANGE
- conviction: 2
- horizon: 1-5d
- key_levels:
    support: 157.50 (gamma wall, with deeper support at $155 and OPEX
             ZGL $153.09)
    resistance: 165.00 (Jun'26 165C $9.75B GEX magnet — pin, not breakout)
    invalidation: sustained close <$153.09 (OPEX ZGL flip to short-gamma)
                  OR a single-day ask-side sweep print >$5M on near-term
                  ATM calls with vol/OI >5 and NO paired bid leg
- top_signal: Phase-1 top-5 sweeps are paired ask/bid legs (Dec'26 150C
  bid + Mar'27 155C ask, four 400-lot blocks in 3 minutes) = calendar roll,
  NOT directional momentum; corroborated by phase-7 conviction_matrix
  showing aggregate call_bid 36,074 > call_ask 29,426.
- top_risk: A genuine breakout sweep on Jun'26 165C/170C above $163 could
  force dealer delta chase through the $165 gamma wall and turn this from
  pin to squeeze — the tape would invalidate fast.
- one_line_take: No momentum edge here — this is institutional rolling
  and hedging inside a $157-$165 dealer-pinned range; fade extremes, do
  not chase directional sweeps.
```

### risk-monitor

```
VERDICT
- bias: LONG
- conviction: 2
- horizon: 1-5d
- key_levels:
    support: 153.09
    resistance: 165.00
    invalidation: Strait of Hormuz reopening headline OR sustained close
                  below $152.50 (dealer gamma flip)
- top_signal: Phase 6 sector rotation shows Energy +$9.1M vs Technology
  -$299.8M (near 300:1) on 2026-05-18, validating the energy-vs-tech
  rotation that reframes phase-5's 0% bullish-flow backtest as a
  tech-universe artifact XOM sits opposite of.
- top_risk: Binary asymmetry is poor — Hormuz reopening collapses Brent
  $20+ and shreds the entire phase-3/4 bull thesis simultaneously, while
  phase-2 mega-tier 95% sell skew + phase-7 DISTRIBUTION signal show
  institutions are already trimming into strength before that headline
  even hits.
- one_line_take: Setup is structurally bullish but the upside is capped
  at $165 dealer wall while downside is uncapped on a single Hormuz
  headline — size half, define risk, don't chase.
```

### earnings-scout

```
MISSING: earnings-scout
Reason: Next XOM earnings is 2026-08-07 (per phase-7 deep_dive); 80 days
out, far outside the 30-day phase-rubric window. Per phase-8 spec, skip
the agent and proceed with remaining four.
```

## Disagreements

The only divergence in BIAS is **risk-monitor (LONG)** vs the other three
(NEUTRAL/RANGE). However:

1. **risk-monitor's conviction is also 2/5** (same as the others) — it is
   not a high-conviction bull either.
2. **risk-monitor's invalidation overlaps the others** ($152.50 or Hormuz
   headline).
3. **risk-monitor's one-line take "size half, define risk, don't chase"**
   functionally mirrors sweep-tracker's "fade extremes, do not chase".

So there is no *substantive* dissent — all four agents are saying the
**SAME TRADE** with slightly different language: define-risk bullish-biased
structures, do not chase, fade extremes, respect the $152.5 / $165 range.

The only agent whose top_signal would change the trade direction is
risk-monitor, whose top_signal is the macro tailwind (Energy +$9.1M / Tech
-$299.8M rotation). That signal is real but does not justify SIZE — it
justifies a LEAN, not a STRUCTURAL POSITION.

## Tool errors

- `MISSING: earnings-scout` (skipped per rubric — earnings >30d).
- No agent reported tool errors; all four successfully read the phase 1-7
  files.

## Verdict for downstream

- **Plurality bias:** **NEUTRAL/RANGE (3 of 4)** with one cautious LONG.
  No SHORT votes. The composite read is "bullish-biased but pinned" —
  there is more upside catalyst risk (Hormuz reopen) than upside payoff
  (capped at $165 dealer wall).
- **Average conviction across non-MISSING agents:** **2.0 / 5.0** — low.
  The desk does not believe this is a high-conviction setup at this entry
  point.
- **Unanimous horizon:** **1-5d** (next OPEX cycle through May 22 weekly
  and toward Jun'26 monthly OPEX).
- **Three highest-quality signals across all agents:**
  1. **Macro rotation: Energy +$9.1M / Tech -$299.8M today** (risk-monitor's
     top_signal). Reframes phase-5's 0% bullish_flow backtest as a
     tech-universe artifact. [AGENT:risk-monitor → phase-6]
  2. **Mega-tier DP buy_ratio 0.049 + aggregate call_bid 36,074 > call_ask
     29,426** (accumulation-hunter + contrarian-scanner converging on the
     same insight). Institutions trimming + writing into call demand;
     one Jun'26 165C contract is doing all the work on the bull side.
     [AGENT:accumulation-hunter + contrarian-scanner → phase-2 + phase-7]
  3. **Paired ask/bid sweep legs (calendar roll signature)**: Phase-1 top-5
     sweeps are pairs (Dec'26 150C bid + Mar'27 155C ask, executed within
     3 minutes), NOT directional momentum. [AGENT:sweep-tracker → phase-1]
- **Open questions surfaced by agents:**
  - **(accumulation-hunter)** Will the Jun'26 165C build PERSIST on follow-up
    days (i.e., consecutive_build_days > 1 in `historical_oi_trend` next
    session)? If yes, the bull case strengthens; if not, it was a one-shot
    repositioning.
  - **(contrarian-scanner)** Does the COMPLACENT skew normalize back to
    put-favored over the next 5 sessions? Skew normalization confirms the
    "late-stage rally" read; skew widening confirms continued upside demand.
  - **(sweep-tracker)** Will any single ask-side sweep print >$5M on near
    ATM calls without a paired bid leg appear? That's the breakout-confirm
    signal that would flip RANGE to LONG.
  - **(risk-monitor)** What is the consensus probability of Hormuz
    reopening in next 30 days? Single most important unknown — phase 9
    should size as if reopening is 30–50% probability over the trade
    horizon and structure accordingly.

**The desk verdict for phase 9:** Build a **DEFINED-RISK BULLISH-BIASED
STRUCTURE** that:
1. Targets the $160 → $165 range (the OPEX-week pin + the dealer wall).
2. Hard invalidates below $152.50 (OPEX ZGL).
3. Sizes ≤ HALF of the position-size rubric Kelly calculation would
   otherwise produce (because of the 2/5 desk conviction).
4. Uses the COMPLACENT call-IV-rich-vs-put-IV pricing to favor PUT-CREDIT
   spreads over CALL-DEBIT spreads where possible (sell rich call IV, buy
   put protection cheaply).
5. Has a tactical fade-the-extremes overlay: if XOM rallies into $164+
   sharply on a single-headline catalyst, scale into a defined-risk
   bearish hedge (e.g., short call spread) for 1-3 sessions until the
   move mean-reverts.
