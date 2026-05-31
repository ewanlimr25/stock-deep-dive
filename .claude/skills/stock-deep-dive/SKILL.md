---
name: stock-deep-dive
description: End-to-end single-equity deep dive that synthesizes options flow, dark pool prints, dealer positioning, historical context, macro regime, and multi-agent analyst views into an actionable trade blueprint for a US-listed ticker. Use when the user asks for a deep dive, full workup, trade plan, or institutional-grade research on one specific stock or ETF.
---

# Stock Deep Dive

A multi-phase institutional research workflow (steps 0–10, plus a cross-sectional
context pass `0.5`, a fundamentals quality-veto `7b`, a sentiment/positioning gate
`7c`, and a bull/bear disconfirmation `8b`) that produces a desk-PM-grade trade
blueprint for a single US-listed ticker. Each phase writes
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
- **Optional:** as-of date (default = today). If supplied, all UW commands
  receive `--date <as-of>` (where the flag exists). Never call live data when an
  as-of date is given.

## Output convention (MANDATORY)

```
research/<SYMBOL>/<YYYY-MM-DD>/
  phase-0-intake.md
  phase-0.5-context.md         cross-sectional + self-history context (CTX)
  phase-1-flow.md
  phase-2-dark-pool.md
  phase-3-positioning.md
  phase-4-structure.md
  phase-5-historical.md
  phase-6-macro.md
  phase-7-insights.md
  phase-7b-fundamentals.md     deep fundamentals + quality veto (FINNHUB)
  phase-7c-sentiment.md        sentiment + positioning + short interest gate
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
| 0 | `phase-0-intake.md` | input validation + dir setup + local-data probe | `phases/phase-0-intake.md` |
| 0.5 | `phase-0.5-context.md` | `uw screener` + `uw insights deep-dive` (universe/sector rank, self-history) → `[CTX:]` | `phases/phase-0.5-context.md` |
| 1 | `phase-1-flow.md` | `uw options-flow` + `uw hot-chains` + whole-tape aggregate (`uw insights deep-dive`) | `phases/phase-1-flow.md` |
| 2 | `phase-2-dark-pool.md` | `uw dark-pool` | `phases/phase-2-dark-pool.md` |
| 3 | `phase-3-positioning.md` | `uw oi` (incl. `oi-by-strike` walls + `term-structure` OPEX cliffs) | `phases/phase-3-positioning.md` |
| 4 | `phase-4-structure.md` | `uw options-structure` (incl. `max-pain` opex-gravity) | `phases/phase-4-structure.md` |
| 5 | `phase-5-historical.md` | `uw historical` (emits signal win-rate for sizing) | `phases/phase-5-historical.md` |
| 6 | `phase-6-macro.md` | `uw risk market-regime` + `options-flow sector-flow-persistence` + `risk portfolio-correlation` → FRED → WebSearch | `phases/phase-6-macro.md` |
| 7 | `phase-7-insights.md` | `uw insights` composite | `phases/phase-7-insights.md` |
| 7b | `phase-7b-fundamentals.md` | FINNHUB statements / surprise / peers / MSPR + `fz` peer-breadth / insider-clusters / analyst cross-source — quality veto | `phases/phase-7b-fundamentals.md` |
| 7c | `phase-7c-sentiment.md` | FINNHUB news/revisions + `fz` short interest / float (WebSearch fallback; borrow/HTB still WebSearch) + retail-vs-inst — positioning gate | `phases/phase-7c-sentiment.md` |
| 8 | `phase-8-agent-views.md` | 5 analyst sub-agents (parallel) | `phases/phase-8-agent-views.md` |
| 8b | `phase-8b-debate.md` | bull vs bear disconfirmation (1–2 rounds) | `phases/phase-8b-debate.md` |
| 9 | `phase-9-trade-plan.md` | PM-voice synthesis + `decision.json` | `phases/phase-9-trade-plan.md` |
| 10 | `phase-10-audit.md` | confluence score 0–100, backfills `decision.json` | `phases/phase-10-audit.md` |

Each phase MUST cite at least one prior phase by file path and quote at least
one specific datapoint from upstream output. Phase 9 must cite ≥3 distinct
upstream datapoints. Phase 10 must flag every internal contradiction.

**Phase 7b (fundamentals), phase 7c (sentiment/positioning), and phase 8b
(debate) are all downside-only gates.** Each can only *cut* conviction/size,
never add it — they filter the flow, they don't amplify it. **Phase 0.5 sets
context only** (no bias): it tells the later phases whether the flow is
genuinely unusual or a busy name's normal day.

## Orchestration rules

0. **Execution discipline — one phase at a time, run → read → write (CARDINAL).**
   Phases are sequential and data-dependent; the orchestrator MUST NOT race ahead.
   - Finish a phase completely — its tool calls AND its `phase-N-*.md` write — before
     issuing any tool call for the next phase.
   - **Within a phase: run the data command(s) → READ the actual returned values →
     THEN write the MD with those exact numbers.** Never put a phase-MD `Write`/`Edit`
     in the same tool batch as the command whose output it quotes. A number written
     before its source output has returned and been read is fabrication — full stop.
   - Batch tool calls in one message ONLY when every call is read-only AND mutually
     independent (e.g. a few `uw … --help` probes, or independent reads you will all
     inspect before writing anything). The **only** sanctioned parallel batch in this
     skill is phase 8's five sub-agents (independent read-only fan-out; you read all
     five verdicts before writing `phase-8-agent-views.md`).
   - The harness is **fail-fast**: if any call in a parallel batch errors, the
     remaining sibling calls are CANCELLED (`Cancelled: parallel tool call …`). Treat
     a cancelled batch as "nothing in it ran" — re-verify disk state (`ls` the
     research dir) before continuing, and never assume a cancelled `Write` persisted.
   (Hardened 2026-05-31 after a batched-write run pre-filled phase MDs with unread
   numbers; the harness cancellation is the only reason nothing false persisted.)
1. **Phase 0 → phase 0.5 → sequential phases 1–7c**, then **parallel phase 8**
   (5 agents), then **phase 8b** (bull/bear debate), then sequential phases
   9–10. Phase 0.5 runs right after intake so every later phase inherits the
   `[CTX:]` cross-sectional read. Phases 7b and 7c run after phase 7 so the desk
   agents (phase 8) and debate (phase 8b) can read both the fundamental veto and
   the positioning gate.
1b. **`uw` CLI first; DuckDB only for the inexpressible.** The `uw` CLI
   (`unusual-whales-pp-cli`, on `PATH` as `uw`) reads the same `~/Documents/Stocks`
   parquet the skill could query directly, so the CLI is the default for every
   read. Every call emits JSON with `--json` and may narrow output with `--select`.
   Drop to the DuckDB escape hatch (`lib/duckdb-cuts.md`) ONLY for the three cuts
   the CLI can't express (custom aggregations, cross-dataset timestamp joins,
   full-universe/long self-history percentiles) and tag those datapoints
   `[… DUCKDB]`. Never re-implement a `uw` command. The CLI is the same engine the
   old `uw-pp` MCP wrapped (output is bit-identical), so the MCP is deprecated.
   (See `docs/audit/2026-05-25/06` and `docs/audit/2026-05-27/uw-cli-migration`.)
1c. **`fz` for fundamentals/SI/float/peer/breadth only.** The `fz` (Finviz) CLI
   (`lib/fz-recipes.md`) supplies the short-interest / float / peer-breadth /
   sector-breadth data neither the `uw` CLI nor Finnhub carries cleanly. It is a Bash
   CLI like the `curl`/Finnhub calls — used in phases 7c/7b (gates), 2/3 (float
   normalization, advisory), 6 (breadth overlay, advisory), and 0/5/9 (price
   context, advisory). It has **no** flow/greeks/dark-pool/GEX/OI and touches none
   of phases 1–5 as a source. Every `fz` contribution is **downside-only or
   advisory** — it can cut/veto or color, never inflate conviction, and never
   enters the Kelly `p`. Tag `fz` datapoints with the ` fz` source qualifier
   (`rubrics/citation-conventions.md`). Graceful-skip to WebSearch/Finnhub if `fz`
   is absent. (See `docs/audit/2026-05-27`.)
2. **Composite first.** Prefer `uw insights` / `uw playbook` commands over
   re-implementing confluence math from raw flow + DP + OI.
3. **Surface tool errors verbatim.** If a `uw` command errors, write the failing
   command line + the error into the phase MD under a `## Tool errors` section.
   Do not mock or skip.
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
  five downside-only risk gates (fundamentals / **sentiment** / correlation /
  rotation / debate) and the phase-0.5 context modifier
