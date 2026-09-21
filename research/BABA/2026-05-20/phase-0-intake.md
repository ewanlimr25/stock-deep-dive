# Phase 0 — Intake

**Ticker:** BABA
**As-of date:** 2026-05-20
**Data date used (UW cutoff):** 2026-05-19
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/BABA/2026-05-20/
**Version:** v1
**Generated:** 2026-05-20T00:00:00Z
**Upstream phases cited:** (none — this is the first phase)

## Summary

BABA validated as a US-listed NYSE equity with active options (calls trading at $139
strike June expiry with 202x vol/OI). UW MCP reachable. Latest available data is
2026-05-19; the user's `--as-of 2026-05-20` is one trading day ahead of available
parquet snapshots, so all downstream UW calls in this run will use
`date=2026-05-19`. Output directory created; this is a v1 run. Proceeding to phase 1.

## Key signals

- UW data extends through 2026-05-19 across all five families (darkpool, hotchains,
  oi, options, screener); 2026-05-20 (today) is not yet loaded.
- BABA options active: unusual-volume scan returned a 139 strike June call with
  total premium $195,381 and vol/OI = 202 — confirms tradeable activity for the
  remainder of the deep dive.

## Detailed findings

### Input validation

- Ticker `BABA`: valid 4-character uppercase symbol; Alibaba Group Holding Ltd ADR,
  NYSE-listed.
- As-of date `2026-05-20`: parsed as ISO date. Note: today's parquet not yet
  loaded; the run will use **2026-05-19** as the effective UW data date and
  document this carry-back at every phase header.

### Directory & versioning

- Created: `research/BABA/2026-05-20/`
- Pre-existing files in dir: none → this is **v1**.
- All phase artifacts will be written as `phase-N-<topic>.md` (no version suffix).

### UW MCP availability

- `historical_available_dates`: OK.
- Latest available darkpool date: **2026-05-19**
- Latest available options date: **2026-05-19**
- Latest available OI date: **2026-05-19**
- Latest available hotchains date: **2026-05-19**
- Latest available screener date: **2026-05-19**

### Ticker sanity (BABA on 2026-05-19)

- `options_flow_unusual_volume` top-1 result:
  - Contract: BABA 2026-06-18 $139 Call
  - `total_premium`: $195,381
  - `total_volume`: 404
  - `open_interest`: 2
  - `vol_oi_ratio`: 202
  - `avg_iv`: 0.403 (40.3%)
- Conclusion: active options market, new-money positioning visible in mid-DTE
  upside calls. Proceed.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__historical_available_dates` | `{}` | OK — latest 2026-05-19 across all families |
| `mcp__uw-pp__options_flow_unusual_volume` | `{symbol: BABA, top_n: 1, date: 2026-05-20}` | ERROR — no parquet for 2026-05-20 |
| `mcp__uw-pp__options_flow_unusual_volume` | `{symbol: BABA, top_n: 1, date: 2026-05-19}` | OK — BABA 139C Jun18 vol/OI 202 |

## Tool errors

- `options_flow_unusual_volume(symbol=BABA, date=2026-05-20)` →
  `Error: no parquet file for 2026-05-20 in /Users/ewan/Documents/Stocks/All Options`.
  **Resolution:** fall back to 2026-05-19 (latest available). All downstream phases
  will pass `date=2026-05-19` to every UW tool.

## Prior versions

None (v1 run).

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake only).
- **Conviction:** N/A.
- **Three things later phases should remember:**
  1. Data carry-back: every UW call uses `date=2026-05-19`, not `2026-05-20`.
  2. BABA already shows new-money upside positioning in mid-DTE OTM calls
     (139C Jun18, vol/OI 202) — phase 1 must investigate whether this is
     isolated or part of a broader pattern.
  3. Output dir is `research/BABA/2026-05-20/` regardless of data carry-back.
- **Open questions:** Is the 139C buy a one-off or the tip of a larger sweep
  cluster? (→ phase 1.)
