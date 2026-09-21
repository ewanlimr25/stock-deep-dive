# Phase 0 — Intake

**Ticker:** FSLR
**As-of date:** 2026-05-18
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/FSLR/2026-05-18
**Version:** v1
**Generated:** 2026-05-18T00:00:00Z

## Summary

FSLR (First Solar) intake validated. As-of date 2026-05-18 is a Monday; the
most recent UW data is dated 2026-05-15 (the prior Friday). All UW MCP
endpoints (darkpool, hotchains, oi, options, screener) report 2026-05-15 as
their latest available date, so every downstream phase will request
`date=2026-05-15` and frame all narrative against that anchor while still
labelling the run as the 2026-05-18 deep dive. UW MCP is reachable and FSLR
has live options activity (Mar-2027 280C with vol/OI = 10x). Proceeding to
phase 1.

## UW availability

- `historical_available_dates`: ok
- Latest available options date: 2026-05-15
- Latest available darkpool date: 2026-05-15
- Latest available OI date: 2026-05-15
- Latest available hotchains date: 2026-05-15
- Latest available screener date: 2026-05-15

## Ticker sanity

- Options activity (unusual_volume top 1, date=2026-05-15):
  FSLR 2027-03-19 280C, vol/OI = 10, total premium $1.668M, avg IV 57.4%.
  Confirms FSLR has institutional-scale options activity; longer-dated calls
  are being opened.

## Data-date convention for downstream phases

All UW tool calls from phase 1 onward MUST pass `date=2026-05-15` (the latest
available data prior to the requested as-of date 2026-05-18). The cover sheet
of each downstream phase will note: *"As-of=2026-05-18, data anchor=2026-05-15
(prior session)"*.

## Prior versions

None — first run for FSLR on 2026-05-18.

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake only)
- **Conviction:** n/a
- **Three things later phases should remember:**
  1. Use `date=2026-05-15` for all UW tool calls (2026-05-18 is Monday; weekend).
  2. FSLR has live long-dated call activity — flag any further LEAPs in flow.
  3. Output dir is `research/FSLR/2026-05-18/`; never overwrite phase files.
- **Open questions:** What is current spot, IV rank, and macro regime?
  (Resolved in phases 1, 4, 6.)
