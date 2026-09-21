# Phase 0 — Intake

**Ticker:** MSTR
**As-of date (requested):** 2026-05-20
**As-of date (effective for data):** 2026-05-19  *(latest available UW snapshot — see "As-of pivot" below)*
**Output dir:** `/Users/ewan/Development/stock-deep-dive/research/MSTR/2026-05-20/`
**Version:** v1
**Generated:** 2026-05-20T00:00:00Z

## Summary

MSTR (MicroStrategy / Strategy Inc.) validated as a US-listed equity with deep,
active options activity. The UW MCP is reachable for every dataset (options,
hotchains, OI, darkpool, screener) and the latest available trading session is
2026-05-19 — one session prior to the requested 2026-05-20 as-of. All downstream
phases will pass `date=2026-05-19` to UW tools and label findings as `T-1`
relative to the requested as-of. The intake smoke test returned a high-conviction
unusual-volume hit on the June 192.5C strike (vol/OI = 108), confirming live,
non-thin options activity. Proceeding to Phase 1.

## UW availability

- `historical_available_dates`: ok
- Latest available options date: **2026-05-19**
- Latest available darkpool date: **2026-05-19**
- Latest available OI date: **2026-05-19**
- Latest available hotchains date: **2026-05-19**
- Latest available screener date: **2026-05-19**
- Coverage gap noted: there is a data gap between **2026-03-27** and
  **2026-04-27** in *all* datasets. Historical phases should reference this
  gap when interpreting trend windows that straddle it.

## Ticker sanity

- Options activity (unusual_volume top 1, date=2026-05-19):
  - Contract: `MSTR 2026-06-18 192.5 Call`
  - Total volume: 324, Open interest: 3, **vol/OI = 108**
  - Total premium: $155,086, Avg IV: 71.87%, Trade count: 15
- Interpretation: Deep options market; new positions clearly opening. Implied
  vol in the ~70%s on a near-the-money June call is consistent with MSTR's
  historically elevated IV regime tied to BTC reflexivity.

## As-of pivot

The user requested as-of `2026-05-20`. The UW MCP's latest EOD parquet at the
time of execution is `bot-eod-report-2026-05-19.parquet` (today's EOD has not
yet been ingested at 2026-05-20T00:00:00Z). To stay within the skill's
"no live data when an as-of date is given" rule and to avoid mixing today's
in-progress tape with closed-session UW analytics, **all downstream phases use
`date=2026-05-19`** and treat findings as the most recent closed session prior
to the requested as-of. The output directory keeps the requested date
(`2026-05-20`) so the artifact filename matches the user's invocation.

## Prior versions

None — this is v1.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__historical_available_dates` | `{}` | 28 dates available per dataset, latest 2026-05-19 |
| `mcp__uw-pp__options_flow_unusual_volume` | `{symbol: MSTR, top-n: 1, date: 2026-05-20}` | Error: no parquet for 2026-05-20 |
| `mcp__uw-pp__options_flow_unusual_volume` | `{symbol: MSTR, top-n: 1, date: 2026-05-19, json: true}` | 1 hit: MSTR 2026-06-18 192.5C, vol/OI 108 |

## Tool errors

- `mcp__uw-pp__options_flow_unusual_volume` with `date=2026-05-20` →
  `Error: no parquet file for 2026-05-20 in /Users/ewan/Documents/Stocks/All Options`
  *(Resolved by pivoting to 2026-05-19.)*

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake only).
- **Conviction:** 5/5 on data availability and ticker validity.
- **Three things later phases should remember:**
  1. Use `date=2026-05-19` for every UW call.
  2. There is a structural data gap **2026-03-27 → 2026-04-27** — do not
     interpret missing data in that window as a flow vacuum.
  3. MSTR options carry a 70%+ IV baseline; treat absolute IV levels in
     context of this regime, not against an SPX-style benchmark.
- **Open questions:** None at this phase.
