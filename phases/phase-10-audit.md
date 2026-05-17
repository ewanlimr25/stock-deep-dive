# Phase 10 — Audit & Confidence Score

## Goal

Cross-check every phase against every other phase. Compute a 0–100 confluence
score per `rubrics/confluence-scoring.md`. Log every contradiction. Spot-check
phase-9 citations. Emit `phase-10-audit.md`.

## Inputs

- All upstream phase MDs (phases 0–9) from the current `<SYMBOL>/<DATE>` dir.
- `rubrics/confluence-scoring.md`
- `rubrics/citation-conventions.md`

## Steps

1. **Identify dominant bias.** Read phase-9's bias. That is the "thesis" the
   audit scores against.

2. **Score each upstream phase** as one of `++ / + / 0 / - / --` per
   `rubrics/confluence-scoring.md`. Write a one-sentence justification per
   phase quoting the most diagnostic datapoint from that phase.

3. **Score phase 8** as the agent-desk average: each non-MISSING agent
   contributes ±2 based on bias alignment with phase-9.

4. **Compute raw score and confluence_score** (0–100).

5. **Map score to recommended conviction bin** per the table in
   `rubrics/confluence-scoring.md`. Compare to phase-9's actual bin.

6. **Contradiction log.** For every phase scored `-` or `--`, write a
   `## Contradictions` entry with the conflict + a suggested resolution
   (downgrade / tighten invalidation / wait for confirmation).

7. **Citation spot-check.** Pick 3 citations from phase-9's thesis and
   confirm each resolves to a real datapoint in the cited phase. Failed
   citations go under `## Citation failures`.

8. **Sanity checks.**
   - Are all `phase-*.md` files present in the dir?
   - Does phase-9 cite ≥3 distinct upstream datapoints?
   - Is the conviction bin one of {0.55, 0.65, 0.75, 0.85, 0.95}?
   - Are at least 1 directional + 1 defined-risk structure present?
   - Is sizing math shown?

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
   | 8 — agents | + (4/5 align) | ... |

   **Raw score:** N
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
