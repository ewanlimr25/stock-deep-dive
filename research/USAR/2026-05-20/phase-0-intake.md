# Phase 0 — Intake

**Ticker:** USAR
**As-of date:** 2026-05-20
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/USAR/2026-05-20
**Version:** v1
**Generated:** 2026-05-20T09:30:00-04:00

## Summary

Ticker USAR validated as a US-listed equity with active listed options. Output
directory created clean (no prior phases). UW MCP reachable; latest available
EOD data is 2026-05-19, which will be passed as `date=2026-05-19` to all
downstream UW tool calls (the requested as-of of 2026-05-20 is itself today,
so live EOD data does not yet exist for that session). Proceeding to phase 1.

## Key signals

- UW MCP `historical_available_dates` returned 28 dates across all data
  channels (darkpool, hotchains, oi, options, screener) with the most recent
  being **2026-05-19**. [META:availability]
- USAR options pulse confirmed via `options_flow_unusual_volume`:
  **2026-07-17 $19 call** with **221 contracts traded vs OI=3 (vol/OI =
  73.7x)**, total premium **$80,046**, average IV **0.99**. New position
  opening, not closing. [FLOW:unusual_volume]
- Average IV ~99% on a 2-month dated call is materially elevated — flags USAR
  as a high-vol single-name with binary-style positioning, even at the smoke
  test stage. Phase 5 must check IV percentile / z-score for context.

## UW availability

- `historical_available_dates`: ok
- Latest available options date: 2026-05-19
- Latest available darkpool date: 2026-05-19
- Latest available oi date: 2026-05-19
- Latest available hotchains date: 2026-05-19
- Latest available screener date: 2026-05-19
- Gap observed: 2026-03-27 → 2026-04-27 (one month with no entries — likely
  data ingestion outage rather than market holidays). Downstream historical
  series will see a discontinuity here; phase 5 must flag.

## Ticker sanity

- Options activity (unusual_volume top 1):
  `USAR 2026-07-17 $19 C` — vol 221, OI 3, vol/OI 73.7, premium $80,046,
  avg IV 0.991.
- Source parquet: `bot-eod-report-2026-05-19.parquet`.
- Verdict: options are thinly populated (OI=3 on the unusual contract) but
  there IS activity. Treat USAR as a low-OI / high-conviction-print universe
  — single sweeps will move the needle, and routing-tape noise is amplified.

## Detailed findings

### Run parameters

- The user invoked `/stock-deep-dive USAR --as-of 2026-05-20`.
- 2026-05-20 is today (US/Eastern) per the session context. UW data does not
  yet exist for 2026-05-20, so the effective UW date passed downstream is
  **2026-05-19**. Phase MDs will tag this distinction.
- All UW tool calls in phases 1–7 will pass `date=2026-05-19` where the tool
  exposes a `date` parameter, so reruns of this directory are reproducible.

### Versioning

- Directory was empty at start of run. This is **v1**.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__historical_available_dates` | `{}` | 28 dates per channel; latest 2026-05-19; gap 03-27→04-27 |
| `mcp__uw-pp__options_flow_unusual_volume` | `{symbol: USAR, top-n: 1, date: 2026-05-19}` | 7/17 $19C, vol/OI 73.7x, $80k premium, IV 0.99 |

## Tool errors

None.

## Prior versions

None (v1).

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake only — no directional signal yet,
  but the lone unusual print is bullish-coded).
- **Conviction:** 1/5 (insufficient data).
- **Three things later phases should remember:**
  1. USAR is low-OI: a single contract's vol/OI ratio is meaningful but raw
     contract counts will be small. Premium $-weighting will be more
     informative than contract counts.
  2. Effective UW data date is **2026-05-19**, not 2026-05-20. Cite this
     when downstream phases mention "today".
  3. Historical series has a one-month ingestion gap (03-27 → 04-27). Phase 5
     must avoid drawing trend conclusions across that gap.
- **Open questions:**
  - What does USAR actually do? Sector, market cap, recent catalysts?
    (Phase 6 macro and phase 8 fundamental sub-agent should establish.)
  - Is there an upcoming earnings date that explains the 7/17 expiry being
    targeted? (Phase 1 expiry heatmap + phase 7 earnings_play will check.)
