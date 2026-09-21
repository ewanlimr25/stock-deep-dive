# Phase 0 — Intake

**Ticker:** BL
**As-of date:** 2026-05-19 (user requested 2026-05-20; pivoted — see below)
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/BL/2026-05-19
**Version:** v1
**Generated:** 2026-05-19T00:00:00Z

## Summary

Ticker BL (BlackLine, Inc. — accounting/finance SaaS, US-listed equity)
validated. User requested as-of `2026-05-20` but UW data pipeline has no
parquet for that date; latest available across all data types is `2026-05-19`,
which is also today (US/Eastern) per session context. As-of date pivoted to
`2026-05-19`; output directory adjusted accordingly. UW MCP reachable across
all five data streams (darkpool / hotchains / oi / options / screener).
Initial unusual-volume probe returned **zero contracts** for BL on 2026-05-19
— BL has a thin single-name options market, which is itself a finding to carry
forward (sweeps/flow-driven phases will likely be sparse; the deep dive will
have to lean harder on dark pool, OI, structure, and historical/macro context).
Proceeding to phase 1.

## UW availability

- `historical_available_dates`: **ok**
- Latest available **options** date: `2026-05-19`
- Latest available **darkpool** date: `2026-05-19`
- Latest available **oi** date: `2026-05-19`
- Latest available **hotchains** date: `2026-05-19`
- Latest available **screener** date: `2026-05-19`
- Gap pattern observed: continuous trading days `2026-04-27 → 2026-05-19`,
  then a discontinuity (no `2026-03-30 → 2026-04-24` block). Acceptable —
  recent two weeks are fully populated, sufficient for trend math.

## Ticker sanity

- `options_flow_unusual_volume(symbol=BL, top_n=1, date=2026-05-19)` →
  `{"results": []}` (source parquet:
  `bot-eod-report-2026-05-19.parquet` — file exists, BL absent from results).
- **Interpretation:** BL did not generate any contracts on 2026-05-19 with
  volume ≥ 100 AND vol/OI ≥ 5. Either the ticker traded but no contract
  cleared the threshold, OR BL has near-zero retail/options participation.
  Both are consistent with BL's profile (~$3-5B market cap accounting SaaS,
  light options coverage).
- **Decision:** do NOT abort. Note "thin options activity" as a structural
  constraint, push harder on dark pool + OI + historical in later phases,
  and flag in phase 9 that pure options-driven structures may not be liquid
  enough to express the thesis.

## As-of pivot detail

| Field | User-supplied | Effective | Reason |
|-------|---------------|-----------|--------|
| as-of date | `2026-05-20` | `2026-05-19` | No parquet for 2026-05-20 yet; that date is in the future relative to today (2026-05-19). Latest available = 2026-05-19. |
| output dir | `research/BL/2026-05-20/` | `research/BL/2026-05-19/` | Convention: dir matches the effective data date so re-runs are reproducible. |

All downstream phases will pass `date=2026-05-19` (or omit when "latest" is
appropriate). Multi-day historical lookbacks will end at 2026-05-19.

## Prior versions

None — v1.

## Tool errors

| Tool | Args | Error |
|------|------|-------|
| `mcp__uw-pp__options_flow_unusual_volume` | `{symbol: BL, top-n: 1, date: 2026-05-20}` | `Error: no parquet file for 2026-05-20 in /Users/ewan/Documents/Stocks/All Options` |

Resolution: re-ran with `date=2026-05-19` → success (empty result set, see
Ticker sanity above). No further intake errors.

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake only)
- **Conviction:** n/a
- **Three things later phases should remember:**
  1. Effective as-of date is **2026-05-19**, not the user-requested 2026-05-20.
     Every UW call must use this.
  2. BL is **thin in single-name options** — empty unusual-volume on intake.
     Phase 1 needs to relax thresholds (lower `min-volume`, lower
     `min-vol-oi-ratio`) and Phase 9 must consider equity-only / pair / very
     small options structures.
  3. Recent UW data window is **2026-04-27 → 2026-05-19** (continuous), with a
     gap before that. Lookback math in phase 5 should prefer the
     `historical_*` tools' own internal windows rather than naïve calendar
     spans.
- **Open questions:**
  - Did BL trade at all on 2026-05-19, or is the equity itself in some
    corporate-action / halt state? (Resolve in phase 1 via screener and in
    phase 2 via darkpool ticker summary.)
  - Is there an upcoming earnings catalyst? (Resolve in phase 5 / phase 7.)
