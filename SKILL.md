---
name: stock-deep-dive
description: End-to-end single-equity deep dive that synthesizes options flow, dark pool prints, dealer positioning, historical context, macro regime, and multi-agent analyst views into an actionable trade blueprint for a US-listed ticker. Use when the user asks for a deep dive, full workup, trade plan, or institutional-grade research on one specific stock or ETF.
---

# Stock Deep Dive

A multi-phase institutional research workflow (steps 0–10, plus a fundamentals
quality-veto `7b` and a bull/bear disconfirmation `8b`) that produces a
desk-PM-grade trade blueprint for a single US-listed ticker. Each phase writes
an immutable markdown artifact to
`research/<SYMBOL>/<YYYY-MM-DD>/phase-N-<topic>.md`, phase 9 also emits a
structured `decision.json`, and the final phase audits the chain for internal
contradiction. A separate `/deep-dive-calibration` command later marks those
blueprints to market.

## When to invoke

Trigger this skill when the user asks for any of:
- "deep dive on <TICKER>"
- "trade plan / blueprint / setup for <TICKER>"
- "institutional research on <TICKER>"
- "full workup on <TICKER>"
- "what would a PM do with <TICKER>"

Do NOT invoke for: portfolio-wide scans, sector screens, multi-ticker comparisons,
or pure backtests. Use `trade-analysis` instead for the 12-agent buy-side memo
flow if the user wants a CFA-style memo rather than a flow-driven blueprint.

## Inputs

- **Required:** one US-listed ticker (equity or ETF).
- **Optional:** as-of date (default = today). If supplied, all UW tool calls
  receive `date=<as-of>`. Never call live data when an as-of date is given.

## Output convention (MANDATORY)

```
research/<SYMBOL>/<YYYY-MM-DD>/
  phase-0-intake.md
  phase-1-flow.md
  phase-2-dark-pool.md
  phase-3-positioning.md
  phase-4-structure.md
  phase-5-historical.md
  phase-6-macro.md
  phase-7-insights.md
  phase-7b-fundamentals.md     deep fundamentals + quality veto (FINNHUB)
  phase-8-agent-views.md
  phase-8b-debate.md           bull vs bear disconfirmation
  phase-9-trade-plan.md
  decision.json                structured, machine-resolvable envelope
  phase-10-audit.md
```

**Immutability:** never overwrite an existing phase MD in the same
`<SYMBOL>/<DATE>` directory. If a re-run is requested for the same day, append
`-v2.md` (then `-v3.md`, etc.) and reference the prior version in the new file.

## Phase graph

| # | File | Source of truth | Detailed prompt |
|---|------|-----------------|-----------------|
| 0 | `phase-0-intake.md` | input validation + dir setup | `phases/phase-0-intake.md` |
| 1 | `phase-1-flow.md` | UW `options_flow_*` + `hot_chains_*` | `phases/phase-1-flow.md` |
| 2 | `phase-2-dark-pool.md` | UW `dark_pool_*` | `phases/phase-2-dark-pool.md` |
| 3 | `phase-3-positioning.md` | UW `oi_*` | `phases/phase-3-positioning.md` |
| 4 | `phase-4-structure.md` | UW `options_structure_*` | `phases/phase-4-structure.md` |
| 5 | `phase-5-historical.md` | UW `historical_*` (emits signal win-rate for sizing) | `phases/phase-5-historical.md` |
| 6 | `phase-6-macro.md` | UW `risk_market_regime` + `sector_flow_persistence` + `risk_portfolio_correlation` → FRED → WebSearch | `phases/phase-6-macro.md` |
| 7 | `phase-7-insights.md` | UW `insights_*` composite | `phases/phase-7-insights.md` |
| 7b | `phase-7b-fundamentals.md` | FINNHUB statements / surprise / peers / MSPR — quality veto | `phases/phase-7b-fundamentals.md` |
| 8 | `phase-8-agent-views.md` | 5 analyst sub-agents (parallel) | `phases/phase-8-agent-views.md` |
| 8b | `phase-8b-debate.md` | bull vs bear disconfirmation (1–2 rounds) | `phases/phase-8b-debate.md` |
| 9 | `phase-9-trade-plan.md` | PM-voice synthesis + `decision.json` | `phases/phase-9-trade-plan.md` |
| 10 | `phase-10-audit.md` | confluence score 0–100, backfills `decision.json` | `phases/phase-10-audit.md` |

