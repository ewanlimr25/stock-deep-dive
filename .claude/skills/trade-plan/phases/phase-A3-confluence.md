# Phase A3 — Confluence: Direction, Reasons, Levels, Events (goal #3 / #4)

## Goal

Fuse the reused flow/positioning/structure/macro/fundamentals layer with the new
chart layer into ONE direction, a conviction bin, an honest two-sided case
(reasons for / reasons against — goal #3), the consolidated level ladder and the
event calendar (goal #4). No trade structures yet — that's A4.

## Inputs

- `phaseA1-gap-audit.md` (the verdict + size ceiling)
- `phaseA2-chart.md` + `chart.json` (the price layer)
- The reused `decision.json` + phase MDs (flow/DP/OI/structure/macro/fundamentals/sentiment/debate)
- `rubrics/direction-rubric.md`, `rubrics/pattern-rubric.md`
- The stock-deep-dive rubrics: `sizing-rubric.md`, `confluence-scoring.md`, `citation-conventions.md`
- Reasoning-ledger lessons loaded in A0

## Steps

1. **Tally directional votes** across all available lanes (direction-rubric
   Step 1). Bias = plurality. Fundamentals/sentiment/debate can only cut.

2. **Classify flow↔chart agreement** (Step 2): CONFLUENT / FLOW-LEADS /
   CHART-LEADS / DIVERGENT. This is the core of the skill — state it explicitly;
   it drives the entry style and a conviction modifier.

3. **Set the conviction bin** (Step 3): start from the confluence-scoring band,
   then apply the agreement modifier, the five risk gates, the phase-0.5 context
   modifier, the staleness cut, and the gap-audit ceiling. Show each adjustment.

4. **Write reasons_for (≥2) and reasons_against (≥2)** (Step 4, goal #3). Each
   tagged and falsifiable. The top `reason_against` must be the best steelman of
   the other side; ≥1 must be a watchable trigger that reappears in invalidation.
   A DIVERGENT read is always a reason_against.

5. **Build the level ladder** (Step 5): for support / resistance / trigger /
   stop / target / pin / gamma-flip, prefer levels confirmed by BOTH a chart
   source and a dealer/OI source. Tag each with its source. Pull gamma_flip and
   largest_pin from the deep dive's `[STRUCT:gex]` / `[STRUCT:max_pain]` if
   present.

6. **Assemble the event calendar** (goal #4): earnings (from fundamentals /
   `next_earnings_date`), FOMC/CPI/NFP/PPI from the macro phase, OPEX from
   `uw oi opex-concentration` / the third Friday, plus any sector catalyst. Each
   row: date · event · impact (+/-/?) · source. These are the events that have
   historically moved this tape.

7. **Apply ledger lessons.** Adjust the read per any ACTIVE lesson for this
   ticker/sector/setup/pattern; list which lessons you applied.

## Write `trade-plans/<SYMBOL>/<DATE>/phaseA3-confluence.md`

Direction + conviction (with the adjustment trail), the flow↔chart agreement
verdict, reasons_for / reasons_against, the level ladder, the event calendar,
and the invalidation triggers (price / signal / macro per the deep-dive
invalidation rubric). Cite ≥3 distinct upstream datapoints.

## Verdict for downstream

- `bias`, `conviction`, `horizon`
- `reasons_for[]`, `reasons_against[]`
- `levels` (the ladder), `events[]`, `invalidation{}`
- the flow↔chart agreement label (informs A4's entry style)
