# Phase 8 — Multi-Agent Analyst Desk (parallel)

## Goal

Spawn five specialist sub-agents IN PARALLEL, each with the same packed
context (phases 1–7), and collect structured verdicts. Emit
`phase-8-agent-views.md`.

## Agents

Launch all five in a single message via the Agent tool, using these
`subagent_type` values:

| subagent_type | Role |
|---------------|------|
| `accumulation-hunter` | Quiet institutional accumulation detector |
| `contrarian-scanner`  | Crowded-trade / fade opportunities |
| `sweep-tracker`       | Aggressive sweep + momentum |
| `earnings-scout`      | Pre-earnings positioning (skip if earnings > 30d out) |
| `risk-monitor`        | Correlation + regime + portfolio risk |

**If an agent type is unavailable on the user's machine**, write a
`MISSING: <agent_name>` line in that agent's section and proceed with the
remaining four. Do NOT abort the phase.

## Per-agent prompt template

Each agent receives the SAME packed context:

```
You are <ROLE> on a desk doing a deep dive on <SYMBOL> as of <AS-OF>.

Below is the research already gathered. Read it, then return a structured
verdict.

=== PHASE 1: OPTIONS FLOW (phase-1-flow.md) ===
<full contents>

=== PHASE 2: DARK POOL (phase-2-dark-pool.md) ===
<full contents>

=== PHASE 3: OI POSITIONING (phase-3-positioning.md) ===
<full contents>

=== PHASE 4: DEALER STRUCTURE (phase-4-structure.md) ===
<full contents>

=== PHASE 5: HISTORICAL (phase-5-historical.md) ===
<full contents>

=== PHASE 6: MACRO (phase-6-macro.md) ===
<full contents>

=== PHASE 7: UW INSIGHTS (phase-7-insights.md) ===
<full contents>

=== PHASE 7b: DEEP FUNDAMENTALS (phase-7b-fundamentals.md) ===
<full contents — includes the fundamental_signal + tier_adjustment veto>

=== PHASE 7c: SENTIMENT & POSITIONING (phase-7c-sentiment.md) ===
<full contents — includes sentiment_signal, crowd_state, short interest, tier_adjustment>

=== END CONTEXT ===

You may call additional UW MCP tools if and only if you need a specific
datapoint not present above. Do not duplicate work.

Return ONLY the following structured verdict (no preamble, no closing remarks):

VERDICT
- bias: LONG | SHORT | NEUTRAL | RANGE
- conviction: 1 | 2 | 3 | 4 | 5
- horizon: intraday | 1-5d | 1-4w | 1-3m
- key_levels:
    support: <price>
    resistance: <price>
    invalidation: <price-or-condition>
- top_signal: <one sentence citing a specific phase + datapoint>
- top_risk: <one sentence>
- one_line_take: <≤25 words in your role's voice>
```

(Tools listed for the parent orchestrator: `Agent` with the five
`subagent_type` values above, plus all `mcp__uw-pp__*` tools the sub-agent
might need.)

## Output sections (parent assembles after agents return)

1. **Summary** — net agent verdict: how many bullish / bearish / neutral /
   range, conviction distribution.
2. **Agent verdicts table**

   | Agent | bias | conviction | horizon | one_line_take |
   |-------|------|-----------|---------|---------------|
   | accumulation-hunter | ... | ... | ... | ... |
   | ...   | ... | ... | ... | ... |

3. **Per-agent details** (subsection per agent with the full verdict block)
4. **Disagreements** — list any agent that takes the opposite bias from the
   majority, with their top_signal quoted.
5. **Tool errors** — including any `MISSING: <agent>` lines.
6. **Verdict for downstream**
   - Plurality bias + count
   - Average conviction across non-MISSING agents
   - Three highest-quality signals across all agents (top_signal text + tag)
   - Open questions surfaced by agents

## Interpretation heuristics

- **5-of-5 agreement**: high alignment → support 0.75–0.85 conviction in
  phase-9 IF phases 1–7 also align.
- **4-of-5 with one strong dissent**: read the dissent's top_signal carefully
  — often it's the missing piece.
- **Split 3-2**: treat as MIXED; phase-9 should target 0.55–0.65 conviction
  and use a defined-risk structure.
- **risk-monitor flags HIGH correlation** with another active book position:
  phase-9 must call this out in sizing. risk-monitor should read phase-6's
  `risk_portfolio_correlation` and `sector_flow_persistence` verdicts (and may
  re-call those `mcp__uw-pp__risk_*` / `options_flow_sector_flow_persistence`
  tools for a fresh read) — a ≥0.70 cluster with another open blueprint, or an
  adverse sector rotation, is a size-cut the desk must see.

## Common pitfalls

- Sub-agents may try to call expensive tools repeatedly. The phase budget is
  about 30 UW calls total across all five agents.
- Sub-agents may re-derive the same conclusion already in phase-7 — that's
  OK and counts as confirmation.
