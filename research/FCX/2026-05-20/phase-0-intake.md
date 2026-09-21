# Phase 0 — Intake

**Ticker:** FCX
**As-of date:** 2026-05-20 (requested) / **effective data date:** 2026-05-19 (latest available parquet)
**Output dir:** `/Users/ewan/Development/stock-deep-dive/research/FCX/2026-05-20/`
**Version:** v1
**Generated:** 2026-05-20T19:23:00-04:00
**Upstream phases cited:** (none — root phase)

## Summary

Ticker validated (FCX = Freeport-McMoRan, NYSE-listed copper/gold miner). Output
directory created clean (v1). UW MCP reachable; the only catch is that the run
date (2026-05-20) has no parquet built yet — latest available across all data
families is **2026-05-19**. All downstream phases will pass `date=2026-05-19`
to UW tools and treat that as the effective as-of. The output directory keeps
the requested `2026-05-20` name to honour the user's invocation.

Ticker sanity check returned a single unusual-volume put (58P, Jun-2026, 14.2x
vol/OI) — confirms FCX has live options activity. Proceeding to phase 1.

## Key signals

- Effective data date: **2026-05-19** (all 5 data families align) [DP/OI/FLOW/HIST/SCREENER]
- FCX has at least one screen-worthy unusual print already — 58P 2026-06-18,
  $272k premium, vol/OI 14.2x [FLOW:options_flow_unusual_volume]
- Implied vol (avg_iv on that print) ≈ 50% — elevated for a large-cap miner;
  flags either a known catalyst or stress in the copper complex (verify in
  phase 5/6)

## UW availability

- `historical_available_dates`: **ok**
- Latest available options date: **2026-05-19**
- Latest available darkpool date: **2026-05-19**
- Latest available OI date: **2026-05-19**
- Latest available hotchains date: **2026-05-19**
- Latest available screener date: **2026-05-19**
- Note: data archive has a gap between **2026-03-27 → 2026-04-27** (no parquet
  for those weeks). Phase 5 historical lookbacks must handle this gap (likely
  a data-feed pause, not a market holiday — too long a window).

## Ticker sanity

- Options activity (unusual_volume top 1 @ 2026-05-19):
  - Contract: FCX 58P 2026-06-18
  - Total volume: 866 vs OI 61 → **vol/OI 14.2x**
  - Total premium: $272,105
  - Trade count: 29
  - Avg IV: 49.99%
  - Source parquet: `bot-eod-report-2026-05-19.parquet`

## Prior versions

(none — v1)

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__historical_available_dates` | `{}` | 5 families, latest 2026-05-19, gap 2026-03-27→2026-04-27 |
| `mcp__uw-pp__options_flow_unusual_volume` | `{symbol: FCX, top_n: 1, date: 2026-05-20}` | **error: no parquet for 2026-05-20** |
| `mcp__uw-pp__options_flow_unusual_volume` | `{symbol: FCX, top_n: 1, date: 2026-05-19}` | 1 hit: 58P Jun-2026, 14.2x vol/OI |

## Tool errors

```
mcp__uw-pp__options_flow_unusual_volume (date=2026-05-20):
Error: no parquet file for 2026-05-20 in /Users/ewan/Documents/Stocks/All Options
```

**Resolution:** rebase effective data date to 2026-05-19 (latest available);
keep output dir as `2026-05-20/` per user request.

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake only — no thesis yet)
- **Conviction:** 1 (procedural)
- **Three things later phases should remember:**
  1. **Always pass `date=2026-05-19`** to UW tools, never `2026-05-20`.
  2. There is a **data archive gap 2026-03-27 → 2026-04-27** — historical
     lookbacks of 30 trading days won't cover a true 30-session window.
  3. Even on a low-key ticker like FCX, the very first unusual-vol print is a
     **bearish put with 50% IV** — phase 1 should investigate whether this is
     hedging or directional, and phase 5 should check IV percentile.
- **Open questions:** Is the 58P print directional or part of a
  put-spread/collar? Is the 50% IV elevated vs FCX's own history? Is there a
  known catalyst (earnings, copper price event, China data) in the next
  4 weeks?
