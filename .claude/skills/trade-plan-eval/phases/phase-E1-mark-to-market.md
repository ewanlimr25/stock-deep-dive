# Phase E1 — Mark to Market (path-aware outcome)

## Goal

Resolve what actually happened to the trade, path-aware, using the underlying's
OHLC from the plan date to the review date. Outcome only — reasoning grading is
E2.

## Steps

1. **Run the deterministic marker** (foreground; read the JSON):
   ```bash
   python3 .claude/skills/trade-plan-eval/lib/mark_to_market.py \
       --ticker <SYMBOL> --plan-date <PLAN_DATE> --review-date <REVIEW_DATE> \
       --direction <long|short> --entry <entry> --stop <stop> \
       --targets <t1,t2,...> [--invalidation <inval_price>]
   ```
   It returns `outcome` (WIN/LOSS/OPEN), `r_achieved`, `mfe_R`, `mae_R`,
   `first_target_date`, `stop_hit_date`, `invalidation_price_hit`, and the
   per-target hit dates — walking the path in chronological order (stop checked
   conservatively first within a bar; ±1R convention).

2. **Apply the rubric's resolution rules** (`rubrics/eval-rubric.md` §1):
   - WIN = first target before stop; LOSS = stop before first target;
   - OPEN = neither yet inside the horizon (mark to last close);
   - INCONCLUSIVE = horizon elapsed with neither, or a data gap.
   - Use the horizon→window table to decide whether the trade is even resolvable
     yet. **Do not finalize a reasoning grade on an OPEN trade** (E2 stays
     UNRESOLVED).

3. **For an options trade**, the underlying mark sets the outcome, but also note
   whether the structure would have paid (did the underlying clear the
   `target_price` before the `expiry`? did it breach the breakeven? was theta/IV
   a factor near `target_date`?). Record this as color in the eval MD.

## Write the outcome block into the eval MD draft

`status`, `r_achieved`, `mfe_R`/`mae_R` (these feed the level-quality grade in
E2), the hit/stop dates, and the options-structure color.

## Verdict for downstream

- the `outcome` object for the eval JSON + E2's calibration math.
