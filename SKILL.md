---
name: stock-deep-dive
description: End-to-end single-equity deep dive that synthesizes options flow, dark pool prints, dealer positioning, historical context, macro regime, and multi-agent analyst views into an actionable trade blueprint for a US-listed ticker. Use when the user asks for a deep dive, full workup, trade plan, or institutional-grade research on one specific stock or ETF.
---

# Stock Deep Dive

A 10-phase institutional research workflow that produces a desk-PM-grade trade
blueprint for a single US-listed ticker. Each phase writes an immutable
markdown artifact to `research/<SYMBOL>/<YYYY-MM-DD>/phase-N-<topic>.md` and
the final phase audits the chain for internal contradiction.

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
  phase-8-agent-views.md
  phase-9-trade-plan.md
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
| 5 | `phase-5-historical.md` | UW `historical_*` | `phases/phase-5-historical.md` |
| 6 | `phase-6-macro.md` | UW `risk_market_regime` → FRED-free → WebSearch | `phases/phase-6-macro.md` |
| 7 | `phase-7-insights.md` | UW `insights_*` composite | `phases/phase-7-insights.md` |
| 8 | `phase-8-agent-views.md` | 5 analyst sub-agents (parallel) | `phases/phase-8-agent-views.md` |
| 9 | `phase-9-trade-plan.md` | PM-voice synthesis | `phases/phase-9-trade-plan.md` |
| 10 | `phase-10-audit.md` | confluence score 0–100 | `phases/phase-10-audit.md` |

Each phase MUST cite at least one prior phase by file path and quote at least
one specific datapoint from upstream output. Phase 9 must cite ≥3 distinct
upstream datapoints. Phase 10 must flag every internal contradiction.

## Orchestration rules

1. **Sequential phases 0–7**, then **parallel phase 8** (5 agents), then
   sequential phases 9–10.
2. **Composite first.** Prefer `insights_*` / `playbook_*` tools over
   re-implementing confluence math from raw flow + DP + OI.
3. **Surface tool errors verbatim.** If a UW tool errors, write the failing
   call (tool name + args) + the error into the phase MD under a `## Tool
   errors` section. Do not mock or skip.
4. **No paid data.** If FRED requires a paid endpoint, fall back to WebSearch
   + WebFetch and label the source in phase-6.
5. **Cite upstream phases by path**, e.g. `(see phase-1-flow.md §Sweeps)`.
6. **Use the template** at `templates/phase-N-template.md` for every phase
   MD's skeleton.

## Rubrics (load before phase 9 and 10)

- `rubrics/confluence-scoring.md` — 0-100 score formula for phase 10
- `rubrics/invalidation-rubric.md` — what counts as thesis-broken
- `rubrics/sizing-rubric.md` — Kelly-derived sizing with deviation escape hatch
- `rubrics/citation-conventions.md` — `[FLOW:]`, `[DP:]`, `[OI:]`, `[STRUCT:]`,
  `[HIST:]`, `[MACRO:]`, `[AGENT:<name>]` tags

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
