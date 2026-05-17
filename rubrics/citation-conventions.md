# Citation Conventions

Every numeric claim in phase-9 and phase-10 MUST carry a citation tag that
resolves to a specific upstream phase + tool. Adapted from
`claude-trading-agents` PE-02.

## Tag taxonomy

| Tag | Source phase | Source tool family | Example |
|-----|--------------|--------------------|---------|
| `[FLOW:<tool>]`   | phase-1  | `options_flow_*`, `hot_chains_*` | `[FLOW:top_premium_trades]` |
| `[DP:<tool>]`     | phase-2  | `dark_pool_*` | `[DP:largest]` |
| `[OI:<tool>]`     | phase-3  | `oi_*` | `[OI:pin_risk]` |
| `[STRUCT:<tool>]` | phase-4  | `options_structure_*` | `[STRUCT:gex]` |
| `[HIST:<tool>]`   | phase-5  | `historical_*` | `[HIST:iv_percentile_zscore]` |
| `[MACRO:<series>]`| phase-6  | UW regime / FRED / WebSearch | `[MACRO:CPI_YoY_2026-05]` |
| `[INSIGHT:<tool>]`| phase-7  | `insights_*` | `[INSIGHT:conviction_matrix]` |
| `[AGENT:<name>]`  | phase-8  | sub-agent name | `[AGENT:sweep-tracker]` |

## Resolution rule

Each tag must resolve to a quotable line in the cited phase MD. A phase-10
auditor should be able to:

1. Open the cited phase MD.
2. Grep for the tool name (e.g. `top_premium_trades`).
3. Find a specific number that matches the claim in phase-9.

If a citation does not resolve, phase-10 must flag it under `## Citation
failures` and recommend removing the unbacked claim.

## Density target

- Phase-9 thesis paragraph: ≥3 distinct tags (M-04).
- Phase-9 entry/level/invalidation tables: every row tagged.
- Phase-9 macro overlay: every tailwind/headwind tagged.

## Forbidden

- `[FLOW:?]` or `[DP:unknown]` — if the source is unclear, the claim must be
  removed.
- Stale tags from a prior date — re-runs must re-cite from the current
  `<DATE>` directory.
- Aggregating multiple sources into a single tag — split into multiple tags
  instead.