- `rubrics/citation-conventions.md` — `[FLOW:]`, `[DP:]`, `[OI:]`, `[STRUCT:]`,
  `[HIST:]`, `[MACRO:]`, `[INSIGHT:]`, `[FUND:]`, `[SENT:]`, `[CTX:]`,
  `[AGENT:<name>]`, `[DEBATE:]` tags (+ ` DUCKDB` source qualifier for escape-hatch cuts)

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

**Process one phase fully before starting the next** (see Orchestration rule 0).
Each phase is a strict three-step cycle — do not collapse or pipeline these:

1. **READ** the `phases/phase-N-*.md` instructions.
2. **RUN** that phase's data commands and **READ the actual output** (foreground;
   wait for results). Surface any tool error verbatim per rule 3.
3. **WRITE** `research/<SYMBOL>/<DATE>/phase-N-*.md` using the values you just read —
   never values you expect to get. Then, and only then, move to phase N+1.

Do not pre-write a phase MD, do not batch a phase's `Write` with its data commands,
and do not start phase N+1's tool calls until phase N's MD is on disk. The single
exception is phase 8 (five independent sub-agents fanned out in one message, then all
verdicts read before the MD is written).

When invoked, the orchestrator should:

1. Read `phases/phase-0-intake.md` and execute the READ→RUN→WRITE cycle.
2. For each subsequent phase, repeat the cycle — one phase at a time, in order.
3. After phase 10, surface the trade blueprint path + audit score to the user.

Disclaimer to include in every `phase-9-trade-plan.md`: *"For research and
educational use only. Not financial advice. Sizing and structures are
illustrative."*
