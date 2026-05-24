# Phase 10 — Audit & Confidence Score

## Goal

Cross-check every phase against every other phase. Compute a 0–100 confluence
score per `rubrics/confluence-scoring.md`. Log every contradiction. Spot-check
phase-9 citations. Emit `phase-10-audit.md`.

## Inputs

- All upstream phase MDs (phases 0–9, **including 7b and 8b**) from the current
  `<SYMBOL>/<DATE>` dir.
- `decision.json` (the structured envelope phase-9 emitted)
- `rubrics/confluence-scoring.md`
- `rubrics/citation-conventions.md`

## Steps

1. **Identify dominant bias.** Read phase-9's bias. That is the "thesis" the
   audit scores against.

2. **Score each upstream phase** (1, 2, 3, 4, 5, 6, 7, **7b**) as one of
   `++ / + / 0 / - / --` per `rubrics/confluence-scoring.md`. Write a
   one-sentence justification per phase quoting the most diagnostic datapoint.
   Phase-7b `VETO` is capped at `--` and must be called out as a fundamental
   veto; `NA` scores `0`.

3. **Score phase 8** as the agent-desk average: each non-MISSING agent
   contributes ±2 based on bias alignment with phase-9.

4. **Compute base_score and apply the phase-8b debate penalty** (−5 if
   `disconfirmed = true`) to get confluence_score (0–100), per
   `rubrics/confluence-scoring.md`.

5. **Map score to recommended conviction bin** per the table in
   `rubrics/confluence-scoring.md`. Compare to phase-9's actual bin.

5b. **Backfill + validate `decision.json`.** Write the final
   `confluence_score` and `recommended_bin` into the `decision.json` phase-9
   left as `null`, then re-validate:
   ```bash
   python3 schemas/validate_decision.py --file research/<SYMBOL>/<DATE>/decision.json
   ```
   A failed validation is a `## Sanity check` failure — report it; do not
   silently leave a broken envelope.

6. **Contradiction log.** For every phase scored `-` or `--`, write a
   `## Contradictions` entry with the conflict + a suggested resolution
   (downgrade / tighten invalidation / wait for confirmation).

7. **Citation spot-check.** Pick 3 citations from phase-9's thesis and
   confirm each resolves to a real datapoint in the cited phase. Failed
   citations go under `## Citation failures`.

8. **Sanity checks.**
   - Are all `phase-*.md` files present (including `phase-7b` and `phase-8b`)?
   - Does phase-9 cite ≥3 distinct upstream datapoints?
   - Is the conviction bin one of {0.55, 0.65, 0.75, 0.85, 0.95}?
   - Are at least 1 directional + 1 defined-risk structure present?
   - Is sizing math shown, and is Kelly `p` the phase-5 win-rate (or a
     justified bin fallback)?
   - Did every applicable risk gate (fundamentals / correlation / rotation /
     debate) get evaluated in phase-9's sizing block?
   - Does `decision.json` exist and pass `validate_decision.py`?

## Output sections

1. **Summary** — confluence score + recommended conviction bin vs actual +
   contradiction count.

2. **Confluence scorecard**

   | Phase | Score | Justification (quote a datapoint) |
   |-------|-------|-----------------------------------|
   | 1 — flow | + | "Net call premium $42M [FLOW:top_premium_trades]" |
   | 2 — dark pool | ++ | ... |
   | 3 — OI | 0 | ... |
   | 4 — structure | + | ... |
   | 5 — historical | + | ... |
   | 6 — macro | - | ... |
   | 7 — insights | ++ | ... |
   | 7b — fundamentals | + | "CONFIRM: beat-rate 7/8, MSPR +34 [FUND:mspr]" |
   | 8 — agents | + (4/5 align) | ... |

   **Raw score (symmetric):** N
   **Base score:** N/100
   **Debate penalty (phase-8b):** −5 if disconfirmed, else 0 (bull_res X vs bear_res Y)
   **Confluence_score:** N/100
   **Recommended bin:** 0.75
   **Phase-9 actual bin:** 0.75 (MATCH / MISMATCH)

3. **Contradictions** (one bullet per `-` or `--` phase).

4. **Citation failures** (empty if all 3 resolved).

5. **Sanity checks** (checklist with ✓/✗).

6. **Final auditor note** — 2 sentences. State whether the run is internally
   consistent and ready for action, or whether phase-9 should be revised.

## Forbidden moves

- Raising the score by ignoring contradictions.
- Re-running upstream phases to make them agree.
- Skipping the audit because phases 1–9 all agreed — write it anyway.

## Common pitfalls

- A `0` (neutral) score is usually under-used. If a phase is genuinely thin
  (e.g., phase-3 OI on a low-OI ticker), `0` is correct.
- Macro is often `0` or `-` for single-stock setups; don't penalize the
  thesis if macro is sector-neutral.
- A `--` score does NOT necessarily kill the thesis — it's a signal to
  tighten invalidation or downgrade conviction.
