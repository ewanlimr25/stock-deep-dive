# Phase E0 — Intake (load the plan + the trade taken)

## Goal

Load the trade plan being evaluated, the actual trade the user took, and the
forward price path needed to mark it to market.

## Inputs (collect/confirm)

1. **The plan.** `trade-plans/<SYMBOL>/<PLAN_DATE>/trade-plan.json` (+ `.md`).
   Read: `bias`, `conviction`, `stock_plan` (entry/stop/targets/direction),
   `options_plans` (each structure/strikes/expiry/target_date/target_price),
   `reasons_for`, `reasons_against`, `patterns`, `levels`, `invalidation`,
   `sizing`, the flow↔chart agreement note, and `citations`.

2. **The trade taken** (ask the user if not supplied; this is what makes the
   eval real rather than hypothetical):
   - vehicle (stock | option | none/"didn't take it"),
   - direction, actual entry price + date, stop, target(s),
   - if option: which structure + expiry,
   - size taken (% book),
   - whether execution matched the plan (`matched_plan`).
   If the user only says "I took it as planned", inherit the plan's stock_plan
   or the primary options_plan accordingly.

3. **Review date.** Default = today (look-ahead safe). Pick the
   horizon-matched window from the eval rubric (e.g. `1-4w` → review at 10D & 21D).

## Steps

- Parse the plan JSON; record the underlying `direction`, `entry`, `stop`, and
  `targets` to mark to market (for an options trade, mark the **underlying**
  against the plan's `target_price`/`stop`/`invalidation`, since R is defined on
  the underlying path).
- Confirm OHLC is reachable for the window:
  ```bash
  python3 .claude/skills/trade-plan/lib/chart_engine.py --ticker <SYMBOL> --date <REVIEW_DATE> | head -c 200
  ```
- Set up the output path `trade-plans/<SYMBOL>/<PLAN_DATE>/eval-<REVIEW_DATE>.md`
  (immutable; `-v2` on collision).

## Write `phaseE0` notes (inline or to the eval MD draft)

Record the plan summary, the trade-taken parameters, the review date + window,
and any missing inputs (if the user can't supply the actual fill, mark the eval
hypothetical and note it).

## Verdict for downstream

- the mark-to-market parameters: `direction`, `entry`, `stop`, `targets[]`,
  `invalidation_price`, `plan_date`, `review_date`.
