# Trade-Plan Eval Rubric

How to mark a taken plan to market and — more importantly — grade the
**reasoning** behind it, so the reasoning ledger improves. Outcome tells you if
the trade won; reasoning review tells you *why*, and whether the process was
sound even when the result was noise. A good plan can lose and a bad plan can
win — score both axes.

## 1. Outcome resolution (path-aware, ±1R)

Use `lib/mark_to_market.py` over the OHLC path from the plan date to the review
date. Resolution rules (mirror `/deep-dive-calibration`):

- **WIN** — first target reached before the stop, in chronological order.
- **LOSS** — stop reached before the first target.
- **OPEN** — neither hit yet and we're inside the horizon; mark to last close (R
  to-date), do not finalize the reasoning grade for an unresolved trade.
- **INCONCLUSIVE** — horizon elapsed with neither hit (chop), or data gap.

Record: `outcome`, `r_achieved`, `mfe_R` / `mae_R` (was the stop/target placed
where the path actually went?), `first_target_date`, `stop_hit_date`,
`invalidation_price_hit`.

Horizon→review windows (match the plan's `horizon`):
`intraday` same-day · `1-5d` 3D & 10D · `1-4w` 10D & 21D · `1-3m` 30D & 63D ·
`3-12m` 63D & 126D.

## 2. Reasoning review (the point of the loop)

Grade each reasoning component as `RIGHT` / `WRONG` / `UNRESOLVED`:

- **Direction call** — did price go the planned way (regardless of stop/target)?
- **Each reason_for** — did it materialize? (e.g. "ascending triangle breaks
  up" — did it?)
- **Each reason_against** — did the risk you named actually bite? A reason_against
  that fired and you still took full size is a sizing-process miss.
- **Pattern call** — did the detected pattern play out to its measured target,
  fail at its invalidation, or never confirm? Score the pattern engine too.
- **Flow↔chart agreement call** — was CONFLUENT/FLOW-LEADS/CHART-LEADS/DIVERGENT
  the right read in hindsight?
- **Level quality** — did the entry trigger, stop, and targets sit where price
  actually reacted? (Use `mfe_R`/`mae_R`: an `mae_R` near −1 then a win means the
  stop was nearly too tight; an `mfe_R` ≫ target reached means targets were too
  conservative.)

## 3. Calibration (Brier)

`brier = (conviction − outcome_bit)²`, where `outcome_bit = 1` for WIN, `0` for
LOSS (skip OPEN/INCONCLUSIVE). Track per conviction bin over time: a 0.75-bin
plan should win ~75% of the time. Persistent over-confidence (high bins losing)
→ a lesson to down-shift that setup's bin.

## 4. Sizing review

- Was `final_size_pct` justified by the realised edge? A LOSS at full size on a
  setup that the ledger already flagged is a process failure even if "the thesis
  was reasonable."
- Did any risk gate that *should* have fired get skipped? Did a gate fire that
  shouldn't have (cost an opportunity)?

## 5. Attribution

Assign the outcome to the most decisive lane(s): flow / dark-pool / positioning /
dealer-structure / historical / chart-trend / chart-pattern / macro /
fundamentals / sentiment. Over many evals this shows which lanes carry edge for
which setups — the empirical basis for re-weighting `direction-rubric.md`.

## 6. Lessons (propose-only, write to the ledger)

Translate findings into ledger lessons (`../../trade-plans/_eval/reasoning-ledger.md`):

- New, single-trade insight → `CANDIDATE` (cite the plan + outcome).
- Pattern seen in **≥2 marked trades** → promote to `ACTIVE` (cite both).
- A lesson contradicted by later trades → move to `## Retired` with the reason.
- Rubric/weight changes are **proposed**, never auto-applied — emit the exact
  edit (which rubric, which line, old→new) for the user to accept. This skill
  does not silently rewrite the generator's rubrics.

## Forbidden

- Grading reasoning as RIGHT just because the trade won (outcome ≠ process).
- Finalizing a reasoning grade on an OPEN trade.
- Auto-editing `direction-rubric.md` / `sizing-rubric.md` / `pattern-rubric.md`
  (propose only).
