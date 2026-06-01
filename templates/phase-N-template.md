# Phase {{N}} — {{TOPIC}}

**Ticker:** {{SYMBOL}}
**As-of date:** {{YYYY-MM-DD}}
**Generated:** {{ISO-8601 timestamp}}
**Upstream phases cited:** {{phase-X.md, phase-Y.md, ...}}

## Summary

{{2-4 sentences. What did this phase find? Lead with the headline.}}

## Key signals

- {{bullet 1 with tagged citation, e.g. "Net call premium $42M [FLOW:top_premium_trades]"}}
- {{bullet 2}}
- {{bullet 3}}

## Detailed findings

### {{Subsection A — usually one per major tool group}}

{{Tables, numbers, regime classifications. Always quote the exact UW field
name and value, never paraphrase a number.}}

### {{Subsection B}}

...

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|------------------|--------------------------|-----------|
| `uw <group> <leaf> --symbol NVDA … --json` | {{e.g. net_flow=+$1.2M ← `.uw_screener.bullish_premium - .uw_screener.bearish_premium`}} | {{whole-tape / top-N}} |

## Tool errors

{{Empty if none. Otherwise: tool name + args + exact error text.}}

## DATA NOTE / CORRECTION

{{Empty if the first read stood. If any value here was re-read or corrected after
the first draft (e.g. under a slow/degraded harness), record: the field, the wrong
value, the corrected value, and the `jq` path it was re-verified against.}}

## Verdict for downstream phases

- **Bias from this phase:** {{bullish / bearish / mixed / neutral}}
- **Conviction:** {{1-5}}
- **Three things later phases should remember:** {{numbered list}}
- **Open questions:** {{what this phase cannot answer alone}}