Each phase MUST cite at least one prior phase by file path and quote at least
one specific datapoint from upstream output. Phase 9 must cite ≥3 distinct
upstream datapoints. Phase 10 must flag every internal contradiction.

**Phase 7b is a quality veto, phase 8b is a disconfirmation gate.** Both can
only *cut* conviction/size, never add it — they filter the flow, they don't
amplify it.

## Orchestration rules

1. **Sequential phases 0–7b**, then **parallel phase 8** (5 agents), then
   **phase 8b** (bull/bear debate), then sequential phases 9–10. Phase 7b runs
   after phase 7 so the desk agents (phase 8) and debate (phase 8b) can read
   the fundamental veto.
2. **Composite first.** Prefer `insights_*` / `playbook_*` tools over
   re-implementing confluence math from raw flow + DP + OI.
3. **Surface tool errors verbatim.** If a UW tool errors, write the failing
   call (tool name + args) + the error into the phase MD under a `## Tool
   errors` section. Do not mock or skip.
4. **No paid data.** If FRED or Finnhub requires a paid endpoint (or the key is
   unset), fall back gracefully — WebSearch+WebFetch for macro (phase-6),
   `tier_adjustment=NA` for fundamentals (phase-7b) — and label the source.
   Never abort the run for a missing optional key.
5. **Cite upstream phases by path**, e.g. `(see phase-1-flow.md §Sweeps)`.
6. **Use the template** at `templates/phase-N-template.md` for every phase
   MD's skeleton.

## Rubrics (load before phase 9 and 10)

- `rubrics/confluence-scoring.md` — 0-100 score formula for phase 10 (now
  includes phase-7b + the phase-8b debate penalty)
- `rubrics/invalidation-rubric.md` — what counts as thesis-broken
- `rubrics/sizing-rubric.md` — Kelly on the empirical phase-5 win-rate, with the
  fundamentals/correlation/rotation/debate risk gates
- `rubrics/citation-conventions.md` — `[FLOW:]`, `[DP:]`, `[OI:]`, `[STRUCT:]`,
  `[HIST:]`, `[MACRO:]`, `[INSIGHT:]`, `[FUND:]`, `[AGENT:<name>]`, `[DEBATE:]` tags

## Schemas & structured output

- `templates/decision-template.json` — the envelope phase-9 fills.
- `schemas/decision.schema.json` — its JSON Schema.
- `schemas/validate_decision.py` — stdlib-only validator (no pip installs);
  phase-9 must make it print `OK` before finishing.

## Calibration (the outcome loop)

`/deep-dive-calibration` (`commands/deep-dive-calibration.md`) is a separate,
on-demand command that marks past blueprints to market: it resolves
`research/*/*/decision.json` to WIN/LOSS path-aware (±1R via the invalidation
rubric), Brier-scores by phase-10 confluence band, and attributes hit-rate to
phases/tools. Run it periodically once enough dated blueprints exist — it is
what turns the confluence score from an assertion into a measured edge.

## Execution

Read each phase file in `phases/` in order and follow the embedded
instructions exactly. Each phase file is self-contained: tool list, output
template, validation checklist.

When invoked, the orchestrator should:

1. Read `phases/phase-0-intake.md` and execute it.
2. For each subsequent phase, read the file under `phases/` and execute.
3. After phase 10, surface the trade blueprint path + audit score to the user.

Disclaimer to include in every `phase-9-trade-plan.md`: *"For research and
educational use only. Not financial advice. Sizing and structures are
illustrative."*
