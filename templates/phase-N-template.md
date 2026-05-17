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

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__<tool>` | `{symbol: NVDA, ...}` | {{1 line}} |

## Tool errors

{{Empty if none. Otherwise: tool name + args + exact error text.}}

## Verdict for downstream phases

- **Bias from this phase:** {{bullish / bearish / mixed / neutral}}
- **Conviction:** {{1-5}}
- **Three things later phases should remember:** {{numbered list}}
- **Open questions:** {{what this phase cannot answer alone}}
