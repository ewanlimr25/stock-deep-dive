# Phase 9 — Synthesis & Trade Blueprint

## Goal

Speak as a desk PM running an institutional book. Translate phases 1–8 into a
single, actionable, falsifiable trade blueprint. Emit `phase-9-trade-plan.md`
following `templates/trade-plan-template.md`.

## Inputs (read all)

- `phase-1-flow.md` through `phase-8-agent-views.md` from the current run.
- `rubrics/confluence-scoring.md` (for the conviction bin choice)
- `rubrics/invalidation-rubric.md` (for the invalidation section)
- `rubrics/sizing-rubric.md` (for Kelly math)
- `rubrics/citation-conventions.md` (for every numeric claim)
- `templates/trade-plan-template.md` (the skeleton to fill)

## Voice

You are a PM on a $5–50M options-overlay book. You speak plainly. You name
specific strikes. You do not hedge with "could / might / possibly" when the
data is clear. When it is ambiguous, you say so and choose a defined-risk
structure. You write for another PM to either accept, reject, or counter-edit.

Open the plan with:

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Required sections (from template)

Fill every section in `templates/trade-plan-template.md`. Below are the
specific rules per section.

### Thesis (≤3 sentences)

Must cite at least 3 distinct upstream datapoints with proper tags:
- 1 from phases 1–4 (today's tape)
- 1 from phase 5–7 (historical context or UW insight)
- 1 from phase 6 or 8 (macro or agent verdict)

### Bias + conviction

- Bias from the plurality of phases 1–8.
- Conviction MUST snap to one of {0.55, 0.65, 0.75, 0.85, 0.95}.
- Conviction must match the band given by phase-10's confluence score. If
  phase-9 wants to deviate (which is allowed but rare), write a
  `## Conviction deviation` note explaining why.

### Entry zones (primary, aggressive, fade)

- Primary: price + trigger; trigger should be a level cited from phase-2 or
  phase-4 (DP wall or gamma flip).
- Aggressive: a more opportunistic entry; explain the trigger.
- Fade: a counter-trade entry IF the primary thesis invalidates partially —
  this is your hedged plan B.

### Levels to watch

Source every level from a specific upstream phase. The minimum set:
- support (phase-2 price level or phase-3 OI cluster)
- resistance (phase-2 / phase-3)
- gamma flip (phase-4 `today_gamma_flip` if available, else phase-4 ZGL)
- largest pin (phase-3 `pin_risk` if within OPEX week)

### Invalidation

Apply `rubrics/invalidation-rubric.md`: write all three categories
(price-based, signal-based, macro-based) with concrete, falsifiable triggers.

### Sizing (% of risk)

Apply `rubrics/sizing-rubric.md`:
1. Pick p = conviction bin.
2. Pick b = payoff ratio from your chosen target/entry/stop.
3. Compute raw_kelly.
4. Apply fraction=0.25 and cap_pct=5.
5. Write Final size = …, with deviation_reason only if you deviated upward.

### Option structures (≥1 directional + ≥1 defined-risk)

Required minimums:
- One **directional** structure (long call/put, debit spread, or risk reversal)
  with specific strike, expiry, debit/credit, breakeven, max loss.
- One **defined-risk alternative** (credit spread, iron condor, butterfly)
  with the same level of detail.
- Pick strikes by referencing phase-3 OI clusters or phase-4 gamma walls when
  possible.
- Pick expiries that match the time horizon AND avoid binary events you do
  not want to trade (use phase-6 catalyst calendar).

### Macro overlay

Bullet tailwinds and headwinds, each tagged `[MACRO:<series>]` from phase-6.

### Catalyst calendar (next 30d)

Table with date / event / impact direction, all sourced from phase-6.

### Post-trade monitoring checklist

Concrete things to re-check daily / on each phase. At least 4 items.

### Citations summary

Final block listing the ≥3 distinct upstream datapoints from the thesis
(M-04). This is what phase-10 will spot-check.

## Validation before writing the file

- [ ] All template sections are non-empty.
- [ ] Conviction is in {0.55, 0.65, 0.75, 0.85, 0.95}.
- [ ] Sizing math shown explicitly.
- [ ] ≥3 distinct upstream citations in the thesis.
- [ ] ≥1 directional + ≥1 defined-risk structure.
- [ ] All citation tags resolve to actual content in the cited phase MD
      (spot-check 2 of them).
- [ ] Disclaimer line is present at the top.

## Common pitfalls

- Writing the trade plan to fit a pre-existing bias instead of the data.
- Choosing strikes without referencing OI / gamma walls.
- Picking an expiry that straddles earnings without explicitly addressing IV
  crush.
- Saying "sized to conviction" without showing the Kelly math.
- Using vague invalidation ("if it breaks down") — must be a specific price
  or signal flip.
