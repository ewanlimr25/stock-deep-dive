# Phase E3 — Lessons & Ledger Update (improve the reasoning model)

## Goal

Turn the reasoning review into durable, reusable corrections: append lessons to
the reasoning ledger and propose (never auto-apply) rubric/weight edits. This is
the mechanism by which recommendations improve after a real trade (goal #6).

## Inputs

- `reasoning_review` + `calibration` + `attribution` from E2,
- the current ledger `../../../trade-plans/_eval/reasoning-ledger.md`
  (path from repo root: `trade-plans/_eval/reasoning-ledger.md`),
- `rubrics/eval-rubric.md` §6.

## Steps

1. **Derive 1–3 lessons** from the WRONG verdicts and the calibration/attribution
   findings. Each lesson is an imperative correction scoped with tags
   (`ticker:` / `sector:` / `setup:` / `pattern:` / `regime:`) and an
   `applies_to` (which phase/rubric step it should change). Prefer specific,
   testable lessons over platitudes.

2. **Assign the next id** `L-####` (scan the ledger for the max). New lessons
   start `CANDIDATE`.

3. **Promote / retire:**
   - If a CANDIDATE lesson's pattern now has **≥2 marked trades** supporting it,
     promote to `ACTIVE` and cite both plan paths.
   - If a later trade contradicts an ACTIVE lesson, move it to `## Retired` with
     the contradicting evidence. Never silently delete.

4. **Append to the ledger** in the exact lesson format (status, scope, lesson,
   evidence with plan paths + outcomes, applies_to, added date). Read the file,
   add the entries under "Active & candidate lessons" (or "Retired"), and write
   it back — do not clobber existing lessons.

5. **Propose rubric edits (propose-only).** If a finding implies a generator
   change (e.g. soften a conviction modifier, re-weight a lane, tighten a pattern
   tolerance), emit it as a `proposed_rubric_edits[]` entry: `{file, change,
   rationale}`. Do **not** edit `direction-rubric.md` / `sizing-rubric.md` /
   `pattern-rubric.md` yourself — surface the diff for the user to accept.

## Emit & validate the eval JSON

Write `trade-plans/<SYMBOL>/<PLAN_DATE>/eval-<REVIEW_DATE>.json` from
`templates/eval.json`, then:
```bash
python3 .claude/skills/trade-plan-eval/schemas/validate_eval.py \
    --file trade-plans/<SYMBOL>/<PLAN_DATE>/eval-<REVIEW_DATE>.json
```
Fix and re-run until `OK`. Also write the human-readable
`eval-<REVIEW_DATE>.md` from `templates/eval.md`.

## Surface to the user

Print: the outcome (status + R), the calibration verdict, the 1-line takeaway,
the lesson ids added/promoted, and any proposed rubric edits awaiting their
decision.
