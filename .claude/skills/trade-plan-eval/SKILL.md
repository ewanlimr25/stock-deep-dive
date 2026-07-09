---
name: trade-plan-eval
description: Evaluates a trade plan AFTER a trade has been taken and feeds the lessons back so future recommendations improve. Marks the plan to market path-aware (WIN/LOSS/OPEN, R achieved, MFE/MAE), grades the reasoning behind it (was each reason-for/against right, was the direction/pattern/sizing call sound, Brier calibration), attributes the result to the decisive evidence lanes, and appends lessons to a reasoning ledger the trade-plan skill reads. Use when the user says "evaluate / grade / review the trade plan for <TICKER>", "how did the <TICKER> trade work out", "mark my <TICKER> plan to market", or "what did we learn from the <TICKER> trade".
model: fable
effort: high
---

# Trade Plan Eval

The outcome-and-learning loop for `/trade-plan`. A plan that is never marked to
market is an unfalsifiable opinion; this skill closes the loop. After you take a
trade, it resolves what actually happened, grades the *reasoning* (not just the
result), and writes durable lessons to a shared reasoning ledger so the next
plan on that name/sector/setup is sharper. Rubric changes are **proposed**, never
auto-applied.

It is the trade-plan analogue of `/deep-dive-calibration` (which marks deep-dive
blueprints to market), specialized to a single taken trade and to improving the
reasoning model rather than just reporting hit-rate.

## When to invoke

- "evaluate / grade / review the trade plan for <TICKER>"
- "how did the <TICKER> trade work out" · "mark my <TICKER> plan to market"
- "what did we learn from the <TICKER> trade"

Do NOT invoke to build a plan (`/trade-plan`) or to backtest the whole deep-dive
corpus (`/deep-dive-calibration`).

## Inputs

- **Required:** a ticker + the plan date (locates `trade-plans/<SYMBOL>/<DATE>/`).
- **Required for a real eval:** the trade actually taken — vehicle (stock/option),
  direction, entry price + date, stop, target(s), size, structure. If the user
  says "as planned", inherit the plan's stock_plan / primary options_plan. If no
  trade was taken, the eval runs hypothetically against the plan's own levels and
  is labelled as such.
- **Optional:** review date (default = today, look-ahead safe).

## Output convention

```
trade-plans/<SYMBOL>/<PLAN_DATE>/
  eval-<REVIEW_DATE>.md      human-readable evaluation
  eval-<REVIEW_DATE>.json    structured, validated envelope
trade-plans/_eval/
  reasoning-ledger.md        appended with the lessons learned (shared store)
```

Immutable: never overwrite an existing eval; `-v2` on collision.

## Phase graph

| # | File | Purpose | Detailed prompt |
|---|------|---------|-----------------|
| E0 | intake | load plan + trade taken + review window | `phases/phase-E0-intake.md` |
| E1 | mark-to-market | path-aware outcome (WIN/LOSS/OPEN, R, MFE/MAE) | `phases/phase-E1-mark-to-market.md` |
| E2 | reasoning review | grade reasons/pattern/levels/sizing + Brier + attribution | `phases/phase-E2-reasoning-review.md` |
| E3 | lessons | append ledger lessons + propose rubric edits; emit eval.json | `phases/phase-E3-lessons.md` |

## Tooling

- `lib/mark_to_market.py` — deterministic path-aware ±1R resolver; reuses the
  trade-plan skill's `ohlc.py` for OHLC (yfinance → screener parquet).
- `.claude/skills/trade-plan/lib/chart_engine.py` — forward chart context for the
  reasoning review.
- `schemas/validate_eval.py` — stdlib validator; E3 must make it print `OK`.

## Rubric

- `rubrics/eval-rubric.md` — outcome resolution, reasoning grading, Brier
  calibration, attribution, and the ledger-lesson lifecycle (CANDIDATE → ACTIVE
  on ≥2 supporting trades; RETIRED on contradiction).

## Orchestration rules

0. **One phase at a time, run → read → write.** Resolve outcome before grading;
   never grade reasoning RIGHT just because the trade won.
1. **Outcome ≠ process.** Score both; a sound losing trade keeps its process
   credit, an unsound winning trade is flagged.
2. **Don't finalize on OPEN.** If E1 is OPEN/INCONCLUSIVE, reasoning grades stay
   UNRESOLVED and no Brier is recorded.
3. **Propose, don't mutate.** Lessons append to the ledger; generator rubric
   changes are emitted as `proposed_rubric_edits` for the user to accept.
4. **Cite the path.** Every reasoning verdict references what actually happened
   (a hit date, a level breach, a structure flip), not a vibe.

## Execution

Read each `phases/phase-E*.md` in order (E0→E1→E2→E3). After E3, surface the
outcome, the calibration verdict, the one-line takeaway, the lesson ids
added/promoted, and any proposed rubric edits awaiting the user's decision.

Disclaimer for every eval: *"For research and educational use only. Not
financial advice."*
