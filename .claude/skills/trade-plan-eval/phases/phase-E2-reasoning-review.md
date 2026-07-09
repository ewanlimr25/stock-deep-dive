# Phase E2 — Reasoning Review (the point of the loop)

## Goal

Grade the *reasoning* behind the plan, not just the result. A winning trade can
have broken process and a losing trade can have sound process — score both so the
ledger learns the right thing. Skip finalization if E1 returned OPEN.

## Inputs

- the plan (`reasons_for`, `reasons_against`, `patterns`, `levels`, flow↔chart
  agreement, `sizing`, `conviction`),
- the E1 outcome (`status`, `r_achieved`, `mfe_R`, `mae_R`, hit dates),
- forward chart for context: re-run `chart_engine.py --date <REVIEW_DATE>` to see
  what structure/pattern actually did,
- `rubrics/eval-rubric.md` §2–§5.

## Steps

1. **Direction call** — did the underlying move the planned way (regardless of
   stop/target)? RIGHT / WRONG / UNRESOLVED.

2. **Grade each reason** (`reasons_for` + `reasons_against`) RIGHT/WRONG/UNRESOLVED
   with a one-line note citing what happened. A `reason_against` that fired and
   you still sized full is a sizing-process miss — capture it.

3. **Pattern call** — PLAYED_OUT (hit measured target) / FAILED (hit
   invalidation) / UNCONFIRMED (never triggered) / NA. Grade the chart engine's
   read too, so low-quality detectors can be tuned.

4. **Flow↔chart agreement call** — was CONFLUENT/FLOW-LEADS/CHART-LEADS/DIVERGENT
   the right read in hindsight?

5. **Level quality** — use `mfe_R`/`mae_R`: `mae_R` ≈ −1 before a win ⇒ stop
   nearly too tight; `mfe_R` ≫ the target hit ⇒ targets too conservative; a stop
   blown with low `mfe_R` ⇒ entry/level was wrong. Pick the rubric label.

6. **Sizing review** — APPROPRIATE / OVERSIZED / UNDERSIZED given the realised
   edge and which gates did/didn't fire.

7. **Calibration (Brier)** — for WIN/LOSS only:
   `outcome_bit = 1 if WIN else 0`; `brier = (conviction − outcome_bit)²`.
   Verdict: OVERCONFIDENT if a high bin lost / UNDERCONFIDENT if a low bin won /
   WELL_CALIBRATED otherwise. (Aggregate meaning emerges over many evals.)

8. **Attribution** — list the lanes (flow / dark_pool / positioning /
   dealer_structure / historical / chart_trend / chart_pattern / macro /
   fundamentals / sentiment) and tag each `decisive_right` / `decisive_wrong` /
   `minor` / `neutral`. This is the empirical basis for re-weighting the
   direction rubric.

## Write the reasoning-review + calibration + attribution blocks

into the eval MD draft and the eval JSON.

## Verdict for downstream

- `reasoning_review`, `calibration`, `attribution` objects → E3 turns these into
  ledger lessons.
