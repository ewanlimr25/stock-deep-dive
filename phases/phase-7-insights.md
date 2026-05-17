# Phase 7 — UW Insights Confluence

## Goal

Run UW's composite insight tools — these already do confluence math and
scenario classification. This phase is a single point of consolidation; it
should AGREE with phases 1–5 if the run is internally consistent, and
DISAGREE only when one of the upstream phases was thin or wrong. Emit
`phase-7-insights.md`.

## Tools (all `symbol=<SYMBOL>`-scoped)

| Tool | When | What it returns |
|------|------|-----------------|
| `mcp__uw-pp__insights_deep_dive` | always | Full 360° (fundamentals + options + dp + oi) |
| `mcp__uw-pp__insights_signal_confluence` | always | 0–6 factor score + factor list |
| `mcp__uw-pp__insights_conviction_matrix` | always | Scenario classification |
| `mcp__uw-pp__insights_price_vs_flow` | always | Divergence (reversal signal) |
| `mcp__uw-pp__insights_analyst_vs_flow` | always | Wall Street vs options-trader agreement |
| `mcp__uw-pp__insights_institutional_accumulation` | always | Accumulation / distribution / neutral |
| `mcp__uw-pp__insights_earnings_play` | only if earnings within 30d (from phase-6 calendar) | IV + OI buildup setup |

## Composition guidance

- `insights_signal_confluence` is MARKET-WIDE; filter for `<SYMBOL>` in the
  returned list. If `<SYMBOL>` is not in the result, it means the score is
  below `min_score` (default 3). Re-call with `min_score=1` to confirm.
- `insights_deep_dive` calls Yahoo — may be slower (5–10s) and rate-limited.
  Tolerate retries.

## Output sections

1. **Summary** — composite verdict from UW (one paragraph).
2. **Key signals** — top-5 with `[INSIGHT:<tool>]` citations.
3. **Detailed findings**
   - ### Deep dive snapshot (PE, market cap, short %, IV rank, key options
     metrics, dark pool premium, OI signature)
   - ### Signal confluence (score, list of contributing factors)
   - ### Conviction matrix (scenario: DIRECTIONAL_LONG / HEDGED_LONG /
     COVERED_CALL / DIRECTIONAL_SHORT / MIXED — with reasoning)
   - ### Price vs flow (divergence yes/no, direction)
   - ### Analyst vs flow (consensus, options-trader signal, agreement?)
   - ### Institutional accumulation (signal, buy/sell vol, net)
   - ### Earnings play (only if in-window — IV rank + OI buildup + days to
     earnings)
4. **Tool calls** — audit.
5. **Tool errors** — verbatim.
6. **Cross-check vs phases 1–5**

   | UW insight | Phase agreement? | Notes |
   |------------|------------------|-------|
   | signal_confluence | phases 1-3 agree / disagree | ... |
   | conviction_matrix | phase 2 (DP) agrees / disagrees | ... |
   | institutional_accumulation | phase 2 (DP) agrees / disagrees | ... |

7. **Verdict for downstream**
   - UW composite bias
   - Conviction 1–5
   - Phase 9 should treat this as the BASELINE and only override with
     specific contrary evidence from phases 1–8
   - Open questions

## Interpretation heuristics

- **Signal confluence ≥ 5** is rare and high-conviction.
- **Conviction matrix = DIRECTIONAL_LONG** + **institutional_accumulation =
  ACCUMULATION** + **price_vs_flow = no divergence** → strongest possible
  bullish stack on this skill's instrumentation.
- **HEDGED_LONG** means bullish options flow + bearish dark pool → suggests
  long-stock holders buying protection, NOT directional new long. Read
  carefully.
- **price_vs_flow divergence** (bearish flow + rising price OR bullish flow +
  falling price) is a leading reversal signal but often early — pair with
  phase-4 dealer regime before sizing on it.

## Common pitfalls

- `insights_deep_dive` Yahoo fundamentals can be 1–2 quarters stale on
  smaller names.
- `insights_analyst_vs_flow` consensus is yfinance — may not reflect very
  recent rating changes.
- `insights_earnings_play` errors if no earnings date is found in the
  screener; that's not a true error, just "out of window".
